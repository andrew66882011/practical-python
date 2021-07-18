# bounce.py
#
# Exercise 1.5

height = 100
count = 0

while (height >= 0) & (count <=9):
    count+=1
    height*=0.6
    print(round(count, 4), round(height, 4))


