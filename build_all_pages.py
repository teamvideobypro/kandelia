import os
import site_data

print("=== Starting build_all_pages.py ===")

# --- SVG ICONS (Clean, minimal, 24x24 viewBox, stroke-width 2) ---
ICON_CALENDAR = '''<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true" style="width:18px;height:18px;margin-right:6px;vertical-align:-3px;"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>'''
ICON_MAP_PIN = '''<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true" style="width:18px;height:18px;margin-right:6px;vertical-align:-3px;"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>'''
ICON_CLOCK = '''<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true" style="width:18px;height:18px;margin-right:6px;vertical-align:-3px;"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>'''
ICON_CHECK = '''<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="width:18px;height:18px;"><polyline points="20 6 9 17 4 12"></polyline></svg>'''
ICON_CHEVRON = '''<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="width:18px;height:18px;"><polyline points="9 18 15 12 9 6"></polyline></svg>'''
ICON_CAR = '''<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="width:32px;height:32px;"><path d="M19 17h2c.6 0 1-.4 1-1v-3c0-.9-.7-1.7-1.5-1.9C18.7 10.6 16 10 16 10s-1.3-1.4-2.2-2.3c-.5-.4-1.1-.7-1.8-.7H5c-.6 0-1.1.4-1.4.9l-1.5 2.8C2.1 10.7 2 11.2 2 11.7V16c0 .6.4 1 1 1h2"></path><circle cx="7" cy="17" r="2"></circle><path d="M9 17h6"></path><circle cx="17" cy="17" r="2"></circle></svg>'''
ICON_HEART = '''<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="width:28px;height:28px;"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>'''
ICON_GIFT = '''<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="width:28px;height:28px;"><polyline points="20 12 20 22 4 22 4 12"></polyline><rect x="2" y="7" width="20" height="5"></rect><line x1="12" y1="22" x2="12" y2="7"></line><path d="M12 7H7.5a2.5 2.5 0 0 1 0-5C11 2 12 7 12 7z"></path><path d="M12 7h4.5a2.5 2.5 0 0 0 0-5C13 2 12 7 12 7z"></path></svg>'''
ICON_BANK = '''<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="width:28px;height:28px;"><line x1="3" y1="21" x2="21" y2="21"></line><line x1="3" y1="10" x2="21" y2="10"></line><polyline points="5 6 12 3 19 6"></polyline><line x1="4" y1="10" x2="4" y2="21"></line><line x1="20" y1="10" x2="20" y2="21"></line><line x1="8" y1="14" x2="8" y2="17"></line><line x1="12" y1="14" x2="12" y2="17"></line><line x1="16" y1="14" x2="16" y2="17"></line></svg>'''
ICON_TRENDING = '''<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="width:28px;height:28px;"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline><polyline points="17 6 23 6 23 12"></polyline></svg>'''
ICON_GRAD = '''<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="width:26px;height:26px;"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c0 2 4 3 6 3s6-1 6-3v-5"></path></svg>'''
ICON_USERS = '''<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="width:26px;height:26px;"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>'''
ICON_SHIELD = '''<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="width:26px;height:26px;"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>'''

SVG_HEART_CLIP = '''  <svg width="0" height="0" style="position:absolute;visibility:hidden;">
    <defs>
      <clipPath id="heart-clip" clipPathUnits="objectBoundingBox">
        <path d="M 0.5, 0.95 C 0.45, 0.90, 0.05, 0.65, 0.02, 0.38 C -0.02, 0.18, 0.12, 0.02, 0.30, 0.02 C 0.40, 0.02, 0.46, 0.08, 0.5, 0.16 C 0.54, 0.08, 0.60, 0.02, 0.70, 0.02 C 0.88, 0.02, 1.02, 0.18, 0.98, 0.38 C 0.95, 0.65, 0.55, 0.90, 0.5, 0.95 Z" />
      </clipPath>
    </defs>
  </svg>'''

def get_head(title, description):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="icon" type="image/png" href="assets/image_0.png">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Skip Link for Accessibility -->
  <a href="#main-content" class="skip-link">Skip to main content</a>
'''

def get_header(active="home"):
    return f'''  <!-- Global Header -->
  <header class="site-header" role="banner">
    <div class="w header-container">
      <a href="/" class="brand-link" aria-label="Kandelia Home">
        <img src="assets/image_0.png" alt="Kandelia Logo" width="220" height="48">
      </a>

      <!-- Desktop Navigation Menu -->
      <nav class="main-nav" aria-label="Main Navigation">
        <div class="nav-item">
          <a href="/about" class="nav-link {'active' if active=='about' else ''}">About</a>
        </div>
        <div class="nav-item">
          <a href="/get-help" class="nav-link {'active' if active=='get-help' else ''}">Get Help</a>
        </div>
        <div class="nav-item">
          <a href="/ways-to-give" class="nav-link {'active' if active=='ways-to-give' else ''}">Ways to Give</a>
        </div>
        <div class="nav-item">
          <a href="/stories" class="nav-link {'active' if active=='stories' else ''}">Stories & Impact</a>
        </div>
        <div class="nav-item">
          <a href="/giving" class="nav-link {'active' if active=='giving' else ''}">Giving</a>
        </div>
      </nav>

      <a class="btn btn-coral" href="https://kandelia-bloom.kindful.com/embeds/75568458-194c-4924-8a1b-de2cd76e4f92" target="_blank" rel="noopener">Donate</a>

      <button class="mobile-toggle" id="mobile-menu-toggle" aria-expanded="false" aria-controls="mobile-navigation-drawer">
        Menu <svg class="icon menu-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
      </button>
    </div>

    <!-- Mobile Navigation Drawer -->
    <nav class="mobile-nav-drawer" id="mobile-navigation-drawer" aria-label="Mobile Navigation">
      <a href="/" class="{'active' if active=='home' else ''}">Home</a>
      <a href="/about" class="{'active' if active=='about' else ''}">About</a>
      <a href="/get-help" class="{'active' if active=='get-help' else ''}">Get Help</a>
      <a href="/ways-to-give" class="{'active' if active=='ways-to-give' else ''}">Ways to Give</a>
      <a href="/stories" class="{'active' if active=='stories' else ''}">Stories & Impact</a>
      <a href="/giving" class="{'active' if active=='giving' else ''}">Giving & Impact Tiers</a>
      <a class="btn btn-coral btn-donate" href="https://kandelia-bloom.kindful.com/embeds/75568458-194c-4924-8a1b-de2cd76e4f92" target="_blank" rel="noopener">Donate</a>
    </nav>
  </header>'''

def get_support_banner():
    return '''    <!-- Support Our Work CTA Banner (Restored Community Photo with rounded-2xl) -->
    <section class="section-support-banner" id="support-banner">
      <div class="w">
        <div class="support-banner-card">
          <!-- Left Side Visual: Community Photograph with soft rounded corners (rounded-2xl) -->
          <div class="support-banner-photo-col">
            <div class="support-banner-photo-frame">
              <img src="assets/image_1.jpeg" alt="Warm Kandelia community and refugee families" loading="lazy">
            </div>
          </div>

          <!-- Right Content Block -->
          <div class="support-banner-content-col">
            <div class="support-heading-badge-wrap">
              <h3 style="color:#FFFFFF !important;">Support Our Work</h3>
            </div>
            <p class="support-banner-lead" style="color:rgba(255,255,255,0.92) !important;">
              Together, we can ensure every immigrant and refugee family has the resources, voice, and community to flourish.
            </p>
            <div class="support-banner-action">
              <a class="btn btn-coral btn-lg support-donate-pill-btn" href="https://kandelia-bloom.kindful.com/embeds/75568458-194c-4924-8a1b-de2cd76e4f92" target="_blank" rel="noopener">Support Our Work — Donate Today →</a>
            </div>
          </div>
        </div>
      </div>
    </section>'''

def get_footer():
    return '''  <!-- Global Footer -->
  <footer class="site-footer" id="contact" role="contentinfo">
    <div class="w">
      <div class="footer-grid">
        <div class="footer-brand">
          <div class="footer-logo-wrap">
            <img src="assets/image_0.png" alt="Kandelia Logo" width="220" height="48">
          </div>
          <div class="footer-tagline">
            Removing barriers to immigrant and refugee success.
          </div>
          <div class="footer-contact-info">
            <p>3829B S. Edmunds St. Box 9<br>Seattle, WA 98118</p>
            <p>Phone: 206-760-1573<br>Email: <a href="mailto:help@kandelia.org" style="color:#fff;">help@kandelia.org</a> (Programs) | <a href="mailto:info@kandelia.org" style="color:#fff;">info@kandelia.org</a> (Admin)</p>
            <p>Tax ID: 91-1122532<br><span style="white-space:nowrap;">Registered 501(c)(3) Nonprofit Organization</span></p>
          </div>
          <div class="newsletter-social-icons" style="margin-top:14px;">
            <a href="https://linkedin.com/company/kandelia" target="_blank" rel="noopener" class="social-circle-btn" aria-label="LinkedIn">
              <svg class="icon" viewBox="0 0 24 24" fill="currentColor"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
            </a>
            <a href="https://facebook.com/kandelia" target="_blank" rel="noopener" class="social-circle-btn" aria-label="Facebook">
              <svg class="icon" viewBox="0 0 24 24" fill="currentColor"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg>
            </a>
            <a href="https://instagram.com/kandelia" target="_blank" rel="noopener" class="social-circle-btn" aria-label="Instagram">
              <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
            </a>
          </div>
        </div>

        <div class="footer-col">
          <h4>Explore</h4>
          <ul>
            <li><a href="/about">About Kandelia</a></li>
            <li><a href="/about#history">50-Year Milestones</a></li>
            <li><a href="/about#team">Our Team (Staff & Board)</a></li>
            <li><a href="/about#impact-report">2026 Impact Report</a></li>
            <li><a href="/about#careers">Work With Us (Careers)</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Get Help</h4>
          <ul>
            <li><a href="/get-help#high-school">High School Pathways</a></li>
            <li><a href="/get-help#family">Family & Adult Workshops</a></li>
            <li><a href="/get-help#community">Emergency Relief & Circles</a></li>
            <li><a href="/get-help#eligibility">Check Eligibility</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Ways to Give</h4>
          <ul>
            <li><a href="/giving">Giving & Impact Tiers</a></li>
            <li><a href="/ways-to-give#family-giving">Family & Youth Funds</a></li>
            <li><a href="/giving#monthly-donor">Become a Monthly Donor</a></li>
            <li><a href="https://careasy.org/kandelia" target="_blank" rel="noopener noreferrer">Vehicle Donation (CARS)</a></li>
          </ul>
          <div style="margin-top:20px;">
            <a class="btn btn-coral btn-sm" href="https://kandelia-bloom.kindful.com/embeds/75568458-194c-4924-8a1b-de2cd76e4f92" target="_blank" rel="noopener">Donate</a>
          </div>
        </div>
      </div>

      <div class="footer-bottom">
        <div>
          &copy; <span id="copyright-year">2026</span> Kandelia. Registered 501(c)(3) non-profit organization. Tax ID: 91-1122532.
        </div>
        <div class="footer-bottom-links">
          <a href="#">Privacy Policy</a>
          <a href="#">Terms of Use</a>
          <a href="/about#impact-report">Financial Transparency</a>
        </div>
      </div>
    </div>
  </footer>
  <script src="script.js"></script>
