# Design Specification - File Integrity Checker

## Visual Design Reference

### Page Layout

```
┌─────────────────────────────────────────────────┐
│                                                 │
│              🛡️ (Shield Icon)                   │
│                                                 │
│         File Integrity Checker                  │
│   Hash-based file integrity verification        │
│                                                 │
├─────────────────────────────────────────────────┤
│  ┌───────────────────────────────────────────┐  │
│  │                                           │  │
│  │         📤 (Upload Icon)                  │  │
│  │                                           │  │
│  │   Drop file here or click to browse      │  │
│  │   Select a file to verify its integrity  │  │
│  │                                           │  │
│  │      [ document.pdf ]                     │  │
│  │                                           │  │
│  └───────────────────────────────────────────┘  │
│                                                 │
│  ┌──────────────────┐  ┌──────────────────┐    │
│  │  💾 Store Hash   │  │  🛡️ Verify      │    │
│  └──────────────────┘  └──────────────────┘    │
│                                                 │
│  ┌───────────────────────────────────────────┐  │
│  │ 🟢 Hash stored successfully!              │  │
│  └───────────────────────────────────────────┘  │
├─────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐            │
│  │ ℹ️ How it    │  │ 🔒 Secure &  │            │
│  │   works      │  │    Private   │            │
│  │              │  │              │            │
│  │ Upload file  │  │ Only hashes  │            │
│  │ and store... │  │ are stored.. │            │
│  └──────────────┘  └──────────────┘            │
│                                                 │
│           🛡️ Cybersecurity Internship          │
│                  Project                        │
└─────────────────────────────────────────────────┘
```

## Color Palette

### Primary Colors
```css
Background Primary:   #0a0e1a  ████  Deep Navy
Background Secondary: #141821  ████  Slate Navy
Card Background:      #1a1f2e  ████  Charcoal Blue
Hover Background:     #222938  ████  Steel Gray
```

### Accent Colors
```css
Primary (Blue):     #3b82f6  ████  Bright Blue
Primary Dark:       #2563eb  ████  Deep Blue
Success (Green):    #10b981  ████  Emerald
Error (Red):        #ef4444  ████  Crimson
Warning (Orange):   #f59e0b  ████  Amber
```

### Text Colors
```css
Primary Text:       #f1f5f9  ████  Light Gray
Secondary Text:     #94a3b8  ████  Medium Gray
Muted Text:         #64748b  ████  Slate Gray
```

### Border Colors
```css
Border Default:     #2d3748  ████  Dark Steel
Border Light:       #374151  ████  Medium Steel
```

## Typography Scale

```
H1 (Title):          40px / 2.5rem    Bold      Gradient
Subtitle:            16px / 1rem      Regular   Secondary
H3 (Upload):         18px / 1.125rem  Semi-Bold Primary
Body Text:           15px / 0.9375rem Regular   Primary
Small Text:          13px / 0.8125rem Regular   Secondary
Footer:              14px / 0.875rem  Regular   Muted
```

## Spacing System (8px base)

```
xs:   4px   (0.25rem)
sm:   8px   (0.5rem)
md:   16px  (1rem)
lg:   24px  (1.5rem)
xl:   32px  (2rem)
2xl:  48px  (3rem)
3xl:  64px  (4rem)
```

## Component Specifications

### Header Icon (Shield)
- Size: 64px × 64px
- Background: Linear gradient (Blue → Green)
- Border Radius: 12px
- Shadow: Large (0 10px 15px rgba(0,0,0,0.5))

### Upload Zone
- Padding: 48px 32px (desktop), 32px 16px (mobile)
- Border: 2px dashed #374151
- Border Radius: 12px
- Background: #141821
- Hover: Border → #3b82f6, Background → #222938
- Drag Over: Border → #10b981, Scale: 1.02

### Buttons
- Height: 48px (desktop), 42px (mobile)
- Padding: 16px 24px
- Border Radius: 12px
- Font: 16px semi-bold
- Icon: 20px × 20px
- Gap: 8px between icon and text

#### Primary Button (Store Hash)
- Background: Linear gradient (Blue → Darker Blue)
- Text: White
- Hover: Lift -2px, Darker gradient
- Active: Press +1px

#### Secondary Button (Verify)
- Background: #141821
- Border: 1px solid #374151
- Text: White
- Hover: Background → #222938, Border → Green

### Status Indicators

#### Success (Green)
```css
Indicator: 12px circle, #10b981, glow effect
Background: #141821
Border: 1px solid #2d3748
Padding: 20px
```

