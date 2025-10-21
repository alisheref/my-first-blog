#ppp = []
#number = 0
#while True:
#  number += 1
#  s = int(input(f"Ведите {number} число:"))
#  ppp.append(s)
#  if s == 0: break
#g = len(ppp)
oit = 0
s = input("Веди многозначное число")
d = input("какое число искать? (одна цифра): ")
count = s.count(d)
print(f"Цифра {d} встречается {count} раз(а) в числе {s}.")