</body>
</html>'''

# ==============================================================================
# 1. GENERATE index.html (HOME PAGE - TRIMMED HIGH-IMPACT TEASERS)
# ==============================================================================
print("Generating index.html...")
home_html = get_head("Kandelia | 50 Years of Immigrant & Refugee Belonging", "Kandelia removes barriers to immigrant and refugee success through holistic education, family navigation, and community equity.")
home_html += get_header("home")
home_html += f'''
  <main id="main-content">
    {SVG_HEART_CLIP}

    <!-- HERO SECTION -->
    <section class="section-hero" id="hero">
      <div class="w hero-grid">
        <div class="hero-content">
          <span class="badge badge-sage">50 Years of Immigrant & Refugee Belonging</span>
          <h1 class="hero-title">
            Removing Barriers to Immigrant and Refugee Success
          </h1>
          <p class="hero-lead">
            For five decades, Kandelia has partnered with newly arrived youth and families across King County to provide holistic education, systemic navigation, and culturally responsive community pathways.
          </p>

          <div class="hero-actions">
            <a class="btn btn-primary btn-lg" href="/get-help">Get Help →</a>
            <a class="btn btn-outline btn-lg" href="/giving">Support Our Work</a>
          </div>

          <!-- Trust & Impact Snapshot (2x2 Grid Layout: 2 items per row, 2 rows) -->
          <div class="hero-stats-2x2-grid">
            <div class="hero-stat-item">
              <span class="hero-stat-number">570+</span> <span class="hero-stat-label">Served Yearly</span>
            </div>
            <div class="hero-stat-item">
              <span class="hero-stat-number">95%</span> <span class="hero-stat-label">Graduation Rate</span>
            </div>
            <div class="hero-stat-item">
              <span class="hero-stat-number">22</span> <span class="hero-stat-label">Languages Spoken</span>
            </div>
            <div class="hero-stat-item">
              <span class="hero-stat-number">$240K+</span> <span class="hero-stat-label">Direct Relief</span>
            </div>
          </div>
        </div>

        <div class="hero-media-wrapper">
          <div class="hero-organic-composition">
            <!-- Decorative Scalloped / Dashed Ring Backdrop -->
            <div class="hero-scallop-ring" aria-hidden="true"></div>

            <!-- Floating Sticker Badge Top-Right (50 Years • Seattle Roots) -->
            <div class="floating-sticker top-right">50 Years • Seattle Roots</div>

            <!-- Main Image Frame with Organic Curve (Image 1) -->
            <div class="hero-image-frame-enhanced">
              <img src="assets/image_1.jpeg" alt="Two smiling Kandelia students outside their school in Seattle" class="hero-main-img">
            </div>

            <!-- Floating Rounded Stat Card Bottom (95% Graduation Rate) -->
            <div class="floating-stat-card">
              <div class="floating-stat-badge" style="background:#E3F2D4; width:44px; height:44px; border-radius:12px; display:flex; align-items:center; justify-content:center;">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#2A6615" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path></svg>
              </div>
              <div class="floating-stat-text">
                <b style="color:var(--navy); font-size:1.02rem; display:block; line-height:1.2;">95% Graduation Rate</b>
                <span style="color:var(--text-muted); font-size:0.82rem; display:block; margin-top:2px;">Serving 570+ Students & Families</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 50TH ANNIVERSARY CELEBRATION (MAY 2027) -->
    <section class="event-banner-section" id="milestone-gala">
      <div class="w">
        <div class="event-card">
          <div class="event-2col-grid">
            <!-- Left Column: Layered Seattle skyline image with dashed cyan outline (Image 2) -->
            <div class="event-image-col">
              <div class="event-layered-image-wrap">
                <div class="event-image-backing" aria-hidden="true"></div>
                <div class="event-image-frame">
                  <img src="assets/image_2.jpeg" alt="Kandelia group looking out over the Seattle skyline" loading="lazy">
                </div>
                <div class="floating-sticker event-gala-pill">Milestone Gala</div>
              </div>
            </div>

            <!-- Right Column: Event Content & CTAs -->
            <div class="event-content-col">
              <span class="event-milestone-pill">
                Milestone Celebration • 1978–2028
              </span>
              <h2 class="event-title">
                Celebrate 50 years of Kandelia with us in May 2027
              </h2>
              <p class="event-desc">
                Join our landmark 50th anniversary celebration and "Sip & Celebrate" gala at the Seattle Center Pavilion. Honoring five decades of immigrant and refugee leadership, student triumphs, and community solidarity.
              </p>

              <div class="event-meta-row">
                <span class="event-meta-pill">{ICON_CALENDAR}Friday, May 14, 2027</span>
                <span class="event-meta-pill">{ICON_MAP_PIN}Seattle Center Pavilion</span>
                <span class="event-meta-pill">{ICON_CLOCK}6:00 PM PST</span>
              </div>

              <div class="event-cta-row">
                <a class="event-ticket-btn" href="https://kandelia-bloom.kindful.com/embeds/75568458-194c-4924-8a1b-de2cd76e4f92" target="_blank" rel="noopener">
                  Get Tickets →
                </a>
                <a class="event-sponsor-btn" href="mailto:gala@kandelia.org?subject=Become a Sponsor for 50th Anniversary Gala">
                  Become a Sponsor
                </a>
              </div>
            </div>
          </div>

          <!-- Sponsor Row -->
          <div class="event-sponsors-section">
            <div class="event-sponsors-label">Thank you to our community sponsors:</div>
            <div class="event-sponsors-boxes">
              <div class="sponsor-dashed-box">Seattle Foundation</div>
              <div class="sponsor-dashed-box">Rainier Valley Corp</div>
              <div class="sponsor-dashed-box">King County Best Starts</div>
              <div class="sponsor-dashed-box">Boeing Community Fund</div>
              <div class="sponsor-dashed-box">Bill & Melinda Gates Partner</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- WHO WE HELP SECTION (EQUAL-HEIGHT BALANCED CARDS) -->
    <section class="section-who-we-help" id="who-we-help" style="padding:80px 0;">
      <div class="w">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 48px;">
          <span class="badge badge-teal" style="margin-bottom:12px;">Holistic Pathways</span>
          <h2>Who We Support Across King County</h2>
          <p class="lead">From recently arrived high school newcomers to multi-generational immigrant households, we meet community members with dignity, cultural responsiveness, and barrier-free resources.</p>
        </div>

        <div class="who-we-help-grid">
          <!-- Card 1: Youth -->
          <div class="who-card-equal">
            <div class="card-icon-wrap" style="background:#F0FAF9; color:#14857F;">
              {ICON_GRAD}
            </div>
            <h3>Youth Success & Education</h3>
            <p class="card-desc">
              Academic tutoring, credit recovery, bilingual homework clubs, and post-secondary guidance tailored for immigrant and refugee high school students navigating American schools.
            </p>
            <div class="card-action">
              <a href="/get-help#high-school" class="card-link-btn">
                Explore Youth Programs {ICON_CHEVRON}
              </a>
            </div>
          </div>

          <!-- Card 2: Family -->
          <div class="who-card-equal">
            <div class="card-icon-wrap" style="background:#F4FBE8; color:#2A6615;">
              {ICON_USERS}
            </div>
            <h3>Family Navigation & Digital Skills</h3>
            <p class="card-desc">
              Bilingual computer labs, internet safety, school district portal orientation, and direct housing & utility navigation empowering adult family members and caregivers.
            </p>
            <div class="card-action">
              <a href="/get-help#family" class="card-link-btn">
                Explore Family Programs {ICON_CHEVRON}
              </a>
            </div>
          </div>

          <!-- Card 3: Community -->
          <div class="who-card-equal">
            <div class="card-icon-wrap" style="background:#ECEEFF; color:#1F22AA;">
              {ICON_SHIELD}
            </div>
            <h3>Community Resilience & Mutual Aid</h3>
            <p class="card-desc">
              Emergency cash assistance, culturally affirming healing circles, and systemic advocacy ensuring families can flourish without compromising their heritage or values.
            </p>
            <div class="card-action">
              <a href="/get-help#community" class="card-link-btn">
                Explore Community Circles {ICON_CHEVRON}
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ABOUT KANDELIA OVERVIEW TEASER -->
    <section class="section-about-teaser" style="padding:80px 0; background-color:#FFFFFF;">
      <div class="w" style="max-width:980px; margin:0 auto; text-align:center;">
        <span class="badge badge-sage" style="margin-bottom:14px;">Our Mission & Purpose</span>
        <blockquote style="font-size:clamp(1.35rem, 2.5vw, 1.85rem); line-height:1.45; color:var(--navy); font-weight:500; margin:0 0 24px; border:none; padding:0;">
          "We remove barriers to opportunities so immigrant and refugee communities can flourish without compromising values, heritage or ethnicity."
        </blockquote>
        <p style="font-size:1.08rem; color:var(--text-body); max-width:760px; margin:0 auto 32px; line-height:1.65;">
          Guided by our core values of Inclusion, Heart, Equity, Relationships, and Excellence, Kandelia has grown from a grassroots refugee mutual aid effort in 1978 to a regional pillar of community leadership.
        </p>
        <div style="display:flex; justify-content:center; gap:16px; flex-wrap:wrap;">
          <a class="btn btn-outline" href="/about">Discover Our 50-Year Story & Team →</a>
          <a class="btn btn-primary" href="/about#careers">Work With Us</a>
        </div>
      </div>
    </section>

    <!-- STORIES & IMPACT PREVIEW (CLEAN 1:1 SQUARE BORDERLESS IMAGES) -->
    <section class="section-stories-teaser" style="padding:80px 0; background-color:#F0F2FA;">
      <div class="w">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 40px;">
          <span class="badge badge-teal" style="margin-bottom:12px;">Real Voices</span>
          <h2>Stories of Resilience & Belonging</h2>
          <p class="lead">Every newcomer family has a journey of courage, strength, and aspiration. Here are just a few of our community members thriving across Seattle.</p>
        </div>

        <div class="story-square-grid">
          <!-- Story 1: Patrick -->
          <div class="story-square-card">
            <div class="story-square-img-wrap">
              <img src="assets/image_5.jpeg" alt="Patrick's Story" class="story-img-square" loading="lazy">
            </div>
            <div class="story-square-body">
              <span class="badge badge-sage" style="width:fit-content; margin-bottom:6px;">Youth Alumnus</span>
              <h3>Patrick's Story</h3>
              <p>"Kandelia gave me mentors who understood my culture and believed in my dreams. Today, I'm completing college and giving back."</p>
              <a href="/stories" class="card-link-btn" style="font-weight:700; color:var(--navy);">Read Full Story →</a>
            </div>
          </div>

          <!-- Story 2: Sunflower & Tulip -->
          <div class="story-square-card">
            <div class="story-square-img-wrap">
              <img src="assets/image_6.jpeg" alt="Sunflower & Tulip's Story" class="story-img-square" loading="lazy">
            </div>
            <div class="story-square-body">
              <span class="badge badge-coral" style="width:fit-content; margin-bottom:6px;">Sisters & Scholars</span>
              <h3>Sunflower & Tulip</h3>
              <p>"In the after-school program, we found more than homework help—we found a safe community where we belonged from day one."</p>
              <a href="/stories" class="card-link-btn" style="font-weight:700; color:var(--navy);">Read Full Story →</a>
            </div>
          </div>
        </div>

        <div style="text-align:center; margin-top:36px;">
          <a class="btn btn-outline" href="/stories">Read All Community Stories & Reports →</a>
        </div>
      </div>
    </section>

    <!-- WAYS TO GIVE TEASER -->
    <section class="section-ways-teaser" style="padding:80px 0; background-color:#FFFFFF;">
      <div class="w">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 40px;">
          <span class="badge badge-green" style="margin-bottom:12px;">Meaningful Impact</span>
          <h2>Ways to Support Our Community</h2>
          <p class="lead">Whether through monthly giving, family support funds, or vehicle donations, your partnership fuels brighter futures for newcomer families.</p>
        </div>

        <div class="ways-photo-grid">
          <!-- Family Fund Card with Photo -->
          <div class="way-photo-card">
            <div class="way-photo-wrap">
              <img src="assets/image_4.jpeg" alt="Kandelia family gathering in a collaborative workshop" loading="lazy">
            </div>
            <div class="way-photo-body">
              <span class="badge badge-teal" style="width:fit-content; margin-bottom:6px;">Family Care</span>
              <h3>Family Flourishing Fund</h3>
              <p>Directly support adult digital literacy classes, family rental assistance, and bilingual school navigation.</p>
              <div class="way-photo-action">
                <a href="/ways-to-give#family-giving" class="btn btn-outline btn-sm">Support Families →</a>
              </div>
            </div>
          </div>

          <!-- Youth Fund Card with Photo -->
          <div class="way-photo-card">
            <div class="way-photo-wrap">
              <img src="assets/image_3.jpeg" alt="Kandelia high school students smiling in a classroom" loading="lazy">
            </div>
            <div class="way-photo-body">
              <span class="badge badge-sage" style="width:fit-content; margin-bottom:6px;">Education</span>
              <h3>Youth Mentorship & Education</h3>
              <p>Fund after-school tutoring, high school graduation pathways, and paid youth leadership internships.</p>
              <div class="way-photo-action">
                <a href="/ways-to-give#youth-giving" class="btn btn-outline btn-sm">Support Youth →</a>
              </div>
            </div>
          </div>

          <!-- Vehicle Donation Card with SVG Icon -->
          <div class="way-photo-card" style="border:1.5px solid rgba(42,210,201,0.35);">
            <div class="way-photo-body" style="padding-top:28px;">
              <div style="color:var(--teal); margin-bottom:14px;">
                {ICON_CAR}
              </div>
              <span class="badge badge-blue" style="width:fit-content; margin-bottom:6px;">Vehicle Donation</span>
              <h3>Donate Your Vehicle (CARS)</h3>
              <p style="font-size:0.92rem; line-height:1.55;">
                The proceeds from your vehicle will directly benefit Kandelia's programs. Both Kandelia and CARS are 501(c)(3) nonprofit organizations, and donations through this program are tax deductible. Click the link below to fuel brighter futures!
              </p>
              <div class="way-photo-action">
                <a href="https://careasy.org/kandelia" target="_blank" rel="noopener noreferrer" class="btn btn-coral btn-sm">
                  CARS Donation →
                </a>
              </div>
            </div>
          </div>
        </div>

        <div style="text-align:center; margin-top:36px;">
          <a class="btn btn-outline" href="/ways-to-give">Explore All Ways to Give & Donate →</a>
        </div>
      </div>
    </section>

    {get_support_banner()}

    <!-- STAY IN THE LOOP (UPDATED NEWSLETTER SIGNUP FORM) -->
    <section class="section-newsletter" id="newsletter" style="padding:70px 0; background-color:#F0FAF9; border-top:1px solid rgba(42,210,201,0.2);">
      <div class="w" style="max-width:920px; margin:0 auto;">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 32px; text-align:center; display:flex; flex-direction:column; align-items:center;">
          <span class="badge badge-blue" style="margin-bottom:12px;">Stay Connected</span>
          <h2 style="font-size:clamp(1.8rem, 3.2vw, 2.4rem); color:var(--navy); margin-bottom:10px; text-align:center; width:100%;">
            Stay in the Loop with Kandelia
          </h2>
          <p class="lead" style="font-size:1.05rem; color:var(--text-body); max-width:640px; margin:0 auto; line-height:1.6; text-align:center;">
            Receive updates on program outcomes, community stories, and event invitations a few times a year. No spam, ever.
          </p>
        </div>

        <form id="newsletter-signup-form" novalidate>
          <div class="newsletter-form-grid">
            <div>
              <label for="newsletter-fname" class="sr-only">First Name</label>
              <input class="newsletter-input-field" id="newsletter-fname" name="FNAME" type="text" placeholder="First Name" required>
            </div>
            <div>
              <label for="newsletter-lname" class="sr-only">Last Name</label>
              <input class="newsletter-input-field" id="newsletter-lname" name="LNAME" type="text" placeholder="Last Name" required>
            </div>
            <div>
              <label for="newsletter-email" class="sr-only">Email Address</label>
              <input class="newsletter-input-field" id="newsletter-email" name="EMAIL" type="email" placeholder="Email Address" required>
            </div>
            <div>
              <button class="newsletter-submit-btn" type="submit">
                Subscribe
              </button>
            </div>
          </div>
          <div id="newsletter-feedback-msg" class="newsletter-feedback" role="alert" style="text-align:center; margin-top:12px;"></div>
        </form>
      </div>
    </section>
  </main>
