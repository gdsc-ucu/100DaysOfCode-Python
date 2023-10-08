def userVote():
    userAge = int(input("Whats your age? "))

    if userAge >=18:
        print("You are eligible to vote.")
    else:
        print("Sorry, you aren't eligible to vote yet.")
        
userVote()