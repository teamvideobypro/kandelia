import os
import html
import site_data

print("=== Starting build_all_pages.py ===")

# --- SVG ICONS (Clean, minimal, 24x24 viewBox, stroke-width 2, no emojis) ---
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
  <link rel="icon" type="image/png" sizes="64x64" href="assets/favicon.png">
  <link rel="apple-touch-icon" sizes="512x512" href="assets/kandelia_icon_mark.png">
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
        <img src="assets/kandelia_logo_horizontal_no_tag_rgb.png" alt="Kandelia" class="brand-logo" width="220" height="60" style="height:52px; width:auto; display:block;">
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
              <a class="btn btn-coral btn-lg support-donate-pill-btn" href="https://kandelia-bloom.kindful.com/embeds/75568458-194c-4924-8a1b-de2cd76e4f92" target="_blank" rel="noopener">Support &amp; Donate Today&nbsp;→</a>
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
          <!-- Plain white logo as shared by Xochilt (Google Drive: 1rX6tPUveHnbeSscp83D18zBBQDMcJrO2), unconstrained horizontal layout, transparent background -->
          <div class="footer-logo-wrap-clean">
            <img src="assets/kandelia_logo_horizontal_no_tag_reverse.png" alt="Kandelia" width="240" height="66" style="width:100%; max-width:240px; height:auto; display:block;">
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
              <svg class="icon" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" style="width:20px;height:20px;flex-shrink:0;"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
            </a>
            <a href="https://facebook.com/kandelia" target="_blank" rel="noopener" class="social-circle-btn" aria-label="Facebook">
              <svg class="icon" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" style="width:20px;height:20px;flex-shrink:0;"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg>
            </a>
            <a href="https://instagram.com/kandelia" target="_blank" rel="noopener" class="social-circle-btn" aria-label="Instagram">
              <svg class="icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width:20px;height:20px;flex-shrink:0;"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
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
            <li><a href="/careers">Work With Us (Careers)</a></li>
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
            <li><a href="/ways-to-give#give">Give to Kandelia</a></li>
            <li><a href="/ways-to-give#volunteer">Volunteer With Us</a></li>
            <li><a href="/ways-to-give#partner">Partner With Us</a></li>
            <li><a href="https://careasy.org/kandelia" target="_blank" rel="noopener noreferrer">Vehicle Donation (CARS)</a></li>
          </ul>
          <div style="margin-top:20px;">
            <a class="btn btn-coral btn-sm" href="https://kandelia-bloom.kindful.com/embeds/75568458-194c-4924-8a1b-de2cd76e4f92" target="_blank" rel="noopener">Donate</a>
          </div>
        </div>
      </div>

      <!-- Stay in the Loop Newsletter Signup (Integrated at bottom of footer across all pages) -->
      <div class="footer-stay-in-loop">
        <div style="max-width:720px; margin:0 auto; text-align:center;">
          <h4 style="font-size:1.35rem; color:#FFFFFF; margin-bottom:8px; font-weight:700;">Stay in the Loop with Kandelia</h4>
          <p style="font-size:0.95rem; color:rgba(255,255,255,0.85); margin-bottom:18px; line-height:1.5;">Receive community updates, student stories, and event invitations a few times a year. No spam, ever.</p>
          <form class="footer-stay-in-loop-form" onsubmit="event.preventDefault(); handleFooterNewsletter(this);">
            <input type="text" name="first_name" class="footer-stay-in-loop-input" placeholder="First Name" required>
            <input type="text" name="last_name" class="footer-stay-in-loop-input" placeholder="Last Name" required>
            <input type="email" name="email" class="footer-stay-in-loop-input" placeholder="Email Address" required>
            <button type="submit" class="btn btn-coral" style="border-radius:30px; padding:12px 28px; font-weight:700; cursor:pointer;">Subscribe</button>
            <div class="footer-newsletter-feedback" role="alert" style="width:100%; text-align:center; margin-top:10px; font-size:0.92rem; min-height:22px;"></div>
          </form>
        </div>
      </div>

      <div class="footer-bottom">
        <div>
          &copy; <span id="copyright-year">2026</span> Kandelia. Registered 501(c)(3) non-profit organization. Tax ID: 91-1122532.
        </div>
        <div class="footer-bottom-links">
          <a href="#privacy-policy" class="open-privacy-modal">Privacy Policy</a>
          <a href="#terms-of-use" class="open-terms-modal">Terms of Use</a>
          <a href="/about#impact-report">Financial Transparency</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- Global Modal Overlay (Accessible pop-ups for bios, stories, and videos) -->
  <div class="modal-overlay" id="global-modal-overlay" aria-hidden="true" role="dialog" aria-modal="true" aria-labelledby="modal-title">
    <div class="modal-dialog">
      <div class="modal-header">
        <h3 id="modal-title">Modal Title</h3>
        <button class="modal-close-btn" id="modal-close-button" aria-label="Close modal">&times;</button>
      </div>
      <div class="modal-body" id="modal-content-area" style="padding: 28px 36px 36px;"></div>
    </div>
  </div>

  <script src="script.js"></script>
</body>
</html>'''

def get_testimonial_carousel_html(carousel_id="testimonials-carousel"):
    out = f'''    <!-- MOVING TESTIMONIALS CAROUSEL (Image 4 Design: Green bar, Avatar MC, Nav dots & arrows) -->
    <section class="section-testimonials" id="{carousel_id}-section" style="padding:80px 0; background-color:#F4FBE8;">
      <div class="w">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 48px;">
          <span class="badge badge-green" style="margin-bottom:12px;">Community Perspectives</span>
          <h2>Voices of Trust & Gratitude</h2>
          <p class="lead">What students, parents, school counselors, and community leaders say about Kandelia.</p>
        </div>

        <div class="carousel-container" id="{carousel_id}" aria-label="Community Testimonials Carousel">
          <div class="carousel-track-wrapper">
'''
    for idx, test in enumerate(site_data.TESTIMONIALS):
        initials = "".join([part[0] for part in test['author'].split() if part[0].isalpha()])[:2]
        out += f'''            <div class="carousel-slide {'active' if idx==0 else ''}" role="group" aria-roledescription="slide" aria-label="Testimonial {idx+1} of {len(site_data.TESTIMONIALS)}">
              <blockquote class="testimonial-quote">
                "{test['quote']}"
              </blockquote>
              <div class="testimonial-author-block">
                <div class="author-avatar">{initials}</div>
                <div class="author-info">
                  <b>{test['author']}</b>
                  <span>{test['role']} • {test['category']}</span>
                </div>
              </div>
            </div>\n'''

    out += f'''          </div>

          <!-- Carousel Navigation Controls with arrows and elongated center dots pill -->
          <div class="carousel-controls">
            <button class="carousel-btn carousel-btn-prev" aria-label="Previous testimonial">&#8592;</button>
            <div class="carousel-dots">
