# Facebook Workflow

This reference covers the full Facebook engagement workflow. All actions are performed as a **Business Page** (not a personal profile). Discovery and engagement happen exclusively through **Facebook Reels**.

---

## Discovery: Facebook Reels

### How to Access

1. Navigate to `https://www.facebook.com/reel/` or click the **Reels** icon in the left sidebar / bottom nav
2. Facebook loads a vertical Reels feed with auto-playing short videos
3. Browse through looking for content that matches the brand's audience

### What to Engage With

Engage with Reels that feel like they belong in the brand's world. For Table Clay, that means content like:

- Pottery, ceramics, clay work (throwing, glazing, kiln reveals, handbuilding)
- Coffee culture (pour-overs, latte art, morning routines, cafe visits)
- Cute home finds, aesthetic kitchen/table setups
- DIY and artsy projects (painting, crafting, woodworking, candle making)
- Handmade goods and small business showcases
- Cozy lifestyle and mindful living content

**The bar is vibes, not metrics.** If the content feels like something the brand's audience would enjoy, engage with it.

### What to Skip

- Viral memes, news, celebrity gossip, political content
- Big corporate brand ads
- Beauty tutorials, travel accessories, cooking (unless directly tied to the brand's niche)
- Content with zero connection to the brand's niche
- Accounts you've already engaged with (check the engagement log)

### Niche Assessment

Before engaging with a Reel, take a screenshot and quickly assess:

1. Does this content visually fit the brand's world? (pottery, ceramics, coffee, DIY, cozy lifestyle, handmade, home decor)
2. Is this a personal/small creator or an obvious mega-brand?
3. Is the content positive and safe to engage with?

If the answer to #1 is unclear, lean toward engaging. It's better to cast a slightly wide net than to overthink it. Skip only when the content is clearly outside the niche (beauty tutorials, travel vlogs, gaming, etc.).

### Soft Guideline on Size

Don't waste time checking follower counts. But if it's obviously a massive account (100K+ followers visible at a glance, or a well-known brand), skip it -- they won't notice the engagement. If you can't tell, don't worry about it.

---

## Navigating Between Reels

Facebook Reels navigation is unreliable. Different methods work in different contexts, and the best approach depends on what's happening on screen. Use this priority order:

### Primary Method: "Next Card" Button

1. Use `find` tool with query **"Next Card"** or **"Next card button"**
2. Click the returned reference
3. Wait 1-2 seconds for the next Reel to load
4. Take a screenshot to confirm new content appeared

This is the most reliable method. The "Next Card" button is a persistent navigation element in the Reels player that consistently advances to the next Reel regardless of focus state.

### Secondary Method: ArrowDown Key

1. Click on an empty area of the Reel first (not on any interactive element) to ensure the Reel player has focus
2. Press `ArrowDown`
3. Wait 1-2 seconds
4. Take a screenshot to verify new content loaded

**Known issue:** ArrowDown does NOT work when the comment input or any text field has focus. Always clear focus first (click outside or press `Escape`) before attempting ArrowDown.

### Tertiary Method: Scroll

1. Place cursor in the center of the Reel
2. Scroll down (scroll_amount: 3-5)
3. Wait 1-2 seconds
4. Take a screenshot

**Known issue:** Scrolling sometimes cycles between 3-4 previously seen Reels instead of loading new content. If this happens twice in a row, switch to a different method.

### Fallback: Fresh Feed Reset

If navigation becomes stuck (same Reels cycling, content not advancing after 2-3 attempts):

1. Navigate directly to `https://www.facebook.com/reel/`
2. This forces Facebook to load a completely fresh Reels feed
3. Take a screenshot to verify new content
4. Resume normal "Next Card" navigation

### Navigation After Commenting

Commenting is the action most likely to break navigation, because the comment input captures keyboard focus. After posting a comment:

1. Press `Escape` to close/defocus the comment input
2. Click on an empty area of the Reel player to restore player focus
3. Use the "Next Card" button (primary method) to advance -- do NOT rely on ArrowDown immediately after commenting

---

## Engagement Actions

Engage **directly from the Reel** -- no need to visit the creator's profile first. Just react, follow, and (selectively) comment right there.

### 1. React to the Reel

Facebook reactions require a hover-to-reveal interaction. Here's the exact sequence:

#### How to React (Step-by-Step)

**For a simple Like:**
1. Use `find` tool with query **"Like button"** on the current Reel
2. Click the returned reference
3. The thumbs-up Like is applied immediately

**For Love, Care, or other reactions:**
1. Use `find` tool with query **"Like button"** on the current Reel
2. **Hover** (do not click) on the Like button reference for 1-2 seconds
3. A reaction picker bar will appear above the button showing emoji options
4. Take a screenshot to see the picker and identify positions
5. Click the desired reaction:
   - **Love** (heart) is typically the second icon from the left
   - **Care** (hug face) is typically the third icon
6. Wait 1 second to confirm the reaction registered

**If the reaction picker doesn't appear after hovering:**
- Try hovering slightly above or below the Like button
- Hold the hover for a full 2 seconds
- If it still doesn't appear, fall back to a simple Like (click)

#### Reaction Selection Guide

| Reaction | When to Use | Frequency |
|----------|-------------|-----------|
| **Like** (thumbs up) | Safe default for any Reel | ~50% of reactions |
| **Love** (heart) | Beautiful visuals, inspiring work, aesthetic content | ~40% of reactions |
| **Care** (hug) | Personal stories, milestones, vulnerable posts | ~10% of reactions |

**Never use:** Haha, Wow, Sad, or Angry -- too easy to misread coming from a brand Page.

#### Stale Reference Warning

The Like button reference can become stale if the feed has scrolled or loaded new content in the background. **Always re-query the Like button using `find` after navigating to a new Reel.** Never reuse a Like button reference from a previous Reel -- it may target the wrong Reel's button and cause the page to jump unexpectedly.

### 2. Follow the Creator's Page

#### How to Follow (Step-by-Step)

1. Use `find` tool with query **"Follow button"**
2. If multiple results are returned, use the one closest to the creator name overlay on the current Reel (take a screenshot if needed to confirm)
3. Click the Follow button reference
4. Wait 1 second and verify the button text changed to "Following"

**Common issues:**
- The Follow button may be near other clickable elements (music/audio links, creator name links). If you accidentally open a popup, close it with `Escape` or `find` the X/close button, then re-query and click Follow
- If the Follow button isn't visible on the Reel overlay, skip the follow for this Reel -- don't navigate away to the profile page
- If the creator is already followed (button shows "Following"), skip and move on -- do NOT unfollow

### 3. Comment (Selectively)

**4 comments per session max** (see `references/comment-guide.md` for writing guidelines)

#### How to Comment (Step-by-Step)

1. Use `find` tool with query **"Comment"** or **"Comment button"** on the current Reel
2. Click the comment button/icon to open the comment section
3. Wait 1-2 seconds for the comment input to appear
4. Use `find` tool with query **"comment input"** or **"Write a comment"**
5. Click the comment input to focus it
6. Type your comment using the `type` action
7. Use `find` tool with query **"Send"** or **"Submit"** or **"Post comment button"** (it may be an arrow/send icon)
8. Click the send button
9. Wait 1-2 seconds to confirm the comment posted
10. **Critical:** Press `Escape` or click outside the comment area to release focus before attempting to navigate to the next Reel

**If the comment input doesn't appear after clicking the comment icon:**
- Try clicking the comment icon again
- Take a screenshot to see if a different UI element opened
- If the comments section opened but the input isn't visible, scroll down within the comment section

**If the send button is hard to find:**
- Look for a small arrow icon or paper plane icon to the right of the comment input
- Try `find` with queries: "Send", "Post", "Submit", or "arrow button near comment"

#### Comment on Reels where you have something specific to say about what you SAW in the video. Since these are videos, reference the content -- a technique, a transformation, a satisfying moment, a specific detail. Don't comment on every Reel you react to.

---

## Engagement Depth Variation

Not every Reel gets the same level of engagement. Vary the depth to look natural:

| Depth Level | Actions | Approximate Split |
|-------------|---------|-------------------|
| Light | React only | ~40% of engaged Reels |
| Medium | React + Follow | ~35% of engaged Reels |
| Full | React + Follow + Comment | ~25% of engaged Reels (limited by 4 comment max) |

When doing multiple actions on a single Reel, perform them in this order with pauses between:
1. **React** first (this is quick and natural)
2. Wait 10-15 seconds
3. **Follow** the Page
4. Wait 15-30 seconds
5. **Comment** (if this is a Reel worth commenting on)

---

## Session Flow

1. **Navigate** to `https://www.facebook.com/reel/`
2. **Take a screenshot** to see the first Reel
3. **Assess niche fit** -- does this content belong in the brand's world?
4. **Engage** if relevant -- react, follow, and selectively comment
5. **Advance** to the next Reel using the "Next Card" button (primary method)
6. **Repeat** until session limits are reached
7. Track your counts: reactions (target 12), follows (target 8), comments (target 4)

### Handling Non-Niche Content

When you encounter content that doesn't fit the brand's niche, simply advance to the next Reel. No need to wait or interact. If you hit a streak of 5+ non-niche Reels, navigate to `https://www.facebook.com/reel/` for a fresh feed.

---

## Session Limits

| Action | Per Session | Daily Max (2 sessions) |
|--------|-------------|------------------------|
| Page follows | 8 | 16 |
| Reactions | 12 | 24 |
| Comments | 4 | 8 |

**Max 2 sessions per day.** Space sessions at least 4 hours apart.

---

## Pacing

- **45-90 seconds** between Page follows
- **20-40 seconds** between reactions
- **1-3 minutes** between comments
- When doing multiple actions on a single Reel (react + follow + comment), space by **15-30 seconds** between each action
- **Watch each Reel for at least 3-5 seconds** before engaging or scrolling past

Use wait time naturally -- you're watching a video, assessing the content, deciding whether to engage. The pacing should feel like browsing, not like executing a checklist.

---

## Safety and Stop Triggers

If you encounter **ANY** of these, **stop immediately** and inform the user:

- "This Feature is Temporarily Unavailable"
- "You're Going Too Fast" or "Slow Down"
- Account checkpoint or identity verification
- CAPTCHA
- "Your Account Has Been Restricted"
- Phone number verification
- "Something Went Wrong" on repeated actions
- Unexpected redirect to a help/support page
- Being logged out unexpectedly

**Cool-down if flagged:** 6-12 hours minimum. Facebook penalties escalate aggressively -- a Business Page restriction can last 7-30 days.

---

## Troubleshooting Quick Reference

| Problem | Solution |
|---------|----------|
| ArrowDown doesn't advance Reel | Click empty area first to clear focus, or use "Next Card" button via `find` |
| Same Reels cycling on scroll | Navigate to `https://www.facebook.com/reel/` for fresh feed |
| Clicked wrong element (audio link, profile link, etc.) | Close popup with Escape or X button, re-query with `find` |
| Reaction picker doesn't appear on hover | Hold hover for 2 full seconds; if still nothing, fall back to simple Like |
| Follow button not visible | Skip follow for this Reel, move on |
| Comment input doesn't get focus | Click directly on the input field, or try `find` with "Write a comment" |
| Navigation broken after commenting | Press Escape, click empty area, use "Next Card" button (not ArrowDown) |
| Like button reference targets wrong Reel | Always re-query `find` after navigating; never reuse refs from a previous Reel |
| Page jumps to unexpected content | A stale reference was clicked; navigate to `https://www.facebook.com/reel/` and restart |

---

## URL Structure

- **Pages:** `https://www.facebook.com/[pagename]`
- **Reels:** `https://www.facebook.com/reel/[reel_id]`

---

## Time Per Session

15-25 minutes. The pacing rules spread actions naturally. Don't rush.
