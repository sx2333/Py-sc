# from sys import argv
# from os.path import exists

# script, filename = argv

# file = open(filename).read()

# print(file)

# print("请输入你要查看的文件名称：")
# file_name = input('>')

# print("下面将查看您输入的文件是否存在：")
# print(exists(file_name))

# file_txt = open(file_name).read()
# print(file_txt)

# print("下面将删除你的文件内容，确认请敲击回车。")
# input('?')
# target = open(filename, 'w')
# target.truncate()

# print("删除完毕。")

# print("下面请输入你想要录入的三行内容：")
# line = input("请输入第一行内容：")
# line2 = input("请输入第二行内容：")
# line3 = input("请输入第三行内容：")
# target.write(f"{line}\n{line2}\n{line3}")
# print("录入完毕。")
# target.close()

# print("需要查看你的刚刚录入的文件吗？继续请敲击回车")
# input('?')
# target2 = open(filename).read()
# print(target2)

# from sys import argv
# from os.path import exists

# script,filename = argv

# def read_file(f):
#     print (f.read())

# def rewind(f):
#     f.seek(0)

# def read_line(currentline, f):
#     print(currentline, f.readline(),end = '')

# def file_exists(f):
#     print("文件是否存在？", exists(f))

# file_exists(filename)
# current_file = open(filename)

# print("文件内容为:")
# read_file(current_file)

# print("查看文件的前三行内容:")
# rewind(current_file)
# current_line = 1
# read_line(current_line,current_file)
# current_line += 1
# read_line(current_line,current_file)
# current_line += 1
# read_line(current_line,current_file)

# current_file.close()

# def add(a, b):
#     return a + b

# def sub(a, b):
#     return a - b

# def mul(a, b):
#     return a * b

# def div(a, b):
#     return a / b

# def num(started):
#     apple = started * 100
#     banana = int(apple / 2)
#     orange = int(banana - 5)
#     return apple, banana, orange

# started = 10
# apple1, banana1, orange1 = num(started)
# print(apple1)
# print(banana1)
# print(orange1)

# count_num = num(started)
# print("we have{} apples, {}banana, {}oranges".format(*count_num))

# def break_words(stuff):
#     words = stuff.split()
#     return words

# def print_first_word(words):
#     word = words.pop(0)
#     print(word)

# def print_last_word(words):
#     word = words.pop(1)
#     print(word)

# def sort_words(words):
#     return sorted(words)

# def sort_sentence(sentence)
#     words = break_words(sentence)
#     return sort_words

# import random
# boys = random.randint(100,200)
# girls = random.randint(100,200)
# dogs = 150

# if boys > girls:
#     print("男生找不到对象")
# elif boys < girls:
#     print("女生找不到对象")
# else:
#     print("正好")