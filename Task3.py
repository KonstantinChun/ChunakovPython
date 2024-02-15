numbers = input('Введите любое количество целых чисел через пробел: ')
numberArray = [int(number) for number in numbers.split()]
resultMsg = str()
for number in numberArray:
    if number % 3 == 0:
        resultMsg += (f'{number} ' '')
print(resultMsg)

