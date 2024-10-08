import random

# List of moods
moods = ["happy", "sad", "energetic", "calm"]

# List of days
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Loop through each day of the week and print a random mood
for day in days_of_week:
    mood = random.choice(moods)
    print(f"{day}: {mood}")

# Request user input to print the mood for a specific day
user_day = input("Enter a day of the week to see its mood: ")
if user_day in days_of_week:
    mood = random.choice(moods)
    print(f"The mood for {user_day} is: {mood}")
else:
    print("Invalid day entered.")