#!/usr/bin/python3

def uppercase(input_str):
    for char in input_str:
        # Check if the character is lowercase
        if ord('a') <= ord(char) <= ord('z'):
            # Convert to uppercase using ASCII values
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
        else:
            # Leave the character unchanged if it's not lowercase
            uppercase_char = char

        # Print the uppercase character without a newline
        print(uppercase_char, end="")

    # Print a newline after the loop
    print()

# Example usage
uppercase("Hello, World!")
