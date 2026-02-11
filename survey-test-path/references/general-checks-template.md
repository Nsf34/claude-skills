# General Checks Template

This is the standard General Checks section content. Use this as-is unless the survey has unusual requirements that warrant additions or modifications.

## Standard General Checks

- Ensure all questions display correctly with no broken formatting, missing images, or overlapping elements
- Ensure all response options display correctly and completely
- Ensure all skip patterns and routing logic work as programmed
- Ensure all piped text displays the correct variable values (not placeholder text or variable names)
- Ensure all randomization is functioning — response options should appear in different orders across test runs
- Ensure all anchored response options remain in their fixed position (typically bottom) regardless of randomization
- Ensure all "mutually exclusive" response options behave correctly: selecting one deselects all others, and they cannot be selected alongside other options
- Ensure all "Other, please specify" response options open a text input field when selected and close it when deselected
- Ensure all open-ended text fields accept input
- Ensure all required questions prevent the respondent from advancing without providing a response
- Ensure all grid/matrix questions display all rows and columns correctly, with proper headers
- Ensure all scale questions (Likert, numeric, etc.) display the full scale with correct endpoint labels
- Ensure all carousel questions cycle through all assigned items
- Ensure multi-select questions allow multiple selections where specified
- Ensure single-select questions prevent multiple selections where specified
- Ensure the "must select in C1 before selecting in C2" logic works on all grid questions where specified
- Ensure dropdown questions display the full range of options
- Ensure progress indicator advances appropriately through the survey
- Ensure the back button (if enabled) preserves previous selections when navigating backward
- Ensure termination messages display correctly and the survey ends appropriately

## When to Customize

Add items to the General Checks if the survey has:
- **Images or multimedia**: Add checks for image display, alt text, video playback
- **Mobile-specific design**: Add mobile rendering checks
- **Timer-based questions**: Add timer display and enforcement checks
- **Custom UI elements**: Add checks for any non-standard interface components
- **Quota-based routing**: Add notes about quota-dependent behavior
- **External tool integration**: Add checks for segmentation typing tools, MaxDiff exercises, conjoint, etc.

Remove items only if they genuinely don't apply (e.g., remove carousel checks if the survey has no carousel questions).
