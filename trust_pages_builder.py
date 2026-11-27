import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
EN_DIR = os.path.join(PROJECT_DIR, "en")
BINANCE_REF_URL = "https://www.binance.com/register?ref=SHARA10"


def get_ru_header():
    return f"""    <header class="navbar">
        <div class="container">
            <div class="header-brand">
                <a href="/" class="logo">Crypto <span>AI</span> Hub</a>
                <a href="/en/" class="menu-toggle" style="text-decoration:none;"><strong>RU</strong> | EN</a>
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
                <a href="wotd.html" class="nav-link">Ответы WOTD</a>
                <a href="news.html" class="nav-link">Новости</a>
                <a href="partners.html" class="nav-link">Заработок без вложений</a>
                <a href="disclaimer.html" class="nav-link">Дисклеймер</a>
            </nav>
        </div>
    </header>"""


def get_en_header(en_slug):
    return f"""    <header class="navbar">
        <div class="container">
            <div class="header-brand">
                <a href="/en/" class="logo">Crypto <span>AI</span> Hub</a>
                <a href="/{en_slug}" class="menu-toggle" style="text-decoration:none;">RU | <strong>EN</strong></a>
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
                <a href="wotd.html" class="nav-link">WOTD Answers</a>
                <a href="news.html" class="nav-link">News</a>
                <a href="partners.html" class="nav-link">Free Crypto</a>
                <a href="disclaimer.html" class="nav-link">Disclaimer</a>
            </nav>
        </div>
    </header>"""


RU_FOOTER = """    <footer class="footer">
        <div class="container" style="display: flex; flex-direction: column; align-items: center; text-align: center;">
            <p>&copy; 2026 Crypto AI Hub. Все права защищены.</p>
            <p class="footer-note">Контент на сайте носит информационный характер и не является финансовой рекомендацией.</p>
            <p style="margin: 8px 0 14px 0; font-size: 0.9rem;">
                <a href="/about.html" style="color: #00f2fe; text-decoration: none; margin: 0 10px;">О проекте</a> |
                <a href="/privacy.html" style="color: #00f2fe; text-decoration: none; margin: 0 10px;">Политика конфиденциальности</a> |
                <a href="/disclaimer.html" style="color: #00f2fe; text-decoration: none; margin: 0 10px;">Дисклеймер</a>
            </p>
            <a href="https://t.me/crypto_ai_hub" target="_blank" rel="noopener noreferrer" class="footer-tg-btn">Наш Telegram-канал</a>
        </div>
    </footer>
    <script id="mobile-menu-script">
        document.addEventListener('DOMContentLoaded', () => {
            const toggle = document.querySelector('button.menu-toggle');
            const nav = document.querySelector('.nav-links');
            if (toggle && nav) {
                toggle.addEventListener('click', () => {
                    nav.classList.toggle('open');
                    toggle.textContent = nav.classList.contains('open') ? '✕ Меню' : 'Меню';
                });
            }
        });
    </script>"""

EN_FOOTER = """    <footer class="footer">
        <div class="container" style="display: flex; flex-direction: column; align-items: center; text-align: center;">
            <p>&copy; 2026 Crypto AI Hub. All rights reserved.</p>
            <p class="footer-note">Content is for informational purposes only and does not constitute financial advice.</p>
            <p style="margin: 8px 0 14px 0; font-size: 0.9rem;">
                <a href="/en/about.html" style="color: #00f2fe; text-decoration: none; margin: 0 10px;">About Us</a> |
                <a href="/en/privacy.html" style="color: #00f2fe; text-decoration: none; margin: 0 10px;">Privacy Policy</a> |
                <a href="/en/disclaimer.html" style="color: #00f2fe; text-decoration: none; margin: 0 10px;">Disclaimer</a>
            </p>
            <a href="https://t.me/crypto_ai_hub" target="_blank" rel="noopener noreferrer" class="footer-tg-btn">Join our Telegram Channel</a>
        </div>
    </footer>
    <script id="mobile-menu-script">
        document.addEventListener('DOMContentLoaded', () => {
            const toggle = document.querySelector('button.menu-toggle');
            const nav = document.querySelector('.nav-links');
            if (toggle && nav) {
                toggle.addEventListener('click', () => {
                    nav.classList.toggle('open');
                    toggle.textContent = nav.classList.contains('open') ? '✕ Menu' : 'Menu';
                });
            }
        });
    </script>"""


