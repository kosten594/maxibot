from maxibot import MaxiBot
from maxibot import types

bot = MaxiBot("f9LHodD0cOIY1lqCmnpKkDTUMuzVMkhc4qmlAwIx-47A6DKSyycnFb5I1YVzp9fg9BrBTpoyUpqH_Kaa6cwI")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    kbd = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButtonRequestContact("Привет")
    kbd.add(btn)
    bot.send_message(message.chat.id, "Привет! Как дела?", reply_markup=kbd)


@bot.message_handler(content_types=["contact"])
def send_contact(message: types.Message):
    vcf_info = message.update.get('message', {}).get('body', {}).get('attachments', [{}])[0].get('payload', {}).get('vcf_info')
    # bot.send_message(message.chat.id, f"Msg data {vcf_info}")
    print(vcf_info)


bot.polling()
