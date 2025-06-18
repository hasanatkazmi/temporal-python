"""
Tests for Duration class.
"""

import pytest
from temporal import Duration
from temporal.exceptions import InvalidArgumentError


class TestDuration:
    
    def test_constructor(self):
        """Test Duration constructor."""
        duration = Duration(years=1, months=2, days=3, hours=4, minutes=5, seconds=6, microseconds=7)
        assert duration.years == 1
        assert duration.months == 2
        assert duration.days == 3
        assert duration.hours == 4
        assert duration.minutes == 5
        assert duration.seconds == 6
        assert duration.microseconds == 7
    
    def test_constructor_defaults(self):
        """Test Duration constructor with defaults."""
        duration = Duration()
        assert duration.years == 0
        assert duration.months == 0
        assert duration.days == 0
        assert duration.hours == 0
        assert duration.minutes == 0
        assert duration.seconds == 0
        assert duration.microseconds == 0
    
    def test_normalization(self):
        """Test duration normalization."""
        duration = Duration(seconds=3661)  # 1 hour, 1 minute, 1 second
        assert duration.hours == 1
        assert duration.minutes == 1
        assert duration.seconds == 1
    
    def test_total_seconds(self):
        """Test total_seconds calculation."""
        duration = Duration(days=1, hours=1, minutes=1, seconds=1)
        expected = 24 * 3600 + 3600 + 60 + 1
        assert duration.total_seconds() == expected
    
    def test_add(self):
        """Test adding durations."""
        duration1 = Duration(hours=1, minutes=30)
        duration2 = Duration(hours=2, minutes=45)
        result = duration1.add(duration2)
        assert result.hours == 4
        assert result.minutes == 15
    
    def test_subtract(self):
        """Test subtracting durations."""
        duration1 = Duration(hours=3, minutes=45)
        duration2 = Duration(hours=1, minutes=30)
        result = duration1.subtract(duration2)
        assert result.hours == 2
        assert result.minutes == 15
    
    def test_negated(self):
        """Test negating duration."""
        duration = Duration(hours=1, minutes=30)
        negated = duration.negated()
        assert negated.hours == -1
        assert negated.minutes == -30
    
    def test_abs(self):
        """Test absolute value of duration."""
        duration = Duration(hours=-1, minutes=-30)
        abs_duration = duration.abs()
        assert abs_duration.hours == 1
        assert abs_duration.minutes == 30
    
    def test_with_fields(self):
        """Test with_fields method."""
        duration = Duration(hours=1, minutes=30)
        new_duration = duration.with_fields(hours=2, seconds=45)
        assert new_duration.hours == 2
        assert new_duration.minutes == 30
        assert new_duration.seconds == 45
    
    def test_string_representation(self):
        """Test string representation."""
        duration = Duration(days=1, hours=2, minutes=30, seconds=45)
        duration_str = str(duration)
        assert "P1D" in duration_str
        assert "T2H30M45S" in duration_str
    
    def test_zero_duration_string(self):
        """Test zero duration string representation."""
        duration = Duration()
        assert str(duration) == "PT0S"
    
    def test_from_string(self):
        """Test creating duration from string."""
        duration = Duration.from_string("P1DT2H30M45S")
        assert duration.days == 1
        assert duration.hours == 2
        assert duration.minutes == 30
        assert duration.seconds == 45
    
    def test_from_string_fractional_seconds(self):
        """Test creating duration from string with fractional seconds."""
        duration = Duration.from_string("PT1.5S")
        assert duration.seconds == 1
        assert duration.microseconds == 500000
    
    def test_equality(self):
        """Test duration equality."""
        duration1 = Duration(hours=1, minutes=30)
        duration2 = Duration(hours=1, minutes=30)
        duration3 = Duration(hours=2, minutes=0)
        
        assert duration1 == duration2
        assert duration1 != duration3
    
    def test_operators(self):
        """Test duration operators."""
        duration1 = Duration(hours=1)
        duration2 = Duration(minutes=30)
        
        added = duration1 + duration2
        assert added.hours == 1
        assert added.minutes == 30
        
        subtracted = duration1 - duration2
        assert subtracted.hours == 1
        assert subtracted.minutes == -30
        
        negated = -duration1
        assert negated.hours == -1
        
        abs_negated = abs(negated)
        assert abs_negated.hours == 1
