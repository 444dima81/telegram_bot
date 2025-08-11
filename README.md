## Как запустить бота:
### 1. Клонируй репозиторий 

git clone git@github.com:444dima81/telegram_bot.git

cd my_bot # зайти в папку


### 2. Вставь свой токен в строку
- Скопируй свой токен у бота *BotFather* 
- Зайди в файл file.env и вставь свой токен в строку ENV TOKEN=...

ВАЖНО: не используй пробелы и ковычки

### 3. Собери и запусти
Открой командную строку 

docker build -t telegram_translit_bot . # построение образа 

docker run -d --name telegram_translit_bot --env-file .env telegram_translit_bot # запуск контейнера


### 4. Проверьте бота


### 5. Проверка логов
docker logs -f telegram_translit_bot

### 6. Остановка бота
docker stop telegram_translit_bot # Остановка

docker rm telegram_translit_bot # удаление контейнера
