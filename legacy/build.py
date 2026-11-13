import base64
import os

workdir = '/Users/user/Documents/surveymeter-redesign'

def get_b64(fname, mime="image/jpeg"):
    p = os.path.join(workdir, fname)
    if os.path.exists(p):
        with open(p, 'rb') as f:
            encoded = base64.b64encode(f.read()).decode('utf-8')
            return f"data:{mime};base64,{encoded}"
    return ""

logo_b64 = get_b64('surveymeter-logo.png', 'image/png')
pub_repro = get_b64('pub_repro.jpg', 'image/jpeg')
pub_irsa = get_b64('pub_irsa.jpg', 'image/jpeg')
pub_nbs = get_b64('pub_nbs.jpg', 'image/jpeg')
pub_adb_aging = get_b64('pub_adb_aging.jpg', 'image/jpeg')
pub_aceh = get_b64('pub_aceh.jpg', 'image/jpeg')
peta_b64 = get_b64('peta.png', 'image/png')
slai_b64 = get_b64('slai_adb.png', 'image/png')

html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SurveyMETER | Riset Kebijakan & Survei Longitudinal</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400;1,6..72,500&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg-page: #FAF8F5;
      --bg-surface: #FFFFFF;
      --bg-surface-subtle: #F3EFEA;
      --brand-green: #0E5E3A;
      --brand-green-hover: #09472B;
      --brand-green-light: #EBF7EE;
      --brand-green-border: #C2E7CA;
      --text-main: #141A17;
      --text-muted: #535E57;
      --text-light: #7E8B83;
      --border-color: #E6E1D8;
      --border-subtle: #ECE8E0;
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 22px;
      --radius-pill: 9999px;
      --shadow-sm: 0 1px 2px rgba(20, 26, 23, 0.04);
      --shadow-card: 0 4px 16px rgba(20, 26, 23, 0.05);
      --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      --font-serif: 'Newsreader', Georgia, serif;
    }}

    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    html {{
      scroll-behavior: smooth;
      font-size: 16px;
    }}

    body {{
      background-color: var(--bg-page);
      color: var(--text-main);
      font-family: var(--font-sans);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
    }}

    a {{
      color: inherit;
      text-decoration: none;
    }}

    button {{
      font-family: inherit;
      cursor: pointer;
      border: none;
      background: none;
    }}

    /* Container */
    .container {{
      width: 100%;
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 24px;
    }}

    /* Top Announcement Banner (Osome Style) */
    .announcement-bar {{
      background-color: var(--brand-green);
      color: #FFFFFF;
      font-size: 0.875rem;
      padding: 10px 16px;
      position: relative;
      z-index: 50;
    }}
    .announcement-bar .inner {{
      max-width: 1200px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
      flex-wrap: wrap;
      text-align: center;
    }}
    .announcement-badge {{
      background: rgba(255, 255, 255, 0.2);
      padding: 2px 10px;
      border-radius: var(--radius-pill);
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 0.03em;
      text-transform: uppercase;
    }}
    .announcement-link {{
      color: #FFFFFF;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.4);
      transition: border-color 0.2s;
    }}
    .announcement-link:hover {{
      border-color: #FFFFFF;
    }}

    /* Sticky Navbar */
    .site-header {{
      position: sticky;
      top: 0;
      z-index: 40;
      background: rgba(250, 248, 245, 0.94);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border-color);
      transition: all 0.25s ease;
    }}
    .nav-wrapper {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      height: 72px;
    }}
    .brand-logo {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .brand-logo img {{
      height: 42px;
      width: auto;
      object-fit: contain;
    }}
    .brand-tag {{
      display: flex;
      flex-direction: column;
      border-left: 1px solid var(--border-color);
      padding-left: 12px;
      margin-left: 4px;
    }}
    .brand-tag-title {{
      font-size: 0.825rem;
      font-weight: 700;
      color: var(--brand-green);
      letter-spacing: 0.02em;
      line-height: 1.2;
    }}
    .brand-tag-sub {{
      font-size: 0.7rem;
      color: var(--text-muted);
      letter-spacing: 0.02em;
    }}

    .nav-links {{
      display: flex;
      align-items: center;
      gap: 24px;
      list-style: none;
    }}
    .nav-link {{
      font-size: 0.925rem;
      font-weight: 500;
      color: var(--text-muted);
      transition: color 0.15s ease;
      position: relative;
    }}
    .nav-link:hover, .nav-link.active {{
      color: var(--text-main);
    }}
    .nav-link.active::after {{
      content: '';
      position: absolute;
      bottom: -6px;
      left: 0;
      right: 0;
      height: 2px;
      background-color: var(--brand-green);
      border-radius: 2px;
    }}

    .nav-actions {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}
    .lang-switcher {{
      display: inline-flex;
      background: var(--bg-surface-subtle);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-pill);
      padding: 3px;
      font-size: 0.775rem;
      font-weight: 600;
    }}
    .lang-btn {{
      padding: 4px 10px;
      border-radius: var(--radius-pill);
      color: var(--text-muted);
      transition: all 0.2s;
    }}
    .lang-btn.active {{
      background: var(--bg-surface);
      color: var(--brand-green);
      box-shadow: var(--shadow-sm);
    }}

    /* Buttons (Osome geometry: Pill shaped, strong contrast) */
    .btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      font-weight: 600;
      border-radius: var(--radius-pill);
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      white-space: nowrap;
    }}
    .btn-primary {{
      background-color: var(--brand-green);
      color: #FFFFFF;
      padding: 12px 24px;
      font-size: 0.925rem;
    }}
    .btn-primary:hover {{
      background-color: var(--brand-green-hover);
      transform: translateY(-1px);
    }}
    .btn-secondary {{
      background-color: var(--bg-surface);
      color: var(--text-main);
      border: 1px solid var(--border-color);
      padding: 12px 24px;
      font-size: 0.925rem;
    }}
    .btn-secondary:hover {{
      background-color: #F5F2EB;
      border-color: #D6D0C5;
      transform: translateY(-1px);
    }}
    .btn-sm {{
      padding: 8px 16px;
      font-size: 0.825rem;
    }}

    /* Mobile Menu Toggle */
    .mobile-menu-toggle {{
      display: none;
      flex-direction: column;
      gap: 5px;
      width: 24px;
      cursor: pointer;
    }}
    .mobile-menu-toggle span {{
      display: block;
      height: 2px;
      width: 100%;
      background: var(--text-main);
      border-radius: 2px;
    }}

    /* Hero Section (Osome Style with Editorial Research Authority) */
    .hero {{
      padding: 72px 0 60px;
      position: relative;
    }}
    .hero-content {{
      max-width: 860px;
      margin: 0 auto;
      text-align: center;
    }}
    .hero-pretitle {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: var(--brand-green-light);
      border: 1px solid var(--brand-green-border);
      color: var(--brand-green);
      padding: 6px 14px;
      border-radius: var(--radius-pill);
      font-size: 0.825rem;
      font-weight: 600;
      margin-bottom: 24px;
    }}
    .hero-pretitle .dot {{
      width: 6px;
      height: 6px;
      background: var(--brand-green);
      border-radius: 50%;
    }}
    .hero-title {{
      font-size: clamp(2.3rem, 5vw, 3.6rem);
      font-weight: 700;
      line-height: 1.18;
      letter-spacing: -0.02em;
      color: var(--text-main);
      margin-bottom: 24px;
    }}
    .hero-title em {{
      font-family: var(--font-serif);
      font-weight: 400;
      font-style: italic;
      color: var(--brand-green);
      padding: 0 4px;
    }}
    .hero-desc {{
      font-size: clamp(1.05rem, 1.8vw, 1.2rem);
      color: var(--text-muted);
      line-height: 1.65;
      max-width: 720px;
      margin: 0 auto 36px;
    }}
    .hero-cta-group {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 16px;
      flex-wrap: wrap;
      margin-bottom: 56px;
    }}

    /* Metrics Strip */
    .hero-stats-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 28px 36px;
      box-shadow: var(--shadow-card);
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 24px;
      text-align: left;
    }}
    .stat-item {{
      border-right: 1px solid var(--border-subtle);
      padding-right: 20px;
    }}
    .stat-item:last-child {{
      border-right: none;
      padding-right: 0;
    }}
    .stat-num {{
      font-size: 2.1rem;
      font-weight: 800;
      color: var(--brand-green);
      line-height: 1.1;
      letter-spacing: -0.02em;
      margin-bottom: 6px;
    }}
    .stat-label {{
      font-size: 0.85rem;
      color: var(--text-muted);
      font-weight: 500;
      line-height: 1.4;
    }}

    /* Partner Credibility Bar */
    .partners-section {{
      padding: 40px 0 60px;
      border-bottom: 1px solid var(--border-color);
    }}
    .partners-title {{
      text-align: center;
      font-size: 0.825rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-light);
      margin-bottom: 28px;
    }}
    .partners-grid {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: center;
      gap: 36px 48px;
      opacity: 0.85;
    }}
    .partner-pill {{
      font-size: 0.95rem;
      font-weight: 700;
      color: #3C4740;
      padding: 8px 18px;
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-pill);
      letter-spacing: -0.01em;
      transition: all 0.2s;
    }}
    .partner-pill:hover {{
      color: var(--brand-green);
      border-color: var(--brand-green-border);
      background: var(--brand-green-light);
    }}

    /* Section Headers */
    .section-header {{
      text-align: center;
      max-width: 720px;
      margin: 0 auto 52px;
    }}
    .section-kicker {{
      display: inline-block;
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--brand-green);
      margin-bottom: 12px;
    }}
    .section-title {{
      font-size: clamp(1.8rem, 3.2vw, 2.5rem);
      font-weight: 700;
      line-height: 1.25;
      letter-spacing: -0.02em;
      color: var(--text-main);
      margin-bottom: 16px;
    }}
    .section-title em {{
      font-family: var(--font-serif);
      font-weight: 400;
      font-style: italic;
      color: var(--brand-green);
    }}
    .section-subtitle {{
      font-size: 1.05rem;
      color: var(--text-muted);
      line-height: 1.6;
    }}

    /* Capabilities (Osome Feature Cards) */
    .capabilities-section {{
      padding: 88px 0;
    }}
    .capabilities-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 28px;
    }}
    .capability-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 36px;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .capability-card:hover {{
      transform: translateY(-3px);
      box-shadow: var(--shadow-card);
      border-color: #D8D2C6;
    }}
    .capability-top {{
      margin-bottom: 24px;
    }}
    .capability-tag {{
      display: inline-block;
      background: var(--brand-green-light);
      color: var(--brand-green);
      font-size: 0.75rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: var(--radius-pill);
      margin-bottom: 16px;
    }}
    .capability-title {{
      font-size: 1.4rem;
      font-weight: 700;
      color: var(--text-main);
      line-height: 1.3;
      margin-bottom: 12px;
      letter-spacing: -0.01em;
    }}
    .capability-desc {{
      font-size: 0.95rem;
      color: var(--text-muted);
      line-height: 1.6;
      margin-bottom: 20px;
    }}
    .capability-bullets {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin-bottom: 24px;
    }}
    .capability-bullets li {{
      font-size: 0.875rem;
      color: var(--text-main);
      display: flex;
      align-items: flex-start;
      gap: 10px;
    }}
    .capability-bullets li::before {{
      content: '✓';
      color: var(--brand-green);
      font-weight: 800;
      margin-top: 1px;
    }}
    .capability-footer {{
      padding-top: 20px;
      border-top: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    .card-link {{
      font-size: 0.875rem;
      font-weight: 600;
      color: var(--brand-green);
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: gap 0.2s;
    }}
    .card-link:hover {{
      gap: 10px;
      color: var(--brand-green-hover);
    }}

    /* Data Publik Hub (Signature Interactive Section) */
    .data-portal-section {{
      padding: 88px 0;
      background: #F4EFEA;
      border-top: 1px solid var(--border-color);
      border-bottom: 1px solid var(--border-color);
    }}
    .data-portal-box {{
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 44px;
      box-shadow: var(--shadow-card);
    }}
    .data-portal-header {{
      display: flex;
      align-items: flex-end;
      justify-content: space-between;
      gap: 24px;
      margin-bottom: 36px;
      flex-wrap: wrap;
    }}
    .data-search-wrapper {{
      display: flex;
      align-items: center;
      gap: 12px;
      background: var(--bg-page);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-pill);
      padding: 8px 18px;
      width: 100%;
      max-width: 380px;
    }}
    .data-search-input {{
      border: none;
      background: transparent;
      outline: none;
      font-size: 0.9rem;
      font-family: inherit;
      color: var(--text-main);
      width: 100%;
    }}
    .data-search-input::placeholder {{
      color: var(--text-light);
    }}

    /* Dataset Cards */
    .dataset-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
      margin-bottom: 32px;
    }}
    .dataset-card {{
      background: var(--bg-page);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 24px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: border-color 0.2s, background-color 0.2s;
    }}
    .dataset-card:hover {{
      border-color: var(--brand-green);
      background-color: #FFFFFF;
    }}
    .dataset-badge-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 14px;
    }}
    .dataset-status {{
      font-size: 0.725rem;
      font-weight: 700;
      color: var(--brand-green);
      background: var(--brand-green-light);
      padding: 3px 8px;
      border-radius: var(--radius-pill);
    }}
    .dataset-year {{
      font-size: 0.75rem;
      color: var(--text-light);
      font-weight: 600;
    }}
    .dataset-name {{
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--text-main);
      line-height: 1.35;
      margin-bottom: 10px;
    }}
    .dataset-snippet {{
      font-size: 0.85rem;
      color: var(--text-muted);
      line-height: 1.55;
      margin-bottom: 18px;
    }}
    .dataset-meta {{
      font-size: 0.775rem;
      color: var(--text-muted);
      border-top: 1px solid var(--border-color);
      padding-top: 14px;
      margin-bottom: 18px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}
    .dataset-meta-item {{
      display: flex;
      justify-content: space-between;
    }}
    .dataset-actions {{
      display: flex;
      gap: 8px;
    }}
    .btn-dataset {{
      flex: 1;
      padding: 8px 12px;
      font-size: 0.8rem;
      border-radius: var(--radius-pill);
      font-weight: 600;
      text-align: center;
    }}
    .btn-dataset-primary {{
      background: var(--brand-green);
      color: #FFFFFF;
    }}
    .btn-dataset-primary:hover {{
      background: var(--brand-green-hover);
    }}
    .btn-dataset-outline {{
      border: 1px solid var(--border-color);
      color: var(--text-main);
      background: #FFFFFF;
    }}
    .btn-dataset-outline:hover {{
      background: #EFECE6;
    }}

    /* Publications Section */
    .publications-section {{
      padding: 88px 0;
    }}
    .pub-tabs {{
      display: flex;
      justify-content: center;
      gap: 10px;
      margin-bottom: 40px;
      flex-wrap: wrap;
    }}
    .pub-tab-btn {{
      padding: 8px 18px;
      border-radius: var(--radius-pill);
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--text-muted);
      border: 1px solid var(--border-color);
      background: var(--bg-surface);
      transition: all 0.2s;
    }}
    .pub-tab-btn.active, .pub-tab-btn:hover {{
      background: var(--brand-green);
      color: #FFFFFF;
      border-color: var(--brand-green);
    }}

    .pub-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 28px;
    }}
    .pub-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
    }}
    .pub-card:hover {{
      transform: translateY(-3px);
      box-shadow: var(--shadow-card);
    }}
    .pub-cover-wrap {{
      height: 220px;
      background: #F1ECE4;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 16px;
      border-bottom: 1px solid var(--border-color);
      position: relative;
    }}
    .pub-cover-wrap img {{
      max-height: 100%;
      width: auto;
      object-fit: contain;
      box-shadow: 0 4px 12px rgba(0,0,0,0.12);
      border-radius: 4px;
    }}
    .pub-body {{
      padding: 24px;
      display: flex;
      flex-direction: column;
      flex: 1;
      justify-content: space-between;
    }}
    .pub-date {{
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--brand-green);
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin-bottom: 8px;
    }}
    .pub-title {{
      font-size: 1.05rem;
      font-weight: 700;
      line-height: 1.4;
      color: var(--text-main);
      margin-bottom: 12px;
    }}
    .pub-meta {{
      font-size: 0.8rem;
      color: var(--text-muted);
      line-height: 1.5;
      margin-bottom: 16px;
    }}
    .pub-download-link {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 0.825rem;
      font-weight: 700;
      color: var(--brand-green);
      transition: gap 0.2s;
    }}
    .pub-download-link:hover {{
      gap: 10px;
      text-decoration: underline;
    }}

    /* Methodology & Rigor Section (Osome "Why Osome" Style) */
    .rigor-section {{
      padding: 88px 0;
      background: var(--bg-surface);
      border-top: 1px solid var(--border-color);
      border-bottom: 1px solid var(--border-color);
    }}
    .rigor-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
    }}
    .rigor-box {{
      padding: 28px;
      border-radius: var(--radius-md);
      background: var(--bg-page);
      border: 1px solid var(--border-subtle);
    }}
    .rigor-num {{
      font-size: 1.5rem;
      font-weight: 800;
      color: var(--brand-green);
      margin-bottom: 14px;
      display: inline-block;
      padding: 4px 12px;
      background: var(--brand-green-light);
      border-radius: var(--radius-pill);
    }}
    .rigor-title {{
      font-size: 1.15rem;
      font-weight: 700;
      margin-bottom: 10px;
      color: var(--text-main);
    }}
    .rigor-desc {{
      font-size: 0.9rem;
      color: var(--text-muted);
      line-height: 1.6;
    }}

    /* Institutional Profile Section */
    .about-section {{
      padding: 88px 0;
    }}
    .about-layout {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 56px;
      align-items: center;
    }}
    .about-text h3 {{
      font-size: 2rem;
      font-weight: 700;
      line-height: 1.25;
      letter-spacing: -0.02em;
      margin-bottom: 20px;
    }}
    .about-text h3 em {{
      font-family: var(--font-serif);
      font-weight: 400;
      font-style: italic;
      color: var(--brand-green);
    }}
    .about-text p {{
      font-size: 0.95rem;
      color: var(--text-muted);
      line-height: 1.65;
      margin-bottom: 16px;
    }}
    .about-timeline {{
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 32px;
    }}
    .timeline-item {{
      position: relative;
      padding-left: 28px;
      margin-bottom: 24px;
    }}
    .timeline-item:last-child {{
      margin-bottom: 0;
    }}
    .timeline-item::before {{
      content: '';
      position: absolute;
      left: 6px;
      top: 6px;
      bottom: -24px;
      width: 2px;
      background: var(--border-color);
    }}
    .timeline-item:last-child::before {{
      display: none;
    }}
    .timeline-node {{
      position: absolute;
      left: 0;
      top: 6px;
      width: 14px;
      height: 14px;
      border-radius: 50%;
      background: var(--bg-surface);
      border: 3px solid var(--brand-green);
    }}
    .timeline-year {{
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--brand-green);
      margin-bottom: 4px;
    }}
    .timeline-title {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 4px;
    }}
    .timeline-desc {{
      font-size: 0.85rem;
      color: var(--text-muted);
      line-height: 1.5;
    }}

    /* Contact Banner / CTA Strip */
    .cta-strip {{
      padding: 72px 0;
      background: var(--brand-green);
      color: #FFFFFF;
      text-align: center;
    }}
    .cta-strip h2 {{
      font-size: 2.2rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      margin-bottom: 16px;
    }}
    .cta-strip h2 em {{
      font-family: var(--font-serif);
      font-weight: 400;
      font-style: italic;
    }}
    .cta-strip p {{
      font-size: 1.05rem;
      opacity: 0.9;
      max-width: 640px;
      margin: 0 auto 32px;
      line-height: 1.6;
    }}
    .cta-strip-actions {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 16px;
      flex-wrap: wrap;
    }}
    .btn-light {{
      background: #FFFFFF;
      color: var(--brand-green);
      font-weight: 700;
      padding: 14px 30px;
    }}
    .btn-light:hover {{
      background: #F4FAF5;
      transform: translateY(-1px);
    }}
    .btn-ghost-light {{
      background: transparent;
      color: #FFFFFF;
      border: 1px solid rgba(255, 255, 255, 0.4);
      padding: 14px 28px;
    }}
    .btn-ghost-light:hover {{
      border-color: #FFFFFF;
      background: rgba(255, 255, 255, 0.08);
      transform: translateY(-1px);
    }}

    /* Footer */
    .site-footer {{
      background: #121815;
      color: #D3DDD7;
      padding: 68px 0 32px;
      font-size: 0.875rem;
    }}
    .footer-grid {{
      display: grid;
      grid-template-columns: 2fr 1fr 1fr 1.5fr;
      gap: 48px;
      margin-bottom: 56px;
    }}
    .footer-col h4 {{
      color: #FFFFFF;
      font-size: 0.95rem;
      font-weight: 700;
      margin-bottom: 18px;
      letter-spacing: 0.02em;
    }}
    .footer-col p {{
      color: #9BA8A1;
      line-height: 1.6;
      margin-bottom: 14px;
    }}
    .footer-links {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}
    .footer-links a {{
      color: #9BA8A1;
      transition: color 0.15s;
    }}
    .footer-links a:hover {{
      color: #FFFFFF;
    }}
    .footer-contact-item {{
      margin-bottom: 10px;
      color: #9BA8A1;
    }}
    .footer-contact-item strong {{
      color: #FFFFFF;
      display: block;
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}
    .footer-bottom {{
      border-top: 1px solid #232E29;
      padding-top: 28px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 16px;
      font-size: 0.8rem;
      color: #798780;
    }}
    .footer-socials {{
      display: flex;
      gap: 16px;
    }}
    .footer-socials a {{
      color: #9BA8A1;
      transition: color 0.15s;
    }}
    .footer-socials a:hover {{
      color: #FFFFFF;
    }}

    /* Interactive Data Request Modal */
    .modal-overlay {{
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(18, 24, 21, 0.65);
      backdrop-filter: blur(4px);
      z-index: 100;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }}
    .modal-overlay.active {{
      display: flex;
    }}
    .modal-box {{
      background: var(--bg-surface);
      border-radius: var(--radius-lg);
      max-width: 540px;
      width: 100%;
      padding: 36px;
      position: relative;
      box-shadow: 0 20px 40px rgba(0,0,0,0.2);
    }}
    .modal-close-btn {{
      position: absolute;
      top: 20px;
      right: 20px;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      border: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.2rem;
      color: var(--text-muted);
      transition: all 0.2s;
    }}
    .modal-close-btn:hover {{
      background: #F4EFEA;
      color: var(--text-main);
    }}
    .modal-title {{
      font-size: 1.4rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 8px;
    }}
    .modal-desc {{
      font-size: 0.875rem;
      color: var(--text-muted);
      margin-bottom: 24px;
    }}
    .form-group {{
      margin-bottom: 16px;
      text-align: left;
    }}
    .form-label {{
      display: block;
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--text-main);
      margin-bottom: 6px;
    }}
    .form-input, .form-select, .form-textarea {{
      width: 100%;
      padding: 10px 14px;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-sm);
      font-family: inherit;
      font-size: 0.875rem;
      color: var(--text-main);
      background: var(--bg-page);
      outline: none;
      transition: border-color 0.2s;
    }}
    .form-input:focus, .form-select:focus, .form-textarea:focus {{
      border-color: var(--brand-green);
      background: #FFFFFF;
    }}
    .form-textarea {{
      resize: vertical;
      min-height: 80px;
    }}
    .modal-submit-btn {{
      width: 100%;
      margin-top: 10px;
    }}
    .form-success-msg {{
      display: none;
      background: var(--brand-green-light);
      border: 1px solid var(--brand-green-border);
      color: var(--brand-green);
      padding: 14px;
      border-radius: var(--radius-sm);
      font-size: 0.875rem;
      font-weight: 600;
      text-align: center;
    }}

    /* Responsive */
    @media (max-width: 860px) {{
      .hero-stats-card {{
        grid-template-columns: repeat(2, 1fr);
      }}
      .stat-item:nth-child(2) {{
        border-right: none;
      }}
      .capabilities-grid {{
        grid-template-columns: 1fr;
      }}
      .dataset-grid {{
        grid-template-columns: 1fr;
      }}
      .pub-grid {{
        grid-template-columns: 1fr;
      }}
      .rigor-grid {{
        grid-template-columns: 1fr;
      }}
      .about-layout {{
        grid-template-columns: 1fr;
      }}
      .footer-grid {{
        grid-template-columns: 1fr 1fr;
      }}
    }}

    @media (max-width: 640px) {{
      .nav-links {{
        display: none;
      }}
      .mobile-menu-toggle {{
        display: flex;
      }}
      .hero {{
        padding: 44px 0 40px;
      }}
      .hero-stats-card {{
        grid-template-columns: 1fr;
        padding: 24px;
      }}
      .stat-item {{
        border-right: none;
        border-bottom: 1px solid var(--border-subtle);
        padding-bottom: 16px;
        margin-bottom: 16px;
      }}
      .stat-item:last-child {{
        border-bottom: none;
        margin-bottom: 0;
        padding-bottom: 0;
      }}
      .data-portal-box {{
        padding: 24px;
      }}
      .footer-grid {{
        grid-template-columns: 1fr;
      }}
    }}
  </style>