'''
    for idx in range(len(site_data.TESTIMONIALS)):
        out += f'''              <button class="carousel-dot {'active' if idx==0 else ''}" data-index="{idx}" aria-label="Go to testimonial {idx+1}"></button>\n'''

    out += f'''            </div>
            <button class="carousel-btn carousel-btn-next" aria-label="Next testimonial">&#8594;</button>
          </div>
        </div>
      </div>
    </section>'''
    return out


# ==============================================================================
# 1. GENERATE index.html (HOME PAGE - CLEAN HERO WITH ZERO FLOATING BADGES/STATS/DOTS)
# ==============================================================================
print("Generating index.html...")
home_html = get_head("Kandelia | Immigrant & Refugee Belonging in Seattle", "Kandelia removes barriers to immigrant and refugee success through holistic education, family navigation, and community equity in Seattle.")
home_html += get_header("home")
home_html += f'''
  <main id="main-content">
    {SVG_HEART_CLIP}

    <!-- HERO SECTION (CLEAN: No top badge line, No stats 2x2 row, No moving dotted ring, No floating badges on photo) -->
    <section class="section-hero" id="hero">
      <div class="w hero-grid">
        <div class="hero-content">
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
        </div>

        <div class="hero-media-wrapper">
          <div class="hero-organic-composition">
            <!-- Main Image Frame with Organic Curve (Clean photo with no floating stats or badges) -->
            <div class="hero-image-frame-enhanced">
              <img src="assets/image_1.jpeg" alt="Smiling Kandelia students outside their school in Seattle" class="hero-main-img">
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 50TH ANNIVERSARY CELEBRATION (MAY 2027) - CLEAN SOLID PHOTO FRAME WITHOUT DOTTED/DASHED BORDER -->
    <section class="event-banner-section" id="milestone-gala">
      <div class="w">
        <div class="event-card">
          <div class="event-2col-grid">
            <!-- Left Column: Seattle skyline image with clean solid frame (No dotted/dashed lines) -->
            <div class="event-image-col">
              <div class="event-layered-image-wrap" style="position:relative;">
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
                <button type="button" class="event-sponsor-btn open-sponsor-modal">
                  Become a Sponsor
                </button>
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

    <!-- CORE VALUES SECTION (5 VALUES IN BALANCED 3+2 LAYOUT - NO ORPHANED CARD) -->
    <section class="section-values" id="values" style="padding:80px 0; background-color:#FFFFFF;">
      <div class="w">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 48px;">
          <span class="badge badge-teal" style="margin-bottom:12px;">Guiding Principles</span>
          <h2>Our Core Values</h2>
          <p class="lead">These values drive our daily culture, educational cohorts, community advocacy, and strategic partnerships.</p>
        </div>

        <div class="values-even-flex">
          <div class="value-card-item" style="background:#F0FAF9; border:1px solid rgba(42,210,201,0.25);">
            <h3 style="font-size:1.25rem; color:var(--navy); margin-bottom:10px;">Inclusion</h3>
            <p style="font-size:0.96rem; color:var(--text-body); line-height:1.6; margin:0;">
              We embrace diversity and believe all people have value and the right to belong. We commit to active listening and questioning assumptions.
            </p>
          </div>
          <div class="value-card-item" style="background:#FEECEE; border:1px solid rgba(244,54,76,0.22);">
            <h3 style="font-size:1.25rem; color:var(--coral); margin-bottom:10px;">Heart</h3>
            <p style="font-size:0.96rem; color:var(--text-body); line-height:1.6; margin:0;">
              We measure our success by the real difference we make in people's lives. We act with care, empathy, kindness, and fun along the way.
            </p>
          </div>
          <div class="value-card-item" style="background:#F4FBE8; border:1px solid rgba(151,215,0,0.25);">
            <h3 style="font-size:1.25rem; color:#2A6615; margin-bottom:10px;">Equity</h3>
            <p style="font-size:0.96rem; color:var(--text-body); line-height:1.6; margin:0;">
              We believe in just and fair inclusion, identifying inequities and taking proactive responsibility for addressing them.
            </p>
          </div>
          <div class="value-card-item" style="background:#ECEEFF; border:1px solid rgba(30,34,170,0.20);">
            <h3 style="font-size:1.25rem; color:var(--navy); margin-bottom:10px;">Relationships</h3>
            <p style="font-size:0.96rem; color:var(--text-body); line-height:1.6; margin:0;">
              We build strong connections with each other, partners, and the communities we serve in the spirit of genuine collaboration.
            </p>
          </div>
          <div class="value-card-item" style="background:#F0FAF9; border:1px solid rgba(42,210,201,0.25);">
            <h3 style="font-size:1.25rem; color:#14857F; margin-bottom:10px;">Excellence</h3>
            <p style="font-size:0.96rem; color:var(--text-body); line-height:1.6; margin:0;">
              We strive to be the best we can be in all we do, applying discipline, organization, and professionalism to our daily work.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- VIDEO EMBED SECTION (PLACED EXACTLY BETWEEN CORE VALUES AND ABOUT SECTION) -->
    <section class="section-video" id="video" style="padding:80px 0; background-color:#F0F2FA;">
      <div class="w" style="max-width:960px; margin:0 auto;">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 36px;">
          <span class="badge badge-coral" style="margin-bottom:12px;">50-Year Documentary Preview</span>
          <h2>The Story of Kandelia</h2>
          <p class="lead">Watch our commemorative milestone preview celebrating five decades of immigrant and refugee resilience across Seattle.</p>
        </div>

        <div class="video-embed-scalloped" id="kandelia-video-container" role="button" tabindex="0" aria-label="Watch video: The Story of Kandelia">
          <img class="video-poster-img" src="assets/image_2.jpeg" alt="Video preview for The Story of Kandelia" style="width:100%; height:100%; object-fit:cover;">
          <div class="video-play-overlay">
            <div class="video-flower-play-btn">
              <svg style="width:32px;height:32px;fill:currentColor;margin-left:4px;" viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
            </div>
            <div class="video-caption">
              The Story of Kandelia: Deep Roots, Resilience & 50 Years of Mutual Aid
            </div>
            <span class="badge badge-sage" style="border:none; background:rgba(255,255,255,0.92); color:var(--navy); font-weight:700;">Click to Preview Gala Documentary (3:45)</span>
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
          <a class="btn btn-outline" href="/about">Our 50-Year Story &amp; Team&nbsp;→</a>
          <a class="btn btn-primary" href="/careers">Work With Us →</a>
        </div>
      </div>
    </section>

    <!-- 50-YEAR MILESTONES (EXACTLY 4 EVENLY SPACED MILESTONES) -->
    <section class="section-milestones" id="milestones" style="padding:80px 0; background-color:#F0FAF9;">
      <div class="w">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 48px;">
          <span class="badge badge-sage" style="margin-bottom:12px;">Five Decades</span>
          <h2>Milestones of Belonging (1978–2028)</h2>
          <p class="lead">Key inflection points across fifty years of community empowerment and refugee solidarity in King County.</p>
        </div>

        <div class="milestones-4grid">
          <div class="milestone-card-clean">
            <span class="milestone-year-pill">1978</span>
            <h3 style="font-size:1.2rem; color:var(--navy); margin-bottom:8px;">Founded in Mutual Aid</h3>
            <p style="font-size:0.95rem; color:var(--text-body); line-height:1.55; margin:0;">
              Established as the Southeast Asian Refugee Support network to provide direct translation, emergency relief, and community orientation for arriving families.
            </p>
          </div>

          <div class="milestone-card-clean">
            <span class="milestone-year-pill">1995</span>
            <h3 style="font-size:1.2rem; color:var(--navy); margin-bottom:8px;">Public Schools Partnership</h3>
            <p style="font-size:0.95rem; color:var(--text-body); line-height:1.55; margin:0;">
              Formed after-school tutoring programs inside public high schools, ensuring bilingual homework help and credit recovery for newly arrived ELL students.
            </p>
          </div>

          <div class="milestone-card-clean">
            <span class="milestone-year-pill">2020</span>
            <h3 style="font-size:1.2rem; color:var(--navy); margin-bottom:8px;">Direct Relief & Digital Access</h3>
            <p style="font-size:0.95rem; color:var(--text-body); line-height:1.55; margin:0;">
              Disbursed over $240,000 in emergency rental relief and distributed hundreds of cellular-connected laptops to bridge digital inequities.
            </p>
          </div>

          <div class="milestone-card-clean" style="border-color:var(--teal); box-shadow:0 6px 18px rgba(42,210,201,0.15);">
            <span class="milestone-year-pill" style="color:var(--coral);">May 2027</span>
            <h3 style="font-size:1.2rem; color:var(--navy); margin-bottom:8px;">50th Anniversary Gala</h3>
            <p style="font-size:0.95rem; color:var(--text-body); line-height:1.55; margin:0;">
              Gathering five decades of alumni, families, educators, and community champions at the Seattle Center Pavilion for our landmark celebration.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- WHO WE HELP SECTION (EQUAL-HEIGHT BALANCED CARDS) -->
    <section class="section-who-we-help" id="who-we-help" style="padding:80px 0; background-color:#FFFFFF;">
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

    <!-- STORIES & IMPACT PREVIEW (AUTHENTIC STORIES LINKED TO KANDELIA.ORG & MODAL POPUP) -->
    <section class="section-stories-teaser" style="padding:80px 0; background-color:#F0F2FA;">
      <div class="w">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 40px;">
          <span class="badge badge-teal" style="margin-bottom:12px;">Real Voices • Roots & Routes</span>
          <h2>Stories of Resilience & Belonging</h2>
          <p class="lead">Personal journeys of courage, perseverance, and belonging from Kandelia's storytelling archive in Seattle.</p>
        </div>

        <div class="story-square-grid">
          <!-- Story 1: Sunflower & Tulip -->
          <div class="story-square-card open-story-reader"
               role="button" tabindex="0"
               aria-label="Read full story: {site_data.STORIES[0]['title']}"
               data-title="{site_data.STORIES[0]['title']}"
               data-subtitle="{site_data.STORIES[0]['subtitle']}"
               data-image="{site_data.STORIES[0]['image']}"
               data-quote="{site_data.STORIES[0]['quote']}"
               data-story-html="{html.escape(site_data.STORIES[0]['full_text'])}">
            <div class="story-square-img-wrap">
              <img src="{site_data.STORIES[0]['image']}" alt="{site_data.STORIES[0]['title']}" class="story-img-square" loading="lazy">
            </div>
            <div class="story-square-body">
              <span class="badge badge-coral" style="width:fit-content; margin-bottom:6px;">Roots & Routes</span>
              <h3 style="font-size:1.35rem; color:var(--navy); margin-bottom:8px;">{site_data.STORIES[0]['title']}</h3>
              <p style="font-style:italic; margin-bottom:8px; color:var(--coral); font-weight:600;">"{site_data.STORIES[0]['quote']}"</p>
              <p style="color:var(--text-body); line-height:1.6; font-size:0.98rem;">{site_data.STORIES[0]['short']}</p>
              <div style="display:flex; justify-content:flex-start; align-items:center; margin-top:16px; padding-top:12px; border-top:1px solid #F0F2FA;">
                <button class="card-link-btn" type="button" style="background:none; border:none; padding:0; cursor:pointer; font-weight:700; color:var(--navy); font-size:1rem; display:inline-flex; align-items:center; gap:6px;">
                  Read Full Story <span aria-hidden="true">→</span>
                </button>
              </div>
            </div>
          </div>

          <!-- Story 2: Ana's Story -->
          <div class="story-square-card open-story-reader"
               role="button" tabindex="0"
               aria-label="Read full story: {site_data.STORIES[2]['title']}"
               data-title="{site_data.STORIES[2]['title']}"
               data-subtitle="{site_data.STORIES[2]['subtitle']}"
               data-image="{site_data.STORIES[2]['image']}"
               data-quote="{site_data.STORIES[2]['quote']}"
               data-story-html="{html.escape(site_data.STORIES[2]['full_text'])}">
            <div class="story-square-img-wrap">
              <img src="{site_data.STORIES[2]['image']}" alt="{site_data.STORIES[2]['title']}" class="story-img-square" loading="lazy">
            </div>
            <div class="story-square-body">
              <span class="badge badge-sage" style="width:fit-content; margin-bottom:6px;">Roots & Routes</span>
              <h3 style="font-size:1.35rem; color:var(--navy); margin-bottom:8px;">{site_data.STORIES[2]['title']}</h3>
              <p style="font-style:italic; margin-bottom:8px; color:var(--teal-dark); font-weight:600;">"{site_data.STORIES[2]['quote']}"</p>
              <p style="color:var(--text-body); line-height:1.6; font-size:0.98rem;">{site_data.STORIES[2]['short']}</p>
              <div style="display:flex; justify-content:flex-start; align-items:center; margin-top:16px; padding-top:12px; border-top:1px solid #F0F2FA;">
                <button class="card-link-btn" type="button" style="background:none; border:none; padding:0; cursor:pointer; font-weight:700; color:var(--navy); font-size:1rem; display:inline-flex; align-items:center; gap:6px;">
                  Read Full Story <span aria-hidden="true">→</span>
                </button>
              </div>
            </div>
          </div>
        </div>

        <div style="text-align:center; margin-top:36px; display:flex; justify-content:center; gap:16px; flex-wrap:wrap;">
          <a class="btn btn-outline" href="/stories">Read All Community Stories&nbsp;→</a>
          <a class="btn btn-primary" href="/stories">Official Stories Archive →</a>
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
                <a href="/ways-to-give#give" class="btn btn-outline btn-sm">Support Families →</a>
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
                <a href="/ways-to-give#give" class="btn btn-outline btn-sm">Support Youth →</a>
              </div>
            </div>
          </div>

          <!-- Vehicle Donation Card with Cover Photo -->
          <div class="way-photo-card" style="border:1.5px solid rgba(42,210,201,0.35);">
            <div class="way-photo-wrap">
              <img src="assets/vehicle_donation.jpg" alt="Charity vehicle donation supporting Kandelia programs" loading="lazy">
            </div>
            <div class="way-photo-body">
              <span class="badge badge-blue" style="width:fit-content; margin-bottom:6px;">Turn Wheels into Impact</span>
              <h3>Donate Your Vehicle (CARS)</h3>
              <p>The proceeds from your vehicle directly benefit Kandelia's programs. Both Kandelia and CARS are 501(c)(3) nonprofits, making donations fully tax-deductible.</p>
              <div class="way-photo-action">
                <a href="https://careasy.org/kandelia" target="_blank" rel="noopener noreferrer" class="btn btn-coral btn-sm">
                  CARS Donation →
                </a>
              </div>
            </div>
          </div>
        </div>

        <div style="text-align:center; margin-top:36px;">
          <a class="btn btn-outline" href="/ways-to-give">Explore Ways to Give &amp; Donate&nbsp;→</a>
        </div>
      </div>
    </section>

    {get_support_banner()}
  </main>
