#!/usr/bin/env python
# coding: utf-8

# # DATA PROGRAMMING - PROBLEM SET 1

#  # Q1:- What data type is each of the following (evaluate where necessary)?

#  5	<br>
#  5.0	<br>
#  5 > 1	<br>
#  '5'	<br>
#  5 * 2	<br>
#  '5' * 2	<br>
#  '5' + '2'	<br>
#  5 / 2	<br>
#  5% 2	<br>
#  {5, 2, 1}	<br>
#  5== 3	<br>
#  Pi(the number)	<br>

#  ANSWER :-1

# | VALUE      |  DATA TYPE                      |
# |----------- |---------------------------------|
# |5           |INTEGER DATA TYPE                |
# |5.0         | FLOATING POINT DATA TYPE        |
# |5 > 1       |BOOLEAN DATA TYPE (5 IS GREATER THAN 1 , SO IT IS TRUE)|
# |'5'         | STRING DATA TYPE|
# |5 * 2       |INTEGER DATA TYPE (5*2=10)|
# |'5' * 2     | STRING DATA TYPE (55)|
# |'5' + '2'   |STRING DATA TYPE (52)|
# |5 / 2       | FLOATING POINT DECIMAL DATA TYPE (2.5)|
# |5% 2        |INTEGER DATA TYPE (1)|
# |{5, 2, 1}   |SET (3 INTEGERS )|
# |5== 3       |BOOLEAN DATA TYPE (5 IS NOT EQUAL TO 3 , SO IT IS FALSE)|
# |Pi(thenumber)| FLOATING POINT DECIMAL DATA TYPE(3.14.......)|

# In[4]:


print(5>1)


# In[5]:


print(5*2)


# In[6]:


print('5' *2)


# In[7]:


print('5' + '2')


# In[8]:


print(5/2)


# In[9]:


print(5%2)


# In[10]:


print(5==3)


# # Question 2
# # Write (and evaluate) python expressions that answer these questions:
# 
# 

# A)How many letters are there in 'Supercalifragilisticexpialidocious'?

# In[11]:


word= 'Supercalifragilisticexpialidocious'
print(len(word))


# B)Does 'Supercalifragilisticexpialidocious' contain 'ice' as a substring?
# 
# 

# In[12]:


word='Supercalifragilisticexpialidocious'
"ice" in word


# C) Which of the following words is the longest: Supercalifragilisticexpialidocious, Honorificabilitudinitatibus, or Bababadalgharaghtakamminarronnkonn?

# In[13]:


words = ["Supercalifragilisticexpialidocious", "Honorificabilitudinitatibus", "Bababadalgharaghtakamminarronnkonn"]
longest=max(words, key=len)
print("The Longest Word is :",longest)


# D)Which composer comes first in the dictionary: 'Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein'. Which one comes last?

# In[14]:


composer=[ 'Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein']
composer.sort()
print(composer)
print("first_composer:",composer[0])
print("last_composer:",composer[-1])


#  # Question 3

# Implement function triangleArea(a,b,c) that takes as input the lengths of the 3 sides of a triangle and returns the area of the triangle. By Heron's formula, the area of a triangle with side lengths a, b, and c is , where .
# 
#   s(s-a)(s-b)(s-c)
#   s=(a+b+c)/2

#  ANSWER:-3

# In[35]:


a=int(input("enter the length of side a: "))
b=int(input("enter the length of side b: "))
c=int(input("enter the length of side c: "))

import math

s=(a+b+c)/2 

areaoftriangle=math.sqrt(s*(s-a)*(s-b)*(s-c))  

print(areaoftriangle)


# # Question 4
# # Write a program in python to separate odd and even integers in separate arrays.

# In[1]:


def evenodd(Y):
    evenlist = []
    oddlist=[]
    for i in Y:
      if(i%2 == 0):
         evenlist.append(i)
      else:
        oddlist.append(i)
    print("The even elements are : " , evenlist)
    print("The odd elements are : ", oddlist)
            
Y=list()
n=int(input("enter the number of elements to be stored in the array:  "))
print("enter the element : ")
for i in range(int(n)):
    p=int(input(""))
    Y.append(p)
evenodd(Y)


# # Question 5

# a) Write a function inside(x,y,x1,y1,x2,y2) that returns True or False depending on whether the point (x,y) lies in the rectangle with lower left corner (x1,y1) and upper right corner (x2,y2).

# In[3]:


def inside(x,y,x1,y1,x2,y2):
    
    return(x<x2 and x>x1 and y<y2 and y>y1)

print(inside(1,1,0,0,2,3))

print(inside(-1,-1,0,0,2,3))


# b) Use function inside() from part a. to write an expression that tests whether the point (1,1) lies in both of the following rectangles: one with lower left corner (0.3, 0.5) and upper right corner (1.1, 0.7) and the other with lower left corner (0.5, 0.2) and upper right corner (1.1, 2).

# In[2]:


