def add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            return "Error: Cannot divide by zero."
        result /= num
    return result

def calculator():
    while True:
        print("\n--- Command-Line Calculator ---")
        print("Select an operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit")

        user_choice = input("Enter your choice (1-5): ")

        if user_choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        if user_choice in ('1', '2', '3', '4'):
            try:
                nums_input = input("Enter numbers separated by space: ")
                numbers = [float(num) for num in nums_input.split()]
                if len(numbers) < 2:
                    print("Please enter at least two numbers.")
                    continue
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                continue

            if user_choice == '1':
                print(f"Result: {' + '.join(map(str, numbers))} = {add(numbers)}")
            elif user_choice == '2':
                print(f"Result: {' - '.join(map(str, numbers))} = {subtract(numbers)}")
            elif user_choice == '3':
                print(f"Result: {' * '.join(map(str, numbers))} = {multiply(numbers)}")
            elif user_choice == '4':
                result = divide(numbers)
                print(f"Result: {' / '.join(map(str, numbers))} = {result}")
        else:
            print("Invalid choice. Please select an option from 1 to 5.")

if __name__ == "__main__":
    calculator()
