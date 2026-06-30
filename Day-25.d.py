sentence = input("Enter a sentence : ")

words = sentence.split()

for i in range(len(words)):
    for j in range(i + 1, len(words)):
        if len(words[i]) > len(words[j]):
            temp = words[i]
            words[i] = words[j]
            words[j] = temp

print("Words sorted by length:")

for i in words:
    print(i)