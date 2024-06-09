"""
    Name: QuickConverter
    Description: A simple and efficient tool for converting length units.
    Date of Creation: 06/06/2024
    Last Modified On: 09/06/2024
    Creator: Navaneeth P P
    GitHub Profile: github.com/navaneethpp
    Requirements:   
                * Python 3.6,
                * OS Module
    Notes: None
    To do:
        * Back Button
        * Negative Measurements
        * Exit conformation
"""

import os

# Function for clearing the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
# Function for exiting the program
def exit_program():
    clear_screen()
    print("Exiting...\n")
    quit()

def from_meter():
    clear_screen()
    print("\tLength -> Meter\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Kilometer: ", measured_value / 1000)
    print("Centimeter: ", measured_value * 100)
    print("Millimeter: ", measured_value * 1000)
    print("Micrometer: ", measured_value * 1000000)
    print("Nanometer: ", measured_value * 1000000000)
    print("Mile: ", measured_value * 0.000621371)
    print("Yard: ", measured_value * 1.0936)
    print("Foot: ", measured_value * 3.2808)
    print("Inch: ", measured_value * 39.37)
    print("Light Year: ", (measured_value / 1000) * 9.461, "X 10^15 km/ly")

def from_kilometer():
    clear_screen()
    print("\tLength -> Kilometer\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Meter: ", measured_value * 1000)
    print("Centimeter: ", measured_value * 100000)
    print("Millimeter: ", measured_value * 1000000)
    print("Micrometer: ", measured_value * 1000000000)
    print("Nanometer: ", measured_value * 10000000000000)
    print("Mile: ", measured_value * 0.621)
    print("Yard: ", measured_value * 1093.61)
    print("Foot: ", measured_value * 3280.84)
    print("Inch: ", measured_value * 39370.1)
    print("Light Year: ", measured_value * 9.46, "X 10^12 km/ly")

def from_centimeter():
    clear_screen()
    print("\tLength -> Centimeter\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Meter: ", measured_value / 100)
    print("Kilometer: ", measured_value / 100000)
    print("Millimeter: ", measured_value * 10)
    print("Micrometer: ", measured_value * 10000000)
    print("Nanometer: ", measured_value * 10000000000)
    print("Mile: ", measured_value * 0.0006213689)
    print("Yard: ", measured_value * 1.0936132983)
    print("Foot: ", measured_value * 0.0328)
    print("Inch: ", measured_value * 0.3937)
    print("Light Year: ", measured_value * 0.0000000946)
    
def from_millimeter():
    clear_screen()
    print("\tLength -> Millimeter\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Meter: ", measured_value / 1000)
    print("Kilometer: ", measured_value / 1000000)
    print("Centimeter: ", measured_value / 10)
    print("Micrometer: ", measured_value * 1000)
    print("Nanometer: ", measured_value * 1000000000)
    print("Mile: ", measured_value * 0.0000006213689)
    print("Yard: ", measured_value * 0.00010936)
    print("Foot: ", measured_value * 0.0032808)
    print("Inch: ", measured_value * 0.03937)
    print("Light Year: ", (measured_value / 1000000) * 9.46, "X 10^12 km/ly")

def from_micrometer():
    clear_screen()
    print("\tLength -> Micrometer\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Meter: ", measured_value / 1000000)
    print("Kilometer: ", (measured_value / 10000) / 1000 )
    print("Centimeter: ", measured_value / 10000)
    print("Millimeter: ", measured_value / 1000)
    print("Nanometer: ", measured_value * 1000)
    print("Mile: ", (measured_value * 0.0000006213689) / 1000)
    print("Yard: ", measured_value * 0.0000000010936)
    print("Foot: ", measured_value * 3.28084, "10^-6")
    print("Inch: ", measured_value * 0.00003937)
    print("Light Year: ", (measured_value / 1000000000000) * 9.46, "X 10^12 km/ly")
    
