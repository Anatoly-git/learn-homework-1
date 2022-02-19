"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

from datetime import date

import ephem

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {
        'username': settings.PROXY_USERNAME,
        'password': settings.PROXY_PASSWORD
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def get_constellation(update, context):
    current_date = date.today()
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /planet')
    planet = update.message.text.split()[1] 
    planet = planet.lower().capitalize()
    planets = [x[2] for x in ephem._libastro.builtin_planets()]
    #planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if planet.lower().capitalize() in planets:
        current_date = date.today()

        planetEphem = getattr(ephem, planet)
        planet_pos = planetEphem(current_date)
        const = ephem.constellation(planet_pos)

        #update.message.reply_text(f'{current_date} и {planet}')
        update.message.reply_text(f'Сегодня планета {planet} находится в созвездии: {const}')
    else:
        update.message.reply_text(f'Данной планеты нет в солнечной системе: {planet}, или Вы ввели ее название на кириллице')


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('planet', get_constellation))
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Бот стартовал')

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
