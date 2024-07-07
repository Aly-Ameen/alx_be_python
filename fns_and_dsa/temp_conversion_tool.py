FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9 
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32


if __name__ == '__main__':
    temp = input('Enter the temprature to convert: ')
    try:
        temp = int(temp)
        typ = input('Is this temperature in Celsius or Fahrenheit? (C/F): ')
        if typ == 'C':
            res_type = 'F'
            res = convert_to_fahrenheit(temp)
        else:
            res_type = 'C'
            res = convert_to_celsius(temp)
        print(f'{temp}°{typ} is {res}°{res_type}')
    except ValueError:
        print('Invalid temperature. Please enter anumeric value.')
