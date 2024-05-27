import json
import os

def load_car_info_from_json(filename='car_info.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON file. Starting with an empty list.")
        return []

def print_car_info(car_info):
    clear_screen()
    if not car_info:
        print("No car information available.")
    else:
        for index, car in enumerate(car_info):
            print(f'{index + 1}: year: {car["year"]}, model: {car["model"]}, color: {car["color"]}')
    input("\nPress Enter to return to the main menu: ")

def del_car(car_info, filename='car_info.json'):
    clear_screen()
    print_car_info(car_info)
    user_del_index_selected = input("Select car info to delete (or type 'exit' to go back): ")
    if user_del_index_selected.lower() == 'exit':
        return
    try:
        deleted_car = car_info.pop(int(user_del_index_selected) - 1)
        print(f'{user_del_index_selected} was deleted: {deleted_car}')
        save_car_info_to_json(car_info, filename)
    except (ValueError, IndexError):
        print("Invalid index. Please enter a valid number.")
    input("\nPress Enter to return to the delete menu: ")

def add_car(car_info, filename='car_info.json'):
    clear_screen()
    while True:
        tamp_year = input("What is the car year? (or type 'exit' to go back): ")
        if tamp_year.lower() == 'exit':
            return
        tamp_model = input("What is the car model? (or type 'exit' to go back): ")
        if tamp_model.lower() == 'exit':
            return
        tamp_color = input("What is the car color? (or type 'exit' to go back): ")
        if tamp_color.lower() == 'exit':
            return
        try:
            car_info.append({"year": int(tamp_year), "model": tamp_model, "color": tamp_color})
            save_car_info_to_json(car_info, filename)
            break
        except ValueError:
            print("Invalid input. Please enter valid car details.")
    input("\nPress Enter to return to the add menu: ")

def update_car(car_info, filename='car_info.json'):
    clear_screen()
    print_car_info(car_info)
    car_index = input("Enter the index of the car to update (or type 'exit' to go back): ")
    if car_index.lower() == 'exit':
        return
    try:
        car_index = int(car_index) - 1
        if 0 <= car_index < len(car_info):
            year = input(f"Enter the new year (current: {car_info[car_index]['year']}) (or type 'exit' to go back): ")
            if year.lower() == 'exit':
                return
            model = input(f"Enter the new model (current: {car_info[car_index]['model']}) (or type 'exit' to go back): ")
            if model.lower() == 'exit':
                return
            color = input(f"Enter the new color (current: {car_info[car_index]['color']}) (or type 'exit' to go back): ")
            if color.lower() == 'exit':
                return

            if year:
                car_info[car_index]['year'] = int(year)
            if model:
                car_info[car_index]['model'] = model
            if color:
                car_info[car_index]['color'] = color

            print("Car updated successfully!")
            save_car_info_to_json(car_info, filename)
        else:
            print("Invalid index!")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    input("\nPress Enter to return to the update menu: ")

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def save_car_info_to_json(car_info, filename='car_info.json'):
    with open(filename, 'w') as f:
        json.dump(car_info, f, indent=4)
    print(f"Car information saved to {filename}")