'''
home_html += get_footer()

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(home_html)
print("index.html written successfully!")


# ==============================================================================
# 2. GENERATE about.html (ABOUT US, VALUES, 4 MILESTONES, STAFF PHOTO, 2 LEADERS, 9 BOARD PHOTOS, CAREERS)
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

    <!-- BRAND VALUES PLATFORM (5 VALUES IN BALANCED 3+2 LAYOUT) -->
    <section style="padding:80px 0; background-color:#FFFFFF;">
      <div class="w">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 40px;">
          <span class="badge badge-teal" style="margin-bottom:12px;">Guiding Principles</span>
          <h2>Our Core Values</h2>
          <p class="lead">These values drive our daily culture, hiring practices, community advocacy, and strategic decisions.</p>
        </div>

        <div class="values-even-flex">
          <div class="value-card-item" style="background:#F0FAF9; border:1px solid rgba(42,210,201,0.25);">
            <h3 style="font-size:1.25rem; color:var(--navy); margin-bottom:10px;">Inclusion</h3>
            <p style="font-size:0.96rem; color:var(--text-body); line-height:1.6; margin:0;">
              We embrace diversity and believe all people have value and the right to belong. We commit to active listening and questioning assumptions.
            </p>
          </div>
          <div class="value-card-item" style="background:#FEECEE; border:1px solid rgba(244,54,76,0.22);">
            <h3 style="font-size:1.25rem; color:var(--coral); margin-bottom:10px;">Heart</h3>
            <p style="font-size:0.96rem; color:var(--text-body); line-height:1.6; margin:0;">
              We measure our success by the real difference we make in people's lives. We act with care, empathy, kindness, and fun along the way.
            </p>
          </div>
          <div class="value-card-item" style="background:#F4FBE8; border:1px solid rgba(151,215,0,0.25);">
            <h3 style="font-size:1.25rem; color:#2A6615; margin-bottom:10px;">Equity</h3>
            <p style="font-size:0.96rem; color:var(--text-body); line-height:1.6; margin:0;">
              We believe in just and fair inclusion, identifying inequities and taking proactive responsibility for addressing them.
            </p>
          </div>
          <div class="value-card-item" style="background:#ECEEFF; border:1px solid rgba(30,34,170,0.20);">
            <h3 style="font-size:1.25rem; color:var(--navy); margin-bottom:10px;">Relationships</h3>
            <p style="font-size:0.96rem; color:var(--text-body); line-height:1.6; margin:0;">
              We build strong connections with each other, partners, and the communities we serve in the spirit of genuine collaboration.
            </p>
          </div>
          <div class="value-card-item" style="background:#F0FAF9; border:1px solid rgba(42,210,201,0.25);">
            <h3 style="font-size:1.25rem; color:#14857F; margin-bottom:10px;">Excellence</h3>
            <p style="font-size:0.96rem; color:var(--text-body); line-height:1.6; margin:0;">
              We strive to be the best we can be in all we do, applying discipline, organization, and professionalism to our daily work.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- 50-YEAR MILESTONES (EXACTLY 4 EVENLY SPACED MILESTONES) -->
    <section class="section-timeline" id="history" style="padding:80px 0; background-color:#F0F2FA;">
      <div class="w">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 48px;">
          <span class="badge badge-sage" style="margin-bottom:12px;">Five Decades</span>
          <h2>Milestones of Belonging (1978–2028)</h2>
          <p class="lead">Fifty years of immigrant and refugee leadership in South Seattle and across King County.</p>
        </div>

        <div class="milestones-4grid">
          <div class="milestone-card-clean">
            <span class="milestone-year-pill">1978</span>
            <h3 style="font-size:1.2rem; color:var(--navy); margin-bottom:8px;">Founded in Mutual Aid</h3>
            <p style="font-size:0.95rem; color:var(--text-body); line-height:1.55; margin:0;">
              Established as the Southeast Asian Refugee Support network to provide direct translation, emergency relief, and community orientation for arriving families.
            </p>
          </div>

          <div class="milestone-card-clean">
            <span class="milestone-year-pill">1995</span>
            <h3 style="font-size:1.2rem; color:var(--navy); margin-bottom:8px;">Public Schools Partnership</h3>
            <p style="font-size:0.95rem; color:var(--text-body); line-height:1.55; margin:0;">
              Formed formal after-school tutoring partnerships inside high schools, ensuring bilingual homework help and credit recovery for newly arrived ELL students.
            </p>
          </div>

          <div class="milestone-card-clean">
            <span class="milestone-year-pill">2020</span>
            <h3 style="font-size:1.2rem; color:var(--navy); margin-bottom:8px;">Direct Relief & Digital Access</h3>
            <p style="font-size:0.95rem; color:var(--text-body); line-height:1.55; margin:0;">
              Rapidly mobilized over $240,000 in direct emergency assistance, distributed hundreds of cellular-connected laptops, and established virtual support circles.
            </p>
          </div>

          <div class="milestone-card-clean" style="border-color:var(--teal); box-shadow:0 6px 18px rgba(42,210,201,0.15);">
            <span class="milestone-year-pill" style="color:var(--coral);">May 2027</span>
            <h3 style="font-size:1.2rem; color:var(--navy); margin-bottom:8px;">50th Anniversary Gala</h3>
            <p style="font-size:0.95rem; color:var(--text-body); line-height:1.55; margin:0;">
              Gathering five decades of alumni, families, educators, and community champions at the Seattle Center Pavilion for our landmark celebration.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- STAFF PHOTO SECTION (LARGE GROUP PHOTO WITH "Kandelia staff" CAPTION DIRECTLY BELOW) -->
    <section class="section-staff" id="team" style="padding:80px 0; background-color:#FFFFFF;">
      <div class="w">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 40px;">
          <span class="badge badge-teal" style="margin-bottom:12px;">Our Team</span>
          <h2>Kandelia Staff & Leadership</h2>
          <p class="lead">Experienced educators, youth advocates, and community organizers with deep roots in King County.</p>
        </div>

        <!-- Large Staff Group Photograph with Caption -->
        <div style="max-width:960px; margin:0 auto 48px;">
          <div style="border-radius:24px; overflow:hidden; box-shadow:0 12px 36px rgba(30,34,170,0.08); border:1px solid rgba(42,210,201,0.25);">
            <img src="assets/image_9.jpeg" alt="Kandelia staff team gathering together" style="width:100%; height:auto; display:block;">
          </div>
          <p style="font-size:1.05rem; font-weight:600; color:var(--navy); margin-top:14px; text-align:center;">Kandelia dedicated staff & leadership team</p>
        </div>

        <!-- EXECUTIVE DIRECTORS (ONLY TWO CARDS WITH REAL PHOTOS & MODAL BIO EXPANSION) -->
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 32px;">
          <h3 style="font-size:1.5rem; color:var(--navy);">Executive Leadership</h3>
        </div>

        <div class="leadership-2grid">
          <!-- Leader 1: Tram Lam, MNPL -->
          <div class="leader-card-featured open-leader-bio"
               role="button"
               tabindex="0"
               data-name="Tram Lam, MNPL"
               data-role="Co-Executive Director"
               data-photo="assets/tram_lam_headshot_studio.jpg"
               data-languages="English, Vietnamese"
               data-bio="Tram has dedicated over 18 years to non-profit management, immigrant rights, and educational justice in King County. She guides Kandelia's strategic vision with deep reverence for our 50-year mutual aid heritage, overseeing regional community partnerships, long-term sustainability endowment, and systemic advocacy across Washington State."
               data-quote="Our work is about tending to deep roots. Just like the mangrove tree that gives Kandelia its name, we provide a secure, nurturing ecosystem so youth and families can stand strong through any storm.">
            <div class="leader-photo-wrap">
              <img src="assets/tram_lam_headshot_studio.jpg" alt="Tram Lam, MNPL - Co-Executive Director">
            </div>
            <h3 style="font-size:1.35rem; color:var(--navy); margin-bottom:4px;">Tram Lam, MNPL</h3>
            <div style="font-size:0.96rem; font-weight:700; color:var(--teal-dark); margin-bottom:6px;">Co-Executive Director</div>
            <div style="font-size:0.88rem; color:var(--text-muted); margin-bottom:12px;">Languages: English, Vietnamese</div>
            <p style="font-size:0.95rem; color:var(--text-body); line-height:1.55; margin-bottom:18px;">
              Tram has dedicated over 18 years to non-profit management, immigrant rights, and educational justice in King County. She guides Kandelia's strategic vision with deep reverence for our 50-year mutual aid heritage.
            </p>
            <div style="margin-top:auto; width:100%;">
              <button class="btn btn-outline btn-sm"
                      type="button"
                      style="width:100%; text-align:center; display:flex; justify-content:center; align-items:center;"
                      tabindex="-1">
                View Bio & Credentials →
              </button>
            </div>
          </div>

          <!-- Leader 2: Khadar Abdi -->
          <div class="leader-card-featured open-leader-bio"
               role="button"
               tabindex="0"
               data-name="Khadar Abdi"
               data-role="Co-Executive Director"
               data-photo="assets/khadar_abdi_headshot.jpg"
               data-languages="English, Somali, Swahili"
               data-bio="Khadar spearheads our high school cohort models, paid summer internships, and youth leadership initiatives, focusing on culturally affirming mentorship and college-and-career pathways across King County public schools. Having arrived in Seattle as a newcomer himself, he brings authentic lived experience to youth empowerment."
               data-quote="Over 90% of our staff have lived the immigrant and refugee journey themselves. When a family walks through our doors, they are met with shared language, shared empathy, and unconditional dignity.">
            <div class="leader-photo-wrap">
              <img src="assets/khadar_abdi_headshot.jpg" alt="Khadar Abdi - Co-Executive Director">
            </div>
            <h3 style="font-size:1.35rem; color:var(--navy); margin-bottom:4px;">Khadar Abdi</h3>
            <div style="font-size:0.96rem; font-weight:700; color:var(--teal-dark); margin-bottom:6px;">Co-Executive Director</div>
            <div style="font-size:0.88rem; color:var(--text-muted); margin-bottom:12px;">Languages: English, Somali, Swahili</div>
            <p style="font-size:0.95rem; color:var(--text-body); line-height:1.55; margin-bottom:18px;">
              Khadar spearheads our high school cohort models, paid summer internships, and youth leadership initiatives, focusing on culturally affirming mentorship and college-and-career pathways.
            </p>
            <div style="margin-top:auto; width:100%;">
              <button class="btn btn-outline btn-sm"
                      type="button"
                      style="width:100%; text-align:center; display:flex; justify-content:center; align-items:center;"
                      tabindex="-1">
                View Bio & Credentials →
              </button>
            </div>
          </div>
        </div>

        <!-- All Staff Team & Program Coordinators (Direct from kandelia.org) -->
        <div style="max-width:960px; margin:40px auto 0;">
          <div style="background:#FFFFFF; border-radius:18px; padding:28px 32px; border:1px solid rgba(30,34,170,0.12); box-shadow:0 4px 14px rgba(30,34,170,0.04);">
            <div style="text-align:center; margin-bottom:20px;">
              <span class="badge badge-teal" style="margin-bottom:8px;">Program Staff & Coordinators</span>
              <h4 style="font-size:1.3rem; color:var(--navy); font-weight:700; margin:0;">
                Our Dedicated Staff Team
              </h4>
              <p style="font-size:0.92rem; color:var(--text-muted); margin-top:6px; margin-bottom:0;">
                Our multilingual team coordinates high school tutoring, adult education, and community assistance across King County.
              </p>
            </div>
            <div class="staff-directory-grid">
              <div style="padding:14px 18px; background:#F8FAFC; border-radius:12px; border-left:4px solid var(--teal);">
                <div style="font-weight:700; color:var(--navy); font-size:1rem;">Carolina</div>
                <div style="font-size:0.86rem; color:var(--text-muted); margin-top:2px;">Administrative Coordinator</div>
              </div>
              <div style="padding:14px 18px; background:#F8FAFC; border-radius:12px; border-left:4px solid var(--teal);">
                <div style="font-weight:700; color:var(--navy); font-size:1rem;">Gaugdy</div>
                <div style="font-size:0.86rem; color:var(--text-muted); margin-top:2px;">Family Program Coordinator</div>
              </div>
              <div style="padding:14px 18px; background:#F8FAFC; border-radius:12px; border-left:4px solid var(--teal);">
                <div style="font-weight:700; color:var(--navy); font-size:1rem;">Gustavo</div>
                <div style="font-size:0.86rem; color:var(--text-muted); margin-top:2px;">Youth Program Coordinator</div>
              </div>
              <div style="padding:14px 18px; background:#F8FAFC; border-radius:12px; border-left:4px solid var(--teal);">
                <div style="font-weight:700; color:var(--navy); font-size:1rem;">Kelebet</div>
                <div style="font-size:0.86rem; color:var(--text-muted); margin-top:2px;">Youth Program Manager</div>
              </div>
              <div style="padding:14px 18px; background:#F8FAFC; border-radius:12px; border-left:4px solid var(--teal);">
                <div style="font-weight:700; color:var(--navy); font-size:1rem;">Sieng</div>
                <div style="font-size:0.86rem; color:var(--text-muted); margin-top:2px;">Community Engagement Manager</div>
              </div>
              <div style="padding:14px 18px; background:#F8FAFC; border-radius:12px; border-left:4px solid var(--teal);">
                <div style="font-weight:700; color:var(--navy); font-size:1rem;">Thu</div>
                <div style="font-size:0.86rem; color:var(--text-muted); margin-top:2px;">Family Program Manager</div>
              </div>
              <div style="padding:14px 18px; background:#F8FAFC; border-radius:12px; border-left:4px solid var(--teal);">
                <div style="font-weight:700; color:var(--navy); font-size:1rem;">Xochilt</div>
                <div style="font-size:0.86rem; color:var(--text-muted); margin-top:2px;">Development Coordinator</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- BOARD OF DIRECTORS (ALL 9 MEMBERS WITH REAL PHOTOS & MODAL BIO EXPANSION) -->
    <section class="section-board" id="board" style="padding:80px 0; background-color:#F0F2FA;">
      <div class="w">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 48px;">
          <span class="badge badge-sage" style="margin-bottom:12px;">Governance & Stewardship</span>
          <h2>Our Board of Directors</h2>
          <p class="lead">Passionate educators, legal advocates, finance executives, and alumni providing strategic fiduciary governance.</p>
        </div>

        <div class="board-grid-enhanced">
'''

