# build_enhanced_site.py - Master generation script for Kandelia website with playful organic shapes
import os
import base64
import json
from site_data import (
    BOARD_MEMBERS,
    STAFF_LEADERSHIP,
    TESTIMONIALS,
    STAFF_BOARD_QUOTES,
    STORIES,
    CAREERS
)

def get_base64_img(path, mime):
    with open(path, 'rb') as f:
        data = f.read()
    b64 = base64.b64encode(data).decode('utf-8')
    return f'data:{mime};base64,{b64}'

print("Loading base64 images...")
images = {
    'logo': get_base64_img('assets/image_0.png', 'image/png'),
    'hero': get_base64_img('assets/image_1.jpeg', 'image/jpeg'),
    'event': get_base64_img('assets/image_2.jpeg', 'image/jpeg'),
    'youth': get_base64_img('assets/image_3.jpeg', 'image/jpeg'),
    'family': get_base64_img('assets/image_4.jpeg', 'image/jpeg'),
    'patrick': get_base64_img('assets/image_5.jpeg', 'image/jpeg'),
    'sunflower': get_base64_img('assets/image_6.jpeg', 'image/jpeg'),
    'mother': get_base64_img('assets/image_7.jpeg', 'image/jpeg'),
    'vidia': get_base64_img('assets/image_8.jpeg', 'image/jpeg'),
    'community': get_base64_img('assets/image_9.jpeg', 'image/jpeg'),
    'logo_footer': get_base64_img('assets/image_10.png', 'image/png'),
}

SVGS = {
    'heart': '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>',
    'mail': '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>',
    'phone': '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>',
    'chevron-down': '<svg class="icon chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>',
    'arrow-right': '<svg class="icon icon-arrow-right" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>',
    'check': '<svg class="icon check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>',
    'shield': '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>',
    'facebook': '<svg class="icon" viewBox="0 0 24 24" fill="currentColor"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg>',
    'instagram': '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>',
    'linkedin': '<svg class="icon" viewBox="0 0 24 24" fill="currentColor"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>',
    'globe': '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>',
    'play': '<svg class="icon play" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>',
    'close': '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>',
}

with open('styles.css', 'r', encoding='utf-8') as f:
    CSS = f.read()

with open('script.js', 'r', encoding='utf-8') as f:
    JS = f.read()

print("All dependencies loaded. Building enhanced HTML components...")

# 1. Testimonials slides (In Their Words)
testimonials_slides_html = ""
testimonials_dots_html = ""
for i, t in enumerate(TESTIMONIALS):
    active_cls = " active" if i == 0 else ""
    aria_hidden = "false" if i == 0 else "true"
    testimonials_slides_html += f"""
      <div class="carousel-slide{active_cls}" aria-hidden="{aria_hidden}">
        <span class="badge badge-sage" style="margin-bottom:14px;">{t['category']}</span>
        <blockquote class="testimonial-quote">
          "{t['quote']}"
        </blockquote>
        <div class="testimonial-author-block">
          <div class="author-avatar avatar-shape-flower-8" style="background:var(--green-soft);">{t['author'][0]}</div>
          <div class="author-info">
            <b>{t['author']}</b>
            <span>{t['role']}</span>
          </div>
        </div>
      </div>
    """
    testimonials_dots_html += f"""
      <button class="carousel-dot{active_cls}" aria-label="Slide {i+1}" aria-current="{ 'true' if i == 0 else 'false'}"></button>
    """

# 2. Staff & Board Quotes carousel slides
staff_quotes_slides_html = ""
staff_quotes_dots_html = ""
for i, q in enumerate(STAFF_BOARD_QUOTES):
    active_cls = " active" if i == 0 else ""
    aria_hidden = "false" if i == 0 else "true"
    staff_quotes_slides_html += f"""
      <div class="carousel-slide{active_cls}" aria-hidden="{aria_hidden}">
        <blockquote class="testimonial-quote" style="border-left-color: var(--coral);">
          "{q['quote']}"
        </blockquote>
        <div class="testimonial-author-block">
          <div class="author-avatar avatar-shape-hexagon" style="background:var(--coral-soft);color:var(--coral);">{q['author'][0]}</div>
          <div class="author-info">
            <b>{q['author']}</b>
            <span>{q['title']}</span>
          </div>
        </div>
      </div>
    """
    staff_quotes_dots_html += f"""
      <button class="carousel-dot{active_cls}" aria-label="Quote {i+1}" aria-current="{ 'true' if i == 0 else 'false'}"></button>
    """

# 3. Board members grid - Canva-Style Double-Layer Sticker Silhouettes (Clover, Flower, Hexagon, Pentagon, Pebble)
board_shapes_classes = [
    ('avatar-shape-hexagon', 'backdrop-honey'),
    ('avatar-shape-flower-8', 'backdrop-mint'),
    ('avatar-shape-clover-4', 'backdrop-rose'),
    ('avatar-shape-pentagon', 'backdrop-sky'),
    ('avatar-shape-pebble', 'backdrop-lavender'),
    ('avatar-shape-flower-12', 'backdrop-coral'),
    ('avatar-shape-clover-4', 'backdrop-mint'),
]

board_cards_html = ""
for i, b in enumerate(BOARD_MEMBERS):
    shape_cls, backdrop_cls = board_shapes_classes[i % len(board_shapes_classes)]
    board_cards_html += f"""
      <div class="board-card" id="{b['id']}">
        <div class="avatar-sticker-wrap">
          <div class="avatar-sticker-backdrop {shape_cls} {backdrop_cls}"></div>
          <div class="board-avatar {shape_cls}" style="background: {b['color']};">
            {b['initials']}
          </div>
        </div>
        <h4 class="board-name">{b['name']}</h4>
        <div class="board-role">{b['role']}</div>
        <div class="board-tenure">{b['tenure']}</div>
        <button class="btn btn-outline btn-sm board-bio-btn open-board-bio"
          data-name="{b['name']}"
          data-role="{b['role']}"
          data-tenure="{b['tenure']}"
          data-bio="{b['bio']}"
          data-quote="{b['quote']}"
          data-initials="{b['initials']}"
          data-color="{b['color']}"
          aria-label="View bio for {b['name']}">
          Click to Expand Bio {SVGS['chevron-down']}
        </button>
      </div>
    """

# 4. Staff grid with Canva-Style Double-Layer Sticker Silhouettes
staff_shapes_classes = [
    ('avatar-shape-flower-8', 'backdrop-mint'),
    ('avatar-shape-hexagon', 'backdrop-honey'),
    ('avatar-shape-clover-4', 'backdrop-rose'),
    ('avatar-shape-pentagon', 'backdrop-sky'),
    ('avatar-shape-pebble', 'backdrop-sage'),
]

staff_cards_html = ""
for i, s in enumerate(STAFF_LEADERSHIP):
    shape_cls, backdrop_cls = staff_shapes_classes[i % len(staff_shapes_classes)]
    staff_cards_html += f"""
      <div class="staff-card">
        <div class="avatar-sticker-wrap">
          <div class="avatar-sticker-backdrop {shape_cls} {backdrop_cls}"></div>
          <div class="staff-avatar {shape_cls}" style="background:var(--bg-sage-tint);">{s['name'][0]}</div>
        </div>
        <h4>{s['name']}</h4>
        <div class="staff-role">{s['role']}</div>
        <div class="staff-languages">Languages: {s['languages']}</div>
        <p>{s['bio']}</p>
      </div>
    """

# 5. Stories grid with intentional, subject-preserving playful shapes
story_shape_configs = [
    {
        'backdrop_cls': 'story-shape-backdrop-flower',
        'clip_cls': 'shape-clip-flower-8 patrick-focal',
        'badge_label': 'Youth Voice • 8-Petal Flower',
        'shape_name': 'Soft Flower Shape'
    },
    {
        'backdrop_cls': 'story-shape-backdrop-clover',
        'clip_cls': 'shape-clip-clover-4 hands-focal',
        'badge_label': 'Sisterhood • 4-Leaf Clover',
        'shape_name': 'Four-Leaf Clover Shape'
    },
    {
        'backdrop_cls': 'story-shape-backdrop-hexagon',
        'clip_cls': 'shape-clip-hexagon mother-focal',
        'badge_label': 'Art & Resilience • Rounded Hexagon',
        'shape_name': 'Rounded Hexagon Shape'
    },
    {
        'backdrop_cls': 'story-shape-backdrop-arch',
        'clip_cls': 'shape-clip-arch vidia-focal',
        'badge_label': 'Leadership • Organic Arch',
        'shape_name': 'Organic Arch Shape'
    }
]