'''
home_html += get_footer()

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(home_html)
print("index.html written successfully!")


# ==============================================================================
# 2. GENERATE about.html (ABOUT US, MISSION, HISTORY, STAFF, BOARD, REPORT, CAREERS)
# ==============================================================================
print("Generating about.html...")
about_html = get_head("About Kandelia | 50 Years of Immigrant & Refugee Belonging", "Learn about Kandelia's 50-year history, mission platform, staff leadership, board of directors, and career opportunities in Seattle.")
about_html += get_header("about")
about_html += f'''
  <main id="main-content">
    {SVG_HEART_CLIP}

    <!-- PAGE HERO -->
    <section class="inner-hero" id="mission">
      <div class="w inner-hero-content">
        <span class="badge badge-sage">Our History & Leadership</span>
        <h1 class="inner-hero-title">About Kandelia</h1>
        <p class="inner-hero-lead">
          "We remove barriers to opportunities so immigrant and refugee communities can flourish without compromising values, heritage or ethnicity."
        </p>
      </div>
    </section>

    <!-- BRAND VALUES PLATFORM (Brand Guide Page 3) -->
    <section style="padding:70px 0; background-color:#FFFFFF;">
      <div class="w">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 40px;">
          <span class="badge badge-teal" style="margin-bottom:12px;">Guiding Principles</span>
          <h2>Our Core Values</h2>
          <p class="lead">These values drive our daily culture, hiring practices, community advocacy, and strategic decisions.</p>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:24px;">
          <div style="background:#F0FAF9; border-radius:18px; padding:28px 24px; border:1px solid rgba(42,210,201,0.25);">
            <h3 style="font-size:1.25rem; color:var(--navy); margin-bottom:10px;">Inclusion</h3>
            <p style="font-size:0.96rem; color:var(--text-body); line-height:1.6; margin:0;">
              We embrace diversity and believe all people have value and the right to belong. We commit to active listening and questioning assumptions.
            </p>
          </div>
          <div style="background:#FEECEE; border-radius:18px; padding:28px 24px; border:1px solid rgba(244,54,76,0.22);">
            <h3 style="font-size:1.25rem; color:var(--coral); margin-bottom:10px;">Heart</h3>
            <p style="font-size:0.96rem; color:var(--text-body); line-height:1.6; margin:0;">
              We measure our success by the real difference we make in people's lives. We act with care, empathy, kindness, and fun along the way.
            </p>
          </div>
          <div style="background:#F4FBE8; border-radius:18px; padding:28px 24px; border:1px solid rgba(151,215,0,0.25);">
            <h3 style="font-size:1.25rem; color:#2A6615; margin-bottom:10px;">Equity</h3>
            <p style="font-size:0.96rem; color:var(--text-body); line-height:1.6; margin:0;">
              We believe in just and fair inclusion, identifying inequities and taking proactive responsibility for addressing them.
            </p>
          </div>
          <div style="background:#ECEEFF; border-radius:18px; padding:28px 24px; border:1px solid rgba(30,34,170,0.20);">
            <h3 style="font-size:1.25rem; color:var(--navy); margin-bottom:10px;">Relationships</h3>
            <p style="font-size:0.96rem; color:var(--text-body); line-height:1.6; margin:0;">
              We build strong connections with each other, partners, and the communities we serve in the spirit of genuine collaboration.
            </p>
          </div>
          <div style="background:#F0FAF9; border-radius:18px; padding:28px 24px; border:1px solid rgba(42,210,201,0.25);">
            <h3 style="font-size:1.25rem; color:#14857F; margin-bottom:10px;">Excellence</h3>
            <p style="font-size:0.96rem; color:var(--text-body); line-height:1.6; margin:0;">
              We strive to be the best we can be in all we do, applying discipline, organization, and professionalism to our daily work.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- 50-YEAR TIMELINE -->
    <section class="section-timeline" id="history" style="padding:80px 0; background-color:#F0F2FA;">
      <div class="w">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 48px;">
          <span class="badge badge-sage" style="margin-bottom:12px;">Five Decades</span>
          <h2>Milestones of Belonging (1978–2028)</h2>
          <p class="lead">Fifty years of immigrant and refugee leadership in South Seattle and across King County.</p>
        </div>

        <div class="timeline-container" style="max-width:880px; margin:0 auto;">
          <div class="timeline-item">
            <div class="timeline-shape-badge">1978</div>
            <div class="timeline-content">
              <h3>Founded in Mutual Aid</h3>
              <p>Established as the Southeast Asian Refugee Support network to provide direct translation, emergency relief, and community orientation for families arriving in Seattle.</p>
            </div>
          </div>

          <div class="timeline-item">
            <div class="timeline-shape-badge">1995</div>
            <div class="timeline-content">
              <h3>Seattle Public Schools Partnership</h3>
              <p>Formed formal after-school tutoring partnerships inside high schools, ensuring bilingual homework help and credit recovery for newly arrived ELL students.</p>
            </div>
          </div>

          <div class="timeline-item">
            <div class="timeline-shape-badge">2000</div>
            <div class="timeline-content">
              <h3>Pan-Immigrant & Refugee Expansion</h3>
              <p>Broadened organizational charter to welcome newcomer families from East Africa, Latin America, the Middle East, and Eastern Europe.</p>
            </div>
          </div>

          <div class="timeline-item">
            <div class="timeline-shape-badge">2012</div>
            <div class="timeline-content">
              <h3>Whole-Family Wraparound Services</h3>
              <p>Launched adult digital literacy labs, job readiness workshops, and youth leadership summer programs to support multi-generational flourishing.</p>
            </div>
          </div>

          <div class="timeline-item">
            <div class="timeline-shape-badge">2020</div>
            <div class="timeline-content">
              <h3>Direct Emergency Relief & Digital Access</h3>
              <p>Rapidly mobilized over $240,000 in direct emergency assistance, distributed hundreds of cellular-connected laptops, and established virtual support circles.</p>
            </div>
          </div>

          <div class="timeline-item">
            <div class="timeline-shape-badge">2027</div>
            <div class="timeline-content">
              <h3>50th Anniversary Gala Celebration</h3>
              <p>Gathering five decades of alumni, families, educators, and community partners at the Seattle Center Pavilion for our landmark milestone celebration.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- STAFF LEADERSHIP ROSTER -->
    <section class="section-staff" id="team" style="padding:80px 0; background-color:#FFFFFF;">
      <div class="w">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 48px;">
          <span class="badge badge-teal" style="margin-bottom:12px;">Our Team</span>
          <h2>Staff Leadership</h2>
          <p class="lead">Experienced educators, youth advocates, and community organizers with deep roots in King County.</p>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:28px;">
