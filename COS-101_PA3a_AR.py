# A program that asks the user to enter a number between 1 and 20 (inclusive). 
# It then prints out whether the number is between 
# 1 and 10 (inclusive) or between 11 and 20 (inclusive)
# or if it is not in the 1-20 range. 
# The following would be three sample runs of the program.

# Examples:
## Enter an integer in 1-20 range: 5
## It is between 1 and 10 (inclusive).
 
## Enter an integer in 1-20 range: 15
## It is between 11 and 20 (inclusive).
 
## Enter an integer in 1-20 range: 50
## It is not in the specified range.

class RangeChecker:
    def inputRangeChecker():
        
        # Prompt the user for input and validate as hard-typed integer
        numberInput = int(input("Enter an integer in 1-20 range: "))

        # Run checks on whether the number is inclusive or not
        # First check is between 1-10
        if 1 <= numberInput <= 10:
            # if the given number is between 1-10 then print out
            print("It is between 1 and 10 (inclusive).")
    
        elif 11 <= numberInput <= 20:
            # if the given number is between 1-10 then print out
            print("It is between 11 and 20 (inclusive).")
    
        else:
            # if the given number doesn't match the prior checks, print out that it isn't within the range
            print("It is not in the specified range.")            

        # Add a pause at the end, waiting for any input to proceed
        input("Press Enter to exit...")

    inputRangeChecker()
