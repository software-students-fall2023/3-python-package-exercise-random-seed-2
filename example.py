from math_randomseed.math_randomseed import add, subtract, multiply, divide

def main():
    # addition
    sum_result = add(10, 5)
    print(f"The sum of 10 and 5 is {sum_result}.")

    # subtraction
    difference = subtract(10, 5)
    print(f"The difference between 10 and 5 is {difference}.")

    # multiplication
    product = multiply(10, 5)
    print(f"The product of 10 and 5 is {product}.")

    # division
    quotient = divide(10, 5)
    print(f"The quotient of 10 divided by 5 is {quotient}.")

    # divison by zero handling 
    try:
        divide_by_zero = divide(10, 0)
    except ZeroDivisionError as e:
        print(f"Caught an error when trying to divide by zero: {e}")

if __name__ == "__main__":
    main()
