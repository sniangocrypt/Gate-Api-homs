#Получение цены токенов на Gate

#Создайте программу, которая будет делать GET-запрос к API биржи Gate и получать ордербук для монет BTC, ETH и SOL. Используйте документацию API, чтобы разобраться, как именно отправлять запросы.

#Требования:

#	1.	Используйте библиотеку requests для выполнения HTTP-запросов.

#	2.	Программа должна запрашивать ордербук для следующих пар: BTC/USDT, ETH/USDT, SOL/USDT.

#	3.	Обработайте возможные ошибки, которые могут возникнуть при выполнении запроса. Например, если файл не найден, или есть проблема с подключением, выведите понятное сообщение.

#	4.	Полученные данные должны содержать информацию о текущих ордерах на покупку и продажу.


import requests
from colorama import Fore, Back, Style


try:
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    url = '/spot/order_book'
    query_param = 'currency_pair=BTC_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    data = r.json()
    try:
        print(Fore.GREEN + f"Данные об ордерах на покупку БТЦ(цена,объем):  {data['asks']}")
        print(Fore.GREEN + f"Данные об ордерах на продажу БТЦ(цена,объем):  {data['bids']}")
        print()
        print()
    except KeyError:
        print(Fore.RED +f"Проверте правильность запрашиваемого эллемента")
        print()
        print()
except requests.exceptions.ConnectionError:
    print(Fore.RED +f"Ошибка соединения, проверте подключение или адрес запроса- {host}")

# ЗАПРОС ДЛЯ ETH/USDT

# ЗАПРОС ДЛЯ ETH/USDT

try:
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    url = '/spot/order_book'
    query_param = 'currency_pair=ETH_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    data = r.json()
    try:
        print(Fore.GREEN + f"Данные об ордерах на покупку ETH(цена,объем): {data['asks']}")
        print(Fore.GREEN + f"Данные об ордерах на продажу ETH(цена,объем): {data['bids']}")
        print()
        print()
    except KeyError:
        print(Fore.RED + f"Проверте правильность запрашиваемого эллемента")
except requests.exceptions.ConnectionError:
    print(Fore.RED +f"Ошибка соединения, проверте подключение или адрес запроса- {host}")

# ЗАПРОС ДЛЯ SOL/USDT

try:
    host = "https://api.gateio.ws"
    prefix = "/api/v4"
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    url = '/spot/order_book'
    query_param = 'currency_pair=SOL_USDT'
    r = requests.request('GET', host + prefix + url + "?" + query_param, headers=headers)
    data = r.json()
    try:
        print(Fore.GREEN + f"Данные об ордерах на покупку SOL(цена,объем): {data['asks']}")
        print(Fore.GREEN + f"Данные об ордерах на продажу SOL(цена,объем): {data['bids']}")
        print()
        print()
    except KeyError:
        print(Fore.RED +f"Проверте правильность запрашиваемого эллемента")
except requests.exceptions.ConnectionError:
    print(Fore.RED +f"Ошибка соединения, проверте подключение или адрес запроса- {host}")
