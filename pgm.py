"""
    Name: QuickConverter
    Description: A simple and efficient tool for converting length units.
    Date of Creation: 06/06/2024
    Last Modified On: 15/06/2024
    Creator: Navaneeth P P
    GitHub Profile: github.com/navaneethpp
    Requirements:   
        * Python 3.6,
        * os, time, itertools & sys Module
    Notes: None
    To do:
        * Documentation
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
    
# Function for exiting the program
def exit_program():
    clear_screen()
    exit = input("Are you sure you want to exit?[y/n]")
    if exit.lower() != 'n':
        print("Exiting...")
        loading_animation(0.5)
        clear_screen()
        quit()
        
# Function to handle negative measurements
def error_handler():
    print("Negative number can't be a measurement")
    loading_animation(1.3)
    clear_screen()
    
# Function for formatting the output
def format_number_with_commas(number):
    return "{:,}".format(number)

# Conversion from meter
def from_meter():
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