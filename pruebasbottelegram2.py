import telebot

token='5527887301:AAH67sGGa5NMyxU823UE5EqiTtBTKmgduLs'
bot = telebot.TeleBot(token, parse_mode=None)
TIMEOUT=2

@bot.message_handler(commands=['id'])
def send_welcome(message):
    message.text
    chatid = message.chat.id
    bot.reply_to(message, f"su ID es: {chatid}")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    message.text
    chatid = message.chat.id

@bot.callback_query_handler(func=lambda call: True)
def manejador_seleccion(call):

    chat_id = call.message.chat.id
    print('call')
    print(call)


@bot.message_handler(func=lambda message: True)
def manejador_seleccion(message):
	
    chatid=message.chat.id
    messageid=message.id
    message.text
    #print('message')
    print(f'ID del usuario: {message.from_user.id}')
    print(f'ID del chat: {chatid}')
    print(f'mensaje recibido: {message.text}')
    if (message.text == 'mensaje desde el bot 1'):
        bot.send_message(chat_id=chatid,text='mensaje desde el bot 2')
    # try:
    #     opciones.index(message.text)

    # except:
    #     pass
    # finally:
    #     bot.delete_message(chat_id=chatid, message_id=messageid)


#bot.polling(skip_pending=True, timeout=TIMEOUT)
bot.infinity_polling(skip_pending=True, timeout=TIMEOUT)
bot.stop_polling()
