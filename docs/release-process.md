# Release Process

## Development

Make and test changes on hardware.

Commit small, understandable changes:

```text
git add .
git commit -m "Describe the change"
git push
```

## Releases

Use semantic-style version tags:

- `v0.2.0` — current prototype milestone
- `v0.2.1` — bug-fix release
- `v0.3.0` — feature release
- `v1.0.0` — first stable release

A GitHub Release should contain:

- release title
- concise release notes
- known limitations
- a downloadable firmware/package when appropriate

Never overwrite an existing release artifact. Create a new version instead.