'''

for staff in site_data.STAFF_LEADERSHIP:
    about_html += f'''          <div class="staff-card" style="background:#F0FAF9; border-radius:20px; padding:28px; border:1px solid rgba(42,210,201,0.25);">
            <h3 style="font-size:1.3rem; color:var(--navy); margin-bottom:4px;">{staff['name']}</h3>
            <div style="font-size:0.95rem; font-weight:700; color:var(--teal-dark); margin-bottom:6px;">{staff['role']}</div>
            <div style="font-size:0.85rem; color:var(--text-muted); margin-bottom:12px;">Languages: {staff['languages']}</div>
            <div style="font-size:0.9rem; color:var(--text-body); line-height:1.5;">{staff['bio']}</div>
          </div>\n'''

about_html += '''        </div>
      </div>
    </section>

    <!-- BOARD OF DIRECTORS -->
    <section class="section-board" id="board" style="padding:80px 0; background-color:#F0F2FA;">
      <div class="w">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 48px;">
          <span class="badge badge-sage" style="margin-bottom:12px;">Governance & Stewardship</span>
          <h2>Our Board of Directors</h2>
          <p class="lead">Passionate educators, legal advocates, finance executives, and alumni providing strategic fiduciary governance.</p>
        </div>

        <div class="board-grid">
'''

for board in site_data.BOARD_MEMBERS:
    about_html += f'''          <div class="board-card" style="background:#FFFFFF; border-radius:18px; padding:24px; border:1px solid rgba(30,34,170,0.12); box-shadow:0 4px 14px rgba(30,34,170,0.03);">
            <div style="width:48px; height:48px; border-radius:50%; background:#ECEEFF; color:var(--navy); display:flex; align-items:center; justify-content:center; font-weight:700; font-size:1.1rem; margin-bottom:14px;">
              {board['initials']}
            </div>
            <h3 style="font-size:1.2rem; color:var(--navy); margin-bottom:4px;">{board['name']}</h3>
            <div style="font-size:0.9rem; font-weight:700; color:var(--teal-dark); margin-bottom:8px;">{board['role']}</div>
            <div style="font-size:0.85rem; color:var(--text-muted); line-height:1.45;">{board.get('tenure', '')}</div>
          </div>\n'''

about_html += '''        </div>
      </div>
    </section>

    <!-- 2026 ANNUAL REPORT -->
    <section class="section-report" id="impact-report" style="padding:80px 0; background-color:#FFFFFF;">
      <div class="w">
        <div class="pinned-report-card">
          <div class="report-cover-box" style="background:#1F22AA; border-radius:20px; padding:32px 24px; color:#FFFFFF; display:flex; flex-direction:column; justify-content:space-between; min-height:240px; box-shadow:0 10px 30px rgba(31,34,170,0.15);">
            <div>
              <span class="badge" style="margin-bottom:12px; border:none; background:rgba(255,255,255,0.2); color:#FFFFFF; font-size:0.75rem; text-transform:uppercase; letter-spacing:0.05em; padding:4px 12px; border-radius:20px; display:inline-block;">Annual Report</span>
              <div style="font-size:1.6rem; font-weight:700; line-height:1.2; color:#FFFFFF; margin-top:8px;">2026 Impact Report</div>
            </div>
            <div style="font-size:1.05rem; font-weight:700; color:rgba(255,255,255,0.9); letter-spacing:0.02em;">Kandelia</div>
          </div>

          <div class="report-details-body">
            <span class="badge badge-sage" style="margin-bottom:10px; background:#E6FAF9; color:#14857F; border-color:rgba(42,210,201,0.3);">Featured Publication</span>
            <h3>Deep Roots, Lasting Flourish</h3>
            <p>Explore our comprehensive evaluation of student graduation rates, family economic mobility, and direct assistance distribution across King County.</p>
            <ul class="report-datapoints">
              <li><svg class="icon check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true" style="width:18px;height:18px;margin-right:8px;vertical-align:-2px;"><polyline points="20 6 9 17 4 12"></polyline></svg><strong>570+ Newcomers</strong> guided through academic and civic pathways</li>
              <li><svg class="icon check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true" style="width:18px;height:18px;margin-right:8px;vertical-align:-2px;"><polyline points="20 6 9 17 4 12"></polyline></svg><strong>95% Graduation Rate</strong> among cohort high school seniors</li>
              <li><svg class="icon check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true" style="width:18px;height:18px;margin-right:8px;vertical-align:-2px;"><polyline points="20 6 9 17 4 12"></polyline></svg><strong>$240,000+ Distributed</strong> in direct emergency family relief & rental aid</li>
              <li><svg class="icon check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true" style="width:18px;height:18px;margin-right:8px;vertical-align:-2px;"><polyline points="20 6 9 17 4 12"></polyline></svg><strong>1,200+ Hours</strong> of bilingual adult digital literacy training delivered</li>
            </ul>
            <div style="display:flex; gap:14px; flex-wrap:wrap;">
              <a class="btn btn-primary" href="#contact">Read the 2026 Impact Report →</a>
              <a class="btn btn-outline" href="mailto:info@kandelia.org?subject=Request 2026 Impact Report PDF">Request PDF Copy</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CAREERS & LEADERSHIP (WORK WITH US) -->
    <section class="section-careers" id="careers" style="padding:80px 0; background-color:#F0FAF9; border-top:1px solid rgba(42,210,201,0.2);">
      <div class="w">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 48px;">
          <span class="badge badge-blue" style="margin-bottom:12px;">Join Our Team</span>
          <h2>Work With Us</h2>
          <p class="lead">Build meaningful careers advancing equity, youth belonging, and refugee solidarity across King County.</p>
        </div>

        <div style="display:flex; flex-direction:column; gap:20px; max-width:920px; margin:0 auto;">
