"""
    Name: QuickConverter
    Description: A simple and efficient tool for converting length units.
    Date of Creation: 06/06/2024
    Last Modified On: 16/06/2024
    Creator: Navaneeth P P
    GitHub Profile: github.com/navaneethpp
    Requirements:   
        * Python 3.6,
        * os, time, itertools & sys Module
    Notes: 
        * Let me know if there is any problem
    To do:
        
"""

import os
import time
import itertools
import sys

# Loading Animation
def loading_animation(duration):
    spinner = itertools.cycle(['-', '\\', '|', '/'])
    end_time = time.time() + duration
    while time.time() < end_time:
        sys.stdout.write(next(spinner))  # Write the next character
        sys.stdout.flush()               # Flush the output to the terminal
        time.sleep(0.1)                  # Pause for a moment
        sys.stdout.write('\b')

# Function for clearing the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def exit_program():
    """
    Prompts the user to confirm if they want to exit the program and exits if confirmed.

    This function clears the screen, asks the user for confirmation to exit, and if the user
    confirms (anything other than 'n' or 'N'), it prints an exiting message, shows a loading
    animation, clears the screen again, and quits the program.

    Args:
        None

    Returns:
        None
    """
    clear_screen()
    exit = input("Are you sure you want to exit?[y/n]")
    if exit.lower() != 'n':
        print("Exiting...")
        loading_animation(0.5)
        clear_screen()
        quit()
        
def error_handler():
    """
    Handles errors related to invalid measurements.

    This function prints an error message indicating that a negative number 
    cannot be a measurement, displays a loading animation for 1.3 seconds, 
    and then clears the screen.

    Args:
        None
    """
    print("Negative number can't be a measurement")
    loading_animation(1.3)
    clear_screen()
    
# Function for formatting the output
def format_number_with_commas(number):
    return "{:,}".format(number)

def from_meter():
    """
    Converts a measurement in meters to various other units and displays the results.

    This function continuously prompts the user to input a measurement in meters,
    validates the input, and converts it to different units including kilometers, 
    centimeters, millimeters, micrometers, nanometers, miles, yards, feet, inches, 
    and light years. It handles invalid inputs and provides an option for the user 
    to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        
        clear_screen()
        print("\tQuickConvertor\t\t")
        print("\t--------------\n")
        print("\tLength -> Meter\n")
        
        try:
            print(exit)
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Kilometer: ", format_number_with_commas(measured_value / 1000))
            print("Centimeter: ", format_number_with_commas(measured_value * 100))
            print("Millimeter: ", format_number_with_commas(measured_value * 1000))
            print("Micrometer: ", format_number_with_commas(measured_value * 1000000))
            print("Nanometer: ", format_number_with_commas(measured_value * 1000000000))
            print("Mile: ", format_number_with_commas(measured_value * 0.000621371))
            print("Yard: ", format_number_with_commas(measured_value * 1.0936))
            print("Foot: ", format_number_with_commas(measured_value * 3.2808))
            print("Inch: ", format_number_with_commas(measured_value * 39.37))
            print("Light Year: ", format_number_with_commas((measured_value / 1000) * 9.461), "X 10^15 km/ly")
            print("_" * 40)
            
            decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()
        
def from_kilometer():
    """
    Converts a measurement in kilometers to various other units and displays the results.

    This function continuously prompts the user to input a measurement in kilometers,
    validates the input, and converts it to different units including meters, 
    centimeters, millimeters, micrometers, nanometers, miles, yards, feet, inches, 
    and light years. It handles invalid inputs and provides an option for the user 
    to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\tLength -> Kilometer\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue        
        
        if measured_value > 0:    
            print("Meter: ", format_number_with_commas(measured_value * 1000))
            print("Centimeter: ", format_number_with_commas(measured_value * 100000))
            print("Millimeter: ", format_number_with_commas(measured_value * 1000000))
            print("Micrometer: ", format_number_with_commas(measured_value * 1000000000))
            print("Nanometer: ", format_number_with_commas(measured_value * 10000000000000))
            print("Mile: ", format_number_with_commas(measured_value * 0.621))
            print("Yard: ", format_number_with_commas(measured_value * 1093.61))
            print("Foot: ", format_number_with_commas(measured_value * 3280.84))
            print("Inch: ", format_number_with_commas(measured_value * 39370.1))
            print("Light Year: ", format_number_with_commas(measured_value * 9.46), "X 10^12 km/ly")
            print("_" * 40)
            
            decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()

def from_centimeter():
    """
    Converts a measurement in centimeters to various other units and displays the results.

    This function continuously prompts the user to input a measurement in centimeters,
    validates the input, and converts it to different units including meters, 
    kilometers, millimeters, micrometers, nanometers, miles, yards, feet, inches, 
    and light years. It handles invalid inputs and provides an option for the user 
    to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\tLength -> Centimeter\n")
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Meter: ", format_number_with_commas(measured_value * 0.01))
            print("Kilometer: ", format_number_with_commas(measured_value * 0.00001))
            print("Millimeter: ", format_number_with_commas(measured_value * 10))
            print("Micrometer: ", format_number_with_commas(measured_value * 10000))
            print("Nanometer: ", format_number_with_commas(measured_value * 10000000))
            print("Mile: ", format_number_with_commas(measured_value * 0.0000062137))
            print("Yard: ", format_number_with_commas(measured_value * 0.010936))
            print("Foot: ", format_number_with_commas(measured_value * 0.032808))
            print("Inch: ", format_number_with_commas(measured_value * 0.393701))
            print("Light Year: ",  measured_value * 1.057 * (10 ** -18))
            print("_" * 40)
            
            decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()
    
def from_millimeter():
    """
    Converts a measurement in millimeters to various other units and displays the results.

    This function continuously prompts the user to input a measurement in millimeters,
    validates the input, and converts it to different units including meters, 
    kilometers, centimeters, micrometers, nanometers, miles, yards, feet, inches, 
    and light years. It handles invalid inputs and provides an option for the user 
    to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\tLength -> Millimeter\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Meter: ", format_number_with_commas(measured_value / 1000))
            print("Kilometer: ", format_number_with_commas(measured_value / 1000000))
            print("Centimeter: ", format_number_with_commas(measured_value / 10))
            print("Micrometer: ", format_number_with_commas(measured_value * 1000))
            print("Nanometer: ", format_number_with_commas(measured_value * 1000000000))
            print("Mile: ", format_number_with_commas(measured_value * 0.0000006213689))
            print("Yard: ", format_number_with_commas(measured_value * 0.0010936))
            print("Foot: ", format_number_with_commas(measured_value * 0.0032808))
            print("Inch: ", format_number_with_commas(measured_value * 0.03937))
            print("Light Year: ", format_number_with_commas((measured_value / 1000000) * 9.46), "X 10^12 km/ly")
            print("_" * 40)
            
            decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()

