"""
Tests for PlainDateTime class.
"""

import pytest
from temporal import PlainDateTime, PlainDate, PlainTime, Duration, Calendar
from temporal.exceptions import InvalidArgumentError, RangeError


class TestPlainDateTime:
    
    def test_constructor(self):
        """Test PlainDateTime constructor."""
        dt = PlainDateTime(2023, 6, 15, 14, 30, 45, 123456)
        assert dt.year == 2023
        assert dt.month == 6
        assert dt.day == 15
        assert dt.hour == 14
        assert dt.minute == 30
        assert dt.second == 45
        assert dt.microsecond == 123456
    
    def test_constructor_with_calendar(self):
        """Test PlainDateTime constructor with calendar."""
        calendar = Calendar("iso8601")
        dt = PlainDateTime(2023, 6, 15, 14, 30, 45, calendar=calendar)
        assert dt.calendar == calendar
    
    def test_to_plain_date(self):
        """Test conversion to PlainDate."""
        dt = PlainDateTime(2023, 6, 15, 14, 30, 45)
        date = dt.to_plain_date()
        assert isinstance(date, PlainDate)
        assert date.year == 2023
        assert date.month == 6
        assert date.day == 15
    
    def test_to_plain_time(self):
        """Test conversion to PlainTime."""
        dt = PlainDateTime(2023, 6, 15, 14, 30, 45, 123456)
        time = dt.to_plain_time()
        assert isinstance(time, PlainTime)
        assert time.hour == 14
        assert time.minute == 30
        assert time.second == 45
        assert time.microsecond == 123456
    
    def test_add_duration(self):
        """Test adding duration to datetime."""
        dt = PlainDateTime(2023, 6, 15, 14, 30, 45)
        duration = Duration(days=1, hours=2)
        new_dt = dt.add(duration)
        assert new_dt.day == 16
        assert new_dt.hour == 16
    
    def test_subtract_duration(self):
        """Test subtracting duration from datetime."""
        dt = PlainDateTime(2023, 6, 15, 14, 30, 45)
        duration = Duration(days=1, hours=2)
        new_dt = dt.subtract(duration)
        assert new_dt.day == 14
        assert new_dt.hour == 12
    
    def test_subtract_datetime(self):
        """Test subtracting datetime from datetime."""
        dt1 = PlainDateTime(2023, 6, 16, 14, 30, 45)
        dt2 = PlainDateTime(2023, 6, 15, 12, 15, 30)
        duration = dt1.subtract(dt2)
        assert duration.days == 1
        assert duration.hours == 2
        assert duration.minutes == 15
        assert duration.seconds == 15
    
    def test_with_fields(self):
        """Test with_fields method."""
        dt = PlainDateTime(2023, 6, 15, 14, 30, 45)
        new_dt = dt.with_fields(year=2024, hour=16)
        assert new_dt.year == 2024
        assert new_dt.hour == 16
        assert new_dt.month == 6  # Unchanged
    
    def test_comparison(self):
        """Test datetime comparison."""
        dt1 = PlainDateTime(2023, 6, 15, 14, 30, 45)
        dt2 = PlainDateTime(2023, 6, 15, 16, 0, 0)
        dt3 = PlainDateTime(2023, 6, 15, 14, 30, 45)
        
        assert dt1 < dt2
        assert dt2 > dt1
        assert dt1 == dt3
    
    def test_string_representation(self):
        """Test string representation."""
        dt = PlainDateTime(2023, 6, 15, 14, 30, 45)
        assert str(dt) == "2023-06-15T14:30:45"
        
        dt_with_micro = PlainDateTime(2023, 6, 15, 14, 30, 45, 123456)
        assert str(dt_with_micro) == "2023-06-15T14:30:45.123456"
    
    def test_from_string(self):
        """Test creating datetime from string."""
        dt = PlainDateTime.from_string("2023-06-15T14:30:45")
        assert dt.year == 2023
        assert dt.month == 6
        assert dt.day == 15
        assert dt.hour == 14
        assert dt.minute == 30
        assert dt.second == 45
    
    def test_now(self):
        """Test now method."""
        now = PlainDateTime.now()
        assert isinstance(now, PlainDateTime)
        assert now.year >= 2023
