#if statement
veg = str(input("type the vegitable Name:"))
if veg == "Tomato":
    print("The vegitable is Tomato")
else:
    print("The vagitable is not the same")

#elif statement

tomorrow =str(input("Type the Tommorrow's wether:"))
if tomorrow == "warm":
    print("I'll go to the sea.")
elif tomorrow == "very hot":
    print("I'll go to the forest.")
else:
    print("I'll stay home.")

#nested if else
score = int(input("Please enter the student's score. "))
 
if score >= 90:
    print("This student's score of " + str(score) + " is an A.")
else:
    if score >= 80:
        print("This student's score of " + str(score) + " is a B.")
    else:
        if score >= 70:
            print("This student's score of " + str(score) + " is a C.")
        else:
            if score >= 60:
                print("This student's score of " + str(score) + " is a D.")
            else:
                print("This student's score of " + str(score) + " is a F.")
#try th program in elif statment
score = int(input("Please enter the student's score. "))
 
if score >= 90:
    print("This student's score of " + str(score) + " is an A.")
elif score >= 80:
        print("This student's score of " + str(score) + " is a B.")
elif score >= 70:
        print("This student's score of " + str(score) + " is a C.")
elif score >= 60:
        print("This student's score of " + str(score) + " is a D.")
else:
        print("This student's score of " + str(score) + " is a F.")
































































