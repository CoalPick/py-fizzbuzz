#FizzBuzz example

for num in range(1, 101):  # Range in Python and other languages go from a range of min to max - 1
    strOut = ""            # The string for the final output
    
    # For each Fizz, Buzz or other conditon in this dictionary, add it to the string
    conditions = { 3 : "Fizz", 5 : "Buzz" }
    for key in conditions:				# For numbers like 15 multiple conditions are met, so they need to be concatonated together
        if (num % key) == 0:
            strOut += conditions[key]	# Add the condition matching the key, i.e. Fizz from 3
    
    # Check if any conditions were met
    if strOut == "":
        print (str(num))	    # Output the number if no conditions were met
    else:
        print (strOut)		    # Output the string if any conditions are met

input("Press ENTER to exit...") # Stops the program from exiting automatically
