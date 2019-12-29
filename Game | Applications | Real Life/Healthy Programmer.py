"""
9-5pm
Water - water.mp3 (3.5 ltr) - Drank - Log
Eyes - eyes.mp3 - every 30min -Eydone
Physical Activity - physical.mp3 every - 45mins - ExDone - log
pygame to play audio
"""
import time

import datetime

import pygame


def getdate():
    return datetime.datetime.now()


def reminder(mp3, stop_word, file):
    pygame.init()

    pygame.display.set_mode((200, 100))

    pygame.mixer.music.load(mp3)

    pygame.mixer.music.play(0)

    while True:

        if input("Enter done if over: ") == stop_word:

            pygame.mixer.music.stop()

            with open(file, 'a') as f:

                f.write("\n" + str(getdate()) + " : " + stop_word)

                print("Data Recorded successfully")

            break

        else:

            clock = pygame.time.Clock()

            clock.tick(10)

            while pygame.mixer.music.get_busy():
                pygame.event.poll()

                clock.tick(10)


def time_limit(currenttime):
    if currenttime > '08:00:00' and currenttime < '17:00:01':

        return True

    else:

        print("Out of office time")

        return False


print("\t\t\t\t\t Welcome to Healthy Programmer System ")

print("\t\t\t\tI will keep your eyes and your body healthy")

water_level = 18

water_reminder = 1200  # 20 min

eyes_reminder = 1800  # 30 min

physical_reminder = 2700  # 45 min

currenttime = time.strftime('%H:%M:%S')

previous_water_time = time.time()

previous_eye_exercise_time = time.time()

previous_physical_exercise_time = time.time()

while time_limit(currenttime):

    if water_level > 0:

        if (time.time() - previous_water_time) > water_reminder:  # water after every 20 minutes

            print("Time to drink water")

            while True:
                reminder('water.mp3', 'drank', 'water.txt')

                previous_water_time = time.time()

                water_level -= 1

                break

        if time.time() - previous_eye_exercise_time > eyes_reminder:

            print("Time to do eye exercise")

            while True:
                reminder('eyes.mp3', 'eydone', 'eyes.txt')

                previous_eye_exercise_time = time.time()

                break

        if time.time() - previous_physical_exercise_time > physical_reminder:

            print("Time to do Physical exercise")

            while True:
                reminder('physical.mp3', 'exdone', 'physical.txt')

                previous_physical_exercise_time = time.time()

                break

print("\t\t\t\t\t Bye! and Take care of your health")