stories_cards_html = ""
for i, st in enumerate(STORIES):
    cfg = story_shape_configs[i % len(story_shape_configs)]
    img_data = images[st['image_key']]
    stories_cards_html += f"""
      <div class="story-card open-story-reader"
        data-title="{st['title']}"
        data-subtitle="{st['subtitle']}"
        data-quote="{st['quote']}"
        data-story-html="{st['full_text'].replace('"', '&quot;').replace('\n', ' ')}"
        tabindex="0"
        role="button"
        aria-label="Read full story: {st['title']}">
        <!-- Playful Organic Shape Container (Subject 100% Preserved) -->
        <div class="story-image-shape-container">
          <div class="{cfg['backdrop_cls']}"></div>
          <div class="story-image-inner {cfg['clip_cls']}">
            <img src="{img_data}" alt="{st['title']}">
          </div>
        </div>
        <div class="story-card-body">
          <span class="badge badge-sage" style="margin-bottom:8px;align-self:flex-start;">{cfg['badge_label']}</span>
          <h4>{st['title']}</h4>
          <p>{st['short']}</p>
          <span class="story-read-link">
            Read full story {SVGS['arrow-right']}
          </span>
        </div>
      </div>
    """

# 6. Careers panels
def build_job_list(jobs):
    html = ""
    for j in jobs:
        html += f"""
          <div class="job-card">
            <div class="job-info">
              <h4>{j['title']}</h4>
              <div class="job-meta-pills">
                <span class="badge badge-sage">{j['type']}</span>
                <span class="badge">{j['location']}</span>
                <span class="badge badge-gold">{j['compensation']}</span>
              </div>
              <p>{j['description']}</p>
              <p style="font-size:0.92rem;color:var(--text-subtle);"><strong>Qualifications:</strong> {j['qualifications']}</p>
            </div>
            <a class="btn btn-primary" href="mailto:careers@kandelia.org?subject=Application for {j['title']}">
              Apply Now {SVGS['arrow-right']}
            </a>
          </div>
        """
    return html

careers_staff_html = build_job_list(CAREERS['staff'])
careers_contract_html = build_job_list(CAREERS['contract'])
careers_youth_html = build_job_list(CAREERS['youth'])
careers_board_html = build_job_list(CAREERS['board'])

print("HTML Components successfully synthesized.")

