import sys


def star_length(n):
    return 2*(input_value - abs(n - input_value)) - 1


def space_length(n):
    return (longest_star - star_length(n)) // 2


def print_diamond_row(n):
    if n >= 2 * input_value:
        return ""
    else:
        return " "*space_length(n) + "*"*star_length(n) + "\n" + print_diamond_row(n+1)


try:
    input_value = int(sys.argv[1])
    assert input_value >= 0
    longest_star = star_length(input_value)
    print(print_diamond_row(1).rstrip("\n"))
except (ValueError, AssertionError):
    print("Invalid Argument. Please provide a non-negative integer.")
except IndexError:
    print("Missing a required argument. Please provide a non-negative integer.")