def from_micrometer():
    """
    Converts a measurement in micrometers to various other units and displays the results.

    This function continuously prompts the user to input a measurement in micrometers,
    validates the input, and converts it to different units including meters, 
    kilometers, centimeters, millimeters, nanometers, miles, yards, feet, inches, 
    and light years. It handles invalid inputs and provides an option for the user 
    to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\tLength -> Micrometer\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Meter: ", format_number_with_commas(measured_value / 1000000))
            print("Kilometer: ", format_number_with_commas((measured_value / 10000) / 1000))
            print("Centimeter: ", format_number_with_commas(measured_value / 10000))
            print("Millimeter: ", format_number_with_commas(measured_value / 1000))
            print("Nanometer: ", format_number_with_commas(measured_value * 1000))
            print("Mile: ", format_number_with_commas((measured_value * 0.0000006213689) / 1000))
            print("Yard: ", format_number_with_commas(measured_value * 0.0000000010936))
            print("Foot: ", format_number_with_commas(measured_value * 3.28084), "10^-6")
            print("Inch: ", format_number_with_commas(measured_value * 0.00003937))
            print("Light Year: ", format_number_with_commas((measured_value / 1000000000000) * 9.46), "X 10^12 km/ly")
            print("_" * 40)
            
            decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()
    
def from_nanometer():
    """
    Converts a measurement in nanometers to various other units and displays the results.

    This function continuously prompts the user to input a measurement in nanometers,
    validates the input, and converts it to different units including meters, 
    kilometers, centimeters, millimeters, micrometers, miles, yards, feet, inches, 
    and light years. It handles invalid inputs and provides an option for the user 
    to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\tLength -> Nanometer\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Meter: ", format_number_with_commas(measured_value / 1000000000))
            print("Kilometer: ", format_number_with_commas(measured_value / 1000000000000))
            print("Centimeter: ", format_number_with_commas(measured_value / 100000000))
            print("Millimeter: ", format_number_with_commas(measured_value / 1000000))
            print("Micrometer: ", format_number_with_commas(measured_value / 1000))
            print("Mile: ", format_number_with_commas((measured_value / 1000000000) * 0.000621371))
            print("Yard: ", format_number_with_commas(measured_value * 0.000000000946))
            print("Foot: ", format_number_with_commas((measured_value / 1000000000) * 1.0936))
            print("Inch: ", format_number_with_commas(measured_value * 0.00000003937))
            print("Light Year: ", format_number_with_commas((measured_value / 1000000000000) * 9.46), "X 10^12 km/ly")
            print("_" * 40)
            
            decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (decision.lower() != 'y'):
                print("Going back...")
                loading_animation(1)
                break
        elif measured_value == 0:
            continue
        else:
            error_handler()

def from_mile():
    """
    Converts a measurement in miles to various other units and displays the results.

    This function continuously prompts the user to input a measurement in miles,
    validates the input, and converts it to different units including meters, 
    kilometers, centimeters, millimeters, micrometers, nanometers, yards, feet, 
    inches, and light years. It handles invalid inputs and provides an option for 
    the user to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\tLength -> Mile\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Meter: ", format_number_with_commas(measured_value * 1609.344))
            print("Kilometer: ", format_number_with_commas(measured_value * 1.609344))
            print("Centimeter: ", format_number_with_commas(measured_value * 160934.4))
            print("Millimeter: ", format_number_with_commas(measured_value * 1609344))
            print("Micrometer: ", format_number_with_commas(measured_value * 1609344000))
            print("Nanometer: ", format_number_with_commas(measured_value * 1.609344 * (10 ** 12)))
            print("Yard: ", format_number_with_commas(measured_value * 1760))
            print("Foot: ", format_number_with_commas(measured_value * 5280))
            print("Inch: ", format(measured_value * 63360))
            print("Light Year: ", format_number_with_commas(measured_value * 1.7011), "X 10^12 km/ly")
            print("_" * 40)
            
            decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()

def from_yard():
    """
    Converts a measurement in yards to various other units and displays the results.

    This function continuously prompts the user to input a measurement in yards,
    validates the input, and converts it to different units including meters, 
    kilometers, centimeters, millimeters, micrometers, nanometers, miles, feet, 
    inches, and light years. It handles invalid inputs and provides an option for 
    the user to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\tLength -> Yard\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Meter: ", format_number_with_commas(measured_value * 0.9144))
            print("Kilometer: ", format_number_with_commas((measured_value * 0.9144) / 1000))
            print("Centimeter: ", format_number_with_commas(measured_value * 91.44))
            print("Millimeter: ", format_number_with_commas(measured_value * 914.4))
            print("Micrometer: ", format_number_with_commas(measured_value * 914400))
            print("Nanometer: ", format_number_with_commas(measured_value * 914400000))
            print("Mile: ", format_number_with_commas(measured_value / 1760))
            print("Foot: ", format_number_with_commas(measured_value * 3))
            print("Inch: ", format_number_with_commas(measured_value * 36))
            print("Light Year: ", format_number_with_commas(measured_value / 9.461), "X 10^16 km/ly")
            print("_" * 40)
            
            decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()

def from_foot():
    """
    Converts a measurement in feet to various other units and displays the results.

    This function continuously prompts the user to input a measurement in feet,
    validates the input, and converts it to different units including meters, 
    kilometers, centimeters, millimeters, micrometers, nanometers, miles, yards, 
    inches, and light years. It handles invalid inputs and provides an option for 
    the user to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\tLength -> Foot\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Meter: ", format_number_with_commas(measured_value * 0.3048))
            print("Kilometer: ", format_number_with_commas(measured_value * 0.0003048))
            print("Centimeter: ", format_number_with_commas(measured_value * 30.48))
            print("Millimeter: ", format_number_with_commas(measured_value * 304.8))
            print("Micrometer: ", format_number_with_commas(measured_value * 304800))
            print("Nanometer: ", format_number_with_commas(measured_value * 304800000))
            print("Mile: ", format_number_with_commas(measured_value / 5280))
            print("Yard: ", format_number_with_commas(measured_value / 3))
            print("Inch: ", format_number_with_commas(measured_value * 12))
            print("Light Year: ", format_number_with_commas((measured_value * 0.348) / 9.461), "X 10^16 km/ly")
            print("_" * 40)
            
            decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()

def from_inch():
    """
    Converts a measurement in inches to various other units and displays the results.

    Continuously prompts the user to input a measurement in inches, validates the input, 
    and converts it to meters, kilometers, centimeters, millimeters, micrometers, 
    nanometers, miles, yards, feet, and light years. Provides an option to continue 
    or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\tLength -> Inch\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Meter: ", format_number_with_commas(measured_value * 0.0254))
            print("Kilometer: ", format_number_with_commas((measured_value * 0.0254) / 1000))
            print("Centimeter: ", format_number_with_commas(measured_value * 2.54))
            print("Millimeter: ", format_number_with_commas(measured_value * 25.4))
            print("Micrometer: ", format_number_with_commas(measured_value * 25400))
            print("Nanometer: ", format_number_with_commas(measured_value * 25400000))
            print("Mile: ", format_number_with_commas(measured_value / 63360))
            print("Yard: ", format_number_with_commas(measured_value / 36))
            print("Foot: ", format_number_with_commas(measured_value / 12))
            print("Light Year: ", format_number_with_commas((measured_value * 0.0254) / 9.461), "X 10^16 m/ly")
            print("_" * 40)
            
            decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()    

