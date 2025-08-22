from telebot import TeleBot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from logic import *
from config import *

bot = TeleBot(API_TOKEN)

manager = DB_Manager(DATABASE)

reg_keyboard = InlineKeyboardMarkup(row_width=1)
reg_keyboard.add(
    InlineKeyboardButton(text='Как оформить заказ?', callback_data='1'),
    InlineKeyboardButton(text='Как узнать статус моего заказа?', callback_data='2',),
    InlineKeyboardButton(text='Как отменить заказ?', callback_data='3',),
    InlineKeyboardButton(text='Что делать, если товар пришел поврежденным?', callback_data='4',),
    InlineKeyboardButton(text='Как связаться с вашей технической поддержкой?', callback_data='5',),
    InlineKeyboardButton(text='Как узнать информацию о доставке?', callback_data='6',),
InlineKeyboardButton(text='другой вариант', callback_data='7',))

reg_keyboard2 = InlineKeyboardMarkup(row_width=1)
reg_keyboard2.add(
    InlineKeyboardButton(text='Проблема с сайтом или оплатой', callback_data='7_1'),
    InlineKeyboardButton(text='Проблема с товаром', callback_data='7_2',))

@bot.message_handler(commands=['start'])
def help_command(message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, 'Здравствуйте! Это бот тех. поддержки интернет-магазина "Продаем все на свете". Чем могу помочь?', reply_markup=reg_keyboard)

@bot.callback_query_handler(func=lambda call: True)
def call_handler(call):
    match call.data:
        case '1':
            bot.send_chat_action(call.message.chat.id, 'typing')
            bot.send_message(call.message.chat.id, 'Для оформления заказа, пожалуйста, выберите интересующий вас товар и нажмите кнопку "Добавить в корзину", затем перейдите в корзину и следуйте инструкциям для завершения покупки.')
        case '2':
            bot.send_chat_action(call.message.chat.id, 'typing')
            bot.send_message(call.message.chat.id, 'Вы можете узнать статус вашего заказа, войдя в свой аккаунт на нашем сайте и перейдя в раздел "Мои заказы". Там будет указан текущий статус вашего заказа.')
        case '3':
            bot.send_chat_action(call.message.chat.id, 'typing')
            bot.send_message(call.message.chat.id, 'Если вы хотите отменить заказ, пожалуйста, свяжитесь с нашей службой поддержки как можно скорее. Мы постараемся помочь вам с отменой заказа до его отправки.')
        case '4':
            bot.send_chat_action(call.message.chat.id, 'typing')
            bot.send_message(call.message.chat.id, 'При получении поврежденного товара, пожалуйста, сразу свяжитесь с нашей службой поддержки и предоставьте фотографии повреждений. Мы поможем вам с обменом или возвратом товара.')
        case '5':
            bot.send_chat_action(call.message.chat.id, 'typing')
            bot.send_message(call.message.chat.id, 'Вы можете связаться с нашей технической поддержкой через телефон на нашем сайте или написать нам в чат-бота.')
        case '6':
            bot.send_chat_action(call.message.chat.id, 'typing')
            bot.send_message(call.message.chat.id, 'Информацию о доставке вы можете найти на странице оформления заказа на нашем сайте. Там указаны доступные способы доставки и сроки.')
        case '7':
            bot.send_chat_action(call.message.chat.id, 'typing')
            bot.send_message(call.message.chat.id, 'Какая у вас проблема', reply_markup=reg_keyboard2)
        case '7_1':
            bot.send_chat_action(call.message.chat.id, 'typing')
            bot.send_message(call.message.chat.id, 'Хорошо, подробно опишите проблему и как она возникла.', reply_markup=reg_keyboard2)
            bot.register_next_step_handler(call.message, get_text1)
        case '7_2':
            bot.send_chat_action(call.message.chat.id, 'typing')
            bot.send_message(call.message.chat.id, 'Хорошо, подробно опишите проблему и как она возникла.', reply_markup=reg_keyboard2)
            bot.register_next_step_handler(call.message, get_text2)

def get_text1(message):
    bot.send_chat_action(call.message.chat.id, 'typing')
    text1 = message.text
    bot.send_message(message.chat.id,'Хорошо, укажите свой номер телефона или электронную почту.')
    bot.register_next_step_handler(call.message, get_contact1, text1)
def get_contact1(message, text1=text1):
    bot.send_chat_action(call.message.chat.id, 'typing')
    contact1 = message.text
    id1 = manager.get_id1()
    manager.add_request1(id1, text1, contact1)
    bot.send_message(message.chat.id,'Ваш запрос сохранен.')

def get_text2(message):
    bot.send_chat_action(call.message.chat.id, 'typing')
    text2 = message.text
    bot.send_message(message.chat.id,'Хорошо, укажите свой номер телефона или электронную почту.')
    bot.register_next_step_handler(call.message, get_contact2, text2)
def get_contact1(message, text2=text2):
    bot.send_chat_action(call.message.chat.id, 'typing')
    contact2 = message.text
    id2 = manager.get_id2()
    manager.add_request1(id2, text2, contact2)
    bot.send_message(message.chat.id,'Ваш запрос сохранен.')

if __name__ == '__main__':
    bot.infinity_polling()
