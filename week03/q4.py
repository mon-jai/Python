def check(temperature, wind, humidity):
    if((temperature > 30 and wind == 0) or humidity > 85):
        print('開冷氣')

temperature = int(input())
wind = int(input())
humidity = int(input())

check(temperature, wind, humidity)
