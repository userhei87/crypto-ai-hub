import os
from datetime import datetime

# НАСТРОЙКА: Замените 'ВАШ_НИКНЕЙМ' на ваш логин на GitHub после регистрации
BASE_URL = "https://userhei87.github.io/crypto-ai-hub" 

def generate_sitemap():
    print("🤖 Запуск генерации sitemap.xml...")
    
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    current_date = datetime.today().strftime('%Y-%m-%d')
    
    # 1. Добавляем главную страницу
    if os.path.exists("index.html"):
        xml_content += f"  <url>\n"
        xml_content += f"    <loc>{BASE_URL}/index.html</loc>\n"
        xml_content += f"    <lastmod>{current_date}</lastmod>\n"
        xml_content += f"    <priority>1.0</priority>\n"
        xml_content += f"  </url>\n"
        print(" -> Добавлен в карту: index.html")
    
    # [НОВОЕ] 2. Добавляем страницу новостей из корня проекта
    if os.path.exists("news.html"):
        xml_content += f"  <url>\n"
        xml_content += f"    <loc>{BASE_URL}/news.html</loc>\n"
        xml_content += f"    <lastmod>{current_date}</lastmod>\n"
        xml_content += f"    <priority>0.9</priority>\n"
        xml_content += f"  </url>\n"
        print(" -> Добавлен в карту: news.html")

    # 3. Сканируем папку guides/
    guides_dir = "guides"
    if os.path.exists(guides_dir):
        for file in os.listdir(guides_dir):
            if file.endswith(".html"):
                xml_content += f"  <url>\n"
                xml_content += f"    <loc>{BASE_URL}/guides/{file}</loc>\n"
                xml_content += f"    <lastmod>{current_date}</lastmod>\n"
                xml_content += f"    <priority>0.8</priority>\n"
                xml_content += f"  </url>\n"
                print(f" -> Добавлен в карту: guides/{file}")
                
    xml_content += "</urlset>\n"
    
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(xml_content)
        
    print("✅ Файл sitemap.xml успешно создан в корне проекта!")

if __name__ == "__main__":
    generate_sitemap()
