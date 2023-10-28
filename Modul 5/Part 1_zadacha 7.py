def Палиндромом(число):
    a = str(число)
    if a == a[::-1]:
        return True
    else:
        return False

num1 = 148321
num2 = 123321
num3 = 321987

print(Палиндромом(num1))  
print(Палиндромом(num2)) 
print(Палиндромом(num3))  
