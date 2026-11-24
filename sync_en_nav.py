import os
from bs4 import BeautifulSoup

CYBER_ICONS = {
    "prompts": '<svg class="cyber-icon cyan" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="16" height="16" rx="2"/><path d="M9 9h6"/><path d="M9 13l2 2-2 2"/><path d="M13 17h3"/><path d="M9 1v3M15 1v3M9 20v3M15 20v3M1 9h3M1 15h3M20 9h3M20 15h3"/></svg>',
    "calc": '<svg class="cyber-icon gold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="2"/><line x1="8" y1="6" x2="16" y2="6"/><line x1="8" y1="11" x2="8.01" y2="11"/><line x1="12" y1="11" x2="12.01" y2="11"/><line x1="16" y1="11" x2="16.01" y2="11"/><line x1="8" y1="15" x2="8.01" y2="15"/><line x1="12" y1="15" x2="12.01" y2="15"/><path d="M16 15v4"/></svg>'
}

count = 0
for root, dirs, files in os.walk("en"):
    for file in files:
        if not file.endswith(".html"):
            continue
        path = os.path.join(root, file)
        is_guide = "guides" in os.path.normpath(root).split(os.sep)
        prefix = "../" if is_guide else ""

        with open(path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")

        nav = soup.find("nav", class_="nav-links")
        if nav:
            nav.clear()
            nav_html = f"""
                <a href="/en/" class="nav-link">Home</a>
                <a href="/en/#guides-section" class="nav-link">Guides</a>
                <div class="dropdown">
                    <a href="#" class="nav-link">Tools ▾</a>
                    <div class="dropdown-content">
                        <a href="{prefix}prompts.html">{CYBER_ICONS['prompts']}AI Prompt Library</a>
                        <a href="{prefix}calculator.html">{CYBER_ICONS['calc']}Crypto Calculators</a>
                    </div>
                </div>
                <a href="{prefix}news.html" class="nav-link">News</a>
                <a href="{prefix}partners.html" class="nav-link">Free Crypto</a>
                <a href="{prefix}disclaimer.html" class="nav-link">Disclaimer</a>
            """
            nav.append(BeautifulSoup(nav_html, "html.parser"))
            with open(path, "w", encoding="utf-8") as f:
                f.write(str(soup))
            count += 1

print(f"✅ Единое английское меню (с Disclaimer и Free Crypto) прошито в {count} файлах!")
