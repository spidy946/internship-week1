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
weights = []

# Input and store data for each pupil
for i in range(class_size):
    name = input(f"Enter name for pupil {i + 1}: ")
    weight_input = input(f"Enter weight for {name}: ")

    # Validate weight input
    while not validate_weight(weight_input):
        weight_input = input(f"Enter weight for {name}: ")

    # Store valid data
    names.append(name)
    weights.append(float(weight_input))

# Output names and weights of pupils
print("\nNames and Weights of Pupils:")
for i in range(class_size):
    print(f"{names[i]}: {weights[i]} kilograms")
