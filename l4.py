#1
strings = ["мука", "боль", "соль", "остров", "кол", "ролл"]
for string in strings:
    if string.endswith("л"):
        print(string)

#2
input_string = "Лира Литература Лаврушка Петрушка Колян"
input_string = input_string.lower()
new_string = ""
for char in input_string:
    if char == "л" :
        new_string += char

print(new_string)


#3
import random
random_string = ''
valid = False
while not valid:
    random_string = ''.join(random.choice('0123456789') for _ in range(6))
    if '3' in random_string:
        valid = True

print(random_string)


#4

input_string = "Солнце светит, птицы поют, а цветы расцветают весной. самоедлинноеслово"
words = input_string.split()
new_string = ""
for word in words:
    if 5 <= len(word) <= 10:
        new_string += word + " "

print(new_string)