board_photos = [f"assets/board_{i}.jpg" for i in range(1, 10)]

for idx, board in enumerate(site_data.BOARD_MEMBERS):
    photo_src = board.get('photo', board_photos[idx] if idx < len(board_photos) else "assets/board_1.jpg")
    subline = board.get('languages') or board.get('tenure', '')
    escaped_name = html.escape(board['name'])
    escaped_role = html.escape(board['role'])
    escaped_subline = html.escape(subline)
    escaped_bio = html.escape(board['bio'])
    escaped_quote = html.escape(board.get('quote', ''))
    about_html += f'''          <div class="board-card-enhanced open-board-bio"
               role="button"
               tabindex="0"
               data-name="{escaped_name}"
               data-role="{escaped_role}"
               data-tenure="{escaped_subline}"
               data-bio="{escaped_bio}"
               data-quote="{escaped_quote}"
               data-photo="{photo_src}">
            <div class="board-member-photo-frame">
              <img src="{photo_src}" alt="{escaped_name}" loading="lazy">
            </div>
            <h3 class="board-member-name">{escaped_name}</h3>
            <div class="board-member-role">{escaped_role}</div>
            <div class="board-member-meta">{escaped_subline}</div>
            <div class="board-member-actions">
              <button class="btn btn-outline btn-sm"
                      type="button"
                      style="width:100%; text-align:center; display:flex; justify-content:center; align-items:center;"
                      tabindex="-1">
                Read Bio →
              </button>
            </div>
          </div>\n'''

about_html += f'''        </div>
      </div>
    </section>

    <!-- 2026 ANNUAL REPORT -->
    <section class="section-report" id="impact-report" style="padding:80px 0; background-color:#FFFFFF;">
      <div class="w">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 40px; text-align:center; display:flex; flex-direction:column; align-items:center;">
          <span class="badge badge-teal" style="margin-bottom:12px;">Accountability & Impact</span>
          <h2>2026 Community Impact Report</h2>
          <p class="lead" style="text-align:center; margin:0 auto;">Our annual evaluation of student graduation rates, family economic mobility, and direct assistance distribution across King County.</p>
        </div>

        <div class="pinned-report-card">
          <div class="report-cover-box" style="background:#1F22AA; border-radius:20px; padding:32px 24px; color:#FFFFFF; display:flex; flex-direction:column; justify-content:space-between; min-height:240px; box-shadow:0 10px 30px rgba(31,34,170,0.15);">
            <div>
              <span class="badge" style="margin-bottom:12px; border:none; background:rgba(255,255,255,0.2); color:#FFFFFF; font-size:0.75rem; text-transform:uppercase; letter-spacing:0.05em; padding:4px 12px; border-radius:20px; display:inline-block;">Annual Report</span>
              <div style="font-size:1.6rem; font-weight:700; line-height:1.2; color:#FFFFFF; margin-top:8px;">2026 Impact Report</div>
            </div>
            <div>
              <img src="assets/kandelia_logo_horizontal_reverse.png" alt="Kandelia Logo" style="height:32px; width:auto; opacity:0.95; display:block;">
            </div>
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
              <button type="button" class="btn btn-primary open-impact-report-modal">Read 2026 Impact Report&nbsp;→</button>
              <button type="button" class="btn btn-outline open-request-pdf-modal">Request PDF Copy</button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CAREERS & LEADERSHIP (WORK WITH US - 4 DISTINCT GROUPS AS REQUESTED) -->
    <section class="section-careers" id="careers" style="padding:80px 0; background-color:#F0FAF9; border-top:1px solid rgba(42,210,201,0.2);">
      <div class="w">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 48px;">
          <span class="badge badge-blue" style="margin-bottom:12px;">Join Our Team</span>
          <h2>Work With Us</h2>
          <p class="lead">Build meaningful careers advancing equity, youth belonging, and refugee solidarity across King County.</p>
        </div>

        <div style="max-width:920px; margin:0 auto; display:flex; flex-direction:column; gap:40px;">
          <!-- Group 1: Staff Positions -->
          <div class="careers-group">
            <div class="careers-group-header" style="margin-bottom:18px; padding-bottom:12px; border-bottom:2px solid rgba(42,210,201,0.3); display:flex; align-items:center; gap:12px;">
              <span class="badge badge-teal" style="font-weight:700; font-size:0.88rem;">Group 1</span>
              <h3 style="font-size:1.45rem; color:var(--navy); margin:0;">Staff Positions</h3>
            </div>
            <div style="display:flex; flex-direction:column; gap:18px;">
'''

for job in site_data.CAREERS.get('staff', []):
    about_html += f'''              <div class="job-card" style="background:#FFFFFF; border-radius:18px; padding:28px 32px; border:1px solid rgba(42,210,201,0.25); box-shadow:0 4px 14px rgba(30,34,170,0.03);">
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

about_html += '''            </div>
          </div>

          <!-- Group 2: Board Positions -->
          <div class="careers-group">
            <div class="careers-group-header" style="margin-bottom:18px; padding-bottom:12px; border-bottom:2px solid rgba(151,215,0,0.35); display:flex; align-items:center; gap:12px;">
              <span class="badge badge-green" style="font-weight:700; font-size:0.88rem;">Group 2</span>
              <h3 style="font-size:1.45rem; color:var(--navy); margin:0;">Board Positions</h3>
            </div>
            <div style="display:flex; flex-direction:column; gap:18px;">
'''

for job in site_data.CAREERS.get('board', []):
    about_html += f'''              <div class="job-card" style="background:#FFFFFF; border-radius:18px; padding:28px 32px; border:1px solid rgba(42,210,201,0.25); box-shadow:0 4px 14px rgba(30,34,170,0.03);">
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

about_html += '''            </div>
          </div>

          <!-- Group 3: Contracted Opportunities -->
          <div class="careers-group">
            <div class="careers-group-header" style="margin-bottom:18px; padding-bottom:12px; border-bottom:2px solid rgba(31,34,170,0.25); display:flex; align-items:center; gap:12px;">
              <span class="badge badge-blue" style="font-weight:700; font-size:0.88rem;">Group 3</span>
              <h3 style="font-size:1.45rem; color:var(--navy); margin:0;">Contracted Opportunities</h3>
            </div>
            <div style="display:flex; flex-direction:column; gap:18px;">
'''

for job in site_data.CAREERS.get('contract', []):
    about_html += f'''              <div class="job-card" style="background:#FFFFFF; border-radius:18px; padding:28px 32px; border:1px solid rgba(42,210,201,0.25); box-shadow:0 4px 14px rgba(30,34,170,0.03);">
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

about_html += '''            </div>
          </div>

          <!-- Group 4: Youth Leadership -->
          <div class="careers-group">
            <div class="careers-group-header" style="margin-bottom:18px; padding-bottom:12px; border-bottom:2px solid rgba(244,54,76,0.25); display:flex; align-items:center; gap:12px;">
              <span class="badge badge-coral" style="font-weight:700; font-size:0.88rem;">Group 4</span>
              <h3 style="font-size:1.45rem; color:var(--navy); margin:0;">Youth Leadership</h3>
            </div>
            <div style="display:flex; flex-direction:column; gap:18px;">
'''

for job in site_data.CAREERS.get('youth', []):
    about_html += f'''              <div class="job-card" style="background:#FFFFFF; border-radius:18px; padding:28px 32px; border:1px solid rgba(42,210,201,0.25); box-shadow:0 4px 14px rgba(30,34,170,0.03);">
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

