# QuickConvert

**QuickConvert** is a Python tool designed for quick and efficient unit conversions. It supports converting various length units such as meters, kilometers, centimeters, millimeters, micrometers, and more.

## Description

QuickConvert offers a simple command-line interface for converting measurements between different length units. This tool is ideal for students, engineers, and anyone who needs to perform unit conversions swiftly and accurately.

## Features

- Converts between multiple length units
- User-friendly command-line interface
- Supports common length units such as meters, kilometers, and inches
- Provides accurate and reliable conversions
- Open-source and easy to extend

## Requirements

- Python 3.6 or higher
- No additional libraries required

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/navaneethpp/QuickConvert.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd QuickConvert
    ```

## Usage

To use QuickConvert, run the Python script and follow the prompts to enter your measurements and choose the units for conversion.

1. **Run the script:**
    ```bash
    python quickconvert.py
    ```

2. **Follow the prompts:**
    - Choose the type of measurement (currently supports only length).
    - Enter the value and select the unit for conversion.
    - View the converted values in various units.

### Example

Here's an example of how to use QuickConvert:

```text
Choose the correct option by the number:
1. Length
2. Temperature
3. Area
4. Volume
5. Weight
6. Time
Enter your choice: 1

Choose measured value unit:
1. Meter
2. Kilometer
3. Centimeter
4. Millimeter
5. Micrometer
6. Nanometer
7. Mile
8. Yard
9. Foot
10. Inch
11. Light Year
Enter the value: 1

Enter the measurement: 100

Kilometer:  0.1
Centimeter:  10000
Millimeter:  100000
Micrometer:  100000000
Nanometer:  100000000000
Mile:  0.0621371
Yard:  109.36
Foot:  328.08
Inch:  3937
Light Year:  0.946 X 10^15 km/ly
