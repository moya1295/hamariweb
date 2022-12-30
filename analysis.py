"""
This is python script to analyse names obtained from hamariweb scrapes. I have writter multiple
functions to use for doing analysis eg. finding palindrom names, finding 3 vowels names, finding 7 char names.
I will be adding more functions to this script as needed.
Author: Muhammad Owais
Date: 27-12-2022
"""

import pandas as pd

### Select file which you want to do analysis on
filename = ""

df = pd.read_csv(filename)

### Drop names which have no meaning, it helps to clean data especially removing names like "Muhammad Ali" "Muhammad Umar"
df = df.dropna(subset=["Meaning"])

### Function to check if name is a palindrom or not
def check_palindrome(name):
    name = name.lower()
    return name == name[::-1]


### if name give it will count number of vowels in it eg "Ali" will output 2
def vowel_count(name):
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    count = 0
    for char in name:
        if char in vowels:
            count += 1
    return count


### Find names which are palindromes
def find_palindrome_names():
    for row in df.iterrows():
        if check_palindrome(row[1][0]):
            print (row)

### Find names by number of vowels eg. if num_vowels = 2 it will output "Ali" "Umar" "Usman"
def find_num_of_vowels(num_vowels):
    for row in df.iterrows():
        name = row[1][0]
        if vowel_count(name) == num_vowels:
            print (row)

### Find names by starting alphabet eg. if char= "A" it will out "Ali" "Anzala" "Abu Bakr"
def find_name_by_char(char):
    for row in df.iterrows():
        name = row[1][0]
        if name[0].lower() == char:
            print (row)

### Find Names by length eg. 5 length words "Usman" "Owais"
def find_name_by_length(length):
    for row in df.iterrows():
        name = row[1][0]
        if (len(name) == length):
            print (row)

### Find names which are single word eg "Ali" "Usman" not "Abu Bakr"
def find_one_word_name(some_length):
    for row in df.iterrows():
        length = row[1][7].split(" ")[-2]
        if length == some_length:
            print (row)