def build_pages():
    os.makedirs(EN_DIR, exist_ok=True)

    # 1. about.html (RU)
    about_ru = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>О проекте Crypto AI Hub — Редакционная политика и миссия</title>
    <meta name="description" content="Узнайте о миссии образовательного портала Crypto AI Hub, стандартах проверки материалов по Web3 и ИИ, а также принципах раскрытия партнёрских ссылок.">
    <link rel="canonical" href="https://crypto-ai-hub.com/about.html">
    <link rel="alternate" hreflang="ru" href="https://crypto-ai-hub.com/about.html">
    <link rel="alternate" hreflang="en" href="https://crypto-ai-hub.com/en/about.html">
    <link rel="stylesheet" href="css/style.css">
    <link rel="icon" type="image/png" sizes="144x144" href="/images/favicon.png">
</head>
<body>
{get_ru_header()}
    <main class="guides-section">
        <div class="container" style="max-width: 820px; margin: 0 auto; padding: 40px 20px;">
            <h1 style="color: #fff; margin-bottom: 20px;">О проекте Crypto AI Hub</h1>
            <div class="article-text" style="color: var(--text-main); font-size: 1.05rem; line-height: 1.8;">
                <p><strong>Crypto AI Hub</strong> — независимый образовательный и технологический портал, посвящённый практическому применению искусственного интеллекта на криптовалютном рынке и безопасному освоению экосистемы Web3.</p>
                <h2>Наша миссия</h2>
                <p>Криптовалютная индустрия перегружена сложным жаргоном и эмоциональными прогнозами. Наша цель — давать читателям понятные пошаговые инструкции, бесплатные аналитические калькуляторы и проверенные промпты для локальных и облачных нейросетей, помогающие принимать взвешенные решения.</p>
                <h2>Редакционные стандарты и проверка фактов</h2>
                <ul>
                    <li><strong>Практическая проверка:</strong> Все пошаговые руководства по биржам, кошелькам, локальным моделям (Ollama, Qwen) и скриптам тестируются перед публикацией.</li>
                    <li><strong>Использование ИИ:</strong> Мы применяем языковые модели для структурирования данных, перевода и первичного анализа новостей, но каждый материал проходит ручную вычитку и редакционную проверку.</li>
                    <li><strong>Актуализация:</strong> Мы регулярно обновляем руководства и еженедельные разделы (включая ответы Binance WOTD) при изменении правил платформ.</li>
                </ul>
                <h2>Раскрытие информации о монетизации</h2>
                <p>Все гайды и инструменты на Crypto AI Hub бесплатны для пользователей. Проект поддерживается за счёт партнёрских программ (включая реферальную программу Binance с бонусной скидкой на комиссии для читателей) и контекстной рекламы. Наличие партнёрских ссылок не влияет на объективность наших обзоров безопасности и предупреждений о рисках.</p>
                <h2>Обратная связь</h2>
                <p>По вопросам сотрудничества, предложений по новым инструментам и сообщениям об ошибках пишите в наш официальный Telegram-канал: <a href="https://t.me/crypto_ai_hub" target="_blank" rel="noopener noreferrer" style="color: #00f2fe;">@crypto_ai_hub</a>.</p>
            </div>
        </div>
    </main>
{RU_FOOTER}
</body>
</html>"""

    # 2. en/about.html (EN)
    about_en = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Crypto AI Hub — Editorial Policy &amp; Mission</title>
    <meta name="description" content="Learn about Crypto AI Hub's mission, editorial fact-checking standards for Web3 and AI content, and affiliate disclosure policy.">
    <link rel="canonical" href="https://crypto-ai-hub.com/en/about.html">
    <link rel="alternate" hreflang="ru" href="https://crypto-ai-hub.com/about.html">
    <link rel="alternate" hreflang="en" href="https://crypto-ai-hub.com/en/about.html">
    <link rel="stylesheet" href="../css/style.css">
    <link rel="icon" type="image/png" sizes="144x144" href="/images/favicon.png">
</head>
<body>
{get_en_header("about.html")}
    <main class="guides-section">
        <div class="container" style="max-width: 820px; margin: 0 auto; padding: 40px 20px;">
            <h1 style="color: #fff; margin-bottom: 20px;">About Crypto AI Hub</h1>
            <div class="article-text" style="color: var(--text-main); font-size: 1.05rem; line-height: 1.8;">
                <p><strong>Crypto AI Hub</strong> is an independent educational and technology portal focused on practical Artificial Intelligence applications in cryptocurrency markets and safe Web3 onboarding.</p>
                <h2>Our Mission</h2>
                <p>The crypto space is often clouded by complex jargon and hype-driven speculation. Our mission is to provide clear step-by-step tutorials, free client-side calculators, and tested prompts for local and cloud LLMs to help users build disciplined, data-driven workflows.</p>
                <h2>Editorial Standards &amp; Fact-Checking</h2>
                <ul>
                    <li><strong>Hands-On Verification:</strong> All tutorials covering exchanges, self-custody wallets, local AI setups (Ollama, Qwen), and Python workflows are tested before publication.</li>
                    <li><strong>AI Transparency:</strong> We use AI tools to assist with translation, structuring, and news summarization, while every published guide undergoes human editorial review.</li>
                    <li><strong>Regular Updates:</strong> Core guides and weekly resources (such as Binance WOTD answers) are updated regularly to reflect current platform rules.</li>
                </ul>
                <h2>Affiliate &amp; Advertising Disclosure</h2>
                <p>All guides and tools on Crypto AI Hub are free to use. The portal is funded through display advertising and partner referral programs (such as Binance fee-discount links). Affiliate partnerships never compromise our security recommendations or risk warnings.</p>
                <h2>Contact Us</h2>
                <p>For partnerships, tool suggestions, or editorial corrections, reach out via our official Telegram community: <a href="https://t.me/crypto_ai_hub" target="_blank" rel="noopener noreferrer" style="color: #00f2fe;">@crypto_ai_hub</a>.</p>
            </div>
        </div>
    </main>
{EN_FOOTER}
</body>
</html>"""

    # 3. privacy.html (RU)
    privacy_ru = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Политика конфиденциальности — Crypto AI Hub</title>
    <meta name="description" content="Политика конфиденциальности портала Crypto AI Hub: обработка файлов cookie, аналитика, сторонние виджеты и защита данных пользователей.">
    <link rel="canonical" href="https://crypto-ai-hub.com/privacy.html">
    <link rel="alternate" hreflang="ru" href="https://crypto-ai-hub.com/privacy.html">
    <link rel="alternate" hreflang="en" href="https://crypto-ai-hub.com/en/privacy.html">
    <link rel="stylesheet" href="css/style.css">
    <link rel="icon" type="image/png" sizes="144x144" href="/images/favicon.png">
