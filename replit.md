# Python Temporal API

## Overview

This repository implements a Python port of JavaScript's Temporal API, providing modern date and time handling capabilities. The library offers a more intuitive and reliable alternative to Python's standard `datetime` module, with comprehensive temporal objects for working with dates, times, durations, and time zones.

## System Architecture

The project follows a modular Python package architecture with clear separation of concerns:

**Core Architecture:**
- **Package-based structure**: All temporal objects are organized under the `temporal/` package
- **Object-oriented design**: Each temporal concept is implemented as a separate class
- **ISO 8601 compliance**: Built-in support for ISO 8601 parsing and formatting
- **Type safety**: Complete type hint coverage for better development experience

**Key Design Principles:**
- Immutable temporal objects (operations return new instances)
- Comprehensive validation and error handling
- Calendar system abstraction for future extensibility
- Time zone handling using Python's `zoneinfo`

## Key Components

### Core Temporal Objects
1. **PlainDate** (`temporal/plain_date.py`)
   - Represents calendar dates without time information
   - Supports date arithmetic and calendar operations
   - Includes day-of-week and day-of-year calculations

2. **PlainTime** (`temporal/plain_time.py`)
   - Represents time-of-day without date or timezone
   - Handles time arithmetic with overflow normalization
   - Supports microsecond precision

3. **PlainDateTime** (`temporal/plain_date_time.py`)
   - Combines date and time without timezone information
   - Provides conversion methods to PlainDate and PlainTime
   - Supports comprehensive date-time arithmetic

4. **ZonedDateTime** (`temporal/zoned_date_time.py`)
   - Represents date-time with timezone information
   - Integrates with Python's zoneinfo for timezone handling
   - Provides conversion to Instant for UTC operations

### Utility Components
5. **Duration** (`temporal/duration.py`)
   - Represents time spans with multiple units
   - Supports normalization of time components
   - Handles arithmetic operations between temporal objects

6. **Instant** (`temporal/instant.py`)
   - Represents exact points in time (Unix timestamps)
   - Provides epoch time access in various units
   - Supports duration arithmetic (excluding calendar units)

7. **TimeZone** (`temporal/timezone.py`)
   - Wraps Python's zoneinfo for timezone operations
   - Provides timezone validation and comparison
   - Handles timezone offset calculations

8. **Calendar** (`temporal/calendar.py`)
   - Abstracts calendar systems (currently ISO 8601 only)
   - Designed for future calendar system extensibility
   - Provides calendar identification and comparison

### Support Infrastructure
9. **Utilities** (`temporal/utils.py`)
   - ISO 8601 parsing with regex patterns
   - Field validation functions
   - Date/time formatting utilities
   - Calendar calculation helpers

10. **Exceptions** (`temporal/exceptions.py`)
    - Custom exception hierarchy for temporal operations
    - Specific error types for range, type, and argument errors
    - Clear error messaging for debugging

## Data Flow

The system follows a clear data flow pattern:

1. **Input Validation**: All constructors validate input parameters using utility functions
2. **Object Creation**: Temporal objects store validated data as private attributes
3. **Operations**: Arithmetic and comparison operations create new instances
4. **Output Formatting**: Objects provide string representations and conversion methods

**Arithmetic Operations Flow:**
```
Temporal Object + Duration → Validation → Calculation → New Temporal Object
```

**Parsing Flow:**
```
ISO String → Regex Parsing → Validation → Object Construction
```

## External Dependencies

**Runtime Dependencies:**
- **zoneinfo/backports.zoneinfo**: Time zone handling
  - Uses `zoneinfo` for Python 3.9+
  - Falls back to `backports.zoneinfo` for Python < 3.9
  - Provides IANA timezone database access

**Development Dependencies:**
- **pytest**: Testing framework with coverage support
- **black**: Code formatting
- **flake8**: Linting and style checking

**Python Version Support:**
- Primary target: Python 3.11 (Replit environment)
- Compatibility: Python 3.7+ with backports

## Deployment Strategy

**Local Development:**
- Editable installation via `pip install -e .`
- Direct execution of examples with `python example.py`

**Replit Environment:**
- Configured for Python 3.11 with Nix modules
- Parallel workflow execution for testing
- Automatic dependency installation on run

**Package Distribution:**
- Setuptools-based packaging
- PyPI-ready configuration
- Comprehensive metadata and classifiers

**Testing Strategy:**
- Comprehensive unit test coverage
- Property-based testing for edge cases
- Integration testing for temporal operations

## Changelog

```
Changelog:
- June 18, 2025: Complete Python Temporal API implementation
  ✓ All core temporal objects implemented (PlainDate, PlainTime, PlainDateTime, ZonedDateTime, Duration, Instant)
  ✓ Full ISO 8601 parsing and formatting support
  ✓ Comprehensive test suite (75 tests passing)
  ✓ Time zone handling with zoneinfo integration
  ✓ Calendar system abstraction
  ✓ Error handling and validation
  ✓ Working examples and documentation
```

## User Preferences

```
Preferred communication style: Simple, everyday language.
```