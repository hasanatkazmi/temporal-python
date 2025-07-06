"""
Example usage of the Python Temporal API.
"""

from temporal import Calendar, Duration, Instant, PlainDate, PlainDateTime, PlainTime, TimeZone, ZonedDateTime


def demonstrate_basic_types() -> None:
    """Demonstrate PlainDate, PlainTime, and PlainDateTime."""
    # 1. Working with PlainDate
    print("1. PlainDate Examples:")
    date = PlainDate(2023, 6, 15)
    print(f"   Date: {date}")
    print(f"   Year: {date.year}, Month: {date.month}, Day: {date.day}")
    print(f"   Day of week: {date.day_of_week} (1=Monday, 7=Sunday)")
    print(f"   Day of year: {date.day_of_year}")

    # Date arithmetic
    future_date = date.add(Duration(days=7))
    print(f"   Date + 7 days: {future_date}")

    past_date = date.subtract(Duration(days=14))
    print(f"   Date - 14 days: {past_date}")

    # Date from string
    parsed_date = PlainDate.from_string("2023-12-25")
    print(f"   Parsed date: {parsed_date}")
    print()

    # 2. Working with PlainTime
    print("2. PlainTime Examples:")
    time = PlainTime(14, 30, 45, 123456)
    print(f"   Time: {time}")
    print(f"   Hour: {time.hour}, Minute: {time.minute}")
    print(f"   Second: {time.second}, Microsecond: {time.microsecond}")

    # Time arithmetic
    later_time = time.add(Duration(hours=2, minutes=15))
    print(f"   Time + 2h 15m: {later_time}")

    # Time from string
    parsed_time = PlainTime.from_string("09:15:30.500")
    print(f"   Parsed time: {parsed_time}")
    print()

    # 3. Working with PlainDateTime
    print("3. PlainDateTime Examples:")
    dt = PlainDateTime(2023, 6, 15, 14, 30, 45, 123456)
    print(f"   DateTime: {dt}")

    # Extract components
    date_part = dt.to_plain_date()
    time_part = dt.to_plain_time()
    print(f"   Date part: {date_part}")
    print(f"   Time part: {time_part}")

    # DateTime arithmetic
    future_dt = dt.add(Duration(days=1, hours=3, minutes=30))
    print(f"   DateTime + 1d 3h 30m: {future_dt}")

    # DateTime from string
    parsed_dt = PlainDateTime.from_string("2023-06-15T20:45:30")
    print(f"   Parsed datetime: {parsed_dt}")
    print()


def demonstrate_duration_and_zoned() -> TimeZone:
    """Demonstrate Duration and ZonedDateTime."""
    # 4. Working with Duration
    print("4. Duration Examples:")
    duration1 = Duration(days=1, hours=2, minutes=30, seconds=45)
    print(f"   Duration 1: {duration1}")
    print(f"   Total seconds: {duration1.total_seconds()}")

    duration2 = Duration(hours=1, minutes=15)
    print(f"   Duration 2: {duration2}")

    # Duration arithmetic
    total_duration = duration1.add(duration2)
    print(f"   Duration 1 + Duration 2: {total_duration}")

    diff_duration = duration1.subtract(duration2)
    print(f"   Duration 1 - Duration 2: {diff_duration}")

    # Duration from string
    parsed_duration = Duration.from_string("P1DT2H30M45S")
    print(f"   Parsed duration: {parsed_duration}")
    print()

    # 5. Working with TimeZone and ZonedDateTime
    print("5. ZonedDateTime Examples:")
    utc_tz = TimeZone("UTC")
    zdt = ZonedDateTime(2023, 6, 15, 14, 30, 45, timezone=utc_tz)
    print(f"   ZonedDateTime (UTC): {zdt}")
    print(f"   Offset: {zdt.offset_string}")

    # Convert to different timezone (if available)
    try:
        est_tz = TimeZone("US/Eastern")
        est_zdt = zdt.with_timezone(est_tz)
        print(f"   Same moment in US/Eastern: {est_zdt}")
    except Exception:
        print("   US/Eastern timezone not available")

    # ZonedDateTime arithmetic
    future_zdt = zdt.add(Duration(hours=6))
    print(f"   ZonedDateTime + 6 hours: {future_zdt}")
    print()

    return utc_tz


def demonstrate_instant_and_comparison(utc_tz: TimeZone) -> None:
    """Demonstrate Instant and comparison operations."""
    # 6. Working with Instant
    print("6. Instant Examples:")
    now = Instant.now()
    print(f"   Current instant: {now}")
    print(f"   Epoch seconds: {now.epoch_seconds}")
    print(f"   Epoch milliseconds: {now.epoch_milliseconds}")

    # Create instant from epoch
    epoch_instant = Instant.from_epoch_seconds(1687438245)
    print(f"   Instant from epoch: {epoch_instant}")

    # Instant arithmetic
    future_instant = now.add(Duration(hours=1))
    print(f"   Instant + 1 hour: {future_instant}")

    # Convert instant to zoned datetime
    zdt_from_instant = now.to_zoned_date_time(utc_tz)
    print(f"   Instant as ZonedDateTime: {zdt_from_instant}")
    print()

    # 7. Comparison operations
    print("7. Comparison Examples:")
    date1 = PlainDate(2023, 6, 15)
    date2 = PlainDate(2023, 6, 20)
    print(f"   {date1} < {date2}: {date1 < date2}")
    print(f"   {date1} == {date2}: {date1 == date2}")

    time1 = PlainTime(14, 30, 0)
    time2 = PlainTime(16, 0, 0)
    print(f"   {time1} < {time2}: {time1 < time2}")

    dt1 = PlainDateTime(2023, 6, 15, 14, 30, 0)
    dt2 = PlainDateTime(2023, 6, 15, 16, 0, 0)
    print(f"   {dt1} < {dt2}: {dt1 < dt2}")
    print()


def demonstrate_error_handling() -> None:
    """Demonstrate error handling."""
    print("8. Error Handling Examples:")
    try:
        PlainDate(2023, 13, 45)
    except Exception as e:
        print(f"   Invalid date error: {e}")

    try:
        PlainTime.from_string("25:00:00")
    except Exception as e:
        print(f"   Invalid time string error: {e}")

    try:
        Duration.from_string("invalid")
    except Exception as e:
        print(f"   Invalid duration string error: {e}")
    print()


def demonstrate_advanced_usage() -> None:
    """Demonstrate advanced usage with business day calculations."""
    print("9. Advanced Usage - Business Day Calculation:")

    def add_business_days(start_date: PlainDate, business_days: int) -> PlainDate:
        """Add business days (Monday-Friday) to a date."""
        current_date = start_date
        days_added = 0

        while days_added < business_days:
            current_date = current_date.add(Duration(days=1))
            # Skip weekends (Saturday = 6, Sunday = 7)
            if current_date.day_of_week <= 5:
                days_added += 1

        return current_date

    start_date = PlainDate(2023, 6, 15)  # Thursday
    business_end = add_business_days(start_date, 5)
    print(f"   Start date: {start_date} (day of week: {start_date.day_of_week})")
    print(f"   After 5 business days: {business_end} (day of week: {business_end.day_of_week})")
    print()


def main() -> None:
    """Demonstrate the Python Temporal API functionality."""
    print("=== Python Temporal API Examples ===\n")

    demonstrate_basic_types()
    utc_tz = demonstrate_duration_and_zoned()
    demonstrate_instant_and_comparison(utc_tz)
    demonstrate_error_handling()
    demonstrate_advanced_usage()

    print("=== Examples Complete ===")


if __name__ == "__main__":
    main()
