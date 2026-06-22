#!/usr/bin/env python3
"""Bulk-update navigation in all BurgerLab HTML files to add 10 new pages."""

import os, glob

BASE_DIR = "/Users/elvinmammadoff/Documents/themeforest/burgerlab-html"
NOIMAGES_DIR = os.path.join(BASE_DIR, "burgerlab-noImages")

# ─── Desktop dropdown ───────────────────────────────────────────────────────
# OLD Restaurant group (find exact block)
OLD_RESTAURANT = """              <div class="bl-dropdown__group">
                <span class="bl-dropdown__label">Restaurant</span>
              <a href="about.html""""


# We'll do a targeted replacement: insert after "Reservation" link in Restaurant group
# and add a new "More" group after the Journal group in col 1

OLD_RESTAURANT_BLOCK = '''              <div class="bl-dropdown__group">
                <span class="bl-dropdown__label">Restaurant</span>
              <a href="about.html" class="is-active">About</a>
              <a href="chef.html">The Lab Crew</a>
              <a href="services.html">Services</a>
              <a href="service-detail.html">Service Detail</a>
              <a href="gallery.html">Gallery</a>
              <a href="reservation.html">Reservation</a>
              </div>
              <div class="bl-dropdown__group">
                <span class="bl-dropdown__label">Journal</span>
              <a href="blog.html">Journal</a>
              <a href="blog-single.html">Journal Single</a>
              <a href="faq.html">FAQ</a>
              </div>'''

NEW_RESTAURANT_BLOCK = '''              <div class="bl-dropdown__group">
                <span class="bl-dropdown__label">Restaurant</span>
              <a href="about.html" class="is-active">About</a>
              <a href="chef.html">The Lab Crew</a>
              <a href="services.html">Services</a>
              <a href="service-detail.html">Service Detail</a>
              <a href="gallery.html">Gallery</a>
              <a href="reservation.html">Reservation</a>
              <a href="event.html">Events</a>
              <a href="event-detail.html">Event Detail</a>
              <a href="pricing.html">Pricing</a>
              </div>
              <div class="bl-dropdown__group">
                <span class="bl-dropdown__label">Journal</span>
              <a href="blog.html">Journal</a>
              <a href="blog-single.html">Journal Single</a>
              <a href="faq.html">FAQ</a>
              </div>
              <div class="bl-dropdown__group">
                <span class="bl-dropdown__label">More</span>
              <a href="careers.html">Careers</a>
              <a href="testimonials.html">Testimonials</a>
              <a href="press.html">Press &amp; Media</a>
              </div>'''

# The "about.html" class="is-active" is only on about.html — all others just have href
# So we need a version without is-active too
OLD_RESTAURANT_BLOCK_NO_ACTIVE = OLD_RESTAURANT_BLOCK.replace(
    '<a href="about.html" class="is-active">About</a>',
    '<a href="about.html">About</a>'
)
NEW_RESTAURANT_BLOCK_NO_ACTIVE = NEW_RESTAURANT_BLOCK.replace(
    '<a href="about.html" class="is-active">About</a>',
    '<a href="about.html">About</a>'
)

# ─── Shop group ─────────────────────────────────────────────────────────────
OLD_SHOP_BLOCK = '''              <div class="bl-dropdown__group">
                <span class="bl-dropdown__label">Shop</span>
              <a href="menu-category.html">Menu by Category</a>
              <a href="menu-inside.html">Inside The Lab Burger</a>
              <a href="shopping-cart.html">Shopping Cart</a>
              <a href="single-product.html">Single Product</a>
              <a href="checkout.html">Checkout</a>
              </div>'''

NEW_SHOP_BLOCK = '''              <div class="bl-dropdown__group">
                <span class="bl-dropdown__label">Shop</span>
              <a href="menu-category.html">Menu by Category</a>
              <a href="menu-inside.html">Inside The Lab Burger</a>
              <a href="shopping-cart.html">Shopping Cart</a>
              <a href="single-product.html">Single Product</a>
              <a href="checkout.html">Checkout</a>
              <a href="order-tracking.html">Order Tracking</a>
              <a href="loyalty.html">Loyalty Program</a>
              <a href="gift-cards.html">Gift Cards</a>
              </div>'''

# ─── Utility group ───────────────────────────────────────────────────────────
OLD_UTILITY_BLOCK = '''              <div class="bl-dropdown__group">
                <span class="bl-dropdown__label">Utility</span>
              <a href="privacy-policy.html">Privacy Policy</a>
              <a href="terms.html">Terms &amp; Conditions</a>
              <a href="404.html">404</a>
              <a href="coming-soon.html">Coming Soon</a>
              <a href="headers.html">Header Layouts</a>
              <a href="footers.html">Footer Layouts</a>
              </div>'''

