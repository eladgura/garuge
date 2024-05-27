from garagebranch import add_car, del_car, print_car_info, update_car, clear_screen, save_car_info_to_json, load_car_info_from_json

car_info = load_car_info_from_json()

def display_menu():
    while True:
        clear_screen()
        print("1 - Exit")
        print("2 - Add car")
        print("3 - Update car")
        print("4 - Delete car")
        print("5 - Print all cars")

        user_selection = input("What is your selection? ")
        if user_selection == "1":
            save_car_info_to_json(car_info)
            exit()
        elif user_selection == "2":
            add_car(car_info)
        elif user_selection == "3":
            update_car(car_info)
        elif user_selection == "4":
            del_car(car_info)
        elif user_selection == "5":
            print_car_info(car_info)
        else:
            print("Please choose a valid option.")
            input("\nPress Enter to continue: ")

if __name__ == "__main__":
    clear_screen()
    display_menu()
