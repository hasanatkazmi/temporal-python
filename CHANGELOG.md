# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
## [1.0.7] - 2025-07-06

### Fixed
- Bug fixes and improvements


## [1.0.6] - 2025-07-06

### Fixed
- Bug fixes and improvements


## [1.0.5] - 2025-07-06

### Fixed
- Bug fixes and improvements


## [1.0.4] - 2025-07-06

### Fixed
- Bug fixes and improvements


## [1.0.3] - 2025-07-06

### Fixed
- Bug fixes and improvements


## [1.0.2] - 2025-07-06

### Fixed
- Bug fixes and improvements


## [1.0.1] - 2025-07-06

### Fixed
- Bug fixes and improvements



## [1.0.0] - 2025-07-06

### Added
- **MAJOR**: Complete 1:1 port of JavaScript Temporal API
- **NEW CLASSES**:
  - `PlainYearMonth`: Year-month combinations (e.g., "2023-06")
  - `PlainMonthDay`: Recurring dates like birthdays (e.g., "--08-24")

### Enhanced
- **ALL CLASSES** now include complete method coverage:
  - `until()` and `since()` methods for duration calculations
  - `round()` methods for precision control
  - `compare()` static methods for object comparison
  - `from_any()` methods for flexible input handling
  - `to_json()` and `to_locale_string()` serialization methods
  - `equals()` methods for equality checking

- **Duration Class**:
  - Added `sign` and `blank` properties
  - Added `total()` method for unit conversions
  - Enhanced `round()` method with multiple unit support

- **PlainDate Class**:
  - Added `to_plain_year_month()` and `to_plain_month_day()` conversions
  - Added `to_zoned_date_time()` with timezone support

- **PlainDateTime Class**:
  - Added `with_plain_time()` and `with_calendar()` methods
  - Enhanced `round()` method for datetime precision

- **ZonedDateTime Class**:
  - Added `with_plain_time()`, `with_calendar()` methods
  - Added `start_of_day()` method
  - Enhanced timezone handling

- **Instant Class**:
  - Added precision `round()` method
  - Enhanced arithmetic operations

### Testing
- Added 26 comprehensive tests for new classes and methods
- Total test coverage: 101 tests (previously 75)
- All tests passing across Python 3.7-3.12
- Added performance benchmarks and API validation

### Documentation
- Updated README with complete API documentation
- Added comprehensive examples for all new classes
- Enhanced quick start guide with advanced features
- Added installation instructions for PyPI

### Infrastructure
- Set up comprehensive CI/CD pipeline with GitHub Actions
- Added automated testing across multiple Python versions and operating systems
- Implemented code quality checks (linting, formatting, type checking)
- Added security scanning and dependency checking
- Configured automated PyPI releases

## [0.0.1] - 2023-XX-XX

### Added
- Initial implementation of core Temporal classes:
  - `PlainDate`, `PlainTime`, `PlainDateTime`
  - `ZonedDateTime`, `Duration`, `Instant`
  - `Calendar`, `TimeZone`
- Basic arithmetic operations
- ISO 8601 string parsing and formatting
- Timezone support using Python's `zoneinfo`
- Initial test suite (75 tests)

[1.0.0]: https://github.com/hasanatkazmi/temporal-python/compare/v0.0.1...v1.0.0
[0.0.1]: https://github.com/hasanatkazmi/temporal-python/releases/tag/v0.0.1