NEW_UTILITY_BLOCK = '''              <div class="bl-dropdown__group">
                <span class="bl-dropdown__label">Utility</span>
              <a href="privacy-policy.html">Privacy Policy</a>
              <a href="terms.html">Terms &amp; Conditions</a>
              <a href="sitemap.html">Sitemap</a>
              <a href="404.html">404</a>
              <a href="coming-soon.html">Coming Soon</a>
              <a href="headers.html">Header Layouts</a>
              <a href="footers.html">Footer Layouts</a>
              </div>'''

# ─── Mobile menu sub-panel ───────────────────────────────────────────────────
OLD_MOBILE = '''        <a href="about.html">About</a>
        <a href="chef.html">The Lab Crew</a>
        <a href="services.html">Services</a>
        <a href="service-detail.html">Service Detail</a>
        <a href="gallery.html">Gallery</a>
        <a href="blog.html">Journal</a>
        <a href="blog-single.html">Journal Single</a>
        <a href="reservation.html">Reservation</a>
        <a href="faq.html">FAQ</a>
        <a href="menu-category.html">Menu by Category</a>
        <a href="menu-inside.html">Inside The Lab Burger</a>
        <a href="checkout.html">Checkout</a>
        <a href="shopping-cart.html">Shopping Cart</a>
        <a href="single-product.html">Single Product</a>
        <a href="privacy-policy.html">Privacy Policy</a>
        <a href="terms.html">Terms &amp; Conditions</a>
        <a href="404.html">404</a>
        <a href="coming-soon.html">Coming Soon</a>
        <a href="headers.html">Header Layouts</a>
        <a href="footers.html">Footer Layouts</a>'''

NEW_MOBILE = '''        <a href="about.html">About</a>
        <a href="chef.html">The Lab Crew</a>
        <a href="services.html">Services</a>
        <a href="service-detail.html">Service Detail</a>
        <a href="gallery.html">Gallery</a>
        <a href="blog.html">Journal</a>
        <a href="blog-single.html">Journal Single</a>
        <a href="reservation.html">Reservation</a>
        <a href="faq.html">FAQ</a>
        <a href="event.html">Events</a>
        <a href="event-detail.html">Event Detail</a>
        <a href="pricing.html">Pricing</a>
        <a href="careers.html">Careers</a>
        <a href="testimonials.html">Testimonials</a>
        <a href="press.html">Press &amp; Media</a>
        <a href="menu-category.html">Menu by Category</a>
        <a href="menu-inside.html">Inside The Lab Burger</a>
        <a href="checkout.html">Checkout</a>
        <a href="shopping-cart.html">Shopping Cart</a>
        <a href="single-product.html">Single Product</a>
        <a href="order-tracking.html">Order Tracking</a>
        <a href="loyalty.html">Loyalty Program</a>
        <a href="gift-cards.html">Gift Cards</a>
        <a href="privacy-policy.html">Privacy Policy</a>
        <a href="terms.html">Terms &amp; Conditions</a>
        <a href="sitemap.html">Sitemap</a>
        <a href="404.html">404</a>
        <a href="coming-soon.html">Coming Soon</a>
        <a href="headers.html">Header Layouts</a>
        <a href="footers.html">Footer Layouts</a>'''


def update_file(path):
    with open(path, encoding="utf-8") as f:
        html = f.read()

    original = html

    # Desktop nav – Restaurant + Journal group (handle with or without is-active)
    if OLD_RESTAURANT_BLOCK in html:
        html = html.replace(OLD_RESTAURANT_BLOCK, NEW_RESTAURANT_BLOCK)
    elif OLD_RESTAURANT_BLOCK_NO_ACTIVE in html:
        html = html.replace(OLD_RESTAURANT_BLOCK_NO_ACTIVE, NEW_RESTAURANT_BLOCK_NO_ACTIVE)

    # Desktop nav – Shop group
    html = html.replace(OLD_SHOP_BLOCK, NEW_SHOP_BLOCK)

    # Desktop nav – Utility group
    html = html.replace(OLD_UTILITY_BLOCK, NEW_UTILITY_BLOCK)

    # Mobile menu
    html = html.replace(OLD_MOBILE, NEW_MOBILE)

    if html != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        return True
    return False


# Process all files in both directories
all_files = (
    glob.glob(os.path.join(BASE_DIR, "*.html")) +
    glob.glob(os.path.join(NOIMAGES_DIR, "*.html"))
)

updated = 0
skipped = 0
for path in sorted(all_files):
    basename = os.path.basename(path)
    result = update_file(path)
    if result:
        updated += 1
        print(f"  Updated: {os.path.relpath(path, BASE_DIR)}")
    else:
        skipped += 1
        print(f"  Skipped (no match): {os.path.relpath(path, BASE_DIR)}")

print(f"\nDone. {updated} files updated, {skipped} skipped.")
