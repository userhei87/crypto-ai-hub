import os
import requests
from bs4 import BeautifulSoup

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
GUIDES_DIR = os.path.join(ROOT_DIR, "guides")

def check_url(url):
    """Проверяет внешнюю ссылку на код ответа сервера."""
    if url.startswith("#") or not url.startswith("http"):
        return True
    try:
        # Отправляем HEAD запрос, чтобы не качать всю страницу целиком
        response = requests.head(url, timeout=5, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code >= 400:
            # Если HEAD не разрешен сервером, перепроверяем через GET
            response = requests.get(url, timeout=5, headers={"User-Agent": "Mozilla/5.0"})
        return response.status_code < 400
    except Exception:
        return False

def check_file_links(file_path):
    """Сканирует HTML-файл на битые ссылки."""
    if not os.path.exists(file_path):
        return
    
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    
    rel_path = os.path.relpath(file_path, ROOT_DIR)
    print(f"\n🔍 Сканирование файла: {rel_path}")
    
    broken_count = 0
    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        
        # 1. Проверка внутренних относительных ссылок хаба
        if not href.startswith("http") and not href.startswith("#"):
            # Отсекаем HTML-якорь (#), если он есть в ссылке
            clean_href = href.split("#")[0]
            
            # Вычисляем физический путь к файлу на диске
            if clean_href.startswith("guides/"):
                target_path = os.path.join(ROOT_DIR, clean_href)
            elif rel_path.startswith("guides") and not clean_href.startswith(".."):
                target_path = os.path.join(GUIDES_DIR, clean_href)
            else:
                target_path = os.path.join(ROOT_DIR, clean_href.replace("../", ""))
                
            if not os.path.exists(target_path):
                print(f"❌ Битая внутренняя ссылка: '{href}' (Файл не найден на диске)")
                broken_count += 1
                
        # 2. Проверка внешних ссылок (включая реферальные ссылки Binance)
        elif href.startswith("http"):
            if not check_url(href):
                print(f"❌ Битая внешняя ссылка: '{href}' (Сервер вернул ошибку)")
                broken_count += 1
                
    if broken_count == 0:
        print("✅ Все ссылки в файле исправны!")

def main():
    print("=" * 60)
    print("       CRYPTO-AI HUB — СИСТЕМА ПРОВЕРКИ РАБОТОСПОСОБНОСТИ URL")
    print("=" * 60)
    
    # Проверяем главную страницу
    check_file_links(os.path.join(ROOT_DIR, "index.html"))
    
    # Проверяем все гайды в папке guides/
    if os.path.exists(GUIDES_DIR):
        for file in os.listdir(GUIDES_DIR):
            if file.endswith(".html"):
                check_file_links(os.path.join(GUIDES_DIR, file))
                
    print("\n🏁 Проверка завершена.")

if __name__ == "__main__":
    main()
