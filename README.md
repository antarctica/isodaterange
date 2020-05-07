# README

This project contains a library which converts an ISO date/time string into a range.

## Usage

The module contains one function - `get_date_range` - which converts a given ISO
date/time string into a range and returns this range as a list. It is used as
follows:

```python
import isodaterange

range = isodaterange.get_date_range("2019-07")
# returns [datetime.datetime(2019, 7, 1, 0, 0, 0), datetime.datetime(2019, 7, 31, 23, 59, 59)]

range = isodaterange.get_date_range("2019-04-01/2019-06-23")
# returns [datetime.datetime(2019, 4, 1, 0, 0, 0), datetime.datetime(2019, 6, 23, 23, 59, 59)]

range = isodaterange.get_date_range("P1Y")
# returns [now, date one year from now]
```

## Testing

There is a `tests` module which contains unit tests. This can be run as follows:

```
python3 -m unittest isodaterange.tests
```

## License

(c) UK Research and Innovation (UKRI), 2019 - 2020, British Antarctic Survey.
You may use and re-use this software and associated documentation files free of charge in any format or medium, under
the terms of the Open Government Licence v3.0.
You may obtain a copy of the Open Government Licence at http://www.nationalarchives.gov.uk/doc/open-government-licence/
