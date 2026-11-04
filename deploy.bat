@echo off
chcp 65001 > nul
echo 🤖 Шаг 1: Пересборка карты сайта...
python sitemap_gen.py

echo 🚀 Шаг 2: Отправка обновлений на живой сервер GitHub Pages...
git add .
git commit -m "Automated content update and grid synchronization"
git push origin main

echo 🎉 Готово! Сайт успешно обновлен и будет доступен в сети через минуту.
pause
