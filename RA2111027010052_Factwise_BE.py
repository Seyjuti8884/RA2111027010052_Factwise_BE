#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question 1:
def to_english(number):
    _ones = {
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine',
            10: 'ten',
            11: 'eleven',
            12: 'twelve',
            13: 'thirteen',
            14: 'fourteen',
            15: 'fifteen',
            16: 'sixteen',
            17: 'seventeen',
            18: 'eighteen',
            19: 'nineteen',
            }

    _tens = {
            2: 'twenty',
            3: 'thirty',
            4: 'forty',
            5: 'fifty',
            6: 'sixty',
            7: 'seventy',
            8: 'eighty',
            9: 'ninety'
            }
    if abs(number) >= 10000:
        return str(number)
    elif number == 0:
        return 'zero'
    else:
        output = ''

        if number < 0:
            output += 'negative '
            number = abs(number)

        if number >= 1000:
            output += _ones[number // 1000]
            if number % 1000 == 0:
                output += " thousand"
            else:
                output += " thousand "
            number %= 1000

        if number >= 100:
            output += _ones[number // 100]
            if number % 100 == 0:
                output += " hundred"
            else:
                output += " hundred and "
            number %= 100

        if number >= 20:
            output += _tens[number // 10]
            number %= 10
            if number % 10 in _ones:
                output += '-'

        if number in _ones:
            output += _ones[number]

        return output

def cleanse_string(string):
    string = string.replace(' ', '')
    string = string.replace('-', '')
    return string

print(sum(len(cleanse_string(to_english(i))) for i in range(1, 1001)))

#Output: 21124
# In[ ]:


#Question 2:
from typing import List

def maxScore(cardPoints: List[int], k: int) -> int:
    ans = s = sum(cardPoints[-k:])
    for i, x in enumerate(cardPoints[:k]):
        s += x - cardPoints[-k + i]
        ans = max(ans, s)
    return ans


cardPoints = list(map(int, input("Enter card points separated by spaces: ").split()))
k = int(input("Enter the value of k: "))

result = maxScore(cardPoints, k)

print("Maximum score:", result)

#output -
# Enter card points separated by spaces: 2 2 2
# Enter the value of k: 2
# Maximum score: 4

# In[ ]:




