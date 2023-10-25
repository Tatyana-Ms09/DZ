def is_palindrome(s):

    s = s.replace(" ", "").lower()
    
    return s == s[::-1]

input_string = input("Введите строку: ")

if is_palindrome(input_string):
    print("Введенная строка - палиндром.")
else:
    print("Введенная строка - не палиндром.")