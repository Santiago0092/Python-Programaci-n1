num1 = 5
num2 = 5
num3 = 10

print(num1 == num2 and num1 != num3)# 1 1 = 1
print(num1 == num2 and num1 > num3)# 1 0 = 0
print(num1 != num2 and num1 > num3)#1 0 = 0
print(num1 != num2 and num1 < num3)# 0 1 = 0
#suma logica
print(num1 == num2 or num1 != num3)# 1 1 = 1
print(num1 == num2 or num1 > num3)# 1 0 = 1
print(num1 != num2 or num1 > num3)# 0 0 = 0
print(num1 != num2 or num1 < num3)# 0 1 = 1

#not - inversor logico
print(not num1 == num2)# 1=0
print(not num1 != num2)# 0=1

print(num1 != num2 & num1 <num3) #0 1= 0