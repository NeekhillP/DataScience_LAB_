#ask the user to input the list of words and reverse only if the length of words is even 

words_input=input("Enter the words seperate by the space:")
words=words_input.split()
reversed_words=[]
for word in words:
    if len(word)%2==0:
        reversed_words.append(word[::-1])
    else:
        reversed_words.append(word)
        

print(" ".join(reversed_words))