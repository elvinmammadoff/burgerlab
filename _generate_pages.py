#!/usr/bin/env python3
"""Generate 10 new inner pages for BurgerLab HTML template."""

import os, re

BASE_DIR = "/Users/elvinmammadoff/Documents/themeforest/burgerlab-html"
NOIMAGES_DIR = os.path.join(BASE_DIR, "burgerlab-noImages")

# ─── Read about.html to extract the structural chrome ───────────────────────
with open(os.path.join(BASE_DIR, "about.html"), encoding="utf-8") as f:
    about = f.read()

# Split on <main id="main"> and </main>
pre_main  = about[:about.index('<main id="main">') + len('<main id="main">')]
post_main = about[about.index('</main>') + len('</main>'):]

# ─── Helper ─────────────────────────────────────────────────────────────────
def make_page(title, meta_desc, main_html):
    head_new = pre_main.replace(
        "<title>About — BurgerLab Premium Burger &amp; Restaurant Template</title>",
        f"<title>{title} — BurgerLab Premium Burger &amp; Restaurant Template</title>"
    ).replace(
        'content="The BurgerLab story — how a SoHo kitchen turned the smash burger into a craft, engineered for flavor and grilled over fire."',
        f'content="{meta_desc}"'
    )
    return head_new + "\n" + main_html + "\n" + post_main


def make_noimages(html):
    """Replace local image src with placehold.co equivalents."""
    # hero background-image
    html = re.sub(
        r"background-image:\s*url\('assets/images/[^']+'\)",
        "background-image: url('https://placehold.co/1920x800')",
        html
    )
    # img src with assets/images
    def replace_img(m):
        attrs = m.group(0)
        w_match = re.search(r'width="(\d+)"', attrs)
        h_match = re.search(r'height="(\d+)"', attrs)
        w = w_match.group(1) if w_match else "800"
        h = h_match.group(1) if h_match else "600"
        attrs = re.sub(r'src="assets/images/[^"]+"',
                       f'src="https://placehold.co/{w}x{h}/1a1815/e5a52b?text=BurgerLab"', attrs)
        return attrs
    html = re.sub(r'<img[^>]+assets/images/[^>]+>', replace_img, html)
    return html


