import os
import logging
from datetime import datetime
from ollama import Client

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BINANCE_REF_URL = "https://binance.com"

# =========================================================================
# ПОДГОТОВКА И КОНФИГУРАЦИЯ НОВОСТИ
# =========================================================================
RAW_NEWS_TEXT = """
On November 13, 2026, the U.S. Justice Department and FBI announced they disrupted a massive $400 million North Korean crypto scam network that used AI-generated deepfakes and fake video meetings to steal digital assets over 18 months. 
Authorities seized cloud servers used by the hackers to impersonate executives and trick victims into transferring funds or exposing private keys. 
Security experts warn that AI-powered social engineering is becoming the primary threat in Web3 during market volatility, urging users to verify contacts strictly and store assets safely.
"""
NEWS_CATEGORY = "🚨 ИИ & Безопасность"
# =========================================================================

# 2. Укажите категорию (например: 🔥 Громкое событие, 📈 Тренды ИИ, ⚡ Важно)
NEWS_CATEGORY = "🔥 Громкое событие"
# =========================================================================

PROMPT = f"""
Ты профессиональный SEO-копирайтер и эксперт в Web3. 
Твоя задача — взять сырой текст новости, перевести его на русский язык, сделать глубокий качественный рерайт и оформить его в виде готовой статьи для статического сайта.

Исходная новость для обработки:
"{RAW_NEWS_TEXT}"

Используй строгие правила генерации:
1. Выдай мне готовый заголовок в теге <h2> и тело новости, разбитое на 1-2 абзаца в тегах <p>.
2. Оформление должно быть в виде чистого HTML. Выдавай ТОЛЬКО текст новости, БЕЗ каких-либо оберток ```html, markdown-разметки или приветствий от ИИ.
3. Текст должен быть емким, профессиональным и аналитическим. Свяжи новость с общим развитием рынка ИИ или криптовалют в конце 2026 года.
4. Если в тексте ты упоминаешь биржу Binance, ОБЯЗАТЕЛЬНО делай это в виде ссылки: <a href="{BINANCE_REF_URL}" target="_blank" rel="noopener noreferrer">официальный сайт Binance</a>.
"""

def generate_news_block():
    logging.info("🤖 Подключаюсь к локальной Ollama...")
    logging.info("⏳ Видеокарта GTX 1070 начала обработку и рерайт новости. Пожалуйста, подождите...")
    
    try:
        client = Client()
        response = client.generate(model='qwen2.5-coder:7b', prompt=PROMPT)
        news_content = response['response'].strip()
        
        # Автоматически определяем сегодняшнюю дату
        current_date = datetime.now().strftime("%d.%m.%Y")
        
        # Собираем готовую новостную карточку для вставки
        news_card_template = f"""
                <!-- NEWS_CARD_START -->
                <article class="news-card" style="background: #1e2026; border: 1px solid #2b3139; padding: 25px; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.2); margin-bottom: 25px;">
                    <div class="news-meta" style="color: #f3ba2f; font-size: 0.85rem; margin-bottom: 10px; font-weight: bold; text-transform: uppercase;">{NEWS_CATEGORY} • {current_date}</div>
                    <div class="news-body-content" style="color: var(--text-main); font-size: 1.05rem; line-height: 1.7;">
                        {news_content}
                    </div>
                </article>
                <!-- NEWS_CARD_END -->
"""
        
        # Путь к файлу-ленте новостей в корне хаба
        news_hub_path = os.path.join(PROJECT_DIR, "news.html")
        
        if not os.path.exists(news_hub_path):
            logging.error("❌ Файл news.html не найден в корне проекта! Сначала создайте его.")
            return

        with open(news_hub_path, "r", encoding="utf-8") as f:
            content = f.read()

        marker = "<!-- START_CRYPTO_AI_NEWS -->"
        if marker not in content:
            logging.error(f"❌ Внутри news.html не найден маркер автоматизации: {marker}")
            return

        # Вставляем свежую новость сразу под маркером автоматизации (чтобы новые новости шли сверху вниз)
        updated_content = content.replace(marker, f"{marker}\n{news_card_template}")

        with open(news_hub_path, "w", encoding="utf-8") as f:
            f.write(updated_content)

        logging.info("🎉 Новость успешно сгенерирована, отформатирована и добавлена на страницу news.html!")

    except Exception as e:
        logging.error(f"Произошла ошибка при работе скрипта: {e}")

if __name__ == "__main__":
    generate_news_block()