about_html += f'''            </div>
          </div>

          <div style="text-align:center; margin-top:32px;">
            <a href="/careers" class="btn btn-primary btn-lg">
              Explore Careers &amp; Benefits&nbsp;→
            </a>
          </div>
        </div>
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
# 3. GENERATE get-help.html (TWO PILLARS: YOUTH & FAMILY, NO BUTTONS ON PILLARS, MAIN BUTTON ON ELIGIBILITY, NO SUPPORT BANNER)
# ==============================================================================
print("Generating get-help.html...")
help_html = get_head("Get Help & Programs | Kandelia", "Explore Kandelia's culturally responsive youth and family programs in King County.")
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
          We partner with newly arrived immigrant and refugee youth and families across King County with free, culturally affirming educational, digital, and emergency navigation programs.
        </p>
      </div>
    </section>

    <!-- TWO PILLARS: YOUTH & FAMILY (IMAGE ON TOP, DESCRIPTION BELOW, NO BUTTONS ON CARDS) -->
    <section style="padding:80px 0; background-color:#FFFFFF;">
      <div class="w">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 48px;">
          <span class="badge badge-sage" style="margin-bottom:12px;">Our Two Core Pillars</span>
          <h2>Comprehensive Support Programs</h2>
          <p class="lead">Every program is designed around active listening, language access, and whole-family empowerment.</p>
        </div>

        <div class="pillars-2grid">
          <!-- Pillar 1: Youth Success & High School Pathways -->
          <div class="pillar-2card" id="high-school">
            <img src="assets/image_3.jpeg" alt="Kandelia high school students smiling in a classroom" class="pillar-2card-img" loading="lazy">
            <div class="pillar-2card-body">
              <span class="badge badge-sage" style="width:fit-content; margin-bottom:8px;">Ages 14–21</span>
              <h3 style="font-size:1.35rem; color:var(--navy); margin-bottom:12px;">Youth Success & High School Pathways</h3>
              <p style="font-size:1rem; color:var(--text-body); line-height:1.6; margin-bottom:16px;">
                Dedicated after-school tutoring, ELL credit recovery, bilingual homework clubs, and post-secondary planning inside King County public high schools.
              </p>
              <ul class="program-feature-list" style="margin-bottom:0;">
                <li>{ICON_CHECK} 1-on-1 academic mentoring & English conversation practice</li>
                <li>{ICON_CHECK} Graduation audit & college / vocational application guidance</li>
                <li>{ICON_CHECK} Paid summer youth leadership stipends and community projects</li>
                <li>{ICON_CHECK} Culturally responsive peer mentoring and career exploration</li>
              </ul>
            </div>
          </div>

          <!-- Pillar 2: Family Flourishing & Digital Literacy -->
          <div class="pillar-2card" id="family">
            <img src="assets/image_4.jpeg" alt="Kandelia family gathering in a collaborative workshop" class="pillar-2card-img" loading="lazy">
            <div class="pillar-2card-body">
              <span class="badge badge-teal" style="width:fit-content; margin-bottom:8px;">Parents & Adults</span>
              <h3 style="font-size:1.35rem; color:var(--navy); margin-bottom:12px;">Family Flourishing & Digital Literacy</h3>
              <p style="font-size:1rem; color:var(--text-body); line-height:1.6; margin-bottom:16px;">
                Hands-on computer workshops designed for adult caregivers to navigate school district portals (The Source), email, digital banking, and job applications.
              </p>
              <ul class="program-feature-list" style="margin-bottom:0;">
                <li>{ICON_CHECK} Free Wi-Fi hotspots and subsidized home computer setups</li>
                <li>{ICON_CHECK} Multilingual adult ESL cohorts in evening and weekend sessions</li>
                <li>{ICON_CHECK} Direct emergency family rental assistance and utility stabilization</li>
                <li>{ICON_CHECK} Healthcare navigation, tenant rights, and school system orientation</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ELIGIBILITY & INTAKE SECTION (HOLDS MAIN ACTION BUTTON TO ENROLL/CONTACT) -->
    <section class="section-eligibility" id="eligibility" style="padding:80px 0; background-color:#F0FAF9; border-top:1px solid rgba(42,210,201,0.2);">
      <div class="w" style="max-width:880px; margin:0 auto;">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 36px; text-align:center; display:flex; flex-direction:column; align-items:center;">
          <span class="badge badge-blue" style="margin-bottom:12px;">Simple & Barrier-Free</span>
          <h2>Program Eligibility Guidelines</h2>
          <p class="lead" style="text-align:center; margin:0 auto;">All Kandelia programs are 100% free of charge. We warmly welcome immigrants, refugees, asylees, and first-generation families.</p>
        </div>

        <div class="eligibility-card" style="background:#FFFFFF; border-radius:24px; padding:36px 40px; border:1px solid rgba(42,210,201,0.25); box-shadow:0 6px 20px rgba(30,34,170,0.04);">
          <h3 style="font-size:1.35rem; color:var(--navy); margin-bottom:14px;">You are eligible for our programs if:</h3>
          <ul style="list-style-type:disc; padding-left:24px; margin-bottom:28px; font-size:1.02rem; color:var(--text-body); line-height:1.7;">
            <li>You or a family member are an immigrant, refugee, asylee, or humanitarian parolee residing in King County.</li>
            <li>For youth programs: You are between the ages of 14 and 21 and enrolled in a King County middle or high school.</li>
            <li>For adult workshops: You are a parent, caregiver, or adult seeking English language or digital literacy skills.</li>
            <li>All languages, countries of origin, and immigration documentation statuses are embraced without barrier or disclosure requirements.</li>
          </ul>

          <div class="eligibility-cta-box" style="background:#F0F2FA; border-radius:18px; padding:24px 28px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:20px;">
            <div>
              <strong style="color:var(--navy); font-size:1.1rem; display:block; margin-bottom:4px;">Ready to enroll or have questions?</strong>
              <span style="font-size:0.95rem; color:var(--text-muted);">Call our intake line at <strong>206-760-1573</strong> or connect with an advocate directly.</span>
            </div>
            <!-- Main Action Button to Enroll / Contact -->
            <button type="button" class="btn btn-primary btn-lg open-intake-modal" style="font-weight:700;">
              Enroll or Contact Advocate →
            </button>
          </div>
        </div>
      </div>
    </section>
  </main>
'''
help_html += get_footer()

with open('get-help.html', 'w', encoding='utf-8') as f:
    f.write(help_html)
print("get-help.html written successfully!")


# ==============================================================================
# 4. GENERATE ways-to-give.html (EXACTLY THREE CARDS: GIVE, VOLUNTEER, PARTNER WITH UPDATED LINKS)
# ==============================================================================
print("Generating ways-to-give.html...")
ways_html = get_head("Ways to Give | Kandelia", "Explore flexible pathways to support Kandelia: direct giving, volunteering, and institutional partnerships.")
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
          Your partnership ensures immigrant and refugee youth stay on track to graduate, while equipping newcomer parents with the tools to build economic resilience.
        </p>
      </div>
    </section>

    <!-- EXACTLY THREE CARDS: GIVE, VOLUNTEER, PARTNER (WITH UPDATED CLIENT LINKS) -->
    <section style="padding:80px 0; background-color:#FFFFFF;">
      <div class="w">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 48px;">
          <span class="badge badge-teal" style="margin-bottom:12px;">Meaningful Partnership</span>
          <h2>Three Meaningful Ways to Support Our Mission</h2>
          <p class="lead">Choose the pathway that fits your passion and fuels lasting community transformation across Seattle.</p>
        </div>

        <div class="ways-3card-grid">
          <!-- Card 1: Give -->
          <div class="way-3card" id="give">
            <img src="assets/image_4.jpeg" alt="Kandelia family gathering in a collaborative workshop" class="way-3card-img" loading="lazy">
            <div class="way-3card-body">
              <span class="badge badge-teal" style="width:fit-content; margin-bottom:8px;">Financial & Fund Support</span>
              <h3 style="font-size:1.35rem; color:var(--navy); margin-bottom:12px;">Give to Kandelia</h3>
              <p>
                Your tax-deductible contributions directly fund high school tutoring, adult digital workshops, and emergency family relief funds. Choose from flexible one-time, monthly, or fund-designated gifts.
              </p>
              <div style="margin-top:auto;">
                <a href="https://kandelia-bloom.kindful.com/embeds/75568458-194c-4924-8a1b-de2cd76e4f92" target="_blank" rel="noopener noreferrer" class="btn btn-coral">
                  Donate Online Now →
                </a>
              </div>
            </div>
          </div>

          <!-- Card 2: Volunteer (Google Form Link as requested) -->
          <div class="way-3card" id="volunteer">
            <img src="assets/image_3.jpeg" alt="Kandelia high school students smiling with tutors" class="way-3card-img" loading="lazy">
            <div class="way-3card-body">
              <span class="badge badge-sage" style="width:fit-content; margin-bottom:8px;">Mentorship & Tutoring</span>
              <h3 style="font-size:1.35rem; color:var(--navy); margin-bottom:12px;">Volunteer With Us</h3>
              <p>
                Share your skills, professional experience, and cultural empathy. Volunteer as an after-school tutor, career mentor, digital literacy coach, or event volunteer for our May 2027 50th Anniversary Gala.
              </p>
              <div style="margin-top:auto;">
                <a href="https://docs.google.com/forms/d/e/1FAIpQLSeXxISZyibWTeAGMH7MU5rUYerKFk0--B1PB0rmNZNR4c20HQ/viewform" target="_blank" rel="noopener noreferrer" class="btn btn-primary">
                  Sign Up to Volunteer →
                </a>
              </div>
            </div>
          </div>

          <!-- Card 3: Partner (Email to Info@kandelia.org as requested) -->
          <div class="way-3card" id="partner">
            <img src="assets/image_9.jpeg" alt="Community and corporate partners collaborating at Kandelia" class="way-3card-img" loading="lazy">
            <div class="way-3card-body">
              <span class="badge badge-blue" style="width:fit-content; margin-bottom:8px;">Institutional Alliances</span>
              <h3 style="font-size:1.35rem; color:var(--navy); margin-bottom:12px;">Partner With Us</h3>
              <p>
                School districts, corporate employers, and regional foundations partner with Kandelia through institutional grants, corporate matching gifts, community sponsorships, and paid youth internship placements. Reach our team directly at <a href="mailto:Info@kandelia.org" style="color:var(--teal-dark); font-weight:700; text-decoration:underline;">Info@kandelia.org</a>.
              </p>
              <div style="margin-top:auto;">
                <a href="mailto:Info@kandelia.org" class="btn btn-outline open-partner-modal" style="width:100%; text-align:center; display:flex; justify-content:center; align-items:center;" aria-label="Open partnership contact information">
                  Partner With Us →
                </a>
              </div>
            </div>
          </div>
        </div>

        <div style="text-align:center; margin-top:48px;">
          <a class="btn btn-primary btn-lg" href="/giving">View Donation Tiers&nbsp;→</a>
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
# 5. GENERATE stories.html (AUTHENTIC STORIES + MOVING TESTIMONIALS CAROUSEL)
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

    <!-- AUTHENTIC IMMIGRANT STORIES (MATCHING KANDELIA.ORG ROOTS & ROUTES) -->
    <section style="padding:80px 0; background-color:#FFFFFF;" id="stories-grid-container">
      <div class="w">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 40px;">
          <span class="badge badge-sage" style="margin-bottom:12px;">Participant Journeys • Roots & Routes</span>
          <h2>Roots & Routes Stories</h2>
          <p class="lead">Click on any story card to read the full first-person narrative directly on this page.</p>
        </div>

        <div class="story-square-grid">