'''

for cat, job_list in site_data.CAREERS.items():
    for job in job_list:
        about_html += f'''          <div class="job-card" style="background:#FFFFFF; border-radius:18px; padding:28px 32px; border:1px solid rgba(42,210,201,0.25); box-shadow:0 4px 14px rgba(30,34,170,0.03);">
            <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:12px; margin-bottom:12px;">
              <div>
                <h3 style="font-size:1.35rem; color:var(--navy); margin-bottom:6px;">{job['title']}</h3>
                <div style="display:flex; gap:10px; flex-wrap:wrap;">
                  <span class="badge badge-sage">{job['type']}</span>
                  <span class="badge">{job['location']}</span>
                  <span class="badge badge-blue">{job['compensation']}</span>
                </div>
              </div>
              <a href="mailto:careers@kandelia.org?subject=Application for {job['title']}" class="btn btn-outline btn-sm">Apply Now →</a>
            </div>
            <p style="font-size:0.98rem; color:var(--text-body); line-height:1.6; margin-bottom:10px;">{job['description']}</p>
            <div class="job-qualifications" style="font-size:0.92rem; color:var(--text-dark); background:#F0F2FA; border-left:3px solid var(--navy); padding:8px 14px; border-radius:0 8px 8px 0; line-height:1.5;">
              <strong>Qualifications:</strong> {job['qualifications']}
            </div>
          </div>\n'''

about_html += f'''        </div>
      </div>
    </section>

    {get_support_banner()}
  </main>
'''
about_html += get_footer()

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(about_html)
print("about.html written successfully!")


# ==============================================================================
# 3. GENERATE get-help.html (GET HELP - FULL PROGRAMS WITH DISTINCT TOP PHOTOS)
# ==============================================================================
print("Generating get-help.html...")
help_html = get_head("Get Help & Programs | Kandelia", "Explore Kandelia's culturally responsive youth, family, digital literacy, and emergency relief programs in King County.")
help_html += get_header("get-help")
help_html += f'''
  <main id="main-content">
    {SVG_HEART_CLIP}

    <!-- PAGE HERO -->
    <section class="inner-hero" id="overview">
      <div class="w inner-hero-content">
        <span class="badge badge-teal">Community Support</span>
        <h1 class="inner-hero-title">Get Support at Kandelia</h1>
        <p class="inner-hero-lead">
          We partner with newly arrived immigrant and refugee youth, adult learners, and families across King County with free, culturally affirming educational, digital, and emergency navigation programs.
        </p>
      </div>
    </section>

    <!-- 4 PROGRAM CARDS EACH WITH DISTINCT TOP PHOTOGRAPH -->
    <section style="padding:80px 0; background-color:#FFFFFF;">
      <div class="w">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 40px;">
          <span class="badge badge-sage" style="margin-bottom:12px;">Our Four Pillars</span>
          <h2>Comprehensive Support Programs</h2>
          <p class="lead">Every program is designed around active listening, language access, and whole-family empowerment.</p>
        </div>

        <div class="program-cards-grid">
          <!-- Program 1: High School Pathways (Photo: Classroom Students) -->
          <div class="program-photo-card" id="high-school">
            <div class="program-photo-wrap">
              <img src="assets/image_3.jpeg" alt="Kandelia high school students smiling in a classroom" loading="lazy">
            </div>
            <div class="program-card-body">
              <span class="badge badge-sage" style="width:fit-content;">Ages 14–21</span>
              <h3>High School Pathways & Youth Leadership</h3>
              <p>Dedicated after-school tutoring, ELL credit recovery, bilingual homework clubs, and post-secondary planning inside King County public high schools.</p>
              <ul class="program-feature-list">
                <li>{ICON_CHECK} 1-on-1 academic mentoring & English conversation practice</li>
                <li>{ICON_CHECK} Graduation audit & college / vocational application support</li>
                <li>{ICON_CHECK} Paid summer youth leadership stipends and community projects</li>
              </ul>
              <div class="program-card-footer">
                <a href="#eligibility" class="btn btn-primary btn-sm">Enroll Student →</a>
                <span style="font-size:0.9rem; color:var(--text-muted);">Free for public school students</span>
              </div>
            </div>
          </div>

          <!-- Program 2: Family Digital Workshops (Photo: Family Gathering) -->
          <div class="program-photo-card" id="family">
            <div class="program-photo-wrap">
              <img src="assets/image_4.jpeg" alt="Kandelia family gathering in a collaborative workshop" loading="lazy">
            </div>
            <div class="program-card-body">
              <span class="badge badge-teal" style="width:fit-content;">Parents & Adults</span>
              <h3>Family Digital Literacy & Tech Navigation</h3>
              <p>Hands-on computer workshops designed for adult caregivers to navigate school district portals (The Source), email, digital banking, and job applications.</p>
              <ul class="program-feature-list">
                <li>{ICON_CHECK} Free Wi-Fi hotspots and subsidized home computer setups</li>
                <li>{ICON_CHECK} Multilingual adult ESL cohorts in evening and Saturday sessions</li>
                <li>{ICON_CHECK} Internet safety, parent advocacy, and healthcare navigation</li>
              </ul>
              <div class="program-card-footer">
                <a href="#eligibility" class="btn btn-primary btn-sm">Join Family Workshop →</a>
                <span style="font-size:0.9rem; color:var(--text-muted);">Bilingual instructors</span>
              </div>
            </div>
          </div>

          <!-- Program 3: Emergency Relief (Photo: Mutual Aid / Community) -->
          <div class="program-photo-card" id="community">
            <div class="program-photo-wrap">
              <img src="assets/image_9.jpeg" alt="Community partners collaborating at Kandelia" loading="lazy">
            </div>
            <div class="program-card-body">
              <span class="badge badge-coral" style="width:fit-content;">Direct Aid</span>
              <h3>Emergency Relief & Housing Stabilization</h3>
              <p>Rapid, barrier-free direct cash assistance, emergency rental relief, and grocery support helping families maintain stability during unexpected hardship.</p>
              <ul class="program-feature-list">
                <li>{ICON_CHECK} Over $240,000 disbursed directly to local newcomer households</li>
                <li>{ICON_CHECK} Eviction prevention, utility assistance, and winter clothing aid</li>
                <li>{ICON_CHECK} Confidential referral coordination with no documentation barriers</li>
              </ul>
              <div class="program-card-footer">
                <a href="#eligibility" class="btn btn-primary btn-sm">Request Relief Aid →</a>
                <span style="font-size:0.9rem; color:var(--text-muted);">Confidential intake</span>
              </div>
            </div>
          </div>

          <!-- Program 4: Mental Health & Healing Circles (Photo: Youth Group) -->
          <div class="program-photo-card" id="circles">
            <div class="program-photo-wrap">
              <img src="assets/image_1.jpeg" alt="Two smiling Kandelia students outside their school in Seattle" loading="lazy">
            </div>
            <div class="program-card-body">
              <span class="badge badge-blue" style="width:fit-content;">Wellness & Voice</span>
              <h3>Healing Circles & Cultural Affirmation</h3>
              <p>Safe, supportive community circles where youth and caregivers explore identity, navigate resettlement stress, and celebrate cultural traditions together.</p>
              <ul class="program-feature-list">
                <li>{ICON_CHECK} Culturally responsive peer mentoring and storytelling spaces</li>
                <li>{ICON_CHECK} Creative arts, cultural celebrations, and civic advocacy</li>
                <li>{ICON_CHECK} Connection to licensed trauma-informed multilingual therapists</li>
              </ul>
              <div class="program-card-footer">
                <a href="#eligibility" class="btn btn-primary btn-sm">Join a Healing Circle →</a>
                <span style="font-size:0.9rem; color:var(--text-muted);">Warm, welcoming spaces</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ELIGIBILITY & INTAKE SECTION -->
    <section class="section-eligibility" id="eligibility" style="padding:80px 0; background-color:#F0FAF9; border-top:1px solid rgba(42,210,201,0.2);">
      <div class="w" style="max-width:880px; margin:0 auto;">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 36px; text-align:center; display:flex; flex-direction:column; align-items:center;">
          <span class="badge badge-blue" style="margin-bottom:12px;">Simple & Barrier-Free</span>
          <h2>Program Eligibility Guidelines</h2>
          <p class="lead" style="text-align:center; margin:0 auto;">All Kandelia programs are 100% free of charge. We warmly welcome immigrants, refugees, asylees, and first-generation families.</p>
        </div>

        <div style="background:#FFFFFF; border-radius:24px; padding:36px 40px; border:1px solid rgba(42,210,201,0.25); box-shadow:0 6px 20px rgba(30,34,170,0.04);">
          <h3 style="font-size:1.35rem; color:var(--navy); margin-bottom:14px;">You are eligible for our programs if:</h3>
          <ul style="list-style-type:disc; padding-left:24px; margin-bottom:24px; font-size:1.02rem; color:var(--text-body); line-height:1.7;">
            <li>You or a family member are an immigrant, refugee, asylee, or humanitarian parolee residing in King County.</li>
            <li>For youth programs: You are between the ages of 14 and 21 and enrolled in a King County middle or high school.</li>
            <li>For adult workshops: You are a parent, caregiver, or adult seeking English language or digital literacy skills.</li>
            <li>All languages, countries of origin, and immigration documentation statuses are embraced without barrier or disclosure requirements.</li>
          </ul>

          <div style="background:#F0F2FA; border-radius:16px; padding:20px 24px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px;">
            <div>
              <strong style="color:var(--navy); font-size:1.05rem; display:block;">Need assistance or have questions?</strong>
              <span style="font-size:0.94rem; color:var(--text-muted);">Call our intake line at <strong>206-760-1573</strong> or email <a href="mailto:help@kandelia.org" style="color:var(--navy); font-weight:700;">help@kandelia.org</a>.</span>
            </div>
            <a href="mailto:help@kandelia.org?subject=Intake Request for Kandelia Programs" class="btn btn-primary btn-sm">Contact an Intake Advocate →</a>
          </div>
        </div>
      </div>
    </section>

    {get_support_banner()}
  </main>
