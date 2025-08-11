# импорт
import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

# Создание логирования
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# формат логов
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

# логирование в файл бот.лог
file_handler = logging.FileHandler('bot.log', encoding='utf-8')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# логирование в консоль
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# Токен, попытка поиска ошибки
TOKEN = os.getenv('TOKEN')
if not TOKEN:
    raise ValueError("TOKEN environment variable is not set")

# иницаилизация бота
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Словарь правил
TRANSLIT_DICT = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'ZH',
    'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O',
    'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'KH', 'Ц': 'TS',
    'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH', 'Ы': 'Y', 'Ъ': 'IE', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA',
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh',
    'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
    'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts',
    'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'y', 'ъ': 'ie', 'э': 'e', 'ю': 'iu', 'я': 'ia'
}

# функция замены букв
def transliterate(text: str) -> str:
    return ''.join(TRANSLIT_DICT.get(char, char) for char in text)

# обработчик старт
@dp.message(Command('start'))
async def process_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}!'
    logging.info(f'{user_name} ({user_id}) запустил бота')
    await message.answer(text)

# обработчик сообщений
@dp.message()
async def send_ru_to_lat(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    logging.info(f'Сообщение от {user_name} ({user_id}): {text}')
    
    translit_text = transliterate(text)
    logging.info(f'Транслитерированный текст: {translit_text}')
    await message.answer(translit_text)

# заупск бота
if __name__ == '__main__':
    import asyncio
    asyncio.run(dp.run_polling(bot))