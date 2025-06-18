"""
Tests for ZonedDateTime class.
"""

import pytest
from temporal import ZonedDateTime, TimeZone, Calendar, Duration
from temporal.exceptions import InvalidArgumentError


class TestZonedDateTime:
    
    def test_constructor(self):
        """Test ZonedDateTime constructor."""
        tz = TimeZone("UTC")
        dt = ZonedDateTime(2023, 6, 15, 14, 30, 45, 123456, tz)
        assert dt.year == 2023
        assert dt.month == 6
        assert dt.day == 15
        assert dt.hour == 14
        assert dt.minute == 30
        assert dt.second == 45
        assert dt.microsecond == 123456
        assert dt.timezone == tz
    
    def test_constructor_requires_timezone(self):
        """Test that constructor requires timezone."""
        with pytest.raises(InvalidArgumentError):
            ZonedDateTime(2023, 6, 15, 14, 30, 45)
    
    def test_offset_string(self):
        """Test offset string representation."""
        utc_tz = TimeZone("UTC")
        dt = ZonedDateTime(2023, 6, 15, 14, 30, 45, timezone=utc_tz)
        assert dt.offset_string == "Z"
    
    def test_to_instant(self):
        """Test conversion to Instant."""
        tz = TimeZone("UTC")
        dt = ZonedDateTime(2023, 6, 15, 14, 30, 45, timezone=tz)
        instant = dt.to_instant()
        assert instant.epoch_seconds > 0
    
    def test_to_plain_date_time(self):
        """Test conversion to PlainDateTime."""
        tz = TimeZone("UTC")
        dt = ZonedDateTime(2023, 6, 15, 14, 30, 45, timezone=tz)
        plain_dt = dt.to_plain_date_time()
        assert plain_dt.year == 2023
        assert plain_dt.hour == 14
    
    def test_with_timezone(self):
        """Test timezone conversion."""
        utc_tz = TimeZone("UTC")
        dt = ZonedDateTime(2023, 6, 15, 14, 30, 45, timezone=utc_tz)
        
        # Convert to different timezone (if available)
        try:
            est_tz = TimeZone("US/Eastern")
            est_dt = dt.with_timezone(est_tz)
            assert est_dt.timezone == est_tz
            # Time should be different but instant should be same
            assert dt.to_instant() == est_dt.to_instant()
        except InvalidArgumentError:
            # Skip if timezone not available
            pass
    
    def test_add_duration(self):
        """Test adding duration to zoned datetime."""
        tz = TimeZone("UTC")
        dt = ZonedDateTime(2023, 6, 15, 14, 30, 45, timezone=tz)
        duration = Duration(hours=2, minutes=30)
        new_dt = dt.add(duration)
        assert new_dt.hour == 17
        assert new_dt.minute == 0
    
    def test_subtract_duration(self):
        """Test subtracting duration from zoned datetime."""
        tz = TimeZone("UTC")
        dt = ZonedDateTime(2023, 6, 15, 14, 30, 45, timezone=tz)
        duration = Duration(hours=1)
        new_dt = dt.subtract(duration)
        assert new_dt.hour == 13
    
    def test_subtract_zoned_datetime(self):
        """Test subtracting zoned datetime from zoned datetime."""
        tz = TimeZone("UTC")
        dt1 = ZonedDateTime(2023, 6, 15, 16, 0, 0, timezone=tz)
        dt2 = ZonedDateTime(2023, 6, 15, 14, 30, 0, timezone=tz)
        duration = dt1.subtract(dt2)
        assert duration.hours == 1
        assert duration.minutes == 30
    
    def test_comparison(self):
        """Test zoned datetime comparison."""
        tz = TimeZone("UTC")
        dt1 = ZonedDateTime(2023, 6, 15, 14, 30, 45, timezone=tz)
        dt2 = ZonedDateTime(2023, 6, 15, 16, 0, 0, timezone=tz)
        dt3 = ZonedDateTime(2023, 6, 15, 14, 30, 45, timezone=tz)
        
        assert dt1 < dt2
        assert dt2 > dt1
        assert dt1 == dt3
    
    def test_string_representation(self):
        """Test string representation."""
        tz = TimeZone("UTC")
        dt = ZonedDateTime(2023, 6, 15, 14, 30, 45, timezone=tz)
        assert "2023-06-15T14:30:45" in str(dt)
        assert "Z" in str(dt) or "+00:00" in str(dt)
    
    def test_now(self):
        """Test now method."""
        tz = TimeZone("UTC")
        now = ZonedDateTime.now(tz)
        assert isinstance(now, ZonedDateTime)
        assert now.timezone == tz
