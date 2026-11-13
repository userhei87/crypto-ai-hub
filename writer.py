import os
import re
import logging
from ollama import Client

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
GUIDES_DIR = os.path.join(PROJECT_DIR, "guides")

BINANCE_REF_URL = "https://www.binance.com/register?ref=SHARA10"

# =========================================================================
# КОНФИГУРАЦИЯ ДЛЯ НОВОГО ГАЙДА (МЕНЯЙТЕ ЭТИ ПАРАМЕТРЫ ПЕРЕД ЗАПУСКОМ)
# =========================================================================
TOPIC = "Психология криптотрейдинга и ИИ: Как победить FOMO и тильт с помощью алгоритмов"
file_name = "crypto-trading-psychology.html"
img_name = "crypto-trading-psychology.png"
# =========================================================================

PROMPT = f"""
Ты профессиональный SEO-копирайтер и эксперт в Web3. 
Напиши подробную, понятную пошаговую статью для новичков на тему: "{TOPIC}".
Статья должна быть на русском языке.

СТРОГИЕ ПРАВИЛА ОФОРМЛЕНИЯ (НАРУШЕНИЕ ЗАПРЕЩЕНО):
1. ЗАПРЕЩЕНО использовать Markdown! Никаких звёздочек (**), решёток (#) или дефисов (-) для списков.
2. Выдавай ТОЛЬКО чистый текст статьи, БЕЗ каких-либо оберток ```html или приветствий от ИИ.
3. Обязательно используй стандартные HTML-теги для структуры текста:
   - <h2>Главные заголовки разделов</h2>
   - <h3>Подзаголовки шагов или подразделов</h3>
   - <p>Обычные абзацы текста</p>
   - <strong>Важные термины или предупреждения</strong>
   - <ul> и <li> для списков.
4. Если приводишь пример системного промпта или кода, оберни его в <pre><code>...</code></pre>. Внутри этих тегов должен быть ИСКЛЮЧИТЕЛЬНО чистый текст без HTML-тегов.
5. Пиши максимально доступно, пошагово, избегая сложного сленга. Упомяни важность использования локальных моделей (например, семейства Qwen через Ollama) для холодного анализа рынка.
6. При упоминании биржи Binance используй ссылку: <a href="{BINANCE_REF_URL}" target="_blank" rel="noopener noreferrer">официальный сайт Binance</a>.
"""

def clean_and_fix_html(raw_text):
    """Автоматически чистит случайный Markdown от ИИ и оборачивает абзацы в HTML."""
    # Убираем случайные обёртки кода
    text = re.sub(r'^```html\s*|\s*```$', '', raw_text.strip(), flags=re.MULTILINE)
    
    # Заменяем **жирный текст** на <strong>жирный текст</strong>
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    
    lines = text.split('\n')
    formatted_lines = []
    in_list = False
    in_pre = False
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
            
        # Не трогаем строки внутри блоков <pre><code>
        if '<pre>' in stripped:
            in_pre = True
        if in_pre:
            formatted_lines.append(line)
            if '</pre>' in stripped:
                in_pre = False
            continue

        # Превращаем строки с "- " в HTML-списки
        if stripped.startswith('- '):
            if not in_list:
                formatted_lines.append('<ul>')
                in_list = True
            formatted_lines.append(f'<li>{stripped[2:]}</li>')
        else:
            if in_list:
                formatted_lines.append('</ul>')
                in_list = False
            # Оборачиваем голый текст в <p>, если он не начинается с тега
            if not stripped.startswith('<'):
                formatted_lines.append(f'<p>{stripped}</p>')
            else:
                formatted_lines.append(stripped)
                
    if in_list:
        formatted_lines.append('</ul>')
        
    return '\n'.join(formatted_lines)

def generate_article():
    logging.info("🤖 Подключаюсь к локальной Ollama...")
    logging.info(f"⏳ Видеокарта GTX 1070 начала генерацию текста для: {TOPIC}")
    
    if not os.path.exists(GUIDES_DIR):
        os.makedirs(GUIDES_DIR)
    
    try:
        client = Client()
        response = client.generate(model='qwen2.5-coder:7b', prompt=PROMPT)
        
        # Прогоняем ответ модели через наш фильтр-чистильщик
        article_content = clean_and_fix_html(response['response'])
        
        html_template = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{TOPIC} — CryptoAI Hub</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <header class="navbar">
        <div class="container">
            <a href="../index.html" class="logo">Crypto<span>AI</span> Hub</a>
            <nav class="nav-links">
                <a href="../index.html" class="nav-link">Главная</a>
                <a href="../index.html#guides-section" class="nav-link">Гайды</a>
                <a href="../news.html" class="nav-link">Новости</a>
                <a href="../disclaimer.html" class="nav-link">Дисклеймер</a>
                <a href="{BINANCE_REF_URL}" target="_blank" rel="noopener noreferrer" class="btn-ref">Регистрация на Binance</a>
            </nav>

        </div>
    </header>

    <main class="guides-section">
        <div class="container" style="max-width: 800px; margin: 0 auto; padding: 40px 20px;">
                        
            <div class="article-cover" style="margin-bottom: 30px; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
                <img src="{img_name}" alt="{TOPIC}" style="width: 100%; max-height: 450px; object-fit: cover; display: block;">
            </div>

            <div class="promo-banner-inline" style="background: linear-gradient(135deg, #1e2026, #2b3139); border-left: 4px solid #f3ba2f; padding: 25px; border-radius: 8px; margin-bottom: 30px; box-shadow: 0 4px 15px rgba(0,0,0,0.2); text-align: center;">
                <h4 style="color: #f3ba2f; margin: 0 0 12px 0; font-size: 1.2rem; font-weight: 600;">🔥 Бонус для читателей CryptoAI Hub</h4>
                <p style="color: #eaeaea; margin: 0 0 20px 0; font-size: 0.95rem; line-height: 1.6;">Регистрируйтесь на Binance по нашей ссылке и получите постоянную скидку 10% на все спотовые комиссии, а также приветственный инвесторский бонус до $100.</p>
                <a href="{BINANCE_REF_URL}" target="_blank" rel="noopener noreferrer" style="display: inline-block; background: #f3ba2f; color: #000; padding: 12px 24px; border-radius: 4px; text-decoration: none; font-weight: bold; font-size: 0.95rem; transition: background 0.2s; margin: 0 auto;">Получить скидку 10% на Binance &rarr;</a>
            </div>

            <div class="article-text" style="color: var(--text-main); font-size: 1.1rem; line-height: 1.8;">
                {article_content}
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

        file_path = os.path.join(GUIDES_DIR, file_name)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_template)
            
        logging.info(f"🎉 Гайд успешно сгенерирован, очищен от Markdown и сохранен в: guides/{file_name}")

    except Exception as e:
        logging.error(f"Произошла ошибка при работе скрипта: {e}")

if __name__ == "__main__":
    generate_article()
