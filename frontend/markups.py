from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


candy = KeyboardButton('/candy')
mosaic = KeyboardButton('/mosaic')
starry_night= KeyboardButton('/starry_night')
feathers = KeyboardButton('/feathers')
la_muse = KeyboardButton('/la_muse')
result = KeyboardButton('/result')


mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(candy, mosaic, starry_night, feathers, la_muse, result)


