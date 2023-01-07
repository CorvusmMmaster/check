import requests
from datetime import datetime
import telebot
from auth_data import token


def get_data():
    req  = requests.get("https://yobit.net/api/3/ticker/btc_usd")
    req1 = requests.get("https://yobit.net/api/3/ticker/eth_usd")
    req2 = requests.get("https://yobit.net/api/3/ticker/doge_usd")
    response = req.json()
    response1 = req1.json()
    response2 =req2.json()
    sell_btc_price = response["btc_usd"]["sell"]
    sell_eth_price = response["eth_usd"]["sell"]
    sell_doge_price = response["doge_usd"]["sell"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_btc_price}")
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell Eth price: {sell_eth_price}")
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell DOGE price: {sell_eth_price}")


def telegram_bot(token):
    bot = telebot.TeleBot(token)
    @bot.message_handler(commands=["start"] or ["начать"])
    def start_message(message):
        bot.send_message(message.chat.id, "Привет,юный криптоинвестор,чтобы узнать стоимость популярных валют и криптовалют на данный момент отправь мне любой символ! \n ")

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        #BTC
        if message.text.lower() == "Крипта" or "crypto":
            try:
                req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
                response = req.json()
                sell_price = response["btc_usd"]["sell"]
                bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}"
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Что-то неправильно введено("
                )


#Eth
        if message.text.lower() == "eth" or "crypto" or "крипта":
            try:
                req = requests.get("https://yobit.net/api/3/ticker/eth_usd")
                response = req.json()
                sell_price = response["eth_usd"]["sell"]
                bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell Eth price: {sell_price}"
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Что-то неправильно введено("
                )


        #DOGE
        if message.text.lower() == "Крипта" or "crypto":
            try:
                req = requests.get("https://yobit.net/api/3/ticker/doge_usd")
                response = req.json()
                sell_price = response["doge_usd"]["sell"]
                bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell DOGE price: {sell_price}"
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Что-то неправильно введено("
                )


#XRP
            if message.text.lower() == "Крипта" or "crypto":
                try:
                    req = requests.get("https://yobit.net/api/3/ticker/xrp_usd")
                    response = req.json()
                    sell_price = response["xrp_usd"]["sell"]
                    bot.send_message(
                        message.chat.id,
                        f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell XRP price: {sell_price}"
                    )
                except Exception as ex:
                    print(ex)
                    bot.send_message(
                        message.chat.id,
                        "Что-то неправильно введено("
                    )
                # USD
                if message.text.lower() == "Крипта" or "crypto":
                    try:
                        req = requests.get("https://yobit.net/api/3/ticker/usd_rur")
                        response = req.json()
                        sell_price = response["usd_rur"]["sell"]
                        bot.send_message(
                            message.chat.id,
                            f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell USD to RUB price: {sell_price}"
                        )
                    except Exception as ex:
                        print(ex)
                        bot.send_message(
                            message.chat.id,
                            "Что-то неправильно введено("
                        )

    bot.polling()


if __name__ == '__main__':
    telegram_bot(token)