'''

for idx, story in enumerate(site_data.STORIES):
    stories_html += f'''          <!-- Story: {story['title']} -->
          <div class="story-square-card open-story-reader"
               role="button" tabindex="0"
               aria-label="Read full story: {story['title']}"
               data-title="{story['title']}"
               data-subtitle="{story['subtitle']}"
               data-image="{story['image']}"
               data-quote="{story['quote']}"
               data-story-html="{html.escape(story['full_text'])}">
            <div class="story-square-img-wrap">
              <img src="{story['image']}" alt="{story['title']}" class="story-img-square" loading="lazy">
            </div>
            <div class="story-square-body">
              <span class="badge badge-coral" style="width:fit-content; margin-bottom:6px;">Roots & Routes</span>
              <h3 style="font-size:1.35rem; color:var(--navy); margin-bottom:8px;">{story['title']}</h3>
              <p style="font-style:italic; margin-bottom:8px; color:var(--coral); font-weight:600;">"{story['quote']}"</p>
              <p style="color:var(--text-body); line-height:1.6; font-size:0.98rem;">{story['short']}</p>
              <div style="display:flex; justify-content:flex-start; align-items:center; margin-top:16px; padding-top:12px; border-top:1px solid #F0F2FA;">
                <button class="card-link-btn" type="button" style="background:none; border:none; padding:0; cursor:pointer; font-weight:700; color:var(--navy); font-size:1rem; display:inline-flex; align-items:center; gap:6px;">
                  Read Full Story <span aria-hidden="true">→</span>
                </button>
              </div>
            </div>
          </div>\n'''

stories_html += f'''        </div>

        <div style="text-align:center; margin-top:48px; background:#F0FAF9; border-radius:20px; padding:36px 24px; border:1px solid rgba(42,210,201,0.3); max-width:840px; margin-left:auto; margin-right:auto;">
          <h3 style="font-size:1.4rem; color:var(--navy); margin-bottom:10px;">Empowering Every Journey</h3>
          <p style="font-size:1.05rem; color:var(--text-body); max-width:640px; margin:0 auto 20px; line-height:1.6;">
            These authentic stories reflect the resilience and determination of our participants. Partner with Kandelia to ensure every newly arrived immigrant and refugee has the tools, education, and community to flourish.
          </p>
          <div style="display:flex; justify-content:center; gap:16px; flex-wrap:wrap;">
            <a class="btn btn-primary" href="/giving">Donate to Support Stories →</a>
            <a class="btn btn-outline" href="/get-help">Request Community Support</a>
          </div>
        </div>
      </div>
    </section>

    {get_testimonial_carousel_html("testimonials-carousel")}

    <!-- 2026 ANNUAL REPORT -->
    <section class="section-report" id="metrics" style="padding:80px 0; background-color:#FFFFFF;">
      <div class="w">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 40px; text-align:center; display:flex; flex-direction:column; align-items:center;">
          <span class="badge badge-teal" style="margin-bottom:12px;">Measurable Impact</span>
          <h2>2026 Community Impact Report</h2>
          <p class="lead" style="text-align:center; margin:0 auto;">Transparent outcomes from our student graduation cohorts, emergency family fund, and adult digital literacy classes.</p>
        </div>

        <div class="pinned-report-card">
          <div class="report-cover-box" style="background:#1F22AA; border-radius:20px; padding:32px 24px; color:#FFFFFF; display:flex; flex-direction:column; justify-content:space-between; min-height:240px; box-shadow:0 10px 30px rgba(31,34,170,0.15);">
            <div>
              <span class="badge" style="margin-bottom:12px; border:none; background:rgba(255,255,255,0.2); color:#FFFFFF; font-size:0.75rem; text-transform:uppercase; letter-spacing:0.05em; padding:4px 12px; border-radius:20px; display:inline-block;">Annual Report</span>
              <div style="font-size:1.6rem; font-weight:700; line-height:1.2; color:#FFFFFF; margin-top:8px;">2026 Impact Report</div>
            </div>
            <div>
              <img src="assets/kandelia_logo_horizontal_reverse.png" alt="Kandelia Logo" style="height:32px; width:auto; opacity:0.95; display:block;">
            </div>
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
              <button type="button" class="btn btn-primary open-impact-report-modal">Read 2026 Impact Report&nbsp;→</button>
              <button type="button" class="btn btn-outline open-request-pdf-modal">Request PDF Copy</button>
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
# 6. GENERATE giving.html (GIVING TIERS, MONTHLY DONOR, MOVING TESTIMONIALS CAROUSEL, NO SUPPORT BANNER)
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

    <!-- MONTHLY DONOR! HIGHLIGHT SECTION -->
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

    <!-- MORE MEANINGFUL WAYS TO SUPPORT KANDELIA (REMOVED MONTHLY GIVING AS REQUESTED) -->
    <section class="section-ways-to-give" style="padding:80px 0; background-color:#FFFFFF;">
      <div class="w">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 40px;">
          <span class="badge badge-green" style="margin-bottom:12px;">Diverse Giving Options</span>
          <h2>More Meaningful Ways to Support Kandelia</h2>
          <p class="lead">From workplace matching gifts to vehicle donations, there are many flexible pathways to advance refugee and immigrant equity.</p>
        </div>

        <div class="giving-options-grid">
          <!-- Option 1: Employer Gift Matching -->
          <div class="way-card" style="background:#FFFFFF; border-radius:20px; padding:28px 24px; border:1px solid rgba(42,210,201,0.25); box-shadow:0 4px 14px rgba(30,34,170,0.04); display:flex; flex-direction:column;">
            <div class="way-icon-bubble" style="background:#F4FBE8; color:#2A6615; width:52px; height:52px; border-radius:14px; display:flex; align-items:center; justify-content:center; margin-bottom:18px;">
              {ICON_GIFT}
            </div>
            <h3 class="way-title" style="font-size:1.2rem; color:var(--navy); margin-bottom:10px;">Employer Matching Gifts</h3>
            <p class="way-desc" style="font-size:0.95rem; color:var(--text-body); line-height:1.6; margin-bottom:16px;">
              Double or triple your impact! Major employers (Microsoft, Boeing, Starbucks, Google) match charitable gifts 1:1. Request a match through your company portal.
            </p>
            <div style="margin-top:auto;">
              <a href="https://kandelia-bloom.kindful.com" target="_blank" rel="noopener" class="btn btn-outline btn-sm">Check Match →</a>
            </div>
          </div>

          <!-- Option 2: DAFs & Stock -->
          <div class="way-card" style="background:#FFFFFF; border-radius:20px; padding:28px 24px; border:1px solid rgba(42,210,201,0.25); box-shadow:0 4px 14px rgba(30,34,170,0.04); display:flex; flex-direction:column;">
            <div class="way-icon-bubble" style="background:#E6FAF9; color:#14857F; width:52px; height:52px; border-radius:14px; display:flex; align-items:center; justify-content:center; margin-bottom:18px;">
              {ICON_BANK}
            </div>
            <h3 class="way-title" style="font-size:1.2rem; color:var(--navy); margin-bottom:10px;">Donor-Advised Funds (DAF)</h3>
            <p class="way-desc" style="font-size:0.95rem; color:var(--text-body); line-height:1.6; margin-bottom:16px;">
              Recommend a grant from your DAF or make direct wire transfers to receive optimal tax benefits while uplifting our communities.
            </p>
            <div style="margin-top:auto;">
              <button type="button" class="btn btn-outline btn-sm open-daf-modal">Give via DAF / Wire →</button>
            </div>
          </div>

          <!-- Option 3: Dedicated Vehicle Donation Card -->
          <div class="way-card" style="background:#FFFFFF; border-radius:20px; padding:28px 24px; border:2px solid rgba(42,210,201,0.40); box-shadow:0 8px 20px rgba(42,210,201,0.08); display:flex; flex-direction:column;">
            <div class="way-icon-bubble" style="background:#ECEEFF; color:var(--teal); width:52px; height:52px; border-radius:14px; display:flex; align-items:center; justify-content:center; margin-bottom:18px;">
              {ICON_CAR}
            </div>
            <h3 class="way-title" style="font-size:1.2rem; color:var(--navy); margin-bottom:10px;">Vehicle Donation Program</h3>
            <p class="way-desc" style="font-size:0.95rem; color:var(--text-body); line-height:1.6; margin-bottom:16px;">
              The proceeds from your vehicle will directly benefit Kandelia's programs. Both Kandelia and CARS are 501(c)(3) nonprofit organizations, and donations through this program are tax deductible. Click the link below to fuel brighter futures!
            </p>
            <div style="margin-top:auto;">
              <a href="https://careasy.org/kandelia" target="_blank" rel="noopener noreferrer" class="btn btn-coral btn-sm">
                CARS Donation →
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- MOVING TESTIMONIALS CAROUSEL (ALSO ON GIVING PAGE AS REQUESTED) -->
    {get_testimonial_carousel_html("giving-testimonials-carousel")}

    <!-- DONATION & STEWARDSHIP FAQ ACCORDION (NO INTERNAL NOTES) -->
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
  </main>
'''
giving_html += get_footer()

with open('giving.html', 'w', encoding='utf-8') as f:
    f.write(giving_html)
print("giving.html written successfully!")


# ==============================================================================
# 7. GENERATE careers.html (DEDICATED CAREERS PAGE WITH CULTURE, BENEFITS, OPEN ROLES & AYAB)
# ==============================================================================
print("Generating careers.html...")
careers_html = get_head("Careers & Opportunities | Kandelia", "Explore staff, board, contracted, and youth leadership opportunities at Kandelia in Seattle. Help remove barriers for immigrant and refugee communities.")
careers_html += get_header("careers")
careers_html += f'''
  <main id="main-content">
    {SVG_HEART_CLIP}

    <!-- PAGE HERO -->
    <section class="inner-hero" id="overview">
      <div class="w inner-hero-content">
        <span class="badge badge-teal">Join Our Team • Flourish Together</span>
        <h1 class="inner-hero-title">Careers at Kandelia</h1>
        <p class="inner-hero-lead">
          Do you want to help break down barriers so that immigrant and refugee communities can thrive? Build a purposeful career advancing holistic education, systemic navigation, and cultural belonging across Seattle and King County.
        </p>
        <div style="display:flex; gap:14px; justify-content:center; margin-top:24px; flex-wrap:wrap;">
          <a href="#open-positions" class="btn btn-primary btn-lg">View Open Positions ↓</a>
          <a href="#culture" class="btn btn-outline btn-lg">Why Work With Us</a>
        </div>
      </div>
    </section>

    <!-- CULTURE, MISSION & BENEFITS -->
    <section id="culture" style="padding:80px 0; background-color:#FFFFFF;">
      <div class="w">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 48px;">
          <span class="badge badge-sage" style="margin-bottom:12px;">Workplace Culture & Wellness</span>
          <h2>Why Work at Kandelia</h2>
          <p class="lead">
            We are an immigrant-led, multicultural organization dedicated to equity, heart, and mutual respect. We invest deeply in our team members with competitive compensation, robust wellness benefits, and meaningful opportunities for growth.
          </p>
        </div>

        <div class="careers-benefits-grid">
          <!-- Benefit 1 -->
          <div style="background:#F0FAF9; border-radius:20px; padding:32px; border:1px solid rgba(42,210,201,0.25);">
            <div style="width:48px; height:48px; border-radius:12px; background:#14857F; color:#fff; display:grid; place-items:center; margin-bottom:18px;">
              <svg style="width:24px; height:24px; fill:none; stroke:currentColor; stroke-width:2;" viewBox="0 0 24 24"><path d="M22 12h-4l-3 9L9 3l-3 9H2"></path></svg>
            </div>
            <h3 style="font-size:1.25rem; color:var(--navy); margin-bottom:10px;">Comprehensive Healthcare</h3>
            <p style="font-size:0.96rem; color:var(--text-body); line-height:1.6; margin:0;">
              100% employer-covered options for comprehensive medical, dental, and vision insurance for full-time staff, with generous dependent support.
            </p>
          </div>

          <!-- Benefit 2 -->
          <div style="background:#FEECEE; border-radius:20px; padding:32px; border:1px solid rgba(244,54,76,0.22);">
            <div style="width:48px; height:48px; border-radius:12px; background:var(--coral); color:#fff; display:grid; place-items:center; margin-bottom:18px;">
              <svg style="width:24px; height:24px; fill:none; stroke:currentColor; stroke-width:2;" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
            </div>
            <h3 style="font-size:1.25rem; color:var(--coral); margin-bottom:10px;">Generous Paid Time Off</h3>
            <p style="font-size:0.96rem; color:var(--text-body); line-height:1.6; margin:0;">
              15+ paid vacation days, 12 recognized holidays, personal wellness days, and an annual paid winter break closure so our team can rest and recharge.
            </p>
          </div>

          <!-- Benefit 3 -->
          <div style="background:#ECEEFF; border-radius:20px; padding:32px; border:1px solid rgba(30,34,170,0.20);">
            <div style="width:48px; height:48px; border-radius:12px; background:var(--navy); color:#fff; display:grid; place-items:center; margin-bottom:18px;">
              <svg style="width:24px; height:24px; fill:none; stroke:currentColor; stroke-width:2;" viewBox="0 0 24 24"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>
            </div>
            <h3 style="font-size:1.25rem; color:var(--navy); margin-bottom:10px;">401(k) Retirement Match</h3>
            <p style="font-size:0.96rem; color:var(--text-body); line-height:1.6; margin:0;">
              Retirement plan with organizational matching contributions to empower long-term financial security and retirement readiness for our employees.
            </p>
          </div>

          <!-- Benefit 4 -->
          <div style="background:#F4FBE8; border-radius:20px; padding:32px; border:1px solid rgba(151,215,0,0.25);">
            <div style="width:48px; height:48px; border-radius:12px; background:#2A6615; color:#fff; display:grid; place-items:center; margin-bottom:18px;">
              <svg style="width:24px; height:24px; fill:none; stroke:currentColor; stroke-width:2;" viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
            </div>
            <h3 style="font-size:1.25rem; color:#2A6615; margin-bottom:10px;">Culturally Affirming Space</h3>
            <p style="font-size:0.96rem; color:var(--text-body); line-height:1.6; margin:0;">
              Over 22 languages spoken across our team. We celebrate lived immigrant experience, community wisdom, and cultural heritage as true professional assets.
            </p>
          </div>

          <!-- Benefit 5 -->
          <div style="background:#F0FAF9; border-radius:20px; padding:32px; border:1px solid rgba(42,210,201,0.25);">
            <div style="width:48px; height:48px; border-radius:12px; background:#14857F; color:#fff; display:grid; place-items:center; margin-bottom:18px;">
              <svg style="width:24px; height:24px; fill:none; stroke:currentColor; stroke-width:2;" viewBox="0 0 24 24"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
            </div>
            <h3 style="font-size:1.25rem; color:var(--navy); margin-bottom:10px;">Professional Growth</h3>
            <p style="font-size:0.96rem; color:var(--text-body); line-height:1.6; margin:0;">
              Annual professional development budgets, leadership coaching, conference sponsorships, and clear internal career progression pathways.
            </p>
          </div>

          <!-- Benefit 6 -->
          <div style="background:#FEECEE; border-radius:20px; padding:32px; border:1px solid rgba(244,54,76,0.22);">
            <div style="width:48px; height:48px; border-radius:12px; background:var(--coral); color:#fff; display:grid; place-items:center; margin-bottom:18px;">
              <svg style="width:24px; height:24px; fill:none; stroke:currentColor; stroke-width:2;" viewBox="0 0 24 24"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>
            </div>
            <h3 style="font-size:1.25rem; color:var(--coral); margin-bottom:10px;">Flexible & Hybrid Scheduling</h3>
            <p style="font-size:0.96rem; color:var(--text-body); line-height:1.6; margin:0;">
              Hybrid scheduling, supportive remote-work allowances, and fully subsidized regional transit (ORCA) passes for sustainable commuting.
            </p>
          </div>
        </div>

        <!-- Mission Quote Callout -->
        <div style="background:linear-gradient(135deg, #1E22AA 0%, #12263A 100%); border-radius:24px; padding:44px 36px; color:#FFFFFF; text-align:center; max-width:880px; margin:0 auto; box-shadow:0 12px 36px rgba(30,34,170,0.18);">
          <blockquote style="font-size:clamp(1.2rem, 2vw, 1.55rem); line-height:1.5; font-style:italic; margin:0 0 16px; border:none; padding:0; color:#FFFFFF;">
            "We remove barriers to opportunities so immigrant and refugee communities can flourish without compromising values, heritage or ethnicity."
          </blockquote>
          <span style="font-size:0.95rem; opacity:0.85; text-transform:uppercase; letter-spacing:0.06em; font-weight:600;">Kandelia Mission Statement</span>
        </div>
      </div>
    </section>

    <!-- OPEN POSITIONS (4 DISTINCT GROUPS) -->
    <section id="open-positions" style="padding:80px 0; background-color:#F0F2FA; border-top:1px solid rgba(42,210,201,0.2);">
      <div class="w">
        <div class="section-header text-center" style="max-width:760px; margin:0 auto 48px;">
          <span class="badge badge-blue" style="margin-bottom:12px;">Explore Opportunities</span>
          <h2>Open Positions & Leadership Roles</h2>
          <p class="lead">
            Join our mission across four distinct engagement pathways: full-time staff, volunteer board governance, specialized consultants, and youth leadership fellowships.
          </p>
        </div>

        <div style="max-width:960px; margin:0 auto; display:flex; flex-direction:column; gap:48px;">
          <!-- Group 1: Staff Positions -->
          <div class="careers-group">
            <div class="careers-group-header" style="margin-bottom:20px; padding-bottom:14px; border-bottom:3px solid var(--teal); display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:12px;">
              <div style="display:flex; align-items:center; gap:12px;">
                <span class="badge badge-teal" style="font-weight:700; font-size:0.88rem;">Staff Positions</span>
                <h3 style="font-size:1.5rem; color:var(--navy); margin:0;">Full-Time Program & Operations</h3>
              </div>
              <span style="font-size:0.92rem; color:var(--text-muted); font-weight:600;">2 Active Openings</span>
            </div>
            <div style="display:flex; flex-direction:column; gap:20px;">
