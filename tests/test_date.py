import re
from datetime import datetime

from pynYNAB.schema import date_from_api

strdate0 = '2015-04-03'
date0 = datetime.strptime(strdate0, '%Y-%m-%d').date()
datestrings = [strdate0+'T00:00:00',strdate0,'random+'+strdate0]


def test_dates():
    # Test some other functionality here

    for s in datestrings:
        test_name = 'test_datefromapi_%s' % re.sub('[^a-zA-Z0-9]+', '', s)
        assert date_from_api(None, s) == date0
