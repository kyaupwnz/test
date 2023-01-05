import json
import re
def to_camel_case(text):
    print(re.split('_|-', text)[0] + ''.join(word.title() for word in re.split('_|-', text)[1::]))

class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

#count_bits = lambda n: bin(n).count('1')

def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))


#even_or_odd = lambda number: "Even" if number % 2 == 0 else "Odd"

lst = [0, 1, 2, 3, 0, 4, 5, 6, 0, 7]
for item in lst:
    if item == 0:
        del lst[lst.index(item)]
        lst.append(item)
#print(lst)

def progression_sum(n):
#количество чисел в строке n равно n, а среднее число в строке n равно n**2 (первое число в строке равно n**2-n+1, а последнее n**2-n+1+(n-1)*2)    
    return n*n*n


def test3():
    with open('operations.json', 'r', encoding = 'utf-8') as file:
        data = json.load(file)
        sorted(data[-5:], key=lambda x: x["date"].split('T')[0], reverse = True)
        counter = 0
        for i in range(len(data)):
            if data[i].get('state') == 'EXECUTED' and data[i].get('description') != "Открытие вклада":
                counter += 1
                date = data[i].get('date').split('T')[0]
                description = data[i].get('description')
                _from = data[i].get('from')
                _from_name = ''
                _from_number = ''
                for _str in _from.split():
                    if _str.isalpha():
                        _from_name += _str + ' '
                    else:
                        _from_number += _str
                _to = data[i].get('to')
                _sum = data[i]['operationAmount'].get('amount')
                currency = data[i]['operationAmount']['currency'].get('name')
                print(date, description)
                print(f"{_from_name} {_from_number[0:4]} {_from_number[5:7]}** **** {_from[-4:]}-> Cчет **{_to[-4:]}")
                print(_sum, currency)
                print()
                if counter >= 15:
                    break



test3()
