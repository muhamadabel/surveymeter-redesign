import re

with open('/Users/user/Documents/surveymeter-redesign/build.py', 'r') as f:
    code = f.read()

# 1. Update brand-logo in header to remove redundant text tag
old_brand_markup = """        <a href="#top" class="brand-logo">
          <img src="{logo_b64}" alt="SurveyMETER Logo">
          <div class="brand-tag">
            <span class="brand-tag-title">SURVEYMETER</span>
            <span class="brand-tag-sub">Research &amp; Measurement</span>
          </div>
        </a>"""

new_brand_markup = """        <a href="#top" class="brand-logo" title="SurveyMETER Indonesia">
          <img src="{logo_b64}" alt="SurveyMETER Logo">
        </a>"""

code = code.replace(old_brand_markup, new_brand_markup)

# 2. Adjust media query breakpoints for smoother responsiveness
code = code.replace("@media (max-width: 992px)", "@media (max-width: 860px)")
code = code.replace("@media (max-width: 768px)", "@media (max-width: 640px)")

# 3. Enhance nav-links so they fit nicely
code = code.replace("gap: 32px;", "gap: 24px;")
code = code.replace("height: 38px;", "height: 42px;")

with open('/Users/user/Documents/surveymeter-redesign/build.py', 'w') as f:
    f.write(code)

print("Patched build.py successfully!")
