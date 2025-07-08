scores = [95, 98, 97, 96, 97, 93, 94, 100, 99, 98]

total = sum(scores)
num_scores = len(scores)
average = total / num_scores

print(f"Your Average Score is: {average:.2f}")

wholesale_dict = {"name" : "Vacuum", "price" : 130.67}

print(f"Wholesale Price: ${wholesale_dict['price']:.2f}")

####################################

def cast_number(number_str_):
    try:
        casted_number = float(number_str_)
    except ValueError:
        print(f"Couldn't cast {repr(number_str_)} to a number")
    else:
        print(f"Casting {repr(number_str_)} to: {casted_number}")

cast_number("123.45")

###################################

list_str = "[1, 2, 3, 4, 5]"
stripped_list = list_str.strip("[]")
number_list = {int(num) for num in stripped_list.split(",")}

print(f"Number List: {number_list}")
#expected output: {1, 2, 3, 4, 5}

####################################

def get_temperature():
    user_input = input("Enter the temperature: ")
    try:
        number = float(user_input)
    except ValueError:
        print(f"Invalid input: {user_input} is not a number.")
        return None
    else:
        if number < 10:
            print(f"you entered: {number}, it's cold!")
        elif number > 10 and number <= 25:
            print(f"you entered: {number}, it's warm!")
        else:
            print(f"you entered: {number}, it's hot!")

get_temperature()

####################################

import ast

def get_user_input():
    user_input = input("Enter something: ")
    try:
        safe_value = ast.literal_eval(user_input)
    except (ValueError, SyntaxError):
        print(f"Invalid input: {user_input} is not a valid Python literal.")
        return None
    return type(safe_value)

get_user_input()

####################################

#split vs rsplt

def split_example():
    text = "Hello, World!"
    split_text = text.split(", ")
    print(f"Split Text: {split_text}") # Expected output: ['Hello', 'World!']

def rsplit_example():
    text = "Hello, World!"
    rsplit_text = text.rsplit(", ", 0)
    print(f"RSplit Text: {rsplit_text}") # Expected output: ['Hello', 'World!']

split_example()
rsplit_example()

####################################

# Basic splitting
text = "apple,banana,cherry"
result = text.split(",")
print(result)  # ['apple', 'banana', 'cherry']

# Splitting on whitespace (default)
text = "Python is fun"
print(text.split())  # ['Python', 'is', 'fun']

# Using maxsplit
text = "a-b-c-d"
print(text.split("-", maxsplit=2))  # ['a', 'b', 'c-d']

# Splitting with a limit
text = "one two three four"
print(text.split(" ", 2))  # ['one', 'two', 'three four

# Splitting with a custom separator
text = "apple;banana;cherry"
print(text.split(";"))  # ['apple', 'banana', 'cherry']

# Splitting with a separator that doesn't exist
text = "apple banana cherry"
print(text.split(","))  # ['apple banana cherry']

# Splitting an empty string
text = ""
print(text.split())  # []

#############################################

# Joining a list of words
words = ["Python", "is", "awesome"]
result = " ".join(words)
print(result)  # Python is awesome

# Joining with custom separator
items = ["apple", "banana", "cherry"]
print(",".join(items))  # apple,banana,cherry

# Joining characters
chars = ['P', 'y', 't', 'h', 'o', 'n']
print("".join(chars))  # Python

# Joining with an empty list
empty_list = []
print(" ".join(empty_list))  # (prints nothing, no error)

# Joining with a single string
single_string = "Hello"
print(" ".join(single_string))  # H e l l o

# Joining with a list containing non-string types
mixed_list = ["Python", 3, "is", "fun"]
try:
    print(" ".join(mixed_list))  # Raises TypeError
except TypeError as e:
    print(f"Error: {e}")

# Joining with a list containing None
none_list = ["Python", None, "is", "fun"]
try:
    print(" ".join(none_list))  # Raises TypeError
except TypeError as e:
    print(f"Error: {e}")

# Joining with a list containing empty strings
empty_strings = ["", "Python", "", "is", "", "fun"]
print(" ".join(empty_strings))  # Python is fun (ignores empty strings)

#############################################