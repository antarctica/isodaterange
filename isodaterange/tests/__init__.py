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
        self.assertRaises(
            NotImplementedError,
            lambda: isodaterange.get_date_range(duration)
        )
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
    # def test_range_datetime_partial(self):
    #     self._test_date("2012-10-24T20:00:00/21:30:00",
    #         (datetime.datetime(2012, 10, 24, 20, 0, 0), datetime.datetime(2012, 10, 24, 21, 30, 0))
    #     )
    def test_range_to_infinity(self):
        self._test_date("2012-10-24/..",
            (datetime.datetime(2012, 10, 24, 0, 0, 0), None)
        )
    def test_range_from_infinity(self):
        self._test_date("../2012-10-24",
            (None, datetime.datetime(2012, 10, 24, 23, 59, 59))
        )
    def test_duration_year(self):
        self._test_duration("P1Y")
    def test_duration_month(self):
        self._test_duration("P2M")
    def test_duration_day(self):
        self._test_duration("P3D")
    def test_duration_week(self):
        self._test_duration("P1W")
    def test_duration_date_mixed(self):
        self._test_duration("P3Y6M4D")
    def test_duration_hour(self):
        self._test_duration("PT1H")
    def test_duration_minute(self):
        self._test_duration("PT5M")
    def test_duration_hour(self):
        self._test_duration("PT72S")
    def test_duration_time_mixed(self):
        self._test_duration("PT12H30M5S")
    def test_duration_mixed(self):
        self._test_duration("P1Y2M10DT2H30M")
