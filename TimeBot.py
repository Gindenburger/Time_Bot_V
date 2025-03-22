# -*- coding:  Windows-1251 -*-
from xmlrpc.client import DateTime
import telebot
from datetime import datetime
from telebot import types # ��� �������� �����

API_TOKEN = '7993358762:AAEbNLpTuUHN7PCrh1mwM1PYAGne8XIjvXo'
SEMESTR_START_MOUTH = 2
SEMESTR_START_DAY = 10
DAY_COUNT = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
WEEK_DAYS = ['�����������', '�������', '�����', '�������', '�������', '�������', '�����������']

bot = telebot.TeleBot(API_TOKEN)
CHAT_ID = 1095553887


@bot.message_handler(commands=['help', 'start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("�������")
    btn2 = types.KeyboardButton("������")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "�����, ����. ����� �������� ����������.", reply_markup=markup)





@bot.message_handler(content_types=['text'])
def send_timetable(message):
    if (message.text == "�������"):
        current_datatime = datetime.today()
        WD = current_datatime.weekday()
        daysAfter = current_datatime.day


        for i in range(SEMESTR_START_MOUTH, current_datatime.month):
            daysAfter += DAY_COUNT[i-1]

        daysAfter -= SEMESTR_START_DAY

        thisWeek = daysAfter // 7 + 1

        if thisWeek % 2 == 0:
            bot.send_message(message.chat.id, f'{current_datatime.day} . {current_datatime.month} . {current_datatime.year}\n������ ������ �{thisWeek}\n{WEEK_DAYS[WD]}')
        
            match WD:
                case 0:
                    bot.send_message(message.chat.id, "16:45 - ���ʠ�Π�ʠȠ������")

                case 1:
                    bot.send_message(message.chat.id, "14:55 --- ������.�������� --- 213* (���)\n\n16:45 --- ��������� --- 327* (���)")

                case 2:
                    bot.send_message(message.chat.id, "10:50 --- �������� --- 328* (���)/n12:40 --- ������.����.�Ƞ�����. --- 310 (���)/n14:55 --- ���ʠ�Π�ʠȠ������")

                case 3:
                    bot.send_message(message.chat.id, "10:50 --- ����.���.Ƞ���.��� --- 450 (���)\n12:40 --- ���������� --- 443 (���)\n14:55 --- ��������� --- 487 (���)")

                case 4:
                    bot.send_message(message.chat.id, "12:40 --- �������.�������� --- 493 (���)\n14:55 --- ����.��. --- 309* (���)")

                case 5:
                    bot.send_message(message.chat.id, "09:00 --- ��������.Ƞ���.���� --- 526* (���)\n10:50 --- �����.����.�Ƞ�����. --- 256* (���)\n12:40 --- ���.���.Ƞ���.��� --- 422* (���)")

                case 6:
                    bot.send_message(message.chat.id, "��� ���! ����������")

        else:
            bot.send_message(message.chat.id, f'{current_datatime.day} . {current_datatime.month} . {current_datatime.year}\n�������� ������ �{thisWeek}\n{WEEK_DAYS[WD]}')
            match WD:
                case 0:
                    bot.send_message(message.chat.id, "16:45 - ���ʠ�Π�ʠȠ������")

                case 1:
                    bot.send_message(message.chat.id, "14:55 --- ������.�������� --- 213* (���)\n16:45 --- ��������� --- 327* (���)")

                case 2:
                    bot.send_message(message.chat.id, "10:50 --- ��������� --- 323* (���)\n12:40 --- ������.����.�Ƞ�����. --- 310 (���)\n14:55 --- ���ʠ�Π�ʠȠ������")

                case 3:
                    bot.send_message(message.chat.id, "09:00 --- ����������� --- 384� (���)\n10:50 --- ����.���.Ƞ���.��� --- 450 (���)\n12:40 --- ���������� --- 443 (���)")

                case 4:
                    bot.send_message(message.chat.id, "10:50 --- ����������� --- 374 (���)\n12:40 --- �������.�������� --- 493 (���)\n14:55 --- ����.��. --- 309* (���)\n16:45 --- �������.Ƞ���.���� --- 218* (���)")

                case 5:
                    bot.send_message(message.chat.id, "09:00 --- ��������.Ƞ���.���� --- 526* (���)\n10:50 --- �����.����.�Ƞ�����. --- 256* (���)\n12:40 --- ���.���.Ƞ���.��� --- 422* (���)")

                case 6:
                    bot.send_message(message.chat.id, "��� ���! ����������")


    elif (message.text == "������"):
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
                bot.send_message(message.chat.id, f'{current_datatime.day + 1} . {current_datatime.month} . {current_datatime.year}\n������ ������ �{thisWeek}\n{WEEK_DAYS[WD]}')
            else:
                bot.send_message(message.chat.id, f'1 . {current_datatime.month + 1} . {current_datatime.year}\n������ ������ �{thisWeek}\n{WEEK_DAYS[WD]}')
        
            match WD:
                case 0:
                    bot.send_message(message.chat.id, "16:45 - ���ʠ�Π�ʠȠ������")

                case 1:
                    bot.send_message(message.chat.id, "14:55 --- ������.�������� --- 213* (���)\n\n16:45 --- ��������� --- 327* (���)")

                case 2:
                    bot.send_message(message.chat.id, "10:50 --- �������� --- 328* (���)/n12:40 --- ������.����.�Ƞ�����. --- 310 (���)/n14:55 --- ���ʠ�Π�ʠȠ������")

                case 3:
                    bot.send_message(message.chat.id, "10:50 --- ����.���.Ƞ���.��� --- 450 (���)\n12:40 --- ���������� --- 443 (���)\n14:55 --- ��������� --- 487 (���)")

                case 4:
                    bot.send_message(message.chat.id, "12:40 --- �������.�������� --- 493 (���)\n14:55 --- ����.��. --- 309* (���)")

                case 5:
                    bot.send_message(message.chat.id, "09:00 --- ��������.Ƞ���.���� --- 526* (���)\n10:50 --- �����.����.�Ƞ�����. --- 256* (���)\n12:40 --- ���.���.Ƞ���.��� --- 422* (���)")

                case 6:
                    bot.send_message(message.chat.id, "��� ���! ����������")

        else:
            if (current_datatime.day + 1) <= DAY_COUNT[current_datatime.month]:
                bot.send_message(message.chat.id, f'{current_datatime.day + 1} . {current_datatime.month} . {current_datatime.year}\n�������� ������ �{thisWeek}\n{WEEK_DAYS[WD]}')
            else:
                bot.send_message(message.chat.id, f'1 . {current_datatime.month + 1} . {current_datatime.year}\n�������� ������ �{thisWeek}\n{WEEK_DAYS[WD]}')
            match WD:
                case 0:
                    bot.send_message(message.chat.id, "16:45 - ���ʠ�Π�ʠȠ������")

                case 1:
                    bot.send_message(message.chat.id, "14:55 --- ������.�������� --- 213* (���)\n16:45 --- ��������� --- 327* (���)")

                case 2:
                    bot.send_message(message.chat.id, "10:50 --- ��������� --- 323* (���)\n12:40 --- ������.����.�Ƞ�����. --- 310 (���)\n14:55 --- ���ʠ�Π�ʠȠ������")

                case 3:
                    bot.send_message(message.chat.id, "09:00 --- ����������� --- 384� (���)\n10:50 --- ����.���.Ƞ���.��� --- 450 (���)\n12:40 --- ���������� --- 443 (���)")

                case 4:
                    bot.send_message(message.chat.id, "10:50 --- ����������� --- 374 (���)\n12:40 --- �������.�������� --- 493 (���)\n14:55 --- ����.��. --- 309* (���)\n16:45 --- �������.Ƞ���.���� --- 218* (���)")

                case 5:
                    bot.send_message(message.chat.id, "09:00 --- ��������.Ƞ���.���� --- 526* (���)\n10:50 --- �����.����.�Ƞ�����. --- 256* (���)\n12:40 --- ���.���.Ƞ���.��� --- 422* (���)")

                case 6:
                    bot.send_message(message.chat.id, "��� ���! ����������")




bot.infinity_polling()