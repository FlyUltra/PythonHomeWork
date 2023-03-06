def find_prime(number):
    prime = True
    if number < 2:
        prime = False
    else:
        for i in range(2, number):
            if number % i == 0:
                prime = False
                break
    return prime


def next_prime():
    number = int(input('Zadej číslo: '))
    flag, i = True, 1

    if find_prime(number):
        print('Nejbližší číslo je: ', number)
    else:
        while flag:
            if find_prime(number + i):
                print(number + i, 'Je nejblížší prvočíslo')
                flag = False
            i += 1


def next_multiple(number, k):
    for i in range(number + k + 1):
        final_number = i * k
        if final_number > number:
            print('Číslo', final_number, 'je větší než', number)
            return final_number
    return 0


assert next_multiple(1, 2) == 2
assert next_multiple(10, 7) == 14
assert next_multiple(10, 5) == 15
assert next_multiple(54, 6) == 60
assert next_multiple(131, 29) == 145
assert next_multiple(123, 112) == 224
assert next_multiple(423, 90) == 450