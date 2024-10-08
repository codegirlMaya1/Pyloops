import random

# Predefined list of moods
moods = ["happy", "sad", "tired", "excited", "anxious", "relaxed"]

# Days of the week and times of the day
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
times = ["morning", "afternoon", "evening"]

# Dictionary to store moods
mood_tracker = {}

# Nested loops to iterate over days and times
for day in days:
    mood_tracker[day] = {}
    for time in times:
        mood = random.choice(moods)
        mood_tracker[day][time] = mood
        print(f"On {day} {time} you were {mood}.")

# Function to get mood for a specific day and time
def get_mood(day, time):
    return mood_tracker.get(day, {}).get(time, "No mood recorded")

# User input to check mood
user_day = input("Enter a day of the week: ")
user_time = input("Enter a time of the day (morning, afternoon, evening): ")
print(f"On {user_day} {user_time} you were {get_mood(user_day, user_time)}.")