'''
help_html += get_footer()

with open('get-help.html', 'w', encoding='utf-8') as f:
    f.write(help_html)
print("get-help.html written successfully!")


# ==============================================================================
# 4. GENERATE ways-to-give.html (WAYS TO GIVE - FAMILY/YOUTH PHOTOS, VEHICLE CARD)
# ==============================================================================
print("Generating ways-to-give.html...")
ways_html = get_head("Ways to Give | Kandelia", "Explore flexible pathways to support Kandelia: monthly giving, family funds, youth education, employer matching, and vehicle donations.")
ways_html += get_header("ways-to-give")
ways_html += f'''
  <main id="main-content">
    {SVG_HEART_CLIP}

    <!-- PAGE HERO -->
    <section class="inner-hero" id="overview">
      <div class="w inner-hero-content">
        <span class="badge badge-green">Impact & Generosity</span>
        <h1 class="inner-hero-title">Ways to Give to Kandelia</h1>
        <p class="inner-hero-lead">
          Your tax-deductible partnership ensures immigrant and refugee youth stay on track to graduate, while equipping newcomer parents with the tools to build economic resilience.
        </p>
      </div>
    </section>

    <!-- 6 GIVING PATHWAYS (FAMILY & YOUTH PHOTOS + DEDICATED VEHICLE DONATION CARD) -->
    <section style="padding:80px 0; background-color:#FFFFFF;">
      <div class="w">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 40px;">
          <span class="badge badge-teal" style="margin-bottom:12px;">Diverse Giving Options</span>
          <h2>Flexible Pathways to Support Our Mission</h2>
          <p class="lead">Choose the giving pathway that fits your philanthropic goals and fuels real community transformation.</p>
        </div>

        <div class="ways-photo-grid">
          <!-- 1. Family Giving (With distinct high-quality family photo) -->
          <div class="way-photo-card" id="family-giving">
            <div class="way-photo-wrap">
              <img src="assets/image_4.jpeg" alt="Kandelia family gathering in a collaborative workshop" loading="lazy">
            </div>
            <div class="way-photo-body">
              <span class="badge badge-teal" style="width:fit-content;">Family Stability</span>
              <h3>Family Flourishing Fund</h3>
              <p>Directly support adult digital literacy classes, family rental assistance, and bilingual school navigation so newcomer households stay housed and connected.</p>
              <div class="way-photo-action">
                <a href="https://kandelia-bloom.kindful.com/embeds/75568458-194c-4924-8a1b-de2cd76e4f92" target="_blank" rel="noopener" class="btn btn-outline btn-sm">Support Families →</a>
              </div>
            </div>
          </div>

          <!-- 2. Youth Giving (With distinct high-quality youth photo) -->
          <div class="way-photo-card" id="youth-giving">
            <div class="way-photo-wrap">
              <img src="assets/image_3.jpeg" alt="Kandelia high school students smiling in a classroom" loading="lazy">
            </div>
            <div class="way-photo-body">
              <span class="badge badge-sage" style="width:fit-content;">Youth Education</span>
              <h3>Youth Mentorship & Education</h3>
              <p>Fund after-school tutoring, high school graduation pathways, and paid youth leadership internships for newcomer high school students.</p>
              <div class="way-photo-action">
                <a href="https://kandelia-bloom.kindful.com/embeds/75568458-194c-4924-8a1b-de2cd76e4f92" target="_blank" rel="noopener" class="btn btn-outline btn-sm">Support Youth →</a>
              </div>
            </div>
          </div>

          <!-- 3. Monthly Sustaining Giving (Clean SVG Line Heart) -->
          <div class="way-photo-card">
            <div class="way-photo-body" style="padding-top:28px;">
              <div style="color:var(--coral); margin-bottom:14px;">
                {ICON_HEART}
              </div>
              <span class="badge badge-coral" style="width:fit-content;">Recurring Impact</span>
              <h3>Flourishing Circle (Monthly Giving)</h3>
              <p>Predictable monthly contributions create dependable funding that keeps classrooms staffed, tutoring active, and emergency funds open 365 days a year.</p>
              <div class="way-photo-action">
                <a href="/giving#monthly-donor" class="btn btn-primary btn-sm">Join Monthly Circle →</a>
              </div>
            </div>
          </div>

          <!-- 4. Employer Gift Matching (Clean SVG Line Gift Box) -->
          <div class="way-photo-card">
            <div class="way-photo-body" style="padding-top:28px;">
              <div style="color:#2A6615; margin-bottom:14px;">
                {ICON_GIFT}
              </div>
              <span class="badge badge-green" style="width:fit-content;">Corporate Match</span>
              <h3>Employer Matching Gifts</h3>
              <p>Double your impact! Major employers (Microsoft, Boeing, Starbucks, Google, Gates Foundation) match charitable gifts 1:1. Request a match through your company portal.</p>
              <div class="way-photo-action">
                <a href="https://kandelia-bloom.kindful.com/embeds/75568458-194c-4924-8a1b-de2cd76e4f92" target="_blank" rel="noopener" class="btn btn-outline btn-sm">Check Match →</a>
              </div>
            </div>
          </div>

          <!-- 5. DAFs & Appreciated Stock (Clean SVG Line Bank) -->
          <div class="way-photo-card">
            <div class="way-photo-body" style="padding-top:28px;">
              <div style="color:#14857F; margin-bottom:14px;">
                {ICON_BANK}
              </div>
              <span class="badge badge-teal" style="width:fit-content;">Tax-Advantaged</span>
              <h3>Donor-Advised Funds & Stock</h3>
              <p>Recommend a grant from your DAF (Seattle Foundation, Fidelity, Schwab, Vanguard) or make direct institutional wire transfers to maximize your philanthropic legacy.</p>
              <div class="way-photo-action">
                <a href="mailto:info@kandelia.org?subject=DAF or Stock Giving Inquiries" class="btn btn-outline btn-sm">Give via DAF / Wire →</a>
              </div>
            </div>
          </div>

          <!-- 6. Dedicated Vehicle Donation Card (Clean SVG Car Icon + Official CARS Copy) -->
          <div class="way-photo-card" style="border:2px solid rgba(42,210,201,0.40); box-shadow:0 8px 24px rgba(42,210,201,0.10);">
            <div class="way-photo-body" style="padding-top:28px;">
              <div style="color:var(--teal); margin-bottom:14px;">
                {ICON_CAR}
              </div>
              <span class="badge badge-blue" style="width:fit-content;">Turn Wheels into Impact</span>
              <h3>Vehicle Donation Program (CARS)</h3>
              <p style="font-size:0.95rem; line-height:1.6; color:var(--text-body);">
                The proceeds from your vehicle will directly benefit Kandelia's programs. Both Kandelia and CARS are 501(c)(3) nonprofit organizations, and donations through this program are tax deductible. Click the link below to fuel brighter futures!
              </p>
              <div class="way-photo-action">
                <a href="https://careasy.org/kandelia" target="_blank" rel="noopener noreferrer" class="btn btn-coral">
                  CARS Donation →
                </a>
              </div>
            </div>
          </div>
        </div>

        <div style="text-align:center; margin-top:48px;">
          <a class="btn btn-primary btn-lg" href="/giving">View Specific Donation Tiers ($50, $100, $250) →</a>
        </div>
      </div>
    </section>

    {get_support_banner()}
  </main>
