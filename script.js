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
      'giving': 'Giving',
      'giving_impact': 'Giving & Impact Tiers',
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

    // Attach to Board bio buttons
    document.querySelectorAll('.open-board-bio').forEach(btn => {
      btn.addEventListener('click', () => {
        const name = btn.getAttribute('data-name');
        const role = btn.getAttribute('data-role');
        const tenure = btn.getAttribute('data-tenure');
        const bio = btn.getAttribute('data-bio');
        const quote = btn.getAttribute('data-quote');
        const initials = btn.getAttribute('data-initials');
        const color = btn.getAttribute('data-color') || '#12263A';

        const content = `
          <div style="display:flex;align-items:center;gap:20px;margin-bottom:24px;">
            <div style="width:72px;height:72px;border-radius:9999px;background:${color};color:#fff;display:grid;place-items:center;font-size:1.6rem;font-weight:700;flex-shrink:0;">
              ${initials}
            </div>
            <div>
              <h4 style="font-size:1.4rem;color:#12263A;margin-bottom:4px;">${name}</h4>
              <p style="color:#D94532;font-weight:700;margin-bottom:2px;">${role}</p>
              <span style="font-size:0.88rem;color:#64748B;">${tenure}</span>
            </div>
          </div>
          <div style="font-size:1.05rem;line-height:1.7;color:#334155;margin-bottom:24px;">
            <p>${bio}</p>
          </div>
          <blockquote style="background:#FAF7F2;border-left:5px solid #8DC73F;padding:18px 24px;border-radius:12px;font-style:italic;color:#12263A;font-size:1.1rem;line-height:1.5;">
            "${quote}"
          </blockquote>
        `;
        openModal(name, content);
      });
    });

    // Attach to Story cards
    document.querySelectorAll('.open-story-reader').forEach(card => {
      card.addEventListener('click', () => {
        const title = card.getAttribute('data-title');
        const subtitle = card.getAttribute('data-subtitle');
        const quote = card.getAttribute('data-quote');
        const fullHtml = card.getAttribute('data-story-html');
        const imgSrc = card.querySelector('img') ? card.querySelector('img').src : '';

        const content = `
          <div style="margin-bottom:20px;">
            <span class="badge badge-sage" style="margin-bottom:10px;">Roots & Routes: Immigrant Stories</span>
            <p style="font-size:1.1rem;color:#D94532;font-weight:700;">${subtitle}</p>
          </div>
          ${imgSrc ? `<div style="border-radius:20px;overflow:hidden;margin-bottom:24px;aspect-ratio:16/9;max-height:300px;"><img src="${imgSrc}" alt="${title}" style="width:100%;height:100%;object-fit:cover;"></div>` : ''}
          <blockquote style="background:#FAF7F2;border-left:5px solid #D94532;padding:18px 24px;border-radius:12px;font-style:italic;color:#12263A;font-size:1.15rem;line-height:1.5;margin-bottom:24px;">
            "${quote}"
          </blockquote>
          <div class="story-full-body" style="font-size:1.08rem;line-height:1.75;color:#334155;">
            ${fullHtml}
          </div>
        `;
        openModal(title, content);
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
  }

  // =========================================================================
  // 4. Captcha & Newsletter Verification
  // =========================================================================
  function initCaptcha() {
    const captchaBox = document.getElementById('human-captcha-box');
    const feedback = document.getElementById('newsletter-feedback-msg');
    const form = document.getElementById('newsletter-signup-form');
    let isHuman = !captchaBox;

    if (captchaBox) {
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
    }

    if (form) {
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        const emailInput = document.getElementById('newsletter-email') || document.getElementById('newsletter-email-input');
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
          feedback.textContent = 'Thank you for subscribing to Kandelia news! We are thrilled to stay connected.';
        }
        form.reset();
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
        mobileBtn.innerHTML = isOpen ? '<svg class="icon close" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg> Close' : 'Menu <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>';
      });

      // Close drawer on link click
      mobileDrawer.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
          mobileDrawer.classList.remove('open');
          mobileBtn.setAttribute('aria-expanded', 'false');
          mobileBtn.innerHTML = 'Menu <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>';
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
  // 6. Interactive Donation FAQ Accordion
  // =========================================================================
  function initFaqAccordion() {
    const faqItems = document.querySelectorAll('.faq-item');
    if (!faqItems.length) return;

    faqItems.forEach(item => {
      const questionBtn = item.querySelector('.faq-question');
      const answer = item.querySelector('.faq-answer');
      if (!questionBtn || !answer) return;

      questionBtn.addEventListener('click', () => {
        const isExpanded = questionBtn.getAttribute('aria-expanded') === 'true';

        // Close all other accordion items for clean accordion UX
        faqItems.forEach(otherItem => {
          if (otherItem !== item) {
            otherItem.classList.remove('active');
            const otherBtn = otherItem.querySelector('.faq-question');
            const otherAns = otherItem.querySelector('.faq-answer');
            if (otherBtn) otherBtn.setAttribute('aria-expanded', 'false');
            if (otherAns) otherAns.style.maxHeight = null;
          }
        });

        if (isExpanded) {
          questionBtn.setAttribute('aria-expanded', 'false');
          item.classList.remove('active');
          answer.style.maxHeight = null;
        } else {
          questionBtn.setAttribute('aria-expanded', 'true');
          item.classList.add('active');
          answer.style.maxHeight = answer.scrollHeight + 'px';
        }
      });
    });
  }

  // =========================================================================
  // Initialize Everything on DOMContentLoaded
  // =========================================================================
  document.addEventListener('DOMContentLoaded', () => {
    initNavigation();
    initCarousel(document.getElementById('testimonials-carousel'), 5500);
    initCarousel(document.getElementById('staff-board-carousel'), 6500);
    initModals();
    initCaptcha();
    initTabs();
    initFaqAccordion();
    console.log("Kandelia Redesign 2026 initialized successfully!");
  });

})();