def from_nanometer():
    clear_screen()
    print("\tLength -> Nanometer\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Meter: ", measured_value / 1000000000)
    print("Kilometer: ", measured_value / 1000000000000)
    print("Centimeter: ", measured_value / 100000000)
    print("Millimeter: ", measured_value / 1000)
    print("Micrometer: ", measured_value / 1000)
    print("Mile: ", (measured_value / 1000000000) * 0.000621371)
    print("Yard: ", measured_value * 0.000000000946)
    print("Foot: ", (measured_value / 1000000000) * 1.0936)
    print("Inch: ", measured_value * 0.00000003937)
    print("Light Year: ", (measured_value / 1000000000000) * 9.46, "X 10^12 km/ly")

def from_mile():
    clear_screen()
    print("\tLength -> Mile\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Meter: ", measured_value * 1609.34)
    print("Kilometer: ", measured_value * 1.60934)
    print("Centimeter: ", measured_value * 1.60934 * 100)
    print("Millimeter: ", measured_value * 1609344)
    print("Micrometer: ", measured_value * 1609344000)
    print("Nanometer: ", measured_value * 1609.34 * 1000000000)
    print("Yard: ", measured_value * 1760)
    print("Foot: ", measured_value * 5280)
    print("Inch: ", measured_value * 63360)
    print("Light Year: ", measured_value / 9.461, "X 10^12 km/ly")
    
def from_yard():
    clear_screen()
    print("\tLength -> Yard\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Meter: ", measured_value * 0.9144)
    print("Kilometer: ", (measured_value * 0.9144) / 1000)
    print("Centimeter: ", measured_value * 91.44)
    print("Millimeter: ", measured_value * 914.4)
    print("Micrometer: ", measured_value * 914400)
    print("Nanometer: ", measured_value * 914400000)
    print("Mile: ", measured_value / 1760)
    print("Foot: ", measured_value * 3)
    print("Inch: ", measured_value * 36)
    print("Light Year: ", measured_value / 9.461, "X 10^16 km/ly")
    
def from_foot():
    clear_screen()
    print("\tLength -> Foot\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Meter: ", measured_value * 0.3048)
    print("Kilometer: ", measured_value * 0.0003048)
    print("Centimeter: ", measured_value * 30.48)
    print("Millimeter: ", measured_value * 304.8)
    print("Micrometer: ", measured_value * 304800)
    print("Nanometer: ", measured_value * 304800000)
    print("Mile: ", measured_value / 5280)
    print("Yard: ", measured_value / 3)
    print("Inch: ", measured_value / 12)
    print("Light Year: ", (measured_value * 0.348) / 9.461, "X 10^16 km/ly")
    
def from_inch():
    clear_screen()
    print("\tLength -> Inch\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Meter: ", measured_value * 0.0254)
    print("Kilometer: ", (measured_value * 0.0254) / 1000)
    print("Centimeter: ", measured_value * 2.54)
    print("Millimeter: ", measured_value * 25.4)
    print("Micrometer: ", measured_value * 25400)
    print("Nanometer: ", measured_value * 25400000)
    print("Mile: ", measured_value / 63360)
    print("Yard: ", measured_value / 36)
    print("Foot: ", measured_value / 12)
    print("Light Year: ", (measured_value * 0.0254) / 9.461, "X 10^16 m/ly")
    

def from_light_year():
    clear_screen()
    print("\tLength -> Light Year\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Meter: ", (measured_value * 9.461) * pow(10, 12))
    print("Kilometer: ", (measured_value * 9.461) * pow(10, 12))
    print("Centimeter: ", (measured_value * 9.461) * pow(10, 17))
    print("Millimeter: ", (measured_value * 9.461) * pow(10, 18))
    print("Micrometer: ", (measured_value * 9.461) * pow(10, 21))
    print("Nanometer: ", (measured_value * 9.461) * pow(10, 24))
    print("Mile: ", (measured_value * 9.461) * pow(10, 12))
    print("Yard: ", (measured_value * 9.461) * pow(10, 15) * 1.09361)
    print("Foot: ", (measured_value * 9.461) * pow(10, 15) * 3.28084)
    print("Inch: ", (measured_value * 9.461) * pow(10, 15) * 39.3701)

