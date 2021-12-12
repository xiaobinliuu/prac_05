count_words = {}

text = input("Enter text: ")
words = text.split()
maximum = len(words)
for word in words:
    count_words[word] = count_words.get(word, 0) + 1
word_list = [word for word in count_words.items()]
word_list.sort()
print(word_list)
for i in range(len(word_list)):
    print(f"{word_list[i][0]:{maximum}}: {word_list[i][1]}")
