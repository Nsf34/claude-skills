| name | description |
|------|-------------|
| social-media-engagement | Automated social media engagement workflow across Instagram, Facebook, and TikTok. Finds relevant accounts, follows/likes them, reacts to posts, and drafts natural comments -- all via browser automation. Supports any brand with swappable brand context files (Table Clay is the default). Instagram: Explore-based discovery, follows, likes, comments. Facebook: Reels-based discovery, Page follows, reactions, comments on relevant Reels only. TikTok: FYP-based discovery, follows, likes, comments on creator videos. Use when user says "run engagement", "Instagram engagement", "Facebook engagement", "TikTok engagement", "social media engagement", "daily engagement run", "find accounts to follow", "run IG session", "run FB session", "run TikTok session", "run TK session", "run engagement on all", "all platforms", or "engagement for [brand name]". Runs in Chrome via browser automation. Does NOT post original content or manage feeds -- only engages with others' content. |

# Social Media Engagement

## Overview

This skill runs engagement sessions on Instagram, Facebook, and/or TikTok. The goal is organic community growth by genuinely engaging with accounts in the brand's niche. Every action should feel like a real person -- a small brand owner -- naturally participating in a community they care about.

The skill is brand-agnostic. Brand context (products, target customers, voice, content themes) is loaded from a swappable reference file. Table Clay is the default.

**Supported platforms:** Instagram, Facebook (Business Page), TikTok
**Session time:** ~8-15 minutes per platform
**Frequency:** Up to 2 sessions per platform per day (morning + evening)

---

## Step 1: Platform Selection

Determine which platform to run based on what the user says:

| User says | Action |
|-----------|--------|
| "Instagram", "IG", "Insta" | Run Instagram workflow |
| "Facebook", "FB" | Run Facebook workflow |
| "TikTok", "TK" | Run TikTok workflow |
| "social media engagement", "run engagement" (no platform specified) | Ask the user which platform |
| "both", "IG and FB", "IG and TK", "FB and TK" | Run the two specified platforms sequentially with a **15-minute gap** |
| "all", "all three", "all platforms" | Run Instagram first, then Facebook, then TikTok, each with a **15-minute gap** |

**Never run multiple platforms simultaneously in one session.** If the user wants more than one, run them sequentially with a gap between each.

---

## Step 2: Load Brand Context

1. Check if the user specified a brand. If they said something like "engagement for Table Clay" or "run FB for [brand]", use that brand.
2. If no brand specified, default to **Table Clay**: read `references/brand-tableclay.md`
3. If a different brand is specified, look for `references/brand-{name}.md`. If the file doesn't exist, ask the user to provide brand details or create the file first.

The brand context file provides:

- Brand name and handles
- Products (so you know what NOT to mention in comments)
- Target customers (shapes what content feels relevant)
- Content themes (what topics to look for in the feed)
- Competitors (used for additional discovery on Instagram)
- Brand voice (used for comment tone)

Keep the brand context in mind throughout the entire session. It shapes what content you engage with and how you write comments.

---

## Step 3: Open the Platform

**Instagram:** Navigate to `https://www.instagram.com/`
**Facebook:** Navigate to `https://www.facebook.com/`
**TikTok:** Navigate to `https://www.tiktok.com/`

**Rules:**

1. Whatever account is signed into the browser is the correct one. Do NOT waste time verifying the handle, Page name, or asking the user to confirm. The browser is the source of truth.
2. If not logged in, ask the user to log in. Never enter credentials yourself.
3. If a CAPTCHA or verification appears, pause and ask the user to complete it.
4. If the platform shows any "suspicious activity" or rate-limiting warning at ANY point during the session, **STOP immediately** and inform the user. Do not attempt to continue.

---

## Step 4: Discover and Engage

Discovery and engagement happen together as one continuous flow. Read the appropriate platform-specific reference file — it contains the complete workflow including discovery method, engagement sequence, pacing, and troubleshooting:

- **Instagram:** Read `references/instagram-workflow.md`
- **Facebook:** Read `references/facebook-workflow.md`
- **TikTok:** Read `references/tiktok-workflow.md`

For writing comments on any platform, read `references/comment-guide.md`.

### Pre-Session: Load Engagement History