def from_celsius():
    clear_screen()
    print("\tTemperature -> Celsius\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Kelvin: ", measured_value + 273.15)
    print("Fahrenheit: ", (measured_value * 1.8) + 32)

def from_kelvin(measured_value):
    clear_screen()
    print("\tTemperature -> Kelvin\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Celsius: ", measured_value - 273.16)
    print("Fahrenheit: ", (1.8 * (measured_value - 273.15)) + 32)

def from_fahrenheit(measured_value):
    clear_screen()
    print("\tTemperature -> Fahrenheit\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Celsius: ", (0.555555556 * (measured_value - 32)))
    print("Kelvin: ", (0.555555556 * (measured_value - 32)) + 273.15)

def from_square_meter():
    clear_screen()
    print("\tArea -> Square Meter\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Square Kilometer: ", measured_value / 1000000)
    print("Square Centimeter: ", measured_value * 10000)
    print("Square Millimeter: ", measured_value * 1000000)
    print("Square Micrometer: ", measured_value * 1 * pow(10, 12))
    print("Hectare: ", measured_value / 10000)
    print("Square Mile: ", measured_value / 2589988.11)
    print("Square Yard: ", measured_value * 1.19599)
    print("Square Foot: ", measured_value * 10.7639)
    print("Square Inch: ", measured_value * 1550.0031)
    print("Acre: ", measured_value / 4,046.85642)
    
def from_square_kilometer():
    clear_screen()
    print("\tArea -> Square Kilometer\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Square Meter: ", measured_value * 1000000)
    print("Square Centimeter: ", measured_value * pow(10, 10))
    print("Square Millimeter: ", measured_value * pow(10, 12))
    print("Square Micrometer: ", measured_value * 1 * pow(10, 12))
    print("Hectare: ", measured_value / 100)
    print("Square Mile: ", measured_value / 1.93051)
    print("Square Yard: ", measured_value * 1195990.05)
    print("Square Foot: ", measured_value * 1076391040)
    print("Square Inch: ", measured_value * 1550.0031)
    print("Acre: ", measured_value / 247.105)

def from_square_centimeter():
    clear_screen()
    print("\tArea -> Square Centimeter\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Square Meter: ", measured_value / 10000)
    print("Square Kilometer: ", measured_value / pow(10, 10))
    print("Square Millimeter: ", measured_value * 100)
    print("Square Micrometer: ", measured_value * 1 * pow(10, 8))
    print("Hectare: ", measured_value / 100000000)
    print("Square Mile: ", measured_value / 25899881103.36)
    print("Square Yard: ", measured_value / 8361.2736)
    print("Square Foot: ", measured_value / 929.0304)
    print("Square Inch: ", measured_value / 6.4516)
    print("Acre: ", measured_value / 40468564.2)

def from_square_millimeter():
    clear_screen()
    print("\tArea -> Square Millimeter\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Square Meter: ", measured_value / 1000000)
    print("Square Kilometer: ", measured_value / pow(10, 12))
    print("Square Centimeter: ", measured_value / 100)
    print("Square Micrometer: ", measured_value * 10 ** 6)
    print("Hectare: ", measured_value / 10 ** 10)
    print("Square Mile: ", measured_value / 2.58998811 * 10 ** 12)
    print("Square Yard: ", measured_value / 836127.36)
    print("Square Foot: ", measured_value / 92903.04)
    print("Square Inch: ", measured_value / 645.16)
    print("Acre: ", measured_value / 40468564.2 * 10 ** 9)

def from_square_micrometer():
    clear_screen()
    print("\tArea -> Square Micrometer\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Square Meter: ", (measured_value / (10 ** 12)) * (10 ** -6))
    print("Square Kilometer: ", (measured_value * (10 ** 12)) * (10 ** -6))
    print("Square Centimeter: ", measured_value / (10 ** 8))
    print("Square Millimeter: ", measured_value / (10 ** 6))
    print("Hectare: ", measured_value / (10 ** 16))
    print("Square Mile: ", measured_value / (2.59 * (10 **12)))
    print("Square Yard: ", measured_value / (8.361 * (10 ** 6)))
    print("Square Foot: ", measured_value / (9.290 * ( 10 ** 6)))
    print("Square Inch: ", measured_value / (645.16 * (10 ** 6)))
    print("Acre: ", measured_value / 4046860000)

