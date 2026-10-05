# learn to code
# step by step
# mark out code with a # in front

'''
put longer text here and computer will ignore
lowkey useful for video notes
'''

# stackoverflow best for python answers on google

# "1 thing in coding is being a good googler" - moondev

# printing is showing something

# variable is a storage box


box = "all my cables" # string = sentence

print(box)

# BOOLEANS = True or False
# types of things that are true or false

answer = 30 > 4
print(answer)

# numbers in python
# 2 types - 1. Integer == Whole number, no decimal, 4, 5, 10, 150
# 2. Float, not a whole number ex. 4.74, 3.69. 345.32432

number = 56.45
print(type(number))

#turn floats into integers
num2 = int(number)
print(num2)

# counting in python
# starts at 0
# 0, 1, 2, 3, 4, 5

count = "fun" #f = 0, u = 1 n = 2
print(count[1])

# importing things / import package / module
import math

# math in python(math operators)
# add +, subract -, multiply *, divide /, power of **

math_box = 34.45 - 34
print(math_box)

# sentences = strings
# slicing sentences[0:0]
sentence = "hey this is my sentence"
print(sentence)

# slice
half = sentence[0:10]
print(half)

# variables = boxes to store stuff

# lists = lists of things to store

numb = 56
sentence = "this is a string"
print(sentence, numb)

mylist = [numb, sentence, 'hey hey', 67.34]
print(mylist)
print(mylist[2])

# (command + shift <-) highlights line
# (command + /) comments whatever you highlighted

# dictionary - key & value
my_dictionary = {'name':'moon', 'age':'30', 'fav food':'pizza'}
print(my_dictionary)
print(my_dictionary['fav food'])

sentence_1 = 'hey whats up'
sent_2 = 'yo yo yo'
number1 = 45 # integer = whole number
number2 = 56.56 # decimal = float
sent_3 = 'hello moto'

# if, elif, else
# if statement does something IF TRUE
# or else (elif) do something else
# else final thing to do is this

# when checking true or false use ==, !=, >=, <=

if number1 > number2: # FALSE
  print(sentence_1)
elif number1 == number2:
  print(sent_2)
elif number1 >= number2:
  print(sent_3)
else: # fail safe, do if all else is false
   print('this is the failsafe')

# _ is a space in python

# if its saturday == do chores

# chores - clean bathroom, kitchen, bedroom

# OPERATORS ==, !=, >=, <=

# indexing - getting things out of list
mylist = [numb, sentence, 'hey hey', 67.34]
print(mylist[-1])
#- = counting backwards, starts at -1 not 0
# going fwd is 0, 1, 2, 3

# loops
# While loops and For loops
# while loops - 2 hours to play video games
# you are in a while loop

hours = 2

# while loops loop until false
# while hours < 2.1:
#   print('play video games')
#   hours = (hours + .5)

# for loops - loop until condition fulfilled
listy = [23.45, 45, 'hey there']

# when using for loops the first word after for can be anything
# for zzzz in listy:
#   print(zzzz)

for efwefw in range(11):
  print(efwefw)

# functions - variables, lists, dictionaries
# 20 variables, 4 lists, 10 dictionaries

#use def for a function then name of func()
def storage_unit():

  shoes = 'jordans'
  game = 'zelda'
  age = 27
  gpa = 2.80

  mylist = [shoes, game, age, 'hey there']

  return shoes, mylist

# returning allows use in other parts of code

mylist = storage_unit()[1]
print(mylist)

# pass in information into a function

car = 'toyota'

# function
def passing(car=car): # if argument has = then there is a default

  num = 67

  print(car)

passing() # since no pass it goes to default(car=car)
passing('lambo') # since pass it changes to lambo

def this_is_a_func():

  hey = 'hiiiii'

# google sheets. excel == PANDAS
# package/module/app
import pandas as pd # get app pandas and use it by typing pd

df = pd.read_csv('/content/BTC-USD.csv') # df == 'dataframe'
print(df) # we dont have the data but this would print it

# time series data - data over the course of time
# data that changes everyday
# weather, sporting events, ticket sales, advertising clicks, spend

first_50 = df.head(50)
print(first_50) # prints first 50 rows(head)

first_50 = df.tail(50) # prints last 50 rows(tail)
print(first_50)

# slicing
print(df[0:100])

print(df['date']) # prints date column

# how to access a value out of one column
# build a new dataframe based off condition
df_40k = df.loc[df['close'] > 40000]
print(df_40k) # prints data frane where it closes over 40000

# how to get a specific value out of a dataframe
df3 = df.loc[df['close']==398.938482, 'date'].values[0]
print(df3)

# watch moondev 30min pandas video
# read pandas 10min documentation