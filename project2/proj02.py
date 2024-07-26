def galacticCalculation (ostart, oend):
    """Calculates the galactic distance between two points. Light years travelled"""
    ostart = float(ostart)
    oend = float(oend)

    if oend >= ostart:
        result = oend - ostart
    else:
        result = (999999 - ostart + 1) + oend

    return result / 10

def xylophoneVoyager(days, odostart, odoend):
    baseCharge = 40.00
    lightYearCharge = 0.25
    lightYearsTraveled = galacticCalculation(odostart, odoend)
    baseCharge = (baseCharge * int(days)) + (lightYearsTraveled * lightYearCharge)
    result = (f"Code: XV\n\tDays in orbit: {days}\n\tLiftoff odometer: {int(odostart)}\n\tTouchdown odometer:{int(odoend)}\n\tLight-years traveled: {lightYearsTraveled}"
              f"\n\tCost in star credits: ${baseCharge:.2f} ")

    return result





def extraterrestrialExplorer(days, odostart, odoend):
    baseCharge = 60.00 #$60.00 for each day
    lightYearCharge = 0
    lightYearsTraveled = galacticCalculation(odostart, odoend)

    averagePerDay = lightYearsTraveled / int(days)

    if  averagePerDay <= 100:
        lightYearCharge = 0
        baseCharge = baseCharge * int(days)
    else:
        lightYearCharge = 0.25
        baseCharge = baseCharge * int(days) + (( lightYearsTraveled * lightYearCharge) - 100)


    result = (
        f"Code: ET\n\tDays in orbit: {days}\n\tLiftoff odometer: {int(odostart)}\n\tTouchdown odometer:{int(odoend)}\n\tLight-years traveled: {lightYearsTraveled}"
        f"\n\tCost in star credits: ${baseCharge:.2f} ")

    return result


def SpaceInvader(days, odostart, odoend):
    baseCharge = 190.00  #
    lightYearCharge = 0
    LightYearsTraveled = galacticCalculation(odostart, odoend)

    #week calculation
    fullWeek = int(days) // 7
    remainingDays = int(days) % 7

    if remainingDays > 0:
        fullWeek += 1

    averagePerWeek = LightYearsTraveled / fullWeek
    print(averagePerWeek)

    if averagePerWeek <= 900:
        lightYearCharge = 0
        baseCharge = baseCharge * fullWeek
    elif averagePerWeek > 900 and averagePerWeek <= 1500:
        lightYearCharge = 100.00 * fullWeek
        baseCharge = baseCharge + lightYearCharge
    else:
        lightYearCharge = (200.00 * fullWeek) + ((LightYearsTraveled - (fullWeek * 1500) ) * 0.25)
        baseCharge = (baseCharge * fullWeek) + lightYearCharge

    result = (
        f"Code: SI\n\tDays in orbit: {days}\n\tLiftoff odometer: {int(odostart)}\n\tTouchdown odometer:{int(odoend)}\n\tLight-years traveled: {LightYearsTraveled}"
        f"\n\tCost in star credits: ${baseCharge:.2f} ")

    return result









def main():
    INTERGALACTIC_BANNER = """
    Welcome to SpaceX Galactic Car Extravaganza!

    Prepare for an interstellar joyride with our cosmic cruisers!
    At the prompt, please enter:
    - Galactic code (XV, ET, SI)
    - Days of your interstellar joyride
    - Odometer at liftoff
    - Odometer at touchdown
    """

    print(INTERGALACTIC_BANNER)


    while True:
        userInput = input(":~Ready for an out-of-this-world adventure (Y/X)? ~:")
        if userInput == "X" or userInput == "x":
            break

        galacticCode = input("\n:~Galactic code (XV, ET, SI) ~:")
        numberOfDays = input("\n:~Number of days (int) ~:")
        OdoAtliftOff = input("\n:~Odometer at liftoff (int) ~:")
        OdoAtTouchdown = input("\n:~Odometer at touchdown (int) ~:")
        print("\nThank you for entrusting us with your joyride!")

        if galacticCode == "XV":
            result = xylophoneVoyager(numberOfDays, OdoAtliftOff, OdoAtTouchdown)
        elif galacticCode == "ET":
            result = extraterrestrialExplorer(numberOfDays, OdoAtliftOff, OdoAtTouchdown)
        elif galacticCode == "SI":
            result = SpaceInvader(numberOfDays, OdoAtliftOff, OdoAtTouchdown)
        print(result)


    print("\nThank you for entrusting us with your joyride!")



if __name__ == "__main__":
    main()



