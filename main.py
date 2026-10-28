"""
=========================================================
PYTHON PROGRAMS COLLECTION
Author: Sourabh Rathore
College: JECRC University, Jaipur
Course: B.Tech CSE (AI/ML)

Programs:
1. Factorial Calculator
2. Fibonacci Series Generator
3. Structure-to-Dictionary Conversion
=========================================================
"""


def factorial(number):
    """Calculate the factorial of a non-negative integer."""
    if number < 0:
        raise ValueError("Number cannot be negative.")

    result = 1

    for value in range(1, number + 1):
        result *= value

    return result


def fibonacci(count):
    """Generate the first 'count' Fibonacci numbers."""
    if count < 0:
        raise ValueError("Count cannot be negative.")

    sequence = []
    first, second = 0, 1

    for _ in range(count):
        sequence.append(first)
        first, second = second, first + second

    return sequence


def structure_to_dictionary(structure):
    """Convert a sequence of key-value pairs into a dictionary."""
    return dict(structure)


def display_menu():
    """Display the main program menu."""
    print("\n" + "=" * 50)
    print("          PYTHON PROGRAMS COLLECTION")
    print("          Created by Sourabh Rathore")
    print("=" * 50)
    print("1. Factorial Calculator")
    print("2. Fibonacci Series Generator")
    print("3. Structure-to-Dictionary Conversion")
    print("4. Exit")
    print("=" * 50)


def run_factorial():
    """Run the factorial calculator."""
    try:
        number = int(input("Enter a non-negative integer: "))

        if number < 0:
            print("Error: Please enter a non-negative integer.")
            return

        result = factorial(number)
        print(f"\nFactorial of {number} = {result}")

    except ValueError:
        print("Error: Please enter a valid whole number.")


def run_fibonacci():
    """Run the Fibonacci series generator."""
    try:
        count = int(input("How many Fibonacci numbers do you want? "))

        if count < 0:
            print("Error: Count cannot be negative.")
            return

        if count > 1000:
            print("Please enter a count of 1000 or less.")
            return

        result = fibonacci(count)
        print(f"\nFirst {count} Fibonacci numbers:")
        print(result)

    except ValueError:
        print("Error: Please enter a valid whole number.")


def run_dictionary_conversion():
    """Demonstrate conversion of key-value pairs into a dictionary."""
    structure = [
        ("name", "Sourabh Rathore"),
        ("college", "JECRC University, Jaipur"),
        ("course", "B.Tech CSE (AI/ML)"),
        ("semester", 3),
    ]

    converted_dictionary = structure_to_dictionary(structure)

    print("\nOriginal structure (list of key-value pairs):")
    print(structure)

    print("\nConverted dictionary:")
    for key, value in converted_dictionary.items():
        print(f"{key}: {value}")


def main():
    """Run the application."""
    print("\nWelcome to the Python Programs Collection!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            run_factorial()

        elif choice == "2":
            run_fibonacci()

        elif choice == "3":
            run_dictionary_conversion()

        elif choice == "4":
            print("\nThank you for using the Python Programs Collection!")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select an option from 1 to 4.")


if __name__ == "__main__":
    main()