#Fibonacci, yeni bir sayıyı önceki iki sayının toplamı oluşturur (sum of a new number to the previous two numbers)
# 1,1,2,3,5,8,13,21,34

a = 1
b = 1

fibo = [a,b]

for i in range(10):
    a,b = b,a+b
    fibo.append(b)
print(fibo)