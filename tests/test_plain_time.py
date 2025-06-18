"""
Tests for PlainTime class.
"""

import pytest
from temporal import PlainTime, Duration
from temporal.exceptions import InvalidArgumentError, RangeError


class TestPlainTime:
    
    def test_constructor(self):
        """Test PlainTime constructor."""
        time = PlainTime(14, 30, 45, 123456)
        assert time.hour == 14
        assert time.minute == 30
        assert time.second == 45
        assert time.microsecond == 123456
    
    def test_constructor_defaults(self):
        """Test PlainTime constructor with defaults."""
        time = PlainTime()
        assert time.hour == 0
        assert time.minute == 0
        assert time.second == 0
        assert time.microsecond == 0
    
    def test_invalid_time(self):
        """Test invalid time values."""
        with pytest.raises(RangeError):
            PlainTime(25, 0, 0)  # Invalid hour
        
        with pytest.raises(RangeError):
            PlainTime(0, 60, 0)  # Invalid minute
        
        with pytest.raises(RangeError):
            PlainTime(0, 0, 60)  # Invalid second
    
    def test_add_duration(self):
        """Test adding duration to time."""
        time = PlainTime(14, 30, 45)
        duration = Duration(hours=2, minutes=15)
        new_time = time.add(duration)
        assert new_time.hour == 16
        assert new_time.minute == 45
    
    def test_add_duration_overflow(self):
        """Test adding duration with overflow."""
        time = PlainTime(22, 30, 0)
        duration = Duration(hours=3)
        new_time = time.add(duration)
        assert new_time.hour == 1  # Wraps around
        assert new_time.minute == 30
    
    def test_subtract_duration(self):
        """Test subtracting duration from time."""
        time = PlainTime(14, 30, 45)
        duration = Duration(hours=1, minutes=15)
        new_time = time.subtract(duration)
        assert new_time.hour == 13
        assert new_time.minute == 15
    
    def test_subtract_time(self):
        """Test subtracting time from time."""
        time1 = PlainTime(14, 30, 45)
        time2 = PlainTime(12, 15, 30)
        duration = time1.subtract(time2)
        assert duration.hours == 2
        assert duration.minutes == 15
        assert duration.seconds == 15
    
    def test_with_fields(self):
        """Test with_fields method."""
        time = PlainTime(14, 30, 45)
        new_time = time.with_fields(hour=16, second=0)
        assert new_time.hour == 16
        assert new_time.minute == 30
        assert new_time.second == 0
    
    def test_comparison(self):
        """Test time comparison."""
        time1 = PlainTime(14, 30, 45)
        time2 = PlainTime(16, 0, 0)
        time3 = PlainTime(14, 30, 45)
        
        assert time1 < time2
        assert time2 > time1
        assert time1 == time3
        assert time1 <= time3
        assert time1 >= time3
    
    def test_string_representation(self):
        """Test string representation."""
        time = PlainTime(14, 30, 45)
        assert str(time) == "14:30:45"
        
        time_with_micro = PlainTime(14, 30, 45, 123456)
        assert str(time_with_micro) == "14:30:45.123456"
    
    def test_from_string(self):
        """Test creating time from string."""
        time = PlainTime.from_string("14:30:45")
        assert time.hour == 14
        assert time.minute == 30
        assert time.second == 45
        
        time_with_micro = PlainTime.from_string("14:30:45.123456")
        assert time_with_micro.microsecond == 123456
