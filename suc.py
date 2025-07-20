# The title regarding what the program is about
print('***** Simple Unit Conversion *****\n')
# First declare a function that converts Celsuis to Fahrenheit
def celsuis_to_fahrenheit():
    # Declared variable user_input is created that contains the user's prompt
    user_input = int(input('Please enter a value: '))
    # Declared a fahrenheit vairable that contains the calculation of temperature
    fahrenheit = (user_input * 9/5) + 32
    # Return the converted value in fahrenheit to the caller
    return fahrenheit
# Declared a function for the Fahrenheit to Celsuis conversion
def fahrenheit_to_celsuis():
    # Declared variable user_input is created that contains the user's prompt
    user_input = int(input('Please enter a value: '))
    # Declared a celsuis vairable that contains the calculation of temperature
    celsuis = (user_input - 32) * 5/9
    # Return the converted value in celsuis to the caller
    return celsuis
# Declared a function for the Kilometers to Miles conversion
def kilometers_to_miles():
    # Declared variable user_input is created that contains the user's prompt
    user_input = int(input('Please enter a value: '))
    # Declared a miles vairable that contains the calculation of temperature
    miles = user_input * 0.621371
    # Return the converted values in user_input and miles to the caller
    return user_input, miles
# Declared a function for the Miles to Kilometers conversion
def miles_to_kilometers():
    # Declared variable user_input is created that contains the user's prompt
    user_input = int(input('Please enter a value: '))
    # Declared a kilometers vairable that contains the calculation of temperature
    kilometers = user_input / 0.621371
    # Return the converted values in user_input and kilometers to the caller
    return user_input, kilometers
# Declared a function for the Kilograms to Pounds conversion
def kilograms_to_pounds():
    # Declared variable user_input is created that contains the user's prompt
    user_input = int(input('Please enter a value: '))
    # Declared a pounds vairable that contains the calculation of temperature
    pounds = user_input * 2.20462
    # Return the converted values in user_input and pounds to the caller
    return user_input, pounds
# Declared a function for the Pounds to Kilograms conversion
def pounds_to_kilograms():
    # Declared variable user_input is created that contains the user's prompt
    user_input = int(input('Please enter a value: '))
    # Declared a kilograms vairable that contains the calculation of temperature
    kilograms = user_input / 2.20462
    # Return the converted values in user_input and kilograms to the caller
    return user_input, kilograms
# Declared a function for the Meters to Feet conversion
def meters_to_feet():
    # Declared variable user_input is created that contains the user's prompt
    user_input = int(input('Please enter a value: '))
    # Declared a feet vairable that contains the calculation of temperature
    feet = user_input * 3.28084
    # Return the converted values in user_input and feet to the caller
    return feet
# Declared a function for the Feet to Meters conversion
def feet_to_meters():
    # Declared variable user_input is created that contains the user's prompt
    user_input = int(input('Please enter a value: '))
    # Declared a meters vairable that contains the calculation of temperature
    meters = user_input / 3.28084
    # Return the converted values in user_input and meters to the caller
    return meters
# Declared a function for the Liters to Gallons conversion
def liters_to_gallons():
    # Declared variable user_input is created that contains the user's prompt
    user_input = int(input('Please enter a value: '))
    # Declared a gallons vairable that contains the calculation of temperature
    gallons = user_input * 0.264172
    # Return the converted values in user_input and gallons to the caller
    return user_input, gallons
# Declared a function for the Gallons to Liters conversion
def gallons_to_liters():
    # Declared variable user_input is created that contains the user's prompt
    user_input= int(input('Please enter a value: '))
    # Declared a liters vairable that contains the calculation of temperature
    liters = user_input / 0.264172
    # Return the converted values user_input and liters to the caller
    return user_input, liters
