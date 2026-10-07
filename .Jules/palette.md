## 2024-05-18 - Newsletter Form Accessibility
**Learning:** Found a common anti-pattern where a newsletter subscription used a `div` and raw `input` rather than a `<form>` tag. This prevents native form submission via the "Enter" key and fails to provide programmatic context to screen readers.
**Action:** Replaced the `div` wrapper with a `<form>`, added a visually hidden `<label>`, `type="submit"` to the button, `aria-live` for error states, and added explicit `focus-visible` ring indicators. Next time, always look for interactive inputs that aren't wrapped in `<form>` tags.
