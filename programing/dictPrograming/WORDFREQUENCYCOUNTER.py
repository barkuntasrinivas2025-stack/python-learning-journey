# WORD FREQUENCY COUNTER
text = "cat dog cat bird dog cat"
print(text)
words = text.split()
print(words)
words_Count={}
for word in words:
    if word in words_Count:
        words_Count[word] += 1
    else:
        words_Count[word] = 1
print(words_Count)