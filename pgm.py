"""
    Name: QuickConverter
    Description: A simple and efficient tool for converting length units.
    Date of Creation: 06/06/2024
    Last Modified On: 07/06/2024
    Creator: Navaneeth P P
    GitHub Profile: navaneethpp
    Requirements: None
    Notes: Not completed
"""

def from_meter(measured_value):
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
        
        
        
def from_kilometer(measured_value):
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
    


def from_centimeter(measured_value):
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
    
    

def from_millimeter(measured_value):
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
    
    
def from_micrometer(measured_value):
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
    
    
def from_nanometer(measured_value):
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
    

def from_mile(measured_value):
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
    

def from_yard(measured_value):
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
    
def from_foot(measured_value):
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
    
def from_inch(measured_value):
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
    

def from_light_year(measured_value):
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
    
    
    
def from_celsius(measured_value):
    print("Kelvin: ", measured_value + 273.15)
    print("Fahrenheit: ", (measured_value * 1.8) + 32)
    
def from_kelvin(measured_value):
    print("Celsius: ", measured_value - 273.16)
    print("Fahrenheit: ", (1.8 * (measured_value - 273.15)) + 32)
    
def from_fahrenheit(measured_value):
    print("Celsius: ", (0.555555556 * (measured_value - 32)))
    print("Kelvin: ", (0.555555556 * (measured_value - 32)) + 273.15)
    

def from_square_meter(measured_value):
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
    
    
def from_square_kilometer(measured_value):
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
    
def from_square_centimeter(measured_value):
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
        
        
def from_square_millimeter(measured_value):
    print("Square Meter: ", measured_value / 1000000)
    print("Square Kilometer: ", measured_value / pow(10, 12))
    print("Square Centimeter: ", measured_value / 100)
    # print("Square Millimeter: ", measured_value * 100)
    print("Square Micrometer: ", measured_value * 10 ** 6)
    print("Hectare: ", measured_value / 10 ** 10)
    print("Square Mile: ", measured_value / 2.58998811 * 10 ** 12)
    print("Square Yard: ", measured_value / 836127.36)
    print("Square Foot: ", measured_value / 92903.04)
    print("Square Inch: ", measured_value / 645.16)
    print("Acre: ", measured_value / 40468564.2 * 10 ** 9)
    

def length():
    print()
    print("Choose measured value unit")
    print("1. Meter\n2. Kilometer\n3. Centimeter\n4. Millimeter\n5. Micrometer\n6. Nanometer\n7. Mile\n8. Yard\n9. Foot\n10. Inch\n11. Light Year\n")
    measured_unit = int(input("Enter the value: "))

    print()

    measured_value = float(input("Enter the measurement: "))
        
    if (measured_unit == 1):
        from_meter(measured_value)
    elif (measured_unit == 2):
        from_kilometer(measured_value)
    elif (measured_unit == 3):
        from_centimeter(measured_value)
    elif (measured_unit == 4):
        from_millimeter(measured_value)
    elif (measured_unit == 5):
        from_micrometer(measured_value)
    elif (measured_unit == 6):
        from_nanometer(measured_value)
    elif (measured_unit == 7):
        from_mile(measured_value)
    elif (measured_unit == 8):
        from_yard(measured_value)
    elif (measured_unit == 9):
        from_foot(measured_value)
    elif (measured_unit == 10):
        from_inch(measured_value)
    elif (measured_unit == 11):
        from_light_year(measured_value)
    else:
        print("Error occurred. Please try again!")
        return

def temperature():
    print()
    print("Choose measured value unit")
    print("1. Celsius\n2. Kelvin\n3. Fahrenheit")
    measured_unit = int(input("Enter the value: "))
    print()
    measured_value = float(input("Enter the measurement: "))
    
    if (measured_unit == 1):
        from_celsius(measured_value)
    elif (measured_unit == 2):
        from_kelvin(measured_value)
    elif (measured_unit == 3):
        from_fahrenheit(measured_value)
    else:
        print("Error occurred. Please try again!")
        

def area():
    print()
    print("Choose measured value unit")
    print("1. Square Meter\n2. Square Kilometer\n3. Square Centimeter\n4. Square Millimeter\n5. Square Micrometer\n6. Hectare\n7. Square Mile\n8. Square Yard\n9. Square Foot\n9. Square Inch\n10. Acre")
    measured_unit = int(input("Enter the value: "))
    print()
    measured_value = float(input("Enter the measurement: "))
    
    if (measured_unit == 1):
        from_square_meter(measured_value)
    elif (measured_unit == 2):
        from_square_kilometer(measured_value)
    elif (measured_unit == 3):
        from_square_centimeter(measured_value)
    elif (measured_unit == 4):
        from_square_millimeter(measured_value)
    
    
    
    

print("Choose correct option by the number")
print("1. Length\n2. Temperature\n3. Area\n4. Volume\n5. Weight\n6. Time")
option = int(input("Enter your choice: "))

if option == 1:
    length()
if option == 2:
    temperature()
if option == 3:
    area()