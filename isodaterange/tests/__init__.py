################################################################################
# tests/dates.py
#
# Unit tests for MMP API
#
# TDBA 2019-11-15:
#   * First version
################################################################################
# CONFIGURATION
################################################################################
import datetime, unittest
import isodaterange
################################################################################
# TESTS
################################################################################
class DateTests(unittest.TestCase):
    def _test_date(self, date, range):
        test_range = isodaterange.get_date_range(date)
        self.assertEqual(test_range[0], range[0])
        self.assertEqual(test_range[1], range[1])
    def _test_duration(self, duration, range=None):
        now = datetime.datetime.now().replace(microsecond=0)
        new_range = {}
        for x in ["year", "month"]:
            if x in range:
                new_range[x] = getattr(now, x) + range[x]
        test_date = now.replace(**new_range)
        for x in ["day", "hour", "minute", "second"]:
            if x in range:
                attr = "{}s".format(x)
                test_date += datetime.timedelta(**{ attr: range[x] })
        test_range = isodaterange.get_date_range(duration)
        self.assertEqual(test_range[0], min([now, test_date]))
        self.assertEqual(test_range[1], max([now, test_date]))
    def test_range_year(self):
        self._test_date("2019",
            (datetime.datetime(2019, 1, 1, 0, 0, 0), datetime.datetime(2019, 12, 31, 23, 59, 59))
        )
    def test_range_year_month(self):
        self._test_date("2019-07",
            (datetime.datetime(2019, 7, 1, 0, 0, 0), datetime.datetime(2019, 7, 31, 23, 59, 59))
        )
    def test_range_date(self):
        self._test_date("2019-03-12",
            (datetime.datetime(2019, 3, 12, 0, 0, 0), datetime.datetime(2019, 3, 12, 23, 59, 59))
        )
    def test_range_datetime_hour(self):
        self._test_date("2016-04-18T12:00:00",
            (datetime.datetime(2016, 4, 18, 12, 0, 0), datetime.datetime(2016, 4, 18, 12, 0, 0))
        )
    def test_range_datetime_hr_min(self):
        self._test_date("2017-11-25T07:32:00",
            (datetime.datetime(2017, 11, 25, 7, 32, 0), datetime.datetime(2017, 11, 25, 7, 32, 0))
        )
    def test_range_datetime_hr_min_sec(self):
        self._test_date("2018-02-14T12:34:56",
            (datetime.datetime(2018, 2, 14, 12, 34, 56), datetime.datetime(2018, 2, 14, 12, 34, 56))
        )
    def test_range_year(self):
        self._test_date("2019/2020",
            (datetime.datetime(2019, 1, 1, 0, 0, 0), datetime.datetime(2020, 12, 31, 23, 59, 59))
        )
    def test_range_year_month(self):
        self._test_date("2019-07/2019-09",
            (datetime.datetime(2019, 7, 1, 0, 0, 0), datetime.datetime(2019, 9, 30, 23, 59, 59))
        )
    def test_range_date(self):
        self._test_date("2019-03-12/2019-04-25",
            (datetime.datetime(2019, 3, 12, 0, 0, 0), datetime.datetime(2019, 4, 25, 23, 59, 59))
        )
    def test_range_datetime_time(self):
        self._test_date("2016-04-18T12:00:00/2016-04-25T07:22:47",
            (datetime.datetime(2016, 4, 18, 12, 0, 0), datetime.datetime(2016, 4, 25, 7, 22, 47))
        )
    def test_range_datetime_december(self):
        self._test_date("2019-12",
            (datetime.datetime(2019, 12, 1, 0, 0, 0), datetime.datetime(2019, 12, 31, 23, 59, 59))
        )
    def test_range_to_infinity(self):
        self._test_date("2012-10-24/..",
            (datetime.datetime(2012, 10, 24, 0, 0, 0), None)
        )
    def test_range_from_infinity(self):
        self._test_date("../2012-10-24",
            (None, datetime.datetime(2012, 10, 24, 23, 59, 59))
        )
    def test_range_malformed(self):
        self.assertRaises(
            ValueError,
            lambda: isodaterange.get_date_range("fake-date")
        )
    def test_duration_year(self):
        self._test_duration("P1Y", { "year": 1 })
    def test_duration_month(self):
        self._test_duration("P2M", { "month": 2 })
    def test_duration_day(self):
        self._test_duration("P3D", { "day": 3 })
    def test_duration_week(self):
        self._test_duration("P1W", { "day": 7 })
    def test_duration_date_mixed(self):
        self._test_duration("P3Y6M4D", { "year": 3, "month": 6, "day": 4 })
    def test_duration_hour(self):
        self._test_duration("PT1H", { "hour": 1 })
    def test_duration_minute(self):
        self._test_duration("PT5M", { "minute": 5 })
    def test_duration_hour(self):
        self._test_duration("PT72S", { "second": 72 })
    def test_duration_time_mixed(self):
        self._test_duration("PT12H30M5S", { "hour": 12, "minute": 30, "second": 5})
    def test_duration_mixed(self):
        self._test_duration("P1Y2M10DT2H30M", { "year": 1, "month": 2, "day": 10, "hour": 2, "minute": 30})
    def test_duration_negative(self):
        self._test_duration("-P1Y", { "year": -1 })
    def test_duration_malformed(self):
        self.assertRaises(
            ValueError,
            lambda: isodaterange.get_date_range("Pfake-duration")
        )
