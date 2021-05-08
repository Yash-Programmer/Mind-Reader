import pyttsx3 
import time
import vlc
import webbrowser

engine = pyttsx3.init()

print("\n")
print("Hey Guys, So I am Python. I can read everyone's mind. If you don't believe Just give it a try.")
engine.say("Hey Guys, So I am Python. I can read everyone's mind. If you don't believe Just give it a try.")
engine.runAndWait()

print("\n" "Think a Number between 0-9 in Your Mind. Don't Tell that Number to Me")
engine.say("Think a Number between 0-9 in Your Mind. Don't Tell that Number to Me")
engine.runAndWait()

time.sleep(2.5)

engine.say("Have you thought a number or not")
engine.runAndWait()
Thinking = input("Have you thought a number or not - ")

if Thinking == 'yes':
    print("That's Cool")
    engine.say("That's Cool")
elif Thinking == 'no':
    print("So, I am Giving you 6 more Seconds")
    engine.say("So, I am Giving you 6 more Seconds")
    engine.runAndWait()
    print("Coundown Starts now: - ")
    second = 6
    for count in range(second):
        print(str(second - count) + "  Seconds Remaining")
        time.sleep(1)
        sound_file = vlc.MediaPlayer("file:///C:/Users/Lenovo/PycharmProjects/VariableTestProject/Count.mp3")
        sound_file.play()
        time.sleep(3)
        print("So, the time is up!!")
        engine.say("So, The Time is Up")
        engine.runAndWait()
    else:
        print("Invalid Input")

print("\n")

time.sleep(3.5)

print("Now, Do as I Say.")
engine.say("Now, Do as I Say")
engine.runAndWait()

print("                     Steps:- ")
print("                                    : Add 11 in the Number that You thought")
engine.say("Add 11 in the Number that You thought")
engine.runAndWait()

time.sleep(3.5)

print("                                     : Subtract 5 from the Number that is coming after adding 11.")
engine.say("Subtract 5 from the Number that is coming after adding 11.")
engine.runAndWait()

time.sleep(3.5)

print("                                     : Add 3 in the Number")
engine.say("Add 3 in the Number")
engine.runAndWait()

time.sleep(3.5)

print("                                     : Subtract 10 from the number")
engine.say("Subtract 10 from the number")
engine.runAndWait()

time.sleep(3.5)

print("                                     : Add 100 to the number which came after all these operations")
engine.say("Add 100 to the number which came after all these operations")
engine.runAndWait()

time.sleep(3.5)
print('\n')
engine.say("What's The Number that You Got After these Simple operations")
engine.runAndWait()
UserNum = int(input("What's The Number that You Got After these Simple operations - "))
Statement = "So Your Input is"
print(Statement, UserNum)
engine.say("Hey User, I have got your input!!")
engine.runAndWait()

print("=========================================Just Processing. This Might Take 5-6 Seconds=========================================")
engine.say("Just Processing. This Might Take 5-6 Seconds")
engine.runAndWait()

time.sleep(5.5)

Answer = UserNum-100+10-3+5-11
AnswerStatement = "So the Number that you thought is"

print(AnswerStatement, Answer)

engine.say("Hey User, Python Has got the number that you thought. You can check the number at the last line..... ")
engine.runAndWait()

time.sleep(5)

User_Ans = input("Is Python Correct Or Not - ")
engine.say("Is Python Correct Or Not?")
engine.runAndWait()

if User_Ans == 'correct':
    print("So, That's Cool")
    print('\n')
    engine.say("So, That's Cool")
    engine.runAndWait()
elif User_Ans == 'incorrect':
    print("Sorry, We Will Improve.")
    print('\n')
    engine.say("Sorry, We Will Improve.")
    engine.runAndWait()
elif User_Ans == "not correct":
    print("Sorry, We Will Improve.")
    print('\n')
    engine.say("Sorry, We Will Improve.")
    engine.runAndWait()
else:
    print("Invalid Input Type")
    print('\n')
    engine.say("Invalid Input Type")

time.sleep(4)

Feedback = input("Would you like to fill out the feedback form -  ")
if Feedback.lower() == "yes":
    print('\n')
    print("I Hope the Feedback From is Opened in your Default Web Browser Automatically. If not, So you can click on the link to open it manually. " + "\n" + "               Form Link = https://forms.gle/h5rAZoqNJ3gpZtBC9" + "\n" + "\n")
    print("\n")
    webbrowser.open('https://forms.gle/h5rAZoqNJ3gpZtBC9')
    engine.say('I Hope the Feedback From is Opened in your Default Web Browser Automatically.')
    engine.runAndWait()
elif Feedback.lower() == "no":
    print('\n')
    print("No problem, you can fill next time.")
    engine.say("No problem, you can fill next time.")
    engine.runAndWait()
    print("\n")
else:
    print('\n')
    print("Invalid Input Command" + "\n")
    engine.say("Invalid Input Command")
    engine.runAndWait()


