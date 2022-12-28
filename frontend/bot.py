from aiogram import Bot, Dispatcher, executor, types
import requests
import markups as nav
from PIL import Image

bot = Bot(token = "5611032277:AAGSzCM2yqOXbeB5mIg2wfaOKHn0yTdGH8k")
db = Dispatcher(bot)

style = 'candy'
@db.message_handler(commands=['start'])
async def welcome(msg: types.Message):
    await msg.answer("To style your image, choose a style from the menu !",reply_markup = nav.mainMenu)

@db.message_handler(commands=['candy'])
async def welcome(msg: types.Message):
    global style
    style = "candy"
    await msg.answer("You chose candy style , send your image!")

@db.message_handler(commands=['mosaic'])
async def welcome(msg: types.Message):
    global style
    style = "mosaic"
    await msg.answer("You chose mosaic style , send your image!")

@db.message_handler(commands=['starry_night'])
async def welcome(msg: types.Message):
    global style
    style = "starry_night"
    await msg.answer("You chose starry night style , send your image!")

@db.message_handler(commands=['feathers'])
async def welcome(msg: types.Message):
    global style
    style = "feathers"
    await msg.answer("You chose feathers style , send your image!")

@db.message_handler(commands=['la_muse'])
async def welcome(msg: types.Message):
    global style
    style = "la_muse"
    await msg.answer("You chose la_muse style , send your image!")

@db.message_handler(content_types=['photo'])
async def handle_docs_photo(message):
    await message.photo[-1].download('D:/test.jpg')

    with open('D:/test.jpg', 'rb') as f:
        byte_im = f.read()
    files = {"file": byte_im}
    global style
    res = requests.post(f"http://localhost:8080/{style}", files=files)



@db.message_handler(commands=['result'])
async def handle_send(msg: types.Message):
    await bot.send_photo(chat_id=msg.chat.id, photo=open("D:/YASS.jpg", 'rb'))

executor.start_polling(db)