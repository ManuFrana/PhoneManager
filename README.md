
# December Labs Mobile Device Registration System

This program is developed to manage the registration of mobile devices used for testing client applications at December Labs. The system allows registering both regular cellphones and smartphones, storing information such as color, model, and brand for cellphones, and additionally, operating system and memory size for smartphones. The program provides functionality to register devices, list all devices, and list only smartphones, all through the console.

I decided it was best to consider some basic data persistence. So...
I also added the possibility to delete all saved mobile devices. (just in case you want to run the script multiple times)

## Getting Started

To run the program, follow these steps:

1. Clone the repository to your local machine.
2. Open the terminal and navigate to the directory where the program is cloned.
   **Note** I decided it was best to use a simple library called `tabulate`. It just helps to display the data in a more user-friendly manner :)
3. Install the dependencies listed in the requirements.txt file using a package manager of your choice. For example, if you are using pip, you can run the following command:
`pip install -r requirements.txt`
5. Run the `PhoneManager.py` script. `py PhoneManager.py` (you will need python)
5. Follow the prompts in the console to interact with the program.

## Features

- Register Cellphones: Allows registering regular cellphones with information such as color, model, and brand.
- Register Smartphones: Allows registering smartphones with information such as color, model, brand, operating system, and memory size.
- List All Devices: Displays a list of all registered devices, including cellphones and smartphones, with their respective information.
- List Smartphones Only: Displays a list of only the registered smartphones, along with their information.
- **BONUS:** Delete current save devices.
- **BONUS:** Data persistence to store registered devices across program executions.

## Improvements

There are several areas where the program could be improved, such as:

- Adding input validation to ensure the correctness and integrity of user-provided data.
  I provided with basic input validation in the menu, there are no validation what so ever in object data
- Adding error handling to gracefully handle unexpected situations during program execution.
  I tried to provide with basic error handling, this area could also be improved
- Providing a user-friendly interface with menus and options for easier interaction with the program.


