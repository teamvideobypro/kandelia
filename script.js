/**
 * Kandelia 2026 Redesign - Interactive Architecture
 * Accessible, Responsive, Self-Contained JavaScript
 */

(function() {
  'use strict';

  // =========================================================================
  // 1. Translation Dictionary (English, Español, Tiếng Việt, العربية, Soomaali)
  // =========================================================================
  const TRANSLATIONS = {
    'en': {
      'get_help': 'Get help: help@kandelia.org',
      'contact': 'Contact',
      'about_us': 'About Us',
      'our_history': 'Our History',
      'our_work': 'Our Work',
      'our_team': 'Our Team',
      'get_support': 'Get Support',
      'high_school': 'High School Programs',
      'family_prog': 'Family Programs',
      'get_involved': 'Get Involved',
      'give': 'Give',
      'volunteer': 'Volunteer',
      'partner': 'Partner',
      'stories_impact': 'Stories & Impact',
      'impact_report': '2026 Impact Report',
      'stories': 'Immigrant Stories',
      'donate': 'Donate',
      'hero_tag': '50 Years of Immigrant & Refugee Belonging',
      'hero_title': 'We remove barriers to immigrant and refugee success',
      'hero_lead': 'We are a community organization addressing systemic inequities so immigrant and refugee families and communities can thrive without having to compromise values, heritage or ethnicity. Through holistic youth programs, adult learning, and family advocacy, we walk alongside new arrivals on their journey to belonging.',
      'btn_support': "I'm looking for support",
      'btn_help': 'I want to help',
      'stat_served': 'Individuals Served',
      'stat_grad': 'Youth Graduation Rate',
      'stat_lang': 'Languages Spoken',
      'stat_fam': 'Families Supported',
      'who_we_help': 'Who We Help',
      'our_impact': 'Our Impact in Numbers',
      'in_their_words': 'In Their Words',
      'work_with_us': 'Work With Us (Careers)'
    },
    'es': {
      'get_help': 'Obtenga ayuda: help@kandelia.org',
      'contact': 'Contacto',
      'about_us': 'Sobre Nosotros',
      'our_history': 'Nuestra Historia',
      'our_work': 'Nuestro Trabajo',
      'our_team': 'Nuestro Equipo',
      'get_support': 'Obtener Apoyo',
      'high_school': 'Programas de Secundaria',
      'family_prog': 'Programas Familiares',
      'get_involved': 'Involúcrate',
      'give': 'Donar',
      'volunteer': 'Voluntariado',
      'partner': 'Colaborar',
      'stories_impact': 'Historias e Impacto',
      'impact_report': 'Informe de Impacto 2026',
      'stories': 'Historias de Inmigrantes',
      'donate': 'Donar Ahora',
      'hero_tag': '50 Años de Apoyo a Inmigrantes y Refugiados',
      'hero_title': 'Eliminamos barreras hacia el éxito de inmigrantes y refugiados',
      'hero_lead': 'Somos una organización comunitaria que aborda inequidades sistémicas para que familias inmigrantes y refugiadas prosperen sin comprometer sus valores ni su identidad.',
      'btn_support': 'Busco apoyo',
      'btn_help': 'Quiero ayudar',
      'stat_served': 'Personas Atendidas',
      'stat_grad': 'Tasa de Graduación Juvenil',
      'stat_lang': 'Idiomas Hablados',
      'stat_fam': 'Familias Apoyadas',
      'who_we_help': 'A Quiénes Ayudamos',
      'our_impact': 'Nuestro Impacto en Cifras',
      'in_their_words': 'En Sus Propias Palabras',
      'work_with_us': 'Trabaja con Nosotros'
    },
    'vi': {
      'get_help': 'Nhận trợ giúp: help@kandelia.org',
      'contact': 'Liên Hệ',
      'about_us': 'Về Chúng Tôi',
      'our_history': 'Lịch Sử Chúng Tôi',
      'our_work': 'Công Việc Của Chúng Tôi',
      'our_team': 'Đội Ngũ Chúng Tôi',
      'get_support': 'Nhận Hỗ Trợ',
      'high_school': 'Chương Trình Trung Học',
      'family_prog': 'Chương Trình Gia Đình',
      'get_involved': 'Tham Gia',
      'give': 'Đóng Góp',
      'volunteer': 'Tình Nguyện',
      'partner': 'Đối Tác',
      'stories_impact': 'Câu Chuyện & Tác Động',
      'impact_report': 'Báo Cáo Tác Động 2026',
      'stories': 'Câu Chuyện Người Nhập Cư',
      'donate': 'Quyên Góp',
      'hero_tag': '50 Năm Đồng Hành Cùng Người Nhập Cư & Tị Nạn',
      'hero_title': 'Chúng tôi xóa bỏ rào cản để người nhập cư và tị nạn thành công',
      'hero_lead': 'Chúng tôi là tổ chức cộng đồng giải quyết bất bình đẳng hệ thống để các gia đình nhập cư và tị nạn phát triển toàn diện mà không phải đánh đổi bản sắc hay văn hóa.',
      'btn_support': 'Tôi đang tìm kiếm hỗ trợ',
      'btn_help': 'Tôi muốn giúp đỡ',
      'stat_served': 'Cá Nhân Được Phục Vụ',
      'stat_grad': 'Tỷ Lệ Tốt Nghiệp Thanh Thiếu Niên',
      'stat_lang': 'Ngôn Ngữ Được Sử Dụng',
      'stat_fam': 'Gia Đình Được Hỗ Trợ',
      'who_we_help': 'Những Người Chúng Tôi Giúp Đỡ',
      'our_impact': 'Tác Động Của Chúng Tôi Qua Các Con Số',
      'in_their_words': 'Theo Lời Của Họ',
      'work_with_us': 'Cơ Hội Việc Làm'
    },
    'ar': {
      'get_help': 'المساعدة: help@kandelia.org',
      'contact': 'اتصل بنا',
      'about_us': 'من نحن',
      'our_history': 'تاريخنا',
      'our_work': 'أعمالنا',
      'our_team': 'فريقنا',
      'get_support': 'طلب الدعم',
      'high_school': 'برامج المدرسة الثانوية',
      'family_prog': 'برامج العائلات',
      'get_involved': 'شارك معنا',
      'give': 'تبرع',
      'volunteer': 'تطوع',
      'partner': 'شراكة',
      'stories_impact': 'القصص والأثر',
      'impact_report': 'تقرير الأثر 2026',
      'stories': 'قصص المهاجرين',
      'donate': 'تبرع الآن',
      'hero_tag': '50 عاماً في خدمة المهاجرين واللاجئين',
      'hero_title': 'نزيل الحواجز أمام نجاح المهاجرين واللاجئين',
      'hero_lead': 'نحن منظمة مجتمعية تعالج أوجه عدم المساواة المنهجية حتى تتمكن عائلات المهاجرين واللاجئين من الازدهار دون المساومة على قيمهم أو هويتهم.',
      'btn_support': 'أبحث عن الدعم',
      'btn_help': 'أريد المساعدة',
      'stat_served': 'أفراد تم خدمتهم',
      'stat_grad': 'نسبة تخرج الشباب',
      'stat_lang': 'لغات يتم التحدث بها',
      'stat_fam': 'عائلات تم دعمها',
      'who_we_help': 'من نساعد',
      'our_impact': 'أثرنا بالأرقام',
      'in_their_words': 'بكلماتهم',
      'work_with_us': 'وظائف وانضم إلينا'
    },
    'so': {
      'get_help': 'Caawin: help@kandelia.org',
      'contact': 'Xiriir',
      'about_us': 'Nagu Saabsan',
      'our_history': 'Taariikhdeena',
      'our_work': 'Shaqadeena',
      'our_team': 'Kooxdeena',
      'get_support': 'Hel Taageero',
      'high_school': 'Barnaamijyada Dugsiga Sare',
      'family_prog': 'Barnaamijyada Qoyska',
      'get_involved': 'Nagu Soo Biir',
      'give': 'Wax Bixi',
      'volunteer': 'Iskood U Shaqee',
      'partner': 'Wada-shaqeyn',
      'stories_impact': 'Sheekooyinka & Saameynta',
      'impact_report': 'Warbixinta Saameynta 2026',
      'stories': 'Sheekooyinka Muhaajiriinta',
      'donate': 'Ku Deeq',
      'hero_tag': '50 Sano oo Taageero Muhaajiriinta iyo Qaxootiga ah',
      'hero_title': 'Waxaan meesha ka saarnaa caqabadaha hortaagan guusha muhaajiriinta iyo qaxootiga',
      'hero_lead': 'Waxaan nahay urur bulsho oo u taagan in qoysaska muhaajiriinta iyo qaxootigu horumar gaaraan iyaga oo ilaashanaya qiyamkooda iyo dhaqankooda.',
      'btn_support': 'Waxaan raadinayaa taageero',
      'btn_help': 'Waxaan rabaa inaan caawiyo',
      'stat_served': 'Shakhsiyaad La Caawiyey',
      'stat_grad': 'Heerka Qalin-jabinta Dhalinyarada',
      'stat_lang': 'Luuqadaha Lagu Hadlo',
      'stat_fam': 'Qoysaska La Taageeray',
      'who_we_help': 'Yaan Caawinaa',
      'our_impact': 'Saameynteena Tiro ahaan',
      'in_their_words': 'Hadalladooda',
      'work_with_us': 'Nala Shaqee'
    }
  };

  function updateLanguage(langCode) {
    const dict = TRANSLATIONS[langCode] || TRANSLATIONS['en'];
    const isRTL = (langCode === 'ar');

    document.documentElement.setAttribute('lang', langCode);
    document.documentElement.setAttribute('dir', isRTL ? 'rtl' : 'ltr');

    // Update all elements with data-i18n
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      if (dict[key]) {
        el.textContent = dict[key];
      }
    });

    console.log(`Language switched to: ${langCode} (RTL: ${isRTL})`);
  }

  // =========================================================================
  // 2. Auto-Scrolling Carousels with Pause-on-Hover & Accessibility
  // =========================================================================
  function initCarousel(carouselElement, intervalMs = 5000) {
    if (!carouselElement) return;

    const slides = carouselElement.querySelectorAll('.carousel-slide');
    const dots = carouselElement.querySelectorAll('.carousel-dot');
    const prevBtn = carouselElement.querySelector('.carousel-btn-prev');
    const nextBtn = carouselElement.querySelector('.carousel-btn-next');
    let currentIndex = 0;
    let timer = null;
    let isPaused = false;

    function showSlide(index) {
      if (index < 0) index = slides.length - 1;
      if (index >= slides.length) index = 0;
      currentIndex = index;

      slides.forEach((slide, idx) => {
        slide.classList.toggle('active', idx === currentIndex);
        slide.setAttribute('aria-hidden', idx !== currentIndex);
      });

      dots.forEach((dot, idx) => {
        dot.classList.toggle('active', idx === currentIndex);
        dot.setAttribute('aria-current', idx === currentIndex ? 'true' : 'false');
      });
    }

    function nextSlide() {
      showSlide(currentIndex + 1);
    }

    function prevSlide() {
      showSlide(currentIndex - 1);
    }

    function startTimer() {
      stopTimer();
      timer = setInterval(() => {
        if (!isPaused) nextSlide();
      }, intervalMs);
    }

    function stopTimer() {
      if (timer) clearInterval(timer);
    }

    // Event listeners
    if (nextBtn) nextBtn.addEventListener('click', () => { nextSlide(); startTimer(); });
    if (prevBtn) prevBtn.addEventListener('click', () => { prevSlide(); startTimer(); });

    dots.forEach((dot, idx) => {
      dot.addEventListener('click', () => {
        showSlide(idx);
        startTimer();
      });
    });

    // Pause on hover & focus
    carouselElement.addEventListener('mouseenter', () => { isPaused = true; });
    carouselElement.addEventListener('mouseleave', () => { isPaused = false; });
    carouselElement.addEventListener('focusin', () => { isPaused = true; });
    carouselElement.addEventListener('focusout', () => { isPaused = false; });

    // Touch Swipe support
    let touchStartX = 0;
    let touchEndX = 0;
    carouselElement.addEventListener('touchstart', e => {
      touchStartX = e.changedTouches[0].screenX;
    }, { passive: true });

    carouselElement.addEventListener('touchend', e => {
      touchEndX = e.changedTouches[0].screenX;
      if (touchStartX - touchEndX > 50) {
        nextSlide();
        startTimer();
      } else if (touchEndX - touchStartX > 50) {
        prevSlide();
        startTimer();
      }
    }, { passive: true });

    // Initial setup
    showSlide(0);
    startTimer();
  }

  // =========================================================================
  // 3. Modals System (Board Bios, Stories Reader, Video Player)
  // =========================================================================
  function initModals() {
    const overlay = document.getElementById('global-modal-overlay');
    const modalTitle = document.getElementById('modal-title');
    const modalContent = document.getElementById('modal-content-area');
    const closeBtn = document.getElementById('modal-close-button');
    let lastActiveElement = null;

    if (!overlay) return;

    function openModal(title, htmlContent) {
      lastActiveElement = document.activeElement;
      modalTitle.textContent = title;
      modalContent.innerHTML = htmlContent;
      overlay.classList.add('open');
      overlay.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
      if (closeBtn) closeBtn.focus();
    }

    function closeModal() {
      overlay.classList.remove('open');
      overlay.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
      modalContent.innerHTML = '';
      if (lastActiveElement) lastActiveElement.focus();
    }

    if (closeBtn) closeBtn.addEventListener('click', closeModal);
    overlay.addEventListener('click', (e) => {
      if (e.target === overlay) closeModal();
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && overlay.classList.contains('open')) {
        closeModal();
      }
    });

    // Attach to Leader bio cards & buttons
    document.querySelectorAll('.open-leader-bio').forEach(el => {
      function triggerLeaderModal(e) {
        if (e) {
          e.preventDefault();
          e.stopPropagation();
        }
        const name = el.getAttribute('data-name');
        const role = el.getAttribute('data-role');
        const photo = el.getAttribute('data-photo');
        const languages = el.getAttribute('data-languages');
        const bio = el.getAttribute('data-bio');
        const quote = el.getAttribute('data-quote') || '';

        const content = `
          <div style="display:flex;align-items:center;gap:20px;margin-bottom:22px;">
            ${photo ? `<div style="width:84px;height:84px;border-radius:9999px;overflow:hidden;flex-shrink:0;border:3px solid var(--teal);box-shadow:0 4px 12px rgba(42,210,201,0.25);"><img src="${photo}" alt="${name}" style="width:100%;height:100%;object-fit:cover;display:block;"></div>` : ''}
            <div>
              <h4 style="font-size:1.45rem;color:var(--navy);margin-bottom:4px;font-weight:700;">${name}</h4>
              <p style="color:var(--teal-dark);font-weight:700;margin-bottom:2px;font-size:1.05rem;">${role}</p>
              ${languages ? `<span style="font-size:0.88rem;color:var(--text-muted);">${languages}</span>` : ''}
            </div>
          </div>
          <div class="bio-editorial-body">
            ${bio.trim().startsWith('<p') ? bio : `<p style="white-space:pre-line;">${bio}</p>`}
          </div>
          ${quote ? `
          <blockquote class="bio-quote-callout">
            "${quote}"
          </blockquote>` : ''}
          <div style="margin-top:24px;padding-top:16px;border-top:1px solid #E5E7EB;display:flex;justify-content:flex-end;">
            <button class="btn btn-outline btn-sm" onclick="document.getElementById('modal-close-button').click();" style="border-radius:20px;padding:8px 24px;cursor:pointer;">
              Close Bio
            </button>
          </div>
        `;
        openModal(name, content);
      }

      el.addEventListener('click', triggerLeaderModal);
      el.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          triggerLeaderModal(e);
        }
      });
    });

    // Attach to Board bio cards & buttons
    document.querySelectorAll('.open-board-bio').forEach(el => {
      function triggerBoardModal(e) {
        if (e) {
          e.preventDefault();
          e.stopPropagation();
        }
        const name = el.getAttribute('data-name');
        const role = el.getAttribute('data-role');
        const tenure = el.getAttribute('data-tenure');
        const photo = el.getAttribute('data-photo');
        const bio = el.getAttribute('data-bio');
        const quote = el.getAttribute('data-quote') || '';

        const content = `
          <div style="display:flex;align-items:center;gap:20px;margin-bottom:22px;">
            ${photo ? `<div style="width:84px;height:84px;border-radius:9999px;overflow:hidden;flex-shrink:0;border:3px solid var(--teal);box-shadow:0 4px 12px rgba(42,210,201,0.25);"><img src="${photo}" alt="${name}" style="width:100%;height:100%;object-fit:cover;display:block;"></div>` : ''}
            <div>
              <h4 style="font-size:1.45rem;color:var(--navy);margin-bottom:4px;font-weight:700;">${name}</h4>
              <p style="color:var(--teal-dark);font-weight:700;margin-bottom:2px;font-size:1.05rem;">${role}</p>
              ${tenure ? `<span style="font-size:0.88rem;color:var(--text-muted);">${tenure}</span>` : ''}
            </div>
          </div>
          <div class="bio-editorial-body">
            ${bio.trim().startsWith('<p') ? bio : `<p style="white-space:pre-line;">${bio}</p>`}
          </div>
          ${quote ? `
          <blockquote class="bio-quote-callout">
            "${quote}"
          </blockquote>` : ''}
          <div style="margin-top:24px;padding-top:16px;border-top:1px solid #E5E7EB;display:flex;justify-content:flex-end;">
            <button class="btn btn-outline btn-sm" onclick="document.getElementById('modal-close-button').click();" style="border-radius:20px;padding:8px 24px;cursor:pointer;">
              Close Bio
            </button>
          </div>
        `;
        openModal(name, content);
      }

      el.addEventListener('click', triggerBoardModal);
      el.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          triggerBoardModal(e);
        }
      });
    });

    // Attach to Story cards (In-page modal reader with authentic text, quotes, and imagery)
    document.querySelectorAll('.open-story-reader').forEach(card => {
      function triggerStoryModal(e) {
        if (e) {
          e.preventDefault();
        }
        const title = card.getAttribute('data-title') || 'Roots & Routes Story';
        const subtitle = card.getAttribute('data-subtitle') || '';
        const quote = card.getAttribute('data-quote') || '';
        const fullHtml = card.getAttribute('data-story-html') || '';
        const imgSrc = card.getAttribute('data-image') || (card.querySelector('img') ? card.querySelector('img').src : '');

        const imgPos = (imgSrc.includes('story_ana') || imgSrc.includes('story_sunflower_tulip')) ? 'center' : 'center 15%';
        const content = `
          <div style="margin-bottom:18px;">
            <span class="badge badge-coral" style="margin-bottom:10px;display:inline-block;">Roots & Routes: Immigrant Stories</span>
            <p style="font-size:1.15rem;color:var(--coral);font-weight:700;margin:6px 0 0;">${subtitle}</p>
          </div>
          ${imgSrc ? `<div class="story-modal-hero-img-wrap"><img src="${imgSrc}" alt="${title}" style="width:100%;height:100%;object-fit:cover;object-position:${imgPos};display:block;"></div>` : ''}
          ${quote ? `
          <blockquote style="background:#FAF7F2;border-left:5px solid var(--coral);padding:18px 24px;border-radius:12px;font-style:italic;color:var(--navy);font-size:1.12rem;line-height:1.55;margin-bottom:24px;">
            "${quote}"
          </blockquote>` : ''}
          <div class="story-full-body" style="font-size:1.06rem;line-height:1.8;color:var(--text-body);">
            ${fullHtml}
          </div>
          <div style="margin-top:32px;padding-top:20px;border-top:1px solid #E5E7EB;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;">
            <a href="/giving" class="btn btn-primary btn-sm" style="border-radius:20px;padding:8px 20px;">
              Support Immigrant Youth →
            </a>
            <button class="btn btn-outline btn-sm" onclick="document.getElementById('modal-close-button').click();" style="border-radius:20px;padding:8px 24px;cursor:pointer;">
              Close Story
            </button>
          </div>
        `;
        openModal(title, content);
      }

      card.addEventListener('click', triggerStoryModal);
      card.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          triggerStoryModal(e);
        }
      });
    });

    // Attach to Video container
    const videoContainer = document.getElementById('kandelia-video-container');
    if (videoContainer) {
      videoContainer.addEventListener('click', () => {
        const content = `
          <div style="background:#0A1724;border-radius:16px;aspect-ratio:16/9;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff;text-align:center;padding:30px;position:relative;overflow:hidden;">
            <div style="width:80px;height:80px;border-radius:9999px;background:#D94532;display:grid;place-items:center;margin-bottom:16px;cursor:pointer;box-shadow:0 8px 24px rgba(217,69,50,0.5);">
              <svg style="width:36px;height:36px;fill:currentColor;margin-left:4px;" viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
            </div>
            <h4 style="font-size:1.4rem;color:#fff;margin-bottom:8px;">The Story of Kandelia: Roots, Resilience & 50 Years</h4>
            <p style="color:rgba(255,255,255,0.8);max-width:520px;font-size:0.95rem;">Premiering for our landmark 50th Anniversary Gala in May 2027. Full streaming broadcast will be hosted here with multilingual captions in Vietnamese, Somali, Spanish, and Arabic.</p>
            <div style="position:absolute;bottom:16px;display:flex;gap:12px;">
              <span class="badge" style="background:rgba(255,255,255,0.15);color:#fff;border:none;">HD 1080p</span>
              <span class="badge" style="background:rgba(255,255,255,0.15);color:#fff;border:none;">Duration: 3:45</span>
              <span class="badge" style="background:rgba(255,255,255,0.15);color:#fff;border:none;">CC: Multi-Language</span>
            </div>
          </div>
        `;
        openModal("Kandelia Documentary & May 2027 Gala Preview", content);
      });
    }

    // Attach to Partner With Us modal buttons
    document.querySelectorAll('.open-partner-modal').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();

        const content = `
          <div style="margin-bottom:20px;">
            <span class="badge badge-blue" style="margin-bottom:10px;">Institutional Alliances & Sponsorships</span>
            <p style="font-size:1.05rem;line-height:1.65;color:var(--text-body);margin-top:8px;">
              Thank you for your interest in partnering with Kandelia! We welcome collaborations with school districts, corporate employers, philanthropic foundations, and community allies to expand educational and economic opportunities for immigrant and refugee communities.
            </p>
          </div>

          <!-- Official Email Box with 1-Click Copy -->
          <div style="background:#F0FAF9;border:1.5px solid var(--teal);border-radius:16px;padding:20px 24px;margin-bottom:22px;">
            <div style="font-size:0.82rem;font-weight:700;color:var(--teal-dark);text-transform:uppercase;letter-spacing:0.05em;margin-bottom:6px;">Official Partnerships Email</div>
            <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;">
              <span style="font-size:1.35rem;font-weight:700;color:var(--navy);font-family:monospace;">Info@kandelia.org</span>
              <button class="btn btn-primary btn-sm" id="copy-partner-email-btn" onclick="
                navigator.clipboard.writeText('Info@kandelia.org').then(() => {
                  this.textContent = 'Copied! ✓';
                  setTimeout(() => { this.textContent = 'Copy Email Address'; }, 3000);
                });
              " style="border-radius:20px;padding:7px 16px;">Copy Email Address</button>
            </div>
            <p style="font-size:0.85rem;color:var(--text-muted);margin-top:10px;margin-bottom:0;">
              Our institutional partnerships team responds to all foundation, employer, and civic inquiries within 1-2 business days.
            </p>
          </div>

          <!-- Direct Actions: Email App vs Web Gmail -->
          <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(210px, 1fr));gap:12px;margin-bottom:24px;">
            <a href="mailto:Info@kandelia.org?subject=Partnership%20Inquiry%20with%20Kandelia" class="btn btn-outline" style="display:flex;align-items:center;justify-content:center;gap:8px;text-align:center;padding:12px 18px;font-size:0.95rem;">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
              Open in Default Email App →
            </a>
            <a href="https://mail.google.com/mail/?view=cm&fs=1&to=Info@kandelia.org&su=Partnership%20Inquiry%20with%20Kandelia" target="_blank" rel="noopener noreferrer" class="btn btn-coral" style="display:flex;align-items:center;justify-content:center;gap:8px;text-align:center;padding:12px 18px;font-size:0.95rem;">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 15h-2v-6h2v6zm4 0h-2v-6h2v6zm-2-8c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1z"/></svg>
              Compose in Web Gmail ↗
            </a>
          </div>

          <!-- Key Partnership Areas -->
          <div style="background:#F8FAFC;border-radius:14px;padding:16px 20px;margin-bottom:20px;border:1px solid #E2E8F0;">
            <h5 style="font-size:0.95rem;color:var(--navy);font-weight:700;margin-bottom:8px;">Ways to Partner with Kandelia:</h5>
            <ul style="font-size:0.9rem;color:var(--text-body);line-height:1.6;margin:0;padding-left:18px;">
              <li><strong>Institutional & Foundation Grants:</strong> Multi-year operational and programmatic support.</li>
              <li><strong>Corporate Matching & Sponsorships:</strong> Workplace giving, employee match programs, and gala sponsors.</li>
              <li><strong>Youth Internships & Mentorship:</strong> Host paid high school student interns in STEM, arts, and business.</li>
            </ul>
          </div>

          <!-- Organization & Phone Details -->
          <div style="padding-top:14px;border-top:1px solid #E5E7EB;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;font-size:0.88rem;color:var(--text-muted);">
            <span>📞 Phone: <a href="tel:2064525200" style="color:var(--teal-dark);font-weight:600;">(206) 452-5200</a></span>
            <span>📍 3829B S. Edmunds St. Box 9, Seattle, WA 98118</span>
          </div>
        `;
        openModal("Partner With Kandelia", content);
      });
    });

    // Attach to Intake & Enrollment Advocate modal buttons (Get Help page)
    document.querySelectorAll('.open-intake-modal').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();

        const content = `
          <div style="margin-bottom:18px;">
            <span class="badge badge-teal" style="margin-bottom:8px;">Free & Confidential Program Intake</span>
            <p style="font-size:1.02rem;line-height:1.6;color:var(--text-body);margin-top:6px;">
              Connect with a multilingual Kandelia intake advocate to enroll in youth or adult programs, or request direct family navigation support. No documentation status is ever required.
            </p>
          </div>

          <form id="intake-request-form" style="display:flex;flex-direction:column;gap:12px;margin-bottom:18px;background:#F8FAFC;padding:16px;border-radius:14px;border:1px solid #E2E8F0;">
            <div>
              <label for="intake-name" style="display:block;font-size:0.88rem;font-weight:700;color:var(--navy);margin-bottom:4px;">Student or Parent Name *</label>
              <input type="text" id="intake-name" required placeholder="Full Name" style="width:100%;padding:10px 14px;border-radius:10px;border:1px solid #CBD5E1;font-size:0.95rem;">
            </div>
            <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,200px),1fr));gap:10px;">
              <div>
                <label for="intake-contact" style="display:block;font-size:0.88rem;font-weight:700;color:var(--navy);margin-bottom:4px;">Phone or Email *</label>
                <input type="text" id="intake-contact" required placeholder="(206) 555-0199 or email" style="width:100%;padding:10px 14px;border-radius:10px;border:1px solid #CBD5E1;font-size:0.95rem;">
              </div>
              <div>
                <label for="intake-program" style="display:block;font-size:0.88rem;font-weight:700;color:var(--navy);margin-bottom:4px;">Program Interest</label>
                <select id="intake-program" style="width:100%;padding:10px 12px;border-radius:10px;border:1px solid #CBD5E1;font-size:0.95rem;background:#fff;">
                  <option value="Youth Programs (Ages 14-21)">High School Youth Programs (14–21)</option>
                  <option value="Adult & Family Workshops">Adult & Family Workshops</option>
                  <option value="Legal & Healthcare Navigation">Legal & Healthcare Navigation</option>
                  <option value="General Support">General Intake / Not Sure Yet</option>
                </select>
              </div>
            </div>
            <div>
              <label for="intake-lang" style="display:block;font-size:0.88rem;font-weight:700;color:var(--navy);margin-bottom:4px;">Preferred Language & Notes</label>
              <input type="text" id="intake-lang" placeholder="e.g., Spanish, Arabic, Somali, Vietnamese, English..." style="width:100%;padding:10px 14px;border-radius:10px;border:1px solid #CBD5E1;font-size:0.95rem;">
            </div>
            <button type="submit" class="btn btn-primary" style="width:100%;margin-top:4px;">Submit Intake Request →</button>
            <div id="intake-form-feedback" style="display:none;padding:12px 14px;border-radius:10px;background:#E6FAF9;color:#0F5D59;font-weight:600;font-size:0.92rem;border:1px solid rgba(42,210,201,0.4);"></div>
          </form>

          <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,210px),1fr));gap:10px;margin-bottom:14px;">
            <a href="tel:2067601573" class="btn btn-outline" style="justify-content:center;font-size:0.92rem;padding:10px 14px;">
              📞 Call 206-760-1573
            </a>
            <a href="mailto:help@kandelia.org?subject=Intake%20Request%20for%20Kandelia%20Programs" class="btn btn-coral" style="justify-content:center;font-size:0.92rem;padding:10px 14px;">
              ✉️ Email help@kandelia.org
            </a>
          </div>

          <div style="padding-top:12px;border-top:1px solid #E5E7EB;font-size:0.86rem;color:var(--text-muted);display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px;">
            <span>🕒 Mon–Fri, 9:00 AM – 5:00 PM</span>
            <span>📍 3829B S. Edmunds St. Box 9, Seattle, WA</span>
          </div>
        `;
        openModal("Enroll Student or Contact an Intake Advocate", content);

        const intakeForm = document.getElementById('intake-request-form');
        const intakeFeedback = document.getElementById('intake-form-feedback');
        if (intakeForm && intakeFeedback) {
          intakeForm.addEventListener('submit', (ev) => {
            ev.preventDefault();
            const nameVal = document.getElementById('intake-name').value.trim();
            const progVal = document.getElementById('intake-program').value;
            intakeFeedback.style.display = 'block';
            intakeFeedback.innerHTML = `✅ Thank you, <strong>${nameVal || 'friend'}</strong>! Your intake request for <strong>${progVal}</strong> has been received. A multilingual advocate will reach out within 1 business day (or call <a href="tel:2067601573" style="color:var(--navy);text-decoration:underline;">206-760-1573</a> for immediate assistance).`;
            intakeForm.reset();
          });
        }
      });
    });

    // Attach to Same-Page 2026 Impact Report Modal buttons
    document.querySelectorAll('.open-impact-report-modal').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();

        const content = `
          <div style="margin-bottom:18px;">
            <span class="badge badge-green" style="margin-bottom:8px;">Annual Publication • 2026 Impact Report</span>
            <h4 style="font-size:1.35rem;color:var(--navy);margin:6px 0 8px;font-weight:700;">Deep Roots, Lasting Flourish</h4>
            <p style="font-size:0.98rem;line-height:1.6;color:var(--text-body);margin:0;">
              Our annual evaluation of student graduation rates, family economic mobility, and direct assistance across King County.
            </p>
          </div>

          <div class="report-modal-metrics-grid">
            <div class="report-metric-tile" style="background:#F0FAF9;border-color:rgba(42,210,201,0.3);">
              <div class="report-metric-num">570+</div>
              <div class="report-metric-label" style="color:var(--teal-dark);">Newcomers Served</div>
              <p>Guided through academic, language, and civic pathways.</p>
            </div>
            <div class="report-metric-tile" style="background:#F4FBE8;border-color:rgba(151,215,0,0.35);">
              <div class="report-metric-num">95%</div>
              <div class="report-metric-label" style="color:#2A6615;">Graduation Rate</div>
              <p>Among cohort high school seniors at Seattle World School.</p>
            </div>
            <div class="report-metric-tile" style="background:#FEECEE;border-color:rgba(244,54,76,0.25);">
              <div class="report-metric-num">$240K+</div>
              <div class="report-metric-label" style="color:var(--coral);">Direct Family Relief</div>
              <p>Distributed in emergency rental, food, and utility aid.</p>
            </div>
            <div class="report-metric-tile" style="background:#F0F2FA;border-color:rgba(30,34,170,0.2);">
              <div class="report-metric-num">1,200+</div>
              <div class="report-metric-label" style="color:var(--navy);">Digital Literacy Hours</div>
              <p>Delivered in bilingual workshops for parents &amp; caregivers.</p>
            </div>
          </div>

          <div class="bio-editorial-body" style="margin-bottom:18px;">
            <p>Over the past year, Kandelia deepened its commitment to holistic, culturally responsive support for newly arrived immigrant and refugee families across King County—partnering closely with Seattle World School educators and multilingual family advocates.</p>
            <p>Through after-school tutoring, Running Start college readiness coaching, paid youth internships, and direct emergency relief, 95% of participating seniors graduated on time—many becoming the first in their families to enter university.</p>
          </div>

          <div style="padding-top:16px;border-top:1px solid #E5E7EB;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;">
            <a class="btn btn-coral btn-sm" href="https://kandelia-bloom.kindful.com/embeds/75568458-194c-4924-8a1b-de2cd76e4f92" target="_blank" rel="noopener">Support 2026 Programs →</a>
            <button type="button" class="btn btn-outline btn-sm" onclick="document.getElementById('modal-close-button').click();">Close Report</button>
          </div>
        `;
        openModal("2026 Impact Report", content);
      });
    });

    // Attach to Request 2026 Impact Report PDF modal buttons
    document.querySelectorAll('.open-request-pdf-modal').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();

        const content = `
          <div style="margin-bottom:18px;">
            <span class="badge badge-green" style="margin-bottom:8px;">Annual Publication • 2026 Impact Report</span>
            <p style="font-size:1.02rem;line-height:1.6;color:var(--text-body);margin-top:6px;">
              Request a complimentary digital PDF copy of Kandelia’s <strong>2026 Impact Report: Deep Roots, Lasting Flourish</strong>, including audited financials and program outcomes.
            </p>
          </div>
          <form id="pdf-request-form" style="display:flex;flex-direction:column;gap:12px;margin-bottom:18px;background:#F8FAFC;padding:16px;border-radius:14px;border:1px solid #E2E8F0;">
            <div>
              <label for="pdf-req-name" style="display:block;font-size:0.88rem;font-weight:700;color:var(--navy);margin-bottom:4px;">Your Name *</label>
              <input type="text" id="pdf-req-name" required placeholder="Full Name" style="width:100%;padding:10px 14px;border-radius:10px;border:1px solid #CBD5E1;font-size:0.95rem;">
            </div>
            <div>
              <label for="pdf-req-email" style="display:block;font-size:0.88rem;font-weight:700;color:var(--navy);margin-bottom:4px;">Email Address *</label>
              <input type="email" id="pdf-req-email" required placeholder="you@example.org" style="width:100%;padding:10px 14px;border-radius:10px;border:1px solid #CBD5E1;font-size:0.95rem;">
            </div>
            <button type="submit" class="btn btn-primary" style="width:100%;">Send PDF Copy Request →</button>
            <div id="pdf-req-feedback" style="display:none;padding:12px 14px;border-radius:10px;background:#E6FAF9;color:#0F5D59;font-weight:600;font-size:0.92rem;border:1px solid rgba(42,210,201,0.4);"></div>
          </form>
          <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,210px),1fr));gap:10px;">
            <a href="mailto:info@kandelia.org?subject=Request%202026%20Impact%20Report%20PDF" class="btn btn-outline" style="justify-content:center;font-size:0.92rem;padding:10px 14px;">
              ✉️ Email info@kandelia.org
            </a>
            <button type="button" class="btn btn-coral open-impact-report-modal" style="justify-content:center;font-size:0.92rem;padding:10px 14px;">
              Read Report Summary →
            </button>
          </div>
        `;
        openModal("Request 2026 Impact Report PDF", content);

        const pdfForm = document.getElementById('pdf-req-feedback') ? document.getElementById('pdf-request-form') : null;
        const pdfFeedback = document.getElementById('pdf-req-feedback');
        if (pdfForm && pdfFeedback) {
          pdfForm.addEventListener('submit', (ev) => {
            ev.preventDefault();
            const emailVal = document.getElementById('pdf-req-email').value.trim();
            pdfFeedback.style.display = 'block';
            pdfFeedback.innerHTML = `✅ Request confirmed! We will email the <strong>2026 Impact Report PDF</strong> to <strong>${emailVal}</strong> shortly.`;
            pdfForm.reset();
          });
        }
      });
    });

    // Attach to Gala Sponsorship modal buttons
    document.querySelectorAll('.open-sponsor-modal').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();

        const content = `
          <div style="margin-bottom:18px;">
            <span class="badge badge-blue" style="margin-bottom:8px;">50th Anniversary Gala • May 14, 2027</span>
            <p style="font-size:1.02rem;line-height:1.6;color:var(--text-body);margin-top:6px;">
              Partner with Kandelia as an institutional or corporate sponsor for our landmark 50th Anniversary "Sip &amp; Celebrate" Gala at Seattle Center Pavilion.
            </p>
          </div>
          <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,180px),1fr));gap:10px;margin-bottom:18px;">
            <div style="background:#F0FAF9;padding:14px;border-radius:12px;border:1px solid rgba(42,210,201,0.3);">
              <div style="font-weight:700;color:var(--navy);font-size:0.95rem;">Community Champion</div>
              <div style="color:var(--teal-dark);font-weight:700;font-size:1.15rem;margin:4px 0;">$2,500</div>
              <div style="font-size:0.84rem;color:var(--text-muted);">Table for 6 + program recognition</div>
            </div>
            <div style="background:#F0F2FA;padding:14px;border-radius:12px;border:1px solid rgba(30,34,170,0.2);">
              <div style="font-weight:700;color:var(--navy);font-size:0.95rem;">Solidarity Partner</div>
              <div style="color:var(--navy);font-weight:700;font-size:1.15rem;margin:4px 0;">$5,000</div>
              <div style="font-size:0.84rem;color:var(--text-muted);">VIP table for 10 + stage acknowledgment</div>
            </div>
            <div style="background:#FEECEE;padding:14px;border-radius:12px;border:1px solid rgba(244,54,76,0.25);">
              <div style="font-weight:700;color:var(--navy);font-size:0.95rem;">Presenting Sponsor</div>
              <div style="color:var(--coral);font-weight:700;font-size:1.15rem;margin:4px 0;">$10,000</div>
              <div style="font-size:0.84rem;color:var(--text-muted);">Premier branding + keynote recognition</div>
            </div>
          </div>
          <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,210px),1fr));gap:10px;">
            <a href="mailto:gala@kandelia.org?subject=Become%20a%20Sponsor%20for%2050th%20Anniversary%20Gala" class="btn btn-primary" style="justify-content:center;font-size:0.92rem;padding:10px 14px;">
              ✉️ Email gala@kandelia.org
            </a>
            <a href="https://mail.google.com/mail/?view=cm&fs=1&to=gala@kandelia.org&su=Become%20a%20Sponsor%20for%2050th%20Anniversary%20Gala" target="_blank" rel="noopener noreferrer" class="btn btn-coral" style="justify-content:center;font-size:0.92rem;padding:10px 14px;">
              Compose in Web Gmail ↗
            </a>
          </div>
        `;
        openModal("Become a 50th Anniversary Gala Sponsor", content);
      });
    });

    // Attach to DAF & Wire Transfer modal buttons
    document.querySelectorAll('.open-daf-modal').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();

        const content = `
          <div style="margin-bottom:18px;">
            <span class="badge badge-teal" style="margin-bottom:8px;">Tax-Deductible 501(c)(3) Giving</span>
            <p style="font-size:1.02rem;line-height:1.6;color:var(--text-body);margin-top:6px;">
              Recommend a grant through your Donor-Advised Fund (Fidelity Charitable, Schwab Charitable, Vanguard Charitable, Seattle Foundation) or initiate a direct wire/stock transfer.
            </p>
          </div>
          <div style="background:#F8FAFC;border-radius:14px;padding:18px;border:1px solid #E2E8F0;margin-bottom:18px;font-size:0.95rem;line-height:1.65;">
            <div style="margin-bottom:6px;"><strong>Legal Organization Name:</strong> Kandelia</div>
            <div style="margin-bottom:6px;"><strong>Federal Tax ID (EIN):</strong> <code style="background:#E6FAF9;padding:2px 8px;border-radius:6px;font-weight:700;color:var(--navy);">91-1122532</code></div>
            <div style="margin-bottom:6px;"><strong>Mailing Address:</strong> 3829B S. Edmunds St. Box 9, Seattle, WA 98118</div>
            <div><strong>Wire / ACH &amp; Stock Instructions:</strong> Contact our finance &amp; development team at <a href="mailto:info@kandelia.org?subject=Wire%20or%20DAF%20Transfer%20Instructions" style="color:var(--teal-dark);font-weight:600;">info@kandelia.org</a> or <a href="tel:2064525200" style="color:var(--teal-dark);font-weight:600;">(206) 452-5200</a> for secure routing &amp; DTC numbers.</div>
          </div>
          <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,210px),1fr));gap:10px;">
            <a href="mailto:info@kandelia.org?subject=DAF%20or%20Wire%20Transfer%20Inquiry" class="btn btn-primary" style="justify-content:center;font-size:0.92rem;padding:10px 14px;">
              ✉️ Request Wire Routing
            </a>
            <a href="https://mail.google.com/mail/?view=cm&fs=1&to=info@kandelia.org&su=DAF%20or%20Wire%20Transfer%20Inquiry" target="_blank" rel="noopener noreferrer" class="btn btn-coral" style="justify-content:center;font-size:0.92rem;padding:10px 14px;">
              Compose in Web Gmail ↗
            </a>
          </div>
        `;
        openModal("Give via Donor-Advised Fund (DAF) or Wire", content);
      });
    });
  }

  // =========================================================================
  // 4. Captcha & Newsletter Verification
  // =========================================================================
  function initCaptcha() {
    const captchaBox = document.getElementById('human-captcha-box');
    const feedback = document.getElementById('newsletter-feedback-msg');
    const form = document.getElementById('newsletter-signup-form');
    let isHuman = false;

    if (!captchaBox) return;

    captchaBox.addEventListener('click', () => {
      if (isHuman) return;

      captchaBox.classList.add('verifying');
      setTimeout(() => {
        captchaBox.classList.remove('verifying');
        captchaBox.classList.add('verified');
        captchaBox.innerHTML = `
          <svg style="width:18px;height:18px;stroke:currentColor;fill:none;stroke-width:3.5;" viewBox="0 0 24 24">
            <polyline points="20 6 9 17 4 12"></polyline>
          </svg>
        `;
        isHuman = true;
        if (feedback) {
          feedback.className = 'newsletter-feedback';
          feedback.textContent = '';
        }
      }, 500);
    });

    if (form) {
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        const emailInput = document.getElementById('newsletter-email-input');
        const email = emailInput ? emailInput.value.trim() : '';

        if (!email || !email.includes('@')) {
          if (feedback) {
            feedback.className = 'newsletter-feedback error';
            feedback.textContent = 'Please enter a valid email address.';
          }
          return;
        }

        if (!isHuman) {
          if (feedback) {
            feedback.className = 'newsletter-feedback error';
            feedback.textContent = 'Please check the box to confirm you are human.';
          }
          return;
        }

        // Success!
        if (feedback) {
          feedback.className = 'newsletter-feedback success';
          feedback.textContent = '🎉 Thank you for subscribing to Kandelia news! Check your inbox soon.';
        }
        if (emailInput) emailInput.value = '';
      });
    }
  }

  // =========================================================================
  // 5. Careers & About Us Tabs
  // =========================================================================
  function initTabs() {
    // Careers Tabs
    const careerTabs = document.querySelectorAll('.careers-tab-btn');
    const careerPanels = document.querySelectorAll('.careers-panel');

    careerTabs.forEach(btn => {
      btn.addEventListener('click', () => {
        const target = btn.getAttribute('data-target');
        careerTabs.forEach(b => b.classList.toggle('active', b === btn));
        careerPanels.forEach(p => p.classList.toggle('active', p.id === target));
      });
    });

    // About Us Subnav Jumps
    const aboutSubnavBtns = document.querySelectorAll('.about-subnav-btn');
    aboutSubnavBtns.forEach(btn => {
      btn.addEventListener('click', (e) => {
        aboutSubnavBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
      });
    });
  }

  // =========================================================================
  // 6. Mobile Navigation Drawer & Sticky Header
  // =========================================================================
  function initNavigation() {
    const mobileBtn = document.getElementById('mobile-menu-toggle');
    const mobileDrawer = document.getElementById('mobile-navigation-drawer');
    const header = document.querySelector('.site-header');

    if (mobileBtn && mobileDrawer) {
      mobileBtn.addEventListener('click', () => {
        const isOpen = mobileDrawer.classList.toggle('open');
        mobileBtn.setAttribute('aria-expanded', isOpen);
        mobileBtn.innerHTML = isOpen ? '✕ Close' : 'Menu ☰';
      });

      // Close drawer on link click
      mobileDrawer.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
          mobileDrawer.classList.remove('open');
          mobileBtn.setAttribute('aria-expanded', 'false');
          mobileBtn.innerHTML = 'Menu ☰';
        });
      });
    }

    // Scroll shadow
    window.addEventListener('scroll', () => {
      if (header) {
        header.classList.toggle('scrolled', window.scrollY > 20);
      }
    }, { passive: true });

    // Language selector change
    const langSelect = document.getElementById('language-picker-select');
    if (langSelect) {
      langSelect.addEventListener('change', (e) => {
        updateLanguage(e.target.value);
      });
    }
  }

  // =========================================================================
  // Initialize Everything on DOMContentLoaded
  // =========================================================================
  document.addEventListener('DOMContentLoaded', () => {
    initNavigation();
    document.querySelectorAll('.carousel-container').forEach(el => {
      initCarousel(el, el.id === 'staff-board-carousel' ? 6500 : 5500);
    });
    initModals();
    initCaptcha();
    initTabs();
    console.log("Kandelia Redesign 2026 initialized successfully!");
  });

})();