def from_light_year():
    """
    Converts a measurement in light years to various other units and displays the results.

    Continuously prompts the user to input a measurement in light years, validates the input, 
    and converts it to meters, kilometers, centimeters, millimeters, micrometers, nanometers, 
    miles, yards, feet, and inches. Provides an option to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\tLength -> Light Year\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Meter: ", format_number_with_commas((measured_value * 9.461) * pow(10, 12)))
            print("Kilometer: ", format_number_with_commas((measured_value * 9.461) * pow(10, 12)))
            print("Centimeter: ", format_number_with_commas((measured_value * 9.461) * pow(10, 17)))
            print("Millimeter: ", format_number_with_commas((measured_value * 9.461) * pow(10, 18)))
            print("Micrometer: ", format_number_with_commas((measured_value * 9.461) * pow(10, 21)))
            print("Nanometer: ", format_number_with_commas((measured_value * 9.461) * pow(10, 24)))
            print("Mile: ", format_number_with_commas(measured_value * 5878559666946))
            print("Yard: ", format_number_with_commas((measured_value * 9.461) * pow(10, 15) * 1.09361))
            print("Foot: ", format_number_with_commas((measured_value * 9.461) * pow(10, 15) * 3.28084))
            print("Inch: ", format_number_with_commas((measured_value * 9.461) * pow(10, 15) * 39.3701))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()

def from_celsius():
    """
    Converts a temperature measurement in Celsius to Kelvin and Fahrenheit.

    Continuously prompts the user to input a temperature in Celsius, validates the input, 
    and converts it to Kelvin and Fahrenheit. Provides an option to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\tTemperature -> Celsius\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Kelvin: ", format_number_with_commas(measured_value + 273.15))
            print("Fahrenheit: ", format_number_with_commas((measured_value * 1.8) + 32))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()

def from_kelvin():
    """
    Converts a temperature measurement in Kelvin to Celsius and Fahrenheit.

    Continuously prompts the user to input a temperature in Kelvin, validates the input, 
    and converts it to Celsius and Fahrenheit. Provides an option to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\tTemperature -> Kelvin\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Celsius: ", format_number_with_commas(measured_value - 273.16))
            print("Fahrenheit: ", format_number_with_commas((1.8 * (measured_value - 273.15)) + 32))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()

def from_fahrenheit():
    """
    Converts a temperature measurement in Fahrenheit to Celsius and Kelvin.

    Continuously prompts the user to input a temperature in Fahrenheit, validates the input, 
    and converts it to Celsius and Kelvin. Provides an option to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\tTemperature -> Fahrenheit\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Celsius: ", format_number_with_commas((0.555555556 * (measured_value - 32))))
            print("Kelvin: ", format_number_with_commas((0.555555556 * (measured_value - 32)) + 273.15))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()

def from_square_meter():
    """
    Converts an area measurement in square meters to various other units.

    Continuously prompts the user to input an area in square meters, validates the input, 
    and converts it to square kilometers, square centimeters, square millimeters, square micrometers,
    hectares, square miles, square yards, square feet, square inches, and acres. 
    Provides an option to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\tArea -> Square Meter\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Square Kilometer: ", format_number_with_commas(measured_value / 1000000))
            print("Square Centimeter: ", format_number_with_commas(measured_value * 10000))
            print("Square Millimeter: ", format_number_with_commas(measured_value * 1000000))
            print("Square Micrometer: ", format_number_with_commas(measured_value * 1 * pow(10, 12)))
            print("Hectare: ", format_number_with_commas(measured_value / 10000))
            print("Square Mile: ", format_number_with_commas(measured_value / 2589988.11))
            print("Square Yard: ", format_number_with_commas(measured_value * 1.19599))
            print("Square Foot: ", format_number_with_commas(measured_value * 10.7639))
            print("Square Inch: ", format_number_with_commas(measured_value * 1550.0031))
            print("Acre: ", format_number_with_commas(measured_value / 4046.85642))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()
    
def from_square_kilometer():
    """
    Converts an area measurement in square kilometers to various other units.

    Continuously prompts the user to input an area in square kilometers, validates the input, 
    and converts it to square meters, square centimeters, square millimeters, square micrometers,
    hectares, square miles, square yards, square feet, square inches, and acres. 
    Provides an option to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\tArea -> Square Kilometer\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return
        
        if measured_value > 0:
            print("Square Meter: ", format_number_with_commas(measured_value * 1000000))
            print("Square Centimeter: ", format_number_with_commas(measured_value * pow(10, 10)))
            print("Square Millimeter: ", format_number_with_commas(measured_value * 1000000000000))
            print("Square Micrometer: ", format_number_with_commas(measured_value * 1000000000000000000))
            print("Hectare: ", format_number_with_commas(measured_value * 100))
            print("Square Mile: ", format_number_with_commas(measured_value * 0.3861018768))
            print("Square Yard: ", format_number_with_commas(measured_value * 1195990.05))
            print("Square Foot: ", format_number_with_commas(measured_value * 10763910.417))
            print("Square Inch: ", format_number_with_commas(measured_value * 1550003100))
            print("Acre: ", format_number_with_commas(measured_value * 247.105))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()

def from_square_centimeter():
    """
    Converts an area measurement in square centimeters to various other units.

    Continuously prompts the user to input an area in square centimeters, validates the input, 
    and converts it to square meters, square kilometers, square millimeters, square micrometers,
    hectares, square miles, square yards, square feet, square inches, and acres. 
    Provides an option to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\tArea -> Square Centimeter\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Square Meter: ", format_number_with_commas(measured_value / 10000))
            print("Square Kilometer: ", format_number_with_commas(measured_value / pow(10, 10)))
            print("Square Millimeter: ", format_number_with_commas(measured_value * 100))
            print("Square Micrometer: ", format_number_with_commas(measured_value * 1 * pow(10, 8)))
            print("Hectare: ", format_number_with_commas(measured_value / 100000000))
            print("Square Mile: ", format_number_with_commas(measured_value / 25899881103.36))
            print("Square Yard: ", format_number_with_commas(measured_value / 8361.2736))
            print("Square Foot: ", format_number_with_commas(measured_value / 929.0304))
            print("Square Inch: ", format_number_with_commas(measured_value / 6.4516))
            print("Acre: ", format_number_with_commas(measured_value / 40468564.2))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()

def from_square_millimeter():
    """
    Converts an area measurement in square millimeters to various other units.

    Continuously prompts the user to input an area in square millimeters, validates the input, 
    and converts it to square meters, square kilometers, square centimeters, square micrometers,
    hectares, square miles, square yards, square feet, square inches, and acres. 
    Provides an option to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\tArea -> Square Millimeter\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Square Meter: ", format_number_with_commas(measured_value / 1000000))
            print("Square Kilometer: ", format_number_with_commas(measured_value / pow(10, 12)))
            print("Square Centimeter: ", format_number_with_commas(measured_value / 100))
            print("Square Micrometer: ", format_number_with_commas(measured_value * 10 ** 6))
            print("Hectare: ", format_number_with_commas(measured_value / 10 ** 10))
            print("Square Mile: ", format_number_with_commas(measured_value / 2.58998811 * 10 ** 12))
            print("Square Yard: ", format_number_with_commas(measured_value / 836127.36))
            print("Square Foot: ", format_number_with_commas(measured_value / 92903.04))
            print("Square Inch: ", format_number_with_commas(measured_value / 645.16))
            print("Acre: ", format_number_with_commas(measured_value / 40468564.2 * 10 ** 9))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()

