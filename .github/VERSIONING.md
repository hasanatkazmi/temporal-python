# Automatic Versioning System

This repository uses an automated versioning system that follows [Semantic Versioning (SemVer)](https://semver.org/) principles.

## How It Works

### Automatic Version Bumping

Every merge to the `main` branch automatically triggers a **patch version bump** (e.g., `1.0.0` → `1.0.1`) unless otherwise specified.

### Version Bump Types

- **PATCH** (`1.0.0` → `1.0.1`): Bug fixes, small improvements, documentation updates
- **MINOR** (`1.0.0` → `1.1.0`): New features, non-breaking changes
- **MAJOR** (`1.0.0` → `2.0.0`): Breaking changes, major updates

## Controlling Version Bumps

### Method 1: Pull Request Labels

Add one of these labels to your PR:

- 🔴 `version:major` - Triggers major version bump (breaking changes)
- 🟡 `version:minor` - Triggers minor version bump (new features)  
- 🔵 `version:patch` - Triggers patch version bump (bug fixes) - **DEFAULT**
- ⚪ `no-version-bump` - Skips automatic versioning

### Method 2: Commit Messages

Include specific keywords in your commit messages:

#### Major Version Bump
```
BREAKING CHANGE: Remove deprecated API
major version: Update core architecture
breaking: Change function signatures
```

#### Minor Version Bump
```
feat: Add new PlainYearMonth class
feature: Implement duration rounding
minor version: Add new methods
```

#### Patch Version Bump (Default)
```
fix: Resolve timezone calculation bug
bugfix: Handle edge case in parsing
patch version: Small improvements
```

#### Skip Version Bump
```
[skip version] Update documentation
[no version] Fix typos in README
skip version bump
no version bump
```

### Method 3: Manual Version Bump

Use the GitHub Actions workflow dispatch:

1. Go to **Actions** → **Version Bump**
2. Click **Run workflow**
3. Select version bump type (patch/minor/major)
4. Optionally skip CI checks

## What Happens During Version Bump

1. **Version Detection**: Analyzes commit messages and PR labels
2. **Version Calculation**: Determines new version number
3. **File Updates**: Updates `pyproject.toml` and `temporal/__init__.py`
4. **Changelog Update**: Adds entry to `CHANGELOG.md`
5. **Testing**: Runs quick tests to ensure functionality
6. **Git Operations**: Commits changes and creates git tag
7. **Release Creation**: Creates GitHub release
8. **PyPI Publishing**: Automatically publishes to PyPI (on tags)

## Examples

### Example 1: Bug Fix (Patch)
```bash
git commit -m "fix: Handle invalid timezone input properly"
# Result: 1.0.0 → 1.0.1
```

### Example 2: New Feature (Minor)
```bash
git commit -m "feat: Add PlainYearMonth.until() method"
# Result: 1.0.0 → 1.1.0
```

### Example 3: Breaking Change (Major)
```bash
git commit -m "BREAKING CHANGE: Remove deprecated Calendar.from_id() method"
# Result: 1.0.0 → 2.0.0
```

### Example 4: Documentation Only (No Bump)
```bash
git commit -m "[skip version] Update README examples"
# Result: No version change
```

### Example 5: Using PR Labels
Create a PR with the `version:minor` label:
```bash
git commit -m "Add new comparison methods to all classes"
# Result: 1.0.0 → 1.1.0 (due to PR label)
```

## Version Bump Priority

The system follows this priority order:

1. **PR Labels** (highest priority)
2. **Commit Message Keywords**
3. **Default Patch Bump** (lowest priority)

## Skipping Version Bumps

Version bumps are automatically skipped for:

- Commits that only change documentation files
- Commits that only change GitHub workflow files
- Commits with `[skip version]` or similar in the message
- PRs with the `no-version-bump` label
- Version bump commits themselves (prevents recursion)

## Release Process

1. **Tag Creation**: `v1.2.3` tags are automatically created
2. **GitHub Release**: Automatic release with changelog
3. **PyPI Publishing**: Packages are built and published to PyPI
4. **Notifications**: Team members can be notified of releases

## Best Practices

### For Contributors

- **Use descriptive commit messages** that clearly indicate the type of change
- **Add appropriate PR labels** when the commit message isn't clear
- **Use conventional commits** format when possible:
  - `fix:` for bug fixes
  - `feat:` for new features
  - `docs:` for documentation
  - `refactor:` for code refactoring

### For Maintainers

- **Review PR labels** before merging
- **Use manual version bump** for coordinated releases
- **Monitor automatic releases** to ensure they're working correctly
- **Update this documentation** when changing the versioning system

## Troubleshooting

### Version Bump Didn't Trigger
- Check if commit matches skip patterns
- Verify PR doesn't have `no-version-bump` label
- Check GitHub Actions logs for errors

### Wrong Version Type
- PR labels override commit messages
- Commit message keywords are case-insensitive
- Manual workflow dispatch can fix incorrect bumps

### Failed Release
- Check PyPI credentials and permissions
- Verify all tests pass before version bump
- Review GitHub Actions workflow logs

## Configuration Files

- **Auto Version**: `.github/workflows/auto-version.yml`
- **Manual Version**: `.github/workflows/version-bump.yml`
- **Release Workflow**: `.github/workflows/release.yml`
- **Labels Config**: `.github/labels.yml`