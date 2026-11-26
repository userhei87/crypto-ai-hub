import os
import logging
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
EN_DIR = os.path.join(PROJECT_DIR, "en")
EN_GUIDES_DIR = os.path.join(EN_DIR, "guides")


def inject_wotd_link(filepath, wotd_href):
    if not os.path.exists(filepath):
        return
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    nav = soup.find("nav", class_="nav-links")
    if nav and not nav.find("a", href=wotd_href):
        news_link = nav.find("a", href=lambda h: h and "news.html" in h)
        wotd_tag = soup.new_tag("a", href=wotd_href, attrs={"class": "nav-link"})
        wotd_tag.string = "WOTD Answers"
        if news_link:
            news_link.insert_before(wotd_tag)
        else:
            nav.append(wotd_tag)

    # Для en/wotd.html добавляем скрипт открытия кнопки Menu
    if os.path.basename(filepath) == "wotd.html":
        body = soup.find("body")
        if body and not body.find("script", id="mobile-menu-script"):
            menu_script = soup.new_tag("script", id="mobile-menu-script")
            menu_script.string = (
                "document.addEventListener('DOMContentLoaded', () => { "
                "const toggle = document.querySelector('button.menu-toggle'); "
                "const navEl = document.querySelector('.nav-links'); "
                "if (toggle && navEl) { "
                "toggle.addEventListener('click', () => { "
                "navEl.classList.toggle('open'); "
                "toggle.textContent = navEl.classList.contains('open') ? '✕ Menu' : 'Menu'; "
                "}); } });"
            )
            body.append(menu_script)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(str(soup))
    logging.info(f"✅ Обновлено меню в: {os.path.relpath(filepath, PROJECT_DIR)}")


def main():
    # 1. Корневые страницы в /en/
    en_root_pages = ["index.html", "wotd.html", "prompts.html", "calculator.html", "news.html", "partners.html", "disclaimer.html"]
    for page in en_root_pages:
        inject_wotd_link(os.path.join(EN_DIR, page), "wotd.html")

    # 2. Все переведённые гайды в /en/guides/
    if os.path.exists(EN_GUIDES_DIR):
        for fname in sorted(os.listdir(EN_GUIDES_DIR)):
            if fname.endswith(".html"):
                inject_wotd_link(os.path.join(EN_GUIDES_DIR, fname), "../wotd.html")


if __name__ == "__main__":
    main()
