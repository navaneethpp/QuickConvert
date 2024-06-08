"""
    Name: QuickConverter
    Description: A simple and efficient tool for converting length units.
    Date of Creation: 06/06/2024
    Last Modified On: 08/06/2024
    Creator: Navaneeth P P
    GitHub Profile: navaneethpp
    Requirements: Python 3.6
    Notes: Not completed,
            Time - Millisecond
    To do:  * Selection Display
            * Other conversions
            * Section exit issue
            * Adding Infinite Loop
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
    print("Square Micrometer: ", measured_value * 10 ** 6)
    print("Hectare: ", measured_value / 10 ** 10)
    print("Square Mile: ", measured_value / 2.58998811 * 10 ** 12)
    print("Square Yard: ", measured_value / 836127.36)
    print("Square Foot: ", measured_value / 92903.04)
    print("Square Inch: ", measured_value / 645.16)
    print("Acre: ", measured_value / 40468564.2 * 10 ** 9)
    

def from_square_micrometer(measured_value):
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
    

def from_hectare(measured_value):
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
    

def from_square_mile(measured_value):
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
    
def from_square_yard(measured_value):
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
    
def from_square_foot(measured_value):
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
    

def from_square_inch(measured_value):
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
    
    
def from_acre(measured_value):
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
    
def from_cubic_meter(measured_value):
    print("Cubic Kilometer: ", (measured_value * 1 * (10 ** -9)))
    print("Cubic Millimeter: ", (measured_value * 1 * (10 ** 9)))
    print("Liter: ", measured_value * 1000)
    print("Milliliter: ", (measured_value * 1 * (10 ** 6)))
    print("US Gallon: ", measured_value * 264.172)
    

def from_cubic_kilometer(measured_value):
    print("Cubic Meter: ", measured_value * 1 * (10 ** 9))
    print("Cubic Millimeter: ", (measured_value * 1 * (10 ** 18)))
    print("Liter: ", measured_value * 1 * (10 ** 12))
    print("Milliliter: ", (measured_value * 1 * (10 ** 15)))
    print("US Gallon: ", measured_value * 2.64172 * (10 ** 11))
    
    
def from_cubic_millimeter(measured_value):
    print("Cubic Meter: ", measured_value * 1 * (10 ** -9))
    print("Cubic Kilometer: ", (measured_value * 1 * (10 ** -18)))
    print("Liter: ", measured_value * 1 * (10 ** -9))
    print("Milliliter: ", (measured_value * 1 * (10 ** -3)))
    print("US Gallon: ", measured_value * 2.64172 * (10 ** -7))
    
def from_liter(measured_value):
    print("Cubic Meter: ", measured_value * 0.001)
    print("Cubic Kilometer: ", (measured_value * 1 * (10 ** -12)))
    print("Cubic Millimeter: ", measured_value * 1 * (10 ** 6))
    print("Milliliter: ", (measured_value * 1000))
    print("US Gallon: ", measured_value * 0.264172)
    
def from_milliliter(measured_value):
    print("Cubic Meter: ", measured_value * 1 * (10 ** -6))
    print("Cubic Kilometer: ", (measured_value * 1 * (10 ** -15)))
    print("Cubic Millimeter: ", measured_value * 1000)
    print("Liter: ", measured_value * 0.001)
    print("US Gallon: ", measured_value * 0.000264172)
    
def from_us_gallon(measured_value):
    print("Cubic Meter: ", measured_value * 0.00378541)
    print("Cubic Kilometer: ", (measured_value * 3.78541 * (10 ** -12)))
    print("Cubic Millimeter: ", measured_value * 3.78541 * (10 ** 6))
    print("Liter: ", measured_value * 3.78541)
    print("Milliliter: ", (measured_value * 3,785.41))
    
def from_kilogram(measured_value):
    print("Gram: ", measured_value * 1000)
    print("Milligram: ", measured_value * 1 * (10 ** 6))
    print("Metric Ton: ", measured_value * 0.001)
    print("Pound: ", measured_value * 2.20462)
    print("Carrat: ", measured_value * 5000)
    print("Atomic Mass Unit: ", measured_value * 6.02214179 * (10 ** 26))
    
def from_gram(measured_value):
    print("Kilogram", measured_value * 0.001)
    print("Milligram: ", measured_value * 1000)
    print("Metric Ton: ", measured_value * 1 * (10 ** -6))
    print("Pound: ", measured_value * 0.00220462)
    print("Carrat: ", measured_value * 5)
    print("Atomic Mass Unit: ", measured_value * 6.02214179 * (10 ** 23))
    
def from_milligram(measured_value):
    print("Kilogram", measured_value * 1 * (10 ** -6))
    print("Gram: ", measured_value * 0.001)
    print("Metric Ton: ", measured_value * 1 * (10 ** -9))
    print("Pound: ", measured_value * 2.20462 * (10 ** -6))
    print("Carrat: ", measured_value * 0.005)
    print("Atomic Mass Unit: ", measured_value * 6.02214179 * (10 ** 20))
    
def from_metric_ton(measured_value):
    print("Kilogram", measured_value * 1000)
    print("Gram: ", measured_value * 1 * (10 ** 6))
    print("Milligram: ", measured_value * 1 * (10 ** 9))
    print("Pound: ", measured_value * 2204.62)
    print("Carrat: ", measured_value * 5 * (10 ** 6))
    print("Atomic Mass Unit: ", measured_value * 6.02214179 * (10 ** 29))
    
def from_pound(measured_value):
    print("Kilogram", measured_value * 0.45359237)
    print("Gram: ", measured_value * 453.59237)
    print("Milligram: ", measured_value * 453592.37)
    print("Metric Ton: ", measured_value * 0.00045359237)
    print("Carrat: ", measured_value * 2267.96185)
    print("Atomic Mass Unit: ", measured_value * 2.73159734 * (10 ** 26))
    
def from_carrat(measured_value):
    print("Kilogram", measured_value * 0.0002)
    print("Gram: ", measured_value * 0.2)
    print("Milligram: ", measured_value * 200)
    print("Metric Ton: ", measured_value * 2 * (10 ** -7))
    print("Pound: ", measured_value * 0.000440925)
    print("Atomic Mass Unit: ", measured_value * 1.20442881 * (10 ** 23))
    
def from_amu(measured_value):
    print("Kilogram", measured_value * 1.66053906660 * (10 ** -27))
    print("Gram: ", measured_value * 1.66053906660 * (10 ** -24))
    print("Milligram: ", measured_value * 1.66053906660 * (10 ** -21))
    print("Metric Ton: ", measured_value * 1.66053906660 * (10 ** -30))
    print("Pound: ", measured_value * 3.660867 * (10 ** -27))
    print("Carrat: ", measured_value * 8.3027 * (10 ** -23))
    
def from_second(measured_value):
    print("Millisecond: ", measured_value * 1000)
    print("Microsecond: ", measured_value * 1000000)
    print("Nanosecond: ", measured_value * 1000000000)
    print("Minute: ", measured_value / 60)
    print("Hour: ", measured_value / 3600)
    print("Day: ", measured_value / 86400)
    print("Week: ", measured_value / 604800)
    print("Month: ", measured_value / 2629746)
    print("Year: ", measured_value / 31557600)
    
def from_millisecond(measured_value):
    print("Second: ", measured_value / 1000)
    # print("Millisecond: ", measured_value * 1000)
    print("Microsecond: ", measured_value * 1000)
    print("Nanosecond: ", measured_value * 1000000)
    print("Minute: ", measured_value / 60000)
    print("Hour: ", measured_value / 3600000)
    print("Day: ", measured_value / 86400000)
    print("Week: ", measured_value / 604800000)
    print("Month: ", measured_value / 2629746000)
    print("Year: ", measured_value / 31557600000)

def length():
    print()
    print("Choose measured value unit")
    print("1. Meter\n2. Kilometer\n3. Centimeter\n4. Millimeter\n5. Micrometer\n6. Nanometer\n7. Mile\n8. Yard\n9. Foot\n10. Inch\n11. Light Year\n0. Exit\n0. Exit\n")
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
    print("1. Celsius\n2. Kelvin\n3. Fahrenheit\n0. Exiting")
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
    print("1. Square Meter\n2. Square Kilometer\n3. Square Centimeter\n4. Square Millimeter\n5. Square Micrometer\n6. Hectare\n7. Square Mile\n8. Square Yard\n9. Square Foot\n10. Square Inch\n11. Acre\n0. Exiting...")
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
    elif (measured_unit == 5):
        from_square_micrometer(measured_value)
    elif (measured_unit == 6):
        from_hectare(measured_value)
    elif (measured_unit == 7):
        from_square_mile(measured_value)
    elif (measured_unit == 8):
        from_square_yard(measured_value)
    elif (measured_unit == 9):
        from_square_foot(measured_value)
    elif (measured_unit == 10):
        from_square_inch(measured_value)
    elif (measured_unit == 11):
        from_acre(measured_value)
    elif (measured_value == 0):
        print("Exiting...")
    else:
        print("Error occurred. Please try again!")
        
        
def volume():
    print()
    print("Choose measured value unit")
    print("1. Cubic Meter\n2. Cubic Kilometer\n3. Cubic Millimeter\n4. Liter\n5. Milliliter\n6. US Gallon\n0. Exit")
    measured_unit = int(input("Enter the value: "))
    print()
    measured_value = float(input("Enter the measurement: "))
    
    if measured_unit == 1:
        from_cubic_meter(measured_value)
    elif measured_unit == 2:
        from_cubic_kilometer(measured_value)
    elif measured_unit == 3:
        from_cubic_millimeter(measured_value)
    elif measured_unit == 4:
        from_liter(measured_value)
    elif measured_unit == 5:
        from_milliliter(measured_value)
    elif measured_unit == 6:
        from_us_gallon(measured_value)
    elif measured_unit == 0:
        print("Exiting...")
    else:
        print("Error Occurred")
        

def weight():
    print()
    print("Choose measured value unit")
    print("1. Kilogram\n2. Gram\n3. Milligram\n4. Metric Ton\n5. Pound\n6. Carrat\n7. Atomic Mass Unit\n0. Exit")
    measured_unit = int(input("Enter the measurement: "))
    print()
    measured_value = float(input("Enter the measurement: "))
    
    if (measured_unit == 1):
        from_kilogram(measured_value)
    elif (measured_unit == 2):
        from_gram(measured_value)
    elif measured_unit == 3:
        from_milligram(measured_value)
    elif measured_unit == 4:
        from_metric_ton(measured_value)
    elif measured_unit == 5:
        from_pound(measured_value)
    elif measured_unit == 6:
        from_carrat(measured_value)
    elif measured_unit == 7:
        from_amu(measured_value)
    elif (measured_unit == 0):
        print("Exiting...")
    else:
        print("Error Occurred. Please try again!")
        
def time():
    print()
    print("Choose measured value unit")
    print("1. Second\n2. Millisecond\n3. Microsecond\n4. Nanosecond\n5. Minute\n6. Hour\n7. Day\n8. Week\n9. Month\n10. Year")
    measured_unit = int(input("Enter the value: "))
    print()
    measured_value = float(input("Enter the measurement: "))
    
    if measured_unit == 1:
        from_second(measured_value)
    elif measured_unit == 2:
        from_millisecond(measured_value)
    elif measured_unit == 0:
        print("Exiting")
    else:
        print("Error occurred. Please try again!")
    
print("Choose correct option by the number")
print("1. Length\n2. Temperature\n3. Area\n4. Volume\n5. Weight\n6. Time\n0. Exit")
option = int(input("Enter your choice: "))

if option == 1:
    length()
elif option == 2:
    temperature()
elif option == 3:
    area()
elif option == 4:
    volume()
elif option == 5:
    weight()
elif option == 6:
    time()
elif option == 0:
    print("Exiting...")