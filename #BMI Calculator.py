#BMI Calculator

def calculate_bmi(weight, height, system):
    try:
        if system == 'metric':
            bmi = weight / (height ** 2)
        elif system == 'imperial':
            bmi = (weight / (height ** 2)) * 703
        else:
            raise ValueError("Invalid measurement system. Please enter 'metric' or 'imperial'.")
        
        return bmi
    except ZeroDivisionError:
        raise ValueError("Height should not be zero.")
    except Exception as e:
        raise ValueError(f"Error: {e}")

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

try:
    measurement_system = input("Choose measurement system (metric/imperial): ").lower()
    
    if measurement_system not in ['metric', 'imperial']:
        raise ValueError("Invalid measurement system. Please enter 'metric' or 'imperial'.")
    
    weight = float(input("Enter your weight: "))
    height = float(input("Enter your height: "))
    
    bmi = calculate_bmi(weight, height, measurement_system)
    classification = classify_bmi(bmi)
    
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Classification: {classification}")
    
except ValueError as ve:
    print(f"Error: {ve}")