#### Error (Red)
```css
Indicator: 12px circle, #ef4444, glow effect
Same styling as success but red color
```

#### Warning (Orange)
```css
Indicator: 12px circle, #f59e0b, glow effect
Same styling but amber color
```

### Info Cards
- Width: 50% each (100% mobile)
- Padding: 24px
- Border Radius: 12px
- Border: 1px solid #2d3748
- Hover: Lift -2px, Border → Blue
- Icon: 24px × 24px, Blue color

## Animation Specifications

### Fade In
```
Duration: 0.8s
Timing: ease
From: opacity 0
To: opacity 1
```

### Fade In Down (Header)
```
Duration: 0.6s
Timing: ease
From: opacity 0, translateY(-20px)
To: opacity 1, translateY(0)
```

### Fade In Up (Content)
```
Duration: 0.6s
Timing: ease
From: opacity 0, translateY(20px)
To: opacity 1, translateY(0)
```

### Slide In (Status)
```
Duration: 0.4s
Timing: ease
From: opacity 0, translateX(-10px)
To: opacity 1, translateX(0)
```

### Hover Effects
```
Duration: 0.25s (250ms)
Timing: ease
Transform: translateY(-2px)
Shadow: Increase depth
```

## Responsive Breakpoints

### Mobile (< 480px)
- Container: 100% width, 16px padding
- Title: 28px
- Upload Zone: 24px padding
- Buttons: Stack vertically, 100% width
- Info Cards: Stack vertically
- Header Icon: 56px

### Tablet (480px - 768px)
- Container: 100% width, 16px padding
- Title: 32px
- Upload Zone: 32px padding
- Buttons: Side by side
- Info Cards: Stack vertically
- Header Icon: 56px

### Desktop (> 768px)
- Container: 720px max-width, centered
- Title: 40px
- Upload Zone: 48px padding
- Buttons: Side by side
- Info Cards: Side by side
- Header Icon: 64px

## Accessibility Features

### Contrast Ratios
- Body Text (White on Dark): 15:1 (AAA)
- Secondary Text: 7:1 (AAA)
- Muted Text: 4.8:1 (AA)
- Link Hover: 12:1 (AAA)

### Focus States
- Outline: 3px solid #3b82f6
- Outline Offset: 2px
- Applied to: Buttons, inputs, upload zone

### Keyboard Navigation
- Tab Order: Upload zone → Store → Verify
- Upload Zone: tabindex="0", role="button"
- Enter/Space: Trigger file picker
- Focus visible indicator on all elements

### Screen Reader
- Semantic HTML5 elements
- Descriptive aria-labels
- Alt text for all icons (SVG titles)
- Status messages announced

### Motion Sensitivity
```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

## Icon Set

All icons use inline SVG with stroke-based design:

- 🛡️ Shield with checkmark (security/verification)
- 📤 Upload arrow (file upload)
- 💾 Save/Database (store hash)
- ℹ️ Info circle (information)
- 🔒 Lock (security/privacy)
- ⚠️ Alert circle (warnings)

## Shadow System

```css
Small:     0 1px 2px rgba(0,0,0,0.3)
Medium:    0 4px 6px rgba(0,0,0,0.4), 0 2px 4px rgba(0,0,0,0.3)
Large:     0 10px 15px rgba(0,0,0,0.5), 0 4px 6px rgba(0,0,0,0.3)
Extra Large: 0 20px 25px rgba(0,0,0,0.5), 0 10px 10px rgba(0,0,0,0.3)
```

## Status Indicator Glow

```css
box-shadow: 0 0 8px currentColor
```

This creates a subtle glow effect matching the indicator color for visual feedback.

## Implementation Notes

### CSS Variables
All colors, spacing, and timing values use CSS custom properties for easy theming and maintenance.

### Browser Prefixes
Vendor prefixes included for:
- `-webkit-font-smoothing`
- `-webkit-background-clip`
- `-webkit-text-fill-color`

### Performance
- Hardware-accelerated transforms
- Will-change hints where appropriate
- Efficient selectors
- No layout thrashing

### Print Styles
Not implemented (not required for web app).

## Future Design Considerations

1. **Dark/Light Toggle** - Add theme switcher
2. **Color Themes** - Multiple accent color options
3. **Compact Mode** - Denser layout option
4. **High Contrast Mode** - Enhanced accessibility
5. **Custom Branding** - Logo upload capability
