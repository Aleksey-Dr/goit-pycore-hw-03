import random

def get_numbers_ticket(min, max, quantity):

    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        print("Некоректні дані. Спробуйте ще раз. Введіть від 1 до 1000")
        return []

    lottery_numbers = []
    while len(lottery_numbers) < quantity:
        new_number = random.randint(min, max)
        if new_number not in lottery_numbers:
            lottery_numbers.append(new_number)

    lottery_numbers.sort()
    return lottery_numbers
    

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)