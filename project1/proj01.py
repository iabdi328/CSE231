"""
 rod = 5.0292 meters
• 1 furlong = 40 rods
• 1 mile = 1609.34 meters
• 1 foot = 0.3048 meters
• average walking speed is 3.1 miles per hour
"""

def rodconversion(userInput):
    # for minute to walk
    metersPerRod = 5.0292
    metersPerMile = 1609.34
    speedMPM = 3.1 / 60

    # Convert rods to various units
    milesPerRod = metersPerRod / metersPerMile
    # Calculate the time to walk 1 rod in minutes
    timePerRod = milesPerRod / speedMPM

    conMeters = round(userInput * 5.0292, 3)
    conFeet = round(userInput * 16.5, 3)
    conMiles = round(userInput * 0.003125, 3)
    conFurlongs = round(userInput * 0.025, 3)
    timeToWalkRods = round(userInput * timePerRod, 3)

    return (f"Conversions\nMeters: {conMeters}\nFeet: {conFeet}\nMiles {conMiles}\nFurlongs"
            f"{conFurlongs}\nMinutes to walk rods: {timeToWalkRods}")


def main():
    while True:
        #get user input
        userInput = (input("\n:~Input rods or press q to quit ~:"))
        #case to exit the program
        if userInput == "q":
            break
        try:
            #converts user input to float
            userInput = float(userInput)

            print("\nYour value is", userInput, "rods.\n")

            #run rodconversion function
            result = rodconversion(userInput)
            print(result)

        #if value not able to convert to float
        except ValueError:
            print("Invalid input. Please enter a numeric value or 'q' to quit.")


if __name__ == "__main__":
    main()
