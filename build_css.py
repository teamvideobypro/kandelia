# build_css.py - Generates production-ready, beautiful, accessible CSS
css_content = """/* ==========================================================================
   Kandelia 2026 Redesign - Design System & Modern CSS Architecture
   Reverse-Engineered & Architected for Accessibility, Warmth, and Community
   ========================================================================== */

@import url('https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&display=swap');

:root {
  /* Core Palette - Warm, Light, & Airy (Client Requirement 1.A) */
  --bg-cream: #FAF7F2;
  --bg-sand: #F3EFE6;
  --bg-sand-light: #F8F5EE;
  --bg-white: #FFFFFF;
  --bg-sage-tint: #EEF5F0;
  --bg-sky-tint: #EDF4F5;
  --bg-tint-warm: #FBF9F5;

  /* Typography & WCAG AAA Contrast (Client Requirement 1.A) */
  --navy: #12263A;
  --navy-dark: #0A1724;
  --navy-light: #1E3A59;
  --charcoal: #1E293B;
  --text-main: #12263A;
  --text-muted: #4A5568;
  --text-subtle: #64748B;
  --text-inverse: #FFFFFF;

  /* Brand Accents */
  --green: #8DC73F;
  --green-dark: #2A6615;
  --green-soft: #E3F2D4;
  --green-tint: #F2F8ED;
  --coral: #D94532;
  --coral-hover: #BF3625;
  --coral-soft: #FDEEEB;
  --gold: #D99B26;
  --gold-soft: #FEF7EA;

  /* Borders & Shadows */
  --border-light: rgba(18, 38, 58, 0.08);
  --border-medium: rgba(18, 38, 58, 0.14);
  --border-strong: rgba(18, 38, 58, 0.22);
  --shadow-subtle: 0 4px 16px rgba(18, 38, 58, 0.04);
  --shadow-card: 0 10px 30px rgba(18, 38, 58, 0.06), 0 2px 6px rgba(18, 38, 58, 0.03);
  --shadow-float: 0 20px 48px rgba(18, 38, 58, 0.10), 0 4px 12px rgba(18, 38, 58, 0.04);
  --shadow-modal: 0 25px 60px rgba(10, 23, 36, 0.35);

  /* Shape Language - Generous Organic Curves (Client Requirement 1.B) */
  --radius-pill: 9999px;
  --radius-badge: 9999px;
  --radius-card: 28px;
  --radius-card-lg: 32px;
  --radius-container: 40px;
  --radius-image: 28px;
  --radius-arch: 36px 36px 120px 36px;

  /* Spacing System (8px Grid) */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 20px;
  --space-6: 24px;
  --space-8: 32px;
  --space-10: 40px;
  --space-12: 48px;
  --space-16: 64px;
  --space-20: 80px;
  --space-24: 96px;

  /* Animation */
  --transition-fast: 150ms ease;
  --transition-base: 250ms cubic-bezier(0.16, 1, 0.3, 1);
  --transition-smooth: 400ms cubic-bezier(0.16, 1, 0.3, 1);
}

/* ==========================================================================
   Base Styles & Reset
   ========================================================================== */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  font-size: 18px;
  scroll-behavior: smooth;
  scroll-padding-top: 100px;
}

body {
  font-family: 'Atkinson Hyperlegible', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  color: var(--text-main);
  background-color: var(--bg-cream);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow-x: hidden;
}

img {
  display: block;
  max-width: 100%;
  height: auto;
}

a {
  color: var(--navy);
  text-decoration-skip-ink: auto;
  transition: color var(--transition-fast), opacity var(--transition-fast);
}

a:hover {
  color: var(--coral);
}

/* Focus Visibility & Accessibility */
:focus-visible {
  outline: 3px solid var(--gold) !important;
  outline-offset: 3px !important;
}

.skip-link {
  position: absolute;
  top: -100px;
  left: 20px;
  background: var(--navy);
  color: var(--bg-white);
  padding: 12px 20px;
  font-weight: 700;
  border-radius: var(--radius-pill);
  z-index: 99999;
  transition: top var(--transition-fast);
  text-decoration: none;
}

.skip-link:focus {
  top: 16px;
}

.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

/* Container Width */
.w {
  width: 100%;
  max-width: 1240px;
  margin-left: auto;
  margin-right: auto;
  padding-left: 28px;
  padding-right: 28px;
}

.w-narrow {
  max-width: 960px;
  margin-left: auto;
  margin-right: auto;
  padding-left: 24px;
  padding-right: 24px;
}

/* Headings */
h1, h2, h3, h4, h5, h6 {
  color: var(--navy);
  font-weight: 700;
  line-height: 1.25;
}

h1 {
  font-size: clamp(34px, 4.5vw, 54px);
  letter-spacing: -0.02em;
}

h2 {
  font-size: clamp(28px, 3.2vw, 42px);
  letter-spacing: -0.015em;
  margin-bottom: 16px;
}

h3 {
  font-size: clamp(22px, 2.2vw, 28px);
  letter-spacing: -0.01em;
}

h4 {
  font-size: 20px;
}

p {
  color: var(--text-muted);
  font-size: 1.05rem;
  line-height: 1.65;
}

.lead {
  font-size: clamp(1.1rem, 1.4vw, 1.25rem);
  color: var(--text-muted);
  line-height: 1.6;
  max-width: 760px;
}

/* ==========================================================================
   Buttons & Pills (Client Requirement 1.B - Full Pill 9999px)
   ========================================================================== */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  padding: 13px 28px;
  font-weight: 700;
  font-size: 1.05rem;
  line-height: 1;
  text-decoration: none;
  border-radius: var(--radius-pill);
  border: 2px solid transparent;
  cursor: pointer;
  transition: all var(--transition-base);
  white-space: nowrap;
}

.btn .icon {
  width: 18px;
  height: 18px;
  transition: transform var(--transition-fast);
}

.btn:hover .icon.chevron,
.btn:hover .icon {
  transform: translateX(3px);
}

.btn-primary {
  background-color: var(--navy);
  color: var(--bg-white);
  border-color: var(--navy);
  box-shadow: 0 4px 14px rgba(18, 38, 58, 0.15);
}

.btn-primary:hover {
  background-color: var(--navy-light);
  border-color: var(--navy-light);
  color: var(--bg-white);
  transform: translateY(-2px);
  box-shadow: 0 6px 18px rgba(18, 38, 58, 0.22);
}

.btn-coral,
.btn-donate {
  background-color: var(--coral);
  color: var(--bg-white);
  border-color: var(--coral);
  box-shadow: 0 4px 14px rgba(217, 69, 50, 0.25);
}

.btn-coral:hover,
.btn-donate:hover {
  background-color: var(--coral-hover);
  border-color: var(--coral-hover);
  color: var(--bg-white);
  transform: translateY(-2px);
  box-shadow: 0 8px 22px rgba(217, 69, 50, 0.35);
}

.btn-outline {
  background-color: transparent;
  color: var(--navy);
  border-color: var(--navy);
}

.btn-outline:hover {
  background-color: rgba(18, 38, 58, 0.06);
  color: var(--navy-dark);
  transform: translateY(-2px);
}

.btn-outline-white {
  background-color: transparent;
  color: var(--bg-white);
  border-color: var(--bg-white);
}

.btn-outline-white:hover {
  background-color: var(--bg-white);
  color: var(--navy);
}

.btn-sm {
  padding: 8px 18px;
  font-size: 0.95rem;
}

.btn-lg {
  padding: 16px 36px;
  font-size: 1.15rem;
}

/* Badges & Chips */
.badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 16px;
  font-size: 0.9rem;
  font-weight: 700;
  border-radius: var(--radius-badge);
  background: var(--bg-sand);
  color: var(--navy);
  border: 1px solid var(--border-light);
}

.badge-sage {
  background: var(--bg-sage-tint);
  color: var(--navy);
  border-color: rgba(141, 199, 63, 0.3);
}

.badge-green {
  background: var(--green-soft);
  color: var(--navy); /* WCAG AAA - dark text on green tint */
}

.badge-coral {
  background: var(--coral-soft);
  color: var(--coral);
}

.badge-gold {
  background: var(--gold-soft);
  color: #925C05;
}

/* ==========================================================================
   Global Utility Bar (Client Requirement 2.Global)
   ========================================================================== */
.util-bar {
  background-color: var(--navy);
  color: var(--bg-white);
  font-size: 0.9rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  position: relative;
  z-index: 1010;
}

.util-bar .w {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 24px;
  height: 42px;
}

.util-bar a {
  color: rgba(255, 255, 255, 0.92);
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.util-bar a:hover {
  color: var(--bg-white);
  text-decoration: underline;
}

.util-bar .icon {
  width: 15px;
  height: 15px;
}

.lang-selector {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(255, 255, 255, 0.12);
  padding: 4px 10px;
  border-radius: var(--radius-pill);
}

.lang-selector label {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 0.85rem;
  color: rgba(255, 255, 255, 0.9);
  cursor: pointer;
}

.lang-selector select {
  background: transparent;
  color: var(--bg-white);
  border: none;
  font-family: inherit;
  font-size: 0.85rem;
  font-weight: 700;
  cursor: pointer;
  outline: none;
  padding-right: 4px;
}

.lang-selector select option {
  background: var(--navy);
  color: var(--bg-white);
}

/* ==========================================================================
   Header & Navigation (Client Requirement 2.Global - Round logo, Donate pill)
   ========================================================================== */
.site-header {
  background-color: var(--bg-white);
  border-bottom: 1px solid var(--border-light);
  position: sticky;
  top: 0;
  z-index: 1000;
  transition: box-shadow var(--transition-base), background-color var(--transition-base);
}

.site-header.scrolled {
  box-shadow: 0 8px 24px rgba(18, 38, 58, 0.08);
}

.header-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 90px;
  gap: 32px;
}

.brand-link {
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
  flex-shrink: 0;
}

.brand-logo {
  height: 52px;
  width: auto;
  object-fit: contain;
  transition: transform var(--transition-base);
}

.brand-link:hover .brand-logo {
  transform: scale(1.03);
}

/* Desktop Navigation */
.main-nav {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-left: auto;
}

.nav-item {
  position: relative;
}

.nav-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 10px 14px;
  color: var(--navy);
  font-weight: 700;
  font-size: 1rem;
  text-decoration: none;
  border-radius: var(--radius-pill);
  transition: background-color var(--transition-fast), color var(--transition-fast);
}

.nav-link:hover,
.nav-link:focus {
  background-color: var(--bg-sand);
  color: var(--navy-dark);
}

.nav-link .icon.chevron {
  width: 14px;
  height: 14px;
  transition: transform var(--transition-fast);
}

.nav-item:hover .nav-link .icon.chevron,
.nav-item:focus-within .nav-link .icon.chevron {
  transform: rotate(180deg);
}

/* Dropdown Menu */
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  min-width: 220px;
  background: var(--bg-white);
  border-radius: 20px;
  padding: 10px;
  box-shadow: var(--shadow-float);
  border: 1px solid var(--border-light);
  opacity: 0;
  visibility: hidden;
  transform: translateY(10px);
  transition: all var(--transition-fast);
  z-index: 1050;
  list-style: none;
}

.nav-item:hover .dropdown-menu,
.nav-item:focus-within .dropdown-menu {
  opacity: 1;
  visibility: visible;
  transform: translateY(4px);
}

.dropdown-link {
  display: block;
  padding: 10px 16px;
  color: var(--navy);
  text-decoration: none;
  font-size: 0.95rem;
  font-weight: 700;
  border-radius: 12px;
  transition: background-color var(--transition-fast), color var(--transition-fast);
}

.dropdown-link:hover {
  background-color: var(--bg-sand);
  color: var(--coral);
}

/* Mobile Toggle */
.mobile-toggle {
  display: none;
  background: transparent;
  border: 2px solid var(--navy);
  color: var(--navy);
  font-family: inherit;
  font-size: 1rem;
  font-weight: 700;
  padding: 8px 16px;
  border-radius: var(--radius-pill);
  cursor: pointer;
  align-items: center;
  gap: 8px;
}

/* Mobile Drawer */
.mobile-nav-drawer {
  display: none;
  background: var(--bg-white);
  border-top: 1px solid var(--border-light);
  padding: 20px 24px 30px;
  box-shadow: 0 10px 20px rgba(18, 38, 58, 0.08);
}

.mobile-nav-drawer.open {
  display: block;
}

.mobile-nav-drawer a {
  display: block;
  padding: 12px 0;
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--navy);
  text-decoration: none;
  border-bottom: 1px solid var(--border-light);
}

.mobile-nav-drawer .mobile-sublink {
  padding-left: 20px;
  font-size: 1rem;
  font-weight: 400;
  color: var(--text-muted);
}

.mobile-nav-drawer .btn-donate {
  margin-top: 20px;
  width: 100%;
}

/* ==========================================================================
   Organic Decorative Elements & Background Blobs (Client Requirement 1.B)
   ========================================================================== */
.organic-bg {
  position: relative;
  overflow: hidden;
}

.organic-blob {
  position: absolute;
  border-radius: 50% 40% 60% 45% / 45% 55% 45% 55%;
  filter: blur(40px);
  pointer-events: none;
  z-index: 0;
  opacity: 0.65;
  transition: transform 12s ease-in-out infinite alternate;
}

.blob-sage {
  background: rgba(141, 199, 63, 0.18);
}

.blob-sand {
  background: rgba(235, 225, 205, 0.55);
}

.blob-sky {
  background: rgba(195, 222, 227, 0.35);
}

.blob-coral {
  background: rgba(224, 90, 71, 0.08);
}

/* ==========================================================================
   Section 1: Home - Hero Section (Client Requirement 1.C, 2.1)
   Light/soft background, organic arch frame, natural text flow around photo
   ========================================================================== */
.section-hero {
  background-color: var(--bg-cream);
  padding: 60px 0 80px;
  position: relative;
}

.hero-grid {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 48px;
  align-items: center;
  position: relative;
  z-index: 1;
}

.hero-content {
  max-width: 650px;
}

.hero-badge-container {
  margin-bottom: 20px;
}

.hero-title {
  margin-bottom: 22px;
  color: var(--navy);
  font-size: clamp(36px, 4.2vw, 56px);
  line-height: 1.16;
}

.hero-lead {
  font-size: clamp(1.15rem, 1.4vw, 1.3rem);
  color: var(--charcoal);
  line-height: 1.68;
  margin-bottom: 34px;
}

.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  align-items: center;
}

/* Hero Media with Organic Arch/Pill mask & Overlapping Card */
.hero-media-wrapper {
  position: relative;
  display: flex;
  justify-content: center;
}

.hero-image-frame {
  position: relative;
  border-radius: var(--radius-arch);
  overflow: hidden;
  box-shadow: var(--shadow-float);
  border: 4px solid var(--bg-white);
  background: var(--bg-sand);
  aspect-ratio: 4 / 3.5;
  width: 100%;
  max-width: 520px;
}

.hero-image-frame img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: 60% 30%;
  transition: transform var(--transition-smooth);
}

.hero-image-frame:hover img {
  transform: scale(1.03);
}

/* Floating Overlapping Card (Treehouse for kids reference) */
.floating-stat-card {
  position: absolute;
  bottom: -24px;
  left: -20px;
  background: var(--bg-white);
  border-radius: var(--radius-card);
  padding: 16px 24px;
  box-shadow: var(--shadow-float);
  border: 1px solid var(--border-light);
  display: flex;
  align-items: center;
  gap: 16px;
  z-index: 2;
  animation: floatSlow 6s ease-in-out infinite;
}

.floating-stat-badge {
  width: 52px;
  height: 52px;
  border-radius: var(--radius-pill);
  background: var(--green-soft);
  color: var(--navy);
  display: grid;
  place-items: center;
  font-size: 24px;
  flex-shrink: 0;
}

.floating-stat-text b {
  display: block;
  font-size: 1.25rem;
  color: var(--navy);
  line-height: 1.2;
}

.floating-stat-text span {
  font-size: 0.88rem;
  color: var(--text-muted);
}

@keyframes floatSlow {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-8px); }
}

/* ==========================================================================
   Section 1: Event Banner - Sip & Celebrate 50 Years (Client Requirement 2.1)
   Floating rounded card overlapping section boundary
   ========================================================================== */
.event-banner-section {
  position: relative;
  z-index: 10;
  margin-top: -30px; /* Slight overlap with hero */
  margin-bottom: 60px;
}

.event-card {
  background: linear-gradient(135deg, var(--bg-white) 0%, var(--bg-sand-light) 100%);
  border-radius: var(--radius-card-lg);
  padding: 40px;
  box-shadow: var(--shadow-card);
  border: 1px solid var(--border-light);
  display: grid;
  grid-template-columns: 240px 1fr auto;
  gap: 36px;
  align-items: center;
  position: relative;
  overflow: hidden;
}

.event-image {
  border-radius: 20px;
  overflow: hidden;
  aspect-ratio: 4 / 3;
  width: 100%;
}

.event-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center 60%;
}

.event-content h3 {
  font-size: clamp(24px, 2.5vw, 32px);
  margin-bottom: 8px;
}

.event-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin: 12px 0 16px;
}

.event-actions {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

/* Sponsors row inside event */
.event-sponsors {
  grid-column: 1 / -1;
  border-top: 1px solid var(--border-light);
  padding-top: 24px;
  margin-top: 10px;
  display: flex;
  align-items: center;
  gap: 20px;
  flex-wrap: wrap;
}

.event-sponsors b {
  font-size: 0.95rem;
  color: var(--text-muted);
}

.sponsor-pill {
  padding: 8px 18px;
  background: rgba(18, 38, 58, 0.04);
  border: 1px dashed var(--border-medium);
  border-radius: var(--radius-pill);
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--text-muted);
}

/* ==========================================================================
   Section 1: Who We Help (2-Column Split: Youth & Families)
   ========================================================================== */
.section-who-we-help {
  padding: 60px 0 90px;
  background-color: var(--bg-white);
  border-radius: var(--radius-container);
  margin: 0 16px;
}

.section-header-center {
  text-align: center;
  max-width: 780px;
  margin: 0 auto 50px;
}

.section-header-center h2 {
  margin-bottom: 12px;
}

.who-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 40px;
}

.program-column-card {
  background: var(--bg-sand-light);
  border-radius: var(--radius-card-lg);
  padding: 36px;
  border: 1px solid var(--border-light);
  display: flex;
  flex-direction: column;
  transition: transform var(--transition-base), box-shadow var(--transition-base);
}

.program-column-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-card);
}

.program-card-image {
  border-radius: var(--radius-image);
  overflow: hidden;
  aspect-ratio: 16 / 9;
  margin-bottom: 24px;
}

.program-card-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform var(--transition-smooth);
}

.program-column-card:hover .program-card-image img {
  transform: scale(1.03);
}

.program-column-card h3 {
  margin-bottom: 12px;
}

.program-column-card > p {
  margin-bottom: 24px;
}

/* Accordion details */
.styled-details {
  border-bottom: 1px solid var(--border-medium);
  margin-bottom: 8px;
}

.styled-details:first-of-type {
  border-top: 1px solid var(--border-medium);
}

.styled-summary {
  padding: 16px 0;
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--navy);
  cursor: pointer;
  list-style: none;
  display: flex;
  justify-content: space-between;
  align-items: center;
  user-select: none;
}

.styled-summary::-webkit-details-marker {
  display: none;
}

.styled-summary .acc-icon {
  width: 28px;
  height: 28px;
  border-radius: var(--radius-pill);
  background: rgba(18, 38, 58, 0.06);
  display: grid;
  place-items: center;
  font-size: 1.2rem;
  color: var(--navy);
  transition: transform var(--transition-fast), background-color var(--transition-fast);
}

.styled-details[open] .styled-summary .acc-icon {
  transform: rotate(45deg);
  background: var(--coral);
  color: var(--bg-white);
}

.details-content {
  padding: 0 0 16px;
  color: var(--text-muted);
  font-size: 1rem;
  line-height: 1.6;
}

.eligibility-box {
  background: var(--bg-white);
  border-radius: 20px;
  padding: 22px;
  margin-top: 28px;
  border: 1px solid var(--border-light);
  margin-bottom: 24px;
}

.eligibility-box b {
  display: block;
  font-size: 1.05rem;
  color: var(--navy);
  margin-bottom: 8px;
}

.eligibility-box ul {
  padding-left: 20px;
  margin-bottom: 12px;
  color: var(--text-muted);
}

.eligibility-box li {
  margin-bottom: 6px;
}

/* ==========================================================================
   Section 1: Our Impact (Client Requirement 1.A, 2.1 - NO heavy blue walls)
   Muted, soft warm sand/sage background, refined non-glaring pill badges
   ========================================================================== */
.section-impact {
  padding: 90px 0;
  background: linear-gradient(180deg, var(--bg-sand) 0%, var(--bg-cream) 100%);
  position: relative;
  overflow: hidden;
}

.impact-header {
  text-align: center;
  max-width: 800px;
  margin: 0 auto 50px;
}

.impact-badges-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
  margin-bottom: 48px;
}

.impact-badge-card {
  background: var(--bg-white);
  border-radius: var(--radius-card);
  padding: 32px 24px;
  text-align: center;
  box-shadow: var(--shadow-card);
  border: 1px solid var(--border-light);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  transition: transform var(--transition-base), box-shadow var(--transition-base);
}

.impact-badge-card:hover {
  transform: translateY(-6px);
  box-shadow: var(--shadow-float);
}

.impact-stat-number {
  font-size: clamp(40px, 4vw, 54px);
  font-weight: 700;
  line-height: 1.1;
  color: var(--navy);
  margin-bottom: 8px;
  display: inline-block;
}

.impact-badge-card:nth-child(1) .impact-stat-number { color: #1E3A59; }
.impact-badge-card:nth-child(2) .impact-stat-number { color: #2A6615; }
.impact-badge-card:nth-child(3) .impact-stat-number { color: #925C05; }
.impact-badge-card:nth-child(4) .impact-stat-number { color: var(--coral); }

.impact-stat-label {
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--navy);
  margin-bottom: 6px;
}

.impact-stat-sub {
  font-size: 0.9rem;
  color: var(--text-muted);
}

/* ==========================================================================
   Section 1: In Their Words Carousel (Client Requirement 1.A, 2.1)
   Auto-scrolling, light warm background, pause on hover, manual controls
   ========================================================================== */
.section-testimonials {
  padding: 80px 0 90px;
  background-color: var(--bg-sage-tint);
  border-radius: var(--radius-container);
  margin: 0 16px;
  position: relative;
}

.carousel-container {
  position: relative;
  max-width: 900px;
  margin: 0 auto;
}

.carousel-track-wrapper {
  overflow: hidden;
  border-radius: var(--radius-card-lg);
  background: var(--bg-white);
  box-shadow: var(--shadow-card);
  border: 1px solid var(--border-light);
  padding: 50px 60px;
  min-height: 300px;
}

.carousel-slide {
  display: none;
  animation: fadeIn 400ms ease;
}

.carousel-slide.active {
  display: block;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(8px); }
  to { opacity: 1; transform: translateY(0); }
}

.testimonial-quote {
  font-size: clamp(1.2rem, 1.8vw, 1.45rem);
  line-height: 1.6;
  color: var(--navy);
  font-weight: 400;
  margin-bottom: 24px;
  position: relative;
  padding-left: 32px;
  border-left: 5px solid var(--green);
}

.testimonial-author-block {
  display: flex;
  align-items: center;
  gap: 16px;
  padding-left: 32px;
}

.author-avatar {
  width: 50px;
  height: 50px;
  border-radius: var(--radius-pill);
  background: var(--bg-sand);
  display: grid;
  place-items: center;
  font-weight: 700;
  color: var(--navy);
  font-size: 1.1rem;
}

.author-info b {
  display: block;
  font-size: 1.1rem;
  color: var(--navy);
}

.author-info span {
  font-size: 0.95rem;
  color: var(--text-muted);
}

/* Carousel Controls */
.carousel-controls {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 20px;
  margin-top: 32px;
}

.carousel-btn {
  width: 44px;
  height: 44px;
  border-radius: var(--radius-pill);
  background: var(--bg-white);
  border: 2px solid var(--navy);
  color: var(--navy);
  display: grid;
  place-items: center;
  cursor: pointer;
  transition: all var(--transition-fast);
}

.carousel-btn:hover {
  background: var(--navy);
  color: var(--bg-white);
}

.carousel-dots {
  display: flex;
  gap: 10px;
}

.carousel-dot {
  width: 12px;
  height: 12px;
  border-radius: var(--radius-pill);
  background: var(--border-medium);
  border: none;
  cursor: pointer;
  transition: all var(--transition-fast);
}

.carousel-dot.active {
  width: 32px;
  background: var(--navy);
}

/* ==========================================================================
   Section 1: Support Our Work Banner (Client Requirement 2.1)
   ========================================================================== */
.section-support-banner {
  padding: 50px 0;
  background: linear-gradient(135deg, var(--navy) 0%, var(--navy-dark) 100%);
  color: var(--bg-white);
  border-radius: var(--radius-card-lg);
  margin: 60px 16px;
}

.support-banner-flex {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 32px;
  flex-wrap: wrap;
}

.support-banner-text h3 {
  color: var(--bg-white);
  font-size: clamp(24px, 2.5vw, 32px);
  margin-bottom: 6px;
}

.support-banner-text p {
  color: rgba(255, 255, 255, 0.85);
  font-size: 1.1rem;
}

/* ==========================================================================
   Section 2: About Us (Newly Expanded: History, Work, Team)
   Sub-navigation tabs, Video embed, Timeline, 3-Card Grid, Staff & Board
   ========================================================================== */
.section-about {
  padding: 80px 0 100px;
  background-color: var(--bg-cream);
}

.about-subnav {
  display: flex;
  justify-content: center;
  gap: 12px;
  margin-bottom: 60px;
  flex-wrap: wrap;
}

.about-subnav-btn {
  padding: 12px 28px;
  font-size: 1.05rem;
  font-weight: 700;
  border-radius: var(--radius-pill);
  background: var(--bg-white);
  color: var(--navy);
  border: 1px solid var(--border-medium);
  cursor: pointer;
  transition: all var(--transition-fast);
  text-decoration: none;
}

.about-subnav-btn.active,
.about-subnav-btn:hover {
  background: var(--navy);
  color: var(--bg-white);
  border-color: var(--navy);
  box-shadow: 0 4px 12px rgba(18, 38, 58, 0.15);
}

.about-block {
  margin-bottom: 100px;
}

/* Part 1: Our History */
.mission-restate-box {
  background: var(--bg-white);
  border-radius: var(--radius-card);
  padding: 36px 40px;
  border-left: 6px solid var(--green);
  box-shadow: var(--shadow-subtle);
  margin-bottom: 40px;
}

.mission-restate-box h3 {
  font-size: 1.5rem;
  color: var(--navy);
  margin-bottom: 8px;
}

/* Video Embed Container */
.video-embed-container {
  background: var(--navy-dark);
  border-radius: var(--radius-card-lg);
  overflow: hidden;
  position: relative;
  aspect-ratio: 16 / 9;
  box-shadow: var(--shadow-card);
  margin-bottom: 48px;
  cursor: pointer;
  border: 4px solid var(--bg-white);
}

.video-poster-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0.75;
  transition: transform var(--transition-smooth), opacity var(--transition-base);
}

.video-embed-container:hover .video-poster-img {
  transform: scale(1.03);
  opacity: 0.85;
}

.video-play-overlay {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 16px;
  color: var(--bg-white);
  z-index: 2;
  text-align: center;
  padding: 20px;
}

.play-circle {
  width: 76px;
  height: 76px;
  border-radius: var(--radius-pill);
  background: var(--coral);
  color: var(--bg-white);
  display: grid;
  place-items: center;
  box-shadow: 0 8px 24px rgba(217, 69, 50, 0.4);
  transition: transform var(--transition-fast), background-color var(--transition-fast);
}

.video-embed-container:hover .play-circle {
  transform: scale(1.12);
  background: var(--coral-hover);
}

.play-circle .icon {
  width: 32px;
  height: 32px;
  margin-left: 4px;
}

.video-caption {
  font-size: 1.25rem;
  font-weight: 700;
  max-width: 600px;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.6);
}

/* Core Truths Narrative */
.core-truths-box {
  background: var(--bg-sand);
  border-radius: var(--radius-card);
  padding: 40px;
  margin-bottom: 60px;
  border: 1px solid var(--border-light);
}

.core-truths-box h3 {
  font-size: 1.6rem;
  margin-bottom: 16px;
}

.core-truths-box p {
  font-size: 1.1rem;
  line-height: 1.7;
  color: var(--charcoal);
  margin-bottom: 16px;
}

/* Interactive Visual Timeline */
.timeline-container {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
  position: relative;
}

.timeline-card {
  background: var(--bg-white);
  border-radius: var(--radius-card);
  padding: 30px 24px;
  border: 1px solid var(--border-light);
  box-shadow: var(--shadow-subtle);
  position: relative;
  transition: transform var(--transition-base), box-shadow var(--transition-base);
}

.timeline-card:hover {
  transform: translateY(-6px);
  box-shadow: var(--shadow-card);
}

.timeline-year {
  font-size: 2.2rem;
  font-weight: 700;
  color: var(--coral);
  line-height: 1;
  margin-bottom: 12px;
}

.timeline-card h4 {
  font-size: 1.15rem;
  margin-bottom: 10px;
  color: var(--navy);
}

.timeline-card p {
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--text-muted);
}

/* Part 2: Our Work (3-Column Rounded Card Grid) */
.our-work-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 32px;
}

.work-card {
  background: var(--bg-white);
  border-radius: var(--radius-card);
  overflow: hidden;
  box-shadow: var(--shadow-subtle);
  border: 1px solid var(--border-light);
  display: flex;
  flex-direction: column;
  transition: transform var(--transition-base), box-shadow var(--transition-base);
}

.work-card:hover {
  transform: translateY(-6px);
  box-shadow: var(--shadow-card);
}

.work-card-img {
  aspect-ratio: 16 / 10;
  width: 100%;
  overflow: hidden;
}

.work-card-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform var(--transition-smooth);
}

.work-card:hover .work-card-img img {
  transform: scale(1.04);
}

.work-card-body {
  padding: 32px 28px;
  flex: 1;
  display: flex;
  flex-direction: column;
}

.work-card-body h3 {
  font-size: 1.35rem;
  margin-bottom: 12px;
}

.work-card-body p {
  font-size: 1rem;
  color: var(--text-muted);
  line-height: 1.6;
  margin-bottom: 20px;
}

.work-bullets {
  padding-left: 20px;
  color: var(--text-muted);
  margin-top: auto;
}

.work-bullets li {
  margin-bottom: 6px;
  font-size: 0.95rem;
}

/* Part 3: Our Team (Staff & Board) */
.staff-hero-banner {
  background: var(--bg-white);
  border-radius: var(--radius-card-lg);
  overflow: hidden;
  box-shadow: var(--shadow-card);
  border: 1px solid var(--border-light);
  margin-bottom: 60px;
}

.staff-hero-image {
  aspect-ratio: 21 / 9;
  width: 100%;
  overflow: hidden;
}

.staff-hero-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center 35%;
}

.staff-hero-text {
  padding: 36px 40px;
}

.staff-hero-text h3 {
  font-size: 1.6rem;
  margin-bottom: 12px;
}

.staff-hero-text p {
  font-size: 1.1rem;
  line-height: 1.7;
}

/* Staff Grid */
.staff-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
  margin-bottom: 80px;
}

.staff-card {
  background: var(--bg-white);
  border-radius: var(--radius-card);
  padding: 28px 24px;
  border: 1px solid var(--border-light);
  box-shadow: var(--shadow-subtle);
  text-align: center;
}

.staff-avatar {
  width: 72px;
  height: 72px;
  border-radius: var(--radius-pill);
  background: var(--bg-sage-tint);
  color: var(--navy);
  font-weight: 700;
  font-size: 1.5rem;
  display: grid;
  place-items: center;
  margin: 0 auto 16px;
}

.staff-card h4 {
  font-size: 1.15rem;
  margin-bottom: 4px;
}

.staff-role {
  font-size: 0.95rem;
  color: var(--coral);
  font-weight: 700;
  margin-bottom: 8px;
}

.staff-languages {
  font-size: 0.85rem;
  color: var(--text-subtle);
  margin-bottom: 12px;
}

.staff-card p {
  font-size: 0.9rem;
  line-height: 1.5;
}

/* Board Responsive Grid (Scales for 7 to 15 members) */
.board-section-title {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  margin-bottom: 30px;
  flex-wrap: wrap;
}

.board-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  margin-bottom: 48px;
}

.board-card {
  background: var(--bg-white);
  border-radius: var(--radius-card);
  padding: 28px;
  border: 1px solid var(--border-light);
  box-shadow: var(--shadow-subtle);
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  transition: transform var(--transition-base), box-shadow var(--transition-base);
}

.board-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-card);
}

.board-avatar {
  width: 80px;
  height: 80px;
  border-radius: var(--radius-pill);
  display: grid;
  place-items: center;
  font-weight: 700;
  font-size: 1.5rem;
  color: var(--bg-white);
  margin-bottom: 16px;
  box-shadow: 0 4px 12px rgba(18, 38, 58, 0.12);
}

.board-name {
  font-size: 1.2rem;
  color: var(--navy);
  margin-bottom: 4px;
}

.board-role {
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--coral);
  margin-bottom: 4px;
}

.board-tenure {
  font-size: 0.85rem;
  color: var(--text-subtle);
  margin-bottom: 18px;
}

.board-bio-btn {
  margin-top: auto;
  width: 100%;
}

/* Board CTA Callout Box */
.board-cta-card {
  background: var(--bg-sand);
  border-radius: var(--radius-card);
  padding: 36px 40px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 32px;
  border: 1px solid var(--border-medium);
  margin-bottom: 70px;
  flex-wrap: wrap;
}

.board-cta-text h3 {
  font-size: 1.4rem;
  margin-bottom: 6px;
}

.board-cta-text p {
  font-size: 1.05rem;
}

/* ==========================================================================
   Section 3: Get Support (High School & Family Programs)
   Top Anchor Cards, Flexible 4-Card Grids, Eligibility Checklists
   ========================================================================== */
.section-get-support {
  padding: 80px 0 100px;
  background-color: var(--bg-white);
}

.support-anchor-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 32px;
  margin-bottom: 70px;
}

.support-anchor-card {
  background: var(--bg-sand-light);
  border-radius: var(--radius-card-lg);
  padding: 40px;
  text-decoration: none;
  color: var(--navy);
  border: 2px solid transparent;
  box-shadow: var(--shadow-subtle);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  transition: all var(--transition-base);
}

.support-anchor-card:hover {
  border-color: var(--navy);
  transform: translateY(-4px);
  box-shadow: var(--shadow-card);
}

.support-anchor-info h3 {
  font-size: 1.6rem;
  margin-bottom: 8px;
}

.support-anchor-info p {
  color: var(--text-muted);
}

.support-anchor-arrow {
  width: 52px;
  height: 52px;
  border-radius: var(--radius-pill);
  background: var(--navy);
  color: var(--bg-white);
  display: grid;
  place-items: center;
  font-size: 1.4rem;
  flex-shrink: 0;
  transition: transform var(--transition-fast);
}

.support-anchor-card:hover .support-anchor-arrow {
  transform: translateX(4px);
  background: var(--coral);
}

/* 4-Card Programs Grid */
.programs-block {
  margin-bottom: 80px;
  padding-top: 20px;
}

.programs-4grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
  margin-bottom: 32px;
}

.subprogram-card {
  background: var(--bg-sand);
  border-radius: var(--radius-card);
  padding: 28px 24px;
  border: 1px solid var(--border-light);
  display: flex;
  flex-direction: column;
}

.subprogram-badge {
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--coral);
  margin-bottom: 8px;
  display: block;
}

.subprogram-card h4 {
  font-size: 1.2rem;
  margin-bottom: 10px;
}

.subprogram-card p {
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--text-muted);
}

.subprogram-visual-card {
  border-radius: var(--radius-card);
  overflow: hidden;
  position: relative;
  border: 1px solid var(--border-light);
}

.subprogram-visual-card img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.visual-card-caption {
  position: absolute;
  bottom: 0;
  inset-inline: 0;
  background: linear-gradient(0deg, rgba(10, 23, 36, 0.9) 0%, transparent 100%);
  color: var(--bg-white);
  padding: 24px 20px 18px;
  font-size: 0.95rem;
  font-weight: 700;
}

/* ==========================================================================
   Section 4: Get Involved (3 Expandable Cards, Captcha Newsletter, Snapshot)
   ========================================================================== */
.section-get-involved {
  padding: 80px 0 100px;
  background-color: var(--bg-cream);
}

.involved-3grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 32px;
  margin-bottom: 70px;
  align-items: start;
}

.action-card {
  background: var(--bg-white);
  border-radius: var(--radius-card-lg);
  padding: 36px 30px;
  border: 1px solid var(--border-light);
  box-shadow: var(--shadow-subtle);
  display: flex;
  flex-direction: column;
  transition: transform var(--transition-base), box-shadow var(--transition-base);
}

.action-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-card);
}

.action-card.card-give {
  border-top: 6px solid var(--coral);
}

.action-card.card-volunteer {
  border-top: 6px solid var(--navy);
}

.action-card.card-partner {
  border-top: 6px solid var(--green);
}

.action-card h3 {
  font-size: 1.6rem;
  margin-bottom: 12px;
}

.action-card > p {
  color: var(--text-muted);
  font-size: 1.05rem;
  margin-bottom: 24px;
}

.action-card-btn {
  margin-top: 24px;
  width: 100%;
}

/* Newsletter Signup with Human-Check Captcha */
.newsletter-card {
  background: var(--bg-white);
  border-radius: var(--radius-card-lg);
  padding: 44px;
  box-shadow: var(--shadow-card);
  border: 1px solid var(--border-light);
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 48px;
  align-items: center;
  margin-bottom: 70px;
}

.newsletter-info h3 {
  font-size: 1.8rem;
  margin-bottom: 8px;
}

.newsletter-social-icons {
  display: flex;
  gap: 12px;
  margin-top: 20px;
}

.social-circle-btn {
  width: 44px;
  height: 44px;
  border-radius: var(--radius-pill);
  background: var(--bg-sand);
  color: var(--navy);
  display: grid;
  place-items: center;
  text-decoration: none;
  transition: all var(--transition-fast);
}

.social-circle-btn:hover {
  background: var(--navy);
  color: var(--bg-white);
  transform: translateY(-2px);
}

.social-circle-btn .icon {
  width: 20px;
  height: 20px;
}

/* Captcha Widget */
.captcha-container {
  background: var(--bg-sand-light);
  border: 1px solid var(--border-medium);
  border-radius: 16px;
  padding: 14px 18px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
  user-select: none;
}

.captcha-checkbox-wrap {
  display: flex;
  align-items: center;
  gap: 14px;
  cursor: pointer;
}

.captcha-checkbox {
  width: 28px;
  height: 28px;
  border-radius: 8px;
  border: 2px solid #8D99AE;
  background: var(--bg-white);
  display: grid;
  place-items: center;
  cursor: pointer;
  transition: all var(--transition-fast);
}

.captcha-checkbox.verified {
  background: var(--green);
  border-color: var(--green);
  color: var(--navy);
}

.captcha-checkbox.verifying {
  border-color: var(--gold);
  border-top-color: transparent;
  animation: spin 600ms linear infinite;
  border-radius: 50%;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.captcha-label {
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--navy);
}

.captcha-badge-tag {
  display: flex;
  flex-direction: column;
  align-items: center;
  color: var(--text-subtle);
  font-size: 0.75rem;
}

.newsletter-form-row {
  display: flex;
  gap: 10px;
}

.newsletter-input {
  flex: 1;
  padding: 14px 20px;
  font-size: 1rem;
  font-family: inherit;
  border: 2px solid var(--border-medium);
  border-radius: var(--radius-pill);
  outline: none;
  background: var(--bg-white);
}

.newsletter-input:focus {
  border-color: var(--navy);
}

.newsletter-feedback {
  margin-top: 10px;
  font-size: 0.9rem;
  font-weight: 700;
  display: none;
}

.newsletter-feedback.success {
  display: block;
  color: var(--green-dark);
}

.newsletter-feedback.error {
  display: block;
  color: var(--coral);
}

/* ==========================================================================
   Section 5: Stories & Impact (Pinned Report Card, Stories Grid, In-Page Reader)
   ========================================================================== */
.section-stories {
  padding: 80px 0 100px;
  background-color: var(--bg-white);
}

.pinned-report-card {
  background: linear-gradient(135deg, var(--bg-sand-light) 0%, var(--bg-white) 100%);
  border-radius: var(--radius-card-lg);
  padding: 44px;
  border: 1px solid var(--border-light);
  box-shadow: var(--shadow-card);
  display: grid;
  grid-template-columns: 260px 1fr;
  gap: 40px;
  align-items: center;
  margin-bottom: 70px;
}

.report-cover-box {
  background: var(--navy);
  color: var(--bg-white);
  border-radius: 20px;
  padding: 32px 24px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: 240px;
  box-shadow: var(--shadow-card);
}

.report-cover-box b {
  font-size: 1.5rem;
  line-height: 1.25;
}

.report-cover-box span {
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.75);
}

.report-details-body h3 {
  font-size: 1.7rem;
  margin-bottom: 12px;
}

.report-datapoints {
  list-style: none;
  margin: 16px 0 24px;
}

.report-datapoints li {
  padding: 8px 0;
  border-bottom: 1px solid var(--border-light);
  color: var(--text-muted);
  display: flex;
  align-items: center;
  gap: 10px;
}

.report-datapoints .icon.check {
  color: var(--green-dark);
  width: 18px;
  height: 18px;
}

/* 4 Stories Grid */
.stories-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
}

.story-card {
  background: var(--bg-cream);
  border-radius: var(--radius-card);
  overflow: hidden;
  border: 1px solid var(--border-light);
  display: flex;
  flex-direction: column;
  cursor: pointer;
  transition: transform var(--transition-base), box-shadow var(--transition-base);
}

.story-card:hover {
  transform: translateY(-6px);
  box-shadow: var(--shadow-card);
}

.story-card-img {
  aspect-ratio: 1 / 1;
  width: 100%;
  overflow: hidden;
}

.story-card-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform var(--transition-smooth);
}

.story-card:hover .story-card-img img {
  transform: scale(1.04);
}

.story-card-body {
  padding: 22px 20px;
  flex: 1;
  display: flex;
  flex-direction: column;
}

.story-card-body h4 {
  font-size: 1.2rem;
  margin-bottom: 8px;
}

.story-card-body p {
  font-size: 0.95rem;
  color: var(--text-muted);
  line-height: 1.5;
  margin-bottom: 16px;
}

.story-read-link {
  margin-top: auto;
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--coral);
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

/* ==========================================================================
   Section 6: Work With Us / Careers (Client Requirement 2.6)
   Interactive categorized tabs/accordion: Staff, Contracted, Youth, Board
   ========================================================================== */
.section-careers {
  padding: 80px 0 100px;
  background-color: var(--bg-cream);
}

.careers-tabs {
  display: flex;
  gap: 12px;
  margin-bottom: 36px;
  flex-wrap: wrap;
}

.careers-tab-btn {
  padding: 12px 26px;
  font-size: 1rem;
  font-weight: 700;
  border-radius: var(--radius-pill);
  background: var(--bg-white);
  border: 1px solid var(--border-medium);
  color: var(--navy);
  cursor: pointer;
  transition: all var(--transition-fast);
}

.careers-tab-btn.active,
.careers-tab-btn:hover {
  background: var(--navy);
  color: var(--bg-white);
  border-color: var(--navy);
}

.careers-panel {
  display: none;
}

.careers-panel.active {
  display: block;
}

.job-card {
  background: var(--bg-white);
  border-radius: var(--radius-card);
  padding: 32px 36px;
  border: 1px solid var(--border-light);
  box-shadow: var(--shadow-subtle);
  margin-bottom: 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 28px;
  flex-wrap: wrap;
}

.job-info h4 {
  font-size: 1.35rem;
  margin-bottom: 8px;
}

.job-meta-pills {
  display: flex;
  gap: 10px;
  margin-bottom: 12px;
  flex-wrap: wrap;
}

.job-info p {
  max-width: 720px;
  font-size: 1rem;
  margin-bottom: 10px;
}

/* ==========================================================================
   Modals (Board Bio, Story Reader, Video Player)
   Smooth backdrop, focus trapped, ESC close, accessible
   ========================================================================== */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(10, 23, 36, 0.65);
  backdrop-filter: blur(6px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
  opacity: 0;
  visibility: hidden;
  transition: all var(--transition-base);
  padding: 20px;
}

.modal-overlay.open {
  opacity: 1;
  visibility: visible;
}

.modal-dialog {
  background: var(--bg-white);
  border-radius: var(--radius-card-lg);
  max-width: 760px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  box-shadow: var(--shadow-modal);
  position: relative;
  transform: translateY(20px) scale(0.96);
  transition: all var(--transition-smooth);
}

.modal-overlay.open .modal-dialog {
  transform: translateY(0) scale(1);
}

.modal-header {
  padding: 28px 36px 20px;
  border-bottom: 1px solid var(--border-light);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.modal-header h3 {
  font-size: 1.5rem;
  color: var(--navy);
}

.modal-close-btn {
  width: 40px;
  height: 40px;
  border-radius: var(--radius-pill);
  background: var(--bg-sand);
  border: none;
  color: var(--navy);
  display: grid;
  place-items: center;
  cursor: pointer;
  transition: background-color var(--transition-fast);
}

.modal-close-btn:hover {
  background: var(--navy);
  color: var(--bg-white);
}

.modal-body {
  padding: 32px 36px 40px;
}

/* ==========================================================================
   Global Footer (Client Requirement 2.Footer)
   Tightened spacing, logo with tagline, Tax ID 91-1122532, LinkedIn
   ========================================================================== */
.site-footer {
  background-color: var(--navy-dark);
  color: rgba(255, 255, 255, 0.9);
  padding: 70px 0 30px;
  font-size: 0.95rem;
}

.footer-grid {
  display: grid;
  grid-template-columns: 1.5fr 1fr 1fr 1fr;
  gap: 48px;
  margin-bottom: 50px;
}

.footer-brand {
  display: flex;
  flex-direction: column;
}

.footer-logo-wrap {
  background: var(--bg-white);
  padding: 10px 18px;
  border-radius: 12px;
  display: inline-block;
  width: fit-content;
  margin-bottom: 14px;
}

.footer-logo-wrap img {
  height: 38px;
  width: auto;
}

.footer-tagline {
  font-size: 1rem;
  font-weight: 700;
  color: var(--bg-white);
  margin-bottom: 14px;
  line-height: 1.4;
}

.footer-contact-info p {
  color: rgba(255, 255, 255, 0.8);
  font-size: 0.95rem;
  line-height: 1.6;
  margin-bottom: 6px;
}

.footer-col h4 {
  color: var(--bg-white);
  font-size: 1.15rem;
  margin-bottom: 18px;
}

.footer-col ul {
  list-style: none;
}

.footer-col li {
  margin-bottom: 10px;
}

.footer-col a {
  color: rgba(255, 255, 255, 0.82);
  text-decoration: none;
  transition: color var(--transition-fast);
}

.footer-col a:hover {
  color: var(--coral-soft);
  text-decoration: underline;
}

.footer-bottom-bar {
  border-top: 1px solid rgba(255, 255, 255, 0.12);
  padding-top: 28px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 16px;
  font-size: 0.88rem;
  color: rgba(255, 255, 255, 0.65);
}

/* ==========================================================================
   RTL Layout Support (Arabic - العربية)
   ========================================================================== */
[dir="rtl"] {
  text-align: right;
}

[dir="rtl"] .util-bar .w {
  justify-content: flex-start;
}

[dir="rtl"] .main-nav {
  margin-left: 0;
  margin-right: auto;
}

[dir="rtl"] .testimonial-quote {
  padding-left: 0;
  padding-right: 32px;
  border-left: none;
  border-right: 5px solid var(--green);
}

[dir="rtl"] .testimonial-author-block {
  padding-left: 0;
  padding-right: 32px;
}

[dir="rtl"] .floating-stat-card {
  left: auto;
  right: -20px;
}

[dir="rtl"] .btn .icon {
  transform: rotate(180deg);
}

/* ==========================================================================
   Responsive Breakpoints (8px Spacing System)
   ========================================================================== */
@media (max-width: 1080px) {
  .hero-grid {
    grid-template-columns: 1fr;
    gap: 40px;
  }

  .hero-media-wrapper {
    order: -1;
  }

  .floating-stat-card {
    position: static;
    margin-top: 16px;
  }

  .event-card {
    grid-template-columns: 1fr;
    gap: 24px;
  }

  .event-image {
    max-width: 320px;
  }

  .impact-badges-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .our-work-grid {
    grid-template-columns: 1fr;
  }

  .timeline-container {
    grid-template-columns: 1fr 1fr;
  }

  .staff-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .board-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .programs-4grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .involved-3grid {
    grid-template-columns: 1fr;
  }

  .stories-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .pinned-report-card {
    grid-template-columns: 1fr;
  }

  .footer-grid {
    grid-template-columns: 1fr 1fr;
  }
}

@media (max-width: 820px) {
  .main-nav,
  .site-header .btn-donate {
    display: none;
  }

  .mobile-toggle {
    display: inline-flex;
  }

  .who-grid {
    grid-template-columns: 1fr;
  }

  .support-anchor-grid {
    grid-template-columns: 1fr;
  }

  .newsletter-card {
    grid-template-columns: 1fr;
    gap: 30px;
  }

  .newsletter-form-row {
    flex-direction: column;
  }
}

@media (max-width: 580px) {
  .w {
    padding-left: 18px;
    padding-right: 18px;
  }

  .section-who-we-help,
  .section-testimonials,
  .section-support-banner {
    margin-left: 0;
    margin-right: 0;
    border-radius: 24px;
  }

  .impact-badges-grid {
    grid-template-columns: 1fr;
  }

  .timeline-container {
    grid-template-columns: 1fr;
  }

  .staff-grid,
  .board-grid,
  .programs-4grid,
  .stories-grid {
    grid-template-columns: 1fr;
  }

  .footer-grid {
    grid-template-columns: 1fr;
  }

  .carousel-track-wrapper {
    padding: 30px 24px;
  }

  .testimonial-quote {
    padding-left: 16px;
    font-size: 1.15rem;
  }
}
"""

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print(f"styles.css created successfully! Length: {len(css_content)} bytes")
