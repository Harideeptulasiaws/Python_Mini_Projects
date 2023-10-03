print("Welcome to my Computer Quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
    
print("Okay, Let's Play : ")

score = 0

answer =input("what does CPU stand for? ")
if answer == "Central Processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer =input("what does GPU stand for? ")

if answer == "Graphic Processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer =input("what does RAM stand for? ")

if answer == "Random Access Memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer =input("what does PC stand for? ")

if answer == "Personal Computer":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
print("You got " + str(score) + " questions correct!")   
print("You got " + str((score/4) * 100) + "%.")  
 
 
