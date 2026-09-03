import audio
import music
import random
import pygame
import time
import pickle  # or import json
import json
from datetime import datetime, timedelta

# Initialize pygame
pygame.init()

# Pet attributes
pet_creation_time = datetime.now()
health = 100 # to track sickness odds
happiness = 100
energy = 100 # how often it needs naps
poop = 100 # when does the pet relieve its bowels
# todo maybe introduce IVs or genetics? breeding?
age = pet_creation_time # todo math conversion type shit. turns days into pet years for age
def calculate_age_in_days(creation_time):
    now = datetime.now()
    age_timedelta = now - creation_time
    return age_timedelta.days

# Function to display pet's age
def display_age(days_old):
    if days_old == 0:
        return "less than a day old"
    elif days_old == 1:
        return "1 day old"
    else:
        return f"{days_old} days old"

# Example usage
days_old = calculate_age_in_days(pet_creation_time)
age_display = display_age(days_old)

# Displaying the age in years for the user interface
# Assuming 1 year = 365 days for display purposes
pet_years = days_old // 365
age_as_years = f"{pet_years} year{'s' if pet_years != 1 else ''} old"

print(f"Your pet is {age_display}. (Displayed as: {age_as_years})")

timer = 0 # maybe obsolete due to datetime library maybe being more useful for this intended task

# todo Random Events: Use the random library to introduce random events that can affect your pet's health or happiness, adding an element of surprise.

def intro():
# audio.play(Sound.HELLO)
    print(" ")
    pass

def species():
    species = ["squirrel", "ferret", "rat", "pika", "gopher"]
    pass

def gender():
    gender = ["male", "female", "non-binary"]
    pass

def get_pet_age():
    current_time = datetime.now()
    age = (current_time - pet_creation_time).days
    return age

def petting():
    for i in range(4):
#        display.scroll(':3')
    sleep(800)
#    display.clear()
    pass

def disease():
    diseases = ["rabies", "virus", "bacterial infection"]
    pass

def die():
#    music.play(music.WAWAWAWAA)
#    display.show(Image.SKULL)
#    music.play(music.FUNERAL)
    sleep(1000)
#    display.show(Image.GHOST)
    sleep(200)
#    music.play(music.JUMP_DOWN)
    for i in range(10):
#        display.scroll('Age: ')
#        display.scroll(age)
    for i in range(4):
#        display.scroll('DEAD! ')
#    display.clear()
    pass

def lonely():
#    music.play(music.WAWAWAWAA)
#    display.show(Image.SAD)
#    speech.say('hello')
    pass

def nap():
    for i in range(4):
#        display.show(Image.ASLEEP)
#        speech.say('z z z')
        sleep(200)
#        display.clear()
    pass

def feed():
    global health
    health += 10  # Increase health by 10
    if health > 100:
        health = 100  # Cap health at 100
    pass

def play():
    global happiness
    happiness += 10  # Increase happiness by 10
    if happiness > 100:
        happiness = 100  # Cap happiness at 100
        pass

def game1():  # left or right
    pass
"""    global timer  # Use the global timer variable
    choices = ['left', 'right']
    secret_choice = random.choice(choices)  # Randomly choose left or right
    display.scroll('Guess Left or Right!')

    # Wait for user input
    while True:
        if button_a.is_pressed():
            display.scroll('You chose Left!')
            if secret_choice == 'left':
                display.scroll('Win!')
                break
            else:
                display.scroll('You Lose!')
                break
        elif button_b.is_pressed():
            display.scroll('You chose Right!')
            if secret_choice == 'right':
                display.scroll('You Win!')
                break
            else:
                display.scroll('You Lose!')
                break"""
    pass

def game2():
    timer = 0
    pass

while True:
    timer += 1
    if timer == 60:
        nap()
    elif timer == 120:
        lonely()
#    elif pin_logo.is_touched():
#        audio.play(Sound.HAPPY)
        touching()
#    elif button_a.is_pressed() or button_b.is_pressed():
        game2()
#    elif timer >= 200:  # Change to >= to trigger die() after 200
        die()

        # Main game loop
while True:
    age = get_pet_age()
    print(f"Pet Age: {age} days, Health: {health}, Happiness: {happiness}")

            # Simulate random events
    if random.random() < 0.1:  # 10% chance of a random event
        health -= 5  # Decrease health randomly
        print("Oh no! Your pet got a little sick!")

            # Wait for user input (you can replace this with pygame event handling)
        time.sleep(5)  # Wait for 5 seconds before the next update
        pass