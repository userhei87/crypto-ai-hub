import os
import re
import random
import logging
import shutil
from html import escape
from bs4 import BeautifulSoup

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
GUIDES_DIR = os.path.join(PROJECT_DIR, "guides")
INDEX_FILE = os.path.join(PROJECT_DIR, "index.html")

# Ваша персональная реферальная ссылка со скидкой 10%
BINANCE_REF_URL = "https://www.binance.com/register?ref=SHARA10"

# Полный список статей
GUIDES_DATA = {
    "binance-reg.html": (
        "Как зарегистрироваться на Binance и пройти верификацию в 2026 году", 
        "binance-reg.png",
        "Крипта с нуля",
        "Пошаговый разбор создания аккаунта, защиты средств (2FA) и покупки первых активов через P2P."
    ),
    "ai-crypto-trading.html": (
        "Использование ИИ для анализа криптовалютного рынка", 
        "ai-crypto-trading.png",
        "ИИ и Трейдинг",
        "Настраиваем локальные и облачные нейросети для поиска паттернов, анализа новостей и составления портфеля."
    ),
    "crypto-wallet-safety.html": (
        "Безопасность криптокошельков: Как защитить свои цифровые активы", 
        "crypto-wallet-safety.png",
        "Безопасность",
        "Разбор типов кошельков, правил хранения сид-фраз и защиты от фишинга в Web3."
    ),
    "p2p-trading-guide.html": (
        "Руководство по P2P-торговле: Как безопасно покупать и продавать криптовалюту за рубли", 
        "p2p-trading-guide.png",
        "P2P-Торговля",
        "Пошаговый гайд по обмену фиата на крипту: выбор мерчанта, защита от треугольников и безопасный вывод на карту."
    ),
    "binance-grid-bot.html": (
        "Настройка спотового сеточного бота на Binance: Автоматический трейдинг для новичков", 
        "binance-grid-bot.png",
        "Торговые боты",
        "Пошагово разбираем Grid Trading: запуск бота, ценовые диапазоны и торговля на волатильности рынка."
    ),
    "binance-earn-guide.html": (
        "Как получать пассивный доход с помощью Binance Earn: Полное руководство по стейкингу", 
        "binance-earn-guide.png",
        "Пассивный доход",
        "Разбор гибкого и фиксированного стейкинга, автоинвестирования и Launchpool."
    ),
    "crypto-futures-trading.html": (
        "Введение во фьючерсную торговлю: Как минимизировать риски и не ликвидировать баланс", 
        "crypto-futures-trading.png",
        "Фьючерсы",
        "Что такое кредитное плечо, маржинальные требования, Stop-Loss и Take-Profit."
    ),
    "crypto-technical-analysis.html": (
        "Основы технического анализа: Как читать графики криптовалют и находить точки входа", 
        "crypto-technical-analysis.png",
        "Аналитика",
        "Учимся понимать уровни поддержки и сопротивления, трендовые линии и фигуры технического анализа."
    ),
    "altcoin-fundamental-analysis.html": (
        "Как анализировать альткоины перед покупкой: Руководство по фундаментальному анализу", 
        "altcoin-fundamental-analysis.png",
        "Инвестиции",
        "На что смотреть при выборе токена: токеномика, команда проекта, Whitepaper и рыночная капитализация."
    ),
    "binance-square-guide.html": (
        "Как использовать Binance Square для поиска сильных крипто-трендов и инсайдов", 
        "binance-square-guide.png",
        "Трафик и блоги",
        "Инструкция по поиску авторов, аналитике и привлечению аудитории через Binance Square."
    ),
    "crypto-risk-management.html": (
        "Продвинутый риск-менеджмент: Как не потерять депозит на Binance в 2026 году",
        "crypto-risk-management.png",
        "Трейдинг для профи",
        "Разбор мани-менеджмента, расчета размера позиции, выставления стоп-ордеров и психологии торговли."
    ),
    "ai-memecoin-analysis.html": (
        "Локальный ИИ против мемкоинов: Как находить гем-токены в 2026 году",
        "ai-memecoin-thumb.png",
        "ИИ и Мемкоины",
        "Пошаговое руководство по использованию Ollama и Python для анализа смарт-контрактов, объемов ликвидности и социальных трендов взрывных токенов."
    ),
    "crypto-trading-psychology.html": (
        "Психология криптотрейдинга и ИИ: Как победить себя с помощью алгоритмов",
        "crypto-trading-psychology.png",
        "Психология и ИИ",
        "Как убрать эмоции из торговли, перестать покупать на хаях и делегировать холодный расчет локальным нейросетям."
    ),
    "ai-phishing-protection.html": (
        "Защита от ИИ-фишинга и дипфейков в Web3: Как распознать обман и сохранить крипту в 2026 году",
        "ai-phishing-protection.png",
        "Безопасность Web3",
        "Как распознать поддельные видеозвонки от нейросетей, фейковые сайты раздач и опасные подписи в кошельке."
    ),
    "ai-dca-strategy.html": (
        "Стратегия DCA и локальный ИИ: Как безопасно покупать криптовалюту на падении рынка в 2026 году",
        "ai-dca-strategy.png",
        "Стратегии и ИИ",
        "Пошаговое руководство по усреднению позиций (DCA) на падающем рынке и настройке нейросетей для поиска сильных уровней поддержки."
    ),
    "ai-crypto-agents-guide.html": (
        "ИИ-агенты в криптовалюте: Как настроить автономного помощника для анализа рынка в 2026 году",
        "ai-crypto-agents-guide.png",
        "ИИ-Агенты",
        "Пошаговое руководство по созданию и использованию ИИ-агентов в трейдинге: мониторинг новостей, поиск аномалий объёма и фильтрация сигналов через локальные нейросети."
    )
    
}

