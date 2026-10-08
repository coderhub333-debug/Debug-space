## 2024-05-18 - Newsletter Form Accessibility
**Learning:** Found a common anti-pattern where a newsletter subscription used a `div` and raw `input` rather than a `<form>` tag. This prevents native form submission via the "Enter" key and fails to provide programmatic context to screen readers.
**Action:** Replaced the `div` wrapper with a `<form>`, added a visually hidden `<label>`, `type="submit"` to the button, `aria-live` for error states, and added explicit `focus-visible` ring indicators. Next time, always look for interactive inputs that aren't wrapped in `<form>` tags.

## 2024-05-18 - Image Accessibility attributes
**Learning:** Discovered an issue where `data-alt` was being used on `<img>` elements instead of the standard `alt` attribute. Screen readers depend on the `alt` attribute to provide descriptions of images to visually impaired users. Using `data-alt` hides this vital information from assistive technologies.
**Action:** Replaced all `data-alt` attributes with standard `alt` attributes. In the future, ensure standard HTML attributes like `alt` are used for accessibility instead of custom data attributes.
