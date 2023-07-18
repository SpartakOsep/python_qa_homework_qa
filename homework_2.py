num = int(input('Введите число: '))

res = [i for i in range(1, num + 1) if num % i == 0]
if num < 0 or num > 99999:
    print('Число должно быть положительным и не более 99999')
elif res[0] == 1 and res[1] == num:
    print(f'Число {num} является простым')
else:
    print(f'Число {num} является составным')
    