import requests

print('Введите любое число:')
number = int(input())

def get_number_fact(number):
    url = f"http://numbersapi.com/{number}"
    response = requests.get(url)
    return response.text


fact = get_number_fact(number)
print(f"Факт о числе {number}: {fact}")
