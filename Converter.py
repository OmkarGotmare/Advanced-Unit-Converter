# Converter.py
class Converter:
    units = {
        "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
        "Length": ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"],
        "Weight": ["Kilogram", "Gram", "Pound", "Ounce"],
        "Currency": ["USD", "INR", "EUR", "GBP"],
        "Speed": ["m/s", "km/h", "mph"],
        "Area": ["Square Meter", "Square Kilometer", "Square Mile"],
        "Volume": ["Liter", "Milliliter", "Gallon"],
        "Time": ["Second", "Minute", "Hour", "Day"],
        "Digital Storage": ["Byte", "Kilobyte", "Megabyte", "Gigabyte"],
        "Pressure": ["Pascal", "Bar", "PSI"],
        "Energy": ["Joule", "Calorie", "kWh"],
        "Power": ["Watt", "Kilowatt", "Horsepower"],
        "Fuel Efficiency": ["km/L", "mpg"],
        "Angle": ["Degree", "Radian"],
        "Frequency": ["Hertz", "Kilohertz", "Megahertz"],
        "Cooking Measures": ["Cup", "Tablespoon", "Teaspoon"],
        "Force": ["Newton", "Dyne", "Pound-force"],
        "Data Transfer Speed": ["Mbps", "Gbps", "KBps"]
    }

    @staticmethod
    def convert(category, value, from_unit, to_unit):
        # Temperature conversions
        if category == "Temperature":
            if from_unit == to_unit:
                return value
            if from_unit == "Celsius":
                if to_unit == "Fahrenheit":
                    return (value * 9/5) + 32
                elif to_unit == "Kelvin":
                    return value + 273.15
            elif from_unit == "Fahrenheit":
                if to_unit == "Celsius":
                    return (value - 32) * 5/9
                elif to_unit == "Kelvin":
                    return ((value - 32) * 5/9) + 273.15
            elif from_unit == "Kelvin":
                if to_unit == "Celsius":
                    return value - 273.15
                elif to_unit == "Fahrenheit":
                    return ((value - 273.15) * 9/5) + 32
        
        # Length (base: meter)
        length_units = {
            "Meter": 1, "Kilometer": 1000, "Centimeter": 0.01,
            "Millimeter": 0.001, "Mile": 1609.34, "Yard": 0.9144,
            "Foot": 0.3048, "Inch": 0.0254
        }
        if category == "Length":
            return value * length_units[from_unit] / length_units[to_unit]

        # Weight (base: kilogram)
        weight_units = {
            "Kilogram": 1, "Gram": 0.001, "Pound": 0.453592, "Ounce": 0.0283495
        }
        if category == "Weight":
            return value * weight_units[from_unit] / weight_units[to_unit]

        # Currency (example fixed rates)
        currency_rates = {"USD": 1, "INR": 83.0, "EUR": 0.92, "GBP": 0.79}
        if category == "Currency":
            return value * currency_rates[to_unit] / currency_rates[from_unit]

        # Speed (base: m/s)
        speed_units = {"m/s": 1, "km/h": 0.277778, "mph": 0.44704}
        if category == "Speed":
            return value * speed_units[from_unit] / speed_units[to_unit]

        # Area (base: square meter)
        area_units = {"Square Meter": 1, "Square Kilometer": 1e6, "Square Mile": 2.59e6}
        if category == "Area":
            return value * area_units[from_unit] / area_units[to_unit]

        # Volume (base: liter)
        volume_units = {"Liter": 1, "Milliliter": 0.001, "Gallon": 3.78541}
        if category == "Volume":
            return value * volume_units[from_unit] / volume_units[to_unit]

        # Time (base: second)
        time_units = {"Second": 1, "Minute": 60, "Hour": 3600, "Day": 86400}
        if category == "Time":
            return value * time_units[from_unit] / time_units[to_unit]

        # Digital Storage (base: byte)
        storage_units = {"Byte": 1, "Kilobyte": 1024, "Megabyte": 1024**2, "Gigabyte": 1024**3}
        if category == "Digital Storage":
            return value * storage_units[from_unit] / storage_units[to_unit]

        # Pressure (base: Pascal)
        pressure_units = {"Pascal": 1, "Bar": 1e5, "PSI": 6894.76}
        if category == "Pressure":
            return value * pressure_units[from_unit] / pressure_units[to_unit]

        # Energy (base: Joule)
        energy_units = {"Joule": 1, "Calorie": 4.184, "kWh": 3.6e6}
        if category == "Energy":
            return value * energy_units[from_unit] / energy_units[to_unit]

        # Power (base: Watt)
        power_units = {"Watt": 1, "Kilowatt": 1000, "Horsepower": 745.7}
        if category == "Power":
            return value * power_units[from_unit] / power_units[to_unit]

        # Angle (base: Degree)
        angle_units = {"Degree": 1, "Radian": 57.2958}
        if category == "Angle":
            return value * angle_units[from_unit] / angle_units[to_unit]

        # Frequency (base: Hertz)
        frequency_units = {"Hertz":1, "Kilohertz":1000, "Megahertz":1e6}
        if category == "Frequency":
            return value * frequency_units[from_unit] / frequency_units[to_unit]

        # Force (base: Newton)
        force_units = {"Newton":1, "Dyne":1e-5, "Pound-force":4.44822}
        if category == "Force":
            return value * force_units[from_unit] / force_units[to_unit]

        # Data Transfer Speed (base: Mbps)
        transfer_units = {"Mbps":1, "Gbps":1000, "KBps":0.008}
        if category == "Data Transfer Speed":
            return value * transfer_units[from_unit] / transfer_units[to_unit]

        # Default
        return value
