from aiogram import Bot, Dispatcher, executor, types
from fonk import *
from keyboard import *
from config import *


bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot=bot)

horoscopes = {
    'козоріг♑': f'Гороскоп для Козорога на 2024: {capricorn}',
    'водолій♒': f'Гороскоп для Водолія на 2024: {aquarius}',
    'риби♓': f'Гороскоп для Риб на 2024: {pisces}',
    'овен♈': f'Гороскоп для Овна на 2024: {aries}',
    'телець♉': f'Гороскоп для Тельця на 2024: {taurus}',
    'близнюки♊': f'Гороскоп для Близнюків на 2024: {gemini}',
    'рак♋': f'Гороскоп для Рака на 2024: {cancer}',
    'лев♌': f'Гороскоп для Лева на 2024: {leo}',
    'діва♍': f'Гороскоп для Діви на 2024: {virgo}',
    'терези♎': f'Гороскоп для Терез на 2024: {libra}',
    'скорпіон♏': f'Гороскоп для Скорпіона на 2024: {scorpio}',
    'стрілець♐': f'Гороскоп для Стрільця на 2024: {sagittarius}',
}

@dp.message_handler(commands=['start'])
async def start_hello(message: types.Message):
    await message.answer(text=START_HELLO, reply_markup=start_menu_list)


@dp.message_handler(commands=['menu'])
@dp.message_handler(text='Повернутися до меню')
async def get_menu(message: types.Message):
    await message.answer(text=MENU, reply_markup=start_menu_list)


@dp.message_handler(text=['Дізнатися свій знак зодіаку 🌟', 'Ще раз'])
async def find_zz(message: types.Message):
    await message.answer(text=FIND)


@dp.message_handler(text='Подивитися свій гороскоп 🔮')
async def get_horoscope(message: types.Message):
    await message.answer(text="Натисни на свій знак зодіаку.",
                         reply_markup=stage1)


@dp.message_handler(text='Подивитися сумісність 💞')
async def compatibility_zs(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    url_button = InlineKeyboardButton(text="Подивитись на долю", url="https://testometrika.com/funny/zodiac-compatibility-test/")
    keyboard.add(url_button)
    await message.answer("Натисніть щоб подивитися сумісність:",
                         reply_markup=keyboard)


@dp.message_handler()
async def handle_message(message: types.Message):
    data = message.text
    if len(data) == 5:
        result = zodiac_find(message.text)
        await message.answer(text=(f'Ваш знак зодіаку - {result}'),
                             reply_markup=find_list)
    elif message.text in horoscopes:
        horoscope_text = horoscopes[message.text]
        await message.answer(horoscope_text,
                             reply_markup=select_list)
    else:
        await message.answer(text=FAULT)


@dp.message_handler(text='Подивитися сумісність 💞')
async def compatibility_zs(message: types.Message):
    await message.answer(text=COMPATIBILITY)


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           allowed_updates=["message", "inline_query", "callback_query"])