</head>
<body>

  <!-- Top Announcement Bar (Osome Pattern) -->
  <aside class="announcement-bar">
    <div class="inner">
      <span class="announcement-badge">Pembaruan Riset</span>
      <span>Dataset Longitudinal Penuaan Penduduk (ILAS 2023) telah resmi dirilis untuk periset dan pembuat kebijakan.</span>
      <a href="#data-publik" class="announcement-link">Akses Portal Data &rarr;</a>
    </div>
  </aside>

  <!-- Sticky Main Header -->
  <header class="site-header">
    <div class="container">
      <div class="nav-wrapper">
        <a href="#top" class="brand-logo" title="SurveyMETER Indonesia">
          <svg width="240" height="48" viewBox="0 0 240 48" fill="none" xmlns="http://www.w3.org/2000/svg" style="display: block;">
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
</svg>
        </a>

        <nav>
          <ul class="nav-links">
            <li><a href="#fokus" class="nav-link">Fokus Riset</a></li>
            <li><a href="#data-publik" class="nav-link">Data Publik</a></li>
            <li><a href="#publikasi" class="nav-link">Publikasi</a></li>
            <li><a href="#metodologi" class="nav-link">Metodologi</a></li>
            <li><a href="#profil" class="nav-link">Tentang Kami</a></li>
          </ul>
        </nav>

        <div class="nav-actions">
          <div class="lang-switcher">
            <button class="lang-btn active">ID</button>
            <button class="lang-btn" onclick="alert('Versi bahasa Inggris dalam proses sinkronisasi.')">EN</button>
          </div>
          <button class="btn btn-primary btn-sm" onclick="openDataModal('Permohonan Akses Data')">
            Permohonan Data
          </button>
          <div class="mobile-menu-toggle" onclick="toggleMobileMenu()">
            <span></span>
            <span></span>
          </div>
        </div>
      </div>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="hero" id="top">
    <div class="container">
      <div class="hero-content">
        <div class="hero-pretitle">
          <span class="dot"></span>
          <span>Lembaga Penelitian Independen Terakreditasi - Yogyakarta</span>
        </div>
        <h1 class="hero-title">
          Riset Kebijakan Berbasis Bukti untuk <em>Pembangunan Berkelanjutan</em>
        </h1>
        <p class="hero-desc">
          SurveyMETER mendesain dan mengelola pengumpulan data longitudinal berskala besar, survei sosial-ekonomi rumah tangga, serta analisis dampak kebijakan publik bagi pembuat kebijakan domestik dan institusi internasional sejak 2002.
        </p>
        <div class="hero-cta-group">
          <a href="#data-publik" class="btn btn-primary">
            Eksplorasi Katalog Data Publik &rarr;
          </a>
          <a href="#publikasi" class="btn btn-secondary">
            Lihat Publikasi &amp; Policy Brief
          </a>
        </div>

        <!-- Metric Strip (Osome Facts & Numbers pattern) -->
        <div class="hero-stats-card">
          <div class="stat-item">
            <div class="stat-num">22+</div>
            <div class="stat-label">Tahun Dedikasi Riset &amp; Pengumpulan Data Lapangan</div>
          </div>
          <div class="stat-item">
            <div class="stat-num">35+</div>
            <div class="stat-label">Kemitraan Lembaga Internasional &amp; Kementerian</div>
          </div>
          <div class="stat-item">
            <div class="stat-num">100+</div>
            <div class="stat-label">Survei Longitudinal, Rumah Tangga &amp; Komunitas</div>
          </div>
          <div class="stat-item">
            <div class="stat-num">100%</div>
            <div class="stat-label">Data Primer Presisi dengan Supervisi Bertingkat</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Strategic Partners Section -->
  <section class="partners-section">
    <div class="container">
      <h3 class="partners-title">Dipercaya Oleh Lembaga Kebijakan &amp; Riset Dunia</h3>
      <div class="partners-grid">
        <div class="partner-pill">The World Bank</div>
        <div class="partner-pill">Asian Development Bank (ADB)</div>
        <div class="partner-pill">BAPPENAS RI</div>
        <div class="partner-pill">RAND Corporation</div>
        <div class="partner-pill">J-PAL (Abdul Latif Jameel)</div>
        <div class="partner-pill">UNICEF</div>
        <div class="partner-pill">TNP2K</div>
        <div class="partner-pill">Kementerian Kesehatan RI</div>
        <div class="partner-pill">Australian National University</div>
        <div class="partner-pill">Universitas Gadjah Mada</div>
      </div>
    </div>
  </section>

  <!-- Research Capabilities (Osome Modular Feature Cards) -->
  <section class="capabilities-section" id="fokus">
    <div class="container">
      <div class="section-header">
        <span class="section-kicker">Kapabilitas &amp; Layanan</span>
        <h2 class="section-title">Solusi Menyeluruh dari <em>Perancangan Instrumen</em> hingga Advokasi Kebijakan</h2>
        <p class="section-subtitle">
          Kami memadukan standar akademik global dengan kepiawaian logistik lapangan untuk menghasilkan data yang akurat dan dapat diandalkan bagi pengambilan keputusan strategis.
        </p>
      </div>

      <div class="capabilities-grid">
        <!-- Card 1 -->
        <article class="capability-card">
          <div class="capability-top">
            <span class="capability-tag">Survei Panel &amp; Kohor</span>
            <h3 class="capability-title">Survei Longitudinal Skala Besar</h3>
            <p class="capability-desc">
              Pelopor pelaksanaan survei panel multi-topik yang melacak dinamika kesejahteraan, kesehatan, dan ekonomi rumah tangga dari waktu ke waktu secara konsisten.
            </p>
            <ul class="capability-bullets">
              <li>Penerapan metodologi panel internasional berbasis standar IFLS (Indonesia Family Life Survey).</li>
              <li>Manajemen pelacakan responden (tracking rate) tinggi hingga ke pelosok daerah terpencil.</li>
              <li>Integrasi modul multi-sektor: pengeluaran, ketenagakerjaan, kesehatan fisik, dan modal sosial.</li>
            </ul>
          </div>
          <div class="capability-footer">
            <span class="card-link" onclick="openDataModal('Survei Longitudinal')">Diskusikan Kebutuhan Survei &rarr;</span>
          </div>
        </article>

        <!-- Card 2 -->
        <article class="capability-card">
          <div class="capability-top">
            <span class="capability-tag">Studi Tematik Unggulan</span>
            <h3 class="capability-title">Penuaan Penduduk &amp; Perawatan Lansia</h3>
            <p class="capability-desc">
              Pusat keunggulan riset demografi penuaan (aging studies) di Asia Tenggara, menginisiasi model perawatan jangka panjang (Long-Term Care) dan Community Care Hub.
            </p>
            <ul class="capability-bullets">
              <li>Inisiator Indonesia Longitudinal Aging Survey (ILAS) bersama Asian Development Bank (ADB).</li>
              <li>Perancangan dan pengujian uji coba Community Care Hub (CCH) terpadu di Bali dan D.I. Yogyakarta.</li>
              <li>Penyusunan naskah kebijakan perlindungan sosial dan partisipasi ekonomi produktif lanjut usia.</li>
            </ul>
          </div>
          <div class="capability-footer">
            <span class="card-link" onclick="openDataModal('Riset Penuaan Penduduk')">Pelajari Inisiatif CCH &rarr;</span>
          </div>
        </article>

        <!-- Card 3 -->
        <article class="capability-card">
          <div class="capability-top">
            <span class="capability-tag">Uji Dampak Terukur</span>
            <h3 class="capability-title">Evaluasi Kebijakan Publik &amp; Sosial</h3>
            <p class="capability-desc">
              Mengukur efektivitas dan dampak intervensi program pemerintah, penanggulangan kemiskinan, reformasi jaminan kesehatan, dan ketahanan iklim daerah kepulauan.
            </p>
            <ul class="capability-bullets">
              <li>Metode Randomized Controlled Trials (RCT) dan Quasi-Experimental Evaluation bekerja sama dengan J-PAL.</li>
              <li>Analisis efisiensi bantuan sosial, perlindungan ibu dan anak, serta pencegahan stunting.</li>
              <li>Penyusunan Policy Brief ringkas dengan rekomendasi berbasis data kuantitatif dan kualitatif.</li>
            </ul>
          </div>
          <div class="capability-footer">
            <span class="card-link" onclick="openDataModal('Evaluasi Kebijakan')">Konsultasi Evaluasi Program &rarr;</span>
          </div>
        </article>

        <!-- Card 4 -->
        <article class="capability-card">
          <div class="capability-top">
            <span class="capability-tag">Kapasitas Statistik</span>
            <h3 class="capability-title">Sistem Integrasi Data Daerah &amp; Pelatihan</h3>
            <p class="capability-desc">
              Membangun kemandirian data pemerintah daerah dan desa melalui pelatihan kader, standardisasi basis data mikro, dan instrumen pendataan terintegrasi.
            </p>
            <ul class="capability-bullets">
              <li>Program pendampingan sistem integrasi data desa/kelurahan seperti SiTEPAT RAMAH.</li>
              <li>Pelatihan intensif enumerator, pengawas lapangan, dan koordinator data lokal.</li>
              <li>Validasi silang data kependudukan mikro untuk ketepatan sasaran bansos daerah.</li>
            </ul>
          </div>
          <div class="capability-footer">
            <span class="card-link" onclick="openDataModal('Pelatihan & Integrasi Data')">Program Pelatihan Kader &rarr;</span>
          </div>
        </article>
      </div>
    </div>
  </section>

  <!-- Data Publik Hub (Interactive Dataset Catalog - Osome Product Showcase Style) -->
  <section class="data-portal-section" id="data-publik">
    <div class="container">
      <div class="data-portal-box">
        <div class="data-portal-header">
          <div>
            <span class="section-kicker">Katalog Repositori Terbuka</span>
            <h2 class="section-title" style="margin-bottom: 8px;">Portal <em>Data Publik</em> SurveyMETER</h2>
            <p class="section-subtitle">
              Akses dataset survei sekunder, kuesioner resmi, dan kamus data untuk keperluan riset ilmiah, tesis, dan analisis kebijakan publik.
            </p>
          </div>
          <div class="data-search-wrapper">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="color: var(--text-light);"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
            <input type="text" id="datasetSearchInput" class="data-search-input" placeholder="Cari dataset, topik, atau tahun..." oninput="filterDatasets()">
          </div>
        </div>

        <div class="dataset-grid" id="datasetGrid">
          <!-- Dataset 1 -->
          <div class="dataset-card" data-title="ifls east indonesia timur rumah tangga">
            <div>
              <div class="dataset-badge-row">
                <span class="dataset-status">Tersedia untuk Peneliti</span>
                <span class="dataset-year">Publikasi 2019</span>
              </div>
              <h4 class="dataset-name">Survei Aspek Kehidupan Rumah Tangga Indonesia Timur (IFLS East)</h4>
              <p class="dataset-snippet">
                Survei kondisi kehidupan rumah tangga dan komunitas multi-topik berskala besar yang mencakup provinsi-provinsi di kawasan timur Indonesia.
              </p>
            </div>
            <div>
              <div class="dataset-meta">
                <div class="dataset-meta-item"><span>Cakupan:</span> <strong>7 Provinsi Timur</strong></div>
                <div class="dataset-meta-item"><span>Format:</span> <strong>STATA (.dta) / SPSS</strong></div>
                <div class="dataset-meta-item"><span>Akses:</span> <strong>Terbuka (Registrasi)</strong></div>
              </div>
              <div class="dataset-actions">
                <button class="btn btn-dataset btn-dataset-primary" onclick="openDataModal('IFLS East')">Unduh Metadata</button>
                <button class="btn btn-dataset btn-dataset-outline" onclick="openDataModal('IFLS East (Data Penuh)')">Minta Akses</button>
              </div>
            </div>
          </div>

          <!-- Dataset 2 -->
          <div class="dataset-card" data-title="ilas 2023 indonesia longitudinal aging survey lansia adb">
            <div>
              <div class="dataset-badge-row">
                <span class="dataset-status">Dataset Unggulan Baru</span>
                <span class="dataset-year">Rilis 2024</span>
              </div>
              <h4 class="dataset-name">Indonesia Longitudinal Aging Survey (ILAS) 2023</h4>
              <p class="dataset-snippet">
                Data komprehensif penuaan penduduk: kesehatan fisik-mental, jejaring dukungan keluarga, kesiapan ekonomi, dan perlindungan jangka panjang lansia bekerja sama dengan Asian Development Bank (ADB).
              </p>
            </div>
            <div>
              <div class="dataset-meta">
                <div class="dataset-meta-item"><span>Sampel:</span> <strong>Lansia &amp; Pengasuh</strong></div>
                <div class="dataset-meta-item"><span>Kemitraan:</span> <strong>ADB &amp; Bappenas</strong></div>
                <div class="dataset-meta-item"><span>Format:</span> <strong>Kuesioner &amp; Dataset</strong></div>
              </div>
              <div class="dataset-actions">
                <button class="btn btn-dataset btn-dataset-primary" onclick="openDataModal('ILAS 2023')">Unduh Codebook</button>
                <button class="btn btn-dataset btn-dataset-outline" onclick="openDataModal('ILAS 2023 (Dataset Lengkap)')">Minta Akses</button>
              </div>
            </div>
          </div>

          <!-- Dataset 3 -->
          <div class="dataset-card" data-title="tsunami aceh pemulihan bencana longitudinal star">
            <div>
              <div class="dataset-badge-row">
                <span class="dataset-status">Arsip Longitudinal</span>
                <span class="dataset-year">Long-term Panel</span>
              </div>
              <h4 class="dataset-name">Studi Tahap Pemulihan Wilayah Pasca Tsunami Aceh</h4>
              <p class="dataset-snippet">
                Survei longitudinal multi-putaran untuk mengukur dampak jangka panjang rekonstruksi sosial, perumahan, pemulihan ekonomi, dan ketahanan psikososial pasca bencana tsunami Aceh.
              </p>
            </div>
            <div>
              <div class="dataset-meta">
                <div class="dataset-meta-item"><span>Fokus:</span> <strong>Rekonstruksi &amp; Dampak</strong></div>
                <div class="dataset-meta-item"><span>Kolaborasi:</span> <strong>Duke &amp; World Bank</strong></div>
                <div class="dataset-meta-item"><span>Status:</span> <strong>Katalog Terverifikasi</strong></div>
              </div>
              <div class="dataset-actions">
                <button class="btn btn-dataset btn-dataset-primary" onclick="openDataModal('Studi Tsunami Aceh')">Unduh Laporan</button>
                <button class="btn btn-dataset btn-dataset-outline" onclick="openDataModal('Studi Aceh (Dataset)')">Minta Akses</button>
              </div>
            </div>
          </div>
        </div>

        <div style="text-align: center; padding-top: 10px;">
          <p style="font-size: 0.875rem; color: var(--text-muted); margin-bottom: 12px;">
            Memerlukan dataset spesifik atau data mikro khusus untuk riset kolaboratif?
          </p>
          <button class="btn btn-secondary btn-sm" onclick="openDataModal('Permohonan Dataset Kustom')">
            Kirim Pengajuan Kustom ke Tim Manajemen Data &rarr;
          </button>
        </div>
      </div>
    </div>
  </section>

  <!-- Publications & Policy Briefs Section -->
  <section class="publications-section" id="publikasi">
    <div class="container">
      <div class="section-header">
        <span class="section-kicker">Diseminasi Hasil Riset</span>
        <h2 class="section-title">Publikasi Akademik &amp; <em>Naskah Kebijakan</em></h2>
        <p class="section-subtitle">
          Temuan empiris tim peneliti SurveyMETER yang diterbitkan di jurnal internasional terindeks, buku rujukan kebijakan, dan seri laporan kerja sama donor.
        </p>
      </div>

      <div class="pub-tabs">
        <button class="pub-tab-btn active" onclick="filterPubs('all', this)">Semua Publikasi</button>
        <button class="pub-tab-btn" onclick="filterPubs('aging', this)">Penuaan &amp; Demografi</button>
        <button class="pub-tab-btn" onclick="filterPubs('health', this)">Kesehatan &amp; Sosial</button>
        <button class="pub-tab-btn" onclick="filterPubs('economy', this)">Ekonomi &amp; Wilayah</button>
      </div>

      <div class="pub-grid">
        <!-- Pub 1 -->
        <article class="pub-card" data-category="health">
          <div class="pub-cover-wrap">
            <img src="{pub_repro}" alt="Perceptions of Adolescents Sexual and Reproductive Health">
          </div>
          <div class="pub-body">
            <div>
              <div class="pub-date">14 Oktober 2024</div>
              <h4 class="pub-title">Studi Kualitatif Persepsi Pendidikan Seks &amp; Kesehatan Reproduksi Remaja di Yogyakarta</h4>
              <p class="pub-meta">Peneliti: Sikoki, Larastiti, Suriastini, Pujiastuti. Menelaah kesenjangan pemahaman dan akses konseling reproduksi remaja di tingkat komunitas sekolah dan keluarga.</p>
            </div>
            <a href="javascript:void(0)" onclick="openDataModal('Publikasi: Kesehatan Reproduksi Remaja')" class="pub-download-link">
              Lihat Ringkasan Eksekutif &rarr;
            </a>
          </div>
        </article>

        <!-- Pub 2 -->
        <article class="pub-card" data-category="economy">
          <div class="pub-cover-wrap">
            <img src="{pub_irsa}" alt="COVID-19 Disruption and Regional Development">
          </div>
          <div class="pub-body">
            <div>
              <div class="pub-date">17 Juli 2024</div>
              <h4 class="pub-title">COVID-19 Disruption and Regional Development in Small Island Economies</h4>
              <p class="pub-meta">Konferensi Internasional IRSA 2024. Analisis pemulihan ekonomi wilayah kepulauan kecil di Indonesia pasca guncangan pandemi.</p>
            </div>
            <a href="javascript:void(0)" onclick="openDataModal('Publikasi: IRSA Small Island Economies')" class="pub-download-link">
              Lihat Ringkasan Eksekutif &rarr;
            </a>
          </div>
        </article>

        <!-- Pub 3 -->
        <article class="pub-card" data-category="aging">
          <div class="pub-cover-wrap">
            <img src="{pub_adb_aging}" alt="Asian Development Policy Report 2024">
          </div>
          <div class="pub-body">
            <div>
              <div class="pub-date">15 Mei 2024</div>
              <h4 class="pub-title">Aging Well in Asia: Asian Development Policy Report 2024</h4>
              <p class="pub-meta">Bekerja sama dengan Asian Development Bank (ADB). Laporan kebijakan regional terkait strategi kesiapan perlindungan sosial menghadapi lonjakan populasi lanjut usia.</p>
            </div>
            <a href="javascript:void(0)" onclick="openDataModal('Publikasi: Aging Well in Asia (ADB)')" class="pub-download-link">
              Lihat Ringkasan Eksekutif &rarr;
            </a>
          </div>
        </article>

        <!-- Pub 4 -->
        <article class="pub-card" data-category="aging">
          <div class="pub-cover-wrap">
            <img src="{pub_nbs}" alt="Enhancing Decent Work in Nature-based Solutions">
          </div>
          <div class="pub-body">
            <div>
              <div class="pub-date">31 Mei 2024</div>
              <h4 class="pub-title">Mengangkat Kerja Layak bagi Lanjut Usia dalam Solusi Berbasis Alam di Indonesia</h4>
              <p class="pub-meta">Kajian potensi pekerjaan layak dan partisipasi ekonomi inklusif bagi kelompok usia lanjut di sektor restorasi ekosistem pedesaan.</p>
            </div>
            <a href="javascript:void(0)" onclick="openDataModal('Publikasi: Kerja Layak Lansia')" class="pub-download-link">
              Lihat Ringkasan Eksekutif &rarr;
            </a>
          </div>
        </article>

        <!-- Pub 5 -->
        <article class="pub-card" data-category="economy">
          <div class="pub-cover-wrap">
            <img src="{pub_aceh}" alt="Sustainability Report Aceh Tsunami Recovery">
          </div>
          <div class="pub-body">
            <div>
              <div class="pub-date">18 Desember 2023</div>
              <h4 class="pub-title">Mengukur Pemulihan Bencana: Pelajaran Tahap Awal Wilayah Pasca Tsunami Aceh</h4>
              <p class="pub-meta">Jurnal Sustainability. Evaluasi efektivitas bantuan perumahan dan rekonstruksi infrastruktur dasar dalam memulihkan penghidupan masyarakat pesisir.</p>
            </div>
            <a href="javascript:void(0)" onclick="openDataModal('Publikasi: Evaluasi Pemulihan Bencana Aceh')" class="pub-download-link">
              Lihat Ringkasan Eksekutif &rarr;
            </a>
          </div>
        </article>

        <!-- Pub 6 -->
        <article class="pub-card" data-category="health">
          <div class="pub-cover-wrap" style="background: #E8F0EA;">
            <div style="text-align: center; padding: 20px;">
              <div style="font-size: 0.8rem; font-weight: 700; color: var(--brand-green); margin-bottom: 6px;">POLICY PAPER</div>
              <div style="font-size: 1.1rem; font-weight: 800; color: var(--text-main);">Gerakan Jogja Sapa Lansia</div>
              <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 8px;">Dinsosnakertrans Kota Yogyakarta</div>
            </div>
          </div>
          <div class="pub-body">
            <div>
              <div class="pub-date">04 Oktober 2024</div>
              <h4 class="pub-title">Pedoman Operasional Gerakan Jogja Sapa Lansia Dinsosnakertrans</h4>
              <p class="pub-meta">Pendampingan perumusan panduan intervensi kunjungan sosial, skrining kesehatan mandiri lansia, dan aktivasi kader peduli lansia di Kota Yogyakarta.</p>
            </div>
            <a href="javascript:void(0)" onclick="openDataModal('Publikasi: Pedoman Jogja Sapa Lansia')" class="pub-download-link">
              Lihat Ringkasan Eksekutif &rarr;
            </a>
          </div>
        </article>
      </div>
    </div>
  </section>

  <!-- Rigor & Field Protocols (Osome "What sets us apart" Style) -->
  <section class="rigor-section" id="metodologi">
    <div class="container">
      <div class="section-header">
        <span class="section-kicker">Integritas Metodologi</span>
        <h2 class="section-title">Standar Kualitas Data <em>Tanpa Kompromi</em></h2>
        <p class="section-subtitle">
          Integritas temuan kebijakan bertumpu pada kualitas data mentah di lapangan. Kami menerapkan protokol kendali mutu berlapis di setiap tahapan pendataan.
        </p>
      </div>

      <div class="rigor-grid">
        <div class="rigor-box">
          <span class="rigor-num">01</span>
          <h3 class="rigor-title">Verifikasi Bertingkat 100% Real-Time</h3>
          <p class="rigor-desc">
            Setiap kuesioner yang diisi enumerator diperiksa silang oleh pengawas tim di hari yang sama melalui Computer-Assisted Personal Interviewing (CAPI) dengan deteksi anomali otomatis.
          </p>
        </div>

        <div class="rigor-box">
          <span class="rigor-num">02</span>
          <h3 class="rigor-title">Audit Geotagging &amp; Kunjungan Ulang</h3>
          <p class="rigor-desc">
            Verifikasi fisik lokasi responden dengan koordinat GPS dan re-interview acak independen (back-check) sebesar 10-15% dari total sampel guna mencegah fabrikasi jawaban.
          </p>
        </div>

        <div class="rigor-box">
          <span class="rigor-num">03</span>
          <h3 class="rigor-title">Kepatuhan Etik &amp; Kerahasiaan Responden</h3>
          <p class="rigor-desc">
            Persetujuan tindakan medis/survei (informed consent) terstandarisasi, anonimisasi identitas, dan enkripsi data berlapis sesuai etika penelitian nasional dan internasional.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- About & Leadership Section -->
  <section class="about-section" id="profil">
    <div class="container">
      <div class="about-layout">
        <div class="about-text">
          <span class="section-kicker">Tentang Lembaga</span>
          <h3>Dua Dekade Menjembatani <em>Data Lapangan</em> dan Kebijakan Publik</h3>
          <p>
            SurveyMETER didirikan pada tanggal 20 Februari 2002 di Yogyakarta sebagai yayasan penelitian yang awalnya meresmikan hubungan kerja staf peneliti yang telah berpengalaman lebih dari 15 tahun mengumpulkan data Indonesia Family Life Survey (IFLS) bersama RAND Corporation.
          </p>
          <p>
            Pada tahun 2011, lembaga menguatkan komitmen pada pendampingan advokasi kebijakan sosial. Sejak 2020, bertransformasi menjadi PT SurveyMETER guna memperluas jangkauan kolaborasi profesional internasional dengan tetap memegang teguh independensi ilmiah.
          </p>
          <p>
            Kiprah lembaga dipimpin berturut-turut oleh Bondan S. Sikoki (2002-2012), Dr. Ir. Ni Wayan Suriastini, M.Phil (2012-2024), dan kini dipimpin oleh <strong>Dr. Cecep Sukria Sumantri</strong> sebagai Direktur Eksekutif.
          </p>
          <div style="margin-top: 28px;">
            <button class="btn btn-primary" onclick="openDataModal('Profil Lembaga & Kolaborasi')">
              Jajaki Kolaborasi Penelitian &rarr;
            </button>
          </div>
        </div>

        <div class="about-timeline">
          <div class="timeline-item">
            <span class="timeline-node"></span>
            <div class="timeline-year">2002</div>
            <div class="timeline-title">Pendirian SurveyMETER di Yogyakarta</div>
            <div class="timeline-desc">Merangkul para staf peneliti berpengalaman IFLS RAND untuk menyediakan data primer berkualitas tinggi bagi kebijakan publik Indonesia.</div>
          </div>
          <div class="timeline-item">
            <span class="timeline-node"></span>
            <div class="timeline-year">2011</div>
            <div class="timeline-title">Transformasi Lembaga Penelitian &amp; Advokasi</div>
            <div class="timeline-desc">Fokus diperluas mencakup evaluasi program pemerintah, perlindungan lansia, dan perbaikan gizi masyarakat bersama kementerian terkait.</div>
          </div>
          <div class="timeline-item">
            <span class="timeline-node"></span>
            <div class="timeline-year">2020</div>
            <div class="timeline-title">PT SurveyMETER &amp; Ekspansi Global</div>
            <div class="timeline-desc">Penguatan tata kelola profesional dan peluncuran riset longitudinal penuaan (ILAS) bekerja sama erat dengan Asian Development Bank.</div>
          </div>
          <div class="timeline-item">
            <span class="timeline-node"></span>
            <div class="timeline-year">2024 - Sekarang</div>
            <div class="timeline-title">Era Kepemimpinan Baru &amp; Repositori Digital</div>
            <div class="timeline-desc">Di bawah Dr. Cecep Sukria Sumantri, SurveyMETER mempercepat modernisasi diseminasi data publik dan asistensi sistem data daerah.</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA Banner Section -->
  <section class="cta-strip">
    <div class="container">
      <h2>Mulai Riset Berkualitas Bersama <em>SurveyMETER</em></h2>
      <p>
        Apakah institusi Anda membutuhkan desain survei sampel acak berskala nasional, pengumpulan data lapangan dengan kendali mutu ketat, atau analisis kebijakan publik berbasis bukti?
      </p>
      <div class="cta-strip-actions">
        <button class="btn btn-light" onclick="openDataModal('Konsultasi Kemitraan Baru')">
          Hubungi Tim Peneliti &rarr;
        </button>
        <a href="#data-publik" class="btn btn-ghost-light">
          Jelajahi Data Publik
        </a>
      </div>
    </div>
  </section>

  <!-- Site Footer -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-col">
          <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 16px;">
            <svg width="240" height="48" viewBox="0 0 240 48" fill="none" xmlns="http://www.w3.org/2000/svg" style="display: block;">
  <!-- Emblem: Dynamic scientific measurement swirl -->
  <g transform="translate(4, 2)">
    <circle cx="22" cy="22" r="20" fill="#EBF7EE" stroke="#C2E7CA" stroke-width="1.2"/>
    <!-- Swirl Arcs -->
    <path d="M 12 28 C 10 18, 18 10, 28 10 C 33 10, 37 13, 39 17 C 35 15, 30 14, 25 16 C 18 19, 15 25, 17 31 C 18 33, 20 35, 22 36 C 18 35, 14 32, 12 28 Z" fill="#34D399"/>
    <path d="M 15 22 C 16 15, 23 11, 30 13 C 35 15, 38 19, 38 24 C 36 21, 32 18, 27 18 C 21 18, 18 22, 19 27 C 20 30, 23 32, 26 33 C 21 32, 17 28, 15 22 Z" fill="#16A34A"/>
    <path d="M 22 17 C 25 15, 30 16, 33 19 C 35 22, 35 26, 32 29 C 30 31, 26 31, 23 29 C 21 27, 21 24, 23 21 C 24 19, 27 18, 29 19 C 27 21, 25 24, 26 26 C 27 27, 29 27, 30 26 C 31 24, 30 22, 28 20 C 26 19, 23 18, 22 17 Z" fill="#34D399"/>
    <circle cx="22" cy="22" r="3.2" fill="#34D399"/>
  </g>
  <!-- Wordmark -->
  <text x="56" y="27" font-family="'Plus Jakarta Sans', Georgia, serif" font-size="20" font-weight="700" fill="#34D399" letter-spacing="-0.02em">Survey<tspan font-weight="800" fill="#FFFFFF">METER</tspan></text>
  <text x="57" y="38" font-family="'Plus Jakarta Sans', -apple-system, sans-serif" font-size="6.5" font-weight="700" fill="#9BA8A1" letter-spacing="0.14em">SURVEY • MEASUREMENT • TRAINING • RESEARCH</text>
