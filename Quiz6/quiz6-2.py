import sys
try:
    input_value = int(sys.argv[1])
    assert input_value != 0
    star_counts = [2*(input_value - abs(input_value - i)) - 1 for i in range(1, 2*input_value)]
    longest_star = max(star_counts)
    diamond_rows = [" "*((longest_star - star_count)//2) + "*" * star_count + "\n" for star_count in star_counts]
    print("".join(diamond_rows).rstrip("\n"))
except ValueError:
    print("Invalid Argument. Please provide a non-negative integer.")
except IndexError:
    print("Missing a required argument. Please provide a non-negative integer.")
except AssertionError:
    print("")