# Master HTML Assembly with SVG ClipPaths and Enhanced Layouts
html_document = f"""<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Kandelia | Removing barriers to immigrant and refugee success</title>
  <meta name="description" content="Kandelia is a community organization in Seattle addressing systemic inequities so immigrant and refugee families can thrive without compromising values, heritage, or identity.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400;1,700&display=swap" rel="stylesheet">
  <style>
{CSS}
  </style>
</head>
<body>

  <!-- Skip to Content for Accessibility -->
  <a href="#main-content" class="skip-link">Skip to main content</a>

  <!-- ====================================================================
       SCALABLE SVG CLIPPATTH & MASK DEFINITIONS (objectBoundingBox 0 to 1)
       Enables smooth, responsive flower, hexagon, pentagon & organic shapes
       ==================================================================== -->
  <svg width="0" height="0" style="position:absolute;width:0;height:0;overflow:hidden;pointer-events:none;" aria-hidden="true">
    <defs>
      <!-- 1. Soft Rounded Hexagon -->
      <clipPath id="shape-hexagon-soft" clipPathUnits="objectBoundingBox">
        <path d="M 0.4307 0.0800 Q 0.5000 0.0400 0.5693 0.0800 L 0.8291 0.2300 Q 0.8984 0.2700 0.8984 0.3500 L 0.8984 0.6500 Q 0.8984 0.7300 0.8291 0.7700 L 0.5693 0.9200 Q 0.5000 0.9600 0.4307 0.9200 L 0.1709 0.7700 Q 0.1016 0.7300 0.1016 0.6500 L 0.1016 0.3500 Q 0.1016 0.2700 0.1709 0.2300 Z" />
      </clipPath>

      <!-- 2. Soft Rounded Pentagon -->
      <clipPath id="shape-pentagon-soft" clipPathUnits="objectBoundingBox">
        <path d="M 0.4353 0.0870 Q 0.5000 0.0400 0.5647 0.0870 L 0.8728 0.3108 Q 0.9375 0.3579 0.9128 0.4339 L 0.7951 0.7961 Q 0.7704 0.8721 0.6904 0.8721 L 0.3096 0.8721 Q 0.2296 0.8721 0.2049 0.7961 L 0.0872 0.4339 Q 0.0625 0.3579 0.1272 0.3108 Z" />
      </clipPath>

      <!-- 3. Soft 8-Petal Scalloped Flower -->
      <clipPath id="shape-flower-8" clipPathUnits="objectBoundingBox">
        <path d="M 0.3469 0.1304 Q 0.5000 0.0200 0.6531 0.1304 Q 0.8394 0.1606 0.8696 0.3469 Q 0.9800 0.5000 0.8696 0.6531 Q 0.8394 0.8394 0.6531 0.8696 Q 0.5000 0.9800 0.3469 0.8696 Q 0.1606 0.8394 0.1304 0.6531 Q 0.0200 0.5000 0.1304 0.3469 Q 0.1606 0.1606 0.3469 0.1304 Z" />
      </clipPath>

      <!-- 4. Soft 12-Petal Scalloped Daisy -->
      <clipPath id="shape-flower-12" clipPathUnits="objectBoundingBox">
        <path d="M 0.3887 0.0847 Q 0.5000 0.0200 0.6113 0.0847 Q 0.7400 0.0843 0.8041 0.1959 Q 0.9157 0.2600 0.9153 0.3887 Q 0.9800 0.5000 0.9153 0.6113 Q 0.9157 0.7400 0.8041 0.8041 Q 0.7400 0.9157 0.6113 0.9153 Q 0.5000 0.9800 0.3887 0.9153 Q 0.2600 0.9157 0.1959 0.8041 Q 0.0843 0.7400 0.0847 0.6113 Q 0.0200 0.5000 0.0847 0.3887 Q 0.0843 0.2600 0.1959 0.1959 Q 0.2600 0.0843 0.3887 0.0847 Z" />
      </clipPath>

      <!-- 5. Soft 6-Petal Flower -->
      <clipPath id="shape-flower-6" clipPathUnits="objectBoundingBox">
        <path d="M 0.3100 0.1709 Q 0.5000 0.0200 0.6900 0.1709 Q 0.9157 0.2600 0.8800 0.5000 Q 0.9157 0.7400 0.6900 0.8291 Q 0.5000 0.9800 0.3100 0.8291 Q 0.0843 0.7400 0.1200 0.5000 Q 0.0843 0.2600 0.3100 0.1709 Z" />
      </clipPath>

      <!-- 6. Organic Pebble -->
      <clipPath id="shape-pebble-soft" clipPathUnits="objectBoundingBox">
        <path d="M 0.5000 0.0500 C 0.7800 0.0400 0.9500 0.2200 0.9500 0.5000 C 0.9500 0.7800 0.7800 0.9500 0.5000 0.9500 C 0.2200 0.9500 0.0500 0.7800 0.0500 0.5000 C 0.0500 0.2200 0.2200 0.0600 0.5000 0.0500 Z" />
      </clipPath>

      <!-- 7. Organic Arch -->
      <clipPath id="shape-organic-arch" clipPathUnits="objectBoundingBox">
        <path d="M 0.0600 0.4000 C 0.0600 0.1600 0.2200 0.0400 0.5000 0.0400 C 0.7800 0.0400 0.9400 0.1600 0.9400 0.4000 L 0.9400 0.9000 C 0.9400 0.9500 0.8800 0.9600 0.8200 0.9600 L 0.1800 0.9600 C 0.1200 0.9600 0.0600 0.9500 0.0600 0.9000 Z" />
      </clipPath>
      <!-- 8. Soft Four-Leaf Clover -->
      <clipPath id="shape-clover-4" clipPathUnits="objectBoundingBox">
        <path d="M 0.2454 0.2454 Q 0.5000 0.0200 0.7546 0.2454 Q 0.9800 0.5000 0.7546 0.7546 Q 0.5000 0.9800 0.2454 0.7546 Q 0.0200 0.5000 0.2454 0.2454 Z" />
      </clipPath>
      <!-- 9. Soft Organic Heart Shape for Support CTA (clip-path: url(#heart-clip)) -->
      <clipPath id="heart-clip" clipPathUnits="objectBoundingBox">
        <path d="M 0.5 0.28 C 0.5 0.20, 0.40 0.06, 0.25 0.06 C 0.10 0.06, 0.02 0.22, 0.02 0.38 C 0.02 0.60, 0.25 0.78, 0.50 0.96 C 0.75 0.78, 0.98 0.60, 0.98 0.38 C 0.98 0.22, 0.90 0.06, 0.75 0.06 C 0.60 0.06, 0.50 0.20, 0.50 0.28 Z" />
      </clipPath>
    </defs>
  </svg>

  <!-- Global Utility Bar -->
  <div class="util-bar">
    <div class="w">
      <a href="mailto:help@kandelia.org">
        {SVGS['mail']}
        <span data-i18n="get_help">Get help: help@kandelia.org</span>
      </a>
      <a href="#contact">
        <span data-i18n="contact">Contact</span>
      </a>
      <div class="lang-selector">
        <label for="language-picker-select">
          {SVGS['globe']}
          <span>Language:</span>
        </label>
        <select id="language-picker-select" aria-label="Select language for page translation">
          <option value="en" selected>English</option>
          <option value="es">Español</option>
          <option value="vi">Tiếng Việt</option>
          <option value="ar">العربية</option>
          <option value="so">Soomaali</option>
        </select>
      </div>
    </div>
  </div>

  <!-- Global Header & Top Nav (Round logo, no 'Home' text, donate pill) -->
  <header class="site-header" role="banner">
    <div class="w header-container">
      <a href="#" class="brand-link" aria-label="Kandelia Home">
        <img src="{images['logo']}" alt="Kandelia logo" class="brand-logo">
      </a>

      <!-- Desktop Nav -->
      <nav class="main-nav" aria-label="Main Navigation">
        <div class="nav-item">
          <a href="#about" class="nav-link" data-i18n="about_us">
            About Us {SVGS['chevron-down']}
          </a>
          <ul class="dropdown-menu">
            <li><a href="#history" class="dropdown-link" data-i18n="our_history">Our History</a></li>
            <li><a href="#our-work" class="dropdown-link" data-i18n="our_work">Our Work</a></li>
            <li><a href="#our-team" class="dropdown-link" data-i18n="our_team">Our Team (Staff & Board)</a></li>
          </ul>
        </div>

        <div class="nav-item">
          <a href="#get-support" class="nav-link" data-i18n="get_support">
            Get Support {SVGS['chevron-down']}
          </a>
          <ul class="dropdown-menu">
            <li><a href="#high-school-programs" class="dropdown-link" data-i18n="high_school">High School Programs</a></li>
            <li><a href="#family-programs" class="dropdown-link" data-i18n="family_prog">Family Programs</a></li>
          </ul>
        </div>

        <div class="nav-item">
          <a href="#get-involved" class="nav-link" data-i18n="get_involved">
            Get Involved {SVGS['chevron-down']}
          </a>
          <ul class="dropdown-menu">
            <li><a href="#give" class="dropdown-link" data-i18n="give">Give</a></li>
            <li><a href="#volunteer" class="dropdown-link" data-i18n="volunteer">Volunteer</a></li>
            <li><a href="#partner" class="dropdown-link" data-i18n="partner">Partner</a></li>
          </ul>
        </div>

        <div class="nav-item">
          <a href="#stories-impact" class="nav-link" data-i18n="stories_impact">
            Stories & Impact {SVGS['chevron-down']}
          </a>
          <ul class="dropdown-menu">
            <li><a href="#impact-report" class="dropdown-link" data-i18n="impact_report">2026 Impact Report</a></li>
            <li><a href="#stories" class="dropdown-link" data-i18n="stories">Roots & Routes Stories</a></li>
          </ul>
        </div>
      </nav>

      <a class="btn btn-coral" href="https://kandelia-bloom.kindful.com/embeds/75568458-194c-4924-8a1b-de2cd76e4f92" target="_blank" rel="noopener" data-i18n="donate">
        {SVGS['heart']} Donate
      </a>

      <button class="mobile-toggle" id="mobile-menu-toggle" aria-expanded="false" aria-controls="mobile-navigation-drawer">
        Menu ☰
      </button>
    </div>

    <!-- Mobile Navigation Drawer -->
    <nav class="mobile-nav-drawer" id="mobile-navigation-drawer" aria-label="Mobile Navigation">
      <a href="#about" data-i18n="about_us">About Us</a>
      <a href="#history" class="mobile-sublink" data-i18n="our_history">↳ Our History</a>
      <a href="#our-work" class="mobile-sublink" data-i18n="our_work">↳ Our Work</a>
      <a href="#our-team" class="mobile-sublink" data-i18n="our_team">↳ Our Team</a>
      <a href="#get-support" data-i18n="get_support">Get Support</a>
      <a href="#high-school-programs" class="mobile-sublink" data-i18n="high_school">↳ High School Programs</a>
      <a href="#family-programs" class="mobile-sublink" data-i18n="family_prog">↳ Family Programs</a>
      <a href="#get-involved" data-i18n="get_involved">Get Involved</a>
      <a href="#stories-impact" data-i18n="stories_impact">Stories & Impact</a>
      <a href="#careers" data-i18n="work_with_us">Work With Us (Careers)</a>
      <a class="btn btn-coral btn-donate" href="https://kandelia-bloom.kindful.com/embeds/75568458-194c-4924-8a1b-de2cd76e4f92" target="_blank" rel="noopener">
        {SVGS['heart']} Donate
      </a>
    </nav>
  </header>

  <!-- Main Content -->
  <main id="main-content">

    <!-- ====================================================================
         SECTION 1: HOME PAGE
         ==================================================================== -->

    <!-- Hero Section: Enhanced Playful Organic Composition -->
    <section class="section-hero organic-bg">
      <div class="organic-blob blob-sage" style="width:480px;height:480px;top:-100px;right:-50px;"></div>
      <div class="organic-blob blob-sand" style="width:520px;height:520px;bottom:-150px;left:-100px;"></div>

      <div class="w hero-grid">
        <div class="hero-content">
          <div class="hero-badge-container">
            <span class="badge badge-sage">
              🌸 <span data-i18n="hero_tag">50 Years of Immigrant & Refugee Belonging</span>
            </span>
          </div>
          <h1 class="hero-title" data-i18n="hero_title">
            We remove barriers to immigrant and refugee success
          </h1>
          <p class="hero-lead" data-i18n="hero_lead">
            We are a community organization addressing systemic inequities so immigrant and refugee families and communities can thrive without having to compromise values, heritage or ethnicity. Through holistic youth programs, adult learning, and family advocacy, we walk alongside new arrivals on their journey to belonging.
          </p>
          <div class="hero-actions">
            <a class="btn btn-primary" href="#get-support" data-i18n="btn_support">
              I'm looking for support {SVGS['arrow-right']}
            </a>
            <a class="btn btn-outline" href="#get-involved" data-i18n="btn_help">
              I want to help
            </a>
          </div>
        </div>

        <!-- Hero Media: Layered Organic Scalloped Flower Composition (Zero Subject Cropping) -->
        <div class="hero-media-wrapper">
          <div class="hero-organic-composition">
            <!-- Decorative Scalloped Flower Backdrop -->
            <div class="hero-flower-backdrop"></div>
            <div class="hero-scallop-ring"></div>

            <!-- Floating Playful Sticker Badge -->
            <div class="floating-sticker top-right">🌸 50 Years • Seattle Roots</div>

            <!-- Main Image Frame with Organic Curve (Both students 100% visible) -->
            <div class="hero-image-frame-enhanced">
              <img src="{images['hero']}" alt="Two smiling Kandelia students outside their school in Seattle">
            </div>

            <!-- Floating Rounded Hexagon Stat Badge -->
            <div class="floating-stat-card">
              <div class="floating-stat-badge shape-clip-hexagon" style="background:var(--green-soft);">
                🎓
              </div>
              <div class="floating-stat-text">
                <b>95% Graduation Rate</b>
                <span>Serving 570+ Students & Families</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Wave Divider 1: Hero to Event -->
    <svg class="section-wave-divider to-sand wave-hero-event" viewBox="0 0 1200 44" preserveAspectRatio="none" aria-hidden="true"><path d="M0,0 C300,38 600,6 900,32 1050,42 1150,20 1200,0 L1200,44 L0,44 Z"></path></svg>

    <!-- Event Banner: Enhanced Rounded Hexagonal Composition -->
    <section class="event-banner-section" id="milestone-gala">
      <div class="w">
        <div class="event-card">
          <!-- 1. Strict 2-Column Split Grid (50% Left / 50% Right) -->
          <div class="event-2col-grid">
            <!-- LEFT COLUMN: Layered Image Container (From Design 2) -->
            <div class="event-image-col">
              <div class="event-layered-image-wrap">
                <!-- Soft warm yellow/gold card backing with dashed border -->
                <div class="event-image-backing" aria-hidden="true"></div>

                <!-- Rounded photograph inside -->
                <div class="event-image-frame">
                  <img src="{images['event']}" alt="Kandelia group looking out over the Seattle skyline" loading="lazy">
                </div>

                <!-- Floating white pill badge at bottom-left corner of the image -->
                <div class="floating-sticker event-gala-pill">
                  ✨ Milestone Gala
                </div>
              </div>
            </div>

            <!-- RIGHT COLUMN: All Content & CTAs stacked vertically with clean left-alignment -->
            <div class="event-content-col">
              <!-- 1. Top Pill Badge (soft warm cream pill with muted gold text) -->
              <span class="event-milestone-pill">
                Milestone Celebration • 1978–2028
              </span>

              <!-- 2. Large Heading in deep navy (#12263A) -->
              <h2 class="event-title">
                Celebrate 50 years of Kandelia with us in May 2027
              </h2>

              <!-- 3. Description Paragraph -->
              <p class="event-desc">
                Join our landmark 50th anniversary celebration and "Sip & Celebrate" gala at the Seattle Center Pavilion. Honoring five decades of immigrant and refugee leadership, student triumphs, and community solidarity.
              </p>

              <!-- 4. Event Metadata Pills -->
              <div class="event-meta-row">
                <span class="event-meta-pill">📅 Friday, May 14, 2027</span>
                <span class="event-meta-pill">📍 Seattle Center Pavilion</span>
                <span class="event-meta-pill">🕕 6:00 PM PST</span>
              </div>

              <!-- 5. CTA Buttons (In SAME Right Column directly below text/pills) -->
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

          <!-- 3. Centered Sponsor Row (From Design 1) with 5 dashed placeholder boxes -->
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

    <!-- Wave Divider 2: Event to Who We Help -->
    <svg class="section-wave-divider to-cream wave-event-who" viewBox="0 0 1200 44" preserveAspectRatio="none" aria-hidden="true"><path d="M0,20 C350,0 700,44 1200,12 L1200,44 L0,44 Z"></path></svg>

    <!-- Who We Help (Organic Asymmetric Frames, Wide Panoramas 100% Preserved) -->
    <section class="section-who-we-help" id="who-we-help">
      <div class="w">
        <div class="section-header-center">
          <span class="badge badge-sage" style="margin-bottom:12px;">Holistic Support Model</span>
          <h2 data-i18n="who_we_help">Who We Help</h2>
          <p class="lead">Tailored, culturally affirming programs for high school students and for whole families across King County.</p>
        </div>

        <div class="who-grid who-grid-staggered">
          <!-- Column 1: Youth / High School Students (Organic Asymmetric Frame) -->
          <div class="program-column-card stagger-up">
            <div class="program-image-organic-wrap">
              <span class="petal-badge-tag">🌸 Youth Pathways</span>
              <img src="{images['youth']}" alt="Kandelia high school students smiling in a classroom">
            </div>
            <span class="badge badge-sage" style="margin-bottom:10px;align-self:flex-start;">Youth Champions</span>
            <h3>High School Students</h3>
            <p>Our youth programs champion young people so that they can succeed academically, explore careers, and be their full, authentic selves.</p>

            <details class="styled-details">
              <summary class="styled-summary">
                <span>English Classes & Academic Tutoring</span>
                <span class="acc-icon">+</span>
              </summary>
              <div class="details-content">
                Culturally responsive English language support, bilingual homework tutoring, and credit recovery cohorts designed to ensure students thrive in the classroom.
              </div>
            </details>

            <details class="styled-details">
              <summary class="styled-summary">
                <span>Job Readiness and Career Navigation</span>
                <span class="acc-icon">+</span>
              </summary>
              <div class="details-content">
                Resume building, paid summer internship placements, mock interviews, and workplace site visits with industry mentors across technology, healthcare, and trades.
              </div>
            </details>

            <details class="styled-details">
              <summary class="styled-summary">
                <span>1-on-1 Mentorship</span>
                <span class="acc-icon">+</span>
              </summary>
              <div class="details-content">
                Connecting students with caring adult mentors who share similar cultural backgrounds, offering college guidance, life navigation, and unconditional encouragement.
              </div>
            </details>

            <div class="eligibility-box">
              <b>You're eligible if:</b>
              <ul>
                <li>Enrolled in a high school in King County or South Seattle.</li>
                <li>Identify as an immigrant, refugee, or asylee youth (ages 14–21).</li>
                <li>Seeking academic tutoring, career exploration, or mentorship.</li>
              </ul>
              <p style="font-size:0.92rem;margin:0;">Questions? Email <a href="mailto:help@kandelia.org">help@kandelia.org</a> or call 206-760-1573</p>
            </div>

            <a class="btn btn-outline" href="#high-school-programs" style="margin-top:auto;">
              Explore High School Programs {SVGS['arrow-right']}
            </a>
          </div>

          <!-- Column 2: Families (Inverted Asymmetric Frame) -->
          <div class="program-column-card stagger-down">
            <div class="program-image-organic-wrap family-wrap">
              <span class="petal-badge-tag">🍀 Family Unity</span>
              <img src="{images['family']}" alt="Kandelia family gathering in a collaborative workshop">
            </div>
            <span class="badge badge-sage" style="margin-bottom:10px;align-self:flex-start;">Whole Family Power</span>
            <h3>Families & Caregivers</h3>
            <p>Our family programs provide immigrant and refugee parents with tools, language skills, and advocacy to help entire households thrive.</p>

            <details class="styled-details">
              <summary class="styled-summary">
                <span>Adult English Classes (ESL)</span>
                <span class="acc-icon">+</span>
              </summary>
              <div class="details-content">
                Practical, beginner-to-intermediate ESL classes with flexible evening schedules and childcare support, tailored for parents and working adults.
              </div>
            </details>

            <details class="styled-details">
              <summary class="styled-summary">
                <span>Digital Literacy Classes</span>
                <span class="acc-icon">+</span>
              </summary>
              <div class="details-content">
                Hands-on computer training: navigating school district portals (The Source), setting up email, accessing telehealth, and safe digital practices.
              </div>
            </details>

            <details class="styled-details">
              <summary class="styled-summary">
                <span>Community Workshops & Advocacy</span>
                <span class="acc-icon">+</span>
              </summary>
              <div class="details-content">
                Informative clinics on tenant rights, affordable housing navigation, financial wellness, public benefits access, and citizenship preparation.
              </div>
            </details>

            <div class="eligibility-box">
              <b>You're eligible if:</b>
              <ul>
                <li>Immigrant or refugee parent, caregiver, or adult family member.</li>
                <li>Residing in King County seeking language, computer, or community navigation.</li>
                <li>Open to all residency and documentation statuses without barrier.</li>
              </ul>
              <p style="font-size:0.92rem;margin:0;">Questions? Email <a href="mailto:help@kandelia.org">help@kandelia.org</a> or call 206-760-1573</p>
            </div>

            <a class="btn btn-outline" href="#family-programs" style="margin-top:auto;">
              Explore Family Programs {SVGS['arrow-right']}
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Our Impact (Muted, soft background, refined non-glaring badges) -->
    <section class="section-impact" id="impact">
      <div class="w">
        <div class="impact-header">
          <span class="badge badge-sage" style="margin-bottom:12px;">Proven Outcomes</span>
          <h2 data-i18n="our_impact">Our Impact in Numbers</h2>
          <p class="lead">Read how Kandelia's culturally rooted programs supported students, parents, and communities this past year across King County.</p>
        </div>

        <div class="impact-badges-grid">
          <div class="impact-badge-card">
            <span class="impact-stat-number">570+</span>
            <div class="impact-stat-label" data-i18n="stat_served">Individuals Served</div>
            <div class="impact-stat-sub">Youth, parents, and caregivers supported across King County</div>
          </div>

          <div class="impact-badge-card">
            <span class="impact-stat-number">95%</span>
            <div class="impact-stat-label" data-i18n="stat_grad">Youth Graduation Rate</div>
            <div class="impact-stat-sub">Surpassing the 74% regional average for English language learners</div>
          </div>

          <div class="impact-badge-card">
            <span class="impact-stat-number">22</span>
            <div class="impact-stat-label" data-i18n="stat_lang">Languages Spoken</div>
            <div class="impact-stat-sub">Bilingual staff bridging cultures and school systems</div>
          </div>

          <div class="impact-badge-card">
            <span class="impact-stat-number">120+</span>
            <div class="impact-stat-label" data-i18n="stat_fam">Families Supported</div>
            <div class="impact-stat-sub">Provided with wraparound navigation, digital literacy, and relief</div>
          </div>
        </div>
      </div>
    </section>

    <!-- In Their Words Carousel (Light warm background, auto-scrolling with flower/hexagon avatars) -->
    <section class="section-testimonials" id="testimonials">
      <div class="w">
        <div class="section-header-center">
          <span class="badge badge-sage" style="margin-bottom:12px;">Community Voices</span>
          <h2 data-i18n="in_their_words">In Their Words</h2>
          <p class="lead">Reflections from the youth, parents, and community partners walking alongside us.</p>
        </div>

        <div class="carousel-container" id="testimonials-carousel" aria-roledescription="carousel" aria-label="Community Testimonials">
          <div class="carousel-track-wrapper">
            {testimonials_slides_html}
          </div>

          <div class="carousel-controls">
            <button class="carousel-btn carousel-btn-prev" aria-label="Previous testimonial">
              ←
            </button>
            <div class="carousel-dots">
              {testimonials_dots_html}
            </div>
            <button class="carousel-btn carousel-btn-next" aria-label="Next testimonial">
              →
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- Support Our Work CTA Banner (Strictly Aligned with Header Container Bounds) -->
    <section class="section-support-banner" id="support-banner">
      <div class="w">
        <div class="support-banner-card">
          <!-- Left Side Visual: Heart-Shaped Image Mask + Floating Accents -->
          <div class="support-heart-visual-col">
            <div class="support-heart-composition">
              <!-- Decorative Ambient Heart Glow Backdrop -->
              <div class="support-heart-backdrop" aria-hidden="true"></div>

              <!-- Prominent Heart-Masked Photo (Warm Community & Students) -->
              <div class="support-heart-main">
                <img src="{images['community']}" alt="Warm Kandelia community and refugee families" loading="lazy">
              </div>

              <!-- Floating Heart Photo Badge 1 (Top-Right: Hands Heart) -->
              <div class="floating-heart-badge badge-top-right" title="Community Care">
                <div class="floating-heart-badge-img">
                  <img src="{images['sunflower']}" alt="Heart hands">
                </div>
                <span class="floating-heart-mini-icon">❤️</span>
              </div>

              <!-- Floating Heart Photo Badge 2 (Bottom-Left: Youth Smiles) -->
              <div class="floating-heart-badge badge-bottom-left" title="Refugee Youth">
                <div class="floating-heart-badge-img">
                  <img src="{images['youth']}" alt="Smiling youth">
                </div>
                <span class="floating-heart-mini-icon">✨</span>
              </div>

              <!-- Floating Subtle Badge 3 (Bottom-Right Pill) -->
              <div class="floating-heart-pill badge-bottom-right">
                <span>🤝 50 Years Together</span>
              </div>
            </div>
          </div>

          <!-- Right/Adjacent Content Block: Heart Badge, Text, Pill CTA Button -->
          <div class="support-banner-content-col">
            <div class="support-heading-badge-wrap">
              <h3>Support Our Work</h3>
              <span class="support-heart-icon-badge" aria-hidden="true">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="var(--coral)" stroke="none">
                  <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
                </svg>
              </span>
            </div>

            <p class="support-banner-lead">
              Together, we can ensure every immigrant and refugee family has the resources, voice, and community to flourish.
            </p>

            <div class="support-banner-action">
              <a class="btn btn-coral btn-lg support-donate-pill-btn" href="https://kandelia-bloom.kindful.com/embeds/75568458-194c-4924-8a1b-de2cd76e4f92" target="_blank" rel="noopener">
                <svg class="icon icon-heart" width="18" height="18" viewBox="0 0 24 24" fill="currentColor" stroke="none" aria-hidden="true">
                  <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
                </svg>
                Support Our Work — Donate Today
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>


    <!-- ====================================================================
         SECTION 2: ABOUT US (EXPANDED: HISTORY, WORK, & TEAM)
         ==================================================================== -->
    <section class="section-about" id="about">
      <div class="w">
        <div class="section-header-center">
          <span class="badge badge-sage" style="margin-bottom:12px;">Our Heritage & Vision</span>
          <h2>About Kandelia</h2>
          <p class="lead">Founded on the principle that community care has no borders. Discover our 50-year journey, our holistic approach, and the dedicated team driving our mission forward.</p>
        </div>

        <!-- Sub-Navigation Tabs (History, Work, Team) -->
        <div class="about-subnav" role="tablist">
          <a class="about-subnav-btn active" href="#history">Our History</a>
          <a class="about-subnav-btn" href="#our-work">Our Work</a>
          <a class="about-subnav-btn" href="#our-team">Our Team (Staff & Board)</a>
        </div>

        <!-- 1. Our History -->
        <div class="about-block" id="history">
          <!-- Restated Mission Statement -->
          <div class="mission-restate-box">
            <span class="badge badge-sage" style="margin-bottom:10px;">Our Enduring Mission</span>
            <h3>"We remove barriers to immigrant and refugee success so that all communities can thrive without having to compromise values, heritage or ethnicity."</h3>
            <p>Rooted in Seattle since 1978, we walk alongside newcomer youth and families on their journey to self-determination, educational achievement, and belonging.</p>
          </div>

          <!-- Video Embed Container with Scalloped Edge & Flower Play Button -->
          <div class="video-embed-scalloped" id="kandelia-video-container" role="button" tabindex="0" aria-label="Watch video: The Story of Kandelia">
            <img class="video-poster-img" src="{images['event']}" alt="Video preview for The Story of Kandelia">
            <div class="video-play-overlay">
              <div class="video-flower-play-btn">
                {SVGS['play']}
              </div>
              <div class="video-caption">
                The Story of Kandelia: Deep Roots, Resilience & 50 Years of Mutual Aid
              </div>
              <span class="badge badge-gold" style="border:none;">Click to Preview Gala Documentary (3:45)</span>
            </div>
          </div>

          <!-- Core Truths Statement -->
          <div class="core-truths-box">
            <span class="badge badge-sage" style="margin-bottom:10px;">The Evolution to Kandelia</span>
            <h3>Our Core Truths: From VFA to Kandelia</h3>
            <p>
              In 1978, in the wake of the Vietnam War, a small group of Vietnamese refugees founded the <strong>Vietnamese Friendship Association (VFA)</strong> in Seattle. As newcomers navigating an unfamiliar culture and language, they realized that survival and dignity required mutual aid: helping one another find housing, learn English, navigate public schools, and preserve cultural traditions.
            </p>
            <p>
              Over the subsequent decades, South Seattle transformed into one of the most culturally diverse, multilingual communities in the United States. New waves of refugees arrived from East Africa (Somalia, Ethiopia, Eritrea), the Middle East (Iraq, Syria, Afghanistan), and Latin America. VFA expanded its programs to welcome every newcomer who walked through the door.
            </p>
            <p>
              In 2020, our organization embraced a new name: <strong>Kandelia</strong>. The <em>Kandelia obovata</em> is a resilient species of mangrove tree that thrives in brackish, tidal waters. Its deep, intertwined root system anchors shorelines against violent coastal storms, purifies the surrounding waters, and provides a safe, nurturing nursery for young marine life. Like the mangrove, our roots run deep in community resilience—offering shelter, strength, and life to every immigrant and refugee generation that follows.
            </p>
          </div>

          <!-- Interactive Visual Timeline with Playful Geometric Badges -->
          <h3 style="margin-bottom:24px;color:var(--navy);">Milestones of Community Resilience</h3>
          <div class="timeline-container">
            <div class="timeline-card">
              <div class="timeline-shape-badge badge-shape-pentagon">1978</div>
              <h4>Founded as VFA</h4>
              <p>Southeast Asian refugees establish the Vietnamese Friendship Association as a grassroots mutual aid collective in Seattle.</p>
            </div>

            <div class="timeline-card">
              <div class="timeline-shape-badge badge-shape-hexagon">2000s</div>
              <h4>Multicultural Expansion</h4>
              <p>Expanding school-based tutoring and family advocacy to support arriving East African, Middle Eastern, and Latinx families in King County.</p>
            </div>

            <div class="timeline-card">
              <div class="timeline-shape-badge badge-shape-flower">2020</div>
              <h4>Reborn as Kandelia</h4>
              <p>Honoring our Vietnamese founding while adopting the mangrove symbol to reflect a welcoming sanctuary for all immigrant cultures.</p>
            </div>

            <div class="timeline-card">
              <div class="timeline-shape-badge badge-shape-pebble">2026+</div>
              <h4>Whole-Family Advocacy</h4>
              <p>Pioneering multi-generational digital literacy, systemic policy advocacy, and celebrating 50 years of community belonging.</p>
            </div>
          </div>
        </div>

        <!-- 2. Our Work (3-Column Rounded Card Grid with Asymmetrical Contours) -->
        <div class="about-block" id="our-work">
          <div class="section-header-center">
            <span class="badge badge-sage" style="margin-bottom:12px;">Three Pillars of Impact</span>
            <h2>Our Work in Action</h2>
            <p class="lead">We provide wrap-around, culturally affirming support designed to foster self-advocacy and systemic change.</p>
          </div>

          <div class="our-work-grid">
            <div class="work-card">
              <div class="work-card-img" style="border-radius: 28px 14px 0 0;">
                <img src="{images['youth']}" alt="Kandelia youth learning together in a classroom">
              </div>
              <div class="work-card-body">
                <span class="badge badge-sage" style="margin-bottom:8px;align-self:flex-start;">Pillar 1 • Pentagon Accent</span>
                <h3>Supporting Students</h3>
                <p>We provide high school newcomer youth with academic coaching, bilingual tutoring, and culturally matched mentorship so they can graduate and pursue post-secondary dreams.</p>
                <ul class="work-bullets">
                  <li>After-school academic tutoring & ESL credit recovery</li>
                  <li>Paid summer internships & job readiness training</li>
                  <li>1-on-1 mentorship with career role models</li>
                  <li>College application & financial aid guidance</li>
                </ul>
              </div>
            </div>

            <div class="work-card">
              <div class="work-card-img" style="border-radius: 14px 28px 0 0;">
                <img src="{images['family']}" alt="Family workshop participants engaged in learning">
              </div>
              <div class="work-card-body">
                <span class="badge badge-sage" style="margin-bottom:8px;align-self:flex-start;">Pillar 2 • Flower Accent</span>
                <h3>Whole Family Support</h3>
                <p>We walk alongside immigrant and refugee parents, equipping them with language proficiency, computer confidence, and advocacy skills to navigate American institutions.</p>
                <ul class="work-bullets">
                  <li>Evening adult ESL classes with childcare</li>
                  <li>Hands-on digital literacy & computer training</li>
                  <li>Housing, healthcare & public benefits navigation</li>
                  <li>Tenant rights & citizenship preparation clinics</li>
                </ul>
              </div>
            </div>

            <div class="work-card">
              <div class="work-card-img" style="border-radius: 28px 28px 0 0;">
                <img src="{images['community']}" alt="Community partners collaborating at Kandelia">
              </div>
              <div class="work-card-body">
                <span class="badge badge-sage" style="margin-bottom:8px;align-self:flex-start;">Pillar 3 • Hexagon Accent</span>
                <h3>Working in Partnership</h3>
                <p>We forge deep coalitions with Seattle Public Schools, community health clinics, grassroots ethnic mutual aid groups, and civic leaders to dismantle structural barriers.</p>
                <ul class="work-bullets">
                  <li>Direct school district liaison & teacher partnerships</li>
                  <li>Multilingual referral network for emergency relief</li>
                  <li>Community-driven policy & immigrant rights advocacy</li>
                  <li>Collaborative cross-cultural events & annual forums</li>
                </ul>
              </div>
            </div>
          </div>
        </div>

        <!-- 3. Our Team (Staff & Board with Playful Organic Shapes) -->
        <div class="about-block" id="our-team">
          <!-- Staff Hero Banner with Organic Wave Contour -->
          <div class="staff-hero-banner staff-hero-frame-wave">
            <div class="staff-hero-image">
              <img src="{images['community']}" alt="Kandelia diverse staff and community members">
            </div>
            <div class="staff-hero-text">
              <span class="badge badge-sage" style="margin-bottom:8px;">Rooted in Community</span>
              <h3>Our Staff: Reflecting the Communities We Serve</h3>
              <p>
                Over 90% of Kandelia's staff identify as immigrants, refugees, or children of immigrants. Together, our team speaks more than 15 languages and dialects, bringing profound cultural humility, lived empathy, and deep neighborhood relationships to every family interaction.
              </p>
            </div>
          </div>

          <!-- Staff Leadership Grid (Flower, Hexagon, Pentagon, Pebble Avatars) -->
          <h3 style="margin-bottom:24px;color:var(--navy);">Staff Leadership</h3>
          <div class="staff-grid">
            {staff_cards_html}
          </div>

          <!-- Our Board (Alternating Hexagon, Flower, Pentagon, Pebble Avatars) -->
          <div class="board-section-title">
            <div>
              <span class="badge badge-sage" style="margin-bottom:8px;">Governance & Stewardship</span>
              <h3>Our Board of Directors</h3>
              <p style="margin:0;">Passionate educators, legal advocates, finance executives, and youth alumni guiding our strategic mission.</p>
            </div>
          </div>

          <div class="board-grid">
            {board_cards_html}
          </div>

          <!-- Board CTA Callout Box -->
          <div class="board-cta-card">
            <div class="board-cta-text">
              <h3>Interested in joining our Board of Directors?</h3>
              <p>We are seeking dedicated community advocates, corporate allies, and nonprofit champions to help guide Kandelia through our 50th milestone year.</p>
            </div>
            <a class="btn btn-primary" href="#careers-board">
              View Board Job Description {SVGS['arrow-right']}
            </a>
          </div>

          <!-- Staff & Board Quotes Carousel -->
          <div class="section-header-center" style="margin-bottom:28px;">
            <span class="badge badge-sage">Reflections & Commitments</span>
            <h3 style="margin-top:8px;">Voices from Our Team & Leadership</h3>
          </div>
          <div class="carousel-container" id="staff-board-carousel" aria-label="Staff and Board Reflections">
            <div class="carousel-track-wrapper">
              {staff_quotes_slides_html}
            </div>
            <div class="carousel-controls">
              <button class="carousel-btn carousel-btn-prev" aria-label="Previous quote">←</button>
              <div class="carousel-dots">
                {staff_quotes_dots_html}
              </div>
              <button class="carousel-btn carousel-btn-next" aria-label="Next quote">→</button>
            </div>
          </div>
        </div>
      </div>
    </section>


    <!-- ====================================================================
         SECTION 3: GET SUPPORT (PROGRAMS)
         ==================================================================== -->
    <section class="section-get-support" id="get-support">
      <div class="w">
        <div class="section-header-center">
          <span class="badge badge-sage" style="margin-bottom:12px;">Free Programs for Immigrants & Refugees</span>
          <h2>Get Support</h2>
          <p class="lead">Whether you are a high school student striving to graduate and build a career, or a parent seeking English and digital tools, Kandelia is here for your family.</p>
        </div>

        <!-- Top Anchor Cards with Playful Decorative Badges -->
        <div class="support-anchor-grid">
          <a class="support-anchor-card" href="#high-school-programs">
            <div class="support-anchor-info">
              <span class="badge badge-sage" style="margin-bottom:8px;">For Youth Ages 14–21</span>
              <h3>High School Programs</h3>
              <p>Tutoring, paid internships, mentorship, and college preparation.</p>
            </div>
            <div class="support-anchor-arrow shape-clip-hexagon" style="background:var(--navy);">↓</div>
          </a>

          <a class="support-anchor-card" href="#family-programs">
            <div class="support-anchor-info">
              <span class="badge badge-sage" style="margin-bottom:8px;">For Parents & Adults</span>
              <h3>Family Programs</h3>
              <p>Adult ESL, computer labs, tenant rights, and resource navigation.</p>
            </div>
            <div class="support-anchor-arrow shape-clip-flower-8" style="background:var(--coral);">↓</div>
          </a>
        </div>

        <!-- High School Programs Block -->
        <div class="programs-block" id="high-school-programs">
          <div style="margin-bottom:24px;">
            <span class="badge badge-sage">High School Pathways</span>
            <h3 style="font-size:1.8rem;margin-top:6px;">High School Programs</h3>
            <p>Cultivating academic excellence, self-confidence, and career readiness for newcomer youth.</p>
          </div>

          <div class="programs-4grid">
            <div class="subprogram-card">
              <span class="subprogram-badge">Program 1</span>
              <h4>English Classes</h4>
              <p>Multilingual learner tutoring, small-group reading circles, vocabulary acquisition, and individualized academic language support.</p>
            </div>
            <div class="subprogram-card">
              <span class="subprogram-badge">Program 2</span>
              <h4>Job Readiness & Career</h4>
              <p>Resume crafting, workplace communication, mock interviews, and access to paid 8-week summer internships across Seattle.</p>
            </div>
            <div class="subprogram-card">
              <span class="subprogram-badge">Program 3</span>
              <h4>Mentorship</h4>
              <p>1-on-1 pairings with community professionals who share lived immigrant experiences, offering guidance through graduation and beyond.</p>
            </div>
            <!-- Visual Community Card with Pentagon Motif -->
            <div class="subprogram-visual-card" style="border-radius: 32px 14px 32px 14px;">
              <span class="visual-card-shape-overlay">🎓 Youth Community</span>
              <img src="{images['youth']}" alt="Kandelia youth learning and connecting">
              <div class="visual-card-caption">
                "Finding our voices together as future community leaders."
              </div>
            </div>
          </div>

          <div class="eligibility-box" id="support-eligibility">
            <b>You're eligible if:</b>
            <ul>
              <li>You are an immigrant, refugee, or asylee youth aged 14 to 21.</li>
              <li>You are currently enrolled in a King County high school.</li>
              <li>You are seeking tutoring, credit recovery, or career mentorship.</li>
            </ul>
            <p style="margin:0;">Ready to enroll or have questions? Email us directly at <a href="mailto:help@kandelia.org"><strong>help@kandelia.org</strong></a> or call <strong>206-760-1573</strong>.</p>
          </div>
        </div>

        <!-- Family Programs Block -->
        <div class="programs-block" id="family-programs">
          <div style="margin-bottom:24px;">
            <span class="badge badge-sage">Family Empowerment</span>
            <h3 style="font-size:1.8rem;margin-top:6px;">Family Programs</h3>
            <p>Providing multi-generational immigrant and refugee households with tools to build security and thriving futures.</p>
          </div>

          <div class="programs-4grid">
            <div class="subprogram-card">
              <span class="subprogram-badge">Program 1</span>
              <h4>English Classes (ESL)</h4>
              <p>Accessible adult ESL courses emphasizing daily communication, talking with doctors and teachers, and workplace confidence.</p>
            </div>
            <div class="subprogram-card">
              <span class="subprogram-badge">Program 2</span>
              <h4>Digital Literacy Classes</h4>
              <p>Hands-on laptop training: mastering school portals, online job applications, internet safety, and telehealth appointment booking.</p>
            </div>
            <div class="subprogram-card">
              <span class="subprogram-badge">Program 3</span>
              <h4>Workshops & Advocacy</h4>
              <p>Regular clinics on tenant rights, affordable housing lotteries, utility assistance, citizenship interview prep, and nutrition resources.</p>
            </div>
            <!-- Visual Card with Flower Motif -->
            <div class="subprogram-visual-card" style="border-radius: 14px 32px 14px 32px;">
              <span class="visual-card-shape-overlay">🌱 Family Workshops</span>
              <img src="{images['family']}" alt="Family participants at a Kandelia workshop">
              <div class="visual-card-caption">
                "Equipping parents to guide their children's success."
              </div>
            </div>
          </div>

          <div class="eligibility-box">
            <b>You're eligible if:</b>
            <ul>
              <li>You are an adult immigrant or refugee caregiver living in King County.</li>
              <li>You want to build English proficiency, digital skills, or connect to community benefits.</li>
              <li>All languages and documentation statuses warmly welcomed.</li>
            </ul>
            <p style="margin:0;">To join an upcoming cohort, email <a href="mailto:help@kandelia.org"><strong>help@kandelia.org</strong></a> or speak with a bilingual navigator at <strong>206-760-1573</strong>.</p>
          </div>
        </div>
      </div>
    </section>


    <!-- ====================================================================
         SECTION 4: GET INVOLVED
         ==================================================================== -->
    <section class="section-get-involved" id="get-involved">
      <div class="w">
        <div class="section-header-center">
          <span class="badge badge-sage" style="margin-bottom:12px;">Take Action With Us</span>
          <h2>Get Involved</h2>
          <p class="lead">Your time, generosity, and advocacy power our programs and transform the lives of youth and families every single day.</p>
        </div>

        <div class="involved-3grid">
          <div class="action-card card-give" id="give">
            <span class="badge badge-coral" style="margin-bottom:12px;align-self:flex-start;">Sustain Our Programs</span>
            <h3>Give</h3>
            <p>Every dollar directly provides tutoring, digital devices, and emergency resource navigation for newcomer families.</p>
            <details class="styled-details" open>
              <summary class="styled-summary">
                <span>Ways to Give</span>
                <span class="acc-icon">+</span>
              </summary>
              <div class="details-content">
                <ul style="padding-left:20px;margin-bottom:10px;">
                  <li>One-time gift via credit card or ACH</li>
                  <li>Monthly sustaining donor circles</li>
                  <li>Employer matching gifts (double your impact!)</li>
                  <li>Vehicle donations & stock transfers</li>
                  <li>Mail a check to PO Box 28058, Seattle, WA 98118</li>
                </ul>
              </div>
            </details>
            <a class="btn btn-coral action-card-btn" href="https://kandelia-bloom.kindful.com/embeds/75568458-194c-4924-8a1b-de2cd76e4f92" target="_blank" rel="noopener">
              {SVGS['heart']} Donate Today
            </a>
          </div>

          <div class="action-card card-volunteer" id="volunteer">
            <span class="badge badge-sage" style="margin-bottom:12px;align-self:flex-start;">Share Your Time</span>
            <h3>Volunteer</h3>
            <p>Join an inspiring group of community volunteers supporting youth tutoring, adult conversation, and special events.</p>
            <details class="styled-details">
              <summary class="styled-summary">
                <span>Volunteer Opportunities</span>
                <span class="acc-icon">+</span>
              </summary>
              <div class="details-content">
                <ul style="padding-left:20px;margin-bottom:10px;">
                  <li>After-school high school academic tutor</li>
                  <li>Adult ESL conversation partner</li>
                  <li>50th Anniversary Gala planning committee</li>
                  <li>Guest speaker for youth career exploration</li>
                </ul>
              </div>
            </details>
            <a class="btn btn-primary action-card-btn" href="https://forms.gle/kandelia-volunteer-mockup" target="_blank" rel="noopener">
              Volunteer Sign-Up Survey {SVGS['arrow-right']}
            </a>
          </div>

          <div class="action-card card-partner" id="partner">
            <span class="badge badge-sage" style="margin-bottom:12px;align-self:flex-start;">Build Alliances</span>
            <h3>Partner</h3>
            <p>We collaborate with school districts, regional employers, healthcare clinics, and civic foundations to expand our canopy.</p>
            <details class="styled-details">
              <summary class="styled-summary">
                <span>Partnership Examples</span>
                <span class="acc-icon">+</span>
              </summary>
              <div class="details-content">
                <ul style="padding-left:20px;margin-bottom:10px;">
                  <li>Corporate internship host employer</li>
                  <li>School district program integration</li>
                  <li>Community healthcare referral coalition</li>
                  <li>Foundation endowment & grant partnerships</li>
                </ul>
              </div>
            </details>
            <a class="btn btn-outline action-card-btn" href="mailto:info@kandelia.org?subject=Partnership Inquiry with Kandelia">
              Email info@kandelia.org
            </a>
          </div>
        </div>

        <!-- Newsletter Card with Human Check Captcha -->
        <div class="newsletter-card">
          <div class="newsletter-info">
            <span class="badge badge-sage" style="margin-bottom:10px;">Stay Connected</span>
            <h3>Stay in the Loop</h3>
            <p>Receive updates, student stories, and event invitations a few times a year. No spam, ever.</p>
            <div class="newsletter-social-icons">
              <a href="https://linkedin.com/company/kandelia" target="_blank" rel="noopener" class="social-circle-btn shape-clip-flower-8" aria-label="LinkedIn">
                {SVGS['linkedin']}
              </a>
              <a href="https://facebook.com/kandelia" target="_blank" rel="noopener" class="social-circle-btn shape-clip-hexagon" aria-label="Facebook">
                {SVGS['facebook']}
              </a>
              <a href="https://instagram.com/kandelia" target="_blank" rel="noopener" class="social-circle-btn shape-clip-pentagon" aria-label="Instagram">
                {SVGS['instagram']}
              </a>
            </div>
          </div>

          <div>
            <form id="newsletter-signup-form" novalidate>
              <div class="captcha-container">
                <div class="captcha-checkbox-wrap">
                  <div class="captcha-checkbox" id="human-captcha-box" role="checkbox" aria-checked="false" tabindex="0" aria-label="Confirm you are human"></div>
                  <span class="captcha-label">Confirm you're human</span>
                </div>
                <div class="captcha-badge-tag">
                  {SVGS['shield']}
                  <span>Privacy Check</span>
                </div>
              </div>

              <div class="newsletter-form-row">
                <label for="newsletter-email-input" class="sr-only">Email address</label>
                <input class="newsletter-input" id="newsletter-email-input" type="email" placeholder="Enter your email address" required>
                <button class="btn btn-primary" type="submit">
                  Sign Up
                </button>
              </div>
              <div id="newsletter-feedback-msg" class="newsletter-feedback" role="alert"></div>
            </form>
          </div>
        </div>

        <!-- Compact Impact Snapshot with Playful Shapes -->
        <div class="impact-badges-grid" style="margin-bottom:0;">
          <div class="impact-badge-card" style="padding:24px;">
            <span class="impact-stat-number" style="font-size:36px;">570+</span>
            <div class="impact-stat-sub">Served Yearly</div>
          </div>
          <div class="impact-badge-card" style="padding:24px;">
            <span class="impact-stat-number" style="font-size:36px;">95%</span>
            <div class="impact-stat-sub">High School Grad</div>
          </div>
          <div class="impact-badge-card" style="padding:24px;">
            <span class="impact-stat-number" style="font-size:36px;">22</span>
            <div class="impact-stat-sub">Languages Spoken</div>
          </div>
          <div class="impact-badge-card" style="padding:24px;">
            <span class="impact-stat-number" style="font-size:36px;">120+</span>
            <div class="impact-stat-sub">Families Empowered</div>
          </div>
        </div>
      </div>
    </section>


    <!-- ====================================================================
         SECTION 5: STORIES & IMPACT (PLAYFUL FLOWER, HEXAGON, PENTAGON SHAPES)
         ==================================================================== -->
    <section class="section-stories" id="stories-impact">
      <div class="w">
        <!-- Pinned Impact Report -->
        <div class="pinned-report-card" id="impact-report">
          <div class="report-cover-box">
            <div>
              <span class="badge badge-sage" style="margin-bottom:12px;border:none;background:rgba(255,255,255,0.2);color:#fff;">Annual Report</span>
              <b>2026 Impact Report</b>
            </div>
            <span>Kandelia Community Alliance</span>
          </div>

          <div class="report-details-body">
            <span class="badge badge-gold" style="margin-bottom:10px;">Featured Publication</span>
            <h3>Deep Roots, Lasting Flourish</h3>
            <p>Explore our comprehensive evaluation of student graduation rates, family economic mobility, and direct assistance distribution across King County.</p>
            <ul class="report-datapoints">
              <li>{SVGS['check']} <strong>570+ Newcomers</strong> guided through academic and civic pathways</li>
              <li>{SVGS['check']} <strong>95% Graduation Rate</strong> among cohort high school seniors</li>
              <li>{SVGS['check']} <strong>$240,000+ Distributed</strong> in direct emergency family relief & rental aid</li>
              <li>{SVGS['check']} <strong>1,200+ Hours</strong> of bilingual adult digital literacy training delivered</li>
            </ul>
            <div style="display:flex;gap:14px;flex-wrap:wrap;">
              <a class="btn btn-primary" href="https://www.kandelia.org" target="_blank" rel="noopener">
                Read the 2026 Impact Report {SVGS['arrow-right']}
              </a>
              <a class="btn btn-outline" href="mailto:info@kandelia.org?subject=Request Impact Report PDF">
                Request PDF Copy
              </a>
            </div>
          </div>
        </div>

        <!-- 4 Stories Grid (Each image framed with custom flower, pentagon, hexagon, arch) -->
        <div class="section-header-center" id="stories">
          <span class="badge badge-sage" style="margin-bottom:12px;">Roots & Routes</span>
          <h2>Immigrant Stories in Seattle</h2>
          <p class="lead">The folks in our community who have shared their journeys, triumphs, and hopes with us. Click any story to read the full account.</p>
        </div>

        <div class="stories-grid">
          {stories_cards_html}
        </div>
      </div>
    </section>

    <!-- Wave Divider 6: Stories to Careers -->
    <svg class="section-wave-divider to-sand wave-stories-careers" viewBox="0 0 1200 44" preserveAspectRatio="none" aria-hidden="true"><path d="M0,12 C400,36 800,0 1200,22 L1200,44 L0,44 Z"></path></svg>

    <!-- ====================================================================
         SECTION 6: WORK WITH US / CAREERS
         ==================================================================== -->
    <section class="section-careers" id="careers">
      <div class="w">
        <div class="section-header-center">
          <span class="badge badge-sage" style="margin-bottom:12px;">Careers & Leadership</span>
          <h2>Work With Us</h2>
          <p class="lead">Join an awesome, passionate team dedicated to equity, dignity, and immigrant empowerment in South Seattle and King County.</p>
        </div>

        <!-- Categorized Tabs -->
        <div class="careers-tabs" role="tablist">
          <button class="careers-tab-btn active" data-target="careers-staff" role="tab" aria-selected="true">Staff Positions</button>
          <button class="careers-tab-btn" data-target="careers-contract" role="tab" aria-selected="false">Contracted Roles</button>
          <button class="careers-tab-btn" data-target="careers-youth" role="tab" aria-selected="false">Youth Leadership</button>
          <button class="careers-tab-btn" data-target="careers-board" role="tab" aria-selected="false" id="careers-board-tab">Board of Directors</button>
        </div>

        <div class="careers-panel active" id="careers-staff" role="tabpanel">
          {careers_staff_html}
        </div>

        <div class="careers-panel" id="careers-contract" role="tabpanel">
          {careers_contract_html}
        </div>

        <div class="careers-panel" id="careers-youth" role="tabpanel">
          {careers_youth_html}
        </div>

        <div class="careers-panel" id="careers-board" role="tabpanel">
          <div class="mission-restate-box" style="margin-bottom:28px;">
            <h3>Board of Directors Opportunity</h3>
            <p>Kandelia is governed by a committed volunteer board that sets strategic priorities, safeguards financial health, and champions immigrant justice. Board members serve a 3-year term and commit 4–6 hours monthly.</p>
          </div>
          {careers_board_html}
        </div>
      </div>
    </section>

    <!-- Wave Divider 7: Careers to Footer -->
    <svg class="section-wave-divider to-sand wave-careers-footer" viewBox="0 0 1200 44" preserveAspectRatio="none" aria-hidden="true"><path d="M0,20 C450,44 750,0 1200,24 L1200,44 L0,44 Z"></path></svg>

  </main>


  <!-- Global Footer -->
  <footer class="site-footer" id="contact" role="contentinfo">
    <div class="w">
      <div class="footer-grid">
        <div class="footer-brand">
          <div class="footer-logo-wrap">
            <img src="{images['logo_footer']}" alt="Kandelia logo">
          </div>
          <div class="footer-tagline">
            Removing barriers to immigrant and refugee success.
          </div>
          <div class="footer-contact-info">
            <p>PO Box 28058<br>Seattle, WA 98118</p>
            <p>Phone: 206-760-1573<br>Email: <a href="mailto:info@kandelia.org" style="color:#fff;">info@kandelia.org</a></p>
            <p><strong>Tax ID: 91-1122532</strong> (501(c)(3) Organization)</p>
          </div>
          <div class="newsletter-social-icons" style="margin-top:14px;">
            <a href="https://linkedin.com/company/kandelia" target="_blank" rel="noopener" class="social-circle-btn shape-clip-flower-8" aria-label="LinkedIn">
              {SVGS['linkedin']}
            </a>
            <a href="https://facebook.com/kandelia" target="_blank" rel="noopener" class="social-circle-btn shape-clip-hexagon" aria-label="Facebook">
              {SVGS['facebook']}
            </a>
            <a href="https://instagram.com/kandelia" target="_blank" rel="noopener" class="social-circle-btn shape-clip-pentagon" aria-label="Instagram">
              {SVGS['instagram']}
            </a>
          </div>
        </div>

        <div class="footer-col">
          <h4>About Us</h4>
          <ul>
            <li><a href="#history">Our History & Roots</a></li>
            <li><a href="#our-work">Our Work & Impact</a></li>
            <li><a href="#our-team">Our Staff & Board</a></li>
            <li><a href="#careers">Work With Us (Careers)</a></li>
            <li><a href="#who-we-help">Who We Help</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Programs</h4>
          <ul>
            <li><a href="#high-school-programs">High School Programs</a></li>
            <li><a href="#family-programs">Family Programs</a></li>
            <li><a href="#support-eligibility">Eligibility & Registration</a></li>
          </ul>
          <h4 style="margin-top:20px;">Get Involved</h4>
          <ul>
            <li><a href="#give">Donate</a></li>
            <li><a href="#volunteer">Volunteer Opportunities</a></li>
            <li><a href="#partner">Community Partnerships</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Stories & Impact</h4>
          <ul>
            <li><a href="#impact-report">2026 Annual Report</a></li>
            <li><a href="#stories">Immigrant Stories</a></li>
            <li><a href="#testimonials">Community Voices</a></li>
            <li><a href="#contact">Contact Us</a></li>
          </ul>
          <div style="margin-top:24px;">
            <a class="btn btn-coral btn-sm" href="https://kandelia-bloom.kindful.com/embeds/75568458-194c-4924-8a1b-de2cd76e4f92" target="_blank" rel="noopener">
              {SVGS['heart']} Donate
            </a>
          </div>
        </div>
      </div>

      <div class="footer-bottom-bar">
        <span>© 2026 Kandelia. All rights reserved. 501(c)(3) Nonprofit Organization.</span>
        <span>Enhanced with Organic Shapes & Playful Visual Layouts (2026 Standard).</span>
      </div>
    </div>
  </footer>


  <!-- Accessible Global Modal Dialog -->
  <div class="modal-overlay" id="global-modal-overlay" aria-hidden="true" role="dialog" aria-modal="true">
    <div class="modal-dialog">
      <div class="modal-header">
        <h3 id="modal-title">Modal Title</h3>
        <button class="modal-close-btn" id="modal-close-button" aria-label="Close modal dialog">
          {SVGS['close']}
        </button>
      </div>
      <div class="modal-body" id="modal-content-area">
        <!-- Injected via JavaScript -->
      </div>
    </div>
  </div>

  <!-- JavaScript Execution -->
  <script>
{JS}
  </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_document)

print(f"index.html successfully updated! Total size: {len(html_document)} bytes")
