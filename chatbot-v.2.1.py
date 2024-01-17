from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import InputFile

bot = Bot(token='$YOUR_TG_TOKEN')
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот онлайн!')

#BODY
    #KEYBOARDS
        #НАЧАЛЬНАЯ
kb1 = InlineKeyboardMarkup(row_width=1)
b1 = InlineKeyboardButton(text='Об университете', callback_data='uni')
b2 = InlineKeyboardButton(text='Перечень документов для подачи', callback_data='docs')
b3 = InlineKeyboardButton(text='Сроки подачи документов', callback_data='sroki')
b4 = InlineKeyboardButton(text='Формы обучения', callback_data='forms')
b5 = InlineKeyboardButton(text='Специальности (образовательные программы)', callback_data='progsnew')
b6 = InlineKeyboardButton(text='Вступительные испытания', callback_data='exam')
b7 = InlineKeyboardButton(text='Даты сдачи экзаменов', callback_data='dataexam')
b8 = InlineKeyboardButton(text='Стоимость обучения', callback_data='cost')
b9 = InlineKeyboardButton(text='Наши контакты', callback_data='contacts')
b10 = InlineKeyboardButton(text='Наши соцсети', callback_data='links')
kb1.add(b1, b2, b3, b4, b5, b6, b7, b8, b9, b10)
        #ПРОГРАММЫ
kb2 = InlineKeyboardMarkup(row_width=2)
b1 = InlineKeyboardButton(text='Бизнес-информатика', callback_data='bi')
b2 = InlineKeyboardButton(text='Менеджмент', callback_data='man')
b3 = InlineKeyboardButton(text='Экономика', callback_data='econ')
b4 = InlineKeyboardButton(text='Прикладная информатика', callback_data='pi')
b5 = InlineKeyboardButton(text='Назад', callback_data='main')
kb2.add(b1, b2, b3, b4, b5)
        #ВОЗВРАТ В ПРОГРАММЫ
kb3 = InlineKeyboardMarkup(row_width=1)
b1 = InlineKeyboardButton(text='Назад', callback_data='progsnew')
kb3.add(b1)
        #ДИПЛОМ
kb4 = InlineKeyboardMarkup(row_width=1)
b1 = InlineKeyboardButton(text='Диплом', callback_data='diploma')
b2 = InlineKeyboardButton(text='Назад', callback_data='main')
kb4.add(b1, b2)
        #ВЫХОД НА ГЛАВНУЮ
kb20 = InlineKeyboardMarkup(row_width=1)
b1 = InlineKeyboardButton(text='Назад', callback_data='main')
kb20.add(b1)

    #COMMANDS
        #START
@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.answer('Здравствуйте! Вас приветствует команда Минского филиала РЭУ им. Г.В. Плеханова! Данный бот создан для получения оперативной информации о нашем филиале.\n\nДля быстрой навигации по чат-боту рекомендуем использование меню с командами в левом нижнем углу.\n\nДля продолжения выберите интересующий вас раздел:', reply_markup=kb1)
        #HELP
@dp.message_handler(commands=['help'])
async def command_start(message: types.Message):
    await message.answer('Общение с ботом реализуется при помощи кнопок, а также команд, расположенных в меню в левом нижнем углу чата.\n\nДля получения необходимой информации выберите интересующий вас раздел:', reply_markup=kb1)
        #ПРОГРАММЫ
@dp.message_handler(commands=['programms'])
async def command_start(message: types.Message):
    await message.answer('Образовательные программы Минского филиала РЭУ им. Г.В.Плеханова:\n\n(На данный момент чат-бот позволяет ознакомиться только с образовательными программами бакалавриата)', reply_markup=kb2)
        #ОБ УНИВЕРЕ
