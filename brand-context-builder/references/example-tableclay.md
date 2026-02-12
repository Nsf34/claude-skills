# Table Clay Brand Context

This is a complete example of the Extended format, showing all sections filled out. Use this as a reference when generating new brand context files.

## Brand Overview

**Brand name:** Table Clay
**Instagram handle:** _TBD_
**Facebook page:** _TBD_
**TikTok handle:** _TBD_
**Chrome profile name:** _TBD_

**Brand Positioning:** Handmade pottery and creative tools — from mini pottery wheels that bring the studio to your kitchen table, to handcrafted ceramic mugs you'll actually use every day. Premium craftsmanship, handmade quality, creativity-enabling products.

---

## Products

| Product | Price | Description |
|---------|-------|-------------|
| Mini Pottery Wheel | _TBD_ | Starter pottery wheel for beginners and kids — compact, easy cleanup, real clay included |
| Ceramic Travel Mug | _TBD_ | Handmade ceramic travel mug — leakproof, keeps drinks hot, fits standard cupholders |
| Aesthetic/Cute Mugs | _TBD_ | Decorative handmade ceramic mugs for home — unique designs, collectible drops |

---

## Target Customers

- **Apartment adults** — urban dwellers with limited space who want a creative hobby
- **Beginner makers** — new to crafts, intimidated by pottery studios, want an easy start
- **Parents** — looking for screen-free activities for kids (and themselves)
- **Gift seekers** — shopping for unique, handmade, thoughtful gifts
- **Coffee commuters** — daily commute, want a travel mug that feels special
- **Home decor enthusiasts** — care about aesthetics, curate their space

---

## Content Themes

- Pottery and ceramics — process videos, ASMR clay work, finished pieces
- Screen-free activities and mindfulness/stress relief
- Handmade craft culture and maker community
- Coffee culture and morning routines
- Home decor and cozy aesthetic
- Gift guides and unique gift ideas
- Date night and couples activities
- Kids activities and family crafts

---

## Tag Taxonomy

### Angles by Product Line

**mini_wheel:**
- `pottery_therapy` - Stress relief, mindfulness through pottery
- `screen_free_family` - Alternative to screens for kids
- `beginner_confidence` - Anyone can do it, easy to start
- `mess_managed` - Clean, contained, not messy
- `giftable_date_night` - Couples activity, unique gift

**travel_mug:**
- `leakproof_commute` - Won't spill in your bag
- `keeps_hot` - Temperature retention
- `fits_cupholder` - Practical car fit
- `handmade_aesthetic` - Artisan quality, unique look
- `giftable_everyday` - Practical premium gift

**aesthetic_mugs:**
- `morning_ritual` - Elevate your coffee routine
- `cozy_home` - Home comfort aesthetic
- `desk_companion` - Work-from-home style
- `cute_gift` - Giftable adorable design
- `collectible_drops` - Limited editions, collecting

---

### Personas

| Persona | Enum | Description |
|---------|------|-------------|
| Apartment Adult | `apartment_adult` | Urban dweller, limited space |
| Beginner Maker | `beginner_maker` | New to crafts, wants easy start |
| Parent | `parent` | Looking for kid activities |
| Gift Seeker | `gift_seeker` | Shopping for others |
| Coffee Commuter | `coffee_commuter` | Daily commute, needs travel mug |
| Aesthetic Home | `aesthetic_home` | Cares about home décor |

**By Product Line:**
- mini_wheel: `adult_hobbyist`, `apartment_dweller`, `parent`, `gift_seeker`
- travel_mug: `commuter`, `office_worker`, `student`, `gift_seeker`, `coffee_person`
- aesthetic_mugs: `home_decor`, `coffee_person`, `gift_seeker`, `collector`

---

### Intent Context (Job-to-be-Done)

| Context | Enum |
|---------|------|
| Stress relief | `stress_reset` |
| Screen-free time | `screen_free_time` |
| Coffee ritual | `coffee_ritual` |
| Commute | `commute` |
| Gift shopping | `gift` |
| Home decoration | `home_decor` |

---

### Objection Targets by Product Line

**mini_wheel:**
| Objection | Enum | Counter |
|-----------|------|---------|
| Takes up space | `space` | Compact design, stores easily |
| Too messy | `mess` | Contained setup, easy cleanup |
| Hard to learn | `learning_curve` | Beginner-friendly, tutorials included |
| Is it real clay? | `is_it_real_clay` | Yes, air-dry clay included |
| Takes too long | `time` | Quick projects, 30-min sessions |

