## 2024-03-24 - Accessibility: Use standard `alt` attributes instead of `data-alt`
**Learning:** Found a pattern where image descriptions were using `data-alt` instead of `alt`. Screen readers typically do not announce `data-*` attributes by default, making these images inaccessible to visually impaired users relying on assistive technologies.
**Action:** Always ensure that images intended to convey meaning use the standard `alt` attribute instead of custom data attributes.