@dp.message_handler(commands=['uni'])
async def command_start(message: types.Message):
    await message.answer('<b>Российский экономический университет им. Г. В. Плеханова</b> - ведущее экономическое высшее учебное заведение Российской Федерации. РЭУ им. Г. В. Плеханова неизменно входит в <b>десятку</b> лучших университетов, традиционно входит в <b>топ-20</b> вузов, выпускники которых востребованы работодателями (Рейтинг «Топ-100 вузов России» RAEX 2022).\n\nПервый и единственный российский университет, имеющий категорию «5 звезд» в престижном международном рейтинге <b>QS Stars</b>. Всего в мире чуть более 50 вузов имеют такую категорию.\n\n<b>Минский филиал РЭУ им. Г. В. Плеханова</b> работает в Республике Беларусь с 2003г. и имеет более чем 20-летний опыт подготовки высококвалифицированных специалистов.', parse_mode='html', reply_markup=kb4)
        #КОНТАКТЫ
@dp.message_handler(commands=['contacts'])
async def command_start(message: types.Message):
    await message.answer('Наши контакты:\n\nПриёмная комиссия: (+375 44) 762 57 63\nУчебно-методический отдел: (+375 17) 244 12 91\nПриёмная директора: (+375 17) 317 45 56')
        #СОЦСЕТИ
@dp.message_handler(commands=['links'])
async def command_start(message: types.Message):
    await message.answer('Наши соцсети:\n\nInstagram: instagram.com/reu.minsk\nВконтакте: vk.com/abiturient_minskreu')

    #CALLBACKS
        #ДОКИ
@dp.callback_query_handler(text='docs')
async def docs(callback: types.CallbackQuery):
    await callback.message.answer('<b>Перечень необходимых документов для поступления:</b>\n\n1) Паспорт + копии 3х страниц\n2) Аттестат + копия аттестата\n3) Медицинская справка + выписка из амбулаторной карты)\n4) 6 фотографий (3х4)\n5) Сертификаты ЦЭ и ЦТ (по предметам для поступления)\n\nСогласие на обработку персональных данных при подаче документов заполняется законным представителем абитуриента или самим абитуриентом при достижении совершеннолетия.', reply_markup=kb20, parse_mode='html')
    await callback.answer()
        #СРОКИ ПОДАЧИ ДОКУМЕНТОВ
@dp.callback_query_handler(text='sroki')
async def sroki(callback: types.CallbackQuery):
    await callback.message.answer('<b>Сроки подачи документов:</b>\n\nс 20 июня по 10 июля - на бюджет по внутренним испытаниям (до 25 июля по результатам ЦТ/ЦЭ) для очной формы обучения\n\nс 20 июня по 25 августа - прием документов на внебюджетную форму обучения для очной, очно-заочной и заочной форм обучения', reply_markup=kb20, parse_mode='html')
    await callback.answer()
        #ФОРМЫ ОБУЧЕНИЯ
@dp.callback_query_handler(text='forms')
async def forms(callback: types.CallbackQuery):
    await callback.message.answer('Формы обучения и направления по ним:\n\n1) <b>Очная форма обучения</b> (бюджет и внебюджет): Бизнес-информатика, Менеджмент; продолжительность обучения - 4 года\n2) <b>Очно-заочная (вечерняя) форма обучения</b> (внебюджет): Бизнес-информатика, Менеджмент, Экономика; продолжительность обучения - 4,5 года\n3) <b>Заочная форма обучения</b> (внебюджет): Прикладная информатика; продолжительность обучения - 5 лет\n\nСтуденты мужского пола очно-заочной формы обучения имеют право получения отсрочки от армии так же, как и студенты очной формы обучения!', reply_markup=kb20, parse_mode='html')
    await callback.answer()
        #ОБРАЗОВАТЕЛЬНЫЕ ПРОГРАММЫ
@dp.callback_query_handler(text='progsnew')
async def progsnew(callback: types.CallbackQuery):
    await callback.message.answer('Образовательные программы Минского филиала РЭУ им. Г.В.Плеханова:\n\n(На данный момент чат-бот позволяет ознакомиться только с образовательными программами бакалавриата)', reply_markup=kb2)
    await callback.answer()
            #БИЗНЕС-ИНФОРМАТИКА
