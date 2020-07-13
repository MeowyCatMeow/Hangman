import random
# Write your code here
while True:
    print('Type "play" to play the game, "exit" to quit:')
    decision = input()
    if decision == "play":
        break
    elif decision == "exit":
        quit()
    
word = ['python', 'java', 'kotlin', 'javascript']
answer = random.choice(word)
print('H A N G M A N\n')
hypens = ""
for y in answer:
    hypens += "-"
hypenslist = list(hypens)
hint = answer
i = 0
typed = []
while i < 8:
    print("")
    print(''.join(hypenslist))
    print("Input a letter:",end="")
    i += 1     
    
    char = input()
    if len(char) != 1:
        print("You should input a single letter")
        i -= 1
        continue
    if char.islower() == False:
        print("It is not an ASCII lowercase letter")
        i -= 1
        continue
    if char in typed:
        print("You already typed this letter")
        i -= 1
        continue
    typed.append(char)
    
    
    
    if char in answer:
        #print('')
        i -= 1
        for x in range(len(answer)):
            #i -= 1
            if answer[x] == char:
                hypenslist[x] = char         
                
    else:
        print("No such letter in the word")
    if hypenslist == answer:
        print("You guessed the word!\nYou survived!")
if hypenslist != answer:
    print("You are hanged!")       