def from_hectare():
    clear_screen()
    print("\tArea -> Hectare\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Square Meter: ", measured_value * 10000)
    print("Square Kilometer: ", measured_value * 0.01)
    print("Square Centimeter: ", measured_value * 100000000)
    print("Square Millimeter: ", measured_value * 10000000000)
    print("Square Micrometer: ", measured_value * 10000000000000)
    print("Square Mile: ", measured_value * (0.01 / 2.58999))
    print("Square Yard: ", measured_value * 11959.9)
    print("Square Foot: ", measured_value * 107639)
    print("Square Inch: ", measured_value * 15500031)
    print("Acre: ", measured_value * 2.47105)

def from_square_mile():
    clear_screen()
    print("\tArea -> Square Mile\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Square Meter: ", measured_value * 2.59 * (10 ** 6))
    print("Square Kilometer: ", measured_value * 2.58999)
    print("Square Centimeter: ", measured_value * 2.58999 * (10 ** 10))
    print("Square Millimeter: ", measured_value * 2.58999 * (10 ** 12))
    print("Square Micrometer: ", measured_value * 2.58999 * (10 **18)) 
    print("Hectare: ", measured_value * 259)
    print("Square Yard: ", measured_value * 3097600)
    print("Square Foot: ", measured_value * 27878400)
    print("Square Inch: ", measured_value * 4.0144896 * (10 ** 9))
    print("Acre: ", measured_value * 640)
    
def from_square_yard():
    clear_screen()
    print("\tArea -> Square Yard\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Square Meter: ", measured_value * 0.836127)
    print("Square Kilometer: ", measured_value * 8.3613 * (10 ** -7))
    print("Square Centimeter: ", measured_value * 8361.27)
    print("Square Millimeter: ", measured_value * 836127)
    print("Square Micrometer: ", measured_value * 836127000000) 
    print("Hectare: ", measured_value * 0.0000836127)
    print("Square Mile: ", measured_value * 3.2283 * (10 ** -7))
    print("Square Foot: ", measured_value * 9)
    print("Square Inch: ", measured_value * 1296)
    print("Acre: ", measured_value * 0.000206612)
    
def from_square_foot():
    clear_screen()
    print("\tArea -> Square Foot\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Square Meter: ", measured_value * 0.092903)
    print("Square Kilometer: ", measured_value * 9.2903 * (10 ** -8))
    print("Square Centimeter: ", measured_value * 929.0304)
    print("Square Millimeter: ", measured_value * 92903.04)
    print("Square Micrometer: ", measured_value * 92903040000) 
    print("Hectare: ", measured_value * 9.2903 * (10 ** -6))
    print("Square Mile: ", measured_value * 3.587 * (10 ** -8))
    print("Square Yard: ", measured_value * 0.111111)
    print("Square Inch: ", measured_value * 144)
    print("Acre: ", measured_value * 2.2957 * (10 ** -5))

def from_square_inch():
    clear_screen()
    print("\tArea -> Square Inch\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Square Meter: ", measured_value * 0.00064516)
    print("Square Kilometer: ", measured_value * 6.4516 * (10 ** -10))
    print("Square Centimeter: ", measured_value * 6.4516)
    print("Square Millimeter: ", measured_value * 645.16)
    print("Square Micrometer: ", measured_value * 645160000) 
    print("Hectare: ", measured_value * 6.4516 * (10 ** -8))
    print("Square Mile: ", measured_value * 2.491 * (10 ** -10))
    print("Square Yard: ", measured_value * 0.00694444)
    print("Square Foot: ", measured_value * 9)
    print("Acre: ", measured_value * 1.5942 * (10 ** -7))