@dp.callback_query_handler(text='bi')
async def bi(callback: types.CallbackQuery):
    await callback.message.answer('<b>Бизнес-информатика</b> - одно из самых молодых и перспективных направлений подготовки современного высшего образования, новая область профессиональной деятельности, формирующаяся на стыке экономики, менеджмента и информационно-коммуникационных технологий (ИКТ).\n\nДанное направление доступно для очной и очно-заочной форм обучения.',reply_markup=kb3, parse_mode='html')
    await callback.answer()
            #МЕНЕДЖМЕНТ
@dp.callback_query_handler(text='man')
async def man(callback: types.CallbackQuery):
    await callback.message.answer('<b>Менеджмент</b> - освоение современных управленческих технологий, обеспечивающих эффективность менеджмента на практике; обучение на основе комплекса программно-технических средств менеджмента, используемых компаниями-лидерами; эффективное применение элементов электронного образования; участия в международных и всероссийских олимпиадах, конференциях, бизнес-неделях и летних студенческих школах; использование современных образовательных методик и технологий, обеспечивающих формирование компетентностного потенциала выпускника.\n\nДанное направление доступно для очной и очно-заочной форм обучения.', reply_markup=kb3, parse_mode='html')
    await callback.answer()
            #ЭКОНОМИКА
@dp.callback_query_handler(text='econ')
async def econ(callback: types.CallbackQuery):
    await callback.message.answer('<b>Экономика</b> максимально охватывает различные специализации современного аналитика-финансиста, что позволяет овладеть широким спектром его важнейших профессиональных навыков. Это позволяет свободно выбрать профессию в любой области учета, налогообложения, анализа и финансов.\n\nДанное направление доступно только для очно-заочной формы обучения.', reply_markup=kb3, parse_mode='html')
    await callback.answer()
            #ПРИКЛАДНАЯ ИНФОРМАТИКА
@dp.callback_query_handler(text='pi')
async def pi(callback: types.CallbackQuery):
    await callback.message.answer('<b>Прикладная информатика</b> максимально охватывает различные специализации современной информатики, что позволяет овладеть широким спектром его важнейших профессиональных навыков. Это позволяет свободно выбрать профессию в любой области компьютерных наук.\n\nДанное направление доступно только для заочной формы обучения.', reply_markup=kb3, parse_mode='html')
    await callback.answer()
        #ВСТУПИТЕЛЬНЫЕ ИСПЫТАНИЯ
@dp.callback_query_handler(text='exam')
async def exam(callback: types.CallbackQuery):
    await callback.message.answer('<b>Для поступления на очную и очно-заочную формы обучения:</b>\n\nВступительные испытания (бюджет) – для поступающих на базе среднего общего или высшего образования: 1. Математика 2. Русский язык 3. Обществознание/история/иностранный язык (по выбору поступающего)\n\nВступительные испытания (бюджет) – для поступающих на базе среднего специального образования: 1. Математика в социально-экономических науках 2. Русский язык 3. Экономика\n\nВступительное испытание (внебюджет): математика (дистанционно)\n\n<b>Для поступления на заочную форму обучения:</b>\n\nВступительный предмет для граждан Республики Беларусь и иностранных граждан: математика (дистанционно)\n\nВступительные предметы для граждан Российской Федерации: 1. Математика в технических науках 2. Русский язык 3. Информатика в технических науках (все предметы дистанционно)\n\nСертификаты ЦЭ и ЦТ являются альтернативой вступительным экзаменам при подаче документов для поступления.', reply_markup=kb20, parse_mode='html')
    await callback.answer()
        #ДАТЫ ЭКЗАМЕНОВ
