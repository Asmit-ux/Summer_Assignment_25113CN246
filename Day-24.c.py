sentence = input("Enter a sentence : ")

words = sentence.split()

longest = words[0]

for i in words:
    if len(i) > len(longest):
        longest = i

print("Longest word is : ", longest)