#n = int(input("Ведите количество элементов в системе"))
#sp=[]
#for i in range (n):
#     number = int(input(f"Ведите {i+1} число: "))
#     sp.append(number)
#print(sp)
numbers = []
n = int(input("Ведите сколько будет чисел в списке:"))
for u in range (0, n):
    j = int(input("Ведите число: "))
    numbers.append(j)
a = sum(numbers) / len(numbers)
print(a)