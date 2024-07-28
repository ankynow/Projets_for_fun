with open("story.txt", "r") as f:
    story = f.read()

#print(story)

words = set()         #using set insted of using words = [] is an empty list
start_of_word = -1

target_start = "<"
target_end = ">"


for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i+1]
        #words.append(word)       it will give repetative word, set will not support append hence using add.
        words.add(word)
        start_of_word = -1 
#print(words)

answers = {}

for word in words:
    answer = input("enter the word" + word + ": ")
    answers[word] = answer 
#print(answers)

#Final step to replace the word with answers

for word in words:
    story = story.replace(word, answers[word])

print(story)



