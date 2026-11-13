import re

svg_logo = """<svg width="240" height="48" viewBox="0 0 240 48" fill="none" xmlns="http://www.w3.org/2000/svg" style="display: block;">
  <!-- Emblem: Dynamic scientific measurement swirl -->
  <g transform="translate(4, 2)">
    <circle cx="22" cy="22" r="20" fill="#EBF7EE" stroke="#C2E7CA" stroke-width="1.2"/>
    <!-- Swirl Arcs -->
    <path d="M 12 28 C 10 18, 18 10, 28 10 C 33 10, 37 13, 39 17 C 35 15, 30 14, 25 16 C 18 19, 15 25, 17 31 C 18 33, 20 35, 22 36 C 18 35, 14 32, 12 28 Z" fill="#0E5E3A"/>
    <path d="M 15 22 C 16 15, 23 11, 30 13 C 35 15, 38 19, 38 24 C 36 21, 32 18, 27 18 C 21 18, 18 22, 19 27 C 20 30, 23 32, 26 33 C 21 32, 17 28, 15 22 Z" fill="#16A34A"/>
    <path d="M 22 17 C 25 15, 30 16, 33 19 C 35 22, 35 26, 32 29 C 30 31, 26 31, 23 29 C 21 27, 21 24, 23 21 C 24 19, 27 18, 29 19 C 27 21, 25 24, 26 26 C 27 27, 29 27, 30 26 C 31 24, 30 22, 28 20 C 26 19, 23 18, 22 17 Z" fill="#0E5E3A"/>
    <circle cx="22" cy="22" r="3.2" fill="#0E5E3A"/>
  </g>
  <!-- Wordmark -->
  <text x="56" y="27" font-family="'Plus Jakarta Sans', Georgia, serif" font-size="20" font-weight="700" fill="#0E5E3A" letter-spacing="-0.02em">Survey<tspan font-weight="800" fill="#141A17">METER</tspan></text>
  <text x="57" y="38" font-family="'Plus Jakarta Sans', -apple-system, sans-serif" font-size="6.5" font-weight="700" fill="#535E57" letter-spacing="0.14em">SURVEY • MEASUREMENT • TRAINING • RESEARCH</text>
</svg>"""

with open('/Users/user/Documents/surveymeter-redesign/build.py', 'r') as f:
    code = f.read()

# Replace img src in brand-logo with inline svg
code = re.sub(
    r'<a href="#top" class="brand-logo"[^>]*>[\s\S]*?</a>',
    f'<a href="#top" class="brand-logo" title="SurveyMETER Indonesia">\n          {svg_logo}\n        </a>',
    code
)

# Also update footer logo
footer_svg = svg_logo.replace('fill="#141A17"', 'fill="#FFFFFF"').replace('fill="#0E5E3A"', 'fill="#34D399"').replace('fill="#535E57"', 'fill="#9BA8A1"')
code = re.sub(
    r'<img src="\{logo_b64\}" alt="SurveyMETER Logo"[^>]*>',
    footer_svg,
    code
)

with open('/Users/user/Documents/surveymeter-redesign/build.py', 'w') as f:
    f.write(code)

print("Updated with vector SVG logo!")
