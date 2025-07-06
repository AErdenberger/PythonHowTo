scores = [95, 98, 97, 96, 97, 93, 94, 100, 99, 98]

total = sum(scores)
num_scores = len(scores)
average = total / num_scores

print(f"Your Average Score is: {average:.2f}")

wholesale_dict = {"name" : "Vacuum", "price" : 130.67}

print(f"Wholesale Price: ${wholesale_dict['price']:.2f}")

def cast_number(number_str_):
    try:
        casted_number = float(number_str_)
    except ValueError:
        print(f"Couldn't cast {repr(number_str_)} to a number")
    else:
        print(f"Casting {repr(number_str_)} to: {casted_number}")

cast_number("123.45")