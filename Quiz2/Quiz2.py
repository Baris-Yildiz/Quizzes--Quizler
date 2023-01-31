import sys

if __name__ == '__main__' :
    try:
        # PROBLEM 1 : Basketball Score Calculator
        two_point = int(sys.argv[1])
        three_point = int(sys.argv[2])
        single_point = int(sys.argv[3])
        negative_checker = 1 / (abs(two_point + 1) + two_point + 1) + 1 / (abs(three_point + 1) + three_point + 1) + 1 / (abs(single_point + 1) + single_point + 1)  # this line is for breaking the program if any input is a negative number.
        output = two_point * 2 + three_point * 3 + single_point
        print(output)
        # END OF PROBLEM 1
    except:
        print(-1)

# PROBLEM 2 : Body Mass Index Calculator
def healthStatus(height, mass):
    try:
        bmi = mass / (height**2) + 0 * (1 / (abs(height) + height) + 1 / (abs(mass) + mass))  # the 0 * (1 / (abs(height) + height) + 1 / (abs(mass) + mass)) part is for breaking the program if any input is not a positive integer. It doesn't affect the bmi as it is multiplied by zero afterwards.
        if bmi >= 30:
            return "obese"
        elif bmi >= 24.9:
            return "overweight"
        elif bmi >= 18.5:
            return "healthy"
        else:
            return "underweight"
    except:
        return ""
# END OF PROBLEM 2