**Before engaging**, read the engagement log (`engagement-log.csv`) once and keep it in memory for the session. Do NOT re-read the CSV between individual engagements.

- If an account appears in the log **for the current platform** — skip it
- If an account appears in the log **for a different platform** — don't skip, but add a note in the `notes` column

### Engagement Principles

- **Engage based on content, not account evaluation.** If a post/reel/video feels like it belongs in the brand's world, engage with it directly. No profile visits or follower count checks needed.
- **Only soft-skip** obviously massive accounts (100K+ visible at a glance).
- **Never mention the brand's products** in comments.
- **Never write generic comments** ("Great post!", "Love this!", "Amazing!"). Every comment must reference specific content.
- **Never use hashtags** in comments.
- **Never comment on controversial, negative, or drama content.**
- **Never exceed session limits.**

---

## Browser Interaction Patterns

Social media UIs are dynamic and unpredictable. The platform-specific workflow files contain detailed interaction instructions, but these universal patterns apply across all platforms and should be your defaults.

### Element Targeting

**Always prefer the `find` tool over coordinate-based clicks for interactive elements.** Social media layouts shift between sessions, screen sizes, and A/B tests. The `find` tool locates elements by semantic meaning, which is more resilient than hardcoded coordinates.

- Use `find` queries like "Follow button", "Like button", "comment input", "Next Card button"
- If `find` returns multiple matches, use screenshot context to pick the one associated with the currently visible post/reel
- Fall back to coordinates only when `find` can't locate an element, and take a fresh screenshot first

### Stale References

Element references (`ref_XX`) from `find` or `read_page` go stale when the visible content changes. Re-query with `find` when:

