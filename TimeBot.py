# -*- coding:  Windows-1251 -*-
from xmlrpc.client import DateTime
import telebot
from datetime import datetime
from telebot import types # для указание типов

API_TOKEN = '7993358762:AAEbNLpTuUHN7PCrh1mwM1PYAGne8XIjvXo'
SEMESTR_START_MOUTH = 2
SEMESTR_START_DAY = 10
DAY_COUNT = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
WEEK_DAYS = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

bot = telebot.TeleBot(API_TOKEN)
CHAT_ID = 1095553887


@bot.message_handler(commands=['help', 'start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Сегодня")
    btn2 = types.KeyboardButton("Завтра")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Гойда, брат. Давай подскажу расписание.", reply_markup=markup)





@bot.message_handler(content_types=['text'])
def send_timetable(message):
    if (message.text == "Сегодня"):
        current_datatime = datetime.today()
        WD = current_datatime.weekday()
        daysAfter = current_datatime.day


        for i in range(SEMESTR_START_MOUTH, current_datatime.month):
            daysAfter += DAY_COUNT[i-1]

        daysAfter -= SEMESTR_START_DAY

        thisWeek = daysAfter // 7 + 1

        if thisWeek % 2 == 0:
            bot.send_message(message.chat.id, f'{current_datatime.day} . {current_datatime.month} . {current_datatime.year}\nЧЕТНАЯ неделя №{thisWeek}\n{WEEK_DAYS[WD]}')
        
            match WD:
                case 0:
                    bot.send_message(message.chat.id, "16:45 - пр ЭК ПО ФК И СПОРТУ")

                case 1:
                    bot.send_message(message.chat.id, "14:55 --- пр ВЫСШ. МАТЕМАТ --- 213* (УЛК)\n\n16:45 --- лек ФИЗИКА --- 327* (УЛК)")

                case 2:
                    bot.send_message(message.chat.id, "10:50 --- пр ФИЗИКА --- 328* (УЛК)/n12:40 --- лек ИНФ.ТЕХН. И ПРОГР. --- 310 (УЛК)/n14:55 --- пр ЭК ПО ФК И СПОРТУ")

                case 3:
                    bot.send_message(message.chat.id, "10:50 --- лек Д.МАТ.И МАТ.ЛОГ --- 450 (УЛК)\n12:40 --- лек ИСТОРИЯ --- 443 (УЛК)\n14:55 --- пр ИСТОРИЯ --- 487 (УЛК)")

                case 4:
                    bot.send_message(message.chat.id, "12:40 --- лек ВЫСШ. МАТЕМАТ --- 493 (УЛК)\n14:55 --- пр ИН.ЯЗ. --- 309* (УЛК)")

                case 5:
                    bot.send_message(message.chat.id, "09:00 --- лек СТРУК.И ОРГ.ДАНН --- 526* (УЛК)\n10:50 --- пр ИНФ.ТЕХН. И ПРОГР. --- 256* (УЛК)\n12:40 --- пр Д.МАТ.И МАТ.ЛОГ --- 422* (УЛК)")

                case 6:
                    bot.send_message(message.chat.id, "ПАР НЕТ! ГООООООООЛ")

        else:
            bot.send_message(message.chat.id, f'{current_datatime.day} . {current_datatime.month} . {current_datatime.year}\nНЕЧЕТНАЯ неделя №{thisWeek}\n{WEEK_DAYS[WD]}')
            match WD:
                case 0:
                    bot.send_message(message.chat.id, "16:45 - пр ЭК ПО ФК И СПОРТУ")

                case 1:
                    bot.send_message(message.chat.id, "14:55 --- пр ВЫСШ. МАТЕМАТ --- 213* (УЛК)\n16:45 --- лек ФИЗИКА --- 327* (УЛК)")

                case 2:
                    bot.send_message(message.chat.id, "10:50 --- лаб ФИЗИКА --- 323* (УЛК)\n12:40 --- лек ИНФ.ТЕХН. И ПРОГР. --- 310 (УЛК)\n14:55 --- пр ЭК ПО ФК И СПОРТУ")

                case 3:
                    bot.send_message(message.chat.id, "09:00 --- лаб ЭКОЛОГИЯ --- 384а (УЛК)\n10:50 --- лек Д.МАТ.И МАТ.ЛОГ --- 450 (УЛК)\n12:40 --- лек ИСТОРИЯ --- 443 (УЛК)")

                case 4:
                    bot.send_message(message.chat.id, "10:50 --- лек ЭКОЛОГИЯ --- 374 (УЛК)\n12:40 --- лек ВЫСШ. МАТЕМАТ --- 493 (УЛК)\n14:55 --- пр ИН.ЯЗ. --- 309* (УЛК)\n16:45 --- пр СТРУК.И ОРГ.ДАНН --- 218* (УЛК)")

                case 5:
                    bot.send_message(message.chat.id, "09:00 --- лек СТРУК.И ОРГ.ДАНН --- 526* (УЛК)\n10:50 --- пр ИНФ.ТЕХН. И ПРОГР. --- 256* (УЛК)\n12:40 --- пр Д.МАТ.И МАТ.ЛОГ --- 422* (УЛК)")

                case 6:
                    bot.send_message(message.chat.id, "ПАР НЕТ! ГООООООООЛ")


    elif (message.text == "Завтра"):
        current_datatime = datetime.today()
        WD = current_datatime.weekday() + 1
        if WD > 6:
            WD = 0
        daysAfter = current_datatime.day


        for i in range(SEMESTR_START_MOUTH, current_datatime.month):
            daysAfter += DAY_COUNT[i-1]

        daysAfter -= SEMESTR_START_DAY - 1

        thisWeek = daysAfter // 7 + 1

        if thisWeek % 2 == 0:
            if (current_datatime.day + 1) <= DAY_COUNT[current_datatime.month]:
                bot.send_message(message.chat.id, f'{current_datatime.day + 1} . {current_datatime.month} . {current_datatime.year}\nЧЕТНАЯ неделя №{thisWeek}\n{WEEK_DAYS[WD]}')
            else:
                bot.send_message(message.chat.id, f'1 . {current_datatime.month + 1} . {current_datatime.year}\nЧЕТНАЯ неделя №{thisWeek}\n{WEEK_DAYS[WD]}')
        
            match WD:
                case 0:
                    bot.send_message(message.chat.id, "16:45 - пр ЭК ПО ФК И СПОРТУ")

                case 1:
                    bot.send_message(message.chat.id, "14:55 --- пр ВЫСШ. МАТЕМАТ --- 213* (УЛК)\n\n16:45 --- лек ФИЗИКА --- 327* (УЛК)")

                case 2:
                    bot.send_message(message.chat.id, "10:50 --- пр ФИЗИКА --- 328* (УЛК)/n12:40 --- лек ИНФ.ТЕХН. И ПРОГР. --- 310 (УЛК)/n14:55 --- пр ЭК ПО ФК И СПОРТУ")

                case 3:
                    bot.send_message(message.chat.id, "10:50 --- лек Д.МАТ.И МАТ.ЛОГ --- 450 (УЛК)\n12:40 --- лек ИСТОРИЯ --- 443 (УЛК)\n14:55 --- пр ИСТОРИЯ --- 487 (УЛК)")

                case 4:
                    bot.send_message(message.chat.id, "12:40 --- лек ВЫСШ. МАТЕМАТ --- 493 (УЛК)\n14:55 --- пр ИН.ЯЗ. --- 309* (УЛК)")

                case 5:
                    bot.send_message(message.chat.id, "09:00 --- лек СТРУК.И ОРГ.ДАНН --- 526* (УЛК)\n10:50 --- пр ИНФ.ТЕХН. И ПРОГР. --- 256* (УЛК)\n12:40 --- пр Д.МАТ.И МАТ.ЛОГ --- 422* (УЛК)")

                case 6:
                    bot.send_message(message.chat.id, "ПАР НЕТ! ГООООООООЛ")

        else:
            if (current_datatime.day + 1) <= DAY_COUNT[current_datatime.month]:
                bot.send_message(message.chat.id, f'{current_datatime.day + 1} . {current_datatime.month} . {current_datatime.year}\nНЕЧЕТНАЯ неделя №{thisWeek}\n{WEEK_DAYS[WD]}')
            else:
                bot.send_message(message.chat.id, f'1 . {current_datatime.month + 1} . {current_datatime.year}\nНЕЧЕТНАЯ неделя №{thisWeek}\n{WEEK_DAYS[WD]}')
            match WD:
                case 0:
                    bot.send_message(message.chat.id, "16:45 - пр ЭК ПО ФК И СПОРТУ")

                case 1:
                    bot.send_message(message.chat.id, "14:55 --- пр ВЫСШ. МАТЕМАТ --- 213* (УЛК)\n16:45 --- лек ФИЗИКА --- 327* (УЛК)")

                case 2:
                    bot.send_message(message.chat.id, "10:50 --- лаб ФИЗИКА --- 323* (УЛК)\n12:40 --- лек ИНФ.ТЕХН. И ПРОГР. --- 310 (УЛК)\n14:55 --- пр ЭК ПО ФК И СПОРТУ")

                case 3:
                    bot.send_message(message.chat.id, "09:00 --- лаб ЭКОЛОГИЯ --- 384а (УЛК)\n10:50 --- лек Д.МАТ.И МАТ.ЛОГ --- 450 (УЛК)\n12:40 --- лек ИСТОРИЯ --- 443 (УЛК)")

                case 4:
                    bot.send_message(message.chat.id, "10:50 --- лек ЭКОЛОГИЯ --- 374 (УЛК)\n12:40 --- лек ВЫСШ. МАТЕМАТ --- 493 (УЛК)\n14:55 --- пр ИН.ЯЗ. --- 309* (УЛК)\n16:45 --- пр СТРУК.И ОРГ.ДАНН --- 218* (УЛК)")

                case 5:
                    bot.send_message(message.chat.id, "09:00 --- лек СТРУК.И ОРГ.ДАНН --- 526* (УЛК)\n10:50 --- пр ИНФ.ТЕХН. И ПРОГР. --- 256* (УЛК)\n12:40 --- пр Д.МАТ.И МАТ.ЛОГ --- 422* (УЛК)")

                case 6:
                    bot.send_message(message.chat.id, "ПАР НЕТ! ГООООООООЛ")




bot.infinity_polling()