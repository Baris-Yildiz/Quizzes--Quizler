import sys


def find_sequence(*args):  # args stores div, nondiv, lower_limit, upper_limit.
    """ Returns a sequence from a lower limit (args[2]) to an upper one (args[3])
    made of integers that are divisible by div (args[0], but not divisible by non-div (args[1]). """
    sequence = list()
    for number in range(args[2], args[3] + 1):
        if number % args[0] == 0 and number % args[1] != 0:
            sequence.append(str(number))
    return sequence


def round_number(number):
    """ Rounds the provided number. If its decimal part is lower than 5, floors it; otherwise, ceils it. """
    number = float(number)
    decimal_part = number - int(number)
    return int(number) if decimal_part < .5 else int(number) + 1


try:    # tries to open the file and handles file or command line exceptions
    operand_file, result_file = sys.argv[1], sys.argv[2]
    with open(operand_file) as f:
        operands = f.readlines()
    with open(result_file) as f:
        results = f.readlines()
except IndexError:
    print("IndexError: number of input files less than expected.")
except IOError as error:
    error_message = str(error)
    problematic_file = error_message[error_message.index("\'")+1:-1]   # gets the name of the file causing errors
    print(f"IOError: cannot open {problematic_file}")
except:
    print("kaBOOM: run for your life!")
else:
    error_messages = {IndexError: "IndexError: number of operands less than expected.", ZeroDivisionError: "ZeroDivisionError: You can't divide by 0.", ValueError: "ValueError: only numeric input is accepted."}
    for line_index in range(len(operands)):
        line_operands = operands[line_index].rstrip("\n").split()
        try:
            my_sequence = find_sequence(*(round_number(line_operands[index]) for index in range(4)))    # my_sequence is the result sequence we find.
        except (ValueError, IndexError, ZeroDivisionError) as error:
            print("------------\n{}\nGiven input: {}".format(error_messages[type(error)], " ".join(line_operands)))
            continue
        except:
            print("------------\nkaBOOM: run for your life!\nGiven input: {}".format(" ".join(line_operands)))
            continue
        try:
            result_sequence = results[line_index].rstrip("\n").split()  # result sequence is the result sequence we are provided with / we should compare our results with.
            print("------------\nMy results: \t\t{}".format(" ".join(my_sequence)))
            print("Results to compare: \t{}".format(" ".join(result_sequence)))
            assert result_sequence == my_sequence
            print("Goool!!!")
        except AssertionError:
            print("AssertionError: results don't match.")
            continue
        except:
            print("------------\nkaBOOM: run for your life!")
finally:
    print("~ Game Over ~")