'''

for job in site_data.CAREERS.get('staff', []):
    careers_html += f'''              <div class="job-card" style="background:#FFFFFF; border-radius:20px; padding:32px; border:1px solid rgba(42,210,201,0.25); box-shadow:0 4px 16px rgba(30,34,170,0.04);">
                <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:14px; margin-bottom:14px;">
                  <div>
                    <h4 style="font-size:1.4rem; color:var(--navy); margin-bottom:8px; font-weight:700;">{job['title']}</h4>
                    <div style="display:flex; gap:10px; flex-wrap:wrap;">
                      <span class="badge badge-sage">{job['type']}</span>
                      <span class="badge">{job['location']}</span>
                      <span class="badge badge-blue">{job['compensation']}</span>
                    </div>
                  </div>
                  <a href="mailto:careers@kandelia.org?subject=Application for {job['title']}" class="btn btn-primary btn-sm" style="border-radius:20px; padding:8px 22px;">Apply Now →</a>
                </div>
                <p style="font-size:1rem; color:var(--text-body); line-height:1.65; margin-bottom:14px;">{job['description']}</p>
                <div class="job-qualifications" style="font-size:0.92rem; color:var(--text-dark); background:#F0F2FA; border-left:4px solid var(--navy); padding:10px 16px; border-radius:0 10px 10px 0; line-height:1.55;">
                  <strong>Qualifications:</strong> {job['qualifications']}
                </div>
              </div>\n'''

careers_html += '''            </div>
          </div>

          <!-- Group 2: Board Positions -->
          <div class="careers-group">
            <div class="careers-group-header" style="margin-bottom:20px; padding-bottom:14px; border-bottom:3px solid #2A6615; display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:12px;">
              <div style="display:flex; align-items:center; gap:12px;">
                <span class="badge badge-green" style="font-weight:700; font-size:0.88rem;">Board of Directors</span>
                <h3 style="font-size:1.5rem; color:var(--navy); margin:0;">Governance & Fiduciary Leadership</h3>
              </div>
              <span style="font-size:0.92rem; color:var(--text-muted); font-weight:600;">2 Active Openings</span>
            </div>
            <div style="display:flex; flex-direction:column; gap:20px;">
'''

for job in site_data.CAREERS.get('board', []):
    careers_html += f'''              <div class="job-card" style="background:#FFFFFF; border-radius:20px; padding:32px; border:1px solid rgba(42,210,201,0.25); box-shadow:0 4px 16px rgba(30,34,170,0.04);">
                <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:14px; margin-bottom:14px;">
                  <div>
                    <h4 style="font-size:1.4rem; color:var(--navy); margin-bottom:8px; font-weight:700;">{job['title']}</h4>
                    <div style="display:flex; gap:10px; flex-wrap:wrap;">
                      <span class="badge badge-sage">{job['type']}</span>
                      <span class="badge">{job['location']}</span>
                      <span class="badge badge-blue">{job['compensation']}</span>
                    </div>
                  </div>
                  <a href="mailto:careers@kandelia.org?subject=Application for {job['title']}" class="btn btn-outline btn-sm" style="border-radius:20px; padding:8px 22px;">Inquire / Apply →</a>
                </div>
                <p style="font-size:1rem; color:var(--text-body); line-height:1.65; margin-bottom:14px;">{job['description']}</p>
                <div class="job-qualifications" style="font-size:0.92rem; color:var(--text-dark); background:#F0F2FA; border-left:4px solid #2A6615; padding:10px 16px; border-radius:0 10px 10px 0; line-height:1.55;">
                  <strong>Qualifications:</strong> {job['qualifications']}
                </div>
              </div>\n'''

careers_html += '''            </div>
          </div>

          <!-- Group 3: Contracted Opportunities -->
          <div class="careers-group">
            <div class="careers-group-header" style="margin-bottom:20px; padding-bottom:14px; border-bottom:3px solid var(--navy); display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:12px;">
              <div style="display:flex; align-items:center; gap:12px;">
                <span class="badge badge-blue" style="font-weight:700; font-size:0.88rem;">Contracted Roles</span>
                <h3 style="font-size:1.5rem; color:var(--navy); margin:0;">Specialists, Tutors & Translators</h3>
              </div>
              <span style="font-size:0.92rem; color:var(--text-muted); font-weight:600;">2 Active Openings</span>
            </div>
            <div style="display:flex; flex-direction:column; gap:20px;">
'''

for job in site_data.CAREERS.get('contract', []):
    careers_html += f'''              <div class="job-card" style="background:#FFFFFF; border-radius:20px; padding:32px; border:1px solid rgba(42,210,201,0.25); box-shadow:0 4px 16px rgba(30,34,170,0.04);">
                <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:14px; margin-bottom:14px;">
                  <div>
                    <h4 style="font-size:1.4rem; color:var(--navy); margin-bottom:8px; font-weight:700;">{job['title']}</h4>
                    <div style="display:flex; gap:10px; flex-wrap:wrap;">
                      <span class="badge badge-sage">{job['type']}</span>
                      <span class="badge">{job['location']}</span>
                      <span class="badge badge-blue">{job['compensation']}</span>
                    </div>
                  </div>
                  <a href="mailto:careers@kandelia.org?subject=Application for {job['title']}" class="btn btn-outline btn-sm" style="border-radius:20px; padding:8px 22px;">Apply Now →</a>
                </div>
                <p style="font-size:1rem; color:var(--text-body); line-height:1.65; margin-bottom:14px;">{job['description']}</p>
                <div class="job-qualifications" style="font-size:0.92rem; color:var(--text-dark); background:#F0F2FA; border-left:4px solid var(--navy); padding:10px 16px; border-radius:0 10px 10px 0; line-height:1.55;">
                  <strong>Qualifications:</strong> {job['qualifications']}
                </div>
              </div>\n'''

careers_html += '''            </div>
          </div>

          <!-- Group 4: Youth Leadership & AYAB -->
          <div class="careers-group">
            <div class="careers-group-header" style="margin-bottom:20px; padding-bottom:14px; border-bottom:3px solid var(--coral); display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:12px;">
              <div style="display:flex; align-items:center; gap:12px;">
                <span class="badge badge-coral" style="font-weight:700; font-size:0.88rem;">Youth Leadership</span>
                <h3 style="font-size:1.5rem; color:var(--navy); margin:0;">Fellowships, Internships & AYAB</h3>
              </div>
              <span style="font-size:0.92rem; color:var(--text-muted); font-weight:600;">2 Active Openings</span>
            </div>
            <div style="display:flex; flex-direction:column; gap:20px;">
