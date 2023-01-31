#  Name : Barış Yıldız | Student ID : 2210356107
import sys
base = int(sys.argv[1])
exponent = int(sys.argv[2])
number = base ** exponent
output = "{}^{}".format(base, exponent)

while (number >= 10 or number <= -10) or (int(number) != number):
    output = output + "={}=".format(number)
    new_number = 0
    for i in range(len(str(number))):       # go over every digit of the number and add them up.
        if str(number)[i] == "." or str(number)[i] == "-":
            continue
        output = output + "{}+".format(str(number)[i])
        new_number += int(str(number)[i])
    number = new_number
    output = output.rstrip("+")         # strip a + sign from the end because there should be no operator at the end of a mathematical expression.

if abs(number) != number:       # if the number is negative and greater than -10, it will skip the while loop and go into this if statement.
    output = output + "={}={}".format(number, abs(number))
else:
    output = output + "={}".format(abs(number))
print(output)
