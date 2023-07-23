class NotANumber(Exception):
    pass


def divide(numerator, denominator):
    try:
        if denominator == 0:
            raise ZeroDivisionError("You can't divide by '0'. Please try again.")
        if not isinstance(denominator, (int, float)):
            raise NotANumber("This is not a number. Please try again.")
        return numerator / denominator
    except ZeroDivisionError as e:
        raise ZeroDivisionError("You can't divide by '0'. Please try again.") from e


# Input/draft testing code
# if __name__ == '__main__':
#     num_input = int(input("Please enter your numerator: "))
#     denom_input = int(input("Please enter your denominator: "))
#     result = divide(num_input, denom_input)
#     print(int(result))


# ORIGINAL CODE
# def divide():
#     numerator = int(input("Please enter your numerator: "))
#     denominator = int(input("Please enter your denominator: "))
#     print(numerator / denominator)