def from_square_micrometer():
    """
    Converts an area measurement in square micrometers to various other units.

    Continuously prompts the user to input an area in square micrometers, validates the input, 
    and converts it to square meters, square kilometers, square centimeters, square millimeters,
    hectares, square miles, square yards, square feet, square inches, and acres. 
    Provides an option to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\tArea -> Square Micrometer\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Square Meter: ", format_number_with_commas((measured_value / (10 ** 12)) * (10 ** -6)))
            print("Square Kilometer: ", format_number_with_commas((measured_value * (10 ** 12)) * (10 ** -6)))
            print("Square Centimeter: ", format_number_with_commas(measured_value / (10 ** 8)))
            print("Square Millimeter: ", format_number_with_commas(measured_value / (10 ** 6)))
            print("Hectare: ", format_number_with_commas(measured_value / (10 ** 16)))
            print("Square Mile: ", format_number_with_commas(measured_value / (2.59 * (10 **12))))
            print("Square Yard: ", format_number_with_commas(measured_value / (8.361 * (10 ** 6))))
            print("Square Foot: ", format_number_with_commas(measured_value / (9.290 * ( 10 ** 6))))
            print("Square Inch: ", format_number_with_commas(measured_value / (645.16 * (10 ** 6))))
            print("Acre: ", format_number_with_commas(measured_value / 4046860000))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()

def from_hectare():
    """
    Converts an area measurement in hectares to various other units.

    Continuously prompts the user to input an area in hectares, validates the input, 
    and converts it to square meters, square kilometers, square centimeters, square millimeters,
    square micrometers, square miles, square yards, square feet, square inches, and acres. 
    Provides an option to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\tArea -> Hectare\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Square Meter: ", format_number_with_commas(measured_value * 50000))
            print("Square Kilometer: ", format_number_with_commas(measured_value * 0.05))
            print("Square Centimeter: ", format_number_with_commas(measured_value * 500000000))
            print("Square Millimeter: ", format_number_with_commas(measured_value * 50000000000))
            print("Square Micrometer: ", format_number_with_commas(measured_value * 50000000000000000))
            print("Square Mile: ", format_number_with_commas(measured_value * 0.0193050938))
            print("Square Yard: ", format_number_with_commas(measured_value * 59799.502315))
            print("Square Foot: ", format_number_with_commas(measured_value * 538195.52084))
            print("Square Inch: ", format_number_with_commas(measured_value * 77500155))
            print("Acre: ", format_number_with_commas(measured_value * 12.355269073))
            
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()

def from_square_mile():
    """
    Converts an area measurement in square miles to various other units.

    Continuously prompts the user to input an area in square miles, validates the input, 
    and converts it to square meters, square kilometers, square centimeters, square millimeters,
    square micrometers, hectares, square yards, square feet, square inches, and acres. 
    Provides an option to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\tArea -> Square Mile\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Square Meter: ", format_number_with_commas(measured_value * 2.59 * (10 ** 6)))
            print("Square Kilometer: ", format_number_with_commas(measured_value * 2.58999))
            print("Square Centimeter: ", format_number_with_commas(measured_value * 2.58999 * (10 ** 10)))
            print("Square Millimeter: ", format_number_with_commas(measured_value * 2.58999 * (10 ** 12)))
            print("Square Micrometer: ", format_number_with_commas(measured_value * 2.58999 * (10 **18))) 
            print("Hectare: ", format_number_with_commas(measured_value * 259))
            print("Square Yard: ", format_number_with_commas(measured_value * 3097600))
            print("Square Foot: ", format_number_with_commas(measured_value * 27878400))
            print("Square Inch: ", format_number_with_commas(measured_value * 4.0144896 * (10 ** 9)))
            print("Acre: ", format_number_with_commas(measured_value * 640))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()
    
def from_square_yard():
    """
    Converts an area measurement in square yards to various other units.

    Continuously prompts the user to input an area in square yards, validates the input, 
    and converts it to square meters, square kilometers, square centimeters, square millimeters,
    square micrometers, hectares, square miles, square feet, square inches, and acres. 
    Provides an option to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\tArea -> Square Yard\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Square Meter: ", format_number_with_commas(measured_value * 0.836127))
            print("Square Kilometer: ", format_number_with_commas(measured_value * 8.361276 * (10 ** -7)))
            print("Square Centimeter: ", format_number_with_commas(measured_value * 8361.2736))
            print("Square Millimeter: ", format_number_with_commas(measured_value * 836127.36))
            print("Square Micrometer: ", format_number_with_commas(measured_value * 836127000000)) 
            print("Hectare: ", format_number_with_commas(measured_value * 0.0000836127))
            print("Square Mile: ", format_number_with_commas(measured_value * 3.228303429 * (10 ** -7)))
            print("Square Foot: ", format_number_with_commas(measured_value * 9))
            print("Square Inch: ", format_number_with_commas(measured_value * 1296))
            print("Acre: ", format_number_with_commas(measured_value * 0.000206612))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()
    
def from_square_foot():
    """
    Converts an area measurement in square feet to various other units.

    Continuously prompts the user to input an area in square feet, validates the input, 
    and converts it to square meters, square kilometers, square centimeters, square millimeters,
    square micrometers, hectares, square miles, square yards, square inches, and acres. 
    Provides an option to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\tArea -> Square Foot\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Square Meter: ", format_number_with_commas(measured_value * 0.092903))
            print("Square Kilometer: ", format_number_with_commas(measured_value * 9.2903 * (10 ** -8)))
            print("Square Centimeter: ", format_number_with_commas(measured_value * 929.0304))
            print("Square Millimeter: ", format_number_with_commas(measured_value * 92903.04))
            print("Square Micrometer: ", format_number_with_commas(measured_value * 92903040000)) 
            print("Hectare: ", format_number_with_commas(measured_value * 9.2903 * (10 ** -6)))
            print("Square Mile: ", format_number_with_commas(measured_value * 3.587 * (10 ** -8)))
            print("Square Yard: ", format_number_with_commas(measured_value * 0.111111))
            print("Square Inch: ", format_number_with_commas(measured_value * 144))
            print("Acre: ", format_number_with_commas(measured_value * 2.2957 * (10 ** -5)))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()

def from_square_inch():
    """
    Converts an area measurement in square inches to various other units.

    Continuously prompts the user to input an area in square inches, validates the input, 
    and converts it to square meters, square kilometers, square centimeters, square millimeters,
    square micrometers, hectares, square miles, square yards, square feet, and acres. 
    Provides an option to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\tArea -> Square Inch\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Square Meter: ", format_number_with_commas(measured_value * 0.00064516))
            print("Square Kilometer: ", format_number_with_commas(measured_value * 6.4516 * (10 ** -10)))
            print("Square Centimeter: ", format_number_with_commas(measured_value * 6.4516))
            print("Square Millimeter: ", format_number_with_commas(measured_value * 645.16))
            print("Square Micrometer: ", format_number_with_commas(measured_value * 645160000))
            print("Hectare: ", format_number_with_commas(measured_value * 6.4516 * (10 ** -8)))
            print("Square Mile: ", format_number_with_commas(measured_value * 2.491 * (10 ** -10)))
            print("Square Yard: ", format_number_with_commas(measured_value * 0.00694444))
            print("Square Foot: ", format_number_with_commas(measured_value * 9))
            print("Acre: ", format_number_with_commas(measured_value * 1.5942 * (10 ** -7)))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()

