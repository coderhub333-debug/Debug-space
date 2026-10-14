## 2024-03-24 - Accessibility: Use standard `alt` attributes instead of `data-alt`
**Learning:** Found a pattern where image descriptions were using `data-alt` instead of `alt`. Screen readers typically do not announce `data-*` attributes by default, making these images inaccessible to visually impaired users relying on assistive technologies.
**Action:** Always ensure that images intended to convey meaning use the standard `alt` attribute instead of custom data attributes.
## 2024-05-18 - Newsletter Form Accessibility
**Learning:** Found a common anti-pattern where a newsletter subscription used a `div` and raw `input` rather than a `<form>` tag. This prevents native form submission via the "Enter" key and fails to provide programmatic context to screen readers.
**Action:** Replaced the `div` wrapper with a `<form>`, added a visually hidden `<label>`, `type="submit"` to the button, `aria-live` for error states, and added explicit `focus-visible` ring indicators. Next time, always look for interactive inputs that aren't wrapped in `<form>` tags.

## 2024-05-18 - Image Accessibility attributes
**Learning:** Discovered an issue where `data-alt` was being used on `<img>` elements instead of the standard `alt` attribute. Screen readers depend on the `alt` attribute to provide descriptions of images to visually impaired users. Using `data-alt` hides this vital information from assistive technologies.
**Action:** Replaced all `data-alt` attributes with standard `alt` attributes. In the future, ensure standard HTML attributes like `alt` are used for accessibility instead of custom data attributes.

## 2024-05-18 - Skip Links & Unique Interactive Component IDs
**Learning:** Found two distinct issues that hurt accessibility for keyboard and screen reader users:
1. Missing a "Skip to main content" link, forcing users to tab through hidden navigation menus every time the page loads.
2. A language selection dropdown was visually floating but duplicated in the HTML, creating invalid duplicate IDs (`#lang-switcher`) which could cause buggy behavior with JS or confuse screen readers.
**Action:** Added a visually hidden (but focusable) skip link right after the opening body tag. Cleaned up the redundant language switcher and added an `aria-label` to the remaining one. Always verify that interactive components use unique IDs and that a keyboard-accessible skip link exists on every page.

## 2024-10-24 - Stateful Icon-Only Buttons
**Learning:** Icon-only toggle buttons (like a wishlist heart) need multiple cues for state changes. Visually, replacing `transition-colors` with `transition-all active:scale-90` adds a tactile "pop" effect, and dynamically updating the icon fill and color clarifies the active state. Accessibly, toggling `aria-pressed` alone is sometimes less clear than dynamically updating the `aria-label` (e.g., "Save to Wishlist" vs "Remove from Wishlist") in tandem.
**Action:** Always ensure toggleable icons provide tactile feedback, visual state changes (like fill), and dynamic `aria-label` updates for screen readers.

## 2024-10-25 - Filter Pills ARIA & CSS Selection
**Learning:** For horizontal filter pills (tabs), pairing `aria-pressed="true"` (or false) with Tailwind's `aria-[pressed=true]:...` state selectors provides a clean, robust way to handle visual active states. It avoids complex JS class toggling while simultaneously keeping the DOM semantics perfectly aligned for screen readers. Additionally, filtering elements often update the DOM, so adding a visually hidden `aria-live` region (`#filter-status`) is critical to announce the filtered result count to assistive technology.
**Action:** When building interactive filters or custom radio-like groups, drive the visual styling natively through the `aria-pressed` or `aria-selected` attributes using CSS variants instead of redundant utility classes. Always pair dynamic filtering with an `aria-live` status element.
