class_size = 5

# Function to validate weight
def validate_weight(weight):
    try:
        weight = float(weight)
        if 10 <= weight <= 200:
            return True
        else:
            print("Invalid weight! Weight must be between 10 and 200 kilograms.")
            return False
    except ValueError:
        print("Invalid input! Please enter a valid weight.")
        return False

# Initialize arrays
names = []
weights_first_day = []
weights_last_day = []
weight_differences = []

# Input and store data for each pupil on the first day
print("Input weights on the first day:")
for i in range(class_size):
    name = input(f"Enter name for pupil {i + 1}: ")
    weight_input = input(f"Enter weight for {name} on the first day: ")

    # Validate weight input
    while not validate_weight(weight_input):
        weight_input = input(f"Enter weight for {name} on the first day: ")

    # Store valid data
    names.append(name)
    weights_first_day.append(float(weight_input))

# Input and store data for each pupil on the last day
print("\nInput weights on the last day:")
for i in range(class_size):
    weight_input = input(f"Enter weight for {names[i]} on the last day: ")

    # Validate weight input
    while not validate_weight(weight_input):
        weight_input = input(f"Enter weight for {names[i]} on the last day: ")

    # Store valid data
    weights_last_day.append(float(weight_input))

# Calculate and store the difference in weight for each pupil
for i in range(class_size):
    difference = weights_last_day[i] - weights_first_day[i]
    weight_differences.append(difference)

# Output names, weights on the first day, weights on the last day, and differences
print("\nNames, Weights on the First Day, Weights on the Last Day, and Differences:")
for i in range(class_size):
    print(f"{names[i]}: First Day - {weights_first_day[i]} kg, Last Day - {weights_last_day[i]} kg, Difference - {weight_differences[i]} kg")

# Output pupils with a difference in weight of more than 2.5 kilograms
print("\nPupils with a Difference in Weight of More than 2.5 kilograms:")
for i in range(class_size):
    if abs(weight_differences[i]) > 2.5:
        if weight_differences[i] > 0:
            message = "rise"
        else:
            message = "fall"
        print(f"{names[i]}: Difference - {weight_differences[i]} kg, {message}")