def from_acre():
    """
    Converts an area measurement in acres to various other units.

    Continuously prompts the user to input an area in acres, validates the input, 
    and converts it to square meters, square kilometers, square centimeters, square millimeters,
    square micrometers, hectares, square miles, square yards, square feet, and square inches. 
    Provides an option to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\tArea -> Square Acre\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Square Meter: ", format_number_with_commas(measured_value * 4046.86))
            print("Square Kilometer: ", format_number_with_commas(measured_value * 0.00404686))
            print("Square Centimeter: ", format_number_with_commas(measured_value * 40468600))
            print("Square Millimeter: ", format_number_with_commas(measured_value * 4046860000))
            print("Square Micrometer: ", format_number_with_commas(measured_value * 4046860000000)) 
            print("Hectare: ", format_number_with_commas(measured_value * 0.404686))
            print("Square Mile: ", format_number_with_commas(measured_value * 0.0015625))
            print("Square Yard: ", format_number_with_commas(measured_value * 4840))
            print("Square Foot: ", format_number_with_commas(measured_value * 43560))
            print("Square Inch: ", format_number_with_commas(measured_value * 6272640))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()
    
def from_cubic_meter():
    """
    Converts a volume measurement in cubic meters to various other units.

    Continuously prompts the user to input a volume in cubic meters, validates the input, 
    and converts it to cubic kilometers, cubic millimeters, liters, milliliters, and US gallons. 
    Provides an option to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\tVolume -> Cubic Meter\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Cubic Kilometer: ", format_number_with_commas((measured_value * 1 * (10 ** -9))))
            print("Cubic Millimeter: ", format_number_with_commas((measured_value * 1 * (10 ** 9))))
            print("Liter: ", format_number_with_commas(measured_value * 1000))
            print("Milliliter: ", format_number_with_commas((measured_value * 1 * (10 ** 6))))
            print("US Gallon: ", format_number_with_commas(measured_value * 264.172))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()

def from_cubic_kilometer():
    """
    Converts a volume measurement in cubic kilometers to various other units.

    Continuously prompts the user to input a volume in cubic kilometers, validates the input, 
    and converts it to cubic meters, cubic millimeters, liters, milliliters, and US gallons. 
    Provides an option to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\tVolume -> Cubic Kilometer\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Cubic Meter: ", format_number_with_commas(measured_value * 1 * (10 ** 9)))
            print("Cubic Millimeter: ", format_number_with_commas((measured_value * 1 * (10 ** 18))))
            print("Liter: ", format_number_with_commas(measured_value * 1 * (10 ** 12)))
            print("Milliliter: ", format_number_with_commas((measured_value * 1 * (10 ** 15))))
            print("US Gallon: ", format_number_with_commas(measured_value * 2.64172 * (10 ** 11)))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()

def from_cubic_millimeter():
    """
    Converts a volume measurement in cubic millimeters to various other units.

    Continuously prompts the user to input a volume in cubic millimeters, validates the input, 
    and converts it to cubic meters, cubic kilometers, liters, milliliters, and US gallons. 
    Provides an option to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\tVolume -> Cubic Millimeter\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Cubic Meter: ", format_number_with_commas(measured_value * 1 * (10 ** -9)))
            print("Cubic Kilometer: ", format_number_with_commas((measured_value * 1 * (10 ** -18))))
            print("Liter: ", format_number_with_commas(measured_value * 1 * (10 ** -9)))
            print("Milliliter: ", format_number_with_commas((measured_value * 1 * (10 ** -3))))
            print("US Gallon: ", format_number_with_commas(measured_value * 2.64172 * (10 ** -7)))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()
    
def from_liter():
    """
    Converts a volume measurement in liters to various other units.

    Continuously prompts the user to input a volume in liters, validates the input, 
    and converts it to cubic meters, cubic millimeters, milliliters, and US gallons. 
    Provides an option to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\tVolume -> Liter\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Cubic Meter: ", format_number_with_commas(measured_value * 0.001))
            print("Cubic Kilometer: ", format_number_with_commas((measured_value * 1 * (10 ** -12))))
            print("Cubic Millimeter: ", format_number_with_commas(measured_value * 1 * (10 ** 6)))
            print("Milliliter: ", format_number_with_commas((measured_value * 1000)))
            print("US Gallon: ", format_number_with_commas(measured_value * 0.264172))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()
    
def from_milliliter():
    """
    Converts a volume measurement in milliliters to various other units.

    Continuously prompts the user to input a volume in milliliters, validates the input, 
    and converts it to cubic meters, cubic millimeters, liters, and US gallons. 
    Provides an option to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\tVolume -> Milliliter\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Cubic Meter: ", format_number_with_commas(measured_value * 1 * (10 ** -6)))
            print("Cubic Kilometer: ", format_number_with_commas((measured_value * 1 * (10 ** -15))))
            print("Cubic Millimeter: ", format_number_with_commas(measured_value * 1000))
            print("Liter: ", format_number_with_commas(measured_value * 0.001))
            print("US Gallon: ", format_number_with_commas(measured_value * 0.000264172))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()
    
def from_us_gallon():
    """
    Converts a volume measurement in US gallons to various other units.

    Continuously prompts the user to input a volume in US gallons, validates the input, 
    and converts it to cubic meters, cubic millimeters, liters, and milliliters. 
    Provides an option to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\tVolume -> US Gallon\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Cubic Meter: ", format_number_with_commas(measured_value * 0.00378541))
            print("Cubic Kilometer: ", format_number_with_commas((measured_value * 3.78541 * (10 ** -12))))
            print("Cubic Millimeter: ", format_number_with_commas(measured_value * 3.78541 * (10 ** 6)))
            print("Liter: ", format_number_with_commas(measured_value * 3.78541))
            print("Milliliter: ", format_number_with_commas((measured_value * 3,785.41)))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()
    
def from_kilogram():
    """
    Converts a weight measurement in kilograms to various other units.

    Continuously prompts the user to input a weight in kilograms, validates the input, 
    and converts it to grams, milligrams, metric tons, pounds, carats, and atomic mass units. 
    Provides an option to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\Weight -> Kilogram\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Gram: ", format_number_with_commas(measured_value * 1000))
            print("Milligram: ", format_number_with_commas(measured_value * 1 * (10 ** 6)))
            print("Metric Ton: ", format_number_with_commas(measured_value * 0.001))
            print("Pound: ", format_number_with_commas(measured_value * 2.20462))
            print("Carrat: ", format_number_with_commas(measured_value * 5000))
            print("Atomic Mass Unit: ", format_number_with_commas(measured_value * 6.02214179 * (10 ** 26)))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()
    
def from_gram():
    """
    Converts a weight measurement in grams to various other units.

    Continuously prompts the user to input a weight in grams, validates the input, 
    and converts it to kilograms, milligrams, metric tons, pounds, carats, and atomic mass units. 
    Provides an option to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\Weight -> Gram\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Kilogram", format_number_with_commas(measured_value * 0.001))
            print("Milligram: ", format_number_with_commas(measured_value * 1000))
            print("Metric Ton: ", format_number_with_commas(measured_value * 1 * (10 ** -6)))
            print("Pound: ", format_number_with_commas(measured_value * 0.00220462))
            print("Carrat: ", format_number_with_commas(measured_value * 5))
            print("Atomic Mass Unit: ", format_number_with_commas(measured_value * 6.02214179 * (10 ** 23)))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()
    
def from_milligram():
    """
    Converts a weight measurement in milligrams to various other units.

    Continuously prompts the user to input a weight in milligrams, validates the input, 
    and converts it to kilograms, grams, metric tons, pounds, carats, and atomic mass units. 
    Provides an option to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\Weight -> Milligram\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Kilogram", format_number_with_commas(measured_value * 1 * (10 ** -6)))
            print("Gram: ", format_number_with_commas(measured_value * 0.001))
            print("Metric Ton: ", format_number_with_commas(measured_value * 1 * (10 ** -9)))
            print("Pound: ", format_number_with_commas(measured_value * 2.20462 * (10 ** -6)))
            print("Carrat: ", format_number_with_commas(measured_value * 0.005))
            print("Atomic Mass Unit: ", format_number_with_commas(measured_value * 6.02214179 * (10 ** 20)))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()
    