def write_pair(filename, title, meta_desc, main_html):
    page_html = make_page(title, meta_desc, main_html)
    path = os.path.join(BASE_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(page_html)
    print(f"  Created: {filename}")

    ni_html = make_noimages(page_html)
    ni_path = os.path.join(NOIMAGES_DIR, filename)
    with open(ni_path, "w", encoding="utf-8") as f:
        f.write(ni_html)
    print(f"  Created: burgerlab-noImages/{filename}")


# ════════════════════════════════════════════════════════════════════════════
# 1. event.html — Events & Private Dining listing
# ════════════════════════════════════════════════════════════════════════════
event_main = """
  <!-- ===== Page hero ===== -->
  <section class="bl-page-hero bl-page-hero--photo" style="background-image: url('assets/images/hero-reservation.jpg')">
    <div class="bl-container bl-container--narrow">
      <span class="bl-page-hero__eyebrow">Events</span>
      <h1 class="bl-page-hero__title">Events &amp; <em>Private Dining</em></h1>
      <p class="bl-page-hero__lede">From intimate birthday dinners to full corporate buyouts — we make every occasion unforgettable.</p>
      <nav class="bl-breadcrumb" aria-label="Breadcrumb">
        <a href="index.html">Home</a>
        <span class="bl-breadcrumb__sep">/</span>
        <span aria-current="page">Events</span>
      </nav>
    </div>
  </section>

  <!-- ===== Events grid ===== -->
  <section class="bl-section">
    <div class="bl-container bl-container--wide">
      <div class="bl-section-head bl-section-head--center">
        <span class="bl-eyebrow">What we offer</span>
        <h2 class="bl-section-title">Three ways to <em>celebrate</em></h2>
        <p class="bl-section-lede">Whether you're planning a date night or a full company dinner, we have a package built for you.</p>
      </div>
      <div class="bl-menu-grid" data-stagger>
        <!-- Card 1 -->
        <article class="bl-card" data-stagger-item>
          <div class="bl-card__media">
            <img src="assets/images/hero-reservation.jpg" alt="Private Dining setup at BurgerLab" loading="lazy" width="600" height="380">
          </div>
          <div class="bl-card__body">
            <div class="bl-card__meta">
              <span class="bl-chip">Private Dining</span>
              <span class="bl-chip">Up to 30 guests</span>
            </div>
            <h3 class="bl-card__title">Private Dining Room</h3>
            <p class="bl-card__text">Exclusive use of our underground dining room with a custom tasting menu, sommelier-curated drinks, and a dedicated events team from arrival to last course.</p>
            <a href="event-detail.html" class="bl-btn bl-btn--primary">Book this event
              <svg class="bl-btn__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
            </a>
          </div>
        </article>
        <!-- Card 2 -->
        <article class="bl-card" data-stagger-item>
          <div class="bl-card__media">
            <img src="assets/images/hero-poster.jpg" alt="Birthday celebration setup" loading="lazy" width="600" height="380">
          </div>
          <div class="bl-card__body">
            <div class="bl-card__meta">
              <span class="bl-chip">Birthday</span>
              <span class="bl-chip">Up to 15 guests</span>
            </div>
            <h3 class="bl-card__title">Birthday Celebration</h3>
            <p class="bl-card__text">Mark the day with a reserved corner booth, a personalised birthday cake from our pastry kitchen, and a complimentary round of craft cocktails for the group.</p>
            <a href="event-detail.html" class="bl-btn bl-btn--primary">Book this event
              <svg class="bl-btn__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
            </a>
          </div>
        </article>
        <!-- Card 3 -->
        <article class="bl-card" data-stagger-item>
          <div class="bl-card__media">
            <img src="assets/images/hero-services.jpg" alt="Corporate event at BurgerLab" loading="lazy" width="600" height="380">
          </div>
          <div class="bl-card__body">
            <div class="bl-card__meta">
              <span class="bl-chip">Corporate</span>
              <span class="bl-chip">Up to 80 guests</span>
            </div>
            <h3 class="bl-card__title">Corporate Events</h3>
            <p class="bl-card__text">Full-venue buyouts, team lunches, and product-launch dinners — complete with A/V setup, custom branding on menus, and coordinated service for large groups.</p>
            <a href="event-detail.html" class="bl-btn bl-btn--primary">Book this event
              <svg class="bl-btn__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
            </a>
          </div>
        </article>
      </div>
    </div>
  </section>

  <!-- ===== CTA ===== -->
  <section class="bl-section bl-cta">
    <div class="bl-container bl-container--narrow">
      <span class="bl-eyebrow" style="justify-content:center">Plan something special</span>
      <h2 class="bl-cta__title">Ready to <em>book your event?</em></h2>
      <p class="bl-cta__lede">Our events team is available Monday to Friday. Drop us an enquiry and we'll respond within 24 hours with a custom proposal.</p>
      <div class="bl-cta__actions">
        <a href="event-detail.html" class="bl-btn bl-btn--primary bl-btn--lg">Make an enquiry</a>
        <a href="contact.html" class="bl-btn bl-btn--ghost bl-btn--lg">Contact us</a>
      </div>
    </div>
  </section>
"""

write_pair("event.html", "Events &amp; Private Dining",
           "Host your next event at BurgerLab — private dining rooms, birthday celebrations, and full corporate buyouts with a bespoke menu.",
           event_main)


# ════════════════════════════════════════════════════════════════════════════
# 2. event-detail.html — Single event booking detail
# ════════════════════════════════════════════════════════════════════════════
event_detail_main = """
  <!-- ===== Page hero ===== -->
  <section class="bl-page-hero bl-page-hero--photo" style="background-image: url('assets/images/hero-reservation.jpg')">
    <div class="bl-container bl-container--narrow">
      <span class="bl-page-hero__eyebrow">Event Detail</span>
      <h1 class="bl-page-hero__title">Private <em>Dining Room</em></h1>
      <p class="bl-page-hero__lede">Exclusive underground dining for up to 30 guests — tailored menu, curated drinks, and a team dedicated entirely to you.</p>
      <nav class="bl-breadcrumb" aria-label="Breadcrumb">
        <a href="index.html">Home</a>
        <span class="bl-breadcrumb__sep">/</span>
        <a href="event.html">Events</a>
        <span class="bl-breadcrumb__sep">/</span>
        <span aria-current="page">Private Dining Room</span>
      </nav>
    </div>
  </section>

  <!-- ===== Event split ===== -->
  <section class="bl-section">
    <div class="bl-container bl-container--wide">
      <div class="bl-split__grid">
        <div class="bl-split__media bl-reveal-up">
          <img src="assets/images/ingredients-detail.jpg" alt="Private dining room at BurgerLab" loading="lazy" width="700" height="500">
        </div>
        <div class="bl-reveal-up">
          <span class="bl-eyebrow">About this event</span>
          <h2 class="bl-section-title">An evening built <em>entirely around you</em></h2>
          <p class="bl-section-lede">Our private dining room seats up to 30 guests in a fully exclusive setting below the main floor. Your group gets a dedicated server team, a bespoke multi-course menu, and a sommelier to handle pairings from start to finish.</p>
          <p class="bl-section-lede">We accommodate dietary requirements, allergy-aware menus, and custom plating. Every element, from table arrangement to music, can be tailored to your brief.</p>
          <ul class="bl-checklist">
            <li>✔ Exclusive room hire — no shared spaces</li>
            <li>✔ Custom tasting menu (4 or 6 courses)</li>
            <li>✔ Sommelier-curated wine &amp; cocktail pairings</li>
            <li>✔ Dedicated service team (1:5 ratio)</li>
            <li>✔ Floral &amp; décor styling on request</li>
            <li>✔ AV screen &amp; microphone available</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- ===== Booking form ===== -->
  <section class="bl-section bl-section--bg2">
    <div class="bl-container bl-container--narrow">
      <div class="bl-section-head bl-section-head--center">
        <span class="bl-eyebrow">Book this event</span>
        <h2 class="bl-section-title">Send us your <em>enquiry</em></h2>
        <p class="bl-section-lede">Fill in the details below and our events team will come back to you within 24 hours.</p>
      </div>
      <div class="bl-form-card bl-reveal-up">
        <form action="https://api.web3forms.com/submit" method="POST" data-form data-success="Enquiry sent — we'll be in touch within 24 hours.">
          <input type="hidden" name="access_key" value="1689852d-c68d-46fa-977e-51c4bc04d29a">
          <input type="hidden" name="subject" value="New BurgerLab event booking enquiry">
          <input type="hidden" name="from_name" value="BurgerLab Website">
          <input type="checkbox" name="botcheck" class="bl-honeypot" tabindex="-1" aria-hidden="true">
          <div class="bl-form-grid">
            <div class="bl-field">
              <label for="ev-first">First name</label>
              <input class="bl-input" type="text" id="ev-first" name="first_name" autocomplete="given-name" required>
            </div>
            <div class="bl-field">
              <label for="ev-last">Last name</label>
              <input class="bl-input" type="text" id="ev-last" name="last_name" autocomplete="family-name" required>
            </div>
            <div class="bl-field">
              <label for="ev-email">Email</label>
              <input class="bl-input" type="email" id="ev-email" name="email" autocomplete="email" required>
            </div>
            <div class="bl-field">
              <label for="ev-phone">Phone</label>
              <input class="bl-input" type="tel" id="ev-phone" name="phone" autocomplete="tel" required>
            </div>
            <div class="bl-field">
              <label for="ev-date">Event date</label>
              <div class="bl-picker" data-datepicker>
                <input class="bl-input" type="text" id="ev-date" name="date" placeholder="Select a date" required>
                <span class="bl-picker__icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4.5" width="18" height="16" rx="2.5"/><path d="M3 9h18M8 2.5v4M16 2.5v4"/></svg></span>
              </div>
            </div>
            <div class="bl-field">
              <label for="ev-guests">Number of guests</label>
              <select class="bl-select" id="ev-guests" name="guests">
                <option>Up to 10 guests</option>
                <option>11 – 20 guests</option>
                <option>21 – 30 guests</option>
                <option>31 – 50 guests</option>
                <option>50+ guests</option>
              </select>
            </div>
            <div class="bl-field">
              <label for="ev-type">Event type</label>
              <select class="bl-select" id="ev-type" name="event_type">
                <option>Private Dining</option>
                <option>Birthday Celebration</option>
                <option>Corporate Dinner</option>
                <option>Team Lunch</option>
                <option>Other</option>
              </select>
            </div>
            <div class="bl-field">
              <label for="ev-budget">Approximate budget</label>
              <select class="bl-select" id="ev-budget" name="budget">
                <option>Under $1,000</option>
                <option>$1,000 – $3,000</option>
                <option>$3,000 – $7,000</option>
                <option>$7,000+</option>
              </select>
            </div>
            <div class="bl-field bl-field--full">
              <label for="ev-notes">Special requests or dietary requirements</label>
              <textarea class="bl-textarea" id="ev-notes" name="notes" placeholder="Allergies, themes, décor requests, AV requirements…"></textarea>
            </div>
          </div>
          <button type="submit" class="bl-btn bl-btn--primary bl-btn--lg">Send enquiry</button>
          <p class="bl-form__note" role="status" aria-live="polite"></p>
        </form>
      </div>
    </div>
  </section>
"""

write_pair("event-detail.html", "Private Dining Event Detail",
           "Book BurgerLab's exclusive private dining room for up to 30 guests — custom tasting menu, sommelier pairings, dedicated service team.",
           event_detail_main)


# ════════════════════════════════════════════════════════════════════════════
# 3. pricing.html — Pricing & packages
# ════════════════════════════════════════════════════════════════════════════
pricing_main = """
  <!-- ===== Page hero ===== -->
  <section class="bl-page-hero bl-page-hero--photo" style="background-image: url('assets/images/hero-services.jpg')">
    <div class="bl-container bl-container--narrow">
      <span class="bl-page-hero__eyebrow">Pricing</span>
      <h1 class="bl-page-hero__title">Private Dining <em>Packages</em></h1>
      <p class="bl-page-hero__lede">Three tiers to fit any occasion — from a relaxed dinner for two to a full-venue buyout for a hundred.</p>
      <nav class="bl-breadcrumb" aria-label="Breadcrumb">
        <a href="index.html">Home</a>
        <span class="bl-breadcrumb__sep">/</span>
        <span aria-current="page">Pricing</span>
      </nav>
    </div>
  </section>

  <!-- ===== Pricing cards ===== -->
  <section class="bl-section">
    <div class="bl-container bl-container--wide">
      <div class="bl-section-head bl-section-head--center">
        <span class="bl-eyebrow">Our packages</span>
        <h2 class="bl-section-title">Choose your <em>experience</em></h2>
        <p class="bl-section-lede">All packages include dedicated staff, custom menus, and our kitchen's full attention from first course to dessert.</p>
      </div>
      <div class="bl-pricing-grid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:2rem;margin-top:2.5rem" data-stagger>

        <!-- Essential -->
        <div class="bl-card" style="padding:2.5rem 2rem;display:flex;flex-direction:column;gap:1.25rem" data-stagger-item>
          <div>
            <span class="bl-chip">Essential</span>
            <div style="margin-top:1rem;font-size:2.75rem;font-weight:700;color:var(--bl-text)">$65 <span style="font-size:1rem;font-weight:400;color:var(--bl-muted)">/person</span></div>
            <p style="margin-top:.5rem;color:var(--bl-muted);font-size:.9375rem">Perfect for small groups up to 12. Ideal for birthday dinners and date nights.</p>
          </div>
          <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:.75rem;flex:1">
            <li style="display:flex;gap:.625rem;align-items:flex-start"><span style="color:var(--bl-accent)">✔</span> 3-course set menu</li>
            <li style="display:flex;gap:.625rem;align-items:flex-start"><span style="color:var(--bl-accent)">✔</span> Welcome drinks on arrival</li>
            <li style="display:flex;gap:.625rem;align-items:flex-start"><span style="color:var(--bl-accent)">✔</span> Dedicated server</li>
            <li style="display:flex;gap:.625rem;align-items:flex-start"><span style="color:var(--bl-accent)">✔</span> Complimentary table décor</li>
            <li style="display:flex;gap:.625rem;align-items:flex-start;color:var(--bl-muted)"><span>—</span> Sommelier consultation</li>
            <li style="display:flex;gap:.625rem;align-items:flex-start;color:var(--bl-muted)"><span>—</span> AV &amp; presentation setup</li>
            <li style="display:flex;gap:.625rem;align-items:flex-start;color:var(--bl-muted)"><span>—</span> Custom branded menus</li>
          </ul>
          <a href="event-detail.html" class="bl-btn bl-btn--ghost" style="margin-top:auto">Book Essential</a>
        </div>

        <!-- Premium -->
        <div class="bl-card" style="padding:2.5rem 2rem;display:flex;flex-direction:column;gap:1.25rem;border-color:var(--bl-accent);position:relative" data-stagger-item>
          <div style="position:absolute;top:-1rem;left:50%;transform:translateX(-50%);background:var(--bl-accent);color:#1a1815;font-size:.75rem;font-weight:700;padding:.25rem .9rem;border-radius:999px;white-space:nowrap;letter-spacing:.06em">MOST POPULAR</div>
          <div>
            <span class="bl-chip" style="background:var(--bl-accent);color:#1a1815">Premium</span>
            <div style="margin-top:1rem;font-size:2.75rem;font-weight:700;color:var(--bl-text)">$110 <span style="font-size:1rem;font-weight:400;color:var(--bl-muted)">/person</span></div>
            <p style="margin-top:.5rem;color:var(--bl-muted);font-size:.9375rem">Great for groups of 13–30. Weddings, milestones, and corporate dinners.</p>
          </div>
          <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:.75rem;flex:1">
            <li style="display:flex;gap:.625rem;align-items:flex-start"><span style="color:var(--bl-accent)">✔</span> 5-course tasting menu</li>
            <li style="display:flex;gap:.625rem;align-items:flex-start"><span style="color:var(--bl-accent)">✔</span> Welcome champagne</li>
            <li style="display:flex;gap:.625rem;align-items:flex-start"><span style="color:var(--bl-accent)">✔</span> Dedicated server team (1:5)</li>
            <li style="display:flex;gap:.625rem;align-items:flex-start"><span style="color:var(--bl-accent)">✔</span> Premium floral centrepieces</li>
            <li style="display:flex;gap:.625rem;align-items:flex-start"><span style="color:var(--bl-accent)">✔</span> Sommelier consultation</li>
            <li style="display:flex;gap:.625rem;align-items:flex-start"><span style="color:var(--bl-accent)">✔</span> AV &amp; presentation setup</li>
            <li style="display:flex;gap:.625rem;align-items:flex-start;color:var(--bl-muted)"><span>—</span> Custom branded menus</li>
          </ul>
          <a href="event-detail.html" class="bl-btn bl-btn--primary" style="margin-top:auto">Book Premium</a>
        </div>

        <!-- Exclusive -->
        <div class="bl-card" style="padding:2.5rem 2rem;display:flex;flex-direction:column;gap:1.25rem" data-stagger-item>
          <div>
            <span class="bl-chip">Exclusive</span>
            <div style="margin-top:1rem;font-size:2.75rem;font-weight:700;color:var(--bl-text)">$185 <span style="font-size:1rem;font-weight:400;color:var(--bl-muted)">/person</span></div>
            <p style="margin-top:.5rem;color:var(--bl-muted);font-size:.9375rem">Full venue buyout for 30–100 guests. The complete BurgerLab experience, exclusively yours.</p>
          </div>
          <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:.75rem;flex:1">
            <li style="display:flex;gap:.625rem;align-items:flex-start"><span style="color:var(--bl-accent)">✔</span> Bespoke 7-course menu</li>
            <li style="display:flex;gap:.625rem;align-items:flex-start"><span style="color:var(--bl-accent)">✔</span> Open bar (4 hours)</li>
            <li style="display:flex;gap:.625rem;align-items:flex-start"><span style="color:var(--bl-accent)">✔</span> Dedicated events manager</li>
            <li style="display:flex;gap:.625rem;align-items:flex-start"><span style="color:var(--bl-accent)">✔</span> Full venue styling &amp; décor</li>
            <li style="display:flex;gap:.625rem;align-items:flex-start"><span style="color:var(--bl-accent)">✔</span> Private sommelier</li>
            <li style="display:flex;gap:.625rem;align-items:flex-start"><span style="color:var(--bl-accent)">✔</span> Full AV &amp; production rig</li>
            <li style="display:flex;gap:.625rem;align-items:flex-start"><span style="color:var(--bl-accent)">✔</span> Custom branded menus &amp; signage</li>
          </ul>
          <a href="event-detail.html" class="bl-btn bl-btn--ghost" style="margin-top:auto">Book Exclusive</a>
        </div>

      </div>
    </div>
  </section>

  <!-- ===== FAQ accordion ===== -->
  <section class="bl-section bl-section--bg2">
    <div class="bl-container bl-container--narrow">
      <div class="bl-section-head bl-section-head--center">
        <span class="bl-eyebrow">Questions answered</span>
        <h2 class="bl-section-title">Package <em>FAQs</em></h2>
      </div>
      <div class="bl-faq" data-stagger>
        <details class="bl-faq__item" data-stagger-item open>
          <summary>Is there a minimum spend?</summary>
          <div class="bl-faq__a"><p>The Essential package has a minimum of 6 guests. Premium requires at least 13 guests. Exclusive applies for groups of 30 or more. Minimum spends vary by day — contact our events team for a tailored quote.</p></div>
        </details>
        <details class="bl-faq__item" data-stagger-item>
          <summary>Can I customise the menu?</summary>
          <div class="bl-faq__a"><p>All packages include menu consultation. We can work around dietary requirements, allergies, and cuisine preferences. The tasting menu structure is flexible — just let us know at the time of booking.</p></div>
        </details>
        <details class="bl-faq__item" data-stagger-item>
          <summary>What is the deposit to secure a booking?</summary>
          <div class="bl-faq__a"><p>We ask for a 25% non-refundable deposit to confirm your booking. The remaining balance is due 7 days before your event. Cancellations within 48 hours are charged at 50% of the total value.</p></div>
        </details>
        <details class="bl-faq__item" data-stagger-item>
          <summary>Can I bring my own cake or decorations?</summary>
          <div class="bl-faq__a"><p>You're welcome to bring a celebration cake — we'll store and plate it at no extra charge. External decorations are permitted provided they don't require drilling or permanent fixtures. We do not allow confetti or glitter.</p></div>
        </details>
        <details class="bl-faq__item" data-stagger-item>
          <summary>How far in advance should I book?</summary>
          <div class="bl-faq__a"><p>We recommend booking at least 4 weeks in advance for weekend dates, especially during the holiday season. Last-minute bookings may be possible mid-week — enquire directly and we'll do our best to accommodate you.</p></div>
        </details>
      </div>
    </div>
  </section>

  <!-- ===== CTA ===== -->
  <section class="bl-section bl-cta">
    <div class="bl-container bl-container--narrow">
      <span class="bl-eyebrow" style="justify-content:center">Let's talk</span>
      <h2 class="bl-cta__title">Not sure which <em>package fits?</em></h2>
      <p class="bl-cta__lede">Our events team will help you find the right package for your group size, occasion, and budget — no obligation.</p>
      <div class="bl-cta__actions">
        <a href="event-detail.html" class="bl-btn bl-btn--primary bl-btn--lg">Make an enquiry</a>
        <a href="contact.html" class="bl-btn bl-btn--ghost bl-btn--lg">Get in touch</a>
      </div>
    </div>
  </section>
"""

write_pair("pricing.html", "Pricing &amp; Packages",
           "BurgerLab private dining pricing — Essential from $65/person, Premium from $110, and Exclusive full-venue buyout from $185. Bespoke menus included.",
           pricing_main)


# ════════════════════════════════════════════════════════════════════════════
# 4. careers.html — Job openings
# ════════════════════════════════════════════════════════════════════════════
careers_main = """
  <!-- ===== Page hero ===== -->
  <section class="bl-page-hero bl-page-hero--photo" style="background-image: url('assets/images/hero-chef.jpg')">
    <div class="bl-container bl-container--narrow">
      <span class="bl-page-hero__eyebrow">Careers</span>
      <h1 class="bl-page-hero__title">Join the <em>Lab Crew</em></h1>
      <p class="bl-page-hero__lede">We're always looking for talented people who care about great food and even better hospitality.</p>
      <nav class="bl-breadcrumb" aria-label="Breadcrumb">
        <a href="index.html">Home</a>
        <span class="bl-breadcrumb__sep">/</span>
        <span aria-current="page">Careers</span>
      </nav>
    </div>
  </section>

  <!-- ===== Why join us ===== -->
  <section class="bl-section">
    <div class="bl-container bl-container--wide">
      <div class="bl-section-head bl-section-head--center">
        <span class="bl-eyebrow">Why BurgerLab</span>
        <h2 class="bl-section-title">More than a job — <em>a craft</em></h2>
        <p class="bl-section-lede">We invest in our people the same way we invest in our food — with intention, quality, and a genuine obsession with getting it right.</p>
      </div>
      <div class="bl-ing-grid" data-stagger>
        <div class="bl-ing-card" data-stagger-item>
          <span class="bl-ing-card__no">01</span>
          <h3 class="bl-ing-card__name">Real progression</h3>
          <p class="bl-ing-card__text">70% of our senior team started on the floor. We promote from within, run structured training, and fund external courses for high performers.</p>
        </div>
        <div class="bl-ing-card" data-stagger-item>
          <span class="bl-ing-card__no">02</span>
          <h3 class="bl-ing-card__name">Competitive pay</h3>
          <p class="bl-ing-card__text">Above-market base salaries, service charge, and a profit-share scheme for full-time staff. We review compensation twice a year.</p>
        </div>
        <div class="bl-ing-card" data-stagger-item>
          <span class="bl-ing-card__no">03</span>
          <h3 class="bl-ing-card__name">Team culture</h3>
          <p class="bl-ing-card__text">Monthly team meals, weekly family dinners before service, and an open-door policy. If you've got an idea, we want to hear it.</p>
        </div>
      </div>
      <div style="display:flex;gap:.75rem;flex-wrap:wrap;justify-content:center;margin-top:2rem">
        <span class="bl-chip">Health insurance</span>
        <span class="bl-chip">Pension contribution</span>
        <span class="bl-chip">Free staff meals</span>
        <span class="bl-chip">Flexible hours</span>
        <span class="bl-chip">Training budget</span>
        <span class="bl-chip">Staff discounts</span>
      </div>
    </div>
  </section>

  <!-- ===== Open roles ===== -->
  <section class="bl-section bl-section--bg2">
    <div class="bl-container bl-container--wide">
      <div class="bl-section-head">
        <span class="bl-eyebrow">Open positions</span>
        <h2 class="bl-section-title">Current <em>openings</em></h2>
      </div>
      <div class="bl-faq" data-stagger>
        <details class="bl-faq__item" data-stagger-item open>
          <summary>Head Chef — SoHo Flagship <span class="bl-chip" style="margin-left:.75rem;font-size:.75rem">Full-time</span></summary>
          <div class="bl-faq__a">
            <p>We're looking for an experienced Head Chef to lead the kitchen at our SoHo flagship. You'll oversee a team of 12, develop seasonal specials, and maintain the quality standards our guests expect.</p>
            <p><strong>Requirements:</strong> 5+ years kitchen leadership, formal culinary training, knowledge of allergen legislation. Strong communication and team-building skills essential.</p>
            <p><strong>Salary:</strong> $90,000 – $110,000 depending on experience.</p>
            <a href="contact.html" class="bl-btn bl-btn--primary" style="margin-top:1rem">Apply now</a>
          </div>
        </details>
        <details class="bl-faq__item" data-stagger-item>
          <summary>Senior Server — Midtown <span class="bl-chip" style="margin-left:.75rem;font-size:.75rem">Full-time</span></summary>
          <div class="bl-faq__a">
            <p>We need an experienced front-of-house professional to join our Midtown team. You'll run sections of up to 6 tables, handle events service, and mentor junior staff during peak service.</p>
            <p><strong>Requirements:</strong> 3+ years table service, wine knowledge, excellent guest manner.</p>
            <p><strong>Salary:</strong> $50,000 + service charge (average total $65,000+).</p>
            <a href="contact.html" class="bl-btn bl-btn--primary" style="margin-top:1rem">Apply now</a>
          </div>
        </details>
        <details class="bl-faq__item" data-stagger-item>
          <summary>Delivery Driver — Multiple Locations <span class="bl-chip" style="margin-left:.75rem;font-size:.75rem">Part-time</span></summary>
          <div class="bl-faq__a">
            <p>Looking for reliable drivers to join our fleet across Manhattan. Flexible shifts, competitive hourly pay, and mileage covered. Clean driving licence required.</p>
            <p><strong>Requirements:</strong> Valid driving licence, smartphone for dispatch app, professional attitude.</p>
            <p><strong>Pay:</strong> $22/hr + tips.</p>
            <a href="contact.html" class="bl-btn bl-btn--primary" style="margin-top:1rem">Apply now</a>
          </div>
        </details>
        <details class="bl-faq__item" data-stagger-item>
          <summary>Marketing &amp; Social Lead <span class="bl-chip" style="margin-left:.75rem;font-size:.75rem">Full-time</span></summary>
          <div class="bl-faq__a">
            <p>Join our small but fast-moving marketing team to own BurgerLab's social presence, content calendar, and campaign execution. You'll work closely with our photographer, designer, and ops leads.</p>
            <p><strong>Requirements:</strong> 3+ years social/content marketing, food &amp; hospitality experience preferred, strong visual instincts, data-literate.</p>
            <p><strong>Salary:</strong> $55,000 – $70,000.</p>
            <a href="contact.html" class="bl-btn bl-btn--primary" style="margin-top:1rem">Apply now</a>
          </div>
        </details>
        <details class="bl-faq__item" data-stagger-item>
          <summary>Kitchen Porter — All Locations <span class="bl-chip" style="margin-left:.75rem;font-size:.75rem">Full-time / Part-time</span></summary>
          <div class="bl-faq__a">
            <p>The backbone of every great kitchen. We're looking for reliable porters to keep our high-volume kitchens clean, organised, and compliant. Flexible shift patterns available across all nine locations.</p>
            <p><strong>Requirements:</strong> No experience necessary — full training provided. Positive attitude and ability to work at pace.</p>
            <p><strong>Pay:</strong> $20/hr.</p>
            <a href="contact.html" class="bl-btn bl-btn--primary" style="margin-top:1rem">Apply now</a>
          </div>
        </details>
      </div>
    </div>
  </section>

  <!-- ===== CTA ===== -->
  <section class="bl-section bl-cta">
    <div class="bl-container bl-container--narrow">
      <span class="bl-eyebrow" style="justify-content:center">Don't see your role?</span>
      <h2 class="bl-cta__title">Send us a <em>speculative application</em></h2>
      <p class="bl-cta__lede">We're always interested in great people. Drop us your CV and a short note — we keep them on file and reach out when something fits.</p>
      <div class="bl-cta__actions">
        <a href="contact.html" class="bl-btn bl-btn--primary bl-btn--lg">Get in touch</a>
        <a href="about.html" class="bl-btn bl-btn--ghost bl-btn--lg">Learn about us</a>
      </div>
    </div>
  </section>
"""

write_pair("careers.html", "Careers — Join the Lab Crew",
           "Work at BurgerLab — we're hiring chefs, servers, drivers, and marketing specialists. Competitive pay, real progression, and free staff meals.",
           careers_main)


# ════════════════════════════════════════════════════════════════════════════
# 5. testimonials.html — Customer reviews
# ════════════════════════════════════════════════════════════════════════════
testimonials_main = """
  <!-- ===== Page hero ===== -->
  <section class="bl-page-hero bl-page-hero--photo" style="background-image: url('assets/images/hero-about.jpg')">
    <div class="bl-container bl-container--narrow">
      <span class="bl-page-hero__eyebrow">Testimonials</span>
      <h1 class="bl-page-hero__title">What our <em>guests say</em></h1>
      <p class="bl-page-hero__lede">Over 2,400 five-star reviews and counting. Here's what keeps people coming back.</p>
      <nav class="bl-breadcrumb" aria-label="Breadcrumb">
        <a href="index.html">Home</a>
        <span class="bl-breadcrumb__sep">/</span>
        <span aria-current="page">Testimonials</span>
      </nav>
    </div>
  </section>

  <!-- ===== Stats bar ===== -->
  <section class="bl-section bl-section--bg2 bl-section--tight">
    <div class="bl-container bl-container--wide">
      <h2 class="bl-visually-hidden">Review summary</h2>
      <div class="bl-stats" data-stagger>
        <div data-stagger-item><div class="bl-stat__num">4.9</div><div class="bl-stat__label">Average rating</div></div>
        <div data-stagger-item><div class="bl-stat__num" data-count="2400" data-suffix="+">2,400+</div><div class="bl-stat__label">Total reviews</div></div>
        <div data-stagger-item><div class="bl-stat__num">98<span style="font-size:1.5rem">%</span></div><div class="bl-stat__label">Would recommend</div></div>
        <div data-stagger-item><div class="bl-stat__num">★★★★★</div><div class="bl-stat__label">Google &amp; Yelp</div></div>
      </div>
    </div>
  </section>

  <!-- ===== Reviews grid ===== -->
  <section class="bl-section">
    <div class="bl-container bl-container--wide">
      <div class="bl-section-head bl-section-head--center">
        <span class="bl-eyebrow">Guest reviews</span>
        <h2 class="bl-section-title">Straight from <em>our guests</em></h2>
      </div>
      <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:1.5rem;margin-top:2.5rem" data-stagger>

        <div class="bl-card" style="padding:1.75rem" data-stagger-item>
          <div style="color:var(--bl-accent);font-size:1.125rem;letter-spacing:.1em">★★★★★</div>
          <blockquote style="margin:.75rem 0 1.25rem;color:var(--bl-text);line-height:1.65">"Best smash burger I've had in New York, and I've tried them all. The brioche bun stays together until the last bite — a miracle."</blockquote>
          <footer style="font-size:.875rem"><strong>Marcus T.</strong> <span style="color:var(--bl-muted);margin-left:.5rem">SoHo regular</span></footer>
        </div>

        <div class="bl-card" style="padding:1.75rem" data-stagger-item>
          <div style="color:var(--bl-accent);font-size:1.125rem;letter-spacing:.1em">★★★★★</div>
          <blockquote style="margin:.75rem 0 1.25rem;color:var(--bl-text);line-height:1.65">"Booked the private dining room for my 30th and the team went above and beyond. Every detail was exactly as we'd discussed, and the food was exceptional."</blockquote>
          <footer style="font-size:.875rem"><strong>Priya N.</strong> <span style="color:var(--bl-muted);margin-left:.5rem">Birthday dinner</span></footer>
        </div>

        <div class="bl-card" style="padding:1.75rem" data-stagger-item>
          <div style="color:var(--bl-accent);font-size:1.125rem;letter-spacing:.1em">★★★★★</div>
          <blockquote style="margin:.75rem 0 1.25rem;color:var(--bl-text);line-height:1.65">"Ordered delivery for the third time this week. The double smash arrives hot and perfectly wrapped every single time. Fastest 30 minutes of my week."</blockquote>
          <footer style="font-size:.875rem"><strong>Jordan K.</strong> <span style="color:var(--bl-muted);margin-left:.5rem">Delivery customer</span></footer>
        </div>

        <div class="bl-card" style="padding:1.75rem" data-stagger-item>
          <div style="color:var(--bl-accent);font-size:1.125rem;letter-spacing:.1em">★★★★★</div>
          <blockquote style="margin:.75rem 0 1.25rem;color:var(--bl-text);line-height:1.65">"The loaded fries are genuinely the best I've ever had. My partner laughed when I said I'd drive across town just for those, but here we are — again."</blockquote>
          <footer style="font-size:.875rem"><strong>Samira O.</strong> <span style="color:var(--bl-muted);margin-left:.5rem">Repeat diner</span></footer>
        </div>

        <div class="bl-card" style="padding:1.75rem" data-stagger-item>
          <div style="color:var(--bl-accent);font-size:1.125rem;letter-spacing:.1em">★★★★★</div>
          <blockquote style="margin:.75rem 0 1.25rem;color:var(--bl-text);line-height:1.65">"Hosted our company Christmas dinner here. Service was smooth, the food came out perfectly timed for 45 people, and the whole team raved about it for days."</blockquote>
          <footer style="font-size:.875rem"><strong>David R.</strong> <span style="color:var(--bl-muted);margin-left:.5rem">Corporate event</span></footer>
        </div>

        <div class="bl-card" style="padding:1.75rem" data-stagger-item>
          <div style="color:var(--bl-accent);font-size:1.125rem;letter-spacing:.1em">★★★★★</div>
          <blockquote style="margin:.75rem 0 1.25rem;color:var(--bl-text);line-height:1.65">"Took my mum here on a whim and she's now asked to go back four times. Not bad for a place I thought might just be a trendy burger joint."</blockquote>
          <footer style="font-size:.875rem"><strong>Chris M.</strong> <span style="color:var(--bl-muted);margin-left:.5rem">Family dinner</span></footer>
        </div>

        <div class="bl-card" style="padding:1.75rem" data-stagger-item>
          <div style="color:var(--bl-accent);font-size:1.125rem;letter-spacing:.1em">★★★★★</div>
          <blockquote style="margin:.75rem 0 1.25rem;color:var(--bl-text);line-height:1.65">"The plant-based Lab Burger is indistinguishable from the real thing — I'm not even vegetarian and I order it half the time now. Impressive."</blockquote>
          <footer style="font-size:.875rem"><strong>Aisha F.</strong> <span style="color:var(--bl-muted);margin-left:.5rem">Plant-based fan</span></footer>
        </div>

        <div class="bl-card" style="padding:1.75rem" data-stagger-item>
          <div style="color:var(--bl-accent);font-size:1.125rem;letter-spacing:.1em">★★★★★</div>
          <blockquote style="margin:.75rem 0 1.25rem;color:var(--bl-text);line-height:1.65">"Staff remembered my usual order on my third visit. In this city, that level of personal touch is rare. BurgerLab genuinely feels like a neighbourhood spot, not a chain."</blockquote>
          <footer style="font-size:.875rem"><strong>Tom B.</strong> <span style="color:var(--bl-muted);margin-left:.5rem">Loyal customer</span></footer>
        </div>

        <div class="bl-card" style="padding:1.75rem" data-stagger-item>
          <div style="color:var(--bl-accent);font-size:1.125rem;letter-spacing:.1em">★★★★★</div>
          <blockquote style="margin:.75rem 0 1.25rem;color:var(--bl-text);line-height:1.65">"The craft cola is the sleeper hit of the menu. Most places treat the drinks as an afterthought — BurgerLab clearly doesn't. Everything here is deliberate."</blockquote>
          <footer style="font-size:.875rem"><strong>Lena G.</strong> <span style="color:var(--bl-muted);margin-left:.5rem">First-time visitor</span></footer>
        </div>

      </div>
    </div>
  </section>

  <!-- ===== CTA ===== -->
  <section class="bl-section bl-cta">
    <div class="bl-container bl-container--narrow">
      <span class="bl-eyebrow" style="justify-content:center">Your turn</span>
      <h2 class="bl-cta__title">Come taste what <em>everyone's talking about</em></h2>
      <p class="bl-cta__lede">Order online or book a table at the SoHo flagship. We think you'll have something nice to say too.</p>
      <div class="bl-cta__actions">
        <a href="reservation.html" class="bl-btn bl-btn--primary bl-btn--lg">Order now</a>
        <a href="menu.html" class="bl-btn bl-btn--ghost bl-btn--lg">See the menu</a>
      </div>
    </div>
  </section>
"""

write_pair("testimonials.html", "Testimonials — What Our Guests Say",
           "Read 2,400+ five-star reviews of BurgerLab. Our guests love the smash burgers, private dining, and 30-minute delivery — rated 4.9 on Google.",
           testimonials_main)


# ════════════════════════════════════════════════════════════════════════════
# 6. order-tracking.html — Order tracking status
# ════════════════════════════════════════════════════════════════════════════
order_tracking_main = """
  <!-- ===== Page hero ===== -->
  <section class="bl-page-hero bl-page-hero--photo" style="background-image: url('assets/images/hero-burger.jpg')">
    <div class="bl-container bl-container--narrow">
      <span class="bl-page-hero__eyebrow">Track your order</span>
      <h1 class="bl-page-hero__title">Where's my <em>order?</em></h1>
      <p class="bl-page-hero__lede">Enter your order number and email address to see real-time status updates from kitchen to door.</p>
      <nav class="bl-breadcrumb" aria-label="Breadcrumb">
        <a href="index.html">Home</a>
        <span class="bl-breadcrumb__sep">/</span>
        <span aria-current="page">Order Tracking</span>
      </nav>
    </div>
  </section>

  <!-- ===== Tracking form ===== -->
  <section class="bl-section">
    <div class="bl-container bl-container--narrow">
      <div class="bl-form-card bl-reveal-up">
        <div class="bl-section-head" style="margin-bottom:2rem">
          <span class="bl-eyebrow">Look up your order</span>
          <h2 class="bl-section-title" style="font-size:1.75rem">Enter your <em>order details</em></h2>
        </div>
        <form data-form data-success="Tracking info found — see your status below.">
          <div class="bl-form-grid">
            <div class="bl-field">
              <label for="ot-order">Order number</label>
              <input class="bl-input" type="text" id="ot-order" name="order_number" placeholder="e.g. BL-20240622-4827" required>
            </div>
            <div class="bl-field">
              <label for="ot-email">Email address</label>
              <input class="bl-input" type="email" id="ot-email" name="email" autocomplete="email" placeholder="The email used when ordering" required>
            </div>
          </div>
          <button type="submit" class="bl-btn bl-btn--primary bl-btn--lg">Track my order</button>
          <p class="bl-form__note" role="status" aria-live="polite"></p>
        </form>
      </div>
    </div>
  </section>

  <!-- ===== Status timeline ===== -->
  <section class="bl-section bl-section--bg2">
    <div class="bl-container bl-container--narrow">
      <div class="bl-section-head bl-section-head--center">
        <span class="bl-eyebrow">Example order</span>
        <h2 class="bl-section-title">Order <em>#BL-20240622-4827</em></h2>
        <p class="bl-section-lede">The Lab Double Smash × 1 &nbsp;·&nbsp; Loaded Fries × 2 &nbsp;·&nbsp; Craft Cola × 2</p>
      </div>
      <div style="max-width:520px;margin:2.5rem auto 0;display:flex;flex-direction:column;gap:0">

        <!-- Step 1 — complete -->
        <div style="display:flex;gap:1.5rem;align-items:flex-start">
          <div style="display:flex;flex-direction:column;align-items:center;gap:0">
            <div style="width:2.5rem;height:2.5rem;border-radius:50%;background:var(--bl-accent);display:flex;align-items:center;justify-content:center;flex-shrink:0">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1a1815" stroke-width="2.5"><path d="M5 12l5 5L20 7"/></svg>
            </div>
            <div style="width:2px;background:var(--bl-accent);flex:1;min-height:3rem"></div>
          </div>
          <div style="padding-bottom:2.5rem">
            <div style="font-weight:600;color:var(--bl-text)">Order Placed</div>
            <div style="font-size:.875rem;color:var(--bl-muted);margin-top:.25rem">Today at 7:14 pm — Payment confirmed.</div>
          </div>
        </div>

        <!-- Step 2 — complete -->
        <div style="display:flex;gap:1.5rem;align-items:flex-start">
          <div style="display:flex;flex-direction:column;align-items:center;gap:0">
            <div style="width:2.5rem;height:2.5rem;border-radius:50%;background:var(--bl-accent);display:flex;align-items:center;justify-content:center;flex-shrink:0">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1a1815" stroke-width="2.5"><path d="M5 12l5 5L20 7"/></svg>
            </div>
            <div style="width:2px;background:var(--bl-accent);flex:1;min-height:3rem"></div>
          </div>
          <div style="padding-bottom:2.5rem">
            <div style="font-weight:600;color:var(--bl-text)">Preparing Your Order</div>
            <div style="font-size:.875rem;color:var(--bl-muted);margin-top:.25rem">Today at 7:19 pm — Our kitchen is on it.</div>
          </div>
        </div>

        <!-- Step 3 — active -->
        <div style="display:flex;gap:1.5rem;align-items:flex-start">
          <div style="display:flex;flex-direction:column;align-items:center;gap:0">
            <div style="width:2.5rem;height:2.5rem;border-radius:50%;background:var(--bl-accent);display:flex;align-items:center;justify-content:center;flex-shrink:0;box-shadow:0 0 0 6px color-mix(in srgb,var(--bl-accent) 20%,transparent)">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1a1815" stroke-width="2.5"><circle cx="12" cy="12" r="5"/></svg>
            </div>
            <div style="width:2px;background:var(--bl-line);flex:1;min-height:3rem"></div>
          </div>
          <div style="padding-bottom:2.5rem">
            <div style="font-weight:700;color:var(--bl-accent)">Out for Delivery</div>
            <div style="font-size:.875rem;color:var(--bl-muted);margin-top:.25rem">ETA 7:44 pm — Your rider is 8 minutes away.</div>
          </div>
        </div>

        <!-- Step 4 — pending -->
        <div style="display:flex;gap:1.5rem;align-items:flex-start">
          <div style="display:flex;flex-direction:column;align-items:center;gap:0">
            <div style="width:2.5rem;height:2.5rem;border-radius:50%;background:var(--bl-surface);border:2px solid var(--bl-line);display:flex;align-items:center;justify-content:center;flex-shrink:0">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/></svg>
            </div>
          </div>
          <div>
            <div style="font-weight:600;color:var(--bl-muted)">Delivered</div>
            <div style="font-size:.875rem;color:var(--bl-muted);margin-top:.25rem">Estimated 7:44 pm — Almost there!</div>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- ===== Help CTA ===== -->
  <section class="bl-section">
    <div class="bl-container bl-container--narrow">
      <div class="bl-section-head bl-section-head--center">
        <span class="bl-eyebrow">Need help?</span>
        <h2 class="bl-section-title">Issue with your <em>order?</em></h2>
        <p class="bl-section-lede">Our support team is available every day from 11:00 to midnight. We'll sort any issue within the hour.</p>
      </div>
      <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;margin-top:1.5rem">
        <a href="contact.html" class="bl-btn bl-btn--primary bl-btn--lg">Contact support</a>
        <a href="faq.html" class="bl-btn bl-btn--ghost bl-btn--lg">Read FAQs</a>
      </div>
    </div>
  </section>
"""

write_pair("order-tracking.html", "Order Tracking",
           "Track your BurgerLab order in real time — from kitchen to your door in 30 minutes. Enter your order number and email to check live status.",
           order_tracking_main)


# ════════════════════════════════════════════════════════════════════════════
# 7. loyalty.html — Loyalty / rewards program
# ════════════════════════════════════════════════════════════════════════════
loyalty_main = """
  <!-- ===== Page hero ===== -->
  <section class="bl-page-hero bl-page-hero--photo" style="background-image: url('assets/images/hero-burger.jpg')">
    <div class="bl-container bl-container--narrow">
      <span class="bl-page-hero__eyebrow">Loyalty program</span>
      <h1 class="bl-page-hero__title">Earn while you <em>eat</em></h1>
      <p class="bl-page-hero__lede">Every order earns you Lab Points. Stack them up for free burgers, exclusive events, and priority booking.</p>
      <nav class="bl-breadcrumb" aria-label="Breadcrumb">
        <a href="index.html">Home</a>
        <span class="bl-breadcrumb__sep">/</span>
        <span aria-current="page">Loyalty</span>
      </nav>
    </div>
  </section>

  <!-- ===== How it works ===== -->
  <section class="bl-section">
    <div class="bl-container bl-container--wide">
      <div class="bl-section-head bl-section-head--center">
        <span class="bl-eyebrow">How it works</span>
        <h2 class="bl-section-title">Three steps to <em>free burgers</em></h2>
      </div>
      <div class="bl-ing-grid" data-stagger>
        <div class="bl-ing-card" data-stagger-item>
          <span class="bl-ing-card__no">01</span>
          <h3 class="bl-ing-card__name">Sign up free</h3>
          <p class="bl-ing-card__text">Create your Lab account below — it takes 30 seconds. You'll get 100 bonus points the moment you join, enough for a free side on your first order.</p>
        </div>
        <div class="bl-ing-card" data-stagger-item>
          <span class="bl-ing-card__no">02</span>
          <h3 class="bl-ing-card__name">Earn points</h3>
          <p class="bl-ing-card__text">Earn 1 Lab Point for every $1 you spend — whether you dine in, order delivery, or book a private event. Double points on Tuesdays.</p>
        </div>
        <div class="bl-ing-card" data-stagger-item>
          <span class="bl-ing-card__no">03</span>
          <h3 class="bl-ing-card__name">Redeem rewards</h3>
          <p class="bl-ing-card__text">Redeem points at checkout for free menu items, upgrades, and exclusive experience vouchers. No expiry on points for Gold members.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ===== Tier breakdown ===== -->
  <section class="bl-section bl-section--bg2">
    <div class="bl-container bl-container--wide">
      <div class="bl-section-head bl-section-head--center">
        <span class="bl-eyebrow">Member tiers</span>
        <h2 class="bl-section-title">The higher you climb, <em>the more you earn</em></h2>
      </div>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:1.5rem;margin-top:2.5rem" data-stagger>

        <div class="bl-card" style="padding:2rem" data-stagger-item>
          <div style="font-size:2rem;margin-bottom:.75rem">🥉</div>
          <span class="bl-chip">Bronze</span>
          <h3 style="margin:.75rem 0 .5rem;font-size:1.25rem">0 – 499 pts</h3>
          <ul style="list-style:none;padding:0;display:flex;flex-direction:column;gap:.625rem;font-size:.9375rem;color:var(--bl-muted)">
            <li><span style="color:var(--bl-accent)">✔</span> 1 pt per $1 spent</li>
            <li><span style="color:var(--bl-accent)">✔</span> Free birthday burger</li>
            <li><span style="color:var(--bl-accent)">✔</span> Early access to new menu items</li>
          </ul>
        </div>

        <div class="bl-card" style="padding:2rem;border-color:var(--bl-accent)" data-stagger-item>
          <div style="font-size:2rem;margin-bottom:.75rem">🥈</div>
          <span class="bl-chip" style="background:var(--bl-accent);color:#1a1815">Silver</span>
          <h3 style="margin:.75rem 0 .5rem;font-size:1.25rem">500 – 1,499 pts</h3>
          <ul style="list-style:none;padding:0;display:flex;flex-direction:column;gap:.625rem;font-size:.9375rem;color:var(--bl-muted)">
            <li><span style="color:var(--bl-accent)">✔</span> 1.5 pts per $1 spent</li>
            <li><span style="color:var(--bl-accent)">✔</span> Free birthday meal (main + side)</li>
            <li><span style="color:var(--bl-accent)">✔</span> Priority reservations</li>
            <li><span style="color:var(--bl-accent)">✔</span> Monthly surprise reward</li>
          </ul>
        </div>

        <div class="bl-card" style="padding:2rem" data-stagger-item>
          <div style="font-size:2rem;margin-bottom:.75rem">🥇</div>
          <span class="bl-chip">Gold</span>
          <h3 style="margin:.75rem 0 .5rem;font-size:1.25rem">1,500+ pts</h3>
          <ul style="list-style:none;padding:0;display:flex;flex-direction:column;gap:.625rem;font-size:.9375rem;color:var(--bl-muted)">
            <li><span style="color:var(--bl-accent)">✔</span> 2 pts per $1 spent</li>
            <li><span style="color:var(--bl-accent)">✔</span> Full birthday dinner for two</li>
            <li><span style="color:var(--bl-accent)">✔</span> Dedicated concierge line</li>
            <li><span style="color:var(--bl-accent)">✔</span> Invites to exclusive chef events</li>
            <li><span style="color:var(--bl-accent)">✔</span> Points never expire</li>
          </ul>
        </div>

      </div>
    </div>
  </section>

  <!-- ===== Sign-up form ===== -->
  <section class="bl-section">
    <div class="bl-container bl-container--narrow">
      <div class="bl-section-head bl-section-head--center">
        <span class="bl-eyebrow">Join now</span>
        <h2 class="bl-section-title">Start earning <em>today</em></h2>
        <p class="bl-section-lede">Sign up with your email and we'll send you 100 bonus points instantly — enough for a free side on your very first order.</p>
      </div>
      <div class="bl-form-card bl-reveal-up">
        <form action="https://api.web3forms.com/submit" method="POST" data-form data-success="Welcome to the Lab Loyalty Club! Check your email for your 100 bonus points.">
          <input type="hidden" name="access_key" value="1689852d-c68d-46fa-977e-51c4bc04d29a">
          <input type="hidden" name="subject" value="New BurgerLab Loyalty Sign-up">
          <input type="hidden" name="from_name" value="BurgerLab Website">
          <input type="checkbox" name="botcheck" class="bl-honeypot" tabindex="-1" aria-hidden="true">
          <div class="bl-form-grid">
            <div class="bl-field">
              <label for="ly-first">First name</label>
              <input class="bl-input" type="text" id="ly-first" name="first_name" autocomplete="given-name" required>
            </div>
            <div class="bl-field">
              <label for="ly-last">Last name</label>
              <input class="bl-input" type="text" id="ly-last" name="last_name" autocomplete="family-name" required>
            </div>
            <div class="bl-field bl-field--full">
              <label for="ly-email">Email address</label>
              <input class="bl-input" type="email" id="ly-email" name="email" autocomplete="email" required>
            </div>
          </div>
          <button type="submit" class="bl-btn bl-btn--primary bl-btn--lg">Join the Lab Club — it's free</button>
          <p class="bl-form__note" role="status" aria-live="polite"></p>
        </form>
      </div>
    </div>
  </section>
"""

write_pair("loyalty.html", "Lab Loyalty Club — Earn Points on Every Order",
           "Join the BurgerLab loyalty program and earn 1 point per $1 spent. Redeem for free burgers, priority booking, and exclusive chef events.",
           loyalty_main)


# ════════════════════════════════════════════════════════════════════════════
# 8. gift-cards.html — Gift cards
# ════════════════════════════════════════════════════════════════════════════
gift_cards_main = """
  <!-- ===== Page hero ===== -->
  <section class="bl-page-hero bl-page-hero--photo" style="background-image: url('assets/images/hero-poster.jpg')">
    <div class="bl-container bl-container--narrow">
      <span class="bl-page-hero__eyebrow">Gift cards</span>
      <h1 class="bl-page-hero__title">The gift that <em>never misses</em></h1>
      <p class="bl-page-hero__lede">Send the perfect gift — a BurgerLab gift card delivered instantly by email or posted as a physical card.</p>
      <nav class="bl-breadcrumb" aria-label="Breadcrumb">
        <a href="index.html">Home</a>
        <span class="bl-breadcrumb__sep">/</span>
        <span aria-current="page">Gift Cards</span>
      </nav>
    </div>
  </section>

  <!-- ===== Denomination cards ===== -->
  <section class="bl-section">
    <div class="bl-container bl-container--wide">
      <div class="bl-section-head bl-section-head--center">
        <span class="bl-eyebrow">Choose an amount</span>
        <h2 class="bl-section-title">Pick your <em>value</em></h2>
        <p class="bl-section-lede">Gift cards are valid for 24 months and can be used in-restaurant, for delivery, or on events &amp; private dining.</p>
      </div>
      <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:1.5rem;margin-top:2.5rem" data-stagger>

        <label class="bl-card" style="padding:2rem;text-align:center;cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:.75rem" data-stagger-item>
          <input type="radio" name="denomination" value="25" style="position:absolute;opacity:0" checked>
          <div style="font-size:2.25rem;font-weight:700;color:var(--bl-text)">$25</div>
          <p style="color:var(--bl-muted);font-size:.875rem">Great for a solo lunch with sides and a craft drink.</p>
        </label>

        <label class="bl-card" style="padding:2rem;text-align:center;cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:.75rem;border-color:var(--bl-accent)" data-stagger-item>
          <input type="radio" name="denomination" value="50" style="position:absolute;opacity:0">
          <div style="font-size:2.25rem;font-weight:700;color:var(--bl-accent)">$50</div>
          <p style="color:var(--bl-muted);font-size:.875rem">A date-night dinner for two with drinks and dessert.</p>
        </label>

        <label class="bl-card" style="padding:2rem;text-align:center;cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:.75rem" data-stagger-item>
          <input type="radio" name="denomination" value="100" style="position:absolute;opacity:0">
          <div style="font-size:2.25rem;font-weight:700;color:var(--bl-text)">$100</div>
          <p style="color:var(--bl-muted);font-size:.875rem">A small group dinner with cocktails and sharing plates.</p>
        </label>

        <label class="bl-card" style="padding:2rem;text-align:center;cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:.75rem" data-stagger-item>
          <input type="radio" name="denomination" value="200" style="position:absolute;opacity:0">
          <div style="font-size:2.25rem;font-weight:700;color:var(--bl-text)">$200</div>
          <p style="color:var(--bl-muted);font-size:.875rem">Premium dining experience — covers the Exclusive package for two.</p>
        </label>

      </div>
    </div>
  </section>

  <!-- ===== Purchase form ===== -->
  <section class="bl-section bl-section--bg2">
    <div class="bl-container bl-container--narrow">
      <div class="bl-section-head bl-section-head--center">
        <span class="bl-eyebrow">Send a gift</span>
        <h2 class="bl-section-title">Personalise and <em>send</em></h2>
      </div>
      <div class="bl-form-card bl-reveal-up">
        <form action="https://api.web3forms.com/submit" method="POST" data-form data-success="Gift card order placed — the recipient will receive it by email shortly.">
          <input type="hidden" name="access_key" value="1689852d-c68d-46fa-977e-51c4bc04d29a">
          <input type="hidden" name="subject" value="New BurgerLab Gift Card Order">
          <input type="hidden" name="from_name" value="BurgerLab Website">
          <input type="checkbox" name="botcheck" class="bl-honeypot" tabindex="-1" aria-hidden="true">
          <div class="bl-form-grid">
            <div class="bl-field">
              <label for="gc-from">Your name</label>
              <input class="bl-input" type="text" id="gc-from" name="sender_name" autocomplete="given-name" required>
            </div>
            <div class="bl-field">
              <label for="gc-from-email">Your email</label>
              <input class="bl-input" type="email" id="gc-from-email" name="sender_email" autocomplete="email" required>
            </div>
            <div class="bl-field">
              <label for="gc-to">Recipient's name</label>
              <input class="bl-input" type="text" id="gc-to" name="recipient_name" required>
            </div>
            <div class="bl-field">
              <label for="gc-to-email">Recipient's email</label>
              <input class="bl-input" type="email" id="gc-to-email" name="recipient_email" required>
            </div>
            <div class="bl-field">
              <label for="gc-delivery">Delivery date</label>
              <div class="bl-picker" data-datepicker>
                <input class="bl-input" type="text" id="gc-delivery" name="delivery_date" placeholder="Send immediately or schedule">
                <span class="bl-picker__icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4.5" width="18" height="16" rx="2.5"/><path d="M3 9h18M8 2.5v4M16 2.5v4"/></svg></span>
              </div>
            </div>
            <div class="bl-field">
              <label for="gc-amount">Amount</label>
              <select class="bl-select" id="gc-amount" name="amount">
                <option>$25</option>
                <option selected>$50</option>
                <option>$100</option>
                <option>$200</option>
              </select>
            </div>
            <div class="bl-field bl-field--full">
              <label for="gc-message">Personal message (optional)</label>
              <textarea class="bl-textarea" id="gc-message" name="message" placeholder="Write a message to go with the gift card…"></textarea>
            </div>
          </div>
          <button type="submit" class="bl-btn bl-btn--primary bl-btn--lg">Purchase gift card</button>
          <p class="bl-form__note" role="status" aria-live="polite"></p>
        </form>
      </div>
    </div>
  </section>

  <!-- ===== Check balance ===== -->
  <section class="bl-section">
    <div class="bl-container bl-container--narrow">
      <div class="bl-section-head bl-section-head--center">
        <span class="bl-eyebrow">Already have a card?</span>
        <h2 class="bl-section-title">Check your <em>balance</em></h2>
        <p class="bl-section-lede">Enter your gift card code to see the remaining value.</p>
      </div>
      <div class="bl-form-card bl-reveal-up" style="max-width:480px;margin:0 auto">
        <form data-form data-success="Balance checked — please see your result above.">
          <div class="bl-field">
            <label for="gc-code">Gift card code</label>
            <input class="bl-input" type="text" id="gc-code" name="gift_card_code" placeholder="e.g. BLG-XXXX-XXXX-XXXX" required>
          </div>
          <button type="submit" class="bl-btn bl-btn--ghost bl-btn--lg" style="margin-top:1rem">Check balance</button>
          <p class="bl-form__note" role="status" aria-live="polite"></p>
        </form>
      </div>
    </div>
  </section>
"""

write_pair("gift-cards.html", "Gift Cards — Give the Gift of BurgerLab",
           "Buy a BurgerLab gift card in $25, $50, $100 or $200 denominations. Delivered instantly by email. Valid for 24 months on dining, delivery, and events.",
           gift_cards_main)


# ════════════════════════════════════════════════════════════════════════════
# 9. press.html — Press & media
# ════════════════════════════════════════════════════════════════════════════
press_main = """
  <!-- ===== Page hero ===== -->
  <section class="bl-page-hero bl-page-hero--photo" style="background-image: url('assets/images/hero-about.jpg')">
    <div class="bl-container bl-container--narrow">
      <span class="bl-page-hero__eyebrow">Press &amp; Media</span>
      <h1 class="bl-page-hero__title">BurgerLab in <em>the press</em></h1>
      <p class="bl-page-hero__lede">Download our press kit, read recent coverage, or get in touch with our media team.</p>
      <nav class="bl-breadcrumb" aria-label="Breadcrumb">
        <a href="index.html">Home</a>
        <span class="bl-breadcrumb__sep">/</span>
        <span aria-current="page">Press</span>
      </nav>
    </div>
  </section>

  <!-- ===== Press kit CTA ===== -->
  <section class="bl-section bl-section--bg2">
    <div class="bl-container bl-container--narrow">
      <div class="bl-section-head bl-section-head--center">
        <span class="bl-eyebrow">Press kit</span>
        <h2 class="bl-section-title">Everything you need <em>in one download</em></h2>
        <p class="bl-section-lede">Our press kit includes high-resolution photography, brand guidelines, logo files, executive bios, and key facts about BurgerLab.</p>
      </div>
      <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;margin-top:1.5rem">
        <a href="#" class="bl-btn bl-btn--primary bl-btn--lg">
          <svg class="bl-btn__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true" style="margin-right:.375rem"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M7 10l5 5 5-5M12 15V3"/></svg>
          Download press kit (ZIP, 48 MB)
        </a>
        <a href="#media-contact" class="bl-btn bl-btn--ghost bl-btn--lg">Contact media team</a>
      </div>
    </div>
  </section>

  <!-- ===== Press mentions ===== -->
  <section class="bl-section">
    <div class="bl-container bl-container--wide">
      <div class="bl-section-head bl-section-head--center">
        <span class="bl-eyebrow">As seen in</span>
        <h2 class="bl-section-title">Recent <em>coverage</em></h2>
      </div>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1.5rem;margin-top:2.5rem" data-stagger>

        <div class="bl-card" style="padding:2rem;display:flex;flex-direction:column;gap:1.25rem" data-stagger-item>
          <div style="display:flex;align-items:center;gap:1rem">
            <img src="assets/images/ingredients-detail.jpg" alt="Eater NY" width="60" height="60" loading="lazy" style="border-radius:.5rem;object-fit:cover">
            <div>
              <div style="font-weight:700">Eater NY</div>
              <div style="font-size:.8125rem;color:var(--bl-muted)">March 2026</div>
            </div>
          </div>
          <blockquote style="margin:0;color:var(--bl-text);font-size:.9375rem;line-height:1.65;font-style:italic">"BurgerLab has quietly become the benchmark for smash burgers in Manhattan. The double stack is a masterclass in restraint — nothing superfluous, everything perfect."</blockquote>
          <a href="#" class="bl-btn bl-btn--ghost bl-btn--sm" style="align-self:flex-start">Read article</a>
        </div>

        <div class="bl-card" style="padding:2rem;display:flex;flex-direction:column;gap:1.25rem" data-stagger-item>
          <div style="display:flex;align-items:center;gap:1rem">
            <img src="assets/images/hero-poster.jpg" alt="Time Out New York" width="60" height="60" loading="lazy" style="border-radius:.5rem;object-fit:cover">
            <div>
              <div style="font-weight:700">Time Out New York</div>
              <div style="font-size:.8125rem;color:var(--bl-muted)">January 2026</div>
            </div>
          </div>
          <blockquote style="margin:0;color:var(--bl-text);font-size:.9375rem;line-height:1.65;font-style:italic">"Named one of New York's 50 best restaurants of the year. The private dining room alone is worth the visit — intimate, effortlessly cool, and the food matches the room."</blockquote>
          <a href="#" class="bl-btn bl-btn--ghost bl-btn--sm" style="align-self:flex-start">Read article</a>
        </div>

        <div class="bl-card" style="padding:2rem;display:flex;flex-direction:column;gap:1.25rem" data-stagger-item>
          <div style="display:flex;align-items:center;gap:1rem">
            <img src="assets/images/hero-burger.jpg" alt="New York Times" width="60" height="60" loading="lazy" style="border-radius:.5rem;object-fit:cover">
            <div>
              <div style="font-weight:700">New York Times Dining</div>
              <div style="font-size:.8125rem;color:var(--bl-muted)">October 2025</div>
            </div>
          </div>
          <blockquote style="margin:0;color:var(--bl-text);font-size:.9375rem;line-height:1.65;font-style:italic">"In a city crowded with burger concepts, BurgerLab stands apart by taking the work seriously. The kitchen is obsessive, the service is warm, and the result is simply the best burger in SoHo."</blockquote>
          <a href="#" class="bl-btn bl-btn--ghost bl-btn--sm" style="align-self:flex-start">Read article</a>
        </div>

      </div>
    </div>
  </section>

  <!-- ===== Media contact form ===== -->
  <section class="bl-section bl-section--bg2" id="media-contact">
    <div class="bl-container bl-container--narrow">
      <div class="bl-section-head bl-section-head--center">
        <span class="bl-eyebrow">Get in touch</span>
        <h2 class="bl-section-title">Media <em>enquiries</em></h2>
        <p class="bl-section-lede">For interview requests, photography access, fact-checking, or press accreditation, use the form below.</p>
      </div>
      <div class="bl-form-card bl-reveal-up">
        <form action="https://api.web3forms.com/submit" method="POST" data-form data-success="Media enquiry received — our press team will respond within one business day.">
          <input type="hidden" name="access_key" value="1689852d-c68d-46fa-977e-51c4bc04d29a">
          <input type="hidden" name="subject" value="New BurgerLab Media / Press Enquiry">
          <input type="hidden" name="from_name" value="BurgerLab Website">
          <input type="checkbox" name="botcheck" class="bl-honeypot" tabindex="-1" aria-hidden="true">
          <div class="bl-form-grid">
            <div class="bl-field">
              <label for="pr-name">Your name</label>
              <input class="bl-input" type="text" id="pr-name" name="name" autocomplete="name" required>
            </div>
            <div class="bl-field">
              <label for="pr-outlet">Publication / outlet</label>
              <input class="bl-input" type="text" id="pr-outlet" name="outlet" required>
            </div>
            <div class="bl-field bl-field--full">
              <label for="pr-email">Email address</label>
              <input class="bl-input" type="email" id="pr-email" name="email" autocomplete="email" required>
            </div>
            <div class="bl-field bl-field--full">
              <label for="pr-message">Enquiry details</label>
              <textarea class="bl-textarea" id="pr-message" name="message" placeholder="Describe your enquiry, deadline, and any specific requirements…" required></textarea>
            </div>
          </div>
          <button type="submit" class="bl-btn bl-btn--primary bl-btn--lg">Send enquiry</button>
          <p class="bl-form__note" role="status" aria-live="polite"></p>
        </form>
      </div>
    </div>
  </section>
"""

write_pair("press.html", "Press &amp; Media",
           "BurgerLab press room — download the press kit, read recent coverage from Eater NY, Time Out and NYT, and contact our media team.",
           press_main)


# ════════════════════════════════════════════════════════════════════════════
# 10. sitemap.html — HTML sitemap
# ════════════════════════════════════════════════════════════════════════════
sitemap_main = """
  <!-- ===== Page hero ===== -->
  <section class="bl-page-hero bl-page-hero--photo" style="background-image: url('assets/images/hero-menu.jpg')">
    <div class="bl-container bl-container--narrow">
      <span class="bl-page-hero__eyebrow">Sitemap</span>
      <h1 class="bl-page-hero__title">All <em>Pages</em></h1>
      <p class="bl-page-hero__lede">A complete index of every page on the BurgerLab template — find exactly what you need.</p>
      <nav class="bl-breadcrumb" aria-label="Breadcrumb">
        <a href="index.html">Home</a>
        <span class="bl-breadcrumb__sep">/</span>
        <span aria-current="page">Sitemap</span>
      </nav>
    </div>
  </section>

  <!-- ===== Sitemap content ===== -->
  <section class="bl-section">
    <div class="bl-container bl-container--wide">
      <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:3rem" data-stagger>

        <!-- Home Variants -->
        <div data-stagger-item>
          <h2 style="font-size:1.125rem;font-weight:700;margin-bottom:1rem;padding-bottom:.625rem;border-bottom:1px solid var(--bl-line)">Home Variants</h2>
          <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:.5rem">
            <li><a href="index.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">Home 01 — Cinematic</a></li>
            <li><a href="index-2.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">Home 02 — Slider</a></li>
            <li><a href="index-3.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">Home 03 — App</a></li>
            <li><a href="index-4.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">Home 04 — Split</a></li>
            <li><a href="index-5.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">Home 05 — Statement</a></li>
            <li><a href="index-6.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">Home 06 — Bento</a></li>
            <li><a href="index-7.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">Home 07 — Classic</a></li>
          </ul>
        </div>

        <!-- Restaurant -->
        <div data-stagger-item>
          <h2 style="font-size:1.125rem;font-weight:700;margin-bottom:1rem;padding-bottom:.625rem;border-bottom:1px solid var(--bl-line)">Restaurant</h2>
          <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:.5rem">
            <li><a href="about.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">About</a></li>
            <li><a href="chef.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">The Lab Crew</a></li>
            <li><a href="services.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">Services</a></li>
            <li><a href="service-detail.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">Service Detail</a></li>
            <li><a href="gallery.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">Gallery</a></li>
            <li><a href="reservation.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">Reservation</a></li>
            <li><a href="event.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">Events</a></li>
            <li><a href="event-detail.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">Event Detail</a></li>
            <li><a href="pricing.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">Pricing &amp; Packages</a></li>
            <li><a href="contact.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">Contact</a></li>
          </ul>
        </div>

        <!-- Journal -->
        <div data-stagger-item>
          <h2 style="font-size:1.125rem;font-weight:700;margin-bottom:1rem;padding-bottom:.625rem;border-bottom:1px solid var(--bl-line)">Journal</h2>
          <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:.5rem">
            <li><a href="blog.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">Journal</a></li>
            <li><a href="blog-single.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">Journal Single</a></li>
            <li><a href="faq.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">FAQ</a></li>
            <li><a href="testimonials.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">Testimonials</a></li>
            <li><a href="press.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">Press &amp; Media</a></li>
          </ul>
        </div>

        <!-- Shop & Orders -->
        <div data-stagger-item>
          <h2 style="font-size:1.125rem;font-weight:700;margin-bottom:1rem;padding-bottom:.625rem;border-bottom:1px solid var(--bl-line)">Shop &amp; Orders</h2>
          <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:.5rem">
            <li><a href="menu.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">Menu</a></li>
            <li><a href="menu-category.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">Menu by Category</a></li>
            <li><a href="menu-inside.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">Inside The Lab Burger</a></li>
            <li><a href="single-product.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">Single Product</a></li>
            <li><a href="shopping-cart.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">Shopping Cart</a></li>
            <li><a href="checkout.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">Checkout</a></li>
            <li><a href="order-tracking.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">Order Tracking</a></li>
            <li><a href="loyalty.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">Loyalty Program</a></li>
            <li><a href="gift-cards.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">Gift Cards</a></li>
          </ul>
        </div>

        <!-- About Us -->
        <div data-stagger-item>
          <h2 style="font-size:1.125rem;font-weight:700;margin-bottom:1rem;padding-bottom:.625rem;border-bottom:1px solid var(--bl-line)">About Us</h2>
          <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:.5rem">
            <li><a href="careers.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">Careers</a></li>
          </ul>
        </div>

        <!-- Utility -->
        <div data-stagger-item>
          <h2 style="font-size:1.125rem;font-weight:700;margin-bottom:1rem;padding-bottom:.625rem;border-bottom:1px solid var(--bl-line)">Utility</h2>
          <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:.5rem">
            <li><a href="privacy-policy.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">Privacy Policy</a></li>
            <li><a href="terms.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">Terms &amp; Conditions</a></li>
            <li><a href="sitemap.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">Sitemap</a></li>
            <li><a href="404.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">404 Error Page</a></li>
            <li><a href="coming-soon.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">Coming Soon</a></li>
            <li><a href="headers.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">Header Layouts</a></li>
            <li><a href="footers.html" style="color:var(--bl-muted);text-decoration:none;font-size:.9375rem;transition:color .2s" onmouseover="this.style.color='var(--bl-accent)'" onmouseout="this.style.color='var(--bl-muted)'">Footer Layouts</a></li>
          </ul>
        </div>

      </div>
    </div>
  </section>
"""

write_pair("sitemap.html", "Sitemap — All Pages",
           "Complete HTML sitemap for the BurgerLab restaurant template — navigate all 39 pages including home variants, inner pages, shop, and utilities.",
           sitemap_main)


print("\nAll 10 pages created successfully (20 files total — main + noImages).")
