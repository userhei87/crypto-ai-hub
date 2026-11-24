import os

EN_DIR = "en"
count = 0

for root, dirs, files in os.walk(EN_DIR):
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            
            if "querySelector('.menu-toggle')" in content:
                content = content.replace("querySelector('.menu-toggle')", "querySelector('button.menu-toggle')")
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)
                count += 1

print(f"✅ Кнопка Menu исправлена в {count} английских файлах!")
