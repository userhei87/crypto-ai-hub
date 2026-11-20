import os
import requests
from bs4 import BeautifulSoup

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
GUIDES_DIR = os.path.join(ROOT_DIR, "guides")

# Эталонные партнёрские ссылки проекта
EXPECTED_BINANCE_URL = "https://www.binance.com/register?ref=SHARA10"
EXPECTED_FIREFAUCET_URL = "https://firefaucet.win/ref/Faust2021"
EXPECTED_VIEFAUCET_URL = "https://viefaucet.com?r=689a30c473bd65014088c45a"

def check_url(url):
    """Проверяет внешнюю ссылку на код ответа сервера."""
    if url.startswith("#") or not url.startswith("http"):
        return True
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
        }
        response = requests.head(url, timeout=7, headers=headers, allow_redirects=True)
        if response.status_code >= 400:
            response = requests.get(url, timeout=7, headers=headers, allow_redirects=True)
        # Код 403 часто отдаёт защита Cloudflare у криптокранов, для браузера ссылка рабочая
        if response.status_code == 403 and ("firefaucet" in url or "viefaucet" in url):
            return True
        return response.status_code < 400
    except Exception:
        return False

def check_file_links(file_path):
    """Сканирует HTML-файл на битые ссылки и проверяет реферальные коды."""
    if not os.path.exists(file_path):
        return
    
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    
    rel_path = os.path.relpath(file_path, ROOT_DIR)
    print(f"\n🔍 Сканирование файла: {rel_path}")
    
    broken_count = 0
    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"].strip()
        
        # 1. Проверка внутренних относительных ссылок хаба
        if not href.startswith("http") and not href.startswith("#"):
            clean_href = href.split("#")[0]
            
            if clean_href.startswith("guides/"):
                target_path = os.path.join(ROOT_DIR, clean_href)
            elif rel_path.startswith("guides") and not clean_href.startswith(".."):
                target_path = os.path.join(GUIDES_DIR, clean_href)
            else:
                target_path = os.path.join(ROOT_DIR, clean_href.replace("../", ""))
                
            if not os.path.exists(target_path):
                print(f"❌ Битая внутренняя ссылка: '{href}' (Файл не найден на диске)")
                broken_count += 1
                
        # 2. Проверка внешних ссылок и точного совпадения реферальных URL
        elif href.startswith("http"):
            if "binance.com" in href.lower() and href != EXPECTED_BINANCE_URL:
                print(f"⚠️ Неверная ссылка Binance: '{href}' (Ожидается: {EXPECTED_BINANCE_URL})")
                broken_count += 1
            elif "firefaucet.win" in href.lower() and href != EXPECTED_FIREFAUCET_URL:
                print(f"⚠️ Неверная ссылка Fire Faucet: '{href}' (Ожидается: {EXPECTED_FIREFAUCET_URL})")
                broken_count += 1
            elif "viefaucet.com" in href.lower() and href != EXPECTED_VIEFAUCET_URL:
                print(f"⚠️ Неверная ссылка Vie Faucet: '{href}' (Ожидается: {EXPECTED_VIEFAUCET_URL})")
                broken_count += 1

            if not check_url(href):
                print(f"❌ Битая внешняя ссылка: '{href}' (Сервер недоступен или вернул ошибку)")
                broken_count += 1
                
    if broken_count == 0:
        print("✅ Все ссылки и реферальные коды в файле исправны!")

def main():
    print("=" * 65)
    print("   CRYPTO-AI HUB — ПРОВЕРКА ССЫЛОК И РЕФЕРАЛЬНЫХ КОДОВ")
    print("=" * 65)
    
    # Проверяем все корневые страницы сайта
    root_pages = ["index.html", "news.html", "prompts.html", "calculator.html", "partners.html", "disclaimer.html"]
    for page in root_pages:
        check_file_links(os.path.join(ROOT_DIR, page))
    
    # Проверяем все гайды в папке guides/
    if os.path.exists(GUIDES_DIR):
        for file in sorted(os.listdir(GUIDES_DIR)):
            if file.endswith(".html"):
                check_file_links(os.path.join(GUIDES_DIR, file))
                
    print("\n🏁 Проверка завершена.")

if __name__ == "__main__":
    main()
