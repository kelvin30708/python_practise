import os
for i in range(1, 11):
    print(str(i+2), end = " ")
    if i == 5:
        break
if 1: print("\ntrue");print("false") # 條件程式如果只有一行程式碼建議用 ;
# 太長的程式碼可以用 \ 
sum = 1 + 2 + \
      3 + 4 + \
      5
# python contains complex with a + b"j"
h = 5 + 6j
print(type(h))
# multiple assignment
x = y = z = 10
print(x, y, z)
# simutaneous assignment
x, y = 1, 2
x, y = y, x
print(x, y)
# python operator priority
# 01.  ()
# 02.  **          |指數
# 03.  ~           |
# 04.  +,-         |
# 05.  *,/,//, %   |乘, 除, 整數除法, 餘數
# 06.  <<, >>
# 07.  &           |位元運算子 AND
# 08.  ^           |位元運算子 XOR
# 09.  in, not in, 
#      is, is not,
#      <, <=, >, >=
#      <>, !=, ==
# 10.  not         |邏輯運算子 NOT         
# 11.  and         |邏輯運算子 AND
# 12.  or          |邏輯運算子 OR 
# condition with interval <>
t = 21
if 20 <= t <= 22:
    print("put on your light jacket.")
h = 10
# if python
h = h - 12 if h>=12 else h
print(h)
a = 18
if a < 13:
    print("child")
elif a < 20:
    print("teenager")
else:
    print("adult")
# 巢狀條件
a, b, c = 4, 3, 6
if a > b and a > c:
    print("a is the biggest")
else:
    if b > c:
        print("b is the biggest")
    else:
        print("c is the biggest")
# range 的範圍

for i in range(10):
    print(i, end=" ")
print("")
for i in range(5, 0, -1):
    print(i, end=' ')
print("")

# one  -parameter: range(5)       : 0 ~ 4
# two  -parameter: range(1, 5)    : 1 ~ 4
# three-parameter: range(1, 5, 2) : 1, 3
#                : range(5, 0, -2): 5, 3, 1
# os.system('clear')
r, n = 1, 1
while n <=  5:
    r = r * n
    n = n + 1
print(r)

for i in range(1, 10):
    j = 1
    while j <= 9:
        print(str(i),'*',str(j), '=', str(i*j),'\t', end =  ' ')
        j = j + 1
    print("")
sum = 0
for i in range(1, 6):
    sum += 1
else:
    print("for loop is end.")
    print(sum)
print("even num:")
for i in range(1, 7):
    if i  % 2 == 1:
        continue
    print(i, end = ' ')
print("")
i = 1
while True:
    i += 1
    if i > 5:
        break
print(i)
target, guess = 38, 1
while True:
    guess = int(input("guess num from 1~100:"))
    if target == guess:
        print("correct !!", target)
        break
    elif guess > target:
        print("too big")
    else:
        print("too small")