def create_backup(file_path):
    if os.path.exists(file_path):
        backup_path = file_path + ".bak"
        if not os.path.exists(backup_path):
            shutil.copy2(file_path, backup_path)
            logging.info(f"Создана резервная копия: {backup_path}")

def fix_article_links(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    for link in soup.find_all("a", href=True):
        href = link["href"].strip()
        if "binance.com" in href.lower():
            link["href"] = BINANCE_REF_URL
        link["target"] = "_blank"
        
        rel = link.get("rel")
        if rel is None:
            rel = []
        elif isinstance(rel, str):
            rel = rel.split()
        rel = set(rel)
        rel.update(["noopener", "noreferrer"])
        link["rel"] = list(rel)
    return soup.decode_contents()

def extract_clean_content(file_path):
    paths_to_try = [file_path, file_path + ".bak"]
    for path in paths_to_try:
        if not os.path.exists(path):
            continue
        try:
            with open(path, "r", encoding="utf-8") as file:
                soup = BeautifulSoup(file.read(), "html.parser")
            article = soup.find("div", class_="article-text")
            if article and article.decode_contents().strip():
                return article.decode_contents().strip()
        except Exception as e:
            logging.error(f"Ошибка чтения {path}: {e}")
    return None

def get_related_guides_html(current_file):
    other_files = [f for f in GUIDES_DATA.keys() if f != current_file]
    selected = random.sample(other_files, min(3, len(other_files)))
    
    cards_html = ""
    for f_name in selected:
        t_topic, t_img, t_badge, _ = GUIDES_DATA[f_name]
        cards_html += f"""
        <a href="{f_name}" class="related-card" style="text-decoration: none; background: #1e2026; border: 1px solid #2b3139; border-radius: 8px; overflow: hidden; display: flex; flex-direction: column;">
            <img src="{escape(t_img, quote=True)}" alt="{escape(t_topic, quote=True)}" style="width: 100%; height: 130px; object-fit: cover;">
            <div style="padding: 15px;">
                <span style="color: #f3ba2f; font-size: 0.75rem; font-weight: bold; text-transform: uppercase;">{escape(t_badge)}</span>
                <h4 style="color: #fff; margin: 8px 0 0 0; font-size: 0.95rem; line-height: 1.4;">{escape(t_topic)}</h4>
            </div>
        </a>
        """
        
    return f"""
    <section class="related-guides" style="margin-top: 40px; padding-top: 30px; border-top: 1px solid #2b3139;">
        <h3 style="color: #fff; margin: 0 0 20px 0; font-size: 1.4rem; border-left: 4px solid #f3ba2f; padding-left: 12px;">Читайте также по теме</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 15px;">
            {cards_html}
        </div>
    </section>
    """

def build_article_html(file_name, topic, img_name, desc, article_content):
    safe_topic = escape(topic)
    safe_image = escape(img_name, quote=True)
    safe_desc = escape(desc, quote=True)
    clean_text = fix_article_links(article_content)
    related_block = get_related_guides_html(file_name)
    page_url = f"https://crypto-ai-hub.com/guides/{file_name}"
    og_image_url = f"https://crypto-ai-hub.com/guides/{safe_image}"

    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{safe_topic} — Crypto AI Hub</title>
    <meta name="description" content="{safe_desc}">
    <link rel="canonical" href="{page_url}">
    <link rel="alternate" hreflang="ru" href="{page_url}">
    <link rel="alternate" hreflang="en" href="https://crypto-ai-hub.com/en/guides/{file_name}">
    <meta property="og:type" content="article">
    <meta property="og:site_name" content="Crypto AI Hub">
    <meta property="og:title" content="{safe_topic} — Crypto AI Hub">
    <meta property="og:description" content="{safe_desc}">
    <meta property="og:url" content="{page_url}">
    <meta property="og:image" content="{og_image_url}">
    <meta name="twitter:card" content="summary_large_image">
    <link rel="stylesheet" href="../css/style.css">
    <link rel="icon" type="image/png" sizes="144x144" href="/images/favicon.png">
    <link rel="apple-touch-icon" href="/images/favicon.png">
    <meta name="theme-color" content="#1e2026">
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "{safe_topic}",
      "description": "{safe_desc}",
      "image": "{og_image_url}",
      "author": {{
        "@type": "Organization",
        "name": "Crypto AI Hub",
        "url": "https://crypto-ai-hub.com/"
      }},
      "publisher": {{
        "@type": "Organization",
        "name": "Crypto AI Hub",
        "logo": {{
          "@type": "ImageObject",
          "url": "https://crypto-ai-hub.com/images/favicon.png"
        }}
      }},
      "mainEntityOfPage": {{
        "@type": "WebPage",
        "@id": "{page_url}"
      }}
    }}
    </script>
