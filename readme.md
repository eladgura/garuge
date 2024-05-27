# Car Management System

The Car Management System is a command-line interface (CLI) tool for managing car information. This system allows users to add, update, delete, and view car details, with all information being saved to a JSON file for persistence.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Running the Application](#running-the-application)
- [File Structure](#file-structure)
- [Function Descriptions](#function-descriptions)
  - [garagebranch.py](#garagebranchpy)
  - [main.py](#mainpy)
- [Usage](#usage)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

- Python 3.x
- Visual Studio Code (optional but recommended for an enhanced development experience)

## Setup

1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-repository/car-management-system.git
   cd car-management-system
   ```

2. **Create a virtual environment**:
   ```sh
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

4. **Install required packages**:
   ```sh
   pip install -r requirements.txt
   ```

## Running the Application

1. **Open Visual Studio Code** (or your preferred IDE).
2. **Open the folder** containing the project files.
3. **Open a terminal** in Visual Studio Code (Ctrl + `) and ensure your virtual environment is activated.
4. **Run the application**:
   ```sh
   python main.py
   ```

## File Structure

- `main.py`: The main entry point for the application, providing the main menu and handling user inputs.
- `garagebranch.py`: Contains all functions related to car management (add, update, delete, print) and utility functions (load, save, clear screen).

## Function Descriptions

### garagebranch.py

#### `load_car_info_from_json(filename='car_info.json')`
- **Description**: Loads car information from a JSON file.
- **Parameters**: 
  - `filename`: The name of the JSON file (default is 'car_info.json').
- **Returns**: A list of car information dictionaries.

#### `print_car_info(car_info)`
- **Description**: Prints the list of car information.
- **Parameters**: 
  - `car_info`: A list of car information dictionaries.

#### `del_car(car_info, filename='car_info.json')`
- **Description**: Deletes a car from the list based on user input.
- **Parameters**: 
  - `car_info`: A list of car information dictionaries.
  - `filename`: The name of the JSON file (default is 'car_info.json').

#### `add_car(car_info, filename='car_info.json')`
- **Description**: Adds a new car to the list based on user input.
- **Parameters**: 
  - `car_info`: A list of car information dictionaries.
  - `filename`: The name of the JSON file (default is 'car_info.json').

#### `update_car(car_info, filename='car_info.json')`
- **Description**: Updates an existing car's information based on user input.
- **Parameters**: 
  - `car_info`: A list of car information dictionaries.
  - `filename`: The name of the JSON file (default is 'car_info.json').

#### `clear_screen()`
- **Description**: Clears the terminal screen.
- **Parameters**: None.

#### `save_car_info_to_json(car_info, filename='car_info.json')`
- **Description**: Saves the car information to a JSON file.
- **Parameters**: 
  - `car_info`: A list of car information dictionaries.
  - `filename`: The name of the JSON file (default is 'car_info.json').

### main.py

#### `display_menu()`
- **Description**: Displays the main menu and handles user input for different operations (add, update, delete, print).
- **Parameters**: None.

## Usage

1. **Add a Car**:
   - Choose option `2` from the main menu.
   - Enter the car's year, model, and color when prompted.

2. **Update a Car**:
   - Choose option `3` from the main menu.
   - Enter the index of the car to update.
   - Enter the new details for the car.

3. **Delete a Car**:
   - Choose option `4` from the main menu.
   - Enter the index of the car to delete.

4. **Print All Cars**:
   - Choose option `5` from the main menu to view all car information.

5. **Exit**:
   - Choose option `1` from the main menu to save changes and exit the application.

## Error Handling

- Invalid inputs for indices or car details are handled gracefully with appropriate error messages and prompts for re-entry.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests. Please ensure to follow the project's coding standards and guidelines.

## License

This project is licensed under the MIT License.

---

This README provides a comprehensive guide to setting up and using the Car Management System. It includes instructions for initializing the virtual environment, running the application, and detailed descriptions of each function and their usage.