- A new post modal opens (previous post's refs are gone)
- A reel advances to new content
- A popup opens or closes over the content

**Don't re-query** between actions on the same piece of content (e.g., between follow and like on the same post modal). Refs stay valid while the same content is visible.

### Focus Management

After interacting with text inputs (comment boxes, search bars), keyboard-based navigation often breaks because the input retains focus. After typing or submitting a comment:

1. Click outside the input area or press `Escape` to release focus
2. Verify focus is cleared before attempting keyboard navigation
3. If keyboard navigation still doesn't work, use button-based navigation (see platform-specific workflows)

### Fallback: Direct URL Navigation

If feed-based navigation becomes unreliable (cycling through the same content, freezing, or not advancing), navigate directly to a fresh feed URL:

- **Instagram:** `https://www.instagram.com/explore/`
- **Facebook:** `https://www.facebook.com/reel/`
- **TikTok:** `https://www.tiktok.com/foryou`

This forces the platform to load a fresh batch of content. Use this as a reset when you've been stuck for more than 2-3 attempts to advance.

### Popup and Modal Handling

Social platforms frequently show popups (notifications, audio links, login prompts, "turn on notifications" modals). When a popup appears unexpectedly:

1. Look for an X button or "Not Now" / "Close" option using `find`
2. If no close button exists, press `Escape`
3. Take a screenshot to verify the popup is dismissed before continuing
4. Never interact with the content behind a popup -- it will click the wrong thing

### When to Screenshot

Screenshots are useful but expensive. Use them strategically, not on every action.

**Take a screenshot when:**
- First opening the platform to confirm you're on the right page
- Something unexpected happens (wrong content visible, UI looks broken, error messages)
- You need to verify an action worked after troubleshooting an issue
- `find` can't locate an expected element and you need to see why

**Don't screenshot:**
- Before every follow, like, or comment — use `find` to locate elements instead
- Between actions on the same post/reel — if the modal is open, you're still on the same content
- To "confirm" the Explore grid before clicking a post — just click it

---

## Step 5: Session Logging and Summary

After each session, do **two things**:

### A. Show the User a Summary

```
Session Summary -- [Date, Time]
Platform: [Instagram / Facebook / TikTok]
Accounts followed: [count]
Posts liked/reacted to: [count]
Comments posted: [count]
Notable accounts found: [any standout accounts worth revisiting]
Any issues: [rate limiting, CAPTCHAs, errors, or "none"]
```

### B. Append to the Engagement Log

Save session data to `engagement-log.csv` in this skill's directory.

**CSV columns:**

```
date,time,platform,account_id,display_name,follower_count,account_type,content_type,action_taken,comment_text,post_url,notes
```

**Column definitions:**

- `date` -- YYYY-MM-DD (required for every row)
- `time` -- HH:MM (24-hour, required for every row -- never leave blank)
- `platform` -- "instagram", "facebook", or "tiktok"
- `account_id` -- @username (Instagram, TikTok) or Page name/URL slug (Facebook)
- `display_name` -- their profile or Page display name
- `follower_count` -- approximate follower/friend count at time of engagement (use "unknown" if not visible)
- `account_type` -- "profile" (Instagram), "creator" (TikTok), "page" (Facebook Page)
- `content_type` -- what they post (e.g., "pottery", "coffee lifestyle", "DIY crafts", "ceramics")
- `action_taken` -- "follow", "follow+like", "follow+like+comment", "page_follow", "page_follow+react", "page_follow+react+comment"
- `comment_text` -- the exact comment posted (blank if no comment)
- `post_url` -- URL of the post liked/reacted to/commented on
- `notes` -- anything notable (e.g., "great engagement on their posts", "potential collab", "also on IG as @xyz", "very active in pottery groups")

**Logging format rules:**

1. **One row per account per session.** Consolidate all actions taken on one account into a single row using the `action_taken` field (e.g., "follow+like+comment"). Do NOT log each action (follow, like, comment) as separate rows for the same account -- this creates bloat and makes the log harder to read.
2. **Always include the time.** Every row must have an HH:MM timestamp. Use the approximate time the first action was taken on that account.
3. **Keep it consistent across platforms.** The same format applies to Instagram, Facebook, and TikTok -- no platform should use a different row structure.

**Before each session, read this CSV** to check which accounts have already been engaged. This prevents re-following and keeps engagement fresh.

The log also serves as a future resource for re-engagement. Accounts with good notes can be revisited for deeper interaction later.

---

## Safety and Rate Limiting

All platforms actively detect and penalize bot-like behavior. These safeguards are non-negotiable.

### Universal Rules

1. **Never exceed session limits.** Limits are defined in the platform-specific reference files.
2. **Always pace actions.** Timing rules are in the platform-specific reference files.
3. **Vary patterns.** Don't do the same sequence (follow, like, comment) every time. Mix it up.
4. **Stop on any warning.** If the platform shows any blocking message, CAPTCHA, verification, or unusual behavior -- stop immediately and tell the user.
5. **Cool-down after being flagged:**
   - Instagram: Wait at least **4-6 hours**
   - Facebook: Wait at least **6-12 hours** (Facebook penalties escalate more aggressively)
   - TikTok: Wait at least **6-12 hours** (TikTok penalties escalate quickly to temporary bans)
6. **Daily maximums:** No more than **2 sessions per platform per day.**

### Platform-Specific Safety

For detailed stop triggers and safety protocols:

- Instagram: See "Safety and Stop Triggers" in `references/instagram-workflow.md`
- Facebook: See "Safety and Stop Triggers" in `references/facebook-workflow.md`
- TikTok: See "Safety and Stop Triggers" in `references/tiktok-workflow.md`

---

## First-Run Setup

On the very first run of this skill for a platform:

1. Open the platform -- whatever account is signed in is correct
2. Run a **smaller test session** (half the normal limits):
   - Instagram: 7 follows, 7 likes, 2 comments
   - Facebook: 4 Page follows, 6 reactions, 2 comments (all via Reels)
   - TikTok: 5 follows, 6 likes, 2 comments
3. Review the session summary with the user and ask if the engagement style feels right
4. Initialize or verify the `engagement-log.csv` has the correct headers
5. Adjust based on user feedback before running full sessions

This helps catch any issues (wrong account signed in, brand voice mismatch, platform UI changes) before committing to a full session.

---

## Quick Reference: Session Limits

|  | Instagram | Facebook | TikTok |
|---|-----------|----------|--------|
| **Follows** | 15 per session | 8 per session | 10 per session |
| **Likes/Reactions** | 15 per session | 12 per session | 12 per session |
| **Comments** | 5 per session | 4 per session | 4 per session |
| **Sessions/day** | 2 max | 2 max | 2 max |
| **Cool-down if flagged** | 4-6 hours | 6-12 hours | 6-12 hours |
