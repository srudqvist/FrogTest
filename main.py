# FrogTest main.py
# Author: Samuel Rudqvist
# Date: 24/02/2022

# Imports

#from replit import audio
import time
#from playsound import playsound
import os
import random


#The console UI
def console_user_interface():
    p0 = ("FrogSounds/Anaxyrus_americanus.mp3", "anaxyrus americanus")
    p1 = ("FrogSounds/Acris_crepitans.mp3", "acris crepitans")
    p2 = ("FrogSounds/Anaxyrus_fowleri.mp3", "anaxyrus fowleri")
    p3 = ("FrogSounds/Gastrophryne_carolinensis.mp3", "gastrophryne carolinensis")
    p4 = ("FrogSounds/Hyla_chrysoscelis_versicolor.mp3", "hyla chrysoscelis versicolor")
    p5 = ("FrogSounds/Hyla_cinerea.mp3", "hyla cinerea")
    p6 = ("FrogSounds/Lithobates_areolatus.mp3", "lithobates areolatus")
    p7 = ("FrogSounds/Lithobates_catesbeiana.mp3", "lithobates catesbeiana")
    p8 = ("FrogSounds/Lithobates_clamitans.mp3", "lithobates clamitans")
    p9 = ("FrogSounds/Lithobates_palustris.mp3", "lithobates palustris")
    p10 = ("FrogSounds/Lithobates_sphenocephalus.mp3", "lithobates sphenocephalus")
    p11 = ("FrogSounds/Lithobates_sylvatica.mp3", "lithobates sylvatica")
    p12 = ("FrogSounds/Pseudacris_crucifer.mp3", "pseudacris crucifer")
    p13 = ("FrogSounds/Pseudacris_maculata.mp3", "pseudacris maculata")
    p14 = ("FrogSounds/Scaphiopus_holbrookii.mp3", "scaphiopus holbrookii")
    
    sounds = [p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14]
    random.shuffle(sounds)
    print()
    print()

    print("Frog Sounds\n")
    user_input = str(input("Do you want to play? (y/n): ")).strip().lower()
    if "y" in user_input:
        sound_index = 0
        game_over = False
        correct = 0
        while not game_over:
            time.sleep(0.5)
            quit = False
            #source = audio.play_file(file_path, volume, does_loop, loop_count, name)
            
            # Play the sound
            startTime = time.time()
            print("")

            # Play the sound at the current sound_index from the sounds list.
            print(sound_index)
            os.system("afplay " + sounds[sound_index][0])

            # Keep the program running 
            correctBool = False
            while not quit:
                endTime = time.time()

                if not correctBool:
                    user_input = str(input("What frog was that? >>> ")).strip().lower()
                    if user_input == sounds[sound_index][1] and not correctBool:
                        correct += 1
                        print("Correct")
                        correctBool = True
                    else:
                        print("Incorrect, it was", sounds[sound_index][1])
                        correctBool = True
                else:
                    quit = True

            sound_index += 1
            if correct == 15 or sound_index == 16:
                game_over = True

        print(f"Your result: {correct}/{len(sounds)}")  
        
console_user_interface()