# Created a set of variables with each containing different strings for users to select as options
option1 = '1. Celsuis to Fahrenheit'
option2 = '2. Fahrenheit to Celsuis'
option3 = '3. Kilometers to Meters'
option4 = '4. Meters to Kilometers'
option5 = '5. Kilograms to Pounds'
option6 = '6. Pounds to Kilograms'
option7 = '7. Meters to Feet'
option8 = '8. Feet to Meters'
option9 = '9. Liters to Gallons'
option10 = '10. Gallons to Liters'
option11 = '11. Exit'
# Declared a function that will handle the sole logic of the unit conversion program
def conversion_menu():
    # Prints all the varaible options aligning them vertically by adding a \n at the end of each variable
    print(f"{option1}\n{option2}\n{option3}\n{option4}\n{option5}\n{option6}\n{option7}\n{option8}\n{option9}\n{option10}\n{option11}\n")
    # Declared variable user_choice is created that contains the user's prompt
    user_choice = int(input('What would you like to convert today: '))
    # Wrote an if statement to determine the condition based on the user's prompt
    if user_choice == 1:
        # If the user_choice value equaled to 1 then a converted_value variable is created storing the result returned by the celsuis_to_fahrenheit() function
        converted_value = celsuis_to_fahrenheit()
        # Prints a message after a successful conversion
        print("\nConversion Success!")
        # Prints the final result of the conversion
        print(f"The converted temperature is {round(converted_value)}°F\n")
        # Calls the Conversion Menu
        conversion_menu()
    elif user_choice == 2:
        # If the user_choice value equaled to 2 then a converted_value variable is created storing the result returned by the fahrenheit_to_celsuis() function
        converted_value = fahrenheit_to_celsuis()
        # Prints a message after a successful conversion
        print("\nConversion Success!")
        print(f"The converted temperature is {round(converted_value)}°C\n")
        # Calls the Conversion Menu
        conversion_menu()
    elif user_choice == 3:
        # If the user_choice value equaled to 3 then a original_value and converted_value variable are created storing the results returned by the kilometers_to_miles() function
        original_value, converted_value = kilometers_to_miles()
        # Prints a message after a successful conversion
        print("\nConversion Success!")
        # Prints the final result of the conversion
        print(f"The distance of {original_value}km converts to {converted_value:.2f}mi\n")
        # Calls the Conversion Menu
        conversion_menu()
    elif user_choice == 4:
        # If the user_choice value equaled to 4 then a original_value and converted_value variable are created storing the results returned by the miles_to_kilometers() function
        original_value, converted_value = miles_to_kilometers()
        # Prints a message after a successful conversion
        print("\nConversion Success!")
        # Prints the final result of the conversion
        print(f"The distance of {original_value}mi converts to {converted_value:.2f}km\n")
        # Calls the Conversion Menu
        conversion_menu()
    elif user_choice == 5:
        # If the user_choice value equaled to 5 then a original_value and converted_value variable are created storing the results returned by the kilograms_to_pounts() function
        original_value, converted_value = kilograms_to_pounds()
        # Prints a message after a successful conversion
        print("\nConversion Success!")
        # Prints the final result of the conversion
        print(f"{original_value}kg is equal to {converted_value:.2f}lb\n")
        # Calls the Conversion Menu
        conversion_menu()
    elif user_choice == 6:
        # If the user_choice value equaled to 6 then a original_value and converted_value variable are created storing the results returned by the pounds_to_kilograms() function
        original_value, converted_value = pounds_to_kilograms()
        # Prints a message after a successful conversion
        print("\nConversion Success!")
        # Prints the final result of the conversion
        print(f"{original_value}lb is equal to {converted_value:.2f}kg\n")
        # Calls the Conversion Menu
        conversion_menu()
    elif user_choice == 7:
        # If the user_choice value equaled to 7 then a converted_value variable is created storing the result returned by the meters_to_feet() functions
        converted_value = meters_to_feet()
        # Prints a message after a successful conversion
        print("\nConversion Success!")
        # Prints the final result of the conversion
        print(f"The converted length is {converted_value:.2f}ft\n")
        # Calls the Conversion Menu
        conversion_menu()
    elif user_choice == 8:
        # If the user_choice value equaled to 8 then a converted_value variable is created storing the result returned by the feet_to_meters() function
        converted_value = feet_to_meters()
        # Prints a message after a successful conversion
        print("\nConversion Success!")
        # Prints the final result of the conversion
        print(f"The converted length is {round(converted_value)}m\n")
        # Calls the Conversion Menu
        conversion_menu()
    elif user_choice == 9:
        # If the user_choice value equaled to 9 then a original_value and converted_value variable are created storing the results returned by the liters_to_gallons() function
        original_value, converted_value = liters_to_gallons()
        # Prints a message after a successful conversion
        print("\nConversion Success!")
        # Prints the final result of the conversion
        print(f"{original_value}L is equal to {round(converted_value)}gal\n")
        # Calls the Conversion Menu
        conversion_menu()
    elif user_choice == 10:
        # If the user_choice value equaled to 10 then a original_value and converted_value variable are created storing the results returned by the gallons_to_liters() function
        original_value, converted_value = gallons_to_liters()
        # Prints a message after a successful conversion
        print("\nConversion Success!")
        # Prints the final result of the conversion
        print(f"The volume of {original_value}gal converts to {round(converted_value)}L\n")
        # Calls the Conversion Menu
        conversion_menu()
    elif user_choice == 11:
        # Else if the user_choice value equaled to 11 then a goodbye message is printed then the conversion_menu function stops
        print("Goodbye! Stay curious and keep converting!")
        exit()
    else:
        # Else if the user_choice value does not equal to any number between 1 to 11 or a word is prompted instead of a string the the message below is displayed
        print(f"Please enter a valid choice (numbers 1–11 only).")
        conversion_menu()
# The conversion_menu is called when the session starts
conversion_menu()
