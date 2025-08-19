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

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, 'f', reply_markup=reg_keyboard)

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
            bot.send_message(call.message.chat.id, 'fff')
            bot.register_next_step_handler(call.message, get_text)

def get_text(message):
    bot.send_message(message.chat.id, 'gggfff')

if __name__ == '__main__':
    bot.infinity_polling()