"""
Tests for Instant class.
"""

import pytest
from temporal import Instant, Duration, TimeZone
from temporal.exceptions import InvalidArgumentError


class TestInstant:
    
    def test_constructor(self):
        """Test Instant constructor."""
        instant = Instant(1687438245.123456)
        assert instant.epoch_seconds == 1687438245.123456
    
    def test_epoch_properties(self):
        """Test epoch time properties."""
        instant = Instant(1687438245.123456)
        assert instant.epoch_milliseconds == 1687438245123.456
        assert instant.epoch_microseconds == 1687438245123456.0
    
    def test_add_duration(self):
        """Test adding duration to instant."""
        instant = Instant(1687438245)
        duration = Duration(hours=1, minutes=30)
        new_instant = instant.add(duration)
        expected = 1687438245 + 3600 + 1800  # 1 hour + 30 minutes in seconds
        assert new_instant.epoch_seconds == expected
    
    def test_add_duration_with_years_months_fails(self):
        """Test that adding years/months to instant fails."""
        instant = Instant(1687438245)
        duration = Duration(years=1)
        with pytest.raises(InvalidArgumentError):
            instant.add(duration)
    
    def test_subtract_duration(self):
        """Test subtracting duration from instant."""
        instant = Instant(1687438245)
        duration = Duration(hours=1)
        new_instant = instant.subtract(duration)
        expected = 1687438245 - 3600
        assert new_instant.epoch_seconds == expected
    
    def test_subtract_instant(self):
        """Test subtracting instant from instant."""
        instant1 = Instant(1687438245)
        instant2 = Instant(1687434645)  # 1 hour earlier
        duration = instant1.subtract(instant2)
        assert duration.hours == 1
    
    def test_comparison(self):
        """Test instant comparison."""
        instant1 = Instant(1687438245)
        instant2 = Instant(1687441845)  # 1 hour later
        instant3 = Instant(1687438245)
        
        assert instant1 < instant2
        assert instant2 > instant1
        assert instant1 == instant3
    
    def test_string_representation(self):
        """Test string representation."""
        instant = Instant(1687438245)
        iso_string = str(instant)
        assert "T" in iso_string
        assert "Z" in iso_string or "+00:00" in iso_string
    
    def test_from_string(self):
        """Test creating instant from string."""
        iso_string = "2023-06-22T14:30:45Z"
        instant = Instant.from_string(iso_string)
        assert isinstance(instant, Instant)
        assert instant.epoch_seconds > 0
    
    def test_now(self):
        """Test now method."""
        now = Instant.now()
        assert isinstance(now, Instant)
        assert now.epoch_seconds > 1687438245  # After 2023
    
    def test_from_epoch_methods(self):
        """Test creating instant from epoch values."""
        epoch_seconds = 1687438245.123
        
        instant1 = Instant.from_epoch_seconds(epoch_seconds)
        assert instant1.epoch_seconds == epoch_seconds
        
        instant2 = Instant.from_epoch_milliseconds(epoch_seconds * 1000)
        assert abs(instant2.epoch_seconds - epoch_seconds) < 0.001
        
        instant3 = Instant.from_epoch_microseconds(epoch_seconds * 1000000)
        assert abs(instant3.epoch_seconds - epoch_seconds) < 0.000001
    
    def test_to_zoned_date_time(self):
        """Test conversion to ZonedDateTime."""
        instant = Instant(1687438245)
        tz = TimeZone("UTC")
        zdt = instant.to_zoned_date_time(tz)
        assert zdt.timezone == tz
        assert zdt.to_instant().epoch_seconds == instant.epoch_seconds