'''
ways_html += get_footer()

with open('ways-to-give.html', 'w', encoding='utf-8') as f:
    f.write(ways_html)
print("ways-to-give.html written successfully!")


# ==============================================================================
# 5. GENERATE stories.html (STORIES & IMPACT - CLEAN 1:1 SQUARE BORDERLESS IMAGES)
# ==============================================================================
print("Generating stories.html...")
stories_html = get_head("Stories & Impact | Kandelia", "Read authentic immigrant and refugee stories, client testimonials, and 2026 impact outcomes from Kandelia in Seattle.")
stories_html += get_header("stories")
stories_html += f'''
  <main id="main-content">
    {SVG_HEART_CLIP}

    <!-- PAGE HERO -->
    <section class="inner-hero" id="overview">
      <div class="w inner-hero-content">
        <span class="badge badge-teal">Voices of Resilience</span>
        <h1 class="inner-hero-title">Stories & Community Impact</h1>
        <p class="inner-hero-lead">
          Behind every metric is an extraordinary individual journey. Meet the students, caregivers, and community mentors flourishing through Kandelia's programs.
        </p>
      </div>
    </section>

    <!-- 4 IMMIGRANT STORIES - BORDERLESS 1:1 SQUARE IMAGES -->
    <section style="padding:80px 0; background-color:#FFFFFF;">
      <div class="w">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 40px;">
          <span class="badge badge-sage" style="margin-bottom:12px;">Participant Journeys</span>
          <h2>Roots & Routes Stories</h2>
          <p class="lead">First-person reflections of perseverance, leadership, and belonging in Seattle.</p>
        </div>

        <div class="story-square-grid">
          <!-- Story 1: Patrick -->
          <div class="story-square-card">
            <div class="story-square-img-wrap">
              <img src="assets/image_5.jpeg" alt="Patrick's Story" class="story-img-square" loading="lazy">
            </div>
            <div class="story-square-body">
              <span class="badge badge-sage" style="width:fit-content; margin-bottom:6px;">Youth Alumnus</span>
              <h3>Patrick's Story</h3>
              <p style="font-style:italic; margin-bottom:8px;">"{site_data.STORIES[0]['quote']}"</p>
              <p>{site_data.STORIES[0]['short']}</p>
            </div>
          </div>

          <!-- Story 2: Sunflower & Tulip -->
          <div class="story-square-card">
            <div class="story-square-img-wrap">
              <img src="assets/image_6.jpeg" alt="Sunflower & Tulip's Story" class="story-img-square" loading="lazy">
            </div>
            <div class="story-square-body">
              <span class="badge badge-coral" style="width:fit-content; margin-bottom:6px;">Sisters & Scholars</span>
              <h3>Sunflower & Tulip's Story</h3>
              <p style="font-style:italic; margin-bottom:8px;">"{site_data.STORIES[1]['quote']}"</p>
              <p>{site_data.STORIES[1]['short']}</p>
            </div>
          </div>

          <!-- Story 3: A Mother's Story -->
          <div class="story-square-card">
            <div class="story-square-img-wrap">
              <img src="assets/image_7.jpeg" alt="A Mother's Story" class="story-img-square" loading="lazy">
            </div>
            <div class="story-square-body">
              <span class="badge badge-teal" style="width:fit-content; margin-bottom:6px;">Parent Advocate</span>
              <h3>A Mother's Story</h3>
              <p style="font-style:italic; margin-bottom:8px;">"{site_data.STORIES[2]['quote']}"</p>
              <p>{site_data.STORIES[2]['short']}</p>
            </div>
          </div>

          <!-- Story 4: Vidia's Story -->
          <div class="story-square-card">
            <div class="story-square-img-wrap">
              <img src="assets/image_8.jpeg" alt="Vidia's Story" class="story-img-square" loading="lazy">
            </div>
            <div class="story-square-body">
              <span class="badge badge-blue" style="width:fit-content; margin-bottom:6px;">Peer Leader</span>
              <h3>Vidia's Story</h3>
              <p style="font-style:italic; margin-bottom:8px;">"{site_data.STORIES[3]['quote']}"</p>
              <p>{site_data.STORIES[3]['short']}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- TESTIMONIALS -->
    <section class="section-testimonials" id="testimonials" style="padding:80px 0; background-color:#F4FBE8;">
      <div class="w">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 48px;">
          <span class="badge badge-green" style="margin-bottom:12px;">Community Perspectives</span>
          <h2>Voices of Trust & Gratitude</h2>
          <p class="lead">What students, parents, school counselors, and community leaders say about Kandelia.</p>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:28px;">
'''

for test in site_data.TESTIMONIALS:
    stories_html += f'''          <div style="background:#FFFFFF; border-radius:20px; padding:32px 28px; border:1px solid rgba(151,215,0,0.30); box-shadow:0 4px 14px rgba(30,34,170,0.03); display:flex; flex-direction:column; justify-content:space-between;">
            <p style="font-size:1.02rem; color:var(--text-body); line-height:1.65; margin-bottom:18px; font-style:italic;">
              "{test['quote']}"
            </p>
            <div>
              <strong style="color:var(--navy); font-size:1.05rem; display:block;">{test['author']}</strong>
              <span style="font-size:0.9rem; color:var(--teal-dark); font-weight:600;">{test['role']}</span>
            </div>
          </div>\n'''

stories_html += '''        </div>
      </div>
    </section>

    <!-- 2026 ANNUAL REPORT -->
    <section class="section-report" id="metrics" style="padding:80px 0; background-color:#FFFFFF;">
      <div class="w">
        <div class="pinned-report-card">
          <div class="report-cover-box" style="background:#1F22AA; border-radius:20px; padding:32px 24px; color:#FFFFFF; display:flex; flex-direction:column; justify-content:space-between; min-height:240px; box-shadow:0 10px 30px rgba(31,34,170,0.15);">
            <div>
              <span class="badge" style="margin-bottom:12px; border:none; background:rgba(255,255,255,0.2); color:#FFFFFF; font-size:0.75rem; text-transform:uppercase; letter-spacing:0.05em; padding:4px 12px; border-radius:20px; display:inline-block;">Annual Report</span>
              <div style="font-size:1.6rem; font-weight:700; line-height:1.2; color:#FFFFFF; margin-top:8px;">2026 Impact Report</div>
            </div>
            <div style="font-size:1.05rem; font-weight:700; color:rgba(255,255,255,0.9); letter-spacing:0.02em;">Kandelia</div>
          </div>

          <div class="report-details-body">
            <span class="badge badge-sage" style="margin-bottom:10px; background:#E6FAF9; color:#14857F; border-color:rgba(42,210,201,0.3);">Featured Publication</span>
            <h3>Deep Roots, Lasting Flourish</h3>
            <p>Explore our comprehensive evaluation of student graduation rates, family economic mobility, and direct assistance distribution across King County.</p>
            <ul class="report-datapoints">
              <li><svg class="icon check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true" style="width:18px;height:18px;margin-right:8px;vertical-align:-2px;"><polyline points="20 6 9 17 4 12"></polyline></svg><strong>570+ Newcomers</strong> guided through academic and civic pathways</li>
              <li><svg class="icon check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true" style="width:18px;height:18px;margin-right:8px;vertical-align:-2px;"><polyline points="20 6 9 17 4 12"></polyline></svg><strong>95% Graduation Rate</strong> among cohort high school seniors</li>
              <li><svg class="icon check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true" style="width:18px;height:18px;margin-right:8px;vertical-align:-2px;"><polyline points="20 6 9 17 4 12"></polyline></svg><strong>$240,000+ Distributed</strong> in direct emergency family relief & rental aid</li>
              <li><svg class="icon check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true" style="width:18px;height:18px;margin-right:8px;vertical-align:-2px;"><polyline points="20 6 9 17 4 12"></polyline></svg><strong>1,200+ Hours</strong> of bilingual adult digital literacy training delivered</li>
            </ul>
            <div style="display:flex; gap:14px; flex-wrap:wrap;">
              <a class="btn btn-primary" href="#contact">Read the 2026 Impact Report →</a>
              <a class="btn btn-outline" href="mailto:info@kandelia.org?subject=Request 2026 Impact Report PDF">Request PDF Copy</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    {get_support_banner()}
  </main>