**travel_mug:**
| Objection | Enum | Counter |
|-----------|------|---------|
| Will it leak? | `leaks` | Leakproof seal guarantee |
| Won't stay hot | `heat_retention` | 6+ hour heat retention |
| Lid quality | `lid_quality` | Premium silicone seal |
| Fragile ceramic | `fragile` | Double-wall protection |
| Won't fit cupholder | `cupholder_fit` | Standard cupholder size |

**aesthetic_mugs:**
| Objection | Enum | Counter |
|-----------|------|---------|
| Will it break? | `breakage` | Durable stoneware |
| Too small/large | `size` | Multiple sizes available |
| Dishwasher safe? | `dishwasher_safe` | Yes, dishwasher safe |
| Too expensive | `price` | Handmade quality justifies |
| Shipping damage | `shipping` | Secure packaging guaranteed |

---

### Proof Types by Product Line

**mini_wheel:**
- `demo` - Product in action, throwing clay
- `outcome` - Finished pieces made by beginners
- `objection_kill` - Cleanup demo, space demo
- `social_proof` - Reviews, testimonials
- `specs` - What's included in kit

**travel_mug:**
- `test` - Leak test, temperature test
- `demo` - Using in car, commute scene
- `comparison` - vs other mugs
- `social_proof` - Reviews, "X sold"
- `specs` - Dimensions, materials

**aesthetic_mugs:**
- `social_proof` - Reviews, UGC photos
- `lifestyle` - In-situ home shots
- `ugc` - Customer photos
- `specs` - Dimensions, care instructions
- `risk_reversal` - Guarantee, return policy

---

### Ad Creative Enums

**Funnel Stage:**
- `tof` - Top of funnel (awareness)
- `mof` - Middle of funnel (consideration)
- `bof` - Bottom of funnel (decision)
- `rt` - Retargeting

**Format:**
- `video`
- `static`
- `carousel`

**Ratio:**
- `9x16` - Vertical (Stories/Reels)
- `4x5` - Portrait (Feed)
- `1x1` - Square

**Offer Type:**
- `none`
- `bundle`
- `free_shipping`
- `limited_drop`
- `giftable`
- `discount`

### Filename Convention

```
{Brand}_{ProductLine}_{Format}_{FunnelStage}_{Concept}_{Angle}_{ProofType}_{HookKey}_{V#}_{Ratio}
```

**Examples:**
- `TableClay_mini_wheel_video_tof_pottery_therapy_demo_asmr_calm_V3_9x16`
- `TableClay_travel_mug_video_tof_leakproof_test_demo_spillproof_V1_9x16`
- `TableClay_aesthetic_mugs_carousel_mof_morning_ritual_social_proof_cozy_V2_4x5`

---

## Competitors

| Account | Why They Compete |
|---------|-----------------|
| @small_ceramics | Direct competitor — mini pottery wheels, 60K followers, home of the "Small Pottery Wheel" |
| @wodeceramics | Mini pottery/ceramics brand with "WHEELIES" product line, 9.8K followers |
| @ceramics_by_jas | Handmade ceramics for everyday use, 287K followers, teaches pottery and business |
| @thirdwheelceramics | Handmade pottery content creator, 55K followers, mesmerizing process content |
| @softfireceramics | Handmade pottery brand, 9.5K followers, artisan ceramic pieces |

---

## Brand Voice

Warm and enthusiastic — like a fellow pottery-obsessed friend who's genuinely excited about clay. Not salesy. Curious about other makers' processes. Comments should feel like someone who loves the craft community and wants to hype up good work. Encouraging to beginners, respectful to pros.

**Tone examples:**
- "The glaze on this is unreal, what cone did you fire at?"
- "This is exactly why pottery > doomscrolling"
- "Ok this makes me want to throw everything and start over, it's perfect"
- "My hands are itching to get on the wheel after seeing this"

---

## Source Research

This brand context file was distilled from the deep research document:
- **Research doc**: `research/tableclay-research.md`
- **Last synced**: 2026-02-11

For comprehensive brand strategy, market analysis, customer research, and detailed product specifications, refer to the full research document.
