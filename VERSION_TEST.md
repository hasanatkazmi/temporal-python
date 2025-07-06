# Testing automatic versioning system

This commit should trigger an automatic patch version bump from 1.0.0 to 1.0.1

The versioning system will:
1. Detect this is a regular commit (no special keywords)
2. Apply default patch version bump
3. Update pyproject.toml and __init__.py
4. Update CHANGELOG.md
5. Create a git tag
6. Create a GitHub release
7. Trigger PyPI publishing

Let's see it in action\!