</svg>
          </div>
          <p>
            Survey, Measurement, Training and Research. Lembaga penelitian independen di Yogyakarta yang berdedikasi menyediakan informasi akurat dan data terpercaya bagi kebijakan publik yang sehat dan berkelanjutan.
          </p>
          <p style="font-size: 0.8rem; color: #73827A;">
            Badan Hukum: Terdaftar Kemenkumham RI.
          </p>
        </div>

        <div class="footer-col">
          <h4>Fokus &amp; Program</h4>
          <ul class="footer-links">
            <li><a href="#fokus">Survei Longitudinal</a></li>
            <li><a href="#fokus">Kajian Penuaan &amp; CCH</a></li>
            <li><a href="#fokus">Evaluasi Kebijakan Publik</a></li>
            <li><a href="#fokus">Integrasi Data Desa</a></li>
            <li><a href="#data-publik">IFLS East &amp; ILAS</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Tautan Cepat</h4>
          <ul class="footer-links">
            <li><a href="#profil">Tentang SurveyMETER</a></li>
            <li><a href="#publikasi">Publikasi &amp; Policy Brief</a></li>
            <li><a href="#metodologi">Protokol Kendali Mutu</a></li>
            <li><a href="javascript:void(0)" onclick="openDataModal('Karir & Rekrutmen Enumerator')">Peluang Enumerator</a></li>
            <li><a href="#data-publik">Permohonan Data Sekunder</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Kantor Utama Yogyakarta</h4>
          <div class="footer-contact-item">
            <strong>Alamat:</strong>
            Jl. Jenengan Raya No. 109, Maguwoharjo, Depok, Sleman, D.I. Yogyakarta 55282
          </div>
          <div class="footer-contact-item">
            <strong>Telepon &amp; Fax:</strong>
            Tel: +62 274 4477-464 | Fax: +62 274 4477-004
          </div>
          <div class="footer-contact-item">
            <strong>Surat Elektronik:</strong>
            sm@surveymeter.org
          </div>
        </div>
      </div>

      <div class="footer-bottom">
        <div>
          &copy; 2026 PT SurveyMETER. Seluruh hak cipta dilindungi undang-undang.
        </div>
        <div class="footer-socials">
          <a href="https://twitter.com/SurveyMETER_Id" target="_blank" rel="noopener">Twitter / X</a>
          <a href="https://www.facebook.com/Surveymeter/" target="_blank" rel="noopener">Facebook</a>
          <a href="https://surveymeter.org" target="_blank" rel="noopener">Arsip Web Drupal</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- Modal: Data Request & Collaboration Inquiry -->
  <div class="modal-overlay" id="dataModalOverlay" onclick="closeDataModal(event)">
    <div class="modal-box" onclick="event.stopPropagation()">
      <button class="modal-close-btn" onclick="closeDataModal()">&times;</button>
      <h3 class="modal-title" id="modalTitleText">Permohonan Akses Data</h3>
      <p class="modal-desc" id="modalDescText">
        Silakan isi data institusi dan tujuan penggunaan data atau kebutuhan riset Anda. Tim manajemen data SurveyMETER akan merespons dalam 1x24 jam kerja.
      </p>

      <form id="dataRequestForm" onsubmit="submitDataRequest(event)">
        <div class="form-group">
          <label class="form-label">Nama Lengkap</label>
          <input type="text" class="form-input" id="reqName" placeholder="Contoh: Budi Santoso" required>
        </div>

        <div class="form-group">
          <label class="form-label">Institusi / Universitas / Kementerian</label>
          <input type="text" class="form-input" id="reqOrg" placeholder="Contoh: Universitas Gadjah Mada / Bappenas" required>
        </div>

        <div class="form-group">
          <label class="form-label">Email Kerja / Akademik</label>
          <input type="email" class="form-input" id="reqEmail" placeholder="nama@instansi.ac.id" required>
        </div>

        <div class="form-group">
          <label class="form-label">Dataset / Topik yang Diajukan</label>
          <input type="text" class="form-input" id="reqSubject" value="Dataset SurveyMETER" required>
        </div>

        <div class="form-group">
          <label class="form-label">Ringkasan Tujuan Riset</label>
          <textarea class="form-textarea" id="reqNotes" placeholder="Tuliskan secara ringkas tujuan penggunaan data atau lingkup kerja sama yang direncanakan..." required></textarea>
        </div>

        <button type="submit" class="btn btn-primary modal-submit-btn">
          Kirimkan Permohonan Data &rarr;
        </button>
      </form>

      <div class="form-success-msg" id="formSuccessMsg">
        Permohonan Anda berhasil dikirim. Tim sekretariat SurveyMETER akan menghubungi Anda melalui email yang terdaftar.
      </div>
    </div>
  </div>

  <script>
    // Dataset Search / Filtering
    function filterDatasets() {{
      const query = document.getElementById('datasetSearchInput').value.toLowerCase();
      const cards = document.querySelectorAll('.dataset-card');
      cards.forEach(card => {{
        const title = card.getAttribute('data-title') || '';
        const text = card.innerText.toLowerCase();
        if (title.includes(query) || text.includes(query)) {{
          card.style.display = 'flex';
        }} else {{
          card.style.display = 'none';
        }}
      }});
    }}

    // Publication Category Filtering
    function filterPubs(cat, btn) {{
      document.querySelectorAll('.pub-tab-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const cards = document.querySelectorAll('.pub-card');
      cards.forEach(card => {{
        const cardCat = card.getAttribute('data-category');
        if (cat === 'all' || cardCat === cat) {{
          card.style.display = 'flex';
        }} else {{
          card.style.display = 'none';
        }}
      }});
    }}

    // Modal Control
    function openDataModal(contextTitle) {{
      const overlay = document.getElementById('dataModalOverlay');
      const subjectInput = document.getElementById('reqSubject');
      const modalTitle = document.getElementById('modalTitleText');
      
      if (contextTitle) {{
        subjectInput.value = contextTitle;
        modalTitle.innerText = contextTitle;
      }}
      
      document.getElementById('dataRequestForm').style.display = 'block';
      document.getElementById('formSuccessMsg').style.display = 'none';
      overlay.classList.add('active');
    }}

    function closeDataModal(e) {{
      document.getElementById('dataModalOverlay').classList.remove('active');
    }}

    function submitDataRequest(e) {{
      e.preventDefault();
      document.getElementById('dataRequestForm').style.display = 'none';
      document.getElementById('formSuccessMsg').style.display = 'block';
      setTimeout(() => {{
        closeDataModal();
      }}, 3000);
    }}

    function toggleMobileMenu() {{
      const navLinks = document.querySelector('.nav-links');
      if (navLinks.style.display === 'flex') {{
        navLinks.style.display = 'none';
      }} else {{
        navLinks.style.display = 'flex';
        navLinks.style.flexDirection = 'column';
        navLinks.style.position = 'absolute';
        navLinks.style.top = '72px';
        navLinks.style.left = '0';
        navLinks.style.right = '0';
        navLinks.style.background = '#FAF8F5';
        navLinks.style.padding = '20px';
        navLinks.style.borderBottom = '1px solid #E6E1D8';
        navLinks.style.boxShadow = '0 10px 20px rgba(0,0,0,0.05)';
      }}
    }}
  </script>
</body>
</html>
"""

with open('/Users/user/Documents/surveymeter-redesign/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated /Users/user/Documents/surveymeter-redesign/index.html successfully!")
