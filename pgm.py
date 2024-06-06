"""
    Name: QuickConverter
    Description: A simple and efficient tool for converting length units.
    Date of Creation: 06/06/2024
    Last Modified On: 06/06/2024
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
    # print("Nanometer: ", measured_value * 1000)
    print("Mile: ", (measured_value / 1000000000) * 0.000621371)
    print("Yard: ", measured_value * 0.000000000946)
    print("Foot: ", (measured_value / 1000000000) * 1.0936)
    print("Inch: ", measured_value * 0.00000003937)
    print("Light Year: ", (measured_value / 1000000000000) * 9.46, "X 10^12 km/ly")
        
        

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


print("Choose correct option by the number")
print("1. Length\n2. Temperature\n3. Area\n4. Volume\n5. Weight\n6. Time")
option = int(input("Enter your choice: "))

if option == 1:
    length()