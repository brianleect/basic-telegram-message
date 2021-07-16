# Import telegram library
import telegram as telegram
from params import token,chat_id, MULTI_TELE_ENABLED, multi_tele
import time
from time import sleep

def durationToSeconds(str_dur):
    unit = str_dur[-1]
    if unit == 's': unit = 1
    elif unit == 'm': unit = 60
    elif unit == 'h': unit = 3600

    return  int(str_dur[:-1]) * unit

def sleepShortestTimeGap():
    time_gap = 10000 # Any large number would do

    for info in multi_tele:
        tmp_time_gap = info['last_triggered'] + durationToSeconds(info['interval']) - time.time()
        print(tmp_time_gap)
        if (tmp_time_gap > 0) and (tmp_time_gap < time_gap): time_gap = tmp_time_gap

    print("Time_Gap:",time_gap)
    if time_gap == 0: return # Prevent negative time

    print("Sleeping for",time_gap,"seconds")
    sleep(time_gap) # Sleeps till the next closest incoming message

def sendMultiMessage(info_dict):
    
    for info in info_dict:
        if time.time() < info['last_triggered'] + durationToSeconds(info['interval']): continue
        
        bot = telegram.Bot(token=info['token'])
        bot.send_message(chat_id=info['chat_id'],text=info['msg'])
        info['last_triggered'] = time.time()

if MULTI_TELE_ENABLED:
    while True:
        sendMultiMessage(multi_tele) # Sends all messages that fits the interval requirements
        sleepShortestTimeGap() # Sleeps till next incoming interval
else:
    bot = telegram.Bot(token=token)
    bot.send_message(chat_id=chat_id,text='Testing 123')