def from_metric_ton():
    """
    Converts a weight measurement in metric tons to various other units.

    Continuously prompts the user to input a weight in metric tons, validates the input, 
    and converts it to kilograms, grams, milligrams, pounds, carats, and atomic mass units. 
    Provides an option to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\Weight -> Metric Ton\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Kilogram", format_number_with_commas(measured_value * 1000))
            print("Gram: ", format_number_with_commas(measured_value * 1 * (10 ** 6)))
            print("Milligram: ", format_number_with_commas(measured_value * 1 * (10 ** 9)))
            print("Pound: ", format_number_with_commas(measured_value * 2204.62))
            print("Carrat: ", format_number_with_commas(measured_value * 5 * (10 ** 6)))
            print("Atomic Mass Unit: ", measured_value * 6.02214179 * (10 ** 29))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()

def from_pound():
    """
    Converts a weight measurement in pounds to various other units.

    Continuously prompts the user to input a weight in pounds, validates the input, 
    and converts it to kilograms, grams, milligrams, metric tons, carats, and atomic mass units. 
    Provides an option to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\Weight -> Pound\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Kilogram", measured_value * 0.45359237)
            print("Gram: ", measured_value * 453.59237)
            print("Milligram: ", measured_value * 453592.37)
            print("Metric Ton: ", measured_value * 0.00045359237)
            print("Carrat: ", measured_value * 2267.96185)
            print("Atomic Mass Unit: ", measured_value * 2.73159734 * (10 ** 26))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()
    
def from_carrat():
    """
    Converts a weight measurement in carats to various other units.

    Continuously prompts the user to input a weight in carats, validates the input, 
    and converts it to kilograms, grams, milligrams, metric tons, pounds, and atomic mass units. 
    Provides an option to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\Weight -> Carrat\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Kilogram", format_number_with_commas(measured_value * 0.0002))
            print("Gram: ", format_number_with_commas(measured_value * 0.2))
            print("Milligram: ", format_number_with_commas(measured_value * 200))
            print("Metric Ton: ", format_number_with_commas(measured_value * 2 * (10 ** -7)))
            print("Pound: ", format_number_with_commas(measured_value * 0.000440925))
            print("Atomic Mass Unit: ", format_number_with_commas(measured_value * 1.20442881 * (10 ** 23)))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()
    
def from_amu():
    """
    Converts a weight measurement in atomic mass units (AMU) to various other units.

    Continuously prompts the user to input a weight in AMU, validates the input, 
    and converts it to kilograms, grams, milligrams, metric tons, pounds, and carats. 
    Provides an option to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\Weight -> Atomic Mass Unit\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Kilogram", format_number_with_commas(measured_value * 1.66053906660 * (10 ** -27)))
            print("Gram: ", format_number_with_commas(measured_value * 1.66053906660 * (10 ** -24)))
            print("Milligram: ", format_number_with_commas(measured_value * 1.66053906660 * (10 ** -21)))
            print("Metric Ton: ", format_number_with_commas(measured_value * 1.66053906660 * (10 ** -30)))
            print("Pound: ", format_number_with_commas(measured_value * 3.660867 * (10 ** -27)))
            print("Carrat: ", format_number_with_commas(measured_value * 8.3027 * (10 ** -23)))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()
    
