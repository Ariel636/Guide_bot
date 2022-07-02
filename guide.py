from typing import ChainMap
import telebot
import telegram
import time
from time import gmtime, strftime
from telegram import ParseMode
from telebot import types
bot = telebot.TeleBot('1951670952:AAFpTcRJeDVOKfUEUMJHjDEwoSuFSYSe1SQ')
@bot.message_handler(content_types=['text', 'photo'])
def uno(message):
    if message.from_user.id!=1265610505:
        try:
            if message.text.lower()=='/initium' or message.text.lower()== '/start':
                bot.send_message(1707358502, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = {message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
                posle=types.InlineKeyboardMarkup()
                engl=types.InlineKeyboardButton(text='English', callback_data='eng')
                russ=types.InlineKeyboardButton(text='Русский', callback_data='ru')
                posle.add(engl, russ)
                bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAECz_VhKM0NC1fqEbaSYWY2vgpzZAv2IQACVg8AAkdioUisE7h1HoBHsyAE")
                bot.send_message(message.chat.id, text='Привет 'f"<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\n"
                'Выберите язык:\n'
            'Choose language:\n',
                reply_markup=posle, parse_mode='html')
            elif message.text.lower()=='расписание' or message.text.lower()=='/raspi':
                keyboard=types.InlineKeyboardMarkup()
                key_Student = types.InlineKeyboardButton(text='Ученик', callback_data='uchenik')
                keyboard.add(key_Student)
                key_Miss = types.InlineKeyboardButton(text='Учитель', callback_data='uchitel')
                keyboard.add(key_Miss)
                bot.send_message(message.chat.id, 'Кем вы нам приходитесь?', reply_markup=keyboard)
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
            elif message.text.lower()=='смена языка':
                rusya=types.ReplyKeyboardMarkup(resize_keyboard=True)
                rasp=types.KeyboardButton('Расписание')
                socialka=types.KeyboardButton('Социальная жизнь')
                cabinet=types.KeyboardButton('Кабинеты')
                spruvka=types.KeyboardButton('Справки об учителях')
                spravka=types.KeyboardButton('Справки по предметам')
                nacalka=types.KeyboardButton('Связь с разработчиком')
                rulang=types.KeyboardButton('Go to English')
                rusya.add(rasp, socialka, cabinet, spruvka, spravka, nacalka, rulang)
                bot.send_message(message.chat.id, 'Выберите раздел:', reply_markup=rusya)
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')

            elif message.text.lower()=='go to english':
                angl=types.ReplyKeyboardMarkup(resize_keyboard=True)
                sched=types.KeyboardButton('Schedule')
                sociali=types.KeyboardButton('Social life')
                cabinka=types.KeyboardButton('Location of cabinets')
                help1=types.KeyboardButton('Inquiries about teachers')
                help2=types.KeyboardButton('Inquiries about subjects')
                buck=types.KeyboardButton('Connect with creator')
                relang=types.KeyboardButton('Смена языка')
                angl.add(sched, sociali, cabinka, help1, help2, buck, relang)
                bot.send_message(message.chat.id, 'Choose chapter:', reply_markup=angl)
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
            elif message.text.lower()=='connect with creator':
                sures=types.InlineKeyboardMarkup()
                sures1=types.InlineKeyboardButton(text='Yes', callback_data='yes')
                sures.add(sures1)
                sures2=types.InlineKeyboardButton(text='No', callback_data='noo')
                sures.add(sures2)
                bot.reply_to(message, text='Are you sure that you want connect with my developer? If you press Yes I will send him your username, User ID, firstname and phone number.', reply_markup=sures)
                bot.send_message(908927889, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = {message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = выборка нажать или нет/engl', parse_mode='html')
            elif message.text.lower()=='связь с разработчиком':
                suras=types.InlineKeyboardMarkup()
                suras1=types.InlineKeyboardButton(text='Абсолютно да', callback_data='suras1')
                suras.add(suras1)
                suras2=types.InlineKeyboardButton(text='Нет наверное', callback_data='suras2')
                suras.add(suras2)
                bot.reply_to(message, text='Вы уверены что хотите связаться с разработчиком? Как только нажмете на "Абсолютно да", я отправлю разработчику ваш номер телефона, username и user ID\nВ случае если вы нажмете на Абсолютно да будучи прикалываясь или просто нажимая на все кнопки, то разработчик будет вынужден ограничить ваше пользование.', reply_markup=suras)
                bot.send_message(908927889, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = {message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = неуверен в выборке', parse_mode='html')
            elif message.text.lower()=='inquiries about teachers' or message.text.lower()=='справки об учителях':
                choise=types.InlineKeyboardMarkup()
                tucher=types.InlineKeyboardButton(text='Teacher - Учитель', callback_data='tucher')
                choise.add(tucher)
                animi=types.InlineKeyboardButton(text='Administration - Администрация', callback_data='animi')
                choise.add(animi)
                bot.send_message(message.chat.id, text='Another choice...', reply_markup=choise)
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
            elif message.text.lower()=='social life':
                kwoka=types.InlineKeyboardMarkup()
                SUn = types.InlineKeyboardButton(text='SU(Students Union)', callback_data='SUn')
                kwoka.add(SUn)
                Volu = types.InlineKeyboardButton(text='IHT Volunteers', callback_data='volun')
                kwoka.add(Volu)
                FM = types.InlineKeyboardButton(text='IHT FM', callback_data='fm')
                kwoka.add(FM)
                Sleo = types.InlineKeyboardButton(text='SLEO(Social Lyceum Events Organization)', callback_data='sleo')
                kwoka.add(Sleo)
                club=types.InlineKeyboardButton(text='Clubs', callback_data='club')
                kwoka.add(club)
                acosha=types.InlineKeyboardButton(text='Social networks', callback_data='acosha')
                kwoka.add(acosha)
                bot.send_message(message.chat.id, 'Choose direction- ', reply_markup=kwoka)   
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')     
            elif message.text.lower()=='социальная жизнь':
                kwuka=types.InlineKeyboardMarkup()
                SUN = types.InlineKeyboardButton(text='SU(Студенческий союз)', callback_data='surus')
                kwuka.add(SUN)
                Volon = types.InlineKeyboardButton(text='Волонтерство', callback_data='volon')
                kwuka.add(Volon)
                radio = types.InlineKeyboardButton(text='IHT Радио', callback_data='radio')
                kwuka.add(radio)
                sleorus = types.InlineKeyboardButton(text='SLEO(Организаторы мероприятий)', callback_data='sleorus')
                kwuka.add(sleorus)
                klub=types.InlineKeyboardButton(text='Клубы', callback_data='klub')
                kwuka.add(klub)
                account=types.InlineKeyboardButton(text='Социальные сети', callback_data='account')
                kwuka.add(account)
                bot.send_message(message.chat.id, 'Выбираем направление- ', reply_markup=kwuka)  
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
            elif message.text.lower()=='location of cabinets':
                cobeen=types.InlineKeyboardMarkup()
                cotg=types.InlineKeyboardButton(text='Cabinet of the group', callback_data='gcabin')  
                cobeen.add(cotg)  
                others=types.InlineKeyboardButton(text='Others', callback_data='others') 
                cobeen.add(others)
                bot.send_message(message.chat.id, 'Which exactly cabinet?', reply_markup=cobeen)
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
            elif message.text.lower()=='кабинеты':
                kabinet=types.InlineKeyboardMarkup()
                grupkabinet=types.InlineKeyboardButton(text='Кабинеты группы', callback_data='grupkabinet')
                kabinet.add(grupkabinet)
                drugkabinet=types.InlineKeyboardButton(text='Другие кабинеты', callback_data='drugkabinet')
                kabinet.add(drugkabinet)
                bot.send_message(message.chat.id, 'Какой именно кабинет?', reply_markup=kabinet)
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
            elif 'малика' in message.text.lower():
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
                bot.send_media_group(chat_id=message.chat.id, media=[types.InputMediaPhoto('http://iht.uz/wp-content/uploads/2020/06/ahmedova-m.a.-400x600.jpg', caption='''Ахмедова Малика Абдумаликовна:\n1)Дата рождения - 20 октября \n2)Преподает- История Узбекистана\n3)Является куратором 2тн2\n4)Характер преподования - требовательная, компетентная\n'''),
                types.InputMediaPhoto('https://ibb.co/wg8qr0c') ] )
            elif 'сиявуш' in message.text.lower() or 'сиевуш' in message.text.lower():
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
                bot.send_photo(chat_id=message.chat.id, photo='https://ibb.co/zspM2mX', caption='Каххаров Сиявуш Худоёрович:\n1)Дата рождения - 04.09.1994\n2)Преподает - Начальная допризывная подготовка\n3)Является смотрящим во время проведения ИК\n4)Харатер преподавания - требовательный, принципиальный\n5)Звание - старший лейтенант')
            elif 'мамура' in message.text.lower() or 'маъмура' in message.text.lower():
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
                bot.send_photo(chat_id=message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/tadzhibaeva-m-400x600.jpg', caption='Таджибаева Маъмура Халимджановна:\n1)Дата рождения - засекречено\n2)Преподает - информатика\n3)Характер преподавания - засекречено')
            elif 'айгуль' in message.text.lower():
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
                bot.send_photo(chat_id=message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/zaf-kafedroj-sahinaeva-a.k.-400x600.jpg', caption='Сахинаева Айгуль Калабаевна:\n1)Дата рождения - 29 апреля \n2)Преподает - Всемирная история, История России\n3)Характер преподавания - принципиальная, интересная, энергичная\n4)ПК проводит в виде эссе(ответы на вопросы)\n5)Является заведующей кафедры')
            elif 'ильхом' in message.text.lower() or 'илхом' in message.text.lower():
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
                bot.send_photo(chat_id=message.chat.id, photo='https://ibb.co/yY00Skb', caption= 'Хусанов Ильхом Бахромович:\n1)Дата рождения - 10 декабря \n2)Преподает - обществознание в МГИМО группах\nПреподавал - Основы духовности, История религий мира, Основы государства и права\n3)Характер преподавания - экцентричный, принципиальный, хладнокровный\n4)Является смотрящим во время ИК')
            elif 'мирзаев' in message.text.lower() or 'киличбек' in message.text.lower():
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
                bot.send_photo(chat_id=message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/mirzaev-k.u-prepodavatel-osnov-gosudarstva-i-prava-400x600.jpg', caption='Мирзаев Киличбек Улугбек угли:\n1)Дата рождения -  \n2)Преподает - Основы государаства и права\n3)Характер преподавания - ординарный')
            elif 'собиржон' in message.text.lower() or 'собир' in message.text.lower():
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
                bot.send_photo(chat_id=message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/kodirov-sobir-400x600.jpg', caption='Кодиров Собиржон Мамадиёрович:\n1)Дата рождения -  \n2)Преподает - география\n3)Характер преподавания - своеобразный, углубленный, интересный\n4)Работает в Ташкентском ирригационном институте\n')
            elif 'махбуба' in message.text.lower():
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
                bot.send_photo(chat_id=message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/ermatova-m.m-400x600.jpg', caption='Эрматова Махбуба Маматюлдашевна:\n1)Дата рождения - 18 июля \n2)Преподает - алгебра, геометрия\n3)Характер преподавания -  \n4)Является заведующей кафедры точных наук')
            elif 'мунира' in message.text.lower():
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
                bot.send_photo(chat_id=message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/agzamhodzhaeva-m.sh.-400x600.jpg', caption='Агзамходжаева Мунира Шорахматовна:\n1)Дата рождения - засекречено \n2)Преподает - алгебра, геометрия\n3)Характер преподавания -  \n4)Награждена орденом "Мехнат Шухрати".')
            elif 'зульфия' in message.text.lower():
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
                bot.send_photo(chat_id=message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/hasanova-z.s-400x600.jpg', caption='Хасанова Зульфия Салаховна:\n1)Дата рождения - 15 ноября\n2)Преподает - биология\n3)Характер преподавания - квалифицированный, интересный, строгий\n4)Лучше не опаздывать на ее уроки\n5)Высоко оценивает старание учеников и подготовку презентаций')
            elif 'гавхар' in message.text.lower():
                fufufu=types.InlineKeyboardMarkup()
                gusha1=types.InlineKeyboardButton(text='Каримова Гавхар Шавкатжановна', callback_data='gusha1')
                fufufu.add(gusha1)
                gusha2=types.InlineKeyboardButton(text='Каландарова Гавхар Иргашевна', callback_data='gusha2')
                fufufu.add(gusha2)
                bot.send_message(message.chat.id, 'Которая?', reply_markup=fufufu)
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
            elif 'сафин' in message.text.lower() or 'павел' in message.text.lower():
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
                bot.send_photo(chat_id=message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/safin-1-400x600.jpg', caption='Сафин Павел Радикович:\n1)Дата рождения - засекречено \n2)Преподает - алгебра, геометрия\n3)Характер преподавания - высококвалифицированный, интересный')
            elif'мохира' in message.text.lower():
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
                bot.send_media_group(chat_id=message.chat.id, media=[types.InputMediaPhoto('https://ibb.co/wQdjBZr',caption='Курбанова Мохира Абдувахабовна:\n1)Дата рождения - засекречено \n2)Преподает - химия\n3)Характер преподавания - ординарный\n3)Работала в Ташкентском Химико-Технологическом Институте'),
                types.InputMediaPhoto('http://iht.uz/wp-content/uploads/2020/11/333-400x541.png')])
            elif 'борис' in message.text.lower():
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
                bot.send_photo(chat_id=message.chat.id, photo='https://lh3.googleusercontent.com/proxy/VBGFnzFR_56ZN5RYo6bscoU_wRAaCY-KV2TKNfxgLZD10O8JULJPDQWWL8y4RYISkyFVc7xDjfWnEbK2cLkhjKvgylZIypyXYplJHlQApQgFntowlEkFfGs', caption='Дмитриев Борис Григорьевич:\n1)Дата рождения - засекречено\n2)Преподает - физика\n3)Характер преподавания - понятливый, добрый, квалифицированный')
            elif 'айбек' in message.text.lower():
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
                bot.send_photo(chat_id=message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/dzhabirov-a.u-400x600.jpg', caption='Джабиров Айбек Уктамович:\n1)Дата рождения - засекречено\n2)Преподает - алгебра, геометрия\n3)Характер преподавания - интересный, квалифицированный')
            elif 'нодира' in message.text.lower() or 'мавлянова' in message.text.lower():
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
                bot.send_photo(chat_id=message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/mavlyanova-n.m-400x600.jpg', caption='Мавлянова Нодира Зиёвуддиновна:\n1)Дата рождения - засекречено\n2)Преподает - информатика\n3)Характер преподавания - ординарный, принципиальный\n4)Программирует на С++')
            elif 'мухаммаджон' in message.text.lower() or 'узоков' in message.text.lower():
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
                bot.send_photo(chat_id=message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/11/222-400x539.png', caption='Узоков Мухаммаджон Абдулла угли:\n1)Дата рождения - засекречено\n2)Преподает - физика\n3)Характер преподавания - ординарный')
            elif 'хошимжон' in message.text.lower():
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
                bot.send_photo(chat_id=message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/mamazhonov-h..-a-400x600.jpg', caption='Мамажонов Хошимжон Абдумаликович:\n1)Дата рождения - засекречено\n2)Преподает - физика\n3)Характер преподавания - засекречено')
            elif 'шохида' in message.text.lower():
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
                bot.send_photo(chat_id=message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/boltaeva-sh.k-400x600.jpg', caption='Болтаева Шохида Комиловна:\n1)Дата рождения - засекречено\n2)Преподает - алгебра, геометрия\n3)Характер преподавания - засекречено')
            elif 'туйчи' in message.text.lower():
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
                bot.send_photo(chat_id=message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/bobozhanov-t.e-400x600.jpg', caption='Бобожанов Туйчи Эргашевич:\n1)Дата рождения - засекречено\n2)Преподает - алгебра, геометрия\n3)Характер преподавания - засекречено')
            elif message.text.lower()=='inquiries about subjects':
                subj=types.InlineKeyboardMarkup()
                pk=types.InlineKeyboardButton(text='Interim control', callback_data='pk')
                subj.add(pk)
                ik=types.InlineKeyboardButton(text='Final control', callback_data='ik')
                subj.add(ik)
                interim=types.InlineKeyboardButton(text='Interim subjects', callback_data='interim')
                subj.add(interim)
                electronic=types.InlineKeyboardButton(text='Electronic versions of books', callback_data='electronic')
                subj.add(electronic)
                bot.send_message(message.chat.id, 'Choose an option', reply_markup=subj)
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
            elif message.text.lower()=='справки по предметам':
                urok=types.InlineKeyboardMarkup()
                rk=types.InlineKeyboardButton(text='Промежуточный контроль(ПК)', callback_data='rk')
                urok.add(rk)
                ek=types.InlineKeyboardButton(text='Итоговый Контроль(ИК)', callback_data='ek')
                urok.add(ek)
                vremenniy=types.InlineKeyboardButton(text='Временные предметы', callback_data='vremenniy')
                urok.add(vremenniy)
                ilictru=types.InlineKeyboardButton(text='Электронные версии книг', callback_data='ilictru')
                urok.add(ilictru)
                bot.send_message(message.chat.id, 'Выбирайте опцию', reply_markup=urok)
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
            elif 'нигора' in message.text.lower():
                tuoes=types.InlineKeyboardMarkup()
                nigga1=types.InlineKeyboardButton(text='Шамсиева Нигора Зоировна', callback_data='nigga1')
                tuoes.add(nigga1)
                nigga2=types.InlineKeyboardButton(text='Камалиддинова Нигора Сиражиддиновна', callback_data='nigga2')
                tuoes.add(nigga2)
                bot.send_message(message.chat.id, text='Которая?', reply_markup=tuoes)
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
            elif 'марина' in message.text.lower():
                bot.send_photo(chat_id=message.chat.id, photo='https://ibb.co/8zNVQtR',caption='Лебедева Марина Олеговна:\n1)Дата рождения - 3 марта\n2)Преподает - английский язык\n3)Характер преподавания - квалифицированный, строгий\n4)Является заведующей кафедры английской филологии') 
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
            elif 'зухра' in message.text.lower():
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
                bot.send_message(chat_id=message.chat.id, text='Фото удалено по просьбе правообладателя\nХакимова Зухра Икболжон кизи:\n1)Дата рождения - 12 февраля\n2)Преподает - английский язык\n3)Характер преподавания - ординарный')
            elif 'хушнуда' in message.text.lower():
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
                bot.send_photo(chat_id=message.chat.id, photo='http://iht.uz/wp-content/uploads/2019/06/rahmatova-h-1-400x600.jpg', caption='Рахматова Хушнуда Нуриддиновна:\n1)Дата рождения - 26 ноября\n2)Преподает - английский язык\n3)Характер преподавания - интересный')
            elif 'ольга' in message.text.lower():
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
                bot.send_message(chat_id=message.chat.id, text='Фото удалено по просьбе правообладателя\nПрокофьева Ольга Сергеевна:\n1)Дата рождения - 20 июля\n2)Преподает - английский язык\n3)Характер преподавания - квалифицированный, интересный')
            elif 'дильноза' in message.text.lower() or 'дилноза' in message.text.lower() or 'диля' in message.text.lower():
                dilyau=types.InlineKeyboardMarkup()
                dila1=types.InlineKeyboardButton(text='Матякубова Дилноза Владимир кизи', callback_data='dila1')
                dilyau.add(dila1)
                dila2=types.InlineKeyboardButton(text='Содикова Дилноза Закировна', callback_data='dila2')
                dilyau.add(dila2)
                bot.send_message(message.chat.id, text='Которая?', reply_markup=dilyau)
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
            elif 'озода' in message.text.lower():
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
                bot.send_message(chat_id=message.chat.id, text='Фото удалено по просьбе правообладателя\nСадикова Озода Закировна:\n1)Дата рождения - 9 января\n2)Преподает - английский язык\n3)Характер преподавания - ординарный')
            elif 'умида' in message.text.lower():
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
                bot.send_photo(chat_id=message.chat.id, photo='http://iht.uz/wp-content/uploads/2019/06/tolibaeva-u-400x600.jpg', caption='Толибаева Умида Акмальбек кизи:\n1)Дата рождения - засекречено\n2)Преподает - английский язык\n3)Характер преподавания - засекречено')
                                          
            elif 'раиса' in message.text.lower():
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
                bot.send_photo(chat_id=message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/kurban-r.k-400x600.jpg', caption='Курбан Раиса Камиловна:\n1)Дата рождения - 9 февраля\n2)Преподает - русский язык в узбекских группах\n3)Характер преподавания - строгий, квалифицированный\n4)Является заведующей кафедры узбекской и русской филологии')
            elif 'мукаддам' in message.text.lower():
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
                bot.send_photo(chat_id=message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/abdukodirova-m.m-400x600.jpg', caption='Абдукодирова Мукаддам Муйдиновна\n1)Дата рождения - засекречено\n2)Преподает - узбекский язык в группах АФ\n3)Характер преподавания - ординарный')
            elif 'гулхае' in message.text.lower() or 'гулхаё' in message.text.lower():
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
                bot.send_photo(chat_id=message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/ruzikulova-g.f-400x600.jpg', caption='Рузикулова Гулхаё Фархадовна:\n1)Дата рождения - 29 августа\n2)Преподает - узбекский язык в узбекских группах\n3)Характер преподавания - увлекательный')
            elif 'шахина' in message.text.lower():
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
                bot.send_photo(chat_id=message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/muhamedzhanova-sh.sh-400x600.jpg', caption='Мухамеджанова Шахина Шухратовна:\n1)Дата рождения - 3 июня\n2)Преподает - русский язык, литература\n3)Характер преподавания - ординарный, непредсказуемый')
            elif 'алексей' in message.text.lower():
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
                bot.send_photo(chat_id=message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/rostovczev-a.v-400x600.jpg', caption='Ростовцев Алексей Викторович:\n1)Дата рождения - засекречено\n2)Преподает - русский язык, литература\n3)Характер преподавания - увлекательный, принципиальный')
            elif 'ирода' in message.text.lower():
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
                bot.send_photo(chat_id=message.chat.id, photo='https://i.pinimg.com/736x/42/3b/18/423b18621dc0071b816e91a6af154824.jpg', caption='Мамаражабова Ирода Файзуллаевна:\n1)Дата рождения - 25 мая\n2)Преподает - узбекский язык в русских группах\n3)Характер преподавания - ординарный, принципиальный')
            elif 'эльмира' in message.text.lower():
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
                bot.send_photo(chat_id=message.chat.id, photo='https://i.mycdn.me/i?r=AyH4iRPQ2q0otWIFepML2LxRJdnuOdyPQ6MJ1mjqEHDEYg',caption='Отрезова(Яфарова) Эльмира Нуралиевна:\n1)Дата рождения - 6 июля\n2)Преподает - русский язык, литература\n3)Характер преподавания - увлекательный, принципиальный')
            elif message.text.lower()=='schedule' or message.text.lower()=='/schedule':
                keyboard=types.InlineKeyboardMarkup()
                key_Student = types.InlineKeyboardButton(text='Student', callback_data='student')
                keyboard.add(key_Student)
                key_Miss = types.InlineKeyboardButton(text='Teacher', callback_data='teacher')
                keyboard.add(key_Miss)
                bot.send_message(message.chat.id, 'Who are you?', reply_markup=keyboard)
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
            else:
                bot.send_message(1412330377, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = @{message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = ' + f"<a href='tg://user?id={message.from_user.id}'>{message.text}</a>", parse_mode='html')
        except:
            bot.send_message(908927889, text='Че то пошло не по плану')
    else:
        return
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    buton=types.InlineKeyboardButton
    markus=types.InlineKeyboardMarkup()
    if call.message.chat.id==88126752:
        return
    elif call.data == 'eng':
        angl=types.ReplyKeyboardMarkup(resize_keyboard=True)
        sched=types.KeyboardButton('schedule')
        sociali=types.KeyboardButton('Social life')
        cabinka=types.KeyboardButton('Location of cabinets')
        help1=types.KeyboardButton('Inquiries about teachers')
        help2=types.KeyboardButton('Inquiries about subjects')
        buck=types.KeyboardButton('Connect with creator')
        relang=types.KeyboardButton('Смена языка')
        angl.add(sched, sociali, cabinka, help1, help2, buck, relang)
        bot.send_message(call.message.chat.id, 'Choose chapter:', reply_markup=angl)
    elif call.data =='ru':
        rusya=types.ReplyKeyboardMarkup(resize_keyboard=True)
        rasp=types.KeyboardButton('Расписание')
        socialka=types.KeyboardButton('Социальная жизнь')
        cabinet=types.KeyboardButton('Кабинеты')
        spruvka=types.KeyboardButton('Справки об учителях')
        spravka=types.KeyboardButton('Справки по предметам')
        nacalka=types.KeyboardButton('Связь с разработчиком')
        rulang=types.KeyboardButton('Go to English')
        rusya.add(rasp, socialka, cabinet, spruvka, spravka, nacalka, rulang)
        bot.send_message(call.message.chat.id, 'Выберите раздел:', reply_markup=rusya)
    elif call.data=='yes':
        bot.send_message(call.message.chat.id, text="<a href='https://t.me/Secretary_Ariil_bot'>Creator</a>",
                parse_mode=ParseMode.HTML)
        bot.send_message(908927889, f'ID: <code>{call.message.chat.id}</code>\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nХотят связаться', parse_mode='html')
    elif call.data=='noo':
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    elif call.data=='suras1':
        bot.send_message(call.message.chat.id, text="<a href='https://t.me/Secretary_Ariil_bot'>Разработчик</a>",
                parse_mode=ParseMode.HTML)
        bot.send_message(908927889, f'ID: <code>{call.message.chat.id}</code>\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nХотят связаться', parse_mode='html')
    elif call.data=='suras2':
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    elif call.data == 'student' or call.data=='prev2':
            fruct = types.InlineKeyboardMarkup()
            key_1course = types.InlineKeyboardButton(text='1 cousre', callback_data='1co')
            fruct.add(key_1course)
            key_2course = types.InlineKeyboardButton(text='2 course', callback_data='2co')
            fruct.add(key_2course)
            sbas=buton('Back', callback_data='basicsh')
            fruct.add(sbas)
            bot.edit_message_text(chat_id=call.message.chat.id, text='Choose your course:',message_id=call.message.message_id, reply_markup=fruct)
   
    else:
        if call.data=='1co' or call.data=='leng':
            keyboard = types.InlineKeyboardMarkup()
            key_1MGIMO1 = types.InlineKeyboardButton(text='1MGIMO1', callback_data='11')
            keyboard.add(key_1MGIMO1)
            key_1MGIMO2 = types.InlineKeyboardButton(text='1MGIMO2', callback_data='12')
            keyboard.add(key_1MGIMO2)
            key_1ES1 = types.InlineKeyboardButton(text='1ES1', callback_data='01')
            keyboard.add(key_1ES1)
            key_1ES2 = types.InlineKeyboardButton(text='1ES2', callback_data='02')
            keyboard.add(key_1ES2)
            key_1ES3 = types.InlineKeyboardButton(text='1ES3', callback_data='03')
            keyboard.add(key_1ES3)
            key_1ES4 = types.InlineKeyboardButton(text='1ES4', callback_data='04')
            keyboard.add(key_1ES4)
            SS1=types.InlineKeyboardButton(text='1SS1', callback_data='1ss1')
            keyboard.add(SS1)

            AF1=types.InlineKeyboardButton(text='1AF1', callback_data='1af1')
            keyboard.add(AF1)

            AF2=types.InlineKeyboardButton(text='1AF2', callback_data='1af2')
            keyboard.add(AF2)

            AF3=types.InlineKeyboardButton(text='1AF3', callback_data='1af3')
            keyboard.add(AF3)

            prev2=buton('Back', callback_data='prev2')
            keyboard.add(prev2)
            bot.edit_message_text(chat_id=call.message.chat.id, text='Choose your group:',message_id=call.message.message_id, reply_markup=keyboard)
        elif call.data == 'uchenik' or call.data=='back1':
            fractal = types.InlineKeyboardMarkup()
            key_1curs = types.InlineKeyboardButton(text='1 курс', callback_data='little')
            fractal.add(key_1curs)
            key_curs = types.InlineKeyboardButton(text='2 курс', callback_data='huge')
            fractal.add(key_curs)
            nazad=buton(text='Назад', callback_data='nazad')
            fractal.add(nazad)
            bot.edit_message_text(chat_id=call.message.chat.id, text='Выберите группу:',message_id=call.message.message_id, reply_markup=fractal)
        elif call.data=='nazad':
            keyboard=types.InlineKeyboardMarkup()
            key_Student = types.InlineKeyboardButton(text='Ученик', callback_data='uchenik')
            keyboard.add(key_Student)
            key_Miss = types.InlineKeyboardButton(text='Учитель', callback_data='uchitel')
            keyboard.add(key_Miss)
            bot.edit_message_text(chat_id=call.message.chat.id, text='Кем вы нам приходитесь?',message_id=call.message.message_id, reply_markup=keyboard)

        elif call.data=='little' or call.data=='lrus':
            keyboard = types.InlineKeyboardMarkup()
            key_1MGIMO1 = types.InlineKeyboardButton(text='1МТН1', callback_data='101')
            keyboard.add(key_1MGIMO1)
            key_1MGIMO2 = types.InlineKeyboardButton(text='1МТН2', callback_data='102')
            keyboard.add(key_1MGIMO2)
            key_1ES1 = types.InlineKeyboardButton(text='1ТН1', callback_data='011')
            keyboard.add(key_1ES1)
            key_1ES2 = types.InlineKeyboardButton(text='1ТН2', callback_data='022')
            keyboard.add(key_1ES2)
            key_1ES3 = types.InlineKeyboardButton(text='1ТН3', callback_data='033')
            keyboard.add(key_1ES3)
            key_1ES4 = types.InlineKeyboardButton(text='1ТН4', callback_data='044')
            keyboard.add(key_1ES4)
            RS1=types.InlineKeyboardButton(text='1СГ1', callback_data='1ss1')
            keyboard.add(RS1)

            AF1=types.InlineKeyboardButton(text='1AФ1', callback_data='1af1')
            keyboard.add(AF1)

            AF2=types.InlineKeyboardButton(text='1AФ2', callback_data='1af2')
            keyboard.add(AF2)

            AF3=types.InlineKeyboardButton(text='1AФ3', callback_data='1af3')
            keyboard.add(AF3)
            back1=buton('Назад', callback_data='back1')
            keyboard.add(back1)
            bot.edit_message_text(chat_id=call.message.chat.id, text='Выберите группу:',message_id=call.message.message_id, reply_markup=keyboard)
        elif call.data == '11':
            keyboard = types.InlineKeyboardMarkup()
            key_Monday = types.InlineKeyboardButton(text='Monday', callback_data='mn')
            keyboard.add(key_Monday)
            key_Tuesday = types.InlineKeyboardButton(text='Tuesday', callback_data='tu')
            keyboard.add(key_Tuesday)
            key_Wednesday = types.InlineKeyboardButton(text='Wednesday', callback_data='wed')
            keyboard.add(key_Wednesday)
            key_Thursday = types.InlineKeyboardButton(text='Thursday', callback_data='thor')
            keyboard.add(key_Thursday)
            key_Friday = types.InlineKeyboardButton(text='Friday', callback_data='fr')
            keyboard.add(key_Friday)
            key_Saturday = types.InlineKeyboardButton(text='Saturday', callback_data='sat')
            keyboard.add(key_Saturday)
            leng=buton('Back', callback_data='leng')
            keyboard.add(leng)
            bot.edit_message_text(chat_id=call.message.chat.id, text='The day-',message_id=call.message.message_id, reply_markup=keyboard)
            bot.send_message(1412330377, f'ID: <code>{call.message.chat.id}</code>\nUsername = @{call.message.chat.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nРасписание <b>1МТН1</b>', parse_mode='html')
        elif call.data=='mn':
                    bot.send_message(call.message.chat.id, '''1MGIMO1-MONDAY
1)Physics(103)
2)Algebra(103 and 104)
3)English lng:
Group 1 - 209
Group 2 - 26
4)History(103)
5)social science''')
        elif call.data=='tu':
                    bot.send_message(call.message.chat.id, '''1MGIMO1-TUESDAY
1)Russian lng(103)
2)Algebra:
Group 1 - 103
Group 2 - smart room
3)Literature(103)
4)English lng:
Group 1 - 209
Group 2 - 26
5)English lng:
Group 1 - 209
Group 2 - 26
6)PE(gym)''')
        elif call.data=='wed':
                    bot.send_message(call.message.chat.id, '''1MGIMO1-WEDNESDAY
1)English lng:
Group 1 - 209
Group 2 - 26
2)Geography(103)
3)Math(103)
4)Math(103)
5)PE(gym)''')
        if call.data=='thor':
                    bot.send_message(call.message.chat.id, '''1MGIMO1-THURSDAY
1)English lng:
Group 1 - 209
Group 2 - 26
2)Geometry:
Group 1 - 103
Group 2 - 305
3)Upbringing(conf hall)
4)IT:
Group 1 - 103
Group 2 - 21
5)History(103)''')
        if call.data=='fr':
                    bot.send_message(call.message.chat.id, '''1MGIMO1-FRIDAY
1)Geometry:
Group 1 - 103
Group 2 - 305
2)Biology(307)<b>DON'T BE LATE!</b>
3)Chemistry(103)
4)Literature(103)''')
        if call.data=='sat':
                        bot.send_message(call.message.chat.id, '''1MGIMO1-SATURDAY
1)Algebra:
Group 1 - 103
Group 2 - 21
2)Uzbek lng(103)
3)History(103)
4)Russian lng(103)
5)History(103)''')

        else:
            if call.data == '12':
                    keyboard = types.InlineKeyboardMarkup()
                    key_Monday = types.InlineKeyboardButton(text='Monday', callback_data='mn1')
                    keyboard.add(key_Monday)
                    key_Tuesday = types.InlineKeyboardButton(text='Tuesday', callback_data='tu1')
                    keyboard.add(key_Tuesday)
                    key_Wednesday = types.InlineKeyboardButton(text='Wednesday', callback_data='wed1')
                    keyboard.add(key_Wednesday)
                    key_Thursday = types.InlineKeyboardButton(text='Thursday', callback_data='thor1')
                    keyboard.add(key_Thursday)
                    key_Friday = types.InlineKeyboardButton(text='Friday', callback_data='fr1')
                    keyboard.add(key_Friday)
                    key_Saturday = types.InlineKeyboardButton(text='Saturday', callback_data='sat1')
                    keyboard.add(key_Saturday)
                    leng=buton('Back', callback_data='leng')
                    keyboard.add(leng)
                    bot.edit_message_text(chat_id=call.message.chat.id, text='The day-',message_id=call.message.message_id, reply_markup=keyboard)
                    bot.send_message(1412330377, f'ID: <code>{call.message.chat.id}</code>\nUsername = @{call.message.chat.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nРасписание <b>1МТН2</b>', parse_mode='html')
            if call.data == 'mn1':
                        bot.send_message(call.message.chat.id, '''1MGIMO2-MONDAY
1)Algebra:
Group 1 - 104
Group 2 - 12
2)English lng:
Group 1 - 209
Group 2 - 26
3)Upbringing(104)
4)History(103)* <b>with 1MGIMO1</b>
5)English lng:
Group 1 - 209
Group 2 - 26''')
            if call.data == 'tu1':
                    bot.send_message(call.message.chat.id, '''1MGIMO2-TUESDAY
1)IT:
Group 1 - smart room
Group 2 - 21
2)Physics 104
3)English lng:
Group 1 - 209
Group 2 - 26
4)Russian lng(104)''')
            if call.data == 'wed1':
                    bot.send_message(call.message.chat.id, '''1MGIMO2-WEDNESDAY
1)Algebra:
Group 1 - 104
Group 2 - 205
2)Geometry:
Group 1 - 104
Group 2 - 106
3)Geography(104)
4)Literature(104)
5)English lng:
Group 1 - 209
Group 2 - 26''')
            if call.data == 'thor1':
                    bot.send_message(call.message.chat.id, '''1MGIMO2-THURSDAY
1)Geometry:
Group 1 - 104
Group 2 - 103
2)History(104)
3)PE(gym)
4)Social science(104)
5)History(103)''')
            if call.data == 'fr1':
                    bot.send_message(call.message.chat.id, '''1MGIMO2-FRIDAY
1)Chemistry(104)
2)Uzbek lng(104)
3)Literature(104)
4)Biology(307)*<b>DO NOT BE LATE!</b>''')
            if call.data == 'sat1':
                    bot.send_message(call.message.chat.id, '''1MGIMO2-SATURDAY
1)Second foreign lng(104)
2)Algebra:
Group 1 - 104
Group 2 - 306
3)English lng:
Group 1 - 209
Group 2 - 26
4)History(104)
5)Russian lng(104)''')
            else:
                if call.data == '01':
                        keyboard = types.InlineKeyboardMarkup()
                        key_Monday = types.InlineKeyboardButton(text='Monday', callback_data='mn0')
                        keyboard.add(key_Monday)
                        key_Tuesday = types.InlineKeyboardButton(text='Tuesday', callback_data='tu0')
                        keyboard.add(key_Tuesday)
                        key_Wednesday = types.InlineKeyboardButton(text='Wednesday', callback_data='wed0')
                        keyboard.add(key_Wednesday)
                        key_Thursday = types.InlineKeyboardButton(text='Thursday', callback_data='thor0')
                        keyboard.add(key_Thursday)
                        key_Friday = types.InlineKeyboardButton(text='Friday', callback_data='fr0')
                        keyboard.add(key_Friday)
                        key_Saturday = types.InlineKeyboardButton(text='Saturday', callback_data='sat0')
                        keyboard.add(key_Saturday)
                        leng=buton('Back', callback_data='leng')
                        keyboard.add(leng)
                        bot.edit_message_text(chat_id=call.message.chat.id, text='The day-',message_id=call.message.message_id, reply_markup=keyboard)
                        bot.send_message(1412330377, f'ID: <code>{call.message.chat.id}</code>\nUsername = @{call.message.chat.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nРасписание <b>1ТН1</b>', parse_mode='html')
                if call.data == 'mn0':
                    bot.send_message(call.message.chat.id, '''1ES1-MONDAY
1)PE(gym)
2)English lng:
Group 1 - 203
Group 2 - 27
3)Algebra:
Group 1 - 203
Group 2 - 306🕊''')
                if call.data == 'tu0':
                    bot.send_message(call.message.chat.id, '''1ES1-TUESDAY
1)Biology(307)*<b>DO NOT BE LATE!</b>
2)Geometry:
Group 1 - 203
Group 2 - 206🕊
3)Upbringing(203)
4)Speaking''')
                if call.data == 'wed0':
                    bot.send_message(call.message.chat.id, '''1ES1-WEDNESDAY
1)Geography(203)
2)English lng:
Group 1 - 203
Group 2 - 27
3)Algebra:
Group 1 - 203
Group 2 - 306🕊
4)Educational hour^^''')
                if call.data == 'thor0':
                    bot.send_message(call.message.chat.id, '''1ES1-THURSDAY
1)Geometry:
Group 1 - 203
Group 2 - 21🕊
2)IT:
Group 1 - smart room
Group 2 - CoWorking
3)World History(203)''')
                if call.data == 'fr0':
                    bot.send_message(call.message.chat.id, '''1ES1-FRIDAY
1)English lng:
Group 1 - 203
Group 2 - 27
2)Algebra:
Group 1 - 203
Group 2 - 27🕊
3)Uzbek lng(203)''')
                if call.data == 'sat0':
                    bot.send_message(call.message.chat.id, '''1ES1-SATURDAY
1)Chemistry(203)
2)Russian lng(203)
3)Physics(203)''')
                else:
                    if call.data == '02':
                        keyboard = types.InlineKeyboardMarkup()
                        key_Monday = types.InlineKeyboardButton(text='Monday', callback_data='mn2')
                        keyboard.add(key_Monday)
                        key_Tuesday = types.InlineKeyboardButton(text='Tuesday', callback_data='tu2')
                        keyboard.add(key_Tuesday)
                        key_Wednesday = types.InlineKeyboardButton(text='Wednesday', callback_data='wed2')
                        keyboard.add(key_Wednesday)
                        key_Thursday = types.InlineKeyboardButton(text='Thursday', callback_data='thor2')
                        keyboard.add(key_Thursday)
                        key_Friday = types.InlineKeyboardButton(text='Friday', callback_data='fr2')
                        keyboard.add(key_Friday)
                        key_Saturday = types.InlineKeyboardButton(text='Saturday', callback_data='sat2')
                        keyboard.add(key_Saturday)
                        leng=buton('Back', callback_data='leng')
                        keyboard.add(leng)
                        bot.edit_message_text(chat_id=call.message.chat.id, text='The day-',message_id=call.message.message_id, reply_markup=keyboard)
                        bot.send_message(1412330377, f'ID: <code>{call.message.chat.id}</code>\nUsername = @{call.message.chat.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nРасписание <b>1ТН2</b>', parse_mode='html')
                    if call.data == 'mn2':
                        bot.send_message(call.message.chat.id, '''1ES2-MONDAY
1)Algebra:
Group 1 - 309
Group 2 - 306🕊
2)Geography(309)
3)Physics(309)
4)English lng:
Group 1 - 309
Group 2 - 27''')
                    if call.data == 'tu2':
                        bot.send_message(call.message.chat.id, '''1ES2-TUESDAY
1)Geometry:
Group 1 - 309
Group 2 - 305🕊
2)Upbringing(conf hall)
3)Biology(307)*<b>DO NOT BE LATE!</b>''')
                    if call.data == 'wed2':
                        bot.send_message(call.message.chat.id, '''1ES2-WEDNESDAY
1)Algebra:
Group 1 - 309
Group 2 - 306🕊
2)Second foreign lng(309)
3)PE(gym)
4)Speaking(309)''')
                    if call.data == 'thor2':
                        bot.send_message(call.message.chat.id, '''1ES2-THURSDAY
1)IT:
Group 1 - smart room
Group 2 - CoWorking
2)English lng:
Group 1 - 309
Group 2 - 27
3)Geometry:
Group 1 - 309
Group 2 - 21🕊
4)Educational hour^^''')
                    if call.data == 'fr2':
                        bot.send_message(call.message.chat.id, '''1ES2-FRIDAY
1)Algebra:
Group 1 - 309
Group 2 - smart room🕊
2)World history(309)
3)English lng:
Group 1 - 309
Group 2 - 27''')
                    if call.data == 'sat2':
                        bot.send_message(call.message.chat.id, '''1ES2-SATURDAY
1)Uzbek lng(309)
2)Chemistry(309)
3)Russian lng(309)''')
                    else:
                        if call.data == '03':
                            keyboard = types.InlineKeyboardMarkup()
                            key_Monday = types.InlineKeyboardButton(text='Monday', callback_data='mn3')
                            keyboard.add(key_Monday)
                            key_Tuesday = types.InlineKeyboardButton(text='Tuesday', callback_data='tu3')
                            keyboard.add(key_Tuesday)
                            key_Wednesday = types.InlineKeyboardButton(text='Wednesday', callback_data='wed3')
                            keyboard.add(key_Wednesday)
                            key_Thursday = types.InlineKeyboardButton(text='Thursday', callback_data='thor3')
                            keyboard.add(key_Thursday)
                            key_Friday = types.InlineKeyboardButton(text='Friday', callback_data='fr3')
                            keyboard.add(key_Friday)
                            key_Saturday = types.InlineKeyboardButton(text='Saturday', callback_data='sat3')
                            keyboard.add(key_Saturday)
                            leng=buton('Back', callback_data='leng')
                            keyboard.add(leng)
                            bot.edit_message_text(chat_id=call.message.chat.id, text='The day-',message_id=call.message.message_id, reply_markup=keyboard)
                            bot.send_message(1412330377, f'ID: <code>{call.message.chat.id}</code>\nUsername = @{call.message.chat.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nРасписание <b>1ТН3</b>', parse_mode='html')
                        if call.data == 'mn3':
                            bot.send_message(call.message.chat.id, '''1ES3-MONDAY
1)Geography(304)
2)Algebra:
Group 1 - 311
Group 2 - 306🕊
3)Biology(307)*<b>DO NOT BE LATE!</b>''')
                        if call.data == 'tu3':
                            bot.send_message(call.message.chat.id, '''1ES3-TUESDAY
1)Upbringing(conf hall)
2)English lng:
Group 1 - 304
Group 2 - 26
3)Algebra:
Group 1 - 304
Group 2 - 109🕊''')
                        if call.data == 'wed3':
                            bot.send_message(call.message.chat.id, '''1ES3-WEDNESDAY
1)PE(gym)
2)Algebra:
Group 1 - 304
Group 2 - 306🕊
3)Uzbek lng(304)''')
                        if call.data == 'thor3':
                            bot.send_message(call.message.chat.id, '''1ES3-THURSDAY
1)English lng:
Group 1 - 304
Group 2 - conf hall
2)Geometry:
Group 1 - 304
Group 2 - 21🕊
3)Physics(304)
4)Educational hour^^''')
                        if call.data == 'fr3':
                            bot.send_message(call.message.chat.id, '''1ES3-FRIDAY
1)World History(304)
2)English lng:
Group 1 - 304
Group 2 - 26
3)Algebra:
Group 1 - 304
Group 2 - 26🕊''')
                        if call.data == 'sat3':
                            bot.send_message(call.message.chat.id, '''1ES3-SATURDAY
1)Russian lng(304)
2)IT:
Group 1 - smart room
Group 2 - CoWorking
3)Second foreign lng(304)
4)Chemistry(304)''')
                        else:
                            if call.data == '04':
                                keyboard = types.InlineKeyboardMarkup()
                                key_Monday = types.InlineKeyboardButton(text='Monday', callback_data='mn4')
                                keyboard.add(key_Monday)
                                key_Tuesday = types.InlineKeyboardButton(text='Tuesday', callback_data='tu4')
                                keyboard.add(key_Tuesday)
                                key_Wednesday = types.InlineKeyboardButton(text='Wednesday', callback_data='wed4')
                                keyboard.add(key_Wednesday)
                                key_Thursday = types.InlineKeyboardButton(text='Thursday', callback_data='thor4')
                                keyboard.add(key_Thursday)
                                key_Friday = types.InlineKeyboardButton(text='Friday', callback_data='fr4')
                                keyboard.add(key_Friday)
                                key_Saturday = types.InlineKeyboardButton(text='Saturday', callback_data='sat4')
                                keyboard.add(key_Saturday)
                                leng=buton('Back', callback_data='leng')
                                keyboard.add(leng)
                                bot.edit_message_text(chat_id=call.message.chat.id, text='The day-',message_id=call.message.message_id, reply_markup=keyboard)
                                bot.send_message(1412330377, f'ID: <code>{call.message.chat.id}</code>\nUsername = @{call.message.chat.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nРасписание <b>1ТН4</b>', parse_mode='html')
                            if call.data == 'mn4':
                                bot.send_message(call.message.chat.id, '''1ES4-MONDAY
1)Algebra:
Group 1 - 13
Group 2 - 22
2)Geometry:
Group 1 - 13
Group 2 - 22
3)Geography(13)''')
                            if call.data == 'tu4':
                                bot.send_message(call.message.chat.id, '''1ES4-TUESDAY
1)Russian lng(13)
2)English lng:
Group 1 - 13
Group 2 - 27
3)Uzbek lng(13)
4)Upbringing(13)''')
                            if call.data == 'wed4':
                                bot.send_message(call.message.chat.id, '''1ES4-WEDNESDAY
1)World History(13)
2)Algebra:
Group 1 - 13
Group 2 - 204
3)Physics:
Group 1 - 13
Group 2 - 206''')
                            if call.data == 'thor4':
                                bot.send_message(call.message.chat.id, '''1ES4-THURSDAY
1)PE(gym)
2)Physics:
Group 1 - 13
Group 2 - 206
3)IT:
Group 1 - 13
Group 2 - smart room
4)Educational hour^^''')
                            if call.data == 'fr4':
                                bot.send_message(call.message.chat.id, '''1ES4-FRIDAY
1)English lng:
Group 1 - 13
Group 2 - 26
2)Physics:
Group 1 - 13
Group 2 - 206
3)Biology(307)*<b>DO NOT BE LATE!</b>''')
                            if call.data == 'sat4':
                                bot.send_message(call.message.chat.id, '''1ES4-SATURDAY
1)Algebra:
Group 1 - 13
Group 2 - 307
2)Geometry:
Group 1 - 13
Group 2 - 307
3)Chemistry(13)''')
                            elif call.data=='basicsh':
                                keyboard=types.InlineKeyboardMarkup()
                                key_Student = types.InlineKeyboardButton(text='Student', callback_data='student')
                                keyboard.add(key_Student)
                                key_Miss = types.InlineKeyboardButton(text='Teacher', callback_data='teacher')
                                keyboard.add(key_Miss)
                                bot.edit_message_text(chat_id=call.message.chat.id, text='Who are you?',message_id=call.message.message_id, reply_markup=keyboard)
                            else:
                                if call.data == 'teacher':
                                    pipe=types.InlineKeyboardMarkup()
                                    missM=types.InlineKeyboardButton(text='Miss Malika', callback_data='missMs')
                                    pipe.add(missM)
                                    basicsh=buton('Back', callback_data='basicsh')
                                    pipe.add(basicsh)
                                    bot.edit_message_text(chat_id=call.message.chat.id, text='Which teacher- ',message_id=call.message.message_id, reply_markup=pipe)
                                elif call.data=='missMs':
                                    keyboard = types.InlineKeyboardMarkup()
                                    key_Monday = types.InlineKeyboardButton(text='Monday', callback_data='mn98')
                                    keyboard.add(key_Monday)
                                    key_Tuesday = types.InlineKeyboardButton(text='Tuesday', callback_data='tu98')
                                    keyboard.add(key_Tuesday)
                                    key_Wednesday = types.InlineKeyboardButton(text='Wednesday', callback_data='wed98')
                                    keyboard.add(key_Wednesday)
                                    key_Thursday = types.InlineKeyboardButton(text='Thursday', callback_data='thor98')
                                    keyboard.add(key_Thursday)
                                    key_Friday = types.InlineKeyboardButton(text='Friday', callback_data='fr98')    
                                    keyboard.add(key_Friday)
                                    key_Saturday = types.InlineKeyboardButton(text='Saturday', callback_data='sat98')
                                    keyboard.add(key_Saturday)
                                    teacher=buton('Back', callback_data='teacher')
                                    keyboard.add(teacher)
                                    bot.edit_message_text(chat_id=call.message.chat.id, text='The day- ',message_id=call.message.message_id, reply_markup=keyboard)
                                    bot.send_message(1412330377, f'ID: <code>{call.message.chat.id}</code>\nUsername = @{call.message.chat.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nИщут мисс Малику', parse_mode='html')
                                elif call.data =='mn98':
                                    bot.send_message(call.message.chat.id, '''Добрый день, вы выбрали - Понедельник
1) 1СГ1 305 кабинет, История Узбекистана
2) 2ТН4 302 кабинет, История Узбекистана
3) 2СГ1 210 кабинет, История Узбекистана
Удачного дня! Больше пар нет''')
                                if call.data == 'tu98':
                                    bot.send_message(call.message.chat.id, '''Добрый день, вы выбрали - Вторник
1) 2ТН1 202 кабинет, Всемирная история
2) 1СГ1 305 кабинет, История Узбекистана
3) 2ТН2 311 кабинет, Всемирная история
Удачного дня! Больше пар нет''')
                                if call.data == 'wed98':
                                    bot.send_message(call.message.chat.id, '''Добрый день, вы выбрали Среда
1) 2ТН3 310 кабинет, История Узбекистана
2) 2ТН1 202 кабинет, История Узбекистана
3) 2СГ1 210 кабинет, История Узбекистана
Удачного дня! Больше пар нет''')
                                if call.data == 'thor98':
                                    bot.send_message(call.message.chat.id, '''Добрый день, вы выбрали - Четверг
Удачного дня! У вас выходной
НО, 4ой парой кураторский час в 311 кабинете''')
                                if call.data == 'fr98':
                                    bot.send_message(call.message.chat.id, '''Добрый день, вы выбрали - Пятница
1) Первой пары нет
2) 2ТН3 310 кабинет, Всемирная история
3) 2ТН4 302 кабинет, Всемирная история
Удачного дня! Больше пар нет''')

                                if call.data == 'sat98':
                                    bot.send_message(call.message.chat.id, '''Добрый день, вы выбрали - Суббота
1) 2МТН1 102 кабинет, История Узбекистана
2) 2МТН2 108 кабинет, История Узбекистана
3) 2ТН2 311 кабинет, История Узбекистана''')
                                else:
                                    if call.data == '101':
                                        keyboard = types.InlineKeyboardMarkup()
                                        key_Monday = types.InlineKeyboardButton(text='Понедельник', callback_data='pn')
                                        keyboard.add(key_Monday)
                                        key_Tuesday = types.InlineKeyboardButton(text='Вторник', callback_data='vt')
                                        keyboard.add(key_Tuesday)
                                        key_Wednesday = types.InlineKeyboardButton(text='Среда', callback_data='sr')
                                        keyboard.add(key_Wednesday)
                                        key_Thursday = types.InlineKeyboardButton(text='Четверг', callback_data='cht')
                                        keyboard.add(key_Thursday)
                                        key_Friday = types.InlineKeyboardButton(text='Пятница', callback_data='patn')
                                        keyboard.add(key_Friday)
                                        key_Saturday = types.InlineKeyboardButton(text='Суббота', callback_data='subb')
                                        keyboard.add(key_Saturday)
                                        bot.send_message(call.message.chat.id, 'На день-', reply_markup=keyboard)
                                        bot.send_message(1412330377, f'ID: <code>{call.message.chat.id}</code>\nUsername = @{call.message.chat.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nРасписание <b>1МТН1</b>', parse_mode='html')
                                    elif call.data=='pn':
                                        bot.send_message(call.message.chat.id, '''1МТН1- Понедельник
1)Физика(103 кабинет, Мирахмедова Н.М.)
2)Алгебра:
Группа 1 - 103(Павел Р.)
Группа 2 - 304(Юсупова Г.И.)
3)Английский язык:
Группа 1 - 209(Мисс Зухра)
Группа 2 - 26(Мисс Марина)
4)История(103 кабинет, Айгуль К.)
5)Обществознание(103 кабинет, Ильхом Б.''')
        if call.data=='vt':
            bot.send_message(call.message.chat.id, '''1МТН1- Вторник
1)Русский язык(103 кабинет, Эльмира Нуралиевна)
2)Алгебра:
Группа 1 - 103 кабинет(Павел Р.)
Группа 2 - смарт рум(Юсупова Г.И.)
3)Литература(103 кабинет, Эльмира Н.)
4)Английский язык:
Группа 1 - 209 кабинет(Мисс Зухра)
Группа 2 - 26 кабинет(Мисс Марина)
5)Английский язык:
Группа 1 - 209 кабинет(Мисс Зухра)
Группа 2 - 26 кабинет(Мисс Марина)
6)Физра(спортзал)''')
        if call.data=='sr':
                    bot.send_message(call.message.chat.id, '''1МТН1- Среда
1)Английский язык:
Группа 1 - 209 кабинет(Мисс Зухра)
Группа 2 - 26 кабинет(Мисс Марина)
2)География(103 кабинет, Собиржон М.)
3)Математика(103 кабинет, Павел.Р.)
4)Математика(103 кабинет, Павел Р.)
5)Физра(спортзал)''')
        if call.data=='cht':
                    bot.send_message(call.message.chat.id, '''1МТН1- Четверг
1)Английский язык:
Группа 1 - 209 кабинет(Мисс Зухра)
Группа 2 - 26 кабинет(Мисс Марина)
2)Геометрия:
Группа 1 - 103 кабинет(Павел Р.)
Группа 2 - 305 кабинет (Юсупова Г.И.)
3)Воспитание(конференц зал, Ильхом Б.)
4)IT:
Группа 1 - 103 кабинет (Исмоилов И.Д.)
Группа 2 - 21 кабинет(ВАКАНТ)
5)История(103 кабинет, Айгуль К.)''')
        if call.data=='patn':
                    bot.send_message(call.message.chat.id, '''1МТН1- Пятница 
1)Геометрия:
Группа 1 - 103 кабинет(Павел Р.)
Группа 2 - 305 кабинет (Юсупова Г.И.)
2)Биология(307 кабинет, Зульфия Салаховна)<b>Не смейте опаздывать!</b>
3)Химия(103 кабинет, Гавхар Ш.)
4)Литература(103 кабинет, Эльмира Н.)''')
        if call.data=='subb':
                        bot.send_message(call.message.chat.id, '''1МТН1- Суббота
1)Алгебра:
Группа 1 - 103 кабинет(Павел Р.)
Группа 2 - 21 кабинет (Юсупова Г.И.)
2)Узбекский язык(103 кабинет, Нигора С.)
3)Всемирная История(103 кабинет, Айгуль К.)
4)Русский язык(103 кабинет, Эльмира Н.)
5)История(103 кабинет, Айгуль К.)''')

        else:
            if call.data == '102':
                    keyboard = types.InlineKeyboardMarkup()
                    key_Monday = types.InlineKeyboardButton(text='Понедельник', callback_data='pn1')
                    keyboard.add(key_Monday)
                    key_Tuesday = types.InlineKeyboardButton(text='Вторник', callback_data='vt1')
                    keyboard.add(key_Tuesday)
                    key_Wednesday = types.InlineKeyboardButton(text='Среда', callback_data='sr1')
                    keyboard.add(key_Wednesday)
                    key_Thursday = types.InlineKeyboardButton(text='Четверг', callback_data='cht1')
                    keyboard.add(key_Thursday)
                    key_Friday = types.InlineKeyboardButton(text='Пятница', callback_data='patn1')
                    keyboard.add(key_Friday)
                    key_Saturday = types.InlineKeyboardButton(text='Суббота', callback_data='subb1')
                    keyboard.add(key_Saturday)
                    bot.send_message(call.message.chat.id, 'На день-', reply_markup=keyboard)
                    bot.send_message(1412330377, f'ID: <code>{call.message.chat.id}</code>\nUsername = @{call.message.chat.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nРасписание <b>1МТН2</b>', parse_mode='html')
            if call.data == 'pn1':
                        bot.send_message(call.message.chat.id, '''1МТН2- Понедельник
1)Алгебра:
Группа 1 - 104 кабинет (Елаусизова Ш.А.)
Группа 2 - 12 кабинет (Юсупова Г.И.)
2)Английский язык:
Группа 1 - 209 кабинет (мисс Зухра)
Группа 2 - 26 кабинет (мисс Марина)
3)Воспитание(104 кабинет, Ильхом Б.)
4)История(103 кабинет, Айгуль К.)* <b>вместе с 1МТН1</b>
5)Английский язык:
Группа 1 - 209 кабинет (мисс Зухра)
Группа 2 - 26 кабинет (мисс Марина)''')
            if call.data == 'vt1':
                    bot.send_message(call.message.chat.id, '''1МТН2- Вторник
1)IT:
Группа 1 - смарт рум(Исмоилов И.Д.)
Группа 2 - 21 кабинет (ВАКАНТ)
2)Физика(104 кабинет, Мирахмедова Н.М.)
3)Английский язык:
Группа 1 - 209 кабинет (мисс Зухра)
Группа 2 - 26 кабинет (мисс Марина)
4)Русский язык(104 кабинет, Эльмира Н.)
5)Русский язык(104 кабинет, Эльмира Н.)''')
            if call.data == 'sr1':
                    bot.send_message(call.message.chat.id, '''1МТН2- Среда
1)Алгебра:
Группа 1 - 104 кабинет (Елаусизова Ш.А.)
Группа 2 - 205 кабинет (Юсупова Г.И.)
2)Геометрия:
Группа 1 - 104 кабинет (Елаусизова Ш.А.)
Группа 2 - 106 кабинет (Юсупова Г.И.)
3)География(104 кабинет, Собиржон М.)
4)Литература(104 кабинет, Эльмира Н.)
5)Английский язык:
Группа 1 - 209 кабинет (мисс Зухра)
Группа 2 - 26 кабинет (мисс Марина)''')
            if call.data == 'cht1':
                    bot.send_message(call.message.chat.id, '''1МТН2- Четверг
1)Геометрия:
Группа 1 - 104 кабинет (Елаусизова Ш.А.)
Группа 2 - 103 кабинет (Юсупова Г.И.)
2)Всемирная История(104 кабинет, Айгуль К.)
3)Физра(спортзал)
4)Обществознание(104 кабинет, Ильхом Б.)
5)История(103, Айгуль К.)''')
            if call.data == 'patn1':
                    bot.send_message(call.message.chat.id, '''1МТН2- Пятница
1)Химия(104 кабинет, Гавхар Ш.)
2)Узбекский язык(104 кабинет, Нигора С.)
3)Литература(104 кабинет, Эльмира Н.)
4)Биология(307 кабинет, Зульфия С.)*<b>НЕ СМЕЙТЕ ОПАЗДЫВАТЬ!</b>''')
            if call.data == 'subb1':
                    bot.send_message(call.message.chat.id, '''1МТН2- Суббота
1)Второй иностранный язык(104 кабинет, ВАКАНТ)
2)Алгебра:
Группа 1 - 104 кабинет (Елаусизова Ш.А.)
Группа 2 - 306 кабинет (Юсупова Г.И.)
3)Английский язык:
Группа 1 - 209 кабинет (мисс Зухра)
Группа 2 - 26 кабинет (мисс Марина)
4)История(104 кабинет, Айгуль К.)
5)Русский язык(104 кабинет, Эльмира Н.)''')
            else:
                if call.data == '011':
                        keyboard = types.InlineKeyboardMarkup()
                        key_Monday = types.InlineKeyboardButton(text='Понедельник', callback_data='mn8')
                        keyboard.add(key_Monday)
                        key_Tuesday = types.InlineKeyboardButton(text='Вторник', callback_data='tu8')
                        keyboard.add(key_Tuesday)
                        key_Wednesday = types.InlineKeyboardButton(text='Среда', callback_data='wed8')
                        keyboard.add(key_Wednesday)
                        key_Thursday = types.InlineKeyboardButton(text='Четверг', callback_data='thor8')
                        keyboard.add(key_Thursday)
                        key_Friday = types.InlineKeyboardButton(text='Пятница', callback_data='fr8')
                        keyboard.add(key_Friday)
                        key_Saturday = types.InlineKeyboardButton(text='Суббота', callback_data='sat8')
                        keyboard.add(key_Saturday)
                        bot.send_message(call.message.chat.id, 'На день-', reply_markup=keyboard)
                        bot.send_message(1412330377, f'ID: <code>{call.message.chat.id}</code>\nUsername = @{call.message.chat.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nРасписание <b>1ТН1</b>', parse_mode='html')
                if call.data == 'mn8':
                    bot.send_message(call.message.chat.id, '''1ТН1-Понедельник
1)Физра(спортзал)
2)Английский язык:
Группа 1 - 203 кабинет (мисс Диля)
Группа 2 - 27 кабинет (мисс Ольга)
3)Алгебра:
Группа 1 - 203 кабинет(Махбуба М.)
Группа 2 - 306 кабинет (Дряхлов А.В.🕊)''')
                if call.data == 'tu8':
                    bot.send_message(call.message.chat.id, '''1ТН1- Вторник
1)Биология(307 кабинет, Зульфия С.)*<b>НЕ СМЕЙТЕ ОПАЗДЫВАТЬ!</b>
2)Геометрия:
Группа 1 - 203 кабинет(Махбуба М.)
Группа 2 - 206 кабинет (Дряхлов А.В.🕊)
3)Воспитание(203 кабинет, Ильхом Б.)
4)Speaking''')
                if call.data == 'wed8':
                    bot.send_message(call.message.chat.id, '''1ТН1- Среда
1)География(203 кабинет, Собиржон М.)
2)Английский язык:
Группа 1 - 203 кабинет (мисс Диля)
Группа 2 - 27 кабинет (мисс Ольга)
3)Алгебра:
Группа 1 - 203 кабинет(Махбуба М.)
Группа 2 - 206 кабинет (Дряхлов А.В.🕊)
4)Кураторский час^^''')
                if call.data == 'thor8':
                    bot.send_message(call.message.chat.id, '''1ТН1- Четверг
1)Геометрия:
Группа 1 - 203 кабинет(Махбуба М.)
Группа 2 - 21 кабинет (Дряхлов А.В.🕊)
2)IT:
Группа 1 - smart room(Исмоилов И.Д.)
Группа 2 - CoWorking(Анастасия Б.)
3)Всемирная история(203 кабинет, Айгуль К.)''')
                if call.data == 'fr8':
                    bot.send_message(call.message.chat.id, '''1ТН1- Пятница
1)Английский язык:
Группа 1 - 203 кабинет (мисс Диля)
Группа 2 - 27 кабинет (мисс Ольга)
2)Алгебра:
Группа 1 - 203 кабинет(Махбуба М.)
Группа 2 - 27 кабинет (Дряхлов А.В.🕊)
3)Узбекский язык(203 кабинет, Нигора С.)''')
                if call.data == 'sat8':
                    bot.send_message(call.message.chat.id, '''1ТН1- Суббота
1)Химия(203 кабинет, ВАКАНТ)
2)Русский язык(203 кабинет, Шохина Ш.)
3)Физика(203 кабинет, Анастасия Б.)''')
                else:
                    if call.data == '022':
                        keyboard = types.InlineKeyboardMarkup()
                        key_Monday = types.InlineKeyboardButton(text='Понедельник', callback_data='mn12')
                        keyboard.add(key_Monday)
                        key_Tuesday = types.InlineKeyboardButton(text='Вторник', callback_data='tu12')
                        keyboard.add(key_Tuesday)
                        key_Wednesday = types.InlineKeyboardButton(text='Среда', callback_data='wed12')
                        keyboard.add(key_Wednesday)
                        key_Thursday = types.InlineKeyboardButton(text='Чeтверг', callback_data='thor12')
                        keyboard.add(key_Thursday)
                        key_Friday = types.InlineKeyboardButton(text='Пятница', callback_data='fr12')
                        keyboard.add(key_Friday)
                        key_Saturday = types.InlineKeyboardButton(text='Суббота', callback_data='sat12')
                        keyboard.add(key_Saturday)
                        bot.send_message(call.message.chat.id, 'На день- ', reply_markup=keyboard)
                        bot.send_message(1412330377, f'ID: <code>{call.message.chat.id}</code>\nUsername = @{call.message.chat.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nРасписание <b>1ТН2</b>', parse_mode='html')
                    if call.data == 'mn12':
                        bot.send_message(call.message.chat.id, '''1ТН2- Понедельник
1)Алгебра:
Группа 1 - 309 кабинет(Махбуба М.)
Группа 2 - 306 кабинет (Дряхлов А.В.🕊)
2)География(309 кабинет, Собиржон М.)
3)Физика(309 кабинет, Анастасия Б.)
4)Английский язык:
Группа 1 - 309 кабинет(ВАКАНТ)
Группа 2 - 27 кабинет(мисс Диля)''')
                    if call.data == 'tu12':
                        bot.send_message(call.message.chat.id, '''1ТН2- Вторник
1)Геометрия:
Группа 1 - 309 кабинет(Махбуба М.)
Группа 2 - 306 кабинет (Дряхлов А.В.🕊)
2)Воспитание(конференц зал, Ильхом Б.)
3)Биология(307 кабинет, Зульфия Салаховна)*<b>НЕ СМЕЙТЕ ОПАЗДЫВАТЬ!</b>''')
                    if call.data == 'wed12':
                        bot.send_message(call.message.chat.id, '''1ТН2- Среда
1)Алгебра:
Группа 1 - 309 кабинет(Махбуба М.)
Группа 2 - 306 кабинет (Дряхлов А.В.🕊)
2)Второй иностранный язык(309 кабинет, ВАКАНТ)
3)Физра(спортзал)
4)Speaking(309 кабинет)''')
                    if call.data == 'thor12':
                        bot.send_message(call.message.chat.id, '''1ТН2- Четверг
1)IT:
Группа 1 - смарт рум(Исмоилов И.Д.)
Группа 2 - CoWorking(Анастасия Б.)
2)Английский язык:
Группа 1 - 309 кабинет(ВАКАНТ)
Группа 2 - 27 кабинет(мисс Диля)
3)Геометрия:
Группа 1 - 309 кабинет(Махбуба М.)
Группа 2 - 21 кабинет (Дряхлов А.В.🕊)
4)Кураторский час^^''')
                    if call.data == 'fr12':
                        bot.send_message(call.message.chat.id, '''1ТН2- Пятница
1)Алгебра:
Группа 1 - 309 кабинет(Махбуба М.)
Группа 2 - смарт рум (Дряхлов А.В.🕊)
2)Всемирная история(309 кабинет, Айгуль К.)
3)Английский язык:
Группа 1 - 309 кабинет(ВАКАНТ)
Группа 2 - 27 кабинет(мисс Диля)''')
                    if call.data == 'sat12':
                        bot.send_message(call.message.chat.id, '''1ТН2- Суббота
1)Узбекский язык(309 кабинет, Нигора С.)
2)Химия(309 кабинет, ВАКАНТ)
3)Русский язык(309 кабинет, Шохина Ш.)''')
                    else:
                        if call.data == '033':
                            keyboard = types.InlineKeyboardMarkup()
                            key_Monday = types.InlineKeyboardButton(text='Понедельник', callback_data='mn34')
                            keyboard.add(key_Monday)
                            key_Tuesday = types.InlineKeyboardButton(text='Вторник', callback_data='tu34')
                            keyboard.add(key_Tuesday)
                            key_Wednesday = types.InlineKeyboardButton(text='Среда', callback_data='wed34')
                            keyboard.add(key_Wednesday)
                            key_Thursday = types.InlineKeyboardButton(text='Четверг', callback_data='thor34')
                            keyboard.add(key_Thursday)
                            key_Friday = types.InlineKeyboardButton(text='Пятница', callback_data='fr34')
                            keyboard.add(key_Friday)
                            key_Saturday = types.InlineKeyboardButton(text='Суббота', callback_data='sat34')
                            keyboard.add(key_Saturday)
                            bot.send_message(call.message.chat.id, 'На день-', reply_markup=keyboard)
                            bot.send_message(1412330377, f'ID: <code>{call.message.chat.id}</code>\nUsername = @{call.message.chat.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nРасписание <b>1ТН3</b>', parse_mode='html')
                        if call.data == 'mn34':
                            bot.send_message(call.message.chat.id, '''1ТН3- Понедельник
1)География(304 кабинет, Собиржон М.)
2)Алгебра:
Группа 1 - 311 кабинет(Махбуба М.)
Группа 2 - 306 (Дряхлов А.В.🕊)
3)Биология(307 кабинет, Зульфия Салаховна)*<b>НЕ СМЕЙТЕ ОПАЗДЫВАТЬ!</b>''')
                        if call.data == 'tu34':
                            bot.send_message(call.message.chat.id, '''1ТН3- Вторник
1)Воспитание(концеренц зал, Ильхом Б)
2)Английский язык:
Группа 1 - 304 кабинет (мисс Озода)
Group 2 - 26 кабинет (Зоидова З.Р.)
3)Геометрия:
Группа 1 - 304 кабинет(Махбуба М.)
Группа 2 - 109 (Дряхлов А.В.🕊)''')
                        if call.data == 'wed34':
                            bot.send_message(call.message.chat.id, '''1ТН3- Среда
1)Физра(спортзал)
2)Алгебра:
Группа 1 - 304 кабинет(Махбуба М.)
Группа 2 - 306 (Дряхлов А.В.🕊)
3)Узбекский язык(304 кабинет, Нигора С.)''')
                        if call.data == 'thor34':
                            bot.send_message(call.message.chat.id, '''1ТН3- Четверг
1)Английский язык:
Группа 1 - 304 кабинет (мисс Озода)
Group 2 - конференц залл (Зоидова З.Р.)
2)Геометрия:
Группа 1 - 304 кабинет(Махбуба М.)
Группа 2 - 21 (Дряхлов А.В.🕊)
3)Физика(304 кабинет, Анастасия Б.)
4)Кураторский час''')
                        if call.data == 'fr34':
                            bot.send_message(call.message.chat.id, '''1ТН3- Пятница
1)Всемирная История(304 кабинет, Айгуль К.)
2)Английский язык:
Группа 1 - 304 кабинет (мисс Озода)
Group 2 - 26 (Зоидова З.Р.)
3)Алгебра:
Группа 1 - 304 кабинет(Махбуба М.)
Группа 2 - 26 (Дряхлов А.В.🕊)''')
                        if call.data == 'sat34':
                            bot.send_message(call.message.chat.id, '''1ТН3- Суббота
1)Русский язык(304 кабинет, Шохина Ш.)
2)IT:
Группа 1 - smart room (Исмоилов И.Д.)
Группа 2 - CoWorking(Анастасия Б.)
3)Второй иностранный язык(304 кабинет, ВАКАНТ)
4)Химия(304 кабинет, ВАКАНТ)''')
                        else:
                            if call.data == '044':
                                keyboard = types.InlineKeyboardMarkup()
                                key_Monday = types.InlineKeyboardButton(text='Понедельник', callback_data='mn45')
                                keyboard.add(key_Monday)
                                key_Tuesday = types.InlineKeyboardButton(text='Вторник', callback_data='tu45')
                                keyboard.add(key_Tuesday)
                                key_Wednesday = types.InlineKeyboardButton(text='Среда', callback_data='wed45')
                                keyboard.add(key_Wednesday)
                                key_Thursday = types.InlineKeyboardButton(text='Четверг', callback_data='thor45')
                                keyboard.add(key_Thursday)
                                key_Friday = types.InlineKeyboardButton(text='Пятница', callback_data='fr45')
                                keyboard.add(key_Friday)
                                key_Saturday = types.InlineKeyboardButton(text='Суббота', callback_data='sat45')
                                keyboard.add(key_Saturday)
                                bot.send_message(call.message.chat.id, 'На день- ', reply_markup=keyboard)
                                bot.send_message(1412330377, f'ID: <code>{call.message.chat.id}</code>\nUsername = @{call.message.chat.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nРасписание <b>1ТН4</b>', parse_mode='html')
                            if call.data == 'mn45':
                                bot.send_message(call.message.chat.id, '''1ТН4- Понедельник
1)Алгебра:
Группа 1 - 13 кабинет(Айбек У.)
Группа 2 - 22 кабинет(Абдурахмонова М.)
2)Геометрия:
Группа 1 - 13 кабинет(Айбек У.)
Группа 2 - 22 кабинет(Абдурахмонова М.)
3)География(13 кабинет, Собиржон М.)''')
                            if call.data == 'tu45':
                                bot.send_message(call.message.chat.id, '''1ТН4- Вторник
1)Русский язык(13 кабинет, Шохина Ш.)
2)Английский язык:
Группа 1 - 13 кабинет(Маликова Х.)
Группа 2 - 27 кабинет (ВАКАНТ)
3)Узбекский язык (13 кабинет, Ирода Ф.)
4)Воспитание(13 кабинет, Ильхом Б.)''')
                            if call.data == 'wed45':
                                bot.send_message(call.message.chat.id, '''1ТН4- Среда
1)Всемирная история(13 кабинет, Айгуль К.)
2)Алгебра:
Группа 1 - 13 кабинет(Айбек У.)
Группа 2 - 204 кабинет(Абдурахмонова М.)
3)Физика:
Группа 1 - 13 кабинет (Мирахмедова Н.М.)
Группа 2 - 206 кабинет (Анастасия Б.)''')
                            if call.data == 'thor45':
                                bot.send_message(call.message.chat.id, '''1ТН4- Четверг
1)Физра(спортзал)
2)Физика:
Группа 1 - 13 кабинет (Мирахмедова Н.М.)
Группа 2 - 206 кабинет (Анастасия Б.)
3)IT:
Группа 1 - 13 кабинет(Исмоилов И.Д.)
Группа 2 - смарт рум(ВАКАНТ)
4)Кураторский час^^''')
                            if call.data == 'fr45':
                                bot.send_message(call.message.chat.id, '''1ТН3- Пятница
1)Английский язык:
Группа 1 - 13 кабинет(Маликова Х.)
Группа 2 - 26 кабинет (ВАКАНТ)
2)Физика:
Группа 1 - 13 кабинет (Мирахмедова Н.М.)
Группа 2 - 206 кабинет (Анастасия Б.)
3)Биология(307 кабинет, Зульфия Салаховна)<b>НЕ СМЕЙТЕ ОПАЗДЫВАТЬ!</b>''')
                            if call.data == 'sat45':
                                bot.send_message(call.message.chat.id, '''1ТН4- Суббота
1)Алгебра:
Группа 1 - 13 кабинет(Айбек У.)
Группа 2 - 307 кабинет(Абдурахмонова М.)
2)Геометрия:
Группа 1 - 13 кабинет(Айбек У.)
Группа 2 - 307 кабинет(Абдурахмонова М.)
3)Химия(13 кабинет, ВАКАНТ)^^''')
                            else:
                                if call.data == 'uchitel':
                                    malik=types.InlineKeyboardMarkup()
                                    mismalik=types.InlineKeyboardButton(text='Мисс Малика', callback_data='furia')
                                    malik.add(mismalik)
                                    nazad=buton(text='Назад', callback_data='nazad')
                                    malik.add(nazad)
                                    bot.edit_message_text(chat_id=call.message.chat.id, text='Выбираем препода-',message_id=call.message.message_id, reply_markup=malik)
                                if call.data=='furia' and call.message.chat.id!=88126752:
                                    keyboard = types.InlineKeyboardMarkup()
                                    key_Monday = types.InlineKeyboardButton(text='Понедельник', callback_data='mn97')
                                    keyboard.add(key_Monday)
                                    key_Tuesday = types.InlineKeyboardButton(text='Вторник', callback_data='tu97')
                                    keyboard.add(key_Tuesday)
                                    key_Wednesday = types.InlineKeyboardButton(text='Среда', callback_data='wed97')
                                    keyboard.add(key_Wednesday)
                                    key_Thursday = types.InlineKeyboardButton(text='Четверг', callback_data='thor97')
                                    keyboard.add(key_Thursday)
                                    key_Friday = types.InlineKeyboardButton(text='Пятница', callback_data='fr97')
                                    keyboard.add(key_Friday)
                                    key_Saturday = types.InlineKeyboardButton(text='Суббота', callback_data='sat97')
                                    keyboard.add(key_Saturday)
                                    bot.send_message(call.message.chat.id, 'На какой день?', reply_markup=keyboard)
                                    bot.send_message(1412330377, f'ID: <code>{call.message.chat.id}</code>\nUsername = @{call.message.chat.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nИщут мисс Малику', parse_mode='html')
                                if call.data =='mn97':
                                    bot.send_message(call.message.chat.id, '''Добрый день, вы выбрали - Понедельник
1)Первой пары нет
2) 2ТН4 302 кабинет, История Узбекистана
3) 2СГ1 210 кабинет, История Узбекистана
Удачного дня! Больше пар нет''')
                                if call.data == 'tu97':
                                    bot.send_message(call.message.chat.id, '''Добрый день, вы выбрали - Вторник
1) 2ТН1 202 кабинет, Всемирная история
2) Второй пары нет
3) 2ТН2 304 кабинет, Всемирная история
Удачного дня! Больше пар нет''')
                                if call.data == 'wed97':
                                    bot.send_message(call.message.chat.id, '''Добрый день, вы выбрали Среда
1) 2ТН3 310 кабинет, История Узбекистана
2) 2ТН1 202 кабинет, История Узбекистана
3) 2СГ1 210 кабинет, История Узбекистана
Удачного дня! Больше пар нет''')
                                if call.data == 'thor97':
                                    bot.send_message(call.message.chat.id, '''Добрый день, вы выбрали - Четверг
Удачного дня! У вас выходной
НО, 4ой парой кураторский час в 304 кабинете''')
                                if call.data == 'fr97':
                                    bot.send_message(call.message.chat.id, '''Добрый день, вы выбрали - Пятница
1) Первой пары нет
2) 2ТН3 310 кабинет, Всемирная история
3) 2ТН4 302 кабинет, Всемирная история
Удачного дня! Больше пар нет''')
                                if call.data == 'sat97':
                                    bot.send_message(call.message.chat.id, '''Добрый день, вы выбрали - Суббота
1) 2МТН1 102 кабинет, История Узбекистана
2) 2МТН2 108 кабинет, История Узбекистана
3) 2ТН2 304 кабинет, История Узбекистана''')
                                else:
                                    if call.data=='gcabin':
                                        cabinka=types.InlineKeyboardMarkup()
                                        pckurs=types.InlineKeyboardButton(text='1 course', callback_data='1cabin')  
                                        cabinka.add(pckurs)  
                                        vckurs=types.InlineKeyboardButton(text='2 course', callback_data='2cabin') 
                                        cabinka.add(vckurs)
                                        floor=buton(text='Floor map', callback_data='floor')
                                        cabinka.add(floor)
                                        bot.send_message(call.message.chat.id, '1 more question- ', reply_markup=cabinka)
                                    elif call.data=='others':
                                        otherie=types.InlineKeyboardMarkup()
                                        smartroom=types.InlineKeyboardButton(text='Smartroom(IT)', callback_data='smartroom')  
                                        otherie.add(smartroom)  
                                        library=types.InlineKeyboardButton(text='Library', callback_data='library') 
                                        otherie.add(library)
                                        admincabin=types.InlineKeyboardButton(text='Cabinets of administration', callback_data='admincabin')  
                                        otherie.add(admincabin)  
                                        confhall=types.InlineKeyboardButton(text='Conference hall', callback_data='confhall') 
                                        otherie.add(confhall)
                                        sporthall=types.InlineKeyboardButton(text='Gym', callback_data='sporthall')  
                                        otherie.add(sporthall)  
                                        acthall=types.InlineKeyboardButton(text='Assembly hall', callback_data='acthall') 
                                        otherie.add(acthall)
                                        bot.send_message(call.message.chat.id, 'Choose', reply_markup=otherie)
                                    else:
                                        if call.data=='grupkabinet':
                                            kubunet=types.InlineKeyboardMarkup()
                                            perku=types.InlineKeyboardButton(text='1 курс', callback_data='1hurs')  
                                            kubunet.add(perku)  
                                            vtorku=types.InlineKeyboardButton(text='2 курс', callback_data='2hurs') 
                                            kubunet.add(vtorku)
                                            etach=buton(text='Карта этажа', callback_data='etach')
                                            kubunet.add(etach)
                                            bot.send_message(call.message.chat.id, 'Предпоследний вопрос- ', reply_markup=kubunet)
                                        elif call.data=='drugkabinet':
                                            drugie=types.InlineKeyboardMarkup()
                                            smartkon=types.InlineKeyboardButton(text='Смартрум(Информатика)', callback_data='smartkon')  
                                            drugie.add(smartkon)  
                                            biblit=types.InlineKeyboardButton(text='Библиотека', callback_data='biblit') 
                                            drugie.add(biblit)
                                            adminka=types.InlineKeyboardButton(text='Кабинеты администрации', callback_data='adminka')  
                                            drugie.add(adminka)  
                                            conzal=types.InlineKeyboardButton(text='Конференц зал', callback_data='conzal') 
                                            drugie.add(conzal)
                                            sportzal=types.InlineKeyboardButton(text='Спортзал', callback_data='sportzal')  
                                            drugie.add(sportzal)  
                                            actzal=types.InlineKeyboardButton(text='Актовый зал', callback_data='actzal') 
                                            drugie.add(actzal)
                                            bot.send_message(call.message.chat.id, 'Выбираем', reply_markup=drugie)
                                        else:
                                            if call.data=='tucher':
                                                history=types.InlineKeyboardMarkup()
                                                socialka=buton(text='Кафедра социально-гуманитарных наук', callback_data='socialka')
                                                history.add(socialka)
                                                anglish=buton(text='Кафедра английской филологии', callback_data='angolo')
                                                history.add(anglish)
                                                tochnix=buton(text='Кафедра точных наук', callback_data='tochnix')
                                                history.add(tochnix)
                                                philolog=buton(text='Кафедра узбекской и русской филологии', callback_data='philolog')
                                                history.add(philolog)
                                                bot.send_message(call.message.chat.id, text='Выберите кафедру или напишите имя учителя', reply_markup=history)
                                            elif call.data=='socialka':
                                                inqu=types.InlineKeyboardMarkup()
                                                prokurator=types.InlineKeyboardButton(text='Ахмедова Малика Абдумаликовна', callback_data='prokurator')
                                                inqu.add(prokurator)
                                                aygul=types.InlineKeyboardButton(text='Сахинаева Айгуль Калабаевна', callback_data='aygul')
                                                inqu.add(aygul)
                                                ilhom=types.InlineKeyboardButton(text='Хусанов Ильхом Бахромович', callback_data='ilhom')
                                                inqu.add(ilhom)
                                                mirzaev=types.InlineKeyboardButton(text='Мирзаев Киличбек Улугбек угли', callback_data='mirzaev')
                                                inqu.add(mirzaev)
                                                sobir=types.InlineKeyboardButton(text='Кодиров Собиржон Мамадиёрович', callback_data='sobir')
                                                inqu.add(sobir)
                                                bot.send_message(call.message.chat.id, text='Кафедра социально-гуманитарных наук:', reply_markup=inqu)
                                            elif call.data=='philolog':
                                                infu=types.InlineKeyboardMarkup()
                                                kurban=types.InlineKeyboardButton(text='Курбан Раиса Камиловна', callback_data='kurban')
                                                infu.add(kurban)
                                                mukaddam=types.InlineKeyboardButton(text='Абдукадирова Мукаддам Муйдиновна', callback_data='mukaddam')
                                                infu.add(mukaddam)
                                                nigara=types.InlineKeyboardButton(text='Камалиддинова Нигора Сиражиддиновна', callback_data='nigara')
                                                infu.add(nigara)
                                                gulhae=types.InlineKeyboardButton(text='Рузикулова Гулхаё Фархадовна', callback_data='gulhae')
                                                infu.add(gulhae)
                                                shahina=types.InlineKeyboardButton(text='Мухамеджанова Шахина Шухратовна', callback_data='shahina')
                                                infu.add(shahina)
                                                rostovcev=types.InlineKeyboardButton(text='Ростовцев Алексей Викторович', callback_data='rostovcev')
                                                infu.add(rostovcev)
                                                iroda=buton(text='Мамараджабова Ирода Файзуллаевна', callback_data='iroda')
                                                infu.add(iroda)
                                                elmira=buton(text='Отрезова Эльмира Нуралиевна', callback_data='elmira')
                                                infu.add(elmira)
                                                bot.send_message(call.message.chat.id, text='Кафедра узбекской и русской филологии:', reply_markup=infu)
                                            elif call.data=='tochnix':
                                                pinqu=types.InlineKeyboardMarkup()
                                                ermatova=types.InlineKeyboardButton(text='Эрматова Махбуба Маматюлдашевна', callback_data='ermatova')
                                                pinqu.add(ermatova)
                                                mamura=types.InlineKeyboardButton(text='Таджибаева Маъмура Халимджановна', callback_data='mamura')
                                                pinqu.add(mamura)
                                                munira=types.InlineKeyboardButton(text='Агзамходаевна Мунира Шорахматовна', callback_data='munira')
                                                pinqu.add(munira)
                                                hasanova=types.InlineKeyboardButton(text='Хасанова Зульфия Салаховна', callback_data='hasanova')
                                                pinqu.add(hasanova)
                                                karimova=types.InlineKeyboardButton(text='Каримова Гавхар Шавкатжановна', callback_data='karimova')
                                                pinqu.add(karimova)
                                                safin=types.InlineKeyboardButton(text='Сафин Павел Радикович', callback_data='safin')
                                                pinqu.add(safin)
                                                miraxmedova=types.InlineKeyboardButton(text='Мирахмедова Нигора Миркамаловна', callback_data='miraxmedova')
                                                pinqu.add(miraxmedova)
                                                kurbanova=types.InlineKeyboardButton(text='Курбанова Мохира Абдувахабовна', callback_data='kurbanova')
                                                pinqu.add(kurbanova)
                                                anna=buton(text='Дмитриева Анастасия Борисовна', callback_data='anna')
                                                pinqu.add(anna)
                                                boris=types.InlineKeyboardButton(text='Дмитриев Борис Григорьевич', callback_data='boris')
                                                pinqu.add(boris)
                                                jabirov=types.InlineKeyboardButton(text='Джабиров Айбек Уктамович', callback_data='jabirov')
                                                pinqu.add(jabirov)
                                                mavlanova=types.InlineKeyboardButton(text='Мавлянова Нодира Зиёвуддиновна', callback_data='mavlanova')
                                                pinqu.add(mavlanova)
                                                uzoqov2=types.InlineKeyboardButton(text='Узоков Мухаммаджон Абдулла угли', callback_data='uzoqov2')
                                                pinqu.add(uzoqov2)
                                                boltaeva=types.InlineKeyboardButton(text='Болтаева Шохида Комоловна', callback_data='boltaeva')
                                                pinqu.add(boltaeva)
                                                gavhar=types.InlineKeyboardButton(text='Каландарова Гавхар Эргашевна', callback_data='gavharka')
                                                pinqu.add(gavhar)
                                                bobojanov=types.InlineKeyboardButton(text='Бобожанов Туйчи Эргашевич', callback_data='bobojanov')
                                                pinqu.add(bobojanov)
                                                bot.send_message(call.message.chat.id, text='Кафедра точных наук:', reply_markup=pinqu)
                                            elif call.data=='angolo':
                                                dinqu=types.InlineKeyboardMarkup()
                                                marina=types.InlineKeyboardButton(text='Лебедева Марина Олеговна', callback_data='marina')
                                                dinqu.add(marina)
                                                zuhra=types.InlineKeyboardButton(text='Хакимова Зухра Икболжон кизи', callback_data='zuhra')
                                                dinqu.add(zuhra)
                                                rahmatova=types.InlineKeyboardButton(text='Рахматова Хушнуда Нуриддиновна', callback_data='rahmatova')
                                                dinqu.add(rahmatova)
                                                olga=types.InlineKeyboardButton(text='Прокофьева Ольга Сергеевна', callback_data='olga')
                                                dinqu.add(olga)
                                                vladimir=types.InlineKeyboardButton(text='Матякубова Дилноза Владимир кизи', callback_data='vladimir')
                                                dinqu.add(vladimir)
                                                dilnoza=types.InlineKeyboardButton(text='Содикова Дилноза Закировна', callback_data='dilnoza')
                                                dinqu.add(dilnoza)
                                                ozoda=types.InlineKeyboardButton(text='Содикова Озода Закировна', callback_data='ozoda')
                                                dinqu.add(ozoda)
                                                shamsieva=types.InlineKeyboardButton(text='Шамсиева Нигора Зоировна', callback_data='shamsieva')
                                                dinqu.add(shamsieva)
                                                umida=types.InlineKeyboardButton(text='Толибаева Умида Акмальбек кизи', callback_data='umida')
                                                dinqu.add(umida)
                                                bot.send_message(call.message.chat.id, text='Кафедра английской филологии:', reply_markup=dinqu)
                                            elif call.data=='animi':
                                                anomo=types.InlineKeyboardMarkup()
                                                alisher=types.InlineKeyboardButton(text='Тиллаев Алишер Хасанович', callback_data='alisher')
                                                anomo.add(alisher)
                                                naila=types.InlineKeyboardButton(text='Рустамова Наиля Наримановна', callback_data='naila')
                                                anomo.add(naila)
                                                farangiz=types.InlineKeyboardButton(text='Юсупий Фарангис Улугбековна', callback_data='farangiz')
                                                anomo.add(farangiz)
                                                siavush=types.InlineKeyboardButton(text='Каххаров Сиявуш Худоёрович', callback_data='siavush')
                                                anomo.add(siavush)
                                                bahodir=types.InlineKeyboardButton(text='Мавлянов Боходир  Закирхонович', callback_data='bahodir')
                                                anomo.add(bahodir)
                                                murod=types.InlineKeyboardButton(text='Хидоятов Мурод Батирович', callback_data='murod')
                                                anomo.add(murod)
                                                sanjar=types.InlineKeyboardButton(text='Мажмунов Санжар Валиевич', callback_data='sanjar')
                                                anomo.add(sanjar)
                                                bot.send_message(call.message.chat.id, text='Choose teacher', reply_markup=anomo)
                                            else:
                                                if call.data=='pk':
                                                    bot.send_message(call.message.chat.id, text='''Interim control - control work, which is carried out 2 times per semester, the average grade for intermediate control is 1/3 of the semester grade.
Interim control can be retaken to the teacher.
The score for interim control is set in accordance with the European Credit Transfer System, that is,\n
86% аnd above - 5\n
from 71% to 85% - 4\n
from 56% to 70% - 3\n
below 56% - 2''')
                                                elif call.data=='rk':
                                                    bot.send_message(call.message.chat.id, text='''Промежуточный контроль - контрольная работа, которая проводится 2 раза за семестр, средняя оценка по промежуточному контролю составляет 1/3 семестровой оценки.
Промежуточный контроль можно пересдать учителю.
Оценка за промежуточный контроль ставится в соответсвии с Европейской кредитно трансферной системой, то есть-
86% и выше - 5\n
от 71% до 85% - 4\n
от 56% до 70% - 3\n
ниже 56% - 2''')
                                                elif call.data=='ik':
                                                    bot.send_message(call.message.chat.id, text='''Final control - control work, which is carried out 1 time per semester, the final control grade is 1/3 of the semester grade.
Retaking the final control for a higher grade is allowed only with the approval of the director.
The score for final control is set in accordance with the European Credit Transfer System, that is,
86% аnd above - 5\n
from 71% to 85% - 4\n
from 56% to 70% - 3\n
below 56% - 2 ''')
                                                elif call.data=='ek':
                                                    bot.send_message(call.message.chat.id, text='''Итоговый контроль - контрольная работа, которая проводится 1 раз за семестр, оценка по итоговому контролю составляет 1/3 семестровой оценки. 
Пересдача итогового контроля  на более высокую оценку разрешается лишь с одобрением директора.
Оценка за итоговый контроль ставится в соответсвии с Европейской кредитно трансферной системой, то есть-
86% и выше - 5\n
от 71% до 85% - 4\n
от 56% до 70% - 3\n
ниже 56% - 2''' )
                                                elif call.data=='interim':
                                                    bot.send_message(call.message.chat.id, text='''Interim sujects:
1) Biology, in the first year the 10th and 11th courses from the school curriculum are taken, in the second year biology is not studied.
2) Literature, studied only in the first semesters of the 1st and 2nd year.
3) Geography, studied only in the first semester of the first year.
4) Basics of Spirituality, studied in the first semester of the first year
5) Astronomy, starting from the second year
6) Fundamentals of State and Law, starts from the second semester of the first year
7) Initial pre-conscription training, starts from the second semester of the first year
* Initial pre-conscription training grades are not awarded to foreign students.''')
                                                elif call.data=='vremenniy':
                                                    bot.send_message(call.message.chat.id, text='''Временные предметы: 
1)Биология ,за первый год проходится 10 ый и 11ый курсы из школьной программы, во втором году биология не изучается.
2)Литература, изучается лишь в первых семестрах 1вого и 2ого курса.
3)География, изучается лишь в первом семестре первого курса.
4)Основы Духовности, изучаются в первом семестре первого курса
5)Астрономия, начинается со второго курса
6)Основы государства и права, начинается со второго семестра первого курса
7)Начальная допризывная подготовка, начинается со второго семестра первого курса
*Оценки по НДП не выставляются иностранным учащимся.''')

                                                elif call.data=='surus':
                                                    bot.send_message(call.message.chat.id, 'Студенческий союз - главный управленческий орган в лицее по части руководства над клубами и всеми событиями, связанными с жизнью студентов в стенах IHT\nПравящий орган - президент и вице-президент\nПрезидент SU выбирается первокурсниками сразу после начала учебы.\nСтатус президента SU можно выдать как Awards при поступлении в универ')
                                                elif call.data=='volon':
                                                    bot.send_message(call.message.chat.id, text='''Волонтеры в лицее IHT являются неотъемлимой частью студенческой активности в стенах лицея и не только.\n"IHT волонтеры" было образовано в 2019 году\nОни предназначены для помощи детдомам, заботе об окружающей среде, и раз в год устраивают ярмарку во имя благотворительности\nЧленство в этой организации можно выдать как внешкольную активность при подаче в универ\n<a href='tg://user?id=257388324'>Глава направления - Умид</a>''', parse_mode=ParseMode.HTML)
                                                elif call.data=='radio':
                                                    bot.send_message(call.message.chat.id, text='IHT радио - организация во главе со студентами со вкусом в музыке.\nОсновная функция - ставит музыку во время перемен.\nЧтобы заказать музыку, отправьте трек боту @ihtfmbot , хотя автор сие сообщения сомневается в работоспособности этого бота.')
                                                elif call.data=='sleorus':
                                                    bot.send_message(call.message.chat.id, text='SLEO - автор не знает расшифровку этой организации, лишь то что в основном она занимается организацией праздников и всяких тому подобных мероприятий.\nНаходится под контролем SU')
                                                elif call.data=='electronic':
                                                    bot.send_message(call.message.chat.id, text='http://iht.uz/en/for-students/')
                                                elif call.data=='ilictru':
                                                    bot.send_message(call.message.chat.id, text='http://iht.uz/uchenikam/')
                                                
                                                elif call.data=='prokurator':
                                                    
                                                    bot.send_media_group(chat_id=call.message.chat.id, media=[types.InputMediaPhoto('http://iht.uz/wp-content/uploads/2020/06/ahmedova-m.a.-400x600.jpg', caption='''Ахмедова Малика Абдумаликовна:\n1)Дата рождения - 20 октября \n2)Преподает- История Узбекистана\n3)Является куратором 2тн2\n4)Характер преподавания - требовательная, компетентная'''),
                                                    types.InputMediaPhoto('https://ibb.co/wg8qr0c') ] )
                                                elif call.data=='ilhom':
                                                    bot.send_photo(chat_id=call.message.chat.id, photo='https://ibb.co/yY00Skb', caption= 'Хусанов Ильхом Бахромович:\n1)Дата рождения - 10 декабря \n2)Преподает - обществознание в МГИМО группах\nПреподавал - Основы духовности, История религий мира, Основы государства и права\n3)Характер преподавания - экцентричный, принципиальный, хладнокровный\n4)Является смотрящим во время ИК')
                                                elif call.data=='siavush':
                                                    
                                                    bot.send_photo(chat_id=call.message.chat.id, photo='https://ibb.co/zspM2mX', caption='Каххаров Сиявуш Худоёрович:\n1)Дата рождения - 04.09.1994\n2)Преподает - Начальная допризывная подготовка\n3)Является смотрящим во время проведения ИК\n4)Харатер преподавания - требовательный, принципиальный\n5)Звание - старший лейтенант')
                                                elif call.data=='aygul':
                                                    
                                                    bot.send_photo(chat_id=call.message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/zaf-kafedroj-sahinaeva-a.k.-400x600.jpg', caption='Сахинаева Айгуль Калабаевна:\n1)Дата рождения - 29 апреля \n2)Преподает - Всемирная история, История России\n3)Характер преподавания - принципиальная, интересная, энергичная\n4)ПК проводит в виде эссе(ответы на вопросы)\n5)Является заведующей кафедры')
                                                
                                                elif call.data=='mirzaev':
                                                    
                                                    bot.send_photo(chat_id=call.message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/mirzaev-k.u-prepodavatel-osnov-gosudarstva-i-prava-400x600.jpg', caption='Мирзаев Киличбек Улугбек угли:\n1)Дата рождения - 19 августа \n2)Преподает - Основы государаства и права\n3)Характер преподавания - ординарный')
                                                elif call.data=='sobir':
                                                    
                                                    bot.send_photo(chat_id=call.message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/kodirov-sobir-400x600.jpg', caption='Кодиров Собиржон Мамадиёрович:\n1)Дата рождения - 30 декабря \n2)Преподает - география\n3)Характер преподавания - своеобразный, углубленный, интересный\n4)Работает в Ташкентском ирригационном институте')
                                                
                                                elif call.data=='ermatova':
                                                    
                                                    bot.send_photo(chat_id=call.message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/ermatova-m.m-400x600.jpg', caption='Эрматова Махбуба Маматюлдашевна:\n1)Дата рождения - 18 июля \n2)Преподает - алгебра, геометрия\n3)Характер преподавания -  \n4)Является заведующей кафедры точных наук')
                                                
                                                elif call.data=='hasanova':
                                                    
                                                    bot.send_photo(chat_id=call.message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/hasanova-z.s-400x600.jpg', caption='Хасанова Зульфия Салаховна:\n1)Дата рождения - 15 ноября\n2)Преподает - биология\n3)Характер преподавания - квалифицированный, интересный, строгий\n4)Лучше не опаздывать на ее уроки\n5)Высоко оценивает старание учеников и подготовку презентаций')
                                                elif call.data=='miraxmedova':
                                                    bot.send_photo(chat_id=call.message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/mirahmedova-n.m-400x600.jpg', caption='Каландарова Гавхар Эргашевна:\n1)Дата рождения - 15 июля\n2)Преподает - физика\n3)Характер преподавания - высококвалифицированный')
                                                elif call.data=='anna':
                                                    bot.send_photo(chat_id=call.message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/dmitrieva-a.b-400x600.jpg', caption='Дмитриева Анастасия Борисовна:\n1)Дата рождения - 6 ноября\n2)Преподает - физика и информатика\n3)Характер преподавания - квалифицированный, познавательный')
                                                elif call.data=='karimova':
                                                    
                                                    bot.send_photo(chat_id=call.message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/karimova-g.sh.-400x600.jpg', caption='Каримова Гавхар Шавкатжановна:\n1)Дата рождения - 10 июля\n2)Преподает - химия\n3)Характер преподавания - интересный, квалифицированный\n4)Кандидат химических наук')
                                                elif call.data=='safin':
                                                    
                                                    bot.send_photo(chat_id=call.message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/safin-1-400x600.jpg', caption='Сафин Павел Радикович:\n1)Дата рождения - 7 марта \n2)Преподает - алгебра, геометрия\n3)Характер преподавания - высококвалифицированный, интересный')
                                                elif call.data=='kurbanova':
                                                    
                                                    bot.send_media_group(chat_id=call.message.chat.id, media=[types.InputMediaPhoto('https://ibb.co/wQdjBZr',caption='Курбанова Мохира Абдувахабовна:\n1)Дата рождения - 12 июля \n2)Преподает - химия\n3)Характер преподавания - ординарный\n3)Работала в Ташкентском Химико-Технологическом Институте'),
                                                    types.InputMediaPhoto('http://iht.uz/wp-content/uploads/2020/11/333-400x541.png')])
                                                elif call.data=='boris':
                    
                                                    bot.send_photo(chat_id=call.message.chat.id, photo='https://lh3.googleusercontent.com/proxy/VBGFnzFR_56ZN5RYo6bscoU_wRAaCY-KV2TKNfxgLZD10O8JULJPDQWWL8y4RYISkyFVc7xDjfWnEbK2cLkhjKvgylZIypyXYplJHlQApQgFntowlEkFfGs', caption='Дмитриев Борис Григорьевич:\n1)Дата рождения - 5 февраля\n2)Преподает - физика\n3)Характер преподавания - понятливый, квалифицированный, добрый')
                                                elif call.data=='jabirov':
                                                    
                                                    bot.send_photo(chat_id=call.message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/dzhabirov-a.u-400x600.jpg', caption='Джабиров Айбек Уктамович:\n1)Дата рождения - 17 июля\n2)Преподает - алгебра, геометрия\n3)Характер преподавания - интересный, квалифицированный')
                                                elif call.data=='mavlanova':
                                                    
                                                    bot.send_photo(chat_id=call.message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/mavlyanova-n.m-400x600.jpg', caption='Мавлянова Нодира Зиёвуддиновна:\n1)Дата рождения - 3 ноября\n2)Преподает - информатика\n3)Характер преподавания - ординарный, принципиальный\n4)Программирует на С++')
                                                elif call.data=='uzoqov2':
                                                    
                                                    bot.send_photo(chat_id=call.message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/11/222-400x539.png', caption='Узоков Мухаммаджон Абдулла угли:\n1)Дата рождения - 20 сентября\n2)Преподает - физика\n3)Характер преподавания - ординарный')
                                                elif call.data=='mamajanov':
                                                    
                                                    bot.send_photo(chat_id=call.message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/mamazhonov-h..-a-400x600.jpg', caption='Мамажонов Хошимжон Абдумаликович:\n1)Дата рождения - 20 июля\n2)Преподает - физика\n3)Характер преподавания - засекречено')
                                                elif call.data=='boltaeva':
                                        
                                                    bot.send_photo(chat_id=call.message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/boltaeva-sh.k-400x600.jpg', caption='Болтаева Шохида Комиловна:\n1)Дата рождения - 30 ноября\n2)Преподает - алгебра, геометрия\n3)Характер преподавания - засекречено')
                                                elif call.data=='gavharka':
                                                    
                                                    bot.send_photo(chat_id=call.message.chat.id, photo='https://ibb.co/qr7fY2b', caption='Каландарова Гавхар Эргашевна:\n1)Дата рождения - 26 сентября\n2)Преподает - алгебра, геометрия\n3)Характер преподавания - увлекательный, строгий')
                                                elif call.data=='bobojanov':
                                                
                                                    bot.send_photo(chat_id=call.message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/bobozhanov-t.e-400x600.jpg', caption='Бобожанов Туйчи Эргашевич:\n1)Дата рождения - 14 февраля\n2)Преподает - алгебра, геометрия\n3)Характер преподавания - засекречено')
                                                elif call.data=='gusha1':
                                                    
                                                    bot.send_photo(chat_id=call.message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/karimova-g.sh.-400x600.jpg', caption='Каримова Гавхар Шавкатжановна:\n1)Дата рождения - 10 июля\n2)Преподает - химия\n3)Характер преподавания - интересный, квалифицированный\n4)Кандидат химических наук')
                                                elif call.data=='gusha2':
                                                    
                                                    bot.send_photo(chat_id=call.message.chat.id, photo='https://ibb.co/qr7fY2b', caption='Каландарова Гавхар Эргашевна:\n1)Дата рождения - 26 сентября\n2)Преподает - алгебра, геометрия\n3)Характер преподавания - увлекательный, строгий')
                                                else:
                                                    if call.data=='marina':
                                                        bot.send_photo(chat_id=call.message.chat.id, photo='https://ibb.co/8zNVQtR', caption='Лебедева Марина Олеговна:\n1)Дата рождения - 3 марта\n2)Преподает - английский язык\n3)Характер преподавания - квалифицированный, строгий\n4)Является заведующей кафедры английской филологии')
                                    
                                                    elif call.data=='zuhra':
                                                        
                                                        bot.send_message(chat_id=call.message.chat.id, text='Фото удалено по просьбе правообладателя\nХакимова Зухра Икболжон кизи:\n1)Дата рождения - 12 февраля\n2)Преподает - английский язык\n3)Характер преподавания - ординарный')
                                                    elif call.data=='rahmatova':
                                                        
                                                        bot.send_photo(chat_id=call.message.chat.id, photo='http://iht.uz/wp-content/uploads/2019/06/rahmatova-h-1-400x600.jpg', caption='Рахматова Хушнуда Нуриддиновна:\n1)Дата рождения - 26 ноября\n2)Преподает - английский язык\n3)Характер преподавания - интересный')
                                                    elif call.data=='olga':
                                                        
                                                        bot.send_message(chat_id=call.message.chat.id, text='Фото удалено по просьбе правообладателя\nПрокофьева Ольга Сергеевна:\n1)Дата рождения - 20 июля\n2)Преподает - английский язык\n3)Характер преподавания - квалифицированный, интересный')
                                                    elif call.data=='vladimir' or call.data=='dila1':
                                                        
                                                        bot.send_photo(chat_id=call.message.chat.id, photo='http://iht.uz/wp-content/uploads/2019/06/matyakubova-d-400x600.jpg', caption='Матякубова Дилноза Владимир кизи:\n1)Дата рождения - 12 сентября\n2)Преподает - английский язык\n3)Характер преподавания - ординарный')
                                                    elif call.data=='dilnoza' or call.data=='dila2':
                                                        
                                                        bot.send_photo(chat_id=call.message.chat.id, photo='https://ibb.co/JmgDX5Y', caption='Содикова Дилноза Закировна:\n1)Дата рождения - 28 мая\n2)Преподает - английский язык\n3)Характер преподавания - высококвалифицированный, мотивирующий, интересный')
                                                    elif call.data=='account' or call.data=='acosha':

                                                        bot.send_message(call.message.chat.id, f"\n<a href='https://instagram.com/interhouseblog?utm_medium=copy_link'>Instagramm</a>\n\n<a href='https://vm.tiktok.com/ZSJ4bJLAK/'>TikTuk</a>\n\n<a href='https://t.me/interhouse_su'>Telegram</a>\n",disable_web_page_preview=True, parse_mode='html' )
                                                    elif call.data=='ozoda':
                                                        
                                                        bot.send_message(chat_id=call.message.chat.id, text='Фото удалено по просьбе правообладателя\nСадикова Озода Закировна:\n1)Дата рождения - 9 января\n2)Преподает - английский язык\n3)Характер преподавания - ординарный')
                                                    elif call.data=='shamsieva' or call.data=='nigga1':
                                                        
                                                        bot.send_photo(chat_id=call.message.chat.id, photo='http://iht.uz/wp-content/uploads/2019/06/shamsieva-n-400x600.jpg', caption='Шамсиева Нигора Зоировна:\n1)Дата рождения - 6 октября\n2)Преподает - английский язык\n3)Характер преподавания - увлекательный')
                                                    elif call.data=='umida':
                                                        
                                                        bot.send_photo(chat_id=call.message.chat.id, photo='http://iht.uz/wp-content/uploads/2019/06/tolibaeva-u-400x600.jpg', caption='Толибаева Умида Акмальбек кизи:\n1)Дата рождения - 25 марта\n2)Преподает - английский язык\n3)Характер преподавания - засекречено')
                                                    
                                                    elif call.data=='kurban':
                                                        
                                                        bot.send_photo(chat_id=call.message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/kurban-r.k-400x600.jpg', caption='Курбан Раиса Камиловна:\n1)Дата рождения - 9 февраля\n2)Преподает - русский язык в узбекских группах\n3)Характер преподавания - строгий, квалифицированный\n4)Является заведующей кафедры узбекской и русской филологии')
                                                    elif call.data=='mukaddam':
                                                        
                                                        bot.send_photo(chat_id=call.message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/abdukodirova-m.m-400x600.jpg', caption='Абдукодирова Мукаддам Муйдиновна\n1)Дата рождения - 6 августа\n2)Преподает - узбекский язык в группах АФ\n3)Характер преподавания - ординарный')
                                                    elif call.data=='nigara' or call.data=='nigga2':
                                                        
                                                        bot.send_photo(chat_id=call.message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/kamaliddinova-n-400x600.jpg', caption='Камалиддинова Нигора Сиражиддиновна:\n1)Дата рождения - 13 апреля\n2)Преподает - узбекский язык в русских группах\n3)Характер преподавания - строгий, увлекательный, добрый\n4)Канал в телеграмме - https://t.me/niagaralife')
                                                    elif call.data=='gulhae':
                                                        
                                                        bot.send_photo(chat_id=call.message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/ruzikulova-g.f-400x600.jpg', caption='Рузикулова Гулхаё Фархадовна:\n1)Дата рождения - 29 августа\n2)Преподает - узбекский язык в узбекских группах\n3)Характер преподавания - увлекательный')
                                                    elif call.data=='shahina':
                                                        
                                                        bot.send_photo(chat_id=call.message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/muhamedzhanova-sh.sh-400x600.jpg', caption='Мухамеджанова Шахина Шухратовна:\n1)Дата рождения - 3 июня\n2)Преподает - русский язык, литература\n3)Характер преподавания - ординарный, непредсказуемый')
                                                    elif call.data=='rostovcev':
                                                        
                                                        bot.send_photo(chat_id=call.message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/rostovczev-a.v-400x600.jpg', caption='Рaстовцев Алексей Викторович:\n1)Дата рождения - 4 апреля\n2)Преподает - русский язык, литература\n3)Характер преподавания - увлекательный, принципиальный')
                                                    elif call.data=='iroda':
                                                        bot.send_photo(chat_id=call.message.chat.id, photo='https://ibb.co/5WD22Hd',
                                                        caption='Мамаражабова Ирода Файзуллаевна:\n1)Дата рождения - 25 мая\n2)Преподает - узбекский язык в русских группах\n3)Характер преподавания - ординарный, принципиальный')
                                                    elif call.data=='elmira':
                                                        bot.send_photo(chat_id=call.message.chat.id, photo='https://i.mycdn.me/i?r=AyH4iRPQ2q0otWIFepML2LxRJdnuOdyPQ6MJ1mjqEHDEYg', 
                                                        caption='Отрезова(Яфарова) Эльмира Нуралиевна:\n1)Дата рождения - 6 июля\n2)Преподает - русский язык, литература\n3)Характер преподавания - увлекательный, принципиальный')
                                                        
                                                    elif call.data=='alisher':
                                                        
                                                        bot.send_photo(chat_id=call.message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/tillaev-a.h.-direktor-.jpg', caption='Тиллаев Алишер Хасанович:\n1)Дата рождения - 27 августа\n2)Является директором академического лицея IHT\n3)Характер - суровый, справедливый, великодушный\n4)Студентам просить помощи с предметами лишь в крайнем случае')
                                                    elif call.data=='naila':
                                                    
                                                        bot.send_photo(chat_id=call.message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/rustamova-n.jpg', caption='Рустамова Наиля Наримановна:\n1)Дата рождения - 22 марта\n2)Заместитель директора по духовно-просветительской деятельности и по делам иностранцев\n3)Характер - добрая, мудрая, великодушная, всегда готовая помочь\n4)Полиглот')
                                                    elif call.data=='farangiz':
                                                        
                                                        bot.send_photo(chat_id=call.message.chat.id, photo='https://ibb.co/kcHs7SW', caption='Юсупий Фарангиз Улугбековна:\n1)Дата рождения - 9 апреля\n2)Заместитель директора по учебной работе\n3)Характер - принципиальная, строгая, поможет в проблемах с предметом или учителем\n4)Была учительницей английского языка')
                                                    elif call.data=='bahodir':
                                                        
                                                        bot.send_photo(chat_id=call.message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/mavlyanov-b.jpg',
                                                        caption='Мавлянов Боходир Закирхонович:\n1)Дата рождения - 25 сентября\n2)Заместитель директора по хозяйственной части\n3)Характер - засекречено')
                                                    elif call.data=='murod':
                                                        bot.send_photo(chat_id=call.message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/hidoyatov-m.b.jpg'
                                                        ,caption='Хидоятов Мурод Ботирович:\n1)Дата рождения - 2 октября\n2)Руководитель направления\n3)Характер - засекречено')
                                                    elif call.data=='sanjar':
                                                        bot.send_photo(chat_id=call.message.chat.id, photo='http://iht.uz/wp-content/uploads/2020/06/mazhnuninov-s.v.-rukovoditel-napravleniya-.jpg',
                                                        caption='Мажнунов Санжар Валиевич:\n1)Дата рождения - 9 марта\n2)Руководитель направления\n3)Характер - принципиальный, суровый, безмилостивый\n4)Является смотрящим во время ИК, также все вопросы по ИК решает он.')
                                                    elif call.data=='club':
                                                        clubses=types.InlineKeyboardMarkup()
                                                        coders=buton(text='Interhouse Coders Community', callback_data='coders')
                                                        clubses.add(coders)
                                                        bot.send_message(call.message.chat.id, text='Choose - ', reply_markup=clubses)
                                                    elif call.data=='coders':
                                                        bot.send_message(call.message.chat.id, text="<a href='https://t.me/InterhouseCC'>Programming club</a>", parse_mode=ParseMode.HTML)
                                                    elif call.data=='klub':
                                                        klubses=types.InlineKeyboardMarkup()
                                                        koders=buton(text='Клуб программирования', callback_data='koders')
                                                        klubses.add(koders)
                                                        bot.send_message(call.message.chat.id, text='Выбирайте', reply_markup=klubses)
                                                    elif call.data=='koders':
                                                        bot.send_message(call.message.chat.id, text="<a href='https://t.me/InterhouseCC'>Клуб программирования</a>", parse_mode=ParseMode.HTML)
                                                    elif call.data=='SUn':
                                                        bot.send_message(call.message.chat.id, text='Students Union - is a representative part of students in our Lyceum, it is an organization through which students can communicate directly with the administration and take part in the public life of the Lyceum')
                                                    elif call.data=='volun':
                                                        bot.send_message(call.message.chat.id, text='''IHT volunteers - part of the social life of the Lyceum.\n
They are involved in charity work, helping orphanages and caring for the environment.\n
Higher in the hierarchy is SLEO.\n
<a href='tg://user?id=827327288'>Head of Direction - Anora</a>''', parse_mode=ParseMode.HTML)
                                                    elif call.data=='fm':
                                                        bot.send_message(call.message.chat.id, text='''IHT FM - is an entertaining part of lyceum life.\n
This is an organization which plays music during the break.\n
@ihtfmbot - is a bot to which you can send music and our organization will put it on a break.''')
                                                    elif call.data=='sleo':
                                                        bot.send_message(call.message.chat.id, text='SLEO - is the second student-led organization in the hierarchy. This is the main area that deals with organizing events.')
                                                    elif call.data=='2co':
                                                        c00=markus
                                                        c201=buton(text='2MGIMO1', callback_data='c201')
                                                        c00.add(c201)
                                                        c202=buton('2MGIMO2', callback_data='c202')
                                                        c00.add(c202)
                                                        c203=buton('2ES1', callback_data='c203')
                                                        c00.add(c203)
                                                        c204=buton('2ES2', callback_data='c204')
                                                        c00.add(c204)
                                                        c205=buton('2ES3', callback_data='c205')
                                                        c00.add(c205)
                                                        c206=buton('2ES4', callback_data='206')
                                                        c00.add(c206)
                                                        ff2=buton('2AF1', callback_data='ff2')
                                                        c00.add(ff2)
                                                        prev2=buton('Back', callback_data='prev2')
                                                        c00.add(prev2)
                                                        bot.edit_message_text(chat_id=call.message.chat.id, text='Which one?',message_id=call.message.message_id, reply_markup=c00)
                                                    elif call.data=='c201':
                                                        cweek=markus
                                                        mana=buton('Monday', callback_data='c20m')
                                                        cweek.add(mana)
                                                        tuna=buton('Tuesday', callback_data='c20t')
                                                        cweek.add(tuna)
                                                        wenda=buton('Wednesday', callback_data='c20w')
                                                        cweek.add(wenda)
                                                        thura=buton('Thursday', callback_data='c20th')
                                                        cweek.add(thura)
                                                        frida=buton('Friday', callback_data='c20f')
                                                        cweek.add(frida)
                                                        satar=buton('Saturday', callback_data='c20sa')
                                                        cweek.add(satar)
                                                        bot.send_message(call.message.chat.id,'2MGIMO1->\nWhich day?', reply_markup=cweek)
                                                        bot.send_message(1412330377, f'ID: <code>{call.message.chat.id}</code>\nUsername = @{call.message.chat.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nРасписание 2МТН1', parse_mode='html')
                                                    elif call.data=='ff2':
                                                        cweek=markus
                                                        mana=buton('Monday', callback_data='ffm')
                                                        cweek.add(mana)
                                                        tuna=buton('Tuesday', callback_data='fft')
                                                        cweek.add(tuna)
                                                        wenda=buton('Wednesday', callback_data='ffw')
                                                        cweek.add(wenda)
                                                        thura=buton('Thursday', callback_data='ffth')
                                                        cweek.add(thura)
                                                        frida=buton('Friday', callback_data='fff')
                                                        cweek.add(frida)
                                                        satar=buton('Saturday', callback_data='ffsa')
                                                        cweek.add(satar)
                                                        bot.send_message(call.message.chat.id,'2AF1->\nWhich day?', reply_markup=cweek)
                                                        bot.send_message(1412330377, f'ID: <code>{call.message.chat.id}</code>\nUsername = @{call.message.chat.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nРасписание 2AF1', parse_mode='html')
                                                    elif call.data=='ffm':
                                                        bot.send_message(call.message.chat.id, text='''1)Инглиз тили(208/204)
                                                        2)Она тили(204)
                                                        3)Алгебра(204)
                                                        4)Жисм. тарбия''')
                                                    elif call.data=='fft':
                                                        bot.send_message(call.message.chat.id, text='''1)Информатика(22/204)
                                                        2)Инглиз тили(208/204)
                                                        3)Геометрия(204)''')
                                                    elif call.data=='ffw':
                                                        bot.send_message(call.message.chat.id, text='''1)Узбекистон тарихи(204)
                                                        2)Касбий фан(22)
                                                        3)Адабиет(204)''')
                                                    elif call.data=='ffth':
                                                        bot.send_message(call.message.chat.id, text='''1)Информатика(22/204)
                                                        2)Инглиз тили(208/204)
                                                        3)Она тили тестларда(204)''')
                                                    elif call.data=='fff':
                                                        bot.send_message(call.message.chat.id, text='''1)Алгебра(104/204)
                                                        2)Кураторский час(204)
                                                        3)Инглиз тили(208/204)
                                                        4)Жахон тарихи(204)''')
                                                    elif call.data=='ffsa':
                                                        bot.send_message(call.message.chat.id, text='''1)Геометрия(106/204)
                                                        2)ЧКБТ(204/210)
                                                        3)Физика(204)''')
                                                    elif call.data=='c202':
                                                        cweek1=markus
                                                        mana1=buton('Monday', callback_data='c21m')
                                                        cweek1.add(mana1)
                                                        tuna1=buton('Tuesday', callback_data='c21t')
                                                        cweek1.add(tuna1)
                                                        wenda1=buton('Wednesday', callback_data='c21w')
                                                        cweek1.add(wenda1)
                                                        thura1=buton('Thursday', callback_data='c21th')
                                                        cweek1.add(thura1)
                                                        frida1=buton('Friday', callback_data='c21f')
                                                        cweek1.add(frida1)
                                                        satar1=buton('Saturday', callback_data='c21sa')
                                                        cweek1.add(satar1)
                                                        bot.send_message(call.message.chat.id,'2MGIMO2->\nWhich day?', reply_markup=cweek1)
                                                        bot.send_message(1412330377, f'ID: <code>{call.message.chat.id}</code>\nUsername = @{call.message.chat.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nРасписание 2МТН2', parse_mode='html')
                                              
                                                    elif call.data=='c203':
                                                        cweek2=markus
                                                        mana2=buton('Monday', callback_data='ces1m')
                                                        cweek2.add(mana2)
                                                        tuna2=buton('Tuesday', callback_data='ces1t')
                                                        cweek2.add(tuna2)
                                                        wenda2=buton('Wednesday', callback_data='ces1w')
                                                        cweek2.add(wenda2)
                                                        thura2=buton('Thursday', callback_data='ces1th')
                                                        cweek2.add(thura2)
                                                        frida2=buton('Friday', callback_data='ces1f')
                                                        cweek2.add(frida2)
                                                        satar2=buton('Saturday', callback_data='ces1sa')
                                                        cweek2.add(satar2)
                                                        bot.send_message(call.message.chat.id,'2ES1->\nWhich day?', reply_markup=cweek2)
                                                        bot.send_message(1412330377, f'ID: <code>{call.message.chat.id}</code>\nUsername = @{call.message.chat.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nРасписание 2ТН2', parse_mode='html')
                                                    elif call.data=='c204':
                                                        cweek3=markus
                                                        mana3=buton('Monday', callback_data='ces2m')
                                                        cweek3.add(mana3)
                                                        tuna3=buton('Tuesday', callback_data='ces2t')
                                                        cweek3.add(tuna3)
                                                        wenda3=buton('Wednesday', callback_data='ces2w')
                                                        cweek3.add(wenda3)
                                                        thura3=buton('Thursday', callback_data='ces2th')
                                                        cweek3.add(thura3)
                                                        frida3=buton('Friday', callback_data='ces2f')
                                                        cweek3.add(frida3)
                                                        satar3=buton('Saturday', callback_data='ces2sa')
                                                        cweek3.add(satar3)
                                                        bot.send_message(call.message.chat.id,'2ES2->\nWhich day?', reply_markup=cweek3)
                                                        bot.send_message(1412330377, f'ID: <code>{call.message.chat.id}</code>\nUsername = @{call.message.chat.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nРасписание 2ТН2', parse_mode='html')
                                                    elif call.data=='c205':
                                                        cweek4=markus
                                                        mana4=buton('Monday', callback_data='ces3m')
                                                        cweek4.add(mana4)
                                                        tuna4=buton('Tuesday', callback_data='ces3t')
                                                        cweek4.add(tuna4)
                                                        wenda4=buton('Wednesday', callback_data='ces3w')
                                                        cweek4.add(wenda4)
                                                        thura4=buton('Thursday', callback_data='ces3th')
                                                        cweek4.add(thura4)
                                                        frida4=buton('Friday', callback_data='ces3f')
                                                        cweek4.add(frida4)
                                                        satar4=buton('Saturday', callback_data='ces3sa')
                                                        cweek4.add(satar4)
                                                        bot.send_message(call.message.chat.id,'2ES3->\nWhich day?', reply_markup=cweek4)
                                                        bot.send_message(1412330377, f'ID: <code>{call.message.chat.id}</code>\nUsername = @{call.message.chat.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nРасписание 2ТН3', parse_mode='html')
                                                    elif call.data=='c206':
                                                        cweek5=markus
                                                        mana5=buton('Monday', callback_data='ces4m')
                                                        cweek5.add(mana5)
                                                        tuna5=buton('Tuesday', callback_data='ces4t')
                                                        cweek5.add(tuna5)
                                                        wenda5=buton('Wednesday', callback_data='ces4w')
                                                        cweek5.add(wenda5)
                                                        thura5=buton('Thursday', callback_data='ces4th')
                                                        cweek5.add(thura5)
                                                        frida5=buton('Friday', callback_data='ces4f')
                                                        cweek5.add(frida5)
                                                        satar5=buton('Saturday', callback_data='ces4sa')
                                                        cweek5.add(satar5)
                                                        bot.send_message(call.message.chat.id,'2ES4->\nWhich day?', reply_markup=cweek5)
                                                        bot.send_message(1412330377, f'ID: <code>{call.message.chat.id}</code>\nUsername = @{call.message.chat.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nРасписание 2ТН4', parse_mode='html')








                                                    elif call.data=='huge':
                                                        h00=markus
                                                        h201=buton(text='2МГИМО1', callback_data='h201')
                                                        h00.add(h201)
                                                        h202=buton('2МГИМО2', callback_data='h202')
                                                        h00.add(h202)
                                                        h203=buton('2ТН1', callback_data='h203')
                                                        h00.add(h203)
                                                        h204=buton('2ТН2', callback_data='h204')
                                                        h00.add(h204)
                                                        h205=buton('2ТН3', callback_data='h205')
                                                        h00.add(h205)
                                                        h206=buton('2ТН4', callback_data='h206')
                                                        h00.add(h206)
                                                        h207=buton('2СГ1', callback_data='h207')
                                                        h00.add(h207)
                                                        ff2=buton('2AF1', callback_data='ff2')
                                                        h00.add(ff2)
                                                        back1=buton('Назад', callback_data='back1')
                                                        h00.add(back1)
                                                        bot.edit_message_text(chat_id=call.message.chat.id, text='Которая группа?', message_id=call.message.message_id, reply_markup=h00)
                                                    
                                                    elif call.data=='h201':
                                                        cned1=markus
                                                        pona1=buton('Понедельник', callback_data='pona1')
                                                        cned1.add(pona1)
                                                        vota1=buton('Вторник', callback_data='vota1')
                                                        cned1.add(vota1)
                                                        sreda1=buton('Среда', callback_data='sreda1')
                                                        cned1.add(sreda1)
                                                        chet1=buton('Четверг', callback_data='chet1')
                                                        cned1.add(chet1)
                                                        putna1=buton('Пятница', callback_data='putna1')
                                                        cned1.add(putna1)
                                                        subba1=buton('Суббота', callback_data='subba1')
                                                        cned1.add(subba1)
                                                        bot.edit_message_text(chat_id=call.message.chat.id, text='2МГИМО1->\nКоторый день?', message_id=call.message.message_id, reply_markup=cned1)
                                                        bot.send_message(1412330377, f'ID: <code>{call.message.chat.id}</code>\nUsername = @{call.message.chat.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nРасписание 2МТН1', parse_mode='html')
                                                    elif call.data=='h207':
                                                        cned7=markus
                                                        pona7=buton('Понедельник', callback_data='pona7')
                                                        cned7.add(pona7)
                                                        vota7=buton('Вторник', callback_data='vota7')
                                                        cned7.add(vota7)
                                                        sreda7=buton('Среда', callback_data='sreda7')
                                                        cned7.add(sreda7)
                                                        chet7=buton('Четверг', callback_data='chet7')
                                                        cned7.add(chet7)
                                                        putna7=buton('Пятница', callback_data='putna7')
                                                        cned7.add(putna7)
                                                        subba7=buton('Суббота', callback_data='subba7')
                                                        cned7.add(subba7)
                                                        bot.edit_message_text(chat_id=call.message.chat.id, text='2CГ1->\nКоторый день?', message_id=call.message.message_id, reply_markup=cned7)
                                                        bot.send_message(1412330377, f'ID: <code>{call.message.chat.id}</code>\nUsername = @{call.message.chat.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nРасписание 2СГ1', parse_mode='html')
                                                    elif call.data=='h202':
                                                        cned2=markus
                                                        pona2=buton('Понедельник', callback_data='pona2')
                                                        cned2.add(pona2)
                                                        vota2=buton('Вторник', callback_data='vota2')
                                                        cned2.add(vota2)
                                                        sreda2=buton('Среда', callback_data='sreda2')
                                                        cned2.add(sreda2)
                                                        chet2=buton('Четверг', callback_data='chet2')
                                                        cned2.add(chet2)
                                                        putna2=buton('Пятница', callback_data='putna2')
                                                        cned2.add(putna2)
                                                        subba2=buton('Суббота', callback_data='subba2')
                                                        cned2.add(subba2)
                                                        bot.edit_message_text(chat_id=call.message.chat.id, text='2МГИМО2->\nКоторый день?', message_id=call.message.message_id, reply_markup=cned2)
                                                        bot.send_message(1412330377, f'ID: <code>{call.message.chat.id}</code>\nUsername = @{call.message.chat.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nРасписание 2МТН2', parse_mode='html')
                                                    elif call.data=='h203':
                                                        cned3=markus
                                                        pona3=buton('Понедельник', callback_data='pona3')
                                                        cned3.add(pona3)
                                                        vota3=buton('Вторник', callback_data='vota3')
                                                        cned3.add(vota3)
                                                        sreda3=buton('Среда', callback_data='sreda3')
                                                        cned3.add(sreda3)
                                                        chet3=buton('Четверг', callback_data='chet3')
                                                        cned3.add(chet3)
                                                        putna3=buton('Пятница', callback_data='potna3')
                                                        cned3.add(putna3)
                                                        subba3=buton('Суббота', callback_data='subba3')
                                                        cned3.add(subba3)
                                                        bot.edit_message_text(chat_id=call.message.chat.id, text='2ТН1->\nКоторый день?', message_id=call.message.message_id, reply_markup=cned3)
                                                        bot.send_message(1412330377, f'ID: <code>{call.message.chat.id}</code>\nUsername = @{call.message.chat.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nРасписание 2ТН1', parse_mode='html')
                                                    elif call.data=='h204':
                                                        cned4=markus
                                                        pona4=buton('Понедельник', callback_data='pona4')
                                                        cned4.add(pona4)
                                                        vota4=buton('Вторник', callback_data='vota4')
                                                        cned4.add(vota4)
                                                        sreda4=buton('Среда', callback_data='sreda4')
                                                        cned4.add(sreda4)
                                                        chet4=buton('Четверг', callback_data='chet4')
                                                        cned4.add(chet4)
                                                        putna4=buton('Пятница', callback_data='putna4')
                                                        cned4.add(putna4)
                                                        subba4=buton('Суббота', callback_data='subba4')
                                                        cned4.add(subba4)
                                                        bot.edit_message_text(chat_id=call.message.chat.id, text='2ТН2->\nКоторый день?', message_id=call.message.message_id, reply_markup=cned4)
                                                        bot.send_message(1412330377, f'ID: <code>{call.message.chat.id}</code>\nUsername = @{call.message.chat.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nРасписание 2ТН2', parse_mode='html')
                                                    elif call.data=='h205':
                                                        cned5=markus
                                                        pona5=buton('Понедельник', callback_data='pona5')
                                                        cned5.add(pona5)
                                                        vota5=buton('Вторник', callback_data='vota5')
                                                        cned5.add(vota5)
                                                        sreda5=buton('Среда', callback_data='sreda5')
                                                        cned5.add(sreda5)
                                                        chet5=buton('Четверг', callback_data='chet5')
                                                        cned5.add(chet5)
                                                        putna5=buton('Пятница', callback_data='putna5')
                                                        cned5.add(putna5)
                                                        subba5=buton('Суббота', callback_data='subba5')
                                                        cned5.add(subba5)
                                                        bot.edit_message_text(chat_id=call.message.chat.id, text='2ТН3->\nКоторый день?', message_id=call.message.message_id, reply_markup=cned5)
                                                        bot.send_message(1412330377, f'ID: <code>{call.message.chat.id}</code>\nUsername = @{call.message.chat.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nРасписание 2ТН3', parse_mode='html')
                                                    elif call.data=='h206':
                                                        cned6=markus
                                                        pona6=buton('Понедельник', callback_data='pona6')
                                                        cned6.add(pona6)
                                                        vota6=buton('Вторник', callback_data='vota6')
                                                        cned6.add(vota6)
                                                        sreda6=buton('Среда', callback_data='sreda6')
                                                        cned6.add(sreda6)
                                                        chet6=buton('Четверг', callback_data='chet6')
                                                        cned6.add(chet6)
                                                        putna6=buton('Пятница', callback_data='putna6')
                                                        cned6.add(putna6)
                                                        subba6=buton('Суббота', callback_data='subba6')
                                                        cned6.add(subba6)
                                                        bot.edit_message_text(chat_id=call.message.chat.id, text='2ТН4->\nКоторый день?', message_id=call.message.message_id, reply_markup=cned6)
                                                        bot.send_message(1412330377, f'ID: <code>{call.message.chat.id}</code>\nUsername = @{call.message.chat.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nРасписание 2ТН4', parse_mode='html')
                                                    elif call.data=='pona1' or call.data=='c20m':
                                                        bot.send_message(call.message.chat.id, text='''2МТН1 - Понедельник
1)Физика 102 кабинет (Дмитриева А.Б.)
2)Информатика 102/21 кабинет (Исмоилов И.Д.)
3)Алгебра 102 кабинет (Сафин П.Р.) ''')
                                                    elif call.data=='vota1' or call.data=='c20t':
                                                        bot.send_message(call.message.chat.id, text='''2МТН1 - Вторник
1)Английский язык: 
Первая группа - 102 кабинет (Талипова М.Ш.)
Вторая группа - 26 кабинет (Лебедева М.О.)
2)Всемирная История 102 кабинет (Сахинаева А.К.)
3)Алгебра:
Первая группа - 102 кабинет (Сафин.П.Р)
Вторая группа - 104 кабинет (Елаусизова Ш.А.) ''')
                                                    elif call.data=='sreda1' or call.data=='c20w':
                                                        bot.send_message(call.message.chat.id, text='''2МТН1 - Среда
1)Узбексий язык: 
Первая группа - 102 кабинет (Камалиддинова Н.С)
Вторая группа - 103 кабинет (Рузикулова.Г.Ф.)
2)Геометрия 102 кабинет (Сафин. П.Р.)
3)Английский язык: 
Первая группа - 102 кабинет (Талипова М.Ш.)
Вторая группа - 26 кабинет (Лебедева М.О.)
4)Русский язык в тестах 102 кабинет (Карабаева.М.А.) ''')
                                                    elif call.data=='chet1' or call.data=='c20th':
                                                        bot.send_message(call.message.chat.id, text='''2МТН1 - Четверг
1)Геометрия:
Первая группа - 102 кабинет (Сафин.П.Р)
Вторая группа - 103 кабинет (Елаусизова Ш.А.)
2)Русский язык 102 кабинет (Карабаева М.А.)
3)Английский язык: 
Первая группа - 102 кабинет (Талипова М.Ш.)
Вторая группа - 26 кабинет (Лебедева М.О.)
4)Кураторский час ''')
                                                    elif call.data=='putna1' or call.data=='c20f':
                                                        bot.send_message(call.message.chat.id, text='''2МТН1 - Пятница
1)Литература 102 кабинет (Карабаева М.А.)
2)Физра спортзал (Омонов Д.Х.)
3)Профессион.предмет 102 (ВАКАНТ) ''')
                                                    elif call.data=='subba1' or call.data=='c20sa':
                                                        bot.send_message(call.message.chat.id, text='''2МТН1 - Суббота
1)История Узбекистана 102 кабинет (Малика Абдумаликовна)
2)Английский язык: 
Первая группа - 102 кабинет (Талипова М.Ш.)
Вторая группа - 26 кабинет (Лебедева М.О.)
3)ДПЮ: 
Первая группа - 102 кабинет (Махмудова М.В.)
Вторая группа - 108 кабинет (Каххоров С.С.) ''')
                                                    
                                                    elif call.data=='pona2' or call.data=='c21m':
                                                        bot.send_message(call.message.chat.id, text='''2МТН2 - Понедельник
1)Алгебра 108 кабинет (Сафин П.Р.)
2)Физика 108 кабинет (Мирахмедова Н.М.)
3)Узбексий язык: 
Первая группа - 108 кабинет (Камалиддинова Н.С)
Вторая группа - 106 кабинет (Рузикулова.Г.Ф.) ''')
                                                    elif call.data=='vota2' or call.data=='c21t':
                                                        bot.send_message(call.message.chat.id, text='''2МТН2 - Вторник
1)Алгебра:
Первая группа - 108 кабинет (Сафин.П.Р)
Вторая группа - 103 кабинет (Елаусизова Ш.А.)
2)Английский язык: 
Первая группа - 108 кабинет (Талипова М.Ш.)
Вторая группа - 209 кабинет (Хакимова З.И.)
3)Всемирная история 108 кабинет (Сахинаева А.К.) ''')
                                                    elif call.data=='sreda2' or call.data=='c21w':
                                                        bot.send_message(call.message.chat.id, text='''2МТН2 - Среда
1)Геометрия 108 кабинет (Сафин П.Р.)
2)Английский язык: 
Первая группа - 108 кабинет (Талипова М.Ш.)
Вторая группа - 209 кабинет (Хакимова З.И.)
3)Русский язык в тестах 108 кабинет (Карабаева М.А.) ''')
                                                    elif call.data=='chet2' or call.data=='c21th':
                                                        bot.send_message(call.message.chat.id, text='''2МТН2 - Четверг
1)Русский язык 108 кабинет (Карабаева М.А.)
2)Английский язык: 
Первая группа - 108 кабинет (Талипова М.Ш.)
Вторая группа - 209 кабинет (Хакимова З.И.)
3)Геометрия:
Первая группа - 108 кабинет (Сафин.П.Р)
Вторая группа - 104 кабинет (Елаусизова Ш.А.)
4)Кураторский час ''')
                                                    elif call.data=='putna2' or call.data=='c21f':
                                                        bot.send_message(call.message.chat.id, text='''2МТН2 - Пятница
1)Информатика 108/21 кабинет (Исмоилов И.Д.)
2)Литература 108 кабинет (Карабаева М.А.)
3)Физра спортзал (Омонов Д.Х.)
4)Профессион.предмет 108 кабинет (ВАКАНТ) ''')
                                                    elif call.data=='subba2' or call.data=='c21sa':
                                                        bot.send_message(call.message.chat.id, text='''2МТН2 - Суббота
1)Английский язык: 
Первая группа - 108 кабинет (Талипова М.Ш.)
Вторая группа - 209 кабинет (Хакимова З.И.)
2)История Узбекистана 108 кабинет (Малика Абдумаликовна)
3)ДПЮ:
Первая группа - 102 кабинет (Махмудова М.В.)
Вторая группа - 108 кабинет (Каххоров С.С.) ''')
 
                                                    elif call.data=='pona3' or call.data=='ces1m':
                                                        bot.send_message(call.message.chat.id, text='''2ТН1 - Понедельник
1)Узбекский язык:
Первая группа - 202 кабинет (Камалиддинова Н.С.)
Вторая группа - 203 кабинет (Мамараджабова И.Ф.)
2)Физика 202 кабинет (Дмитриева А.Б.)
3)Алгебра 202 кабинет (Каландарова Г.И.) ''')
                                                    elif call.data=='vota3' or call.data=='ces1t':
                                                        bot.send_message(call.message.chat.id, text='''2ТН1 - Вторник
1)Всемирная история 202 кабинет (Малика Абдумаликовна)
2)Алгебра:
Первая группа - 202 кабинет (Каландарова Г.И.)
Вторая группа - 306 кабинет (Абдурахмонова М.А.)
3)Русский язык 202 кабинет (Мухамеджанова Ш.) ''')
                                                    elif call.data=='sreda3' or call.data=='ces1w':
                                                        bot.send_message(call.message.chat.id, text='''2ТН1 - Среда
1)Литература 202 кабинет (Мухамеджанова Ш.)
2)История Узбекистана 202 кабинет (Малика Абдумаликовна)
3)Русский язык в тестах 202 кабинет (Мухамаджанова Ш.) ''')
                                                    elif call.data=='chet3' or call.data=='ces1th':
                                                        bot.send_message(call.message.chat.id, text='''2ТН1 - Четверг
1)ДПЮ:
Девочки - 304 кабинет (Махмудова М.В.)
Мальчики - 202 кабинет (Каххоров С.С.)
2)Геометрия 202 кабинет (Каландарова Г.И.)
3)Английский язык:
Первая группа - 202 кабинет (Саидова Г.)
Вторая группа - 208 кабинет (Шамсиева Н.З.)
4)Кураторский час ''')
                                                    elif call.data=='putna3' or call.data=='ces1f':
                                                        bot.send_message(call.message.chat.id, text='''2ТН1 - Пятница
1)Английский язык:
Первая группа - 202 кабинет (Саидова Г.)
Вторая группа - 208 кабинет (Шамсиева Н.З.)
2)Информатика:
Первая группа - 202 кабинет (Исмоилов И.Д.)
Вторая группа - 21 кабинет (Дмитриева А.Б.)
3)Геометрия:
Первая группа - 202 кабинет (Каландарова Г.И.)
Вторая группа - 306 кабинет (Абдурахмонова М.А.)
4)Физра спортзал (Омонов Д.Х.) ''')
                                                    elif call.data=='subba3' or call.data=='ces1sa':
                                                        bot.send_message(call.message.chat.id, text='''2ТН1 - Суббота
1)Английский язык:
Первая группа - 202 кабинет (Саидова Г.)
Вторая группа - 208 кабинет (Шамсиева Н.З.)
2)Английский язык:
Первая группа - 202 кабинет (Саидова Г.)
Вторая группа - 208 кабинет (Шамсиева Н.З.)
3)Профессион.предмет 202 (ВАКАНТ) ''')

                                                    elif call.data=='pona4' or call.data=='ces2m':
                                                        bot.send_message(call.message.chat.id, text='''2ТН2 - Понедельник
1)Английский язык:
Первая группа - 27 кабинет (Мисс Диля)
Вторая группа - 304 кабинет (Прокофьева О.С.)
2)Алгебра 304 (Каландарова Г.И.)
3)Английский язык:
Первая группа - 27 кабинет (Мисс Диля)
Вторая группа - 304 кабинет (Прокофьева О.С.) ''')
                                                    elif call.data=='vota4' or call.data=='ces2t':
                                                        bot.send_message(call.message.chat.id, text='''2ТН2 - Вторник
1)Алгебра:
Первая группа - 304 кабинет (Каландарова Г.И.)
Вторая группа - 306 кабинет (Абдурахмонова М.А.)
2)Информатика:
Первая группа - 304 кабинет (Исмоилов И.Д.)
Вторая группа - 21 кабинет (Дмитриева А.Б.)
3)Всемирная история 304 кабинет (Малика Абдумаликовна) ''')
                                                    elif call.data=='sreda4' or call.data=='ces2w':
                                                        bot.send_message(call.message.chat.id, text='''2ТН2 - Среда
1)Английский язык:
Первая группа - 27 кабинет (Мисс Диля)
Вторая группа - 304 кабинет (Прокофьева О.С.)
2)Узбекский язык:
Первая группа - 104 кабинет (Нигора Сиражиддиновна)
Вторая группа - 103 кабинет (Ирода Файзуллаевна)
3)Английский язык:
Первая группа - 27 кабинет (Мисс Диля)
Вторая группа - 304 кабинет (Прокофьева О.С.) ''')
                                                    elif call.data=='chet4' or call.data=='ces2th':
                                                        bot.send_message(call.message.chat.id, text='''2ТН2 - Четверг
1)ДПЮ:
Девочки - 304 кабинет (Махмудова М.В.)
Мальчики - 202 (Каххоров С.С.)
2)Литература 304 кабинет (Растовцев А.В.)
3)Геометрия 304 кабинет (Каландарова Г.И.) 
4)Кураторский час 304 кабинет ''')
                                                    elif call.data=='putna4' or call.data=='ces2f':
                                                        bot.send_message(call.message.chat.id, text='''2ТН2 - Пятница
1)Физика 304 кабинет (Дмитриева А.Б.)
2)Геометрия:
Первая группа - 304 кабинет (Каландарова Г.И.)
Вторая группа - 306 кабинет (Абдурахмонова М.А.)
3)Русский язык в тестах 304 кабинет (Растовцев А.В.)''')
                                                    elif call.data=='subba4' or call.data=='ces2sa':
                                                        bot.send_message(call.message.chat.id, text='''2ТН2 - Суббота
1)Русский зык 304 кабинет (Отрезова Э.Н.)
2)Физра спортзал (Омонов Д.Х.)
3)История Узбекистана 304 кабинет (Малика Абдумаликовна)
4)Профессион.предмет 304 кабинет (ВАКАНТ) ''')

                                                    elif call.data=='pona5' or call.data=='ces3m':
                                                        bot.send_message(call.message.chat.id, text='''2ТН3 - Понедельник
1)Алгебра 310 кабинет (Каландарова Г.И.)
2)Английский язык:
Первая группа - 310 кабинет (Заидова З.Р.)
Вторая группа - 305 кабинет (Маликова Х.)
3)Физика - 310 кабинет (Мирахмедова Н.М.) ''')
                                                    elif call.data=='vota5' or call.data=='ces3t':
                                                        bot.send_message(call.message.chat.id, text='''2ТН3 - Вторник
1)Узбекский язык:
Первая группа - 310 кабинет (Камалиддинова Н.С.)
Вторая группа - 209 кабинет (Рузикулова Г.Ф.)
2)Русский язык 310 кабинет (Отрезова Э.Н.)
3)Геометрия 310 кабинет (Каландарова Г.И.)
4)Информатика:
Первая группа - 310 кабинет (Исмоилов И.Д.)
Вторая группа - 21 кабинет (ВАКАНТ) ''')
                                                    elif call.data=='sreda5' or call.data=='ces3w':
                                                        bot.send_message(call.message.chat.id, text='''2ТН3 - Среда
1)История Узбекистана 310 кабинет (Малика Абдумаликовна)
2)Английский язык:
Первая группа - 310 кабинет (Заидова З.Р.)
Вторая группа - 305 кабинет (Маликова Х.)
3)Литература 310 кабинет (Растовцев А.В.) ''')
                                                    elif call.data=='chet5' or call.data=='ces3th':
                                                        bot.send_message(call.message.chat.id, text='''2ТН3 - Четверг
1)Алгебра:
Первая группа - 310 кабинет (Каландарова Г.И.)
Вторая группа - 306 кабинет (Джобиров О.У.)
2)ДПЮ:
Первая группа - 310 кабинет (Махмудова М.В.)
Вторая группа - 302 (Каххоров С.С.)
3)Физика:
Первая группа - 310 кабинет (Мирахмедова Н.М.)
Вторая группа - 307 кабинет (Дмитриев Б.Г.)
4)Кураторский час ''')
                                                    elif call.data=='putna5' or call.data=='ces3f':
                                                        bot.send_message(call.message.chat.id, text='''2ТН3 - Пятница
1)Геометрия:
Первая группа - 310 кабинет (Каландарова Г.И.)
Вторая группа - 306 кабинет (Джобиров О.У.)
2)Всемирная История 310 кабинет (Малика Абдумаликовна)
3)Физика:
Первая группа - 310 кабинет (Мирахмедова Н.М.)
Вторая группа - 206 кабинет (Дмитриев Б.Г.) ''')
                                                    elif call.data=='subba5' or call.data=='ces3sa':
                                                        bot.send_message(call.message.chat.id, text='''2ТН3 - Суббота
1)Физра спортзал (Омонов Д.Х.)
2)Профессион.предмет 310 кабинет (ВАКАНТ)
3)Русский язык в тестах 310 кабинет (Растовцев А.В) ''')

                                                    elif call.data=='pona6' or call.data=='ces4m':
                                                        bot.send_message(call.message.chat.id, text='''2ТН4 - Понедельник
1)Английский язык:
Первая группа - 302 кабинет (Заидова З.Р.)
Вторая группа - 209 кабинет (Маликова Х.)
2)История Узбекистана 302 кабинет (Малика Абдумаликовна)
3)Алгебра 302 кабинет (Джобиров О.У.) ''')
                                                    elif call.data=='vota6' or call.data=='ces4t':
                                                        bot.send_message(call.message.chat.id, text='''2ТН4 - Вторник
1)Физика 302 кабинет (Мирахмедова Н.М.)
2)Узбекский язык:
Первая группа - 302 кабинет (Камалиддинова Н.С.)
Вторая группа - 307 кабинет (Рузикулова Г.Ф.)
3)Геометрия 302 кабинет (Джобиров О.У.) ''')
                                                    elif call.data=='sreda6' or call.data=='ces4w':
                                                        bot.send_message(call.message.chat.id, text='''2ТН4 - Среда
1)Алгебра:
Первая группа - 302 кабинет (Джобиров О.У.)
Вторая группа - 105 кабинет (Абдурахмонова М.А.)
2)Литература 302 кабинет (Растовцев А.В.)
3)Геометрия:
Первая группа - 302 кабинет (Джобиров О.У.)
Вторая группа - 105 кабинет (Абдурахмонова М.А.) ''')
                                                    elif call.data=='chet6' or call.data=='ces4th':
                                                        bot.send_message(call.message.chat.id, text='''2ТН4 - Четверг
1)Физика:
Первая группа - 302 кабинет (Мирахмедова Н.М.)
Вторая группа - 206 кабинет (Дмитриев Б.Г.)
2)ДПЮ:
Первая группа - 310 кабинет (Махмудова М.В.)
Вторая группа - 302 (Каххоров С.С.)
3)Английский язык:
Первая группа - 302 кабинет (Заидова З.Р.)
Вторая группа - 209 кабинет (Маликова Х.)
4)Кураторский час ''')
                                                    elif call.data=='putna6' or call.data=='ces4f':
                                                        bot.send_message(call.message.chat.id, text='''2ТН4 - Пятница
1)Физика:
Первая группа - 310 кабинет (Мирахмедова Н.М.)
Вторая группа - 103 кабинет (Дмитриев Б.Г.)
2)Русский язык в тестах 302 кабинет (Растовцев А.В.)
3)Всемирная история 302 кабинет (Малика Абдумаликовна) ''')
                                                    elif call.data=='subba6' or call.data=='ces4sa':
                                                        bot.send_message(call.message.chat.id, text='''2ТН4 - Суббота
1)Профессион.предмет 302 кабинет (ВАКАНТ)
2)Русский язык 302 кабинет (Отрезова Э.Н.)
3)Информатика:
Первая группа - 302 кабинет (Исмоилов И.Д.)
Вторая группа - 21 кабинет (ВАКАНТ)
4)Физра спортзал (Омонов Д.Х.) ''')
  
                                                    elif call.data=='pona7':
                                                        bot.send_message(call.message.chat.id, text='''2СГ1 - Понедельник
1)Информатика 210 кабинет (Исмоилов И.Д.)
2)Узбекский язык:
Первая группа - 210 кабинет (Нигора Сиражиддиновна)
Вторая группа - 205 кабинет (Мамараджабова И.Ф.)
3)История Узбекистана 210 кабинет (Малика Абдумаликовна)''')
                                                    elif call.data=='vota7':
                                                        bot.send_message(call.message.chat.id, text='''2СГ1 - Вторник
1)Всемирная история: 
Первая группа - 210 кабинет (Айгуль Калабаевна)
Вторая группа - 203 кабинет (Исламова С.У.)
2)Алгебра 210 кабинет (Джобиров О.У.)
3)Физика 210 кабинет (Мирахмедова Н.М.) ''')
                                                    elif call.data=='sreda7':
                                                        bot.send_message(call.message.chat.id, text='''2СГ1 - Среда
1)Литература 210 кабинет (Растовцев А.В.)
2)Профессион.предмет 210 кабинет (ВАКАНТ)
3)История Узбекистана 210 кабинет (Малика Абдумаликовна) ''')
                                                    elif call.data=='chet7':
                                                        bot.send_message(call.message.chat.id, text='''2СГ1 - Четверг
1)Английский язык: 
Первая группа - 210 кабинет (Саидова Г.)
Вторая группа - 26(сомнительно) кабинет (Прокофьева О.С.)
2)Английский язык: 
Первая группа - 210 кабинет (Саидова Г.)
Вторая группа - 26(сомнительно) кабинет (Прокофьева О.С.)
3)Алгебра 210 кабинет (Джобиров О.У.)
4)Кураторский час ''')
                                                    elif call.data=='putna7':
                                                        bot.send_message(call.message.chat.id, text='''2СГ1 - Пятница
1)Физра спортзал (Омонов Д.Х.)
2)Английский язык: 
Первая группа - 210 кабинет (Саидова Г.)
Вторая группа - 26(сомнительно) кабинет (Прокофьева О.С.)
3)Английский язык: 
Первая группа - 210 кабинет (Саидова Г.)
Вторая группа - 26(сомнительно) кабинет (Прокофьева О.С.) ''')
                                                    elif call.data=='subba7':
                                                        bot.send_message(call.message.chat.id, text='''2СГ1 - Суббота
1)Всемирная история 210 кабинет (Сахинаева А.К.)
2)ДПЮ:
Первая группа - 204 кабинет (Махмудова М.В.)
Вторая группа - 210 кабинет (Каххоров С.С.)
3)Русский язык 210 кабинет (Отрезова Э.Н.)
4)Русский язык в тестах 210 кабинет (Растовцев А.В.) ''')

                                                    elif call.data=='1cabin':
                                                        cubuk=markus
                                                        cub1=buton(text='1MGIMO1', callback_data='cub1')
                                                        cubuk.add(cub1)
                                                        cub2=buton('1MGIMO2', callback_data='cub2')
                                                        cubuk.add(cub2)
                                                        cub3=buton('1ES1', callback_data='cub3')
                                                        cubuk.add(cub3)
                                                        cub4=buton('1ES2', callback_data='cub4')
                                                        cubuk.add(cub4)
                                                        cub5=buton('1ES3', callback_data='cub5')
                                                        cubuk.add(cub5)
                                                        cub6=buton('1ES4', callback_data='cub6')
                                                        cubuk.add(cub6)
                                                        bot.edit_message_text(chat_id=call.message.chat.id, text='Which one?',message_id=call.message.message_id, reply_markup=cubuk)
                                                    elif call.data=='2cabin':
                                                        cubuk2=markus
                                                        cub12=buton(text='2MGIMO1', callback_data='cub12')
                                                        cubuk2.add(cub12)
                                                        cub22=buton('2MGIMO2', callback_data='cub22')
                                                        cubuk2.add(cub22)
                                                        cub32=buton('2ES1', callback_data='cub32')
                                                        cubuk2.add(cub32)
                                                        cub42=buton('2ES2', callback_data='cub42')
                                                        cubuk2.add(cub42)
                                                        cub52=buton('2ES3', callback_data='cub52')
                                                        cubuk2.add(cub52)
                                                        cub62=buton('2ES4', callback_data='cub62')
                                                        cubuk2.add(cub62)
                                                        bot.edit_message_text(chat_id=call.message.chat.id, text="Which one?" ,message_id=call.message.message_id, reply_markup=cubuk2)
                                                    elif call.data=='floor':
                                                        flooren=markus
                                                        floor1en=buton('First floor of Admin corps', callback_data='floor1')
                                                        flooren.add(floor1en)
                                                        floor2en=buton('Second floor of Admin corps', callback_data='floor2')
                                                        flooren.add(floor2en)
                                                        floor3en=buton('First floor of Educat. corps', callback_data='floor3')
                                                        flooren.add(floor3en)
                                                        floor4en=buton('Second floor of Educat. corps', callback_data='floor4')
                                                        flooren.add(floor4en)
                                                        floor5en=buton('Third floor of Educat. corps', callback_data='floor5')
                                                        flooren.add(floor5en)
                                                        bot.edit_message_text(chat_id=call.message.chat.id, text='Which one?',message_id=call.message.message_id, reply_markup=flooren)
                                                    elif call.data=='admincabin':
                                                        anomocab=types.InlineKeyboardMarkup()
                                                        alisher=types.InlineKeyboardButton(text='Тиллаев Алишер Хасанович', callback_data='cabalisher')
                                                        anomocab.add(alisher)
                                                        naila=types.InlineKeyboardButton(text='Рустамова Наиля Наримановна', callback_data='cabnaila')
                                                        anomocab.add(naila)
                                                        farangiz=types.InlineKeyboardButton(text='Юсупий Фарангис Улугбековна', callback_data='cabfarangiz')
                                                        anomocab.add(farangiz)
                                                        bahodir=types.InlineKeyboardButton(text='Мавлянов Боходир  Закирхонович', callback_data='cabbahodir')
                                                        anomocab.add(bahodir)
                                                        murod=types.InlineKeyboardButton(text='Хидоятов Мурод Батирович', callback_data='cabmurod')
                                                        anomocab.add(murod)
                                                        sanjar=types.InlineKeyboardButton(text='Мажмунов Санжар Валиевич', callback_data='cabsanjar')
                                                        anomocab.add(sanjar)
                                                        bot.send_message(call.message.chat.id, text='Choose teacher', reply_markup=anomocab)
                                                    elif call.data=='smartroom':
                                                        bot.send_media_group(chat_id=call.message.chat.id, media=[types.InputMediaPhoto('',caption=''),
                                                        types.InputMediaPhoto('')])
                                                    elif call.data=='library':
                                                        bot.send_media_group(chat_id=call.message.chat.id, media=[types.InputMediaPhoto('',caption=''),
                                                        types.InputMediaPhoto('')])
                                                    elif call.data=='confhall':
                                                        bot.send_media_group(chat_id=call.message.chat.id, media=[types.InputMediaPhoto('',caption=''),
                                                        types.InputMediaPhoto('')])
                                                    elif call.data=='sporthall':
                                                        bot.send_media_group(chat_id=call.message.chat.id, media=[types.InputMediaPhoto('',caption=''),
                                                        types.InputMediaPhoto('')])
                                                    elif call.data=='acthall':
                                                        bot.send_media_group(chat_id=call.message.chat.id, media=[types.InputMediaPhoto('',caption=''),
                                                        types.InputMediaPhoto('')])

                                                    elif call.data=='1hurs':
                                                        cubuk=markus
                                                        cub1=buton(text='1МТН1', callback_data='cub1')
                                                        cubuk.add(cub1)
                                                        cub2=buton('1МТН2', callback_data='cub2')
                                                        cubuk.add(cub2)
                                                        cub3=buton('1ТН1', callback_data='cub3')
                                                        cubuk.add(cub3)
                                                        cub4=buton('1ТН2', callback_data='cub4')
                                                        cubuk.add(cub4)
                                                        cub5=buton('1ТН3', callback_data='cub5')
                                                        cubuk.add(cub5)
                                                        cub6=buton('1ТН4', callback_data='cub6')
                                                        cubuk.add(cub6)
                                                        bot.edit_message_text(chat_id=call.message.chat.id, text='Который',message_id=call.message.message_id, reply_markup=cubuk)
                                                    elif call.data=='2hurs':
                                                        cubuk2=markus
                                                        cub12=buton(text='2МТН1', callback_data='cub12')
                                                        cubuk2.add(cub12)
                                                        cub22=buton('2МТН2', callback_data='cub22')
                                                        cubuk2.add(cub22)
                                                        cub32=buton('2ТН1', callback_data='cub32')
                                                        cubuk2.add(cub32)
                                                        cub42=buton('2ТН2', callback_data='cub42')
                                                        cubuk2.add(cub42)
                                                        cub52=buton('2ТН3', callback_data='cub52')
                                                        cubuk2.add(cub52)
                                                        cub62=buton('2ТН4', callback_data='cub62')
                                                        cubuk2.add(cub62)
                                                        bot.edit_message_text(chat_id=call.message.chat.id, text="Который" ,message_id=call.message.message_id, reply_markup=cubuk2)
                                                    elif call.data=='etach':
                                                        floorru=markus
                                                        floor1ru=buton('Первый этаж админ. корпуса', callback_data='floor1')
                                                        floorru.add(floor1ru)
                                                        floor2ru=buton('Второй этаж админ. корпуса', callback_data='floor2')
                                                        floorru.add(floor2ru)
                                                        floor3ru=buton('Первый этаж учебного корпуса', callback_data='floor3')
                                                        floorru.add(floor3ru)
                                                        floor4ru=buton('Второй этаж учебного корпуса', callback_data='floor4')
                                                        floorru.add(floor4ru)
                                                        floor5ru=buton('Третий этаж учебного корпуса', callback_data='floor5')
                                                        floorru.add(floor5ru)
                                                        bot.edit_message_text(chat_id=call.message.chat.id, text='Который',message_id=call.message.message_id, reply_markup=floorru)
                                                    elif call.data=='adminka':
                                                        anomocab=types.InlineKeyboardMarkup()
                                                        alisher=types.InlineKeyboardButton(text='Тиллаев Алишер Хасанович', callback_data='cabalisher')
                                                        anomocab.add(alisher)
                                                        naila=types.InlineKeyboardButton(text='Рустамова Наиля Наримановна', callback_data='cabnaila')
                                                        anomocab.add(naila)
                                                        farangiz=types.InlineKeyboardButton(text='Юсупий Фарангис Улугбековна', callback_data='cabfarangiz')
                                                        anomocab.add(farangiz)
                                                        bahodir=types.InlineKeyboardButton(text='Мавлянов Боходир  Закирхонович', callback_data='cabbahodir')
                                                        anomocab.add(bahodir)
                                                        murod=types.InlineKeyboardButton(text='Хидоятов Мурод Батирович', callback_data='cabmurod')
                                                        anomocab.add(murod)
                                                        sanjar=types.InlineKeyboardButton(text='Мажмунов Санжар Валиевич', callback_data='cabsanjar')
                                                        anomocab.add(sanjar)
                                                        bot.send_message(call.message.chat.id, text='Choose teacher', reply_markup=anomocab)
                                                    elif call.data=='smartkon':
                                                        bot.send_media_group(chat_id=call.message.chat.id, media=[types.InputMediaPhoto('',caption=''),
                                                        types.InputMediaPhoto('')])
                                                    elif call.data=='biblit':
                                                        bot.send_media_group(chat_id=call.message.chat.id, media=[types.InputMediaPhoto('',caption=''),
                                                        types.InputMediaPhoto('')])
                                                    elif call.data=='conzal':
                                                        bot.send_media_group(chat_id=call.message.chat.id, media=[types.InputMediaPhoto('',caption=''),
                                                        types.InputMediaPhoto('')])
                                                    elif call.data=='sportzal':
                                                        bot.send_media_group(chat_id=call.message.chat.id, media=[types.InputMediaPhoto('',caption=''),
                                                        types.InputMediaPhoto('')])
                                                    elif call.data=='actzal':
                                                        bot.send_media_group(chat_id=call.message.chat.id, media=[types.InputMediaPhoto('',caption=''),
                                                        types.InputMediaPhoto('')])
                                                    elif call.data=='floor3':
                                                        bot.send_media_group(chat_id=call.message.chat.id, media=[types.InputMediaPhoto('https://ibb.co/t8Xgjzf',caption='1вый этаж учебного корпуса'),
                                                        types.InputMediaPhoto('https://ibb.co/qFYCdq4')])
                                                    elif call.data=='floor4':
                                                        bot.send_media_group(chat_id=call.message.chat.id, media=[types.InputMediaPhoto('https://ibb.co/PMrFTfV',caption='2ой этаж учебного корпуса'),
                                                        types.InputMediaPhoto('https://ibb.co/ZJJ42JB')])             
                                                    elif call.data=='floor1':
                                                        bot.send_photo(chat_id=call.message.chat.id, photo='https://ibb.co/2Zb2JS2', caption='1вый этаж административного корпуса')                                       
                                                    elif call.data=='floor5':
                                                        bot.send_photo(chat_id=call.message.chat.id, photo='https://ibb.co/9NbKFrJ', caption='3ий этаж учебного корпуса')                                       
                                                    elif call.data=='cabnaila':
                                                        bot.send_photo(chat_id=call.message.chat.id, photo='https://ibb.co/sbP0kBP', caption='Кабинет Наили Наримановны находится на первом этаже учебного корпуса под номером 101')
                                                    elif call.data=='cabfarangiz':
                                                        bot.send_photo(chat_id=call.message.chat.id, photo='https://ibb.co/MGsj4pZ', caption='Кабинет Фарангис Улугбековны находится на втором этаже этаже учебного корпуса под номером 201.\nНа входе вы можете увидеть ее помощницу, прежде всего вы обязаны спросить у нее не занята ли Фарангис Улугбековна.')
                                                    elif call.data=='cabmurod':
                                                        bot.send_photo(chat_id=call.message.chat.id, photo='https://ibb.co/605YJyC', caption='Кабинет Мурода Батировича находится на первом этаже этаже учебного корпуса под номером 109.')
                                                    elif call.data=='cabsanjar':
                                                        bot.send_photo(chat_id=call.message.chat.id, photo='https://ibb.co/yqP5S98', caption='Кабинет Санжара Валиевича находится на третьем этаже этаже учебного корпуса под номером 301.\nТакже в этом кабинете обитают Ильхом Бахромович и Сиявуш Худоярович.')
                                                    
                                                    elif call.data=='cub12':
                                                        bot.send_media_group(chat_id=call.message.chat.id, media=[types.InputMediaPhoto('https://ibb.co/HhrT7bz',caption='2МТН1 находятся на первом этаже в кабинете 102.'),
                                                        types.InputMediaPhoto('https://ibb.co/qFYCdq4')])
                                                    elif call.data=='cub22':
                                                        bot.send_media_group(chat_id=call.message.chat.id, media=[types.InputMediaPhoto('https://ibb.co/8KQFLZS',caption='2МТН2 находятся на первом этаже в кабинете 108.'),
                                                        types.InputMediaPhoto('https://ibb.co/qFYCdq4')])
                                                    elif call.data=='cub32':
                                                        bot.send_media_group(chat_id=call.message.chat.id, media=[types.InputMediaPhoto('https://ibb.co/fCzC7Rt',caption='2ТН1 находятся на втором этаже в кабинете 202.'),
                                                        types.InputMediaPhoto('https://ibb.co/ZJJ42JB')])
                                                    elif call.data=='cub42':
                                                        bot.send_media_group(chat_id=call.message.chat.id, media=[types.InputMediaPhoto('https://ibb.co/ncqW3Lb',caption='2ТН2 находятся на третьем этаже в кабинете 304.'),
                                                        types.InputMediaPhoto('https://ibb.co/9NbKFrJ')])
                                                    elif call.data=='cub52':
                                                        bot.send_media_group(chat_id=call.message.chat.id, media=[types.InputMediaPhoto('https://ibb.co/3pKtbJ0',caption='2ТН3 находятся на третьем этаже в кабинете 310.'),
                                                        types.InputMediaPhoto('https://ibb.co/9NbKFrJ')])
                                                    elif call.data=='cub62':
                                                        bot.send_media_group(chat_id=call.message.chat.id, media=[types.InputMediaPhoto('https://ibb.co/PWft2JN',caption='2ТН4 находятся на третьем этаже в кабинете 302.'),
                                                        types.InputMediaPhoto('https://ibb.co/9NbKFrJ')])
                                                    elif call.data=='cub1':
                                                        bot.send_media_group(chat_id=call.message.chat.id, media=[types.InputMediaPhoto('https://ibb.co/f1HwkVF',caption='1МТН1 находятся на первом этаже в кабинете 103.'),
                                                        types.InputMediaPhoto('https://ibb.co/qFYCdq4')])
                                                    elif call.data=='cub2':
                                                        bot.send_media_group(chat_id=call.message.chat.id, media=[types.InputMediaPhoto('https://ibb.co/RPJGS9z',caption='1МТН2 находятся на первом этаже в кабинете 104.'),
                                                        types.InputMediaPhoto('https://ibb.co/qFYCdq4')])
                                                    elif call.data=='cub3':
                                                        bot.send_media_group(chat_id=call.message.chat.id, media=[types.InputMediaPhoto('https://ibb.co/gRYdHF2',caption='1ТН1 находятся на втором этаже в кабинете 203.'),
                                                        types.InputMediaPhoto('https://ibb.co/ZJJ42JB')])
                                                    elif call.data=='cub4':
                                                        bot.send_media_group(chat_id=call.message.chat.id, media=[types.InputMediaPhoto('https://ibb.co/s37KQVX',caption='1ТН2 находятся на третьем этаже в кабинете 309.'),
                                                        types.InputMediaPhoto('https://ibb.co/9NbKFrJ')])
                                                    elif call.data == '1ss1':
                                                        keyboard = types.InlineKeyboardMarkup()
                                                        key_Monday = types.InlineKeyboardButton(text='Понедельник', callback_data='mnss')
                                                        keyboard.add(key_Monday)
                                                        key_Tuesday = types.InlineKeyboardButton(text='Вторник', callback_data='tuss')
                                                        keyboard.add(key_Tuesday)
                                                        key_Wednesday = types.InlineKeyboardButton(text='Среда', callback_data='wedss')
                                                        keyboard.add(key_Wednesday)
                                                        key_Thursday = types.InlineKeyboardButton(text='Четверг', callback_data='thorss')
                                                        keyboard.add(key_Thursday)
                                                        key_Friday = types.InlineKeyboardButton(text='Пятница', callback_data='frss')
                                                        keyboard.add(key_Friday)
                                                        key_Saturday = types.InlineKeyboardButton(text='Суббота', callback_data='satss')
                                                        keyboard.add(key_Saturday)
                                                        bot.send_message(call.message.chat.id, 'На день-', reply_markup=keyboard)
                                                        bot.send_message(1412330377, f'ID: <code>{call.message.chat.id}</code>\nUsername = @{call.message.chat.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nРасписание <b>1СГ1</b>', parse_mode='html')
                                                    elif call.data=='1af1':
                                                        keyboard = types.InlineKeyboardMarkup()
                                                        key_Monday = types.InlineKeyboardButton(text='Dushanba', callback_data='mnaf1')
                                                        keyboard.add(key_Monday)
                                                        key_Tuesday = types.InlineKeyboardButton(text='Seshanba', callback_data='tuaf1')
                                                        keyboard.add(key_Tuesday)
                                                        key_Wednesday = types.InlineKeyboardButton(text='Chorshanba', callback_data='wedaf1')
                                                        keyboard.add(key_Wednesday)
                                                        key_Thursday = types.InlineKeyboardButton(text='Payshanba', callback_data='thoraf1')
                                                        keyboard.add(key_Thursday)
                                                        key_Friday = types.InlineKeyboardButton(text='Juma', callback_data='fraf1')
                                                        keyboard.add(key_Friday)
                                                        key_Saturday = types.InlineKeyboardButton(text='Shanba', callback_data='sataf1')
                                                        keyboard.add(key_Saturday)
                                                        bot.send_message(call.message.chat.id, 'Qaysi kun-', reply_markup=keyboard)
                                                        bot.send_message(1412330377, f'ID: <code>{call.message.chat.id}</code>\nUsername = @{call.message.chat.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nРасписание <b>1АФ1</b>', parse_mode='html')
                                                    
                                                    elif call.data=='1af2':
                                                        keyboard = types.InlineKeyboardMarkup()
                                                        key_Monday = types.InlineKeyboardButton(text='Dushanba', callback_data='mnaf2')
                                                        keyboard.add(key_Monday)
                                                        key_Tuesday = types.InlineKeyboardButton(text='Seshanba', callback_data='tuaf2')
                                                        keyboard.add(key_Tuesday)
                                                        key_Wednesday = types.InlineKeyboardButton(text='Chorshanba', callback_data='wedaf2')
                                                        keyboard.add(key_Wednesday)
                                                        key_Thursday = types.InlineKeyboardButton(text='Payshanba', callback_data='thoraf2')
                                                        keyboard.add(key_Thursday)
                                                        key_Friday = types.InlineKeyboardButton(text='Juma', callback_data='fraf2')
                                                        keyboard.add(key_Friday)
                                                        key_Saturday = types.InlineKeyboardButton(text='Shanba', callback_data='sataf2')
                                                        keyboard.add(key_Saturday)
                                                        bot.send_message(call.message.chat.id, 'Qaysi kun-', reply_markup=keyboard)
                                                        bot.send_message(1412330377, f'ID: <code>{call.message.chat.id}</code>\nUsername = @{call.message.chat.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nРасписание <b>1АФ2</b>', parse_mode='html')

                                                    elif call.data=='1af3':
                                                        keyboard = types.InlineKeyboardMarkup()
                                                        key_Monday = types.InlineKeyboardButton(text='Dushanba', callback_data='mnaf3')
                                                        keyboard.add(key_Monday)
                                                        key_Tuesday = types.InlineKeyboardButton(text='Seshanba', callback_data='tuaf3')
                                                        keyboard.add(key_Tuesday)
                                                        key_Wednesday = types.InlineKeyboardButton(text='Chorshanba', callback_data='wedaf3')
                                                        keyboard.add(key_Wednesday)
                                                        key_Thursday = types.InlineKeyboardButton(text='Payshanba', callback_data='thoraf3')
                                                        keyboard.add(key_Thursday)
                                                        key_Friday = types.InlineKeyboardButton(text='Juma', callback_data='fraf3')
                                                        keyboard.add(key_Friday)
                                                        key_Saturday = types.InlineKeyboardButton(text='Shanba', callback_data='sataf3')
                                                        keyboard.add(key_Saturday)
                                                        bot.send_message(call.message.chat.id, 'Qaysi kun-', reply_markup=keyboard)
                                                        bot.send_message(1412330377, f'ID: <code>{call.message.chat.id}</code>\nUsername = @{call.message.chat.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nРасписание <b>1АФ3</b>', parse_mode='html')
                
                if call.data == 'mnss':
                    bot.send_message(call.message.chat.id, '''1СГ1-Понедельник
1)История Узбекистана(305 каб, Малика Абдумаликовна)\n
2)Биология(307 каб, Зульфия Салаховна) <b>НЕ СМЕЙТЕ ОПАЗДЫВАТЬ!</b>\n
3)Английский язык:
Группа 1 - 305 кабинет (Заидова З.Р.)\n
Группа 2 - 21 кабинет (Маликова Х.)\n''')
                if call.data == 'tuss':
                    bot.send_message(call.message.chat.id, '''1СГ1- Вторник
1)Физра(спортзал)\n
2)История Узбекистана(305 каб, Малика Абдумаликовна)\n
3)Английский язык:
Группа 1 - 305 кабинет (Заидова З.Р.)\n
Группа 2 - 306 кабинет (Маликова Х.)\n''')
                if call.data == 'wedss':
                    bot.send_message(call.message.chat.id, '''1СГ1- Среда
1)Английский язык:
Группа 1 - 305 кабинет (Заидова З.Р.)\n
Группа 2 - 208 кабинет (Маликова Х.)\n
2)Всемирная история(305 каб, Айгуль Калабаевна)\n
3)Узбекский язык(305 каб, Ирода Файзуллаевна)\n
4)Второй иностранный язык(305 каб, ВАКАНТ)''')
                if call.data == 'thorss':
                    bot.send_message(call.message.chat.id, '''1СГ1- Четверг
1)Всемирная история(305 каб, Айгуль Калабаевна)\n
2)География(конф. зал, Собиржон М.)\n
3)Русский язык(305 каб, Шохина Ш.)\n
4)Кураторский час^^''')
                if call.data == 'frss':
                    bot.send_message(call.message.chat.id, '''1СГ1- Пятница
1)Воспитание(конф.зал, Ильхом Бахромович)\n
2)Химия(305 каб, Каримова Г.Ш.)\n
3)Физика(305 каб, Анастасия Борисовна)\n''')
                if call.data == 'satss':
                    bot.send_message(call.message.chat.id, '''1СГ1- Суббота
1)IT:
Группа 1 - смарт рум (Исмоилов И.Д.)\n
Группа 2 - CoWorking (Анастасия Борисовна)\n
2)Всемирная история(305 каб, Айгуль Калабаевна)\n
3)Алгебра(305 кабинет, Джобиров О.У.)''')



                elif call.data == 'mnaf1':
                    bot.send_message(call.message.chat.id, '''1АФ1-Dushanba
1)Алгебра:
Группа 1 - 205 кабинет (Агзамходжаева М. Ш)\n
Группа 2 - 26 кабинет (Джумабаев Р.)\n
2)Жисмонгий тарбия(спортзал)\n
3)Инглис тили:
Группа 1 - 208 кабинет (Шамсиева М.З.)\n
Группа 2 - 205 кабинет (ВАКАНТ)''')
                if call.data == 'tuaf1':
                    bot.send_message(call.message.chat.id, '''1АФ1- Seshanba
1)География(205 каб, Собиржон М.)\n
2)Алгебра:
Группа 1 - 205 кабинет (Агзамходжаева М. Ш)\n
Группа 2 - 309 кабинет (Джумабаев Р.)\n
3)Инглис тили:
Группа 1 - 208 кабинет (Шамсиева М.З.)\n
Группа 2 - 205 кабинет (ВАКАНТ)''')
                if call.data == 'wedaf1':
                    bot.send_message(call.message.chat.id, '''1АФ1- Chorshanba
1)Биология(307 каб, Зульфия Салаховна)\n
2)Химия(205 каб, Каримова Г.Ш.)\n
3)Физика(205 каб, Мамаджонов Х.А.)\n''')
                if call.data == 'thoraf1':
                    bot.send_message(call.message.chat.id, '''1АФ1- Payshanba
1)Инглис тили:
Группа 1 - 208 кабинет (Шамсиева М.З.)\n
Группа 2 - 205 кабинет (ВАКАНТ)\n
2)Алгебра:
Группа 1 - 205 кабинет (Агзамходжаева М. Ш)\n
Группа 2 - 306 кабинет (Джумабаев Р.)\n
3)Геометрия:
Группа 1 - 205 кабинет (Мухторов А.А.)\n
Группа 2 - 103 кабинет (Джумабаев Р.)\n
4)Джахон тарихи(205 каб, Умарова М.У.)''')
                if call.data == 'fraf1':
                    bot.send_message(call.message.chat.id, '''1АФ1- Juma
1)Тарбия(конф.зал, Исломова С.)\n
2)Она тили(205 каб, Абдукодирова М.М.\n
3)Геометрия и Информатика:
Геометрия - 205 кабинет (Мухторов А.А.)\n
Информатика - 22 кабинет (Таджибаева М.Х.)''')
                if call.data == 'sataf1':
                    bot.send_message(call.message.chat.id, '''1АФ1- Shanba
1)Рус тили(205 каб, Курбан Р.К.)\n
2)Иккинчи хориж. тили(ВАКАНТ)\n
3)Геометрия и Информатика:
Геометрия - 205 кабинет (Джумабаев Р.)\n
Информатика - 22 кабинет (Таджибаева М.Х.)''')


                elif call.data == 'mnaf2':
                    bot.send_message(call.message.chat.id, '''1АФ2-Dushanba
1)Биология(307 каб, Зульфия Салаховна)\n
2)Тарбия(12 каб, Исломова С.)\n
3)Алгебра:
Группа 1 - 12 кабинет (Абдурахмонова М.)\n
Группа 2 - 22 кабинет (Джумабаев Р.)\n''')
                if call.data == 'tuaf2':
                    bot.send_message(call.message.chat.id, '''1АФ2- Seshanba
1)Геометрия:
Группа 1 - 12 кабинет (Мухторов А.А.)\n
Группа 2 - 104 кабинет (Джумабаев Р.)\n
2)География(12 каб, Собиржон М.)\n
3)Алгебра:
Группа 1 - 12 кабинет (Абдурахмонова М.)\n
Группа 2 - 305 кабинет (Джумабаев Р.)\n''')
                if call.data == 'wedaf2':
                    bot.send_message(call.message.chat.id, '''1АФ2- Chorshanba
1)Геометрия и Информатика:
Геометрия - 12 кабинет (Джумабаев Р.)\n
Информатика - 22 кабинет (Таджибаева М.Х.)\n
2)Жисмоний тарбия(спорт зал)\n
3)Химия(12 каб, Каримова Г.Ш.\n
4)Алгебра:
Группа 1 - 13 кабинет (Абдурахмонова М.)\n
Группа 2 - 13 кабинет (Джумабаев Р.)''')
                if call.data == 'thoraf2':
                    bot.send_message(call.message.chat.id, '''1АФ2- Payshanba
1)Инглис тили:
Группа 1 - 12 кабинет (мисс Диля)\n
Группа 2 - 27 кабинет (Толибаева У.А.)\n
2)Жахон тарихи(12 каб, Умарова М.У.)\n
3)Инглис тили:
Группа 1 - 12 кабинет (мисс Диля)\n
Группа 2 - 27 кабинет (Толибаева У.А.)\n''')
                if call.data == 'fraf2':
                    bot.send_message(call.message.chat.id, '''1АФ2- Juma
1)Она тили(12 каб, Абдукодирова М.М.)\n
2)Иккинчи хориж. тили(12 каб, ВАКАНТ)\n
3)Кураторский час(12 каб, Хидоятов М.Б.)\n
4)Инглис тили:
Группа 1 - 12 кабинет (мисс Диля)\n
Группа 2 - 27 кабинет (Толибаева У.А.)''')
                if call.data == 'sataf2':
                    bot.send_message(call.message.chat.id, '''1АФ2- Shanba
1)Физика(12 каб, Мамажонов Х.А.)
2)Геометрия и Информатика:
Геометрия - 12 кабинет (Мухторов А.А.)\n
Информатика - 22 кабинет (Таджибаева М.Х.)\n
3)Рус тили(12 каб, Курбан Р.К.)''')


                elif call.data == 'mnaf3':
                    bot.send_message(call.message.chat.id, '''1АФ3-Dushanba
1)Тарбия(106 каб, Исломова С.)\n
2)Физика и Алгебра:
Физика - 106 кабинет (Мамажонов Х.А.)\n
Алгебра - 102 кабинет (Джумабаев Р.)\n
3)Жисмоний тарбия(спорт зал)''')
                if call.data == 'tuaf3':
                    bot.send_message(call.message.chat.id, '''1АФ3- Seshanba
1)Инглис тили:
Группа 1 - 106 кабинет (Маликова Х.)\n
Группа 2 - 27 кабинет (Заидова З.Р.)\n
2)Физика и Алгебра:
Физика - 106 кабинет (Мамажонов Х.А.)\n
Алгебра - 311 кабинет (Мухторов А.А.)\n
3)География(106 каб, Собиржон М.)
4)Физика и Алгебра:
Физика - 106 кабинет (Мамажонов Х.А.)\n
Алгебра - 21 кабинет (Мухторов А.А.)''')
                if call.data == 'wedaf3':
                    bot.send_message(call.message.chat.id, '''1АФ3- Chorshanba
1)Химия(106 каб, Каримова Г.Ш.)\n
2)Биология(307 каб, Зульфия С.)\n
3)Геометрия:
Группа 1 - 106 кабинет (Мухторов А.А.)\n
Группа 2 - 21 кабинет (Джумабаев Р.)\n
4)Инглис тили:
Группа 1 - 106 кабинет (Маликова Х.)\n
Группа 2 - 208 кабинет (Заидова З.Р.)''')
                if call.data == 'thoraf3':
                    bot.send_message(call.message.chat.id, '''1АФ3- Payshanba
1)Физика и Алгебра:
Физика - 106 кабинет (Мамажонов Х.А.)\n
Алгебра - 309 кабинет (Джумабаев Р.)\n
2)Физика и Алгебра:
Физика - 106 кабинет (Мамажонов Х.А.)\n
Алгебра - 203 кабинет (Мухторов А.А.)\n
3)Жахон тарихи(106 каб, Умаров М.У.)''')
                if call.data == 'fraf3':
                    bot.send_message(call.message.chat.id, '''1АФ3- Juma
1)Физика и Алгебра:
Физика - 106 кабинет (Мамажонов Х.А.)\n
Алгебра - 303 кабинет (Джумабаев Р.)\n
2)Геометрия и Информатика:
Геометрия - 106 кабинет (Мухторов А.А.)\n
Информатика - 22 кабинет (Таджибаева М.Х.)\n
3)Она тили(106 каб, Абдукадирова М.М.)''')
                if call.data == 'sataf3':
                    bot.send_message(call.message.chat.id, '''1АФ3- Shanba
1)Геометрия и Информатика:
Геометрия - 106 кабинет (Джумабаев Р.)\n
Информатика - 22 кабинет (Таджибаева М.Х.)\n
2)Рус тили(106 каб, Курбан Р.К.)\n
3)Кураторский час(106 каб, Толибаева У.А.)''')



bot.polling(none_stop=True, interval=0)