def from_acre():
    clear_screen()
    print("\tArea -> Square Acre\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Square Meter: ", measured_value * 4046.86)
    print("Square Kilometer: ", measured_value * 0.00404686)
    print("Square Centimeter: ", measured_value * 40468600)
    print("Square Millimeter: ", measured_value * 4046860000)
    print("Square Micrometer: ", measured_value * 4046860000000) 
    print("Hectare: ", measured_value * 0.404686)
    print("Square Mile: ", measured_value * 0.0015625)
    print("Square Yard: ", measured_value * 4840)
    print("Square Foot: ", measured_value * 43560)
    print("Square Inch: ", measured_value * 6272640)
    
def from_cubic_meter():
    clear_screen()
    print("\tVolume -> Cubic Meter\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Cubic Kilometer: ", (measured_value * 1 * (10 ** -9)))
    print("Cubic Millimeter: ", (measured_value * 1 * (10 ** 9)))
    print("Liter: ", measured_value * 1000)
    print("Milliliter: ", (measured_value * 1 * (10 ** 6)))
    print("US Gallon: ", measured_value * 264.172)

def from_cubic_kilometer():
    clear_screen()
    print("\tVolume -> Cubic Kilometer\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Cubic Meter: ", measured_value * 1 * (10 ** 9))
    print("Cubic Millimeter: ", (measured_value * 1 * (10 ** 18)))
    print("Liter: ", measured_value * 1 * (10 ** 12))
    print("Milliliter: ", (measured_value * 1 * (10 ** 15)))
    print("US Gallon: ", measured_value * 2.64172 * (10 ** 11))

def from_cubic_millimeter():
    clear_screen()
    print("\tVolume -> Cubic Millimeter\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Cubic Meter: ", measured_value * 1 * (10 ** -9))
    print("Cubic Kilometer: ", (measured_value * 1 * (10 ** -18)))
    print("Liter: ", measured_value * 1 * (10 ** -9))
    print("Milliliter: ", (measured_value * 1 * (10 ** -3)))
    print("US Gallon: ", measured_value * 2.64172 * (10 ** -7))
    
def from_liter():
    clear_screen()
    print("\tVolume -> Liter\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Cubic Meter: ", measured_value * 0.001)
    print("Cubic Kilometer: ", (measured_value * 1 * (10 ** -12)))
    print("Cubic Millimeter: ", measured_value * 1 * (10 ** 6))
    print("Milliliter: ", (measured_value * 1000))
    print("US Gallon: ", measured_value * 0.264172)
    
def from_milliliter():
    clear_screen()
    print("\tVolume -> Milliliter\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Cubic Meter: ", measured_value * 1 * (10 ** -6))
    print("Cubic Kilometer: ", (measured_value * 1 * (10 ** -15)))
    print("Cubic Millimeter: ", measured_value * 1000)
    print("Liter: ", measured_value * 0.001)
    print("US Gallon: ", measured_value * 0.000264172)
    
def from_us_gallon():
    clear_screen()
    print("\tVolume -> US Gallon\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Cubic Meter: ", measured_value * 0.00378541)
    print("Cubic Kilometer: ", (measured_value * 3.78541 * (10 ** -12)))
    print("Cubic Millimeter: ", measured_value * 3.78541 * (10 ** 6))
    print("Liter: ", measured_value * 3.78541)
    print("Milliliter: ", (measured_value * 3,785.41))
    
def from_kilogram():
    clear_screen()
    print("\Weight -> Kilogram\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Gram: ", measured_value * 1000)
    print("Milligram: ", measured_value * 1 * (10 ** 6))
    print("Metric Ton: ", measured_value * 0.001)
    print("Pound: ", measured_value * 2.20462)
    print("Carrat: ", measured_value * 5000)
    print("Atomic Mass Unit: ", measured_value * 6.02214179 * (10 ** 26))
    
def from_gram():
    clear_screen()
    print("\Weight -> Gram\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Kilogram", measured_value * 0.001)
    print("Milligram: ", measured_value * 1000)
    print("Metric Ton: ", measured_value * 1 * (10 ** -6))
    print("Pound: ", measured_value * 0.00220462)
    print("Carrat: ", measured_value * 5)
    print("Atomic Mass Unit: ", measured_value * 6.02214179 * (10 ** 23))
    
