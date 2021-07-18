import telebot

bot = telebot.TeleBot('1811176817:AAFIcq6RrR4NlzPyAu9VJo1Rfst2JSdygaI')

@bot.message_handler(commands=['Consultarlatasadecambiodeldolar' ])
def Dolar (mensaje):
    bot.reply_to(mensaje, "El valor del dolar en Honduras es 23.76 ")

@bot.message_handler(commands=['Consultarlatasadecambiodeleuro' ])
def Euro (mensaje):
    bot.reply_to(mensaje, "El valor del euro en Honduras es 26.76")


@bot.message_handler(commands=['ConsultarelPreciodelOro' ])
def Oro (mensaje):
    bot.reply_to(mensaje, "El precio del oro es: Gramo de oro 24K	1,407.97, Gramo de oro 22K	1,290.99, Gramo de oro 21K	1,233.20, Gramo de oro 18 k	1,057.03")


@bot.message_handler(commands=['Concultarelpreciodelcafe' ])
def Cafe (mensaje):
    bot.reply_to(mensaje, "El precio del cafe es de $149.29 (L3,597.88)")




bot.polling()