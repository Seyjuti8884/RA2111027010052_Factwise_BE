#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question 1:
ones = ["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

def number_to_words(n):
    if n == 1000:
        return "onethousand"
    words = ""
    if n>=100:
        words+= ones[n // 100] + "hundred"
        n %= 100
        if n > 0:
            words += "and"
        
    if n>=20:
        words+= tens[n//10] 
        n %= 10
    words += ones[n]
    return words
total_letters = 0
for i in range(1,1001):
    word = number_to_words(i)
    total_letters+=len(word)

print("Total letters used from 1 to 1000:",total_letters)


# In[ ]:


#Question 2:
class Solution:
    def maxscore(self,cardpoints:list[int],k: int):
        sum_left,sum_right = sum(cardpoints[:k],0)
        res = sum_left
        for i in range(k):
            sum_left -= cardpoints[k-1-i]
            sum_right += cardpoints[len(cardpoints)-1]
            res = max(res,sum_left + sum_right)
        return res


# In[ ]:


if __name__=="__main__":
    solution = Solution()
    cardpoints = []
    while True:
        try:
            value = int(input())
            cardpoints.append(value)
        except ValueError:
            break
    k= int(input())
    result = solution.maxscore(cardpoints, k)
    print(result)


# In[ ]:




