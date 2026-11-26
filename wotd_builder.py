import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BINANCE_REF_URL = "https://www.binance.com/register?ref=SHARA10"

# =========================================================================
# ЕЖЕНЕДЕЛЬНЫЕ ДАННЫЕ BINANCE WOTD (МЕНЯЙТЕ КАЖДЫЙ ПОНЕДЕЛЬНИК)
# =========================================================================
WOTD_THEME = "TradFi Products on Binance"
WOTD_DATES_RU = "23–29 ноября 2026"
WOTD_DATES_EN = "November 23–29, 2026"
WOTD_POOL = "14 BNB"

WOTD_WORDS = {
    8: ["CONTRACT"],
    7: ["CONNECT", "CONVERT", "TRADING"],
    6: ["ACCESS", "EQUITY", "FUTURE", "MARGIN", "MARKET", "OPTION"],
    5: ["ASSET", "HEDGE", "STOCK", "TOKEN", "TRADE"],
    4: ["BOND", "RISK"],
    3: ["ETF", "BUY"]
}
# =========================================================================


def render_table_rows(lang="ru"):
    rows = ""
    for length in sorted(WOTD_WORDS.keys(), reverse=True):
        words = WOTD_WORDS[length]
        if not words:
            continue
        label = f"{length} букв" if lang == "ru" else f"{length} Letters"
        chips = "".join(
            f'<button type="button" class="wotd-word-chip" onclick="copyWotdWord(this, \'{w}\')">{w}</button>'
            for w in words
        )
        rows += f"""
                    <tr>
                        <td style="font-weight: 600; color: #eaeaea; white-space: nowrap;">{label}</td>
                        <td><div class="wotd-words-wrap">{chips}</div></td>
                    </tr>"""
    return rows


COPY_SCRIPT = """
    <script>
        function copyWotdWord(btn, word) {
            navigator.clipboard.writeText(word).then(() => {
                const orig = btn.textContent;
                btn.textContent = '✓ ' + word;
                btn.classList.add('copied');
                setTimeout(() => {
                    btn.textContent = orig;
                    btn.classList.remove('copied');
                }, 1200);
            });
        }
    </script>
"""

FOOTER_RU = """
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
"""

FOOTER_EN = """
    <footer class="footer">
        <div class="container" style="display: flex; flex-direction: column; align-items: center; text-align: center;">
            <p>&copy; 2026 Crypto AI Hub. All rights reserved.</p>
            <p class="footer-note">Content is for informational purposes only and does not constitute financial advice.</p>
            <a href="https://t.me/crypto_ai_hub" target="_blank" rel="noopener noreferrer" class="footer-tg-btn">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/></svg>
                Join our Telegram Channel
            </a>
        </div>
    </footer>
"""


def build_ru_wotd():
    html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ответы Binance WOTD (Слово дня) сегодня — {WOTD_DATES_RU} | Crypto AI Hub</title>
    <meta name="description" content="Актуальные правильные ответы на кроссворд Binance WOTD (Crypto WODL) на {WOTD_DATES_RU}. Тема: {WOTD_THEME}. Призовой фонд {WOTD_POOL}. Копируйте слова в один клик!">
    <link rel="canonical" href="https://crypto-ai-hub.com/wotd.html">
    <link rel="alternate" hreflang="ru" href="https://crypto-ai-hub.com/wotd.html">
    <link rel="alternate" hreflang="en" href="https://crypto-ai-hub.com/en/wotd.html">
    <link rel="stylesheet" href="css/style.css">
    <link rel="icon" type="image/png" sizes="144x144" href="/images/favicon.png">
