import requests
import datetime
from config import weather_tbot


def get_weather(city, weather_tbot):

    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U0001F325",
        "Rain": "Дождь \U0001F327",
        "Drizzzle": "Ливень \U00002614",
        "Thunderstorm": "Гроза \U0001F329",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F328"
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_tbot}&units=metric"
        )
        data = r.json()

        city = data['name']
        cur_weather = data['main']['temp']

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = 'Посмотри в окно, не могу понять, что там!'

        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_the_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(
            data['sys']['sunrise'])

        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
      f"Погода в городе: {city}\nТемпература: {cur_weather}C° {wd}\n"
      f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
      f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
      f"Хорошего дня!")


    except Exception as ex:
        print(ex)
        print('Проверьте название города')

def main():
    city = input('Введите город: ')
    get_weather(city, weather_tbot)

if __name__=='__main__':
    main()