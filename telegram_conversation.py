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
pic=['http://e2412fdcd657.ngrok.io/sticker.png','http://8a1aa16481ce.ngrok.io/meo.png','http://6fab3cf9f76b.ngrok.io/???~~.png','http://6fab3cf9f76b.ngrok.io/???????????????.png','http://6fab3cf9f76b.ngrok.io/????????????.png',
     'http://6fab3cf9f76b.ngrok.io/???????????????.png','http://6fab3cf9f76b.ngrok.io/??????.png','http://6fab3cf9f76b.ngrok.io/???.png','http://6fab3cf9f76b.ngrok.io/????????????.png'] #S56??????


#Q1_list=[]
#with open('Q1.txt',encoding="utf-8") as line:
#		Q1_list = line.read().splitlines()

#print(Q1_list)
'''def callback_30(bot, job):
    bot.send_message(chat_id='1452766072:AAGOSr-679t4yMTtJJtzjJQeMKH9ELDIFFQ', 
                     text='A single message with 30s delay')
j.run_once(callback_30, 30)'''



def start(update: Update, context: CallbackContext) ->  None:
    reply_keyboard = [['Hi~QQ','????????????????????????!']]
    update.message.reply_text(
        'Hi???????????????????????????QQ \n'
        '?????????????????????~ \n'
        '????????????????????????????????? /cancel',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    time.sleep(1)
    update.message.reply_sticker('http://6fab3cf9f76b.ngrok.io/???????????????.png')
    
    return S1


def start2(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("%s: %s", user.first_name, update.message.text)
    time.sleep(1)
    update.message.reply_text(
        '?????????????????????? \n'
    )

    return S2


def start3(update: Update, context: CallbackContext) -> int:
    #user = update.message.from_user
    #logger.info("%s: %s", user.first_name, update.message.text)
    reply_keyboard = [['??????QQ','?????????']]
    time.sleep(0.5)
    update.message.reply_text(
        ' ???????????????????????????????????????{} ! '
        .format(update.message.text),
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    
    return S3

def talk(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("%s: %s", user.first_name, update.message.text)
    update.message.reply_text(
        '{} \n'
        ' ????????????????????????????????? /NO '
        .format(randio("S1"))
    )
    update.message.reply_sticker('http://6fab3cf9f76b.ngrok.io/????????????.png')

    return S4


def que2(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    logger.info("%s: %s", user.first_name, update.message.text)
    if update.message.text=="/NO":
        update.message.reply_text(
        '{}\n'
        '????????????????????????????????? /cancel'
        .format(randio("S5")),
        )
        update.message.reply_sticker(pic[random.randint(0,len(pic)-1)])  #????????????
         
        return S56
    else:
        
        if  PNdis(update.message.text) =="pos":
            update.message.reply_text(
                    '{} \n'
                    ' ???????????????????????????????????? /talk \n '
                     '????????????????????????????????? /cancel'.format(randio("S2")),
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
    if  REBTrej(update.message.text)=="????????????????????????":
        update.message.reply_text(
                '????????????????????? \n'
                )
        update.message.reply_sticker('http://6fab3cf9f76b.ngrok.io/???????????????.png') 
        return S66
    elif REBTrej(update.message.text)=="?????????????????????":
        update.message.reply_text(
                   '{} \n'
                    ' ???????????????????????????????????? /talk \n '
                     '????????????????????????????????? /cancel'.format(randio("S6")) 
                     )
        return S6
    else:
        update.message.reply_text(
                '???????????????????????????????????????????????????:\n'
                '{}\n'
                '?????????????????????~\n'
                ' ???????????????????????????????????? /talk \n '
                '????????????????????????????????? /cancel'
                .format(REBTrej(update.message.text))
                )#, reply_markup=ReplyKeyboardRemove() 
        return S65

   

    #key_list={"??????","??????","?????????","?????????","??????","???"}
    
            
        
        
    



#def que3(update: Update, context: CallbackContext) -> int:
#    reply_keyboard = [['??????',"??????"]]
#    user = update.message.from_user
#    logger.info("%s: %s", user.first_name, update.message.text)
#    if update.message.text =='??????':
#        update.message.reply_text(
#        ' ??????\n'
#        'Send /cancel to stop talking to me.',reply_markup=ReplyKeyboardRemove())
#    else:
#        update.message.reply_text(
#        ' ??????\n'
#        'Send /cancel to stop talking to me.',reply_markup=ReplyKeyboardRemove())
#    
#
#    return S6


def cancel(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        '{} \n'
        '??????????????????????????? /start'
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
            S1: [MessageHandler(Filters.regex('^(Hi~QQ|????????????????????????!|Other)$'), start2)],
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
    