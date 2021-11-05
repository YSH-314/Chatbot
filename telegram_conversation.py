#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=W0613, C0116
# type: ignore[union-attr]
# This program is dedicated to the public domain under the CC0 license.

#pip install jieba 
#pip install BeautifulSoup4   
#pip install html5lib
#pip install python-telegram-bot
#conda install telegram.ext

"""
First, a few callback functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Example of a bot-user conversation using ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
from all_deffunction_5 import *

TOKEN = "1438038757:AAEND*****************"


import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)
import time
import random


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


#Q1_list=randio("S1")
#Q2_list=randio("S2")
#Q4_list=randio("S4")
#Q5_list=randio("S5")
#Q6_list=randio("S6")
#END_list=randio("S8")

S1,S2,S3,S4,S5,S6,S55,S56,S66,S65= range(10)
pic=['http://e2412fdcd657.ngrok.io/sticker.png','http://8a1aa16481ce.ngrok.io/meo.png','http://6fab3cf9f76b.ngrok.io/不~~.png','http://6fab3cf9f76b.ngrok.io/永遠陪伴你.png','http://6fab3cf9f76b.ngrok.io/我在旁邊.png',
     'http://6fab3cf9f76b.ngrok.io/隨時叫我喔.png','http://6fab3cf9f76b.ngrok.io/咕嘰.png','http://6fab3cf9f76b.ngrok.io/啾.png','http://6fab3cf9f76b.ngrok.io/幫你呼呼.png'] #S56圖庫


#Q1_list=[]
#with open('Q1.txt',encoding="utf-8") as line:
#		Q1_list = line.read().splitlines()

#print(Q1_list)
'''def callback_30(bot, job):
    bot.send_message(chat_id='1452766072:AAGOSr-679t4yMTtJJtzjJQeMKH9ELDIFFQ', 
                     text='A single message with 30s delay')
j.run_once(callback_30, 30)'''



def start(update: Update, context: CallbackContext) ->  None:
    reply_keyboard = [['Hi~QQ','我喜歡你的自畫像!']]
    update.message.reply_text(
        'Hi，我是你的情緒助理QQ \n'
        '這是我的自畫像~ \n'
        '如要跟我說掰掰的話請按 /cancel',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    time.sleep(1)
    update.message.reply_sticker('http://6fab3cf9f76b.ngrok.io/我的自畫像.png')
    
    return S1


def start2(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("%s: %s", user.first_name, update.message.text)
    time.sleep(1)
    update.message.reply_text(
        '請問你的名字是? \n'
    )

    return S2


def start3(update: Update, context: CallbackContext) -> int:
    #user = update.message.from_user
    #logger.info("%s: %s", user.first_name, update.message.text)
    reply_keyboard = [['謝謝QQ','我也是']]
    time.sleep(0.5)
    update.message.reply_text(
        ' 真是個好名字，很高興認識你{} ! '
        .format(update.message.text),
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    
    return S3

def talk(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("%s: %s", user.first_name, update.message.text)
    update.message.reply_text(
        '{} \n'
        ' 如果還不想說，請回覆我 /NO '
        .format(randio("S1"))
    )
    update.message.reply_sticker('http://6fab3cf9f76b.ngrok.io/我在聽喔.png')

    return S4


def que2(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    logger.info("%s: %s", user.first_name, update.message.text)
    if update.message.text=="/NO":
        update.message.reply_text(
        '{}\n'
        '如要跟我說掰掰的話請按 /cancel'
        .format(randio("S5")),
        )
        update.message.reply_sticker(pic[random.randint(0,len(pic)-1)])  #隨機找圖
         
        return S56
    else:
        
        if  PNdis(update.message.text) =="pos":
            update.message.reply_text(
                    '{} \n'
                    ' 如果還想多聊聊，請回覆我 /talk \n '
                     '如要跟我說掰掰的話請按 /cancel'.format(randio("S2")),
                     )
            return S55
        else:
            update.message.reply_text(
                    '{} \n'
                    .format(randio("S4")), reply_markup=ReplyKeyboardRemove())
            return S5
    

def que3(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    logger.info("%s: %s", user.first_name, update.message.text)
    if  REBTrej(update.message.text)=="﻿請再多描述一點":
        update.message.reply_text(
                '請再多描述一點 \n'
                )
        update.message.reply_sticker('http://6fab3cf9f76b.ngrok.io/再跟我說說.png') 
        return S66
    elif REBTrej(update.message.text)=="沒有非理性思考":
        update.message.reply_text(
                   '{} \n'
                    ' 如果還想多聊聊，請回覆我 /talk \n '
                     '如要跟我說掰掰的話請按 /cancel'.format(randio("S6")) 
                     )
        return S6
    else:
        update.message.reply_text(
                '我剛剛問了我的造物者，給你一個建議:\n'
                '{}\n'
                '希望對你有幫助~\n'
                ' 如果還想多聊聊，請回覆我 /talk \n '
                '如要跟我說掰掰的話請按 /cancel'
                .format(REBTrej(update.message.text))
                )#, reply_markup=ReplyKeyboardRemove() 
        return S65

   

    #key_list={"絕對","一定","不能不","什麼都","糟透","爛"}
    
            
        
        
    



#def que3(update: Update, context: CallbackContext) -> int:
#    reply_keyboard = [['他人',"事情"]]
#    user = update.message.from_user
#    logger.info("%s: %s", user.first_name, update.message.text)
#    if update.message.text =='他人':
#        update.message.reply_text(
#        ' 他人\n'
#        'Send /cancel to stop talking to me.',reply_markup=ReplyKeyboardRemove())
#    else:
#        update.message.reply_text(
#        ' 事情\n'
#        'Send /cancel to stop talking to me.',reply_markup=ReplyKeyboardRemove())
#    
#
#    return S6


def cancel(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        '{} \n'
        '如果還需要我請輸入 /start'
        .format(randio("S8")), reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def main() -> None:
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        allow_reentry=True,
        states={
            S1: [MessageHandler(Filters.regex('^(Hi~QQ|我喜歡你的自畫像!|Other)$'), start2)],
            S2: [MessageHandler(Filters.text, start3)],
            S3: [MessageHandler(Filters.text, talk)],
            S4: [MessageHandler(Filters.text, que2)],
            S55: [CommandHandler('talk', talk)],#CommandHandler('cancel', cancel)
            S5: [MessageHandler(Filters.text, que3)],
            S66: [MessageHandler(Filters.text, que3)],
            S65: [CommandHandler('talk', talk)],
            S6: [CommandHandler('talk', talk)]
            
            },
                
        fallbacks=[CommandHandler('cancel', cancel)]
        
    )
   
   

    dispatcher.add_handler(conv_handler)
    # Start the Bot
    updater.start_polling()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
    