</head>
<body>
{get_ru_header()}
    <main class="guides-section">
        <div class="container" style="max-width: 820px; margin: 0 auto; padding: 40px 20px;">
            <h1 style="color: #fff; margin-bottom: 10px;">Политика конфиденциальности</h1>
            <p style="color: var(--text-muted); margin-bottom: 24px;">Последнее обновление: Ноябрь 2026 г.</p>
            <div class="article-text" style="color: var(--text-main); font-size: 1.05rem; line-height: 1.8;">
                <p>Настоящая Политика конфиденциальности описывает, как информационный портал <strong>Crypto AI Hub</strong> (<code>https://crypto-ai-hub.com</code>) обрабатывает техническую информацию при посещении сайта.</p>
                <h2>1. Сбор персональных данных</h2>
                <p>Crypto AI Hub является статическим информационным сайтом и <strong>не требует регистрации</strong>, не запрашивает сид-фразы, приватные ключи, пароли или платёжные реквизиты пользователей. Все калькуляторы на сайте выполняют вычисления локально в вашем браузере.</p>
                <h2>2. Файлы Cookie и сторонние сервисы</h2>
                <p>Для корректной работы графиков, аналитики посещаемости и показа рекламы на сайте могут использоваться сторонние сервисы, применяющие файлы cookie:</p>
                <ul>
                    <li><strong>TradingView:</strong> интерактивный график котировок BTC/USDT на главной странице.</li>
                    <li><strong>Системы веб-аналитики (Google Analytics / Microsoft Clarity):</strong> обезличенная статистика посещений, типов устройств и кликов для улучшения структуры сайта.</li>
                    <li><strong>Рекламные сети (включая Google AdSense):</strong> сторонние поставщики, включая Google, используют файлы cookie для показа объявлений на основе предыдущих посещений пользователями этого или других веб-сайтов.</li>
                </ul>
                <h2>3. Внешние и партнёрские ссылки</h2>
                <p>Сайт содержит ссылки на внешние платформы (Binance, Telegram и др.). После перехода по внешней ссылке пользователь руководствуется политикой конфиденциальности соответствующего ресурса.</p>
                <h2>4. Управление файлами Cookie</h2>
                <p>Вы можете в любой момент отключить или очистить файлы cookie в настройках вашего браузера, а также управлять персонализацией рекламы в настройках рекламных предпочтений Google.</p>
            </div>
        </div>
    </main>
{RU_FOOTER}
</body>
</html>"""

    # 4. en/privacy.html (EN)
    privacy_en = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Privacy Policy — Crypto AI Hub</title>
    <meta name="description" content="Privacy Policy for Crypto AI Hub: information on cookies, third-party widgets, analytics, Google AdSense, and user data protection.">
    <link rel="canonical" href="https://crypto-ai-hub.com/en/privacy.html">
    <link rel="alternate" hreflang="ru" href="https://crypto-ai-hub.com/privacy.html">
    <link rel="alternate" hreflang="en" href="https://crypto-ai-hub.com/en/privacy.html">
    <link rel="stylesheet" href="../css/style.css">
    <link rel="icon" type="image/png" sizes="144x144" href="/images/favicon.png">
</head>
<body>
{get_en_header("privacy.html")}
    <main class="guides-section">
        <div class="container" style="max-width: 820px; margin: 0 auto; padding: 40px 20px;">
            <h1 style="color: #fff; margin-bottom: 10px;">Privacy Policy</h1>
            <p style="color: var(--text-muted); margin-bottom: 24px;">Last Updated: November 2026</p>
            <div class="article-text" style="color: var(--text-main); font-size: 1.05rem; line-height: 1.8;">
                <p>This Privacy Policy explains how <strong>Crypto AI Hub</strong> (<code>https://crypto-ai-hub.com</code>) handles technical data when you browse our website.</p>
                <h2>1. Personal Data Collection</h2>
                <p>Crypto AI Hub is a static educational portal. We <strong>do not require user registration</strong> and never ask for seed phrases, private keys, wallet connections, or payment details. All calculators on this website run locally inside your browser.</p>
                <h2>2. Cookies and Third-Party Services</h2>
                <p>To display live market charts, analyze traffic, and serve advertisements, the website may rely on third-party providers that use cookies:</p>
                <ul>
                    <li><strong>TradingView:</strong> embedded BTC/USDT price chart widget on the homepage.</li>
                    <li><strong>Web Analytics (Google Analytics / Microsoft Clarity):</strong> aggregated, anonymized usage statistics to improve content quality and navigation.</li>
                    <li><strong>Advertising Partners (including Google AdSense):</strong> third-party vendors, including Google, use cookies to serve ads based on a user's prior visits to this website or other websites.</li>
                </ul>
                <h2>3. External &amp; Affiliate Links</h2>
                <p>Our articles and tools contain links to external platforms (such as Binance and Telegram). Once you leave Crypto AI Hub, your interaction is governed by the privacy policy of the destination website.</p>
                <h2>4. Managing Cookies</h2>
                <p>You can disable or clear cookies at any time through your browser settings, and you may opt out of personalized advertising by visiting Google Ads Settings.</p>
            </div>
        </div>
    </main>
{EN_FOOTER}
</body>
</html>"""

    files = {
        os.path.join(PROJECT_DIR, "about.html"): about_ru,
        os.path.join(EN_DIR, "about.html"): about_en,
        os.path.join(PROJECT_DIR, "privacy.html"): privacy_ru,
        os.path.join(EN_DIR, "privacy.html"): privacy_en,
    }

    for path, content in files.items():
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        logging.info(f"✅ Создана страница доверия: {os.path.relpath(path, PROJECT_DIR)}")


if __name__ == "__main__":
    build_pages()
