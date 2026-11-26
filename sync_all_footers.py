import os
from bs4 import BeautifulSoup

TG_ICON = '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/></svg>'

FOOTER_RU = f"""
<div class="container" style="display: flex; flex-direction: column; align-items: center; text-align: center;">
    <p>&copy; 2026 Crypto AI Hub. Все права защищены.</p>
    <p class="footer-note">Контент на сайте носит информационный характер и не является финансовой рекомендацией.</p>
    <a href="https://t.me" target="_blank" rel="noopener noreferrer" class="footer-tg-btn">
        {TG_ICON}
        Наш Telegram-канал
    </a>
</div>
"""

FOOTER_EN = f"""
<div class="container" style="display: flex; flex-direction: column; align-items: center; text-align: center;">
    <p>&copy; 2026 Crypto AI Hub. All rights reserved.</p>
    <p class="footer-note">Content is for informational purposes only and does not constitute financial advice.</p>
    <a href="https://t.me" target="_blank" rel="noopener noreferrer" class="footer-tg-btn">
        {TG_ICON}
        Join our Telegram Channel
    </a>
</div>
"""

count = 0
for root, _, files in os.walk("."):
    if ".git" in root:
        continue
    is_en = "en" in os.path.normpath(root).split(os.sep)
    for fname in files:
        if not fname.endswith(".html"):
            continue
        fpath = os.path.join(root, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")

        footer = soup.find("footer")
        if footer:
            footer["class"] = "footer"
            footer.clear()
            footer.append(BeautifulSoup(FOOTER_EN if is_en else FOOTER_RU, "html.parser"))
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(str(soup))
            count += 1

print(f"✅ Единый стандартный подвал с кнопкой Telegram прошит в {count} страницах!")
