#100 Days of Code Begins


# Welcome to the “100 Days of Code” challenge! Today is your first day, and it’s time to start tracking your progress. You need to create a simple program that takes in an input and checks whether it is the first day of your coding challenge or not. Your program should store the number of days you’ve completed so far and let you know if you’ve successfully completed Day 1.
#
# Input
# A single integer days (1 ≤ days ≤ 100), representing how many days you have coded so far in your “100 Days of Code” challenge.
# Output
# If days equals 1, output: "Congratulations! You've completed Day 1!" without quotes.
#
# If days is greater than 1, output: "You're on Day X of the challenge! Keep going!" where X is the number of days you’ve completed without quotes.
# Example
# Sample Input:
# 1
#
# Sample Output:
# Congratulations! You've completed Day 1!
#
# Sample Input:
# 7
#
# Sample Output:
# You're on Day 7 of the challenge! Keep going!




#Coding:
days=int(input())

if days==1:
    print("Congratulations! You've completed Day 1!")
else:
    print(f"You're on Day {days} of the challenge! Keep going!")