'''
stories_html += get_footer()

with open('stories.html', 'w', encoding='utf-8') as f:
    f.write(stories_html)
print("stories.html written successfully!")


# ==============================================================================
# 6. GENERATE giving.html (3 GIVING CARDS + SINGLE GIVE BUTTON, MONTHLY DONOR, CARS, FAQ)
# ==============================================================================
print("Generating giving.html...")
giving_html = get_head("Giving & Impact Tiers | Kandelia", "Support Kandelia's immigrant and refugee programs with transparent giving tiers, monthly donor membership, and vehicle donations.")
giving_html += get_header("giving")
giving_html += f'''
  <main id="main-content">
    {SVG_HEART_CLIP}

    <!-- GIVING HERO -->
    <section class="giving-hero" id="hero">
      <div class="w giving-hero-content">
        <span class="badge badge-teal">Transparent Community Investment</span>
        <h1 class="giving-hero-title">
          Fueling Brighter Futures for Newcomer Families
        </h1>
        <p class="giving-hero-lead">
          Every contribution directly equips newly arrived immigrant and refugee youth and families with the mentorship, language access, and emergency relief they need to thrive.
        </p>

        <div class="giving-trust-pills">
          <div class="giving-trust-pill">{ICON_CHECK} 501(c)(3) Tax Deductible</div>
          <div class="giving-trust-pill">{ICON_CHECK} 100% Program Allocation</div>
          <div class="giving-trust-pill">{ICON_CHECK} Secure Kindful Gateway</div>
        </div>
      </div>
    </section>

    <!-- THREE GIVING CARDS + SINGLE PROMINENT CENTERED GIVE BUTTON -->
    <section class="section-impact-tiers" id="tiers" style="padding:80px 0; background-color:#FFFFFF;">
      <div class="w">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 20px;">
          <span class="badge badge-sage" style="margin-bottom:12px;">Direct Community Outcomes</span>
          <h2>Featured Giving Tiers</h2>
          <p class="lead">See exactly how your gift translates into tangible resources for immigrant and refugee students and families.</p>
        </div>

        <div class="giving-tiers-3grid">
          <!-- Card 1: $50 -->
          <div class="tier-card-clean">
            <span class="badge badge-sage" style="width:fit-content;">Newcomer Essentials</span>
            <div class="tier-amount">$50</div>
            <div class="tier-title">Student Starter Pack</div>
            <p class="tier-outcome">
              Provides essential school supplies, bilingual orientation folders, and public transit passes for a newly arrived high school student entering King County public schools.
            </p>
          </div>

          <!-- Card 2: $100 -->
          <div class="tier-card-clean" style="border-color:var(--teal); box-shadow:0 8px 24px rgba(42,210,201,0.12);">
            <span class="badge badge-teal" style="width:fit-content;">Academic Mentorship</span>
            <div class="tier-amount" style="color:var(--teal-dark);">$100</div>
            <div class="tier-title">1-on-1 Tutoring & ELL Guidance</div>
            <p class="tier-outcome">
              Funds 4 hours of dedicated after-school tutoring, English language navigation, and college application mentoring for an immigrant or refugee student.
            </p>
          </div>

          <!-- Card 3: $250 -->
          <div class="tier-card-clean">
            <span class="badge badge-blue" style="width:fit-content;">Family Stability</span>
            <div class="tier-amount">$250</div>
            <div class="tier-title">Family Digital Access & Navigation</div>
            <p class="tier-outcome">
              Funds one full month of adult digital literacy training, family computer lab access, and direct support navigating school district portals and housing benefits.
            </p>
          </div>
        </div>

        <!-- SINGLE PROMINENT CENTERED GIVE BUTTON -->
        <div class="single-give-cta-wrap">
          <a class="btn btn-coral btn-lg" style="padding:16px 48px; font-size:1.15rem; font-weight:700; border-radius:var(--radius-pill); box-shadow:0 8px 24px rgba(244,54,76,0.35);" href="https://kandelia-bloom.kindful.com" target="_blank" rel="noopener">
            Give to Kandelia →
          </a>
        </div>
      </div>
    </section>

    <!-- MONTHLY DONOR! HIGHLIGHT SECTION (REPLACES CUSTOM AMOUNT) -->
    <section class="section-monthly-donor" id="monthly-donor">
      <div class="w">
        <div class="monthly-donor-card">
          <div class="monthly-donor-content">
            <span class="badge badge-coral" style="margin-bottom:8px;">Flourishing Circle</span>
            <h3>Monthly Donor!</h3>
            <p>
              Join our community of monthly donors. Steady, predictable gifts help Kandelia plan ahead and keep English classes, mentorship, and career exploration going year-round for newly arrived youth and families.
            </p>
          </div>
          <div class="monthly-donor-action">
            <a class="btn btn-primary btn-lg" href="https://kandelia-bloom.kindful.com" target="_blank" rel="noopener">
              Become a Monthly Donor →
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- WAYS TO GIVE (INCLUDING DEDICATED VEHICLE DONATION CARD) -->
    <section class="section-ways-to-give" style="padding:80px 0; background-color:#FFFFFF;">
      <div class="w">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 40px;">
          <span class="badge badge-green" style="margin-bottom:12px;">Diverse Giving Options</span>
          <h2>More Meaningful Ways to Support Kandelia</h2>
          <p class="lead">From workplace matching gifts to vehicle donations, there are many flexible pathways to advance refugee and immigrant equity.</p>
        </div>

        <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:24px;">
          <!-- Option 1: Monthly Sustaining -->
          <div class="way-card" style="background:#FFFFFF; border-radius:20px; padding:28px 24px; border:1px solid rgba(42,210,201,0.25); box-shadow:0 4px 14px rgba(30,34,170,0.04);">
            <div class="way-icon-bubble" style="background:#FEECEE; color:#F4364C; width:52px; height:52px; border-radius:14px; display:flex; align-items:center; justify-content:center; margin-bottom:18px;">
              {ICON_HEART}
            </div>
            <h3 class="way-title" style="font-size:1.2rem; color:var(--navy); margin-bottom:10px;">Monthly Sustaining Giving</h3>
            <p class="way-desc" style="font-size:0.95rem; color:var(--text-body); line-height:1.6;">
              Joining our monthly Flourishing Circle creates reliable funding that keeps classrooms staffed and emergency funds active year-round.
            </p>
          </div>

          <!-- Option 2: Employer Gift Matching -->
          <div class="way-card" style="background:#FFFFFF; border-radius:20px; padding:28px 24px; border:1px solid rgba(42,210,201,0.25); box-shadow:0 4px 14px rgba(30,34,170,0.04);">
            <div class="way-icon-bubble" style="background:#F4FBE8; color:#2A6615; width:52px; height:52px; border-radius:14px; display:flex; align-items:center; justify-content:center; margin-bottom:18px;">
              {ICON_GIFT}
            </div>
            <h3 class="way-title" style="font-size:1.2rem; color:var(--navy); margin-bottom:10px;">Employer Matching Gifts</h3>
            <p class="way-desc" style="font-size:0.95rem; color:var(--text-body); line-height:1.6;">
              Double or triple your impact! Major employers (Microsoft, Boeing, Starbucks, Google) match charitable gifts 1:1.
            </p>
          </div>

          <!-- Option 3: DAFs & Stock -->
          <div class="way-card" style="background:#FFFFFF; border-radius:20px; padding:28px 24px; border:1px solid rgba(42,210,201,0.25); box-shadow:0 4px 14px rgba(30,34,170,0.04);">
            <div class="way-icon-bubble" style="background:#E6FAF9; color:#14857F; width:52px; height:52px; border-radius:14px; display:flex; align-items:center; justify-content:center; margin-bottom:18px;">
              {ICON_BANK}
            </div>
            <h3 class="way-title" style="font-size:1.2rem; color:var(--navy); margin-bottom:10px;">Donor-Advised Funds (DAF)</h3>
            <p class="way-desc" style="font-size:0.95rem; color:var(--text-body); line-height:1.6;">
              Recommend a grant from your DAF or make direct wire transfers to receive optimal tax benefits while uplifting our communities.
            </p>
          </div>

          <!-- Option 4: Dedicated Vehicle Donation Card -->
          <div class="way-card" style="background:#FFFFFF; border-radius:20px; padding:28px 24px; border:2px solid rgba(42,210,201,0.40); box-shadow:0 8px 20px rgba(42,210,201,0.08);">
            <div class="way-icon-bubble" style="background:#ECEEFF; color:var(--teal); width:52px; height:52px; border-radius:14px; display:flex; align-items:center; justify-content:center; margin-bottom:18px;">
              {ICON_CAR}
            </div>
            <span class="badge badge-blue" style="width:fit-content; margin-bottom:8px;">Vehicle Donation</span>
            <h3 class="way-title" style="font-size:1.2rem; color:var(--navy); margin-bottom:10px;">Vehicle Donation Program</h3>
            <p class="way-desc" style="font-size:0.95rem; color:var(--text-body); line-height:1.6; margin-bottom:16px;">
              The proceeds from your vehicle will directly benefit Kandelia's programs. Both Kandelia and CARS are 501(c)(3) nonprofit organizations, and donations through this program are tax deductible. Click the link below to fuel brighter futures!
            </p>
            <a href="https://careasy.org/kandelia" target="_blank" rel="noopener noreferrer" class="btn btn-coral btn-sm">
              CARS Donation →
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- DONATION & STEWARDSHIP FAQ ACCORDION -->
    <section class="section-donation-faq" id="faq" style="padding:80px 0; background-color:#F0FAF9; border-top:1px solid rgba(42,210,201,0.2);">
      <div class="w">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 40px;">
          <span class="badge badge-blue" style="margin-bottom:12px;">Frequently Asked Questions</span>
          <h2>Donation & Stewardship FAQ</h2>
          <p class="lead">We believe in complete financial transparency, responsible stewardship, and making giving seamless and secure.</p>
        </div>

        <div class="faq-wrapper" style="max-width:820px; margin:0 auto;">
          <!-- FAQ 1 -->
          <div class="faq-item">
            <button class="faq-question" aria-expanded="false">
              <span>Is my donation tax-deductible?</span>
              <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="faq-answer">
              <div class="faq-answer-inner">
                Yes, absolutely. Kandelia is a registered 501(c)(3) tax-exempt non-profit organization recognized by the IRS. Contributions are fully tax-deductible to the maximum extent permitted by federal and state law. Immediately after your transaction completes through our Kindful gateway, you will receive an official digital tax receipt for your records.
              </div>
            </div>
          </div>

          <!-- FAQ 2 -->
          <div class="faq-item">
            <button class="faq-question" aria-expanded="false">
              <span>How are my donation dollars allocated?</span>
              <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="faq-answer">
              <div class="faq-answer-inner">
                Over 85% of every dollar goes directly into youth academic mentorship, adult digital literacy workshops, bilingual staff compensation, and direct emergency family relief funds across King County.
              </div>
            </div>
          </div>

          <!-- FAQ 3 -->
          <div class="faq-item">
            <button class="faq-question" aria-expanded="false">
              <span>Can I set up a recurring monthly donation?</span>
              <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="faq-answer">
              <div class="faq-answer-inner">
                Yes! When donating on our Kindful portal, simply select "Monthly" instead of "One-time". Recurring donations can be modified, paused, or cancelled at any time directly through your donor dashboard.
              </div>
            </div>
          </div>

          <!-- FAQ 4 -->
          <div class="faq-item">
            <button class="faq-question" aria-expanded="false">
              <span>What payment methods are accepted?</span>
              <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="faq-answer">
              <div class="faq-answer-inner">
                Our secure Kindful checkout accepts all major credit and debit cards (Visa, MasterCard, American Express, Discover), direct ACH bank transfers, Apple Pay, and Google Pay. We also welcome physical checks mailed to our Seattle office.
              </div>
            </div>
          </div>

          <!-- FAQ 5 -->
          <div class="faq-item">
            <button class="faq-question" aria-expanded="false">
              <span>How does employer matching work?</span>
              <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="faq-answer">
              <div class="faq-answer-inner">
                Thousands of companies match charitable donations dollar-for-dollar. After donating, search for "Kandelia" in your employer's CSR portal (e.g., Benevity, CyberGrants, YourCause) and submit your receipt. Email info@kandelia.org if you need assistance.
              </div>
            </div>
          </div>

          <!-- FAQ 6 -->
          <div class="faq-item">
            <button class="faq-question" aria-expanded="false">
              <span>How does vehicle donation with CARS work?</span>
              <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="faq-answer">
              <div class="faq-answer-inner">
                Donating your vehicle is quick and convenient. Visit our official CARS portal at careasy.org/kandelia or call their toll-free assistance line. CARS arranges complimentary vehicle pickup, completes the sale, delivers tax documentation, and passes the net proceeds directly to Kandelia.
              </div>
            </div>
          </div>

          <!-- FAQ 7 -->
          <div class="faq-item">
            <button class="faq-question" aria-expanded="false">
              <span>How can I give by check or offline pledge?</span>
              <svg class="faq-chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </button>
            <div class="faq-answer">
              <div class="faq-answer-inner">
                Please make checks payable to <strong>Kandelia</strong> and mail to: <strong>3829B S. Edmunds St. Box 9, Seattle, WA 98118</strong>. Please note any program dedication or matching details in the memo line.
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    {get_support_banner()}
  </main>
'''
giving_html += get_footer()

with open('giving.html', 'w', encoding='utf-8') as f:
    f.write(giving_html)
print("giving.html written successfully!")

print("=== All 6 pages built successfully! ===")
