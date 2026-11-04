import os
import re
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

# Полный список из 10 статей
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

def build_article_html(topic, img_name, article_content):
    safe_topic = escape(topic)
    safe_image = escape(img_name, quote=True)
    clean_text = fix_article_links(article_content)

    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{safe_topic} — CryptoAI Hub</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <header class="navbar">
        <div class="container">
            <a href="../index.html" class="logo">Crypto<span>AI</span> Hub</a>
            <nav class="nav-links">
                <a href="../index.html#guides-section" class="nav-link">На главную</a>
                <a href="{BINANCE_REF_URL}" target="_blank" rel="noopener noreferrer" class="btn-ref">Регистрация на Binance</a>
            </nav>
        </div>
    </header>

    <main class="guides-section">
        <div class="container" style="max-width: 800px; margin: 0 auto; padding: 40px 20px;">
                        
            <div class="article-cover" style="margin-bottom: 30px; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
                <img src="{safe_image}" alt="{safe_topic}" style="width: 100%; max-height: 450px; object-fit: cover; display: block;">
            </div>

            <div class="promo-banner-inline" style="background: linear-gradient(135deg, #1e2026, #2b3139); border-left: 4px solid #f3ba2f; padding: 25px; border-radius: 8px; margin-bottom: 30px; box-shadow: 0 4px 15px rgba(0,0,0,0.2); text-align: center;">
                <h4 style="color: #f3ba2f; margin: 0 0 12px 0; font-size: 1.2rem; font-weight: 600;">🔥 Бонус для читателей CryptoAI Hub</h4>
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

        </div>
    </main>

    <footer class="footer">
        <div class="container"><p>&copy; 2026 CryptoAI Hub. Все права защищены.</p></div>
    </footer>
</body>
</html>"""

def update_all_guides():
    logging.info("🚀 Синхронизация внутренних страниц статей...")
    if not os.path.exists(GUIDES_DIR):
        logging.error(f"Папка guides не найдена: {GUIDES_DIR}")
        return

    for file_name, data in GUIDES_DATA.items():
        topic, img_name = data[0], data[1]
        file_path = os.path.join(GUIDES_DIR, file_name)
        
        article_content = extract_clean_content(file_path)
        if not article_content:
            logging.warning(f"⚠️ Текст для {file_name} пуст. Создаем временную структуру.")
            article_content = f"<h2>{topic}</h2><p>Инструкция находится в процессе автоматической генерации локальным ИИ. Пожалуйста, запустите writer.py для обновления контента.</p>"

        try:
            create_backup(file_path)
            new_html = build_article_html(topic, img_name, article_content)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_html)
            logging.info(f"✅ Статья обновлена: {file_name}")
        except Exception as error:
            logging.exception(f"Ошибка записи {file_name}: {error}")

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


def main():
        logging.info("=" * 55)
        logging.info("       CRYPTO AI HUB — COMPLETE WEBSITE UPDATER")
        logging.info("=" * 55)
        update_all_guides()
        rebuild_index_grid()
        logging.info("=" * 55)


if __name__ == "__main__":
        main()
