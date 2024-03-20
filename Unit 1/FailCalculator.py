print("Welcome to to the Did I fail Calculator")
print("This app calculates your grade, and tells you if yor're failing or passing")
print("How many points was your grade out of?")
total_pts_available=int(input("enter total points available"))
pts_earned=int(input("enter your score"))
output=(pts_earned) / (total_pts_available) * (100)
print("your score is",output,"%")
if output > 60:
    print("You passed!")
else:
    print("You failed!")
    
