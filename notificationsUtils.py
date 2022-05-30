import telegram_send

def sendNotification(message):
    telegram_send.send(messages=[message])
