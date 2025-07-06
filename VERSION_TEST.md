# Testing Trusted Publisher Setup

This commit should trigger the trusted publishing workflow:

1. Auto-version workflow will bump to 1.0.3
2. Create git tag v1.0.3
3. Release workflow will trigger on the tag
4. Build and publish to PyPI using trusted publishing
5. Create GitHub release

## Test Status
- ✅ PyPI trusted publisher configured
- ✅ GitHub environment setup complete
- 🧪 Testing automatic publication...

Let's see the trusted publishing in action!