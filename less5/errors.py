def convert_ab_to_int(a:str, b:str) -> tuple[int, int]:
    return a + b

def divide(a : int | float, b: int | float) -> float:
    raise AttributeError('Я НЕНАВИЖУ ТРОЙКИ')
    return a / b

while True:
    a, b = input('введите два числа для их суммы:').split()
    try:
        a,b = convert_ab_to_int(a, b)
        division_score = divide(a, b)

    except (ZeroDivisionError, ValueError) as e:
       print(f'Ошибка: {e}')
       print('Числа быстро ввъёл а не буквы, дэбик')
       print()
       continue

    except AttributeError as ex:
        print(f'Разработчик злой писюкан, потому что он, цитата "{ex}"')
        print('Сделай пж как он просит')
        

    finally:
        print('Мы в финале')

    ab_sum = a + b
    print(f'Сумма {a} + {b} = {ab_sum}')
    print()
