def divide(a: float, b: float) -> float:
    """
    Divide two numbers and return the result.

    Args:
        a (float): The numerator (number to be divided).
        b (float): The denominator (number to divide by).

    Returns:
        float: The result of a / b.

    Raises:
        ZeroDivisionError: If b is 0, since division by zero is undefined.
        TypeError: If a or b is not a number (int/float).
    """
    # Guard against invalid input types before attempting the operation
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both 'a' and 'b' must be numbers (int or float).")

    # Guard against division by zero — this is the most common failure point
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return a / b


# Example usage / quick test block.
# Wrapped in a try-except so the script doesn't crash ungracefully,
# and prints a clear message if something goes wrong.
if __name__ == "__main__":
    try:
        result = divide(10, 2)
        print(f"10 / 2 = {result}")

        # Uncomment the line below to see the ZeroDivisionError handling in action:
        # divide(5, 0)

    except (ZeroDivisionError, TypeError) as e:
        print(f"Error: {e}")