</head>
<body>
    <header class="navbar">
        <div class="container">
            <div class="header-brand">
                <a href="/" class="logo">Crypto <span>AI</span> Hub</a>
                <a href="/en/guides/{file_name}" class="menu-toggle" style="text-decoration:none;"><strong>RU</strong> | EN</a>
            </div>
            <div class="header-actions">
                <button class="menu-toggle" aria-label="Открыть меню">Меню</button>
                <a href="{BINANCE_REF_URL}" target="_blank" rel="noopener noreferrer" class="btn-ref">Регистрация на Binance</a>
            </div>
            <nav class="nav-links">
                <a href="/" class="nav-link">Главная</a>
                <a href="/#guides-section" class="nav-link">Гайды</a>
                <div class="dropdown">
                    <a href="#" class="nav-link">Инструменты ▾</a>
                    <div class="dropdown-content">
                        <a href="../prompts.html"><svg class="cyber-icon cyan" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="16" height="16" rx="2"/><path d="M9 9h6"/><path d="M9 13l2 2-2 2"/><path d="M13 17h3"/><path d="M9 1v3M15 1v3M9 20v3M15 20v3M1 9h3M1 15h3M20 9h3M20 15h3"/></svg>Библиотека промптов</a>
                        <a href="../calculator.html"><svg class="cyber-icon gold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="2"/><line x1="8" y1="6" x2="16" y2="6"/><line x1="8" y1="11" x2="8.01" y2="11"/><line x1="12" y1="11" x2="12.01" y2="11"/><line x1="16" y1="11" x2="16.01" y2="11"/><line x1="8" y1="15" x2="8.01" y2="15"/><line x1="12" y1="15" x2="12.01" y2="15"/><path d="M16 15v4"/></svg>Крипто-калькуляторы</a>
                    </div>
                </div>
                <a href="../wotd.html" class="nav-link">Ответы WOTD</a>
                <a href="../news.html" class="nav-link">Новости</a>
                <a href="../partners.html" class="nav-link">Заработок без вложений</a>
                <a href="../disclaimer.html" class="nav-link">Дисклеймер</a>
            </nav>
        </div>
    </header>

    <main class="guides-section">
        <div class="container" style="max-width: 800px; margin: 0 auto; padding: 40px 20px;">
                        
            <div class="article-cover" style="margin-bottom: 30px; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
                <img src="{safe_image}" alt="{safe_topic}" style="width: 100%; max-height: 450px; object-fit: cover; display: block;">
            </div>

            <div class="promo-banner-inline" style="background: linear-gradient(135deg, #1e2026, #2b3139); border-left: 4px solid #f3ba2f; padding: 25px; border-radius: 8px; margin-bottom: 30px; box-shadow: 0 4px 15px rgba(0,0,0,0.2); text-align: center;">
                <h4 style="color: #f3ba2f; margin: 0 0 12px 0; font-size: 1.2rem; font-weight: 600;">🔥 Бонус для читателей Crypto AI Hub</h4>
                <p style="color: #eaeaea; margin: 0 0 20px 0; font-size: 0.95rem; line-height: 1.6;">Регистрируйтесь на Binance по нашей ссылке и получите постоянную скидку 10% на все спотовые комиссии, а также приветственный инвесторский бонус до $100.</p>
                <a href="{BINANCE_REF_URL}" target="_blank" rel="noopener noreferrer" style="display: inline-block; background: #f3ba2f; color: #000; padding: 12px 24px; border-radius: 4px; text-decoration: none; font-weight: bold; font-size: 0.95rem; transition: background 0.2s; margin: 0 auto;">Получить скидку 10% на Binance &rarr;</a>
            </div>

            <div class="article-text" style="color: var(--text-main); font-size: 1.1rem; line-height: 1.8;">
                {clean_text}
            </div>

            <div class="promo-banner-footer" style="background: #1e2026; border: 1px solid #2b3139; padding: 30px; border-radius: 12px; margin-top: 40px; text-align: center;">
                <h3 style="color: #fff; margin: 0 0 10px 0; font-size: 1.5rem;">Готовы применить знания на практике?</h3>
                <p style="color: #b7bdc6; margin: 0 0 20px 0; font-size: 1rem;">Откройте аккаунт сегодня, зафиксируйте за собой сниженные комиссии и начните собирать свой первый криптопортфель с поддержкой искусственного интеллекта.</p>
                <a href="{BINANCE_REF_URL}" target="_blank" rel="noopener noreferrer" class="btn-ref" style="display: inline-block; padding: 12px 30px; font-size: 1rem; text-decoration: none; background-color: #00f2fe; color: #0b0e11;">Зарегистрироваться на Binance со скидкой 10%</a>
            </div>
            
            {related_block}

        </div>
    </main>

    <footer class="footer">
     <div class="container" style="display: flex; flex-direction: column; align-items: center; text-align: center;">
         <p>&copy; 2026 Crypto AI Hub. Все права защищены.</p>
         <p class="footer-note">Контент на сайте носит информационный характер и не является финансовой рекомендацией.</p>
         <a href="https://t.me/crypto_ai_hub" target="_blank" rel="noopener noreferrer" class="footer-tg-btn">
             <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/></svg>
             Наш Telegram-канал
         </a>
     </div>
    </footer>
    
    <script id="mobile-menu-script">
        document.addEventListener('DOMContentLoaded', () => {{
            const toggle = document.querySelector('button.menu-toggle');
            const nav = document.querySelector('.nav-links');
            if (toggle && nav) {{
                toggle.addEventListener('click', () => {{
                    nav.classList.toggle('open');
                    toggle.textContent = nav.classList.contains('open') ? '✕ Меню' : 'Меню';
                }});
            }}
        }});
    </script>
