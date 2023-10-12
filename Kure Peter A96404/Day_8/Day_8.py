def userVote():
    age = int(input("Whats your age? "))

    if age >=18:
        print("You are eligible to vote.")
    else:
        print("Sorry, you aren't eligible to vote yet.")
        
userVote()