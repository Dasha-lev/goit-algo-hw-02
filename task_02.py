from collections import deque

#Функція для перевірки, чи є рядок паліндромом
def is_palindrome(input_string):
    #Перетворюємо рядок на нижній регістр та видаляємо пробіли
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())

    #Створюємо двосторонню чергу (deque) з символів рядка
    char_deque = deque(cleaned_string)

    #Порівнюємо символи з обох кінців черги
    while len(char_deque) > 1:
        #Вилучаємо перший та останній символи для порівняння
        front = char_deque.popleft()
        back = char_deque.pop()

        #Якщо символи не збігаються, то рядок не є паліндромом
        if front != back:
            return False

    #Якщо всі символи збіглися, рядок є паліндромом
    return True

#Приклади для перевірки
test_string1 = "A man a plan a canal Panama"
test_string2 = "Hello, World"
test_string3 = "racecar"

print(f'"{test_string1}" є паліндромом? {is_palindrome(test_string1)}')
print(f'"{test_string2}" є паліндромом? {is_palindrome(test_string2)}')
print(f'"{test_string3}" є паліндромом? {is_palindrome(test_string3)}')