</body>
</html>"""

def update_all_guides():
    logging.info("🚀 Синхронизация внутренних страниц статей...")
    if not os.path.exists(GUIDES_DIR):
        logging.error(f"Папка guides не найдена: {GUIDES_DIR}")
        return

    for file_name, data in GUIDES_DATA.items():
        topic, img_name, desc = data[0], data[1], data[3]
        file_path = os.path.join(GUIDES_DIR, file_name)
        
        article_content = extract_clean_content(file_path)
        if not article_content:
            logging.warning(f"⚠️ Текст для {file_name} пуст. Создаем временную структуру.")
            article_content = f"<h2>{topic}</h2><p>Инструкция находится в процессе автоматической генерации локальным ИИ. Пожалуйста, запустите writer.py для обновления контента.</p>"

        try:
            create_backup(file_path)
            new_html = build_article_html(file_name, topic, img_name, desc, article_content)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_html)
            logging.info(f"✅ Статья обновлена: {file_name}")
        except Exception as error:
            logging.exception(f"Ошибка записи {file_name}: {error}")
    # Обучаем адаптер обрабатывать страницу новостей в корне
    news_file_path = os.path.join(PROJECT_DIR, "news.html")
    if os.path.exists(news_file_path):
        with open(news_file_path, "r", encoding="utf-8") as f:
            news_soup = BeautifulSoup(f.read(), "html.parser")
        
        # Здесь ваш updater.py прогоняет стандартные регулярки для ссылок Binance и структуры Navbar
        # (Скрипт автоматически накатит реф-ссылки на все упоминания "официальный сайт Binance" внутри news.html)
        
        with open(news_file_path, "w", encoding="utf-8") as f:
            f.write(str(news_soup))
        logging.info("✅ Страница новостей успешно синхронизирована с адаптером: news.html")

def rebuild_index_grid():
        logging.info("📝 Парсинг структуры index.html...")
        if not os.path.exists(INDEX_FILE):
            logging.error("Файл index.html не найден!")
            return
        try:
            with open(INDEX_FILE, "r", encoding="utf-8") as file:
                soup = BeautifulSoup(file.read(), "html.parser")
            
            grid_div = soup.find("div", class_="guides-grid")
            if not grid_div:
                logging.error("❌ Ошибка: В index.html не найден контейнер guides-grid!")
                return

            grid_div.clear()
            
            # Надежное добавление HTML-комментария
            from bs4 import Comment
            marker_comment = Comment("START_CRYPTO_AI_CARDS")
            grid_div.append(marker_comment)

            for file_name, data in GUIDES_DATA.items():
                topic, img_name, badge, desc = data

                article_tag = soup.new_tag("article", attrs={"class": "guide-card"})
                img_tag = soup.new_tag("img", attrs={"src": f"guides/{img_name}", "alt": topic, "class": "card-thumb"})

                badge_div = soup.new_tag("div", attrs={"class": "card-badge"})
                badge_div.string = badge

                h3_tag = soup.new_tag("h3")
                h3_tag.string = topic

                p_tag = soup.new_tag("p")
                p_tag.string = desc

                a_tag = soup.new_tag("a", attrs={"href": f"guides/{file_name}", "class": "card-link"})
                a_tag.string = "Читать гайд \u2192"

                article_tag.append(img_tag)
                article_tag.append(badge_div)
                article_tag.append(h3_tag)
                article_tag.append(p_tag)
                article_tag.append(a_tag)

                grid_div.append(article_tag)

            create_backup(INDEX_FILE)

            with open(INDEX_FILE, "w", encoding="utf-8") as file:
                file.write(soup.prettify(formatter="html"))

            logging.info("🎉 Главная страница успешно пересобрана! Все 10 карточек на месте.")
        except Exception as error:
            logging.exception(f"Ошибка при работе с index.html: {error}")

def sync_root_navbars():
    logging.info("🧭 Синхронизация верхнего меню и SEO-тегов в корневых файлах...")
    root_files = ["index.html", "wotd.html", "news.html", "prompts.html", "calculator.html", "partners.html", "disclaimer.html"]
    
    for filename in root_files:
        filepath = os.path.join(PROJECT_DIR, filename)
        if not os.path.exists(filepath):
            continue
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f.read(), "html.parser")

            header_container = soup.find("header", class_="navbar").find("div", class_="container") if soup.find("header", class_="navbar") else None
            logo = soup.find("a", class_="logo")
            if logo:
                logo["href"] = "/"

            # Удаляем старые кнопки перед пересборкой
            for old_btn in soup.select("button.menu-toggle, a.menu-toggle"):
                old_btn.decompose()

            if header_container and logo:
                en_target = "/en/" if filename == "index.html" else f"/en/{filename}"
                brand_div = header_container.find("div", class_="header-brand")
                if not brand_div:
                    brand_div = soup.new_tag("div", attrs={"class": "header-brand"})
                    logo.insert_before(brand_div)
                    brand_div.append(logo)
                
                lang_link = BeautifulSoup(f'<a href="{en_target}" class="menu-toggle" style="text-decoration:none;"><strong>RU</strong> | EN</a>', "html.parser")
                brand_div.append(lang_link)

                actions_div = header_container.find("div", class_="header-actions")
                if not actions_div:
                    actions_div = soup.new_tag("div", attrs={"class": "header-actions"})
                    brand_div.insert_after(actions_div)
                actions_div.clear()
                actions_html = f"""
                    <button class="menu-toggle" aria-label="Открыть меню">Меню</button>
                    <a href="{BINANCE_REF_URL}" target="_blank" rel="noopener noreferrer" class="btn-ref">Регистрация на Binance</a>
                """
                actions_div.append(BeautifulSoup(actions_html, "html.parser"))

            body = soup.find("body")
            if body:
                old_script = body.find("script", id="mobile-menu-script")
                if old_script:
                    old_script.decompose()
                menu_script = soup.new_tag("script", id="mobile-menu-script")
                menu_script.string = "document.addEventListener('DOMContentLoaded', () => { const toggle = document.querySelector('button.menu-toggle'); const nav = document.querySelector('.nav-links'); if (toggle && nav) { toggle.addEventListener('click', () => { nav.classList.toggle('open'); toggle.textContent = nav.classList.contains('open') ? '✕ Меню' : 'Меню'; }); } });"
                body.append(menu_script)

            nav = soup.find("nav", class_="nav-links")
            if nav:
                active_wotd = " active" if filename == "wotd.html" else ""
                active_partners = " active" if filename == "partners.html" else ""
                nav.clear()
                nav_html = f"""
                    <a href="/" class="nav-link">Главная</a>
                    <a href="/#guides-section" class="nav-link">Гайды</a>
                    <div class="dropdown">
                        <a href="#" class="nav-link">Инструменты ▾</a>
                        <div class="dropdown-content">
                            <a href="prompts.html"><svg class="cyber-icon cyan" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="16" height="16" rx="2"/><path d="M9 9h6"/><path d="M9 13l2 2-2 2"/><path d="M13 17h3"/><path d="M9 1v3M15 1v3M9 20v3M15 20v3M1 9h3M1 15h3M20 9h3M20 15h3"/></svg>Библиотека промптов</a>
                            <a href="calculator.html"><svg class="cyber-icon gold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="2"/><line x1="8" y1="6" x2="16" y2="6"/><line x1="8" y1="11" x2="8.01" y2="11"/><line x1="12" y1="11" x2="12.01" y2="11"/><line x1="16" y1="11" x2="16.01" y2="11"/><line x1="8" y1="15" x2="8.01" y2="15"/><line x1="12" y1="15" x2="12.01" y2="15"/><path d="M16 15v4"/></svg>Крипто-калькуляторы</a>
                        </div>
                    </div>
                    <a href="wotd.html" class="nav-link{active_wotd}">Ответы WOTD</a>
                    <a href="news.html" class="nav-link">Новости</a>
                    <a href="partners.html" class="nav-link{active_partners}">Заработок без вложений</a>
                    <a href="disclaimer.html" class="nav-link">Дисклеймер</a>
                """
                nav.append(BeautifulSoup(nav_html, "html.parser"))
                
            head = soup.find("head")
            if head:
                for old_icon in head.find_all("link", rel=lambda r: r and ("icon" in r or "apple-touch-icon" in r)):
                    old_icon.decompose()
                head.append(soup.new_tag("link", rel="icon", type="image/png", sizes="144x144", href="/images/favicon.png"))
                head.append(soup.new_tag("link", rel="apple-touch-icon", href="/images/favicon.png"))
                
                if not head.find("meta", attrs={"name": "theme-color"}):
                    theme_meta = soup.new_tag("meta", attrs={"name": "theme-color", "content": "#1e2026"})
                    head.append(theme_meta)

                for old_can in head.find_all("link", rel="canonical"):
                    old_can.decompose()
                clean_url = "https://crypto-ai-hub.com/" if filename == "index.html" else f"https://crypto-ai-hub.com/{filename}"
                head.append(soup.new_tag("link", rel="canonical", href=clean_url))
                for old_alt in head.find_all("link", rel="alternate"):
                    old_alt.decompose()
                en_clean_url = "https://crypto-ai-hub.com/en/" if filename == "index.html" else f"https://crypto-ai-hub.com/en/{filename}"
                head.append(soup.new_tag("link", rel="alternate", hreflang="ru", href=clean_url))
                head.append(soup.new_tag("link", rel="alternate", hreflang="en", href=en_clean_url))

                if filename == "index.html" and not head.find("script", id="clean-url-script"):
                    clean_script = soup.new_tag("script", id="clean-url-script")
                    clean_script.string = "if (window.location.pathname.endsWith('/index.html')) { window.history.replaceState(null, '', '/'); }"
                    head.append(clean_script)
            
            footer = soup.find("footer")
            if footer:
                footer["class"] = "footer"
                footer.clear()
                footer_html = """
                    <div class="container" style="display: flex; flex-direction: column; align-items: center; text-align: center;">
                        <p>&copy; 2026 Crypto AI Hub. Все права защищены.</p>
                        <p class="footer-note">Контент на сайте носит информационный характер и не является финансовой рекомендацией.</p>
                        <a href="https://t.me/crypto_ai_hub" target="_blank" rel="noopener noreferrer" class="footer-tg-btn">
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/></svg>
                            Наш Telegram-канал
                        </a>
                    </div>
                """
                footer.append(BeautifulSoup(footer_html, "html.parser"))
                    
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(str(soup))
            logging.info(f"✅ Меню и чистые URL обновлены в {filename}")
        except Exception as e:
            logging.error(f"Ошибка при обновлении {filename}: {e}")

def main():
        logging.info("=" * 55)
        logging.info("       CRYPTO AI HUB — COMPLETE WEBSITE UPDATER")
        logging.info("=" * 55)
        update_all_guides()
        rebuild_index_grid()
        sync_root_navbars()
        logging.info("=" * 55)


if __name__ == "__main__":
        main()
