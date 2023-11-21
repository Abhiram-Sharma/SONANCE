import telepot

def telemsg(msg):
    bot_token = '6892250552:AAGbQEJhnki4i73qpE7mvbq30zMiQVIt6BU'   
    chat_id = -4053309474
    bot = telepot.Bot(bot_token)
    bot.sendMessage(chat_id, msg)
    return "Message Sent"