def from_milligram():
    clear_screen()
    print("\Weight -> Milligram\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Kilogram", measured_value * 1 * (10 ** -6))
    print("Gram: ", measured_value * 0.001)
    print("Metric Ton: ", measured_value * 1 * (10 ** -9))
    print("Pound: ", measured_value * 2.20462 * (10 ** -6))
    print("Carrat: ", measured_value * 0.005)
    print("Atomic Mass Unit: ", measured_value * 6.02214179 * (10 ** 20))
    
def from_metric_ton():
    clear_screen()
    print("\Weight -> Metric Ton\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Kilogram", measured_value * 1000)
    print("Gram: ", measured_value * 1 * (10 ** 6))
    print("Milligram: ", measured_value * 1 * (10 ** 9))
    print("Pound: ", measured_value * 2204.62)
    print("Carrat: ", measured_value * 5 * (10 ** 6))
    print("Atomic Mass Unit: ", measured_value * 6.02214179 * (10 ** 29))
    
def from_pound():
    clear_screen()
    print("\Weight -> Pound\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Kilogram", measured_value * 0.45359237)
    print("Gram: ", measured_value * 453.59237)
    print("Milligram: ", measured_value * 453592.37)
    print("Metric Ton: ", measured_value * 0.00045359237)
    print("Carrat: ", measured_value * 2267.96185)
    print("Atomic Mass Unit: ", measured_value * 2.73159734 * (10 ** 26))
    
def from_carrat():
    clear_screen()
    print("\Weight -> Carrat\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Kilogram", measured_value * 0.0002)
    print("Gram: ", measured_value * 0.2)
    print("Milligram: ", measured_value * 200)
    print("Metric Ton: ", measured_value * 2 * (10 ** -7))
    print("Pound: ", measured_value * 0.000440925)
    print("Atomic Mass Unit: ", measured_value * 1.20442881 * (10 ** 23))
    
def from_amu():
    clear_screen()
    print("\Weight -> Atomic Mass Unit\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Kilogram", measured_value * 1.66053906660 * (10 ** -27))
    print("Gram: ", measured_value * 1.66053906660 * (10 ** -24))
    print("Milligram: ", measured_value * 1.66053906660 * (10 ** -21))
    print("Metric Ton: ", measured_value * 1.66053906660 * (10 ** -30))
    print("Pound: ", measured_value * 3.660867 * (10 ** -27))
    print("Carrat: ", measured_value * 8.3027 * (10 ** -23))
    
