import logging
from aiogram.utils import executor
from aiogram import types

from BotCreate import dp,bot
from TableCreate import createTables
from dbsql import Database,create_connection


async def on_startup(_):
    print('Bot вышел в online ...')

async def on_shutdown(_):
    print('Bot закончил работу ...')

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
)
logger.info("Bot запускается")


createTables('primer.db')    # из  TableCreate.py       создание базы и таблиц

baz = Database('primer.db')  # из dbsql.py


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type=='private':
        print(message.from_user.id,baz.user_exists(message.from_user.id))
        if not baz.user_exists(message.from_user.id):
            baz.add_user(message.from_user.id,message.from_user.full_name)
            await bot.send_message(message.from_user.id,"Tanishganimdan hursandman!")

@dp.message_handler(commands=['sendall'])
async def sendall(message: types.Message):
    if message.chat.type=='private':
        if message.from_user.id==139204666:
            text=message.text[9:]
            users=baz.get_users()

            for row in users:
                if row[2] == None:
                    row[2] = ''

                try:
                    await  bot.send_message(row[0],text)
                    if int(row[1]) !=1 :
                        baz.set_active(row[0],1)
                    await bot.send_message(message.from_user.id,'Успешная рассылка'+' '+ str(row[0]) )
                    print("Рассылка юзеру "+str(row[0])+" "+row[2])
                except:
                    baz.set_active(row[0], 0)
                    print("Юзер "+str(row[0]) +" "+row[2] +" не активен")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
