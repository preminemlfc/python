temp = int(input('Please enter the temparture in Celcius.\ An integer between 0-40:'))

if temp > 30:
    print('wear shorts')
elif temp <= 30 and temp >= 20:
    print('normal temperature')
elif temp <= 20 and temp >= 10:
    print('wear sweaters')
else
    print('Dont go out')