</head>
<body>
    <header class="navbar">
        <div class="container">
            <div class="header-brand">
                <a href="/" class="logo">Crypto <span>AI</span> Hub</a>
                <a href="/en/wotd.html" class="menu-toggle" style="text-decoration:none;"><strong>RU</strong> | EN</a>
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
                        <a href="prompts.html">Библиотека промптов</a>
                        <a href="calculator.html">Крипто-калькуляторы</a>
                    </div>
                </div>
                <a href="wotd.html" class="nav-link active">Ответы WOTD</a>
                <a href="news.html" class="nav-link">Новости</a>
                <a href="partners.html" class="nav-link">Заработок без вложений</a>
                <a href="disclaimer.html" class="nav-link">Дисклеймер</a>
            </nav>
        </div>
    </header>

    <main class="guides-section">
        <div class="container" style="max-width: 860px; margin: 0 auto; padding: 40px 20px;">
            <div style="margin-bottom: 12px; color: #00f2fe; font-weight: 600; font-size: 0.9rem; text-transform: uppercase;">
                🔄 Обновляется каждый понедельник • Актуально на {WOTD_DATES_RU}
            </div>
            <h1 style="font-size: 2rem; margin-bottom: 16px; color: #fff;">Ответы Binance WOTD (Слово дня) сегодня — {WOTD_DATES_RU}</h1>
            <p style="color: var(--text-muted); font-size: 1.05rem; line-height: 1.7; margin-bottom: 24px;">
                Актуальная тема недели: <strong style="color: #f3ba2f;">«{WOTD_THEME}»</strong>. Общий призовой фонд раунда составляет <strong style="color: #fff;">{WOTD_POOL}</strong>. Нажмите на любое подходящее по количеству букв слово в таблице ниже, чтобы мгновенно скопировать его для игры на <a href="{BINANCE_REF_URL}" target="_blank" rel="noopener noreferrer" style="color: #f3ba2f;">Binance</a>.
            </p>

            <table class="wotd-table">
                <thead>
                    <tr>
                        <th style="width: 150px;">Длина слова</th>
                        <th>Правильные слова (нажмите, чтобы скопировать)</th>
                    </tr>
                </thead>
                <tbody>
                    {render_table_rows("ru")}
                </tbody>
            </table>

            <div class="promo-banner-inline" style="background: linear-gradient(135deg, #1e2026, #2b3139); border-left: 4px solid #f3ba2f; padding: 25px; border-radius: 8px; margin: 30px 0; text-align: center;">
                <h4 style="color: #f3ba2f; margin: 0 0 10px 0; font-size: 1.2rem;">🎁 Как забрать награду из пула {WOTD_POOL}?</h4>
                <p style="color: #eaeaea; margin: 0 0 18px 0; font-size: 0.95rem; line-height: 1.6;">
                    Для участия в распределении наград необходим верифицированный аккаунт (KYC). Если у вас ещё нет профиля, зарегистрируйтесь по нашей партнёрской ссылке с кодом <strong>SHARA10</strong> и получите постоянную скидку 10% на все торговые комиссии.
                </p>
                <a href="{BINANCE_REF_URL}" target="_blank" rel="noopener noreferrer" style="display: inline-block; background: #f3ba2f; color: #000; padding: 12px 26px; border-radius: 6px; text-decoration: none; font-weight: bold;">Создать аккаунт Binance со скидкой 10% &rarr;</a>
            </div>

            <div class="article-text" style="color: var(--text-main); font-size: 1.05rem; line-height: 1.8;">
                <h2>Как играть в Binance WOTD и получить максимум наград</h2>
                <p><strong>Binance WOTD (Word of the Day)</strong> — это ежедневная крипто-викторина в формате кроссворда. Пользователям даётся 6 попыток, чтобы угадать загаданный термин по теме недели:</p>
                <ul>
                    <li><strong>Зелёная клетка:</strong> буква есть в слове и стоит на правильном месте.</li>
                    <li><strong>Жёлтая клетка:</strong> буква есть в слове, но находится на другой позиции.</li>
                    <li><strong>Серая (чёрная) клетка:</strong> такой буквы в загаданном слове нет.</li>
                </ul>

                <h2>Условия распределения призового фонда</h2>
                <p>Чтобы претендовать на долю базового пула наград, достаточно дать минимум <strong>5 правильных ответов</strong> в течение игровой недели. Для доступа к повышенному призовому пулу биржа обычно предлагает выполнить дополнительное задание (например, совершить торговый оборот от $50 на споте или в разделе Конвертация).</p>

                <h2>Часто задаваемые вопросы (FAQ)</h2>
                <h3>Когда обновляются ответы на сайте?</h3>
                <p>Мы обновляем таблицу слов каждый понедельник сразу после старта новой темы в 00:00 UTC.</p>
                <h3>Как получить вторую попытку в день?</h3>
                <p>После первой игры нажмите кнопку <strong>«Поделиться»</strong> рядом со статьёй недели внутри интерфейса WOTD и перейдите по сгенерированной ссылке — откроется вторая бонусная игра за сутки.</p>
            </div>
        </div>
    </main>
{FOOTER_RU}
{COPY_SCRIPT}
</body>
</html>
"""
    with open(os.path.join(PROJECT_DIR, "wotd.html"), "w", encoding="utf-8") as f:
        f.write(html)
    logging.info("✅ Создана русская страница ответов WOTD: wotd.html")


def build_en_wotd():
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Binance WOTD Answers Today ({WOTD_DATES_EN}) — {WOTD_THEME} | Crypto AI Hub</title>
    <meta name="description" content="Verified Binance WOTD (Crypto WODL) answers for {WOTD_DATES_EN}. Theme: {WOTD_THEME}. Reward pool: {WOTD_POOL}. Click any word to copy in one click!">
    <link rel="canonical" href="https://crypto-ai-hub.com/en/wotd.html">
    <link rel="alternate" hreflang="ru" href="https://crypto-ai-hub.com/wotd.html">
    <link rel="alternate" hreflang="en" href="https://crypto-ai-hub.com/en/wotd.html">
    <link rel="stylesheet" href="../css/style.css">
    <link rel="icon" type="image/png" sizes="144x144" href="/images/favicon.png">
</head>
<body>
    <header class="navbar">
        <div class="container">
            <div class="header-brand">
                <a href="/en/" class="logo">Crypto <span>AI</span> Hub</a>
                <a href="/wotd.html" class="menu-toggle" style="text-decoration:none;">RU | <strong>EN</strong></a>
            </div>
            <div class="header-actions">
                <button class="menu-toggle" aria-label="Open menu">Menu</button>
                <a href="{BINANCE_REF_URL}" target="_blank" rel="noopener noreferrer" class="btn-ref">Register on Binance</a>
            </div>
            <nav class="nav-links">
                <a href="/en/" class="nav-link">Home</a>
                <a href="/en/#guides-section" class="nav-link">Guides</a>
                <div class="dropdown">
                    <a href="#" class="nav-link">Tools ▾</a>
                    <div class="dropdown-content">
                        <a href="prompts.html">AI Prompt Library</a>
                        <a href="calculator.html">Crypto Calculators</a>
                    </div>
                </div>
                <a href="wotd.html" class="nav-link active">WOTD Answers</a>
                <a href="news.html" class="nav-link">News</a>
                <a href="partners.html" class="nav-link">Free Crypto</a>
                <a href="disclaimer.html" class="nav-link">Disclaimer</a>
            </nav>
        </div>
    </header>

    <main class="guides-section">
        <div class="container" style="max-width: 860px; margin: 0 auto; padding: 40px 20px;">
            <div style="margin-bottom: 12px; color: #00f2fe; font-weight: 600; font-size: 0.9rem; text-transform: uppercase;">
                🔄 Updated Every Monday • Valid for {WOTD_DATES_EN}
            </div>
            <h1 style="font-size: 2rem; margin-bottom: 16px; color: #fff;">Binance WOTD Answers Today — {WOTD_DATES_EN}</h1>
            <p style="color: var(--text-muted); font-size: 1.05rem; line-height: 1.7; margin-bottom: 24px;">
                This week's official theme is <strong style="color: #f3ba2f;">"{WOTD_THEME}"</strong> with a total reward pool of <strong style="color: #fff;">{WOTD_POOL}</strong>. Click any word matching your grid length below to copy it to your clipboard for <a href="{BINANCE_REF_URL}" target="_blank" rel="noopener noreferrer" style="color: #f3ba2f;">Binance</a>.
            </p>

            <table class="wotd-table">
                <thead>
                    <tr>
                        <th style="width: 150px;">Word Length</th>
                        <th>Correct Answers (Click to Copy)</th>
                    </tr>
                </thead>
                <tbody>
                    {render_table_rows("en")}
                </tbody>
            </table>

            <div class="promo-banner-inline" style="background: linear-gradient(135deg, #1e2026, #2b3139); border-left: 4px solid #f3ba2f; padding: 25px; border-radius: 8px; margin: 30px 0; text-align: center;">
                <h4 style="color: #f3ba2f; margin: 0 0 10px 0; font-size: 1.2rem;">🎁 How to Claim Your Share of the {WOTD_POOL} Pool</h4>
                <p style="color: #eaeaea; margin: 0 0 18px 0; font-size: 0.95rem; line-height: 1.6;">
                    A KYC-verified Binance account is required to receive WOTD rewards. New to Binance? Register via our partner link (code <strong>SHARA10</strong>) to unlock a lifetime 10% discount on spot trading fees.
                </p>
                <a href="{BINANCE_REF_URL}" target="_blank" rel="noopener noreferrer" style="display: inline-block; background: #f3ba2f; color: #000; padding: 12px 26px; border-radius: 6px; text-decoration: none; font-weight: bold;">Register on Binance with 10% Fee Discount &rarr;</a>
            </div>

            <div class="article-text" style="color: var(--text-main); font-size: 1.05rem; line-height: 1.8;">
                <h2>How Binance Word of the Day (WOTD) Works</h2>
                <p><strong>Binance WOTD</strong> is a daily educational crypto word puzzle. You get 6 attempts to guess a blockchain or market term related to the weekly theme:</p>
                <ul>
                    <li><strong>Green Tile:</strong> The letter is in the word and in the exact right spot.</li>
                    <li><strong>Yellow Tile:</strong> The letter is in the word but in a different position.</li>
                    <li><strong>Dark Grey Tile:</strong> The letter is not in the word at all.</li>
                </ul>

                <h2>Reward Eligibility Rules</h2>
                <p>Score at least <strong>5 correct wins</strong> during the activity period to qualify for an equal share of the base reward pool. To unlock the bonus pool, complete the optional weekly trading milestone (typically $50 cumulative volume on Spot or Convert).</p>

                <h2>Frequently Asked Questions (FAQ)</h2>
                <h3>When are new answers posted?</h3>
                <p>We update this word list every Monday right after the new weekly theme goes live at 00:00 UTC.</p>
                <h3>How do I unlock a second daily game?</h3>
                <p>After finishing your first daily puzzle, click <strong>"Share"</strong> on the featured Binance article inside the WOTD screen and open the shared link to unlock a second attempt.</p>
            </div>
        </div>
    </main>
{FOOTER_EN}
{COPY_SCRIPT}
</body>
</html>
"""
    os.makedirs(os.path.join(PROJECT_DIR, "en"), exist_ok=True)
    with open(os.path.join(PROJECT_DIR, "en", "wotd.html"), "w", encoding="utf-8") as f:
        f.write(html)
    logging.info("✅ Создана английская страница ответов WOTD: en/wotd.html")


if __name__ == "__main__":
    build_ru_wotd()
    build_en_wotd()