def from_second():
    """
    Converts a time measurement in seconds to various other time units.

    Continuously prompts the user to input a time in seconds, validates the input, 
    and converts it to milliseconds, microseconds, nanoseconds, minutes, hours, days, 
    weeks, months (assuming 30.4375 days in a month), and years. 
    Provides an option to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\Time -> Second\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("\tTime -> Second\n")
            print("Millisecond: ", format_number_with_commas(measured_value * 1000))
            print("Microsecond: ", format_number_with_commas(measured_value * 1000000))
            print("Nanosecond: ", format_number_with_commas(measured_value * 1000000000))
            print("Minute: ", format_number_with_commas(measured_value / 60))
            print("Hour: ", format_number_with_commas(measured_value / 3600))
            print("Day: ", format_number_with_commas(measured_value / 86400))
            print("Week: ", format_number_with_commas(measured_value / 604800))
            print("Month: ", format_number_with_commas(measured_value / 2629746))
            print("Year: ", format_number_with_commas(measured_value / 31557600))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()
    
def from_millisecond():
    """
    Converts a time measurement in milliseconds to various other time units.

    Continuously prompts the user to input a time in milliseconds, validates the input, 
    and converts it to seconds, microseconds, nanoseconds, minutes, hours, days, 
    weeks, months (assuming 30.4375 days in a month), and years. 
    Provides an option to continue or exit the conversion process.

    Args:
        None

    Returns:
        None
    """
    while True:
        clear_screen()
        print("\tTime -> Millisecond\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Second: ", format_number_with_commas(measured_value / 1000))
            print("Microsecond: ", format_number_with_commas(measured_value * 1000))
            print("Nanosecond: ", format_number_with_commas(measured_value * 1000000))
            print("Minute: ", format_number_with_commas(measured_value / 60000))
            print("Hour: ", format_number_with_commas(measured_value / 3600000))
            print("Day: ", format_number_with_commas(measured_value / 86400000))
            print("Week: ", format_number_with_commas(measured_value / 604800000))
            print("Month: ", format_number_with_commas(measured_value / 2629746000))
            print("Year: ", format_number_with_commas(measured_value / 31557600000))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()
    
def from_microsecond(measured_value):
    """
    Converts a measurement from microseconds to seconds, milliseconds,
    nanoseconds, minutes, hours, days, weeks, months, and years.

    Continues to prompt for input until the user chooses to exit.

    Args:
    - measured_value (float): The measurement in microseconds.

   Returns:
    - None

    """
    while True:
        clear_screen()
        print("\tTime -> Microsecond\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Second: ", format_number_with_commas(measured_value / 1000000))
            print("Millisecond: ", format_number_with_commas(measured_value / 1000))
            print("Nanosecond: ", format_number_with_commas(measured_value * 1000))
            print("Minute: ", format_number_with_commas(measured_value / 60000000))
            print("Hour: ", format_number_with_commas(measured_value / 3600000000))
            print("Day: ", format_number_with_commas(measured_value / 86400000000))
            print("Week: ", format_number_with_commas(measured_value / 604800000000))
            print("Month: ", format_number_with_commas(measured_value / 2629746000000))
            print("Year: ", format_number_with_commas(measured_value / 31557600000000))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()

def from_nanosecond(measured_value):
    """
    Converts a measurement from nanoseconds to various units of time.

    Continues to prompt for input until the user chooses to exit.

    Args:
    - measured_value (float): The measurement in nanoseconds.

    Returns:
    - None
    """
    while True:
        clear_screen()
        print("\tTime -> Nanosecond\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Second: ",format_number_with_commas(measured_value / 1000000000))
            print("Millisecond: ", format_number_with_commas(measured_value / 1000000))
            print("Microsecond: ", format_number_with_commas(measured_value / 1000))
            print("Minute: ", format_number_with_commas(measured_value / 60000000000))
            print("Hour: ", format_number_with_commas(measured_value / 3600000000000))
            print("Day: ", format_number_with_commas(measured_value / 86400000000000))
            print("Week: ", format_number_with_commas(measured_value / 604800000000000))
            print("Month: ", format_number_with_commas(measured_value / 2629746000000000))
            print("Year: ", format_number_with_commas(measured_value / 31557600000000000))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()
    
def from_minute(measured_value):
    """
    Converts a measurement from minutes to various units of time.

    Continues to prompt for input until the user chooses to exit.

    Args:
    - measured_value (float): The measurement in minutes.

    Return:
    - None
    """
    while True:
        clear_screen()
        print("\tTime -> Minute\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Second: ", format_number_with_commas(measured_value * 60))
            print("Millisecond: ", format_number_with_commas(measured_value * 60000))
            print("Microsecond: ", format_number_with_commas(measured_value * 60000000))
            print("Nanosecond: ", format_number_with_commas(measured_value * 60000000000))
            print("Hour: ", format_number_with_commas(measured_value / 60))
            print("Day: ", format_number_with_commas(measured_value / 1440))
            print("Week: ", format_number_with_commas(measured_value / 10080))
            print("Month: ", format_number_with_commas(measured_value / 43830))
            print("Year: ", format_number_with_commas(measured_value / 525600))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()
    
def from_hour(measured_value):
    """
    Converts a measurement from hours to various units of time.

    Continues to prompt for input until the user chooses to exit.

    Args:
    - measured_value (float): The measurement in hours.

    Returns:
    - None
    """
    while True:
        clear_screen()
        print("\tTime -> Hour\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Second: ", format_number_with_commas(measured_value * 3600))
            print("Millisecond: ", format_number_with_commas(measured_value * 3.6 * (10 ** 6)))
            print("Microsecond: ", format_number_with_commas(measured_value * 3.6 * (10 ** 9)))
            print("Nanosecond: ", format_number_with_commas(measured_value * 3.6 * (10 ** 12)))
            print("Minute: ", format_number_with_commas(measured_value * 60))
            print("Day: ", format_number_with_commas(measured_value / 24))
            print("Week: ", format_number_with_commas(measured_value / 168))
            print("Month: ", format_number_with_commas(measured_value / 730.5))
            print("Year: ", format_number_with_commas(measured_value / 8766))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()
    
def from_day(measured_value):
    """
    Converts a measurement from days to various units of time.

    Continues to prompt for input until the user chooses to exit.

    Args:
    - measured_value (float): The measurement in days.

    Returns:
    - None
    """
    while True:
        clear_screen()
        print("\tTime -> Day\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Second: ", format_number_with_commas(measured_value * 86400))
            print("Millisecond: ", format_number_with_commas(measured_value * 8.64 * (10 ** 7)))
            print("Microsecond: ", format_number_with_commas(measured_value * 8.64 * (10 ** 10)))
            print("Nanosecond: ", format_number_with_commas(measured_value * 8.64 * (10 ** 13)))
            print("Minute: ", format_number_with_commas(measured_value * 1440))
            print("Hour: ", format_number_with_commas(measured_value * 24))
            print("Week: ", format_number_with_commas(measured_value / 7))
            print("Month: ", format_number_with_commas(measured_value / 30.44))
            print("Year: ", format_number_with_commas(measured_value / 365.25))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()
    
def from_week(measured_value):
    """
    Converts a measurement from weeks to various units of time.

    Continues to prompt for input until the user chooses to exit.

    Args:
    - measured_value (float): The measurement in weeks.

    Return:
    - None
    """
    while True:
        clear_screen()
        print("\tTime -> Week\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Second: ",format_number_with_commas(measured_value * 604800))
            print("Millisecond: ", format_number_with_commas(measured_value * 6.048 * (10 ** 8)))
            print("Microsecond: ", format_number_with_commas(measured_value * 6.048 * (10 ** 11)))
            print("Nanosecond: ", format_number_with_commas(measured_value * 6.048 * (10 ** 14)))
            print("Minute: ", format_number_with_commas(measured_value * 10080))
            print("Hour: ", format_number_with_commas(measured_value * 168))
            print("Day: ", format_number_with_commas(measured_value * 7))
            print("Month: ", format_number_with_commas(measured_value / 434524))
            print("Year: ", format_number_with_commas(measured_value / 52.1429))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()
    
def from_month(measured_value):
    """
    Converts a measurement from months to various units of time.

    Continues to prompt for input until the user chooses to exit.

    Args:
    - measured_value (float): The measurement in months.

    Return:
    - None
    """
    while True:
        clear_screen()
        print("\tTime -> Month\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Second: ", format_number_with_commas(measured_value * 30.44 * 24 * 60 * 60))
            print("Millisecond: ", format_number_with_commas(measured_value * 30.44 * 24 * 60 * 60 * (10 ** 3)))
            print("Microsecond: ", format_number_with_commas(measured_value * 30.44 * 24 * 60 * 60 * (10 ** 6)))
            print("Nanosecond: ", format_number_with_commas(measured_value * 30.44 * 24 * 60 * 60 * (10 ** 9)))
            print("Minute: ", format_number_with_commas(measured_value * 30.44 * 24 * 60))
            print("Hour: ", format_number_with_commas(measured_value * 30.44 * 24))
            print("Day: ", format_number_with_commas(measured_value * 30.44))
            print("Week: ", format_number_with_commas(measured_value * 4.34524))
            print("Year: ", format_number_with_commas(measured_value / 12))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()
    
def from_year(measured_value):
    """
    Converts a measurement from years to various units of time.

    Continues to prompt for input until the user chooses to exit.

    Args:
    - measured_value (float): The measurement in years.

    Returns:
    - None
    """
    while True:
        clear_screen()
        print("\tTime -> Year\n")
        
        try:
            measured_value = float(input("Enter the measurement: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_value > 0:
            print("Second: ", format_number_with_commas(measured_value * 365.25 * 24 * 60 * 60))
            print("Millisecond: ", format_number_with_commas(measured_value * 365.25 * 24 * 60 * 60 * (10 ** 3)))
            print("Microsecond: ", format_number_with_commas(measured_value * 365.25 * 24 * 60 * 60 * (10 ** 6)))
            print("Nanosecond: ", format_number_with_commas(measured_value * 365.25 * 24 * 60 * 60 * (10 ** 9)))
            print("Minute: ", format_number_with_commas(measured_value * 365.25 * 24 * 60))
            print("Hour: ", format_number_with_commas(measured_value * 365.25 * 24))
            print("Day: ", format_number_with_commas(measured_value * 365.25))
            print("Week: ", format_number_with_commas(measured_value * 52.1429))
            print("Month: ", format_number_with_commas(measured_value * 12))
            print("_" * 40)
            
            user_decision = input("If you want continue in here then press 'y'. Other wise it's goes to back: ")
            if (user_decision.lower() != 'y'):
                break
        elif measured_value == 0:
            print("Cannot convert 0 to other units")
            loading_animation(1)
            continue
        else:
            error_handler()

def length():
    """
    Prompts the user to select a unit of length and calls the corresponding conversion function.

    Continues to prompt for input until the user chooses to exit or go back to the previous menu.

    Return:
    - None
    """
    while True:
        clear_screen()
        print("\tLength ->\n")
        print("Choose measured value unit")
        print("1. Meter\n2. Kilometer\n3. Centimeter\n4. Millimeter\n5. Micrometer\n6. Nanometer\n7. Mile\n8. Yard\n9. Foot\n10. Inch\n11. Light Year\n12.Back\n0. Exit\n")
        
        try:
            measured_unit = int(input("Enter the value: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1)
            continue
        
        if measured_unit != 0:
                
            if (measured_unit == 1):
                from_meter()
            elif (measured_unit == 2):
                from_kilometer()
            elif (measured_unit == 3):
                from_centimeter()
            elif (measured_unit == 4):
                from_millimeter()
            elif (measured_unit == 5):
                from_micrometer()
            elif (measured_unit == 6):
                from_nanometer()
            elif (measured_unit == 7):
                from_mile()
            elif (measured_unit == 8):
                from_yard()
            elif (measured_unit == 9):
                from_foot()
            elif (measured_unit == 10):
                from_inch()
            elif (measured_unit == 11):
                from_light_year()
            elif measured_unit == 12:
                break
            else:
                print("Unknown option. Please try again!")
                loading_animation(1.5)
                continue
        else:
            exit_program()

def temperature():
    """
    Prompts the user to select a unit of temperature and calls the corresponding conversion function.

    Continues to prompt for input until the user chooses to exit or go back to the previous menu.

    Return:
    - None
    """
    while True:
        clear_screen()
        print("\tTemperature->\n")
        print("Choose measured value unit")
        print("1. Celsius\n2. Kelvin\n3. Fahrenheit\n4. Back\n0. Exit")
        
        try:
            measured_unit = int(input("Enter the value: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1.5)
            continue
        
        if measured_unit != 0:
            if (measured_unit == 1):
                from_celsius()
            elif (measured_unit == 2):
                from_kelvin()
            elif (measured_unit == 3):
                from_fahrenheit()
            elif measured_unit == 4:
                break
            else:
                print("Unknown option. Please try again!")
                loading_animation(1.5)
                continue
        else:
            exit_program()

def area():
    """
    Prompts the user to select a unit of area and calls the corresponding conversion function.

    Continues to prompt for input until the user chooses to exit or go back to the previous menu.

    Return:
    - None
    """
    while True:
        clear_screen()
        print("\tArea -> \n")
        print("Choose measured value unit")
        print("1. Square Meter\n2. Square Kilometer\n3. Square Centimeter\n4. Square Millimeter\n5. Square Micrometer\n6. Hectare\n7. Square Mile\n8. Square Yard\n9. Square Foot\n10. Square Inch\n11. Acre\n12.Back\n0. Exit")
        
        try:
            measured_unit = int(input("Enter the value: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1.5)
            continue
            
        if measured_unit != 0:        
            if (measured_unit == 1):
                from_square_meter()
            elif (measured_unit == 2):
                from_square_kilometer()
            elif (measured_unit == 3):
                from_square_centimeter()
            elif (measured_unit == 4):
                from_square_millimeter()
            elif (measured_unit == 5):
                from_square_micrometer()
            elif (measured_unit == 6):
                from_hectare()
            elif (measured_unit == 7):
                from_square_mile()
            elif (measured_unit == 8):
                from_square_yard()
            elif (measured_unit == 9):
                from_square_foot()
            elif (measured_unit == 10):
                from_square_inch()
            elif (measured_unit == 11):
                from_acre()
            elif measured_unit == 12:
                break
            else:
                print("Unknown option. Please try again!")
                loading_animation(1.5)
                continue
        else:
            exit_program()

def volume():
    """
    Prompts the user to select a unit of volume and calls the corresponding conversion function.

    Continues to prompt for input until the user chooses to exit or go back to the previous menu.

    Return:
    - None
    """
    while True:
        clear_screen()
        print("\tVolume -> \n")
        print("Choose measured value unit")
        print("1. Cubic Meter\n2. Cubic Kilometer\n3. Cubic Millimeter\n4. Liter\n5. Milliliter\n6. US Gallon\n7.Back\n0. Exit")
        
        try:
            measured_unit = int(input("Enter the value: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1.5)
            continue
        
        if measured_unit != 0:        
            if measured_unit == 1:
                from_cubic_meter()
            elif measured_unit == 2:
                from_cubic_kilometer()
            elif measured_unit == 3:
                from_cubic_millimeter()
            elif measured_unit == 4:
                from_liter()
            elif measured_unit == 5:
                from_milliliter()
            elif measured_unit == 6:
                from_us_gallon()
            elif measured_unit == 7:
                break
            else:
                print("Unknown option. Please try again!")
                loading_animation(1.5)
                continue
        else:
            exit_program()

def weight():
    """
    Prompts the user to select a unit of weight and calls the corresponding conversion function.

    Continues to prompt for input until the user chooses to exit or go back to the previous menu.

    Return:
    - None
    """
    while True:
        clear_screen()
        print("\tWeight -> \n")
        print("Choose measured value unit")
        print("1. Kilogram\n2. Gram\n3. Milligram\n4. Metric Ton\n5. Pound\n6. Carrat\n7. Atomic Mass Unit\n8. Back\n0. Exit")
        
        try:
            measured_unit = int(input("Enter the value: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1.5)
            continue
            
        if measured_unit != 0:        
            if (measured_unit == 1):
                from_kilogram()
            elif (measured_unit == 2):
                from_gram()
            elif measured_unit == 3:
                from_milligram()
            elif measured_unit == 4:
                from_metric_ton()
            elif measured_unit == 5:
                from_pound()
            elif measured_unit == 6:
                from_carrat()
            elif measured_unit == 7:
                from_amu()
            elif measured_unit == 8:
                break
            else:
                print("Unknown option. Please try again!")
                loading_animation(1.5)
                continue
        else:
            exit_program()
        
def time_conversion():
    """
    Prompts the user to select a unit of time and calls the corresponding conversion function.

    Continues to prompt for input until the user chooses to exit or go back to the previous menu.

    Return:
    - None
    """
    while True:
        print("\tTime ->\n")
        print("Choose measured value unit")
        print("1. Second\n2. Millisecond\n3. Microsecond\n4. Nanosecond\n5. Minute\n6. Hour\n7. Day\n8. Week\n9. Month\n10. Year\n11. Back\n0. Exit")
        
        try:
            measured_unit = int(input("Enter the value: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            loading_animation(1.5)
            continue
        
        if measured_unit != 0:
            if measured_unit == 1:
                from_second()
            elif measured_unit == 2:
                from_millisecond()
            elif measured_unit == 3:
                from_microsecond()
            elif measured_unit == 4:
                from_nanosecond()
            elif measured_unit == 5:
                from_minute()
            elif measured_unit == 6:
                from_hour()
            elif measured_unit == 7:
                from_day()
            elif measured_unit == 8:
                from_week()
            elif measured_unit == 9:
                from_month()
            elif measured_unit == 10:
                from_year()
            elif measured_unit == 11:
                break
            else:
                print("Unknown option. Please try again!")
                loading_animation(1.5)
                continue
        else:
            exit_program()


option = 1
while (True):
    clear_screen()
    print("\tQuickConvertor\t\t")
    print("\t--------------\n")
    print("1. Length\n2. Temperature\n3. Area\n4. Volume\n5. Weight\n6. Time\n0. Exit")
    
    try:
        option = int(input("Enter your choice: "))
        clear_screen()
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        loading_animation(1.5)
        clear_screen()
        continue
    
    if option == 1:
        length()
        print("\n")
    elif option == 2:
        temperature()
        print("\n")
    elif option == 3:
        area()
        print("\n")
    elif option == 4:
        volume()
        print("\n")
    elif option == 5:
        weight()
        print("\n")
    elif option == 6:
        time_conversion()
        print("\n")
    elif option == 0:
        exit_program()
    else:
        print("Unknown option. Please try again!...")
        loading_animation(1)