'''

for job in site_data.CAREERS.get('youth', []):
    careers_html += f'''              <div class="job-card" style="background:#FFFFFF; border-radius:20px; padding:32px; border:1px solid rgba(42,210,201,0.25); box-shadow:0 4px 16px rgba(30,34,170,0.04);">
                <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:14px; margin-bottom:14px;">
                  <div>
                    <h4 style="font-size:1.4rem; color:var(--navy); margin-bottom:8px; font-weight:700;">{job['title']}</h4>
                    <div style="display:flex; gap:10px; flex-wrap:wrap;">
                      <span class="badge badge-coral">{job['type']}</span>
                      <span class="badge">{job['location']}</span>
                      <span class="badge badge-blue">{job['compensation']}</span>
                    </div>
                  </div>
                  <a href="mailto:careers@kandelia.org?subject=Application for {job['title']}" class="btn btn-primary btn-sm" style="border-radius:20px; padding:8px 22px;">Apply Now →</a>
                </div>
                <p style="font-size:1rem; color:var(--text-body); line-height:1.65; margin-bottom:14px;">{job['description']}</p>
                <div class="job-qualifications" style="font-size:0.92rem; color:var(--text-dark); background:#F0F2FA; border-left:4px solid var(--coral); padding:10px 16px; border-radius:0 10px 10px 0; line-height:1.55;">
                  <strong>Qualifications:</strong> {job['qualifications']}
                </div>
              </div>\n'''

careers_html += f'''            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ALUMNI YOUTH ADVISORY BOARD (AYAB) FEATURED SPOTLIGHT -->
    <section style="padding:80px 0; background-color:#FFFFFF;">
      <div class="w" style="max-width:960px; margin:0 auto;">
        <div style="background:linear-gradient(135deg, #F0FAF9 0%, #FFFFFF 100%); border:2px solid var(--teal); border-radius:24px; padding:44px 36px; box-shadow:0 10px 30px rgba(42,210,201,0.12);">
          <div style="display:flex; align-items:center; flex-wrap:wrap; gap:12px; margin-bottom:16px;">
            <span class="badge badge-teal" style="font-size:0.85rem; text-transform:uppercase; font-weight:700;">Featured Leadership Initiative</span>
            <span class="badge badge-coral">$400 Stipend</span>
          </div>
          <h3 style="font-size:1.75rem; color:var(--navy); margin-bottom:12px; font-weight:700;">
            Kandelia Alumni Youth Advisory Board (AYAB) — Now Accepting Members
          </h3>
          <p style="font-size:1.05rem; color:var(--text-body); line-height:1.7; margin-bottom:18px;">
            Kandelia is launching its first-ever Alumni Youth Advisory Board, bringing together a dedicated cohort of young adults who attended Seattle Public Schools as Multilingual Learners after 2020. This is a powerful opportunity to share your lived experience, voice your community perspectives, and directly shape the programs and systemic partnerships that support newcomer youth today.
          </p>
          <div style="background:#FFFFFF; border-radius:14px; padding:18px 22px; border:1px solid rgba(42,210,201,0.3); margin-bottom:24px;">
            <p style="margin:0; font-size:0.95rem; color:var(--navy); font-weight:600;">
              🗓️ <strong>Cohort Schedule:</strong> Advisory Board members meet once a month from October through April (6 total sessions; no meeting in December).
            </p>
          </div>
          <div style="display:flex; gap:16px; flex-wrap:wrap; align-items:center;">
            <a href="mailto:careers@kandelia.org?subject=AYAB Application Interest" class="btn btn-primary btn-lg">
              Express Interest in AYAB →
            </a>
            <span style="font-size:0.92rem; color:var(--text-muted);">Questions? Reach out to <a href="mailto:info@kandelia.org" style="color:var(--teal-dark); font-weight:700; text-decoration:underline;">info@kandelia.org</a></span>
          </div>
        </div>
      </div>
    </section>

    <!-- VOLUNTEER SECTION -->
    <section id="volunteer" style="padding:80px 0; background-color:#F0F2FA; border-top:1px solid #E5E7EB;">
      <div class="w" style="max-width:960px; margin:0 auto; text-align:center;">
        <span class="badge badge-green" style="margin-bottom:12px;">Give Your Time</span>
        <h2 style="font-size:2rem; color:var(--navy); margin-bottom:16px;">Interested in Volunteering?</h2>
        <p style="font-size:1.1rem; color:var(--text-body); line-height:1.7; max-width:700px; margin:0 auto 28px;">
          Not looking for employment but eager to empower immigrant and refugee communities? Volunteer as an after-school tutor, career mentor, digital literacy coach, or event coordinator for our landmark 50th Anniversary Gala in May 2027.
        </p>
        <div style="display:flex; justify-content:center; gap:16px; flex-wrap:wrap;">
          <a href="https://docs.google.com/forms/d/e/1FAIpQLSeXxISZyibWTeAGMH7MU5rUYerKFk0--B1PB0rmNZNR4c20HQ/viewform" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-lg">
            Complete Volunteer Interest Form&nbsp;→
          </a>
          <a href="/ways-to-give" class="btn btn-outline btn-lg">
            Explore All Ways to Give
          </a>
        </div>
      </div>
    </section>

    <!-- HR & GENERAL JOB INQUIRIES CONTAINER -->
    <section id="hr-contact" style="padding:64px 0; background-color:#FFFFFF; border-top:1px solid #E5E7EB;">
      <div class="w" style="max-width:960px; margin:0 auto;">
        <div class="hr-contact-card" style="background:linear-gradient(135deg, #F0F2FA 0%, #FFFFFF 100%); border:2px solid rgba(30,34,170,0.18); border-radius:24px; padding:40px 36px; text-align:center; box-shadow:0 8px 24px rgba(30,34,170,0.06);">
          <span class="badge badge-blue" style="margin-bottom:14px;">Human Resources • General Applications</span>
          <h2 style="font-size:1.85rem; color:var(--navy); margin-bottom:12px;">Interested in Future Job Opportunities?</h2>
          <p style="font-size:1.06rem; color:var(--text-body); line-height:1.7; max-width:680px; margin:0 auto 24px;">
            If you are interested in any job opportunities at Kandelia, please send your <strong>resume</strong> and <strong>cover letter</strong> directly to our Human Resources team at
            <a href="mailto:hr@kandelia.org?subject=Job%20Opportunity%20Inquiry%20-%20Resume%20%26%20Cover%20Letter" style="color:var(--navy); font-weight:700; text-decoration:underline;">hr@kandelia.org</a>.
          </p>
          <div style="display:flex; justify-content:center; gap:14px; flex-wrap:wrap;">
            <a href="mailto:hr@kandelia.org?subject=Job%20Opportunity%20Inquiry%20-%20Resume%20%26%20Cover%20Letter" class="btn btn-primary btn-lg">
              Send Resume &amp; Cover Letter →
            </a>
            <a href="https://mail.google.com/mail/?view=cm&fs=1&to=hr@kandelia.org&su=Job%20Opportunity%20Inquiry%20-%20Resume%20%26%20Cover%20Letter" target="_blank" rel="noopener noreferrer" class="btn btn-outline btn-lg">
              Compose in Web Gmail ↗
            </a>
          </div>
        </div>
      </div>
    </section>

    {get_support_banner()}
  </main>
'''
careers_html += get_footer()

with open('careers.html', 'w', encoding='utf-8') as f:
    f.write(careers_html)
print("careers.html written successfully!")

# ==============================================================================
# 8. IMPACT REPORT 2026 PAGE (impact-report-2026.html)
# ==============================================================================
print("Generating impact-report-2026.html...")
impact_html = get_header("impact")
impact_html += '''
  <main id="main-content">
    <section class="hero-inner-section" style="padding:72px 0 56px; background:linear-gradient(135deg, #F0FAF9 0%, #FFFFFF 100%); border-bottom:1px solid rgba(42,210,201,0.2);">
      <div class="w text-center" style="max-width:860px; margin:0 auto;">
        <span class="badge badge-green" style="margin-bottom:14px;">Annual Publication • 2026 Impact Report</span>
        <h1 style="color:var(--navy); margin-bottom:16px;">Deep Roots, Lasting Flourish</h1>
        <p class="lead" style="margin:0 auto 28px;">
          Our comprehensive evaluation of student graduation rates, family economic mobility, and direct emergency assistance distributed across King County.
        </p>
        <div style="display:flex; gap:14px; justify-content:center; flex-wrap:wrap;">
          <button type="button" class="btn btn-primary open-request-pdf-modal">Request PDF Copy →</button>
          <a href="/about" class="btn btn-outline">← Back to About Kandelia</a>
        </div>
      </div>
    </section>

    <section style="padding:64px 0; background:#FFFFFF;">
      <div class="w" style="max-width:1040px; margin:0 auto;">
        <div class="milestones-4grid" style="margin-bottom:48px;">
          <div class="milestone-card-item" style="background:#F0FAF9; border:1px solid rgba(42,210,201,0.3); border-radius:20px; padding:28px 22px; text-align:center;">
            <div style="font-size:2.4rem; font-weight:700; color:var(--navy); margin-bottom:6px;">570+</div>
            <div style="font-weight:700; color:var(--teal-dark); margin-bottom:6px;">Newcomers Served</div>
            <p style="font-size:0.92rem; color:var(--text-body); margin:0;">Guided through academic, language, and civic pathways.</p>
          </div>
          <div class="milestone-card-item" style="background:#F4FBE8; border:1px solid rgba(151,215,0,0.35); border-radius:20px; padding:28px 22px; text-align:center;">
            <div style="font-size:2.4rem; font-weight:700; color:var(--navy); margin-bottom:6px;">95%</div>
            <div style="font-weight:700; color:#2A6615; margin-bottom:6px;">Graduation Rate</div>
            <p style="font-size:0.92rem; color:var(--text-body); margin:0;">Among cohort high school seniors at Seattle World School.</p>
          </div>
          <div class="milestone-card-item" style="background:#FEECEE; border:1px solid rgba(244,54,76,0.25); border-radius:20px; padding:28px 22px; text-align:center;">
            <div style="font-size:2.4rem; font-weight:700; color:var(--navy); margin-bottom:6px;">$240K+</div>
            <div style="font-weight:700; color:var(--coral); margin-bottom:6px;">Direct Family Relief</div>
            <p style="font-size:0.92rem; color:var(--text-body); margin:0;">Distributed in emergency rental, food, and utility aid.</p>
          </div>
          <div class="milestone-card-item" style="background:#F0F2FA; border:1px solid rgba(30,34,170,0.2); border-radius:20px; padding:28px 22px; text-align:center;">
            <div style="font-size:2.4rem; font-weight:700; color:var(--navy); margin-bottom:6px;">1,200+</div>
            <div style="font-weight:700; color:var(--navy); margin-bottom:6px;">Digital Literacy Hours</div>
            <p style="font-size:0.92rem; color:var(--text-body); margin:0;">Delivered in bilingual workshops for parents &amp; caregivers.</p>
          </div>
        </div>

        <div class="story-editorial-article" style="background:#FFFFFF; border:1px solid rgba(42,210,201,0.25); border-radius:24px; padding:36px 32px; box-shadow:0 6px 24px rgba(30,34,170,0.04);">
          <h2 style="color:var(--navy); margin-bottom:16px;">Executive Summary</h2>
          <p>Over the past year, Kandelia deepened its commitment to holistic, culturally responsive support for newly arrived immigrant and refugee families across King County. Working hand-in-hand with educators at Seattle World School, multilingual family advocates, and community partners, we removed systemic barriers so students and parents could thrive together.</p>
          <p>Through after-school tutoring, Running Start college readiness coaching, paid youth internships, and direct emergency relief, 95% of participating seniors graduated on time—many becoming the first in their families to enter university.</p>
          <div style="margin-top:24px; padding-top:20px; border-top:1px solid #E5E7EB; display:flex; gap:14px; flex-wrap:wrap;">
            <a class="btn btn-coral" href="https://kandelia-bloom.kindful.com/embeds/75568458-194c-4924-8a1b-de2cd76e4f92" target="_blank" rel="noopener">Support Our 2026–2027 Programs →</a>
            <button type="button" class="btn btn-outline open-request-pdf-modal">Request Full PDF Copy</button>
          </div>
        </div>
      </div>
    </section>
  </main>
'''
impact_html += get_footer()

with open('impact-report-2026.html', 'w', encoding='utf-8') as f:
    f.write(impact_html)
print("impact-report-2026.html written successfully!")
print("=== All 8 pages built successfully! ===")
