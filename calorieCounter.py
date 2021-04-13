#TODO: DAY 1 - create list that contains known foods and give them set calorie amounts
#TODO: DAY 1 - create method to add calories
#TODO: DAY 1 - create method to view all food consumed
#TODO: DAY 1 - create login mechanism

import numpy as np
import time

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

food_dict = {
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
    for i in range(7):
        print("")
    print("----------------------------------------")


def login():
    # prof_check = input("Welcome to the Calorie Tracker App! Do you have an existing profile? (Y/N)\n")
    # if prof_check == "Y":
    #     print("HI")
    # elif prof_check == "N":
    #     print("Let's make you a profile!")
    #     first_name = input("Enter your first name: ")
    #     last_name = input("Enter your last name: ")
    #     new_file = open(first_name + last_name + ".txt", "w+")
    #     for i in range(10):
    #         new_file.write("This is line %d\r\n" % (i + 1))
    # else:
    #     print("Input not accepted; Restarting Process")
    #     login()

    #CHANGE: Instead of Asking for Existing Profile, ask for name and built-in open method can create new file if one does not already exist
    print("Welcome to the Calorie Tracker App!")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    new_file = open(first_name + last_name + ".txt", "w+")
    new_file.write(first_name+"\r\n") #WRITE TO A SPECIFIC LINE
    new_file.write(last_name + "\r\n")
    new_file.close()
    return first_name, last_name

first_name, last_name = login()

def add_cal():
    print_index = 1 #For printing dictionary
    for key in food_dict:
        print(str(print_index) + ". " + key)
        print_index += 1
    food_selection = input("Enter the corresponding number of your selection: ")
    for key in index_dict:
        if index_dict[key] == index_dict[int(food_selection)]:
            food_add = index_dict[key]
    file = open(first_name + last_name + "CAL.txt", "r")
    original_cal = 0
    # val_line = 0
    # for index, line in enumerate(file):
    #     if index == val_line:
    #         print(line)
    #         original_cal = float(line)
    val_line = file.readlines()
    print(val_line)
    original_cal = float(val_line[0])
    print(original_cal)
    new_cal = original_cal + food_dict[food_add]
    file = open(first_name + last_name + "CAL.txt", "w")
    file.write(str(new_cal) + "\r\n")




def main_page():
    print("What would you like to do " + first_name + "?")
    print("1. Add an Item to your total calorie count.")
    print("2. Remove an Item from your total calorie count.")
    print("3. View total calorie count for the day.")
    menu_selection = input("Enter the corresponding number to your selection (1/2/3): ")
    if int(menu_selection) == 1:
        add_cal()
    elif int(menu_selection) == 2:
        print("2 selected")
    elif int(menu_selection) == 3:
        print("3 selected")
    else:
        print("Input not Accepted. Returning to Main Menu")
        loading_screen()
        main_page()

main_page()









