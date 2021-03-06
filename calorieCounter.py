import numpy as np
import time
import os

dir = "Profiles"
orig_dir = "/Users/**********/PycharmProjects/CalorieCounter/" #ASTERISKS ARE FOR MY NAME (FILE PATH FOR PROFILES FOLDER)
path = os.path.join(orig_dir, dir)

try:
    os.mkdir(path)
except FileExistsError:
    print("")

index_dict = {
    1 : "almond",
    2 : "energy bar",
    3 : "carrot",
    4 : "chicken breast",
    5 : "bacon",
    6 : "slice of bread",
    7 : "1 cup of rice",
    8 : "egg",
    9 : "apple",
    10 : "avocado",
    11 : "banana",
    12 : "1 cup of blueberries"
}

food_dict = { #All calorie values found on google
    "almond" : 8.15,
    "energy bar" : 140,
    "carrot" : 25,
    "chicken breast" : 231,
    "bacon" : 43,
    "slice of bread" : 79,
    "1 cup of rice" : 206,
    "egg" : 78,
    "apple" : 95,
    "avocado" : 234,
    "banana" : 105,
    "1 cup of blueberries" : 85
}

def print_dict(dic):
    print_index = 1
    for key in dic:
        print(str(print_index) + ". " + key)
        print_index += 1

def loading_screen():
    rand_int = np.random.randint(30)
    for i in range(4):
        print(".", end="")
        time.sleep(0.3)
    print(str(rand_int)+"%", end="")
    for i in range(7):
        print(".", end="")
        time.sleep(0.2)
    rand_int2 = np.random.randint(30, 60)
    fin_num = rand_int+rand_int2
    print(str(fin_num)+"%", end="")
    for i in range(5):
        print(".", end="")
        time.sleep(0.3)
    print("100%")
    print("----------------------------------------")


def login():
    print("Welcome to the Calorie Tracker App!")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    new_file = open("Profiles/" + first_name + last_name + ".txt", "w+")
    new_file.write(first_name+"\r\n") #WRITE TO A SPECIFIC LINE
    new_file.write(last_name + "\r\n")
    new_file.close()
    return first_name, last_name

first_name, last_name = login()

def add_cal(food_add, food_selection):
    try:
        file = open("Profiles/" + first_name + last_name + "CAL.txt", "r")
        val_line = file.readlines()
        original_cal = float(val_line[0])
        new_cal = original_cal + food_dict[food_add]
        file = open("Profiles/" + first_name + last_name + "CAL.txt", "w")
        file.write(str(new_cal) + "\r\n")
    except FileNotFoundError:
        file = open("Profiles/" + first_name + last_name + "CAL.txt", "w+")
        original_cal = 0
        new_cal = original_cal + food_dict[food_add]
        file.write(str(new_cal) + "\r\n")
    finally:
        file.close()

    try:
        with open("Profiles/" + first_name + last_name + "FOOD.txt", "a") as file:
            file.write("\n")
            file.write(index_dict[int(food_selection)])
    except FileNotFoundError:
        file = open("Profiles/" + first_name + last_name + "FOOD.txt", "w+")
        file.write(index_dict[int(food_selection)] + "\n")
    finally:
        file.close()

    loading_screen()
    print()
    main_page()

def remove_cal(food_remove, food_selection):
    try:
        with open("Profiles/" + first_name + last_name + "FOOD.txt", "r") as file: #FIX TO CHECK FOR FOOD
            for line in file:
                str_line = line.strip()
                if str_line == index_dict[int(food_selection)]:
                    remove = 1
                    break
                else:
                    remove = 0
    except FileNotFoundError:
        print("Your profile is new. No calories have been added as yet.")
        print("Returning to main menu")
        loading_screen()
        main_page()
    finally:
        file.close()

    if remove == 1:
        file = open("Profiles/" + first_name + last_name + "CAL.txt", "r")
        val_line = file.readlines()
        original_cal = float(val_line[0])
        new_cal = original_cal - food_dict[food_remove]
        file = open("Profiles/" + first_name + last_name + "CAL.txt", "w")
        file.write(str(new_cal) + "\r\n")
        file.close()

        file = open("Profiles/" + first_name + last_name + "FOOD.txt", "r")
        food_lines = file.readlines()
        file.close()
        file = open("Profiles/" + first_name + last_name + "FOOD.txt", "w")
        for line in food_lines:
            if line.strip("\n") != index_dict[int(food_selection)]:
                file.write(line)
        file.close()

    if remove == 0:
        print("Sorry, the food you wish to remove is not in your profile")
        print("Please try again with a food you have already consumed")
        temp = input("Press enter to return to the main menu.")

    loading_screen()
    print()
    main_page()

def show_cal():
    try:
        file = open("Profiles/" + first_name + last_name + "CAL.txt", "r")
        val_line = file.readlines()
        print("Today you have consumed ", val_line[0].strip(), " calories.")
        temp = input("Press enter to return to the main menu.")
        loading_screen()
        main_page()
    except FileNotFoundError:
        print("Your profile is new. No calories have been added as yet.")
        print("Returning to main menu")
        loading_screen()
        print()
        main_page()

def prompt_food():
    print_dict(food_dict)
    food_selection = input("Enter the corresponding number of your selection: ")
    for key in index_dict:
        if index_dict[key] == index_dict[int(food_selection)]:
            food_add = index_dict[key]
    return food_add, food_selection

def main_page():
    print("What would you like to do " + first_name + "?")
    print("1. Add an Item to your total calorie count.")
    print("2. Remove an Item from your total calorie count.")
    print("3. View total calorie count for the day.")
    menu_selection = input("Enter the corresponding number to your selection (1/2/3): ")
    if int(menu_selection) == 1:
        food_add, food_selection = prompt_food()
        add_cal(food_add, food_selection)
    elif int(menu_selection) == 2:
        food_remove, food_selection = prompt_food()
        remove_cal(food_remove, food_selection)
    elif int(menu_selection) == 3:
        show_cal()
    else:
        print("Input not Accepted. Returning to Main Menu")
        loading_screen()
        main_page()

main_page()









