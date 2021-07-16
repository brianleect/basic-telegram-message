import time

# Param for testing simple single tele message
token = ''  # Insert token obtained from @BotFather here
chat_id = 0 # Insert chatId obtained from @userinfo here

# ---------------------------------------------------
# Parameters for MULTI_TELE, ignore if just testing simple sending of message

MULTI_TELE_ENABLED = True # Change to false if testing simple test message

start = time.time()

multi_tele = [
    {'token':'', 'chat_id':0, 'msg':'','interval':'','last_triggered':start},
    {'token':'', 'chat_id':0, 'msg':'','interval':'','last_triggered':start},
    {'token':'', 'chat_id':0, 'msg':'','interval':'','last_triggered':start},
    {'token':'', 'chat_id':0, 'msg':'','interval':'','last_triggered':start},
]

# Note format for intervals is '15s', '15m' , '4h' etc