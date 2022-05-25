from Exceptions.UserDefinedException import MovieError

input_list = ["Admin Rating(1-10)", "Length", "Number of Shows in a day",
              "Language", "First show", "Interval Time", "Gap Between Shows",
              "Capacity"]


def check_num_or_not(value):
    if value.isdigit():
        return True
    return False


def validate_range(low, high, val):
    if low <= int(val) <= high:
        return True
    return False


def input_validator(field, value):
    if field == "Admin Rating(1-10)" or field == "Number of Shows in a day" or field == "Capacity":
        if not check_num_or_not(value):
            raise MovieError(field+" must be numeric value")
        if field == "Admin Rating(1-10)" and not validate_range(1, 10, value):
            raise MovieError("Rating must be between 1 and 10")
        if field == "Capacity" and not validate_range(1, 500, value):
            raise MovieError("Capacity must be between 1 and 500")
        # if field == "First show" or field == "Interval Time" or field == "Gap Between Shows":