def inside(x, y, x1, y1, x2, y2):
    return x1 <= x <= x2 and y1 <= y <= y2


r1 = inside(1, 1, 0.3, 0.5, 1.1, 0.7)


r2 = inside(1, 1, 0.5, 0.2, 1.1, 2)


final_result = r1 and r2

print(final_result)


# # Question 6

#  You can turn a word into pig-Latin using the following two rules (simplified):
# 
# If the word starts with a consonant, move that letter to the end and append 'ay'. For example, 'happy' becomes 'appyhay' and 'pencil' becomes 'encilpay'.
# If the word starts with a vowel, simply append 'way' to the end of the word. For example, 'enter' becomes 'enterway' and 'other' becomes 'otherway' . For our purposes, there are 5 vowels: a, e, i, o, u (so we count y as a consonant).
# Write a function pig() that takes a word (i.e., a string) as input and returns its pig-Latin form. Your function should still work if the input word contains upper case characters. Your output should always be lower case however

# In[1]:


def pig(word):
    word=word.lower()
    
    vowels = ['a','e','i','o','u']
    
    if word[0] not in vowels:
        pig_latin_word = word[1:] + word[0] + 'ay'
    else:
        pig_latin_word = word + 'way'
            
    return pig_latin_word

input_words = []
for i in range(2):
    user_input = input(f"enter word {i + 1}: ")
    input_words.append(user_input)
    
for i , word in enumerate(input_words):
    result = pig(word)
    print(f"pig latin {i+1}: {result}")
    

            


#  # Question 7

# File bloodtype1.txt records blood-types of patients (A, B, AB, O or OO) at a clinic. Write a function bldcount() that reads the file with name name and reports (i.e., prints) how many patients there are in each bloodtype.

# In[21]:


file_path = "Downloads/bloodtype1.txt"
blood_type_counts = {'A': 0, 'B': 0, 'AB': 0, 'O': 0 ,'OO':0}
with open(file_path, 'r') as file:

    for line in file:
        print(line)
        blood_type = line.split()
        for blood_group in blood_type:
            blood_type_counts[blood_group] = blood_type_counts[blood_group]+1
for key,values in  blood_type_counts.items():
    print(f"There are {values} patients of blood type {key}")


# # Question 8

# Write a function curconv() that takes as input:
# 
# a currency represented using a string (e.g., 'JPY' for the Japanese Yen or 'EUR' for the Euro)
# an amount
# and then converts and returns the amount in US dollars.

# In[7]:


dict_currency={}
file_path = "Downloads/currencies.txt"
with open(file_path, 'r') as file:
    for line in file:
        cur_details = line.split('\t')
        key=cur_details[0]
        values=cur_details[1:]
        dict_currency[key]=values
#print(dict_currency)

def currconv(curr,amount):
    print(float(dict_currency[curr][0])*amount)

currconv('EUR',100)
currconv('JPY',100)


# # Question 9

# Each of the following will cause an exception (an error). Identify what type of exception each will cause.
# 
# 

# In[ ]:


A) Trying to add incompatible variables, as in adding 6 + 'a':
    :-TYPE ERROR: This will result in a "TypeError" because we are trying to perform an operation (addition) between two incompatible types(integer and string).

B) Referring to the 12th item of a list that has only 10 items:
   :-INDEXERROR: This will result in an IndexError because we are trying to access an index that is out of the range of the list.
    
C) Using a value that is out of range for a function's input, such as calling math.sqrt(-1.0):
   :-VALUEERROR(Runtime Error): This will result in a ValueError because the math.sqrt() function cannot compute the square root of a negative number. 
    
D) Using an undeclared variable, such as print(x) when x has not been defined:
   :-NAMEERROR: This will result in a NameError because we are trying to use a variable (x) that has not been defined or is not in scope.
    
E) Trying to open a file that does not exist, such as mistyping the file name or looking in the wrong directory:
    :-FILENOTFOUNDERROR: This will result in a FileNotFoundError because we are trying to open a file that does not exist at the specified location.





# # Question 10

# Encryption is the process of hiding the meaning of a text by substituting letters in the message with other letters, according to some system. If the process is successful, no one but the intended recipient can understand the encrypted message. Cryptanalysis refers to attempts to undo the encryption, even if some details of the encryption are unknown (for example, if an encrypted message has been intercepted). The first step of cryptanalysis is often to build up a table of letter frequencies in the encrypted text. Assume that the string letters is already defined as 'abcdefghijklmnopqrstuvwxyz'. Write a function called frequencies() that takes a string as its only parameter, and returns a list of integers, showing the number of times each character appears in the text. Your function may ignore any characters that are not in letters.

# In[20]:


def frequencies(text):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    text = text.lower()
    frequency_list = []
    
    for letter in letters:
        count = text.count(letter)
        frequency_list.append(count)
        
    return frequency_list

r1 = frequencies('The quick red fox got bored and went home.')
r2 = frequencies('apple')

print(r1)
print(r2)


# In[ ]:




