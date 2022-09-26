import telebot
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

token='5592857252:AAF_-Hpfwgn9yXazGnj6SmvucLZ9aJT-ooY'
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
    #bot.send_message(chat_id=chatid,text=message)
    print(f'ID del usuario: {message.from_user.id}')
    print(f'ID del chat: {chatid}')
    print(f'mensaje recibido: {message.text}')
    if (message.text == 'prueba'):
        bot.send_message(chat_id=chatid,text='mensaje desde el bot 1')
    # try:
    #     opciones.index(message.text)

    # except:
    #     pass
    # finally:
    #     bot.delete_message(chat_id=chatid, message_id=messageid)


#bot.polling(skip_pending=True, timeout=TIMEOUT)

def my_interval_job():
    bot.send_message(chat_id=-1001544949758, text="Hello. its 6am!")
    #bot.stop_polling()
    bot.polling(skip_pending=True, timeout=TIMEOUT)
    
    

# sched.add_job(my_interval_job, 'interval',minutes=0.1,replace_existing=True)
# sched.start()


#bot.infinity_polling(skip_pending=True, timeout=TIMEOUT)
#bot.polling(skip_pending=True, timeout=TIMEOUT, non_stop=True)
#bot.stop_polling()
# a=0
# while True:
#     a=a+1
#     bot.polling(skip_pending=True, timeout=TIMEOUT)
#     print(a)
while True:
    bot.polling(skip_pending=True, timeout=TIMEOUT)
    #bot.stop_polling()
    bot.send_message(chat_id=-1001544949758, text="Prueba1")

xd = {'content_type': 'text', 'id': 4, 'message_id': 4, 
'from_user': {'id': 1262315361, 'is_bot': False, 'first_name': 'Mortadelo', 'username': None, 
'last_name': None, 'language_code': 'es', 'can_join_groups': None, 
'can_read_all_group_messages': None, 'supports_inline_queries': None, 
'is_premium': None, 'added_to_attachment_menu': None}, 'date': 1662519774, 
'chat': {'id': -1001544949758, 'type': 'supergroup', 'title': 'xd2.0', 
'username': None, 'first_name': None, 'last_name': None, 'photo': None, 
'bio': None, 'join_to_send_messages': None, 'join_by_request': None, 
'has_private_forwards': None, 'has_restricted_voice_and_video_messages': None, 
'description': None, 'invite_link': None, 'pinned_message': None, 'permissions': None, 
'slow_mode_delay': None, 'message_auto_delete_time': None, 'has_protected_content': None, 
'sticker_set_name': None, 'can_set_sticker_set': None, 'linked_chat_id': None, 
'location': None}, 'sender_chat': None, 'forward_from': None, 'forward_from_chat': None, 
'forward_from_message_id': None, 'forward_signature': None, 'forward_sender_name': None, 
'forward_date': None, 'is_automatic_forward': None, 'reply_to_message': None, 
'via_bot': None, 'edit_date': None, 'has_protected_content': None, 'media_group_id': None, 
'author_signature': None, 'text': 'atat', 'entities': None, 'caption_entities': None, 
'audio': None, 'document': None, 'photo': None, 'sticker': None, 'video': None, 
'video_note': None, 'voice': None, 'caption': None, 'contact': None, 'location': None, 
'venue': None, 'animation': None, 'dice': None, 'new_chat_member': None, 
'new_chat_members': None, 'left_chat_member': None, 'new_chat_title': None, 
'new_chat_photo': None, 'delete_chat_photo': None, 'group_chat_created': None, 
'supergroup_chat_created': None, 'channel_chat_created': None, 'migrate_to_chat_id': None, 
'migrate_from_chat_id': None, 'pinned_message': None, 'invoice': None, 
'successful_payment': None, 'connected_website': None, 'reply_markup': None, 
'json': {'message_id': 4, 'from': {'id': 1262315361, 'is_bot': False, 
'first_name': 'Mortadelo', 'language_code': 'es'}, 'chat': {'id': -1001544949758, 
'title': 'xd2.0', 'type': 'supergroup'}, 'date': 1662519774, 'text': 'atat'}}