@dp.callback_query_handler(text='dataexam')
async def dataexam(callback: types.CallbackQuery):
    await callback.message.answer('Даты сдачи очных экзаменов для поступления на бюджет:\n\n1) Математика, Математика в технических науках, Математика в социально-экономических науках - 13.07 в 9:00 (801 ауд.)\n2) Русский язык - 19.07 в 9:00 (801 ауд.)\n3) Экономика - 17.07 в 9:00 (801 ауд.)\n4) Иностранный язык - 14.07 в 10:00 (801 ауд.)\n5) История - 15.07 в 10:00 (801 ауд.)\n6) Обществознание - 17.07 в 9:00 (801 ауд.)\n\nКонсультация по сдаче очных экзаменов пройдёт дистанционно 11.07 в 10:00 (ссылка на мероприятие придёт на адрес электронной почты, указанный при подаче документов).\n\nЭкзамен по математике для поступления на платную форму обучения проводится в онлайн-формате с 27.06 10:00 по 23.08 23:59:\nhttps://www.рэу.рф/pk/entrant', reply_markup=kb20)
    await callback.answer()
        #СТОИМОСТЬ ОБУЧЕНИЯ
@dp.callback_query_handler(text='cost')
async def cost(callback: types.CallbackQuery):
    await callback.message.answer('Очная форма обучения: 4806 BYN/год\nОчно-заочная форма обучения: 3444 BYN/год\nЗаочная форма обучения: 2852 BYN/год', reply_markup=kb20)
    await callback.answer()
        #ОБ УНИВЕРЕ
@dp.callback_query_handler(text='uni')
async def uni(callback: types.CallbackQuery):
    await callback.message.answer('<b>Российский экономический университет им. Г. В. Плеханова</b> - ведущее экономическое высшее учебное заведение Российской Федерации. РЭУ им. Г. В. Плеханова неизменно входит в <b>десятку</b> лучших университетов, традиционно входит в <b>топ-20</b> вузов, выпускники которых востребованы работодателями (Рейтинг «Топ-100 вузов России» RAEX 2022).\n\nПервый и единственный российский университет, имеющий категорию «5 звезд» в престижном международном рейтинге <b>QS Stars</b>. Всего в мире чуть более 50 вузов имеют такую категорию.\n\n<b>Минский филиал РЭУ им. Г. В. Плеханова</b> работает в Республике Беларусь с 2003г. и имеет более чем 20-летний опыт подготовки высококвалифицированных специалистов.', parse_mode='html', reply_markup=kb4)
    await callback.answer()
            #ДИПЛОМ
@dp.callback_query_handler(text='diploma')
async def diploma(callback: types.CallbackQuery):
    photo = InputFile('diploma.jpeg')
    await bot.send_photo(chat_id=callback.message.chat.id, photo=photo, caption='По окончании обучения выпускникам выдаётся <b>диплом о высшем образовании государственного образца Российской Федерации.</b>', parse_mode='html', reply_markup=kb20)
    await callback.answer()
        #КОНТАКТЫ
@dp.callback_query_handler(text='contacts')
async def contacts(callback: types.CallbackQuery):
    await callback.message.answer('Наши контакты:\n\nПриёмная комиссия: (+375 44) 762 57 63\nУчебно-методический отдел: (+375 17) 244 12 91\nПриёмная директора: (+375 17) 317 45 56', reply_markup=kb20)
    await callback.answer()
        #СОЦСЕТИ
@dp.callback_query_handler(text='links')
async def links(callback: types.CallbackQuery):
    await callback.message.answer('Наши соцсети:\n\nInstagram: instagram.com/reu.minsk\nВконтакте: vk.com/abiturient_minskreu', reply_markup=kb20)
    await callback.answer()
        #ВЫХОД НА ГЛАВНУЮ
@dp.callback_query_handler(text='main')
async def main(callback: types.CallbackQuery):
    await callback.message.answer('<b>Вы вернулись на главную страницу.</b>\nВыберите интересущую Вас информацию:', parse_mode='html', reply_markup=kb1)
    await callback.answer()

    #FINAL HANDLER

@dp.message_handler()
async def echo_send(message : types.message):
    if message.text == 'Hi':
        await message.answer(message.text)
    else:
        await message.answer('Общение с ботом происходит при помощи кнопок, а также команд, расположенных в меню в левом нижнем углу чата.')

executor.start_polling(dp, on_startup=on_startup)
# executor.start_polling(dp, skip_updates=True, on_startup=on_startup)