def from_second():
    clear_screen()
    print("\Time -> Second\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("\tTime -> Second\n")
    print("Millisecond: ", measured_value * 1000)
    print("Microsecond: ", measured_value * 1000000)
    print("Nanosecond: ", measured_value * 1000000000)
    print("Minute: ", measured_value / 60)
    print("Hour: ", measured_value / 3600)
    print("Day: ", measured_value / 86400)
    print("Week: ", measured_value / 604800)
    print("Month: ", measured_value / 2629746)
    print("Year: ", measured_value / 31557600)
    
def from_millisecond():
    clear_screen()
    print("\Time -> Millisecond\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Second: ", measured_value / 1000)
    print("Microsecond: ", measured_value * 1000)
    print("Nanosecond: ", measured_value * 1000000)
    print("Minute: ", measured_value / 60000)
    print("Hour: ", measured_value / 3600000)
    print("Day: ", measured_value / 86400000)
    print("Week: ", measured_value / 604800000)
    print("Month: ", measured_value / 2629746000)
    print("Year: ", measured_value / 31557600000)
    
def from_microsecond(measured_value):
    clear_screen()
    print("\Time -> Microsecond\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Second: ", measured_value / 1000000)
    print("Millisecond: ", measured_value / 1000)
    print("Nanosecond: ", measured_value * 1000)
    print("Minute: ", measured_value / 60000000)
    print("Hour: ", measured_value / 3600000000)
    print("Day: ", measured_value / 86400000000)
    print("Week: ", measured_value / 604800000000)
    print("Month: ", measured_value / 2629746000000)
    print("Year: ", measured_value / 31557600000000)
    
def from_nanosecond(measured_value):
    clear_screen()
    print("\Time -> Nanosecond\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Second: ", measured_value / 1000000000)
    print("Millisecond: ", measured_value / 1000000)
    print("Microsecond: ", measured_value / 1000)
    print("Minute: ", measured_value / 60000000000)
    print("Hour: ", measured_value / 3600000000000)
    print("Day: ", measured_value / 86400000000000)
    print("Week: ", measured_value / 604800000000000)
    print("Month: ", measured_value / 2629746000000000)
    print("Year: ", measured_value / 31557600000000000)
    
def from_minute(measured_value):
    clear_screen()
    print("\Time -> Minute\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Second: ", measured_value * 60)
    print("Millisecond: ", measured_value * 60000)
    print("Microsecond: ", measured_value * 60000000)
    print("Nanosecond: ", measured_value * 60000000000)
    print("Hour: ", measured_value / 60)
    print("Day: ", measured_value / 1440)
    print("Week: ", measured_value / 10080)
    print("Month: ", measured_value / 43830)
    print("Year: ", measured_value / 525600)
    
def from_hour(measured_value):
    clear_screen()
    print("\Time -> Hour\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Second: ", measured_value * 3600)
    print("Millisecond: ", measured_value * 3.6 * (10 ** 6))
    print("Microsecond: ", measured_value * 3.6 * (10 ** 9))
    print("Nanosecond: ", measured_value * 3.6 * (10 ** 12))
    print("Minute: ", measured_value * 60)
    print("Day: ", measured_value / 24)
    print("Week: ", measured_value / 168)
    print("Month: ", measured_value / 730.5)
    print("Year: ", measured_value / 8766)
    
def from_day(measured_value):
    clear_screen()
    print("\Time -> Day\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Second: ", measured_value * 86400)
    print("Millisecond: ", measured_value * 8.64 * (10 ** 7))
    print("Microsecond: ", measured_value * 8.64 * (10 ** 10))
    print("Nanosecond: ", measured_value * 8.64 * (10 ** 13))
    print("Minute: ", measured_value * 1440)
    print("Hour: ", measured_value * 24)
    print("Week: ", measured_value / 7)
    print("Month: ", measured_value / 30.44)
    print("Year: ", measured_value / 365.25)
    
def from_week(measured_value):
    clear_screen()
    print("\Time -> Week\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Second: ", measured_value * 604800)
    print("Millisecond: ", measured_value * 6.048 * (10 ** 8))
    print("Microsecond: ", measured_value * 6.048 * (10 ** 11))
    print("Nanosecond: ", measured_value * 6.048 * (10 ** 14))
    print("Minute: ", measured_value * 10080)
    print("Hour: ", measured_value * 168)
    print("Day: ", measured_value * 7)
    print("Month: ", measured_value / 434524)
    print("Year: ", measured_value / 52.1429)
    
def from_month(measured_value):
    clear_screen()
    print("\Time -> Month\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Second: ", measured_value * 30.44 * 24 * 60 * 60)
    print("Millisecond: ", measured_value * 30.44 * 24 * 60 * 60 * (10 ** 3))
    print("Microsecond: ", measured_value * 30.44 * 24 * 60 * 60 * (10 ** 6))
    print("Nanosecond: ", measured_value * 30.44 * 24 * 60 * 60 * (10 ** 9))
    print("Minute: ", measured_value * 30.44 * 24 * 60)
    print("Hour: ", measured_value * 30.44 * 24)
    print("Day: ", measured_value * 30.44)
    print("Week: ", measured_value * 4.34524)
    print("Year: ", measured_value / 12)
    
def from_year(measured_value):
    clear_screen()
    print("\Time -> Year\n")
    
    measured_value = float(input("Enter the measurement: "))
    print()
    
    print("Second: ", measured_value * 365.25 * 24 * 60 * 60)
    print("Millisecond: ", measured_value * 365.25 * 24 * 60 * 60 * (10 ** 3))
    print("Microsecond: ", measured_value * 365.25 * 24 * 60 * 60 * (10 ** 6))
    print("Nanosecond: ", measured_value * 365.25 * 24 * 60 * 60 * (10 ** 9))
    print("Minute: ", measured_value * 365.25 * 24 * 60)
    print("Hour: ", measured_value * 365.25 * 24)
    print("Day: ", measured_value * 365.25)
    print("Week: ", measured_value * 52.1429)
    print("Month: ", measured_value * 12)

def length():
    clear_screen()
    print("\tLength ->\n")
    print("Choose measured value unit")
    print("1. Meter\n2. Kilometer\n3. Centimeter\n4. Millimeter\n5. Micrometer\n6. Nanometer\n7. Mile\n8. Yard\n9. Foot\n10. Inch\n11. Light Year\n0. Exit\n")
    measured_unit = int(input("Enter the value: "))
    
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
        else:
            print("Error occurred. Please try again!")
    else:
        exit_program()

def temperature():
    clear_screen()
    print("\tTemperature->\n")
    print("Choose measured value unit")
    print("1. Celsius\n2. Kelvin\n3. Fahrenheit\n0. Exit")
    measured_unit = int(input("Enter the value: "))
    
    if measured_unit != 0:
        if (measured_unit == 1):
            from_celsius()
        elif (measured_unit == 2):
            from_kelvin()
        elif (measured_unit == 3):
            from_fahrenheit()
        else:
            print("Error occurred. Please try again!")
    else:
        exit_program()

def area():
    clear_screen()
    print("\tArea -> \n")
    print("Choose measured value unit")
    print("1. Square Meter\n2. Square Kilometer\n3. Square Centimeter\n4. Square Millimeter\n5. Square Micrometer\n6. Hectare\n7. Square Mile\n8. Square Yard\n9. Square Foot\n10. Square Inch\n11. Acre\n0. Exit")
    measured_unit = int(input("Enter the value: "))
        
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
        else:
            print("Error occurred. Please try again!")
    else:
        exit_program()

def volume():
    clear_screen()
    print("\tVolume -> \n")
    print("Choose measured value unit")
    print("1. Cubic Meter\n2. Cubic Kilometer\n3. Cubic Millimeter\n4. Liter\n5. Milliliter\n6. US Gallon\n0. Exit")
    measured_unit = int(input("Enter the value: "))
    
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
        else:
            print("Error Occurred")
    else:
        exit_program()

def weight():
    clear_screen()
    print("\tWeight -> \n")
    print("Choose measured value unit")
    print("1. Kilogram\n2. Gram\n3. Milligram\n4. Metric Ton\n5. Pound\n6. Carrat\n7. Atomic Mass Unit\n0. Exit")
    measured_unit = int(input("Enter the measurement: "))
        
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
        else:
            print("Error Occurred. Please try again!")
    else:
        exit_program()
        
def time():
    print("\tTime ->\n")
    print("Choose measured value unit")
    print("1. Second\n2. Millisecond\n3. Microsecond\n4. Nanosecond\n5. Minute\n6. Hour\n7. Day\n8. Week\n9. Month\n10. Year\n0. Exit")
    measured_unit = int(input("Enter the value: "))
    
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
    else:
        exit_program()

clear_screen()
print("\t\tQuickConvertor\t\t\n")
option = 1
while (option != 0):
    print(exit)
    print("1. Length\n2. Temperature\n3. Area\n4. Volume\n5. Weight\n6. Time\n0. Exit")
    option = int(input("Enter your choice: "))
    clear_screen()
    
    if option == 1:
        length()
        print("_" * 40)
        print("\n")
    elif option == 2:
        temperature()
        print("_" * 40)
        print("\n")
    elif option == 3:
        area()
        print("_" * 40)
        print("\n")
    elif option == 4:
        volume()
        print("_" * 40)
        print("\n")
    elif option == 5:
        weight()
        print("_" * 40)
        print("\n")
    elif option == 6:
        time()
        print("_" * 40)
        print("\n")
    elif option == 0:
        exit_program()
    else:
        print("Unknown option. Please try again!...")
        print("_" * 40)