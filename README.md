# Kandelia – Removing Barriers to Immigrant & Refugee Success

A redesigned, highly accessible web experience for Kandelia (celebrating 50 years of community belonging, youth empowerment, and family advocacy in King County and South Seattle).

##  Key Features
- **Warm, Airy Color Palette:** Built with Warm Cream (`#FAF7F2`), Soft Sand (`#F5EFE6`), Light Sage (`#EEF5F0`), Deep Navy (`#12263A`), and Vibrant Coral (`#E05A47`).
- **5 Organic Geometric Shape Masks:** Normalized SVG clip paths including 8-petal and 12-petal flowers, four-leaf clover, rounded hexagons, soft pentagons, and organic arches.
- **Heart-Masked Community Banner:** Dedicated 2-column "Support Our Work" CTA with organic heart-shaped masking and floating photo badges, strictly aligned to header navigation bounds.
- **50th Anniversary Milestone Celebration:** Balanced 2-column event showcase with layered golden dashed imagery on the left, Seattle skyline photography, and community sponsor highlights.
- **Story Reader & Bio Modals:** Interactive modals for student journeys, staff leadership, and board biographies.
- **Multi-Language Switcher:** Native translations in English, Spanish, Vietnamese, Ukrainian, Somali, and Arabic (with dynamic RTL layout support).
- **Zero Subject Cropping:** Strict preservation of all authentic photography subjects, faces, and panoramic aspect ratios.

##  Project Structure
- `index.html`: Complete, self-contained production HTML with embedded high-resolution assets and SVG defs.
- `styles.css`: Design system and CSS architecture with custom shapes, responsive breakpoints, and animations.
- `script.js`: Interactive logic for modals, multi-language switcher, carousels, and human-check captcha.
- `site_data.py`: Structured dataset for staff, board, stories, testimonials, and careers.
- `build_enhanced_site.py`: Generator script synthesizing data and assets into `index.html`.
- `assets/`: Original high-resolution photography assets.

##  Deployment
Deployed independently on Vercel with automatic continuous integration.
