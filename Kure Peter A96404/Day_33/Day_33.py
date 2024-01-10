# overloading and overriding
class Calculator:
    def add(self, *args):
        if len(args) == 2:
            return args[0] + args[1]
        elif len(args) == 1 and isinstance(args[0], list):
            return sum(args[0])
        else:
            raise ValueError("Invalid input. Use two numbers or a list of numbers.")

class ScientificCalculator(Calculator):
    def add(self, *args):
        result = super().add(*args)
        if len(args) == 2 and all(isinstance(arg, str) for arg in args):
            try:
                num1 = float(args[0])
                num2 = float(args[1])
                return "{:.2e}".format(num1 + num2)
            except ValueError:
                raise ValueError("Invalid scientific notation")
        return result

# Example usage:
calc = Calculator()
result1 = calc.add(2, 3)
result2 = calc.add([1, 2, 3])

sci_calc = ScientificCalculator()
result3 = sci_calc.add(2, 3)
result4 = sci_calc.add("1.5e6", "2.7e6")

print(f"The sum of 2 and 3 is {result1}")  # Output: 5
print(f"The sum of a list containing 1,2 and 3 is: {result2}")  # Output: 6
print("Output from the scientific calculator class: ")
print(f"Addition of 2 and 3: {result3}")  # Output: 5
print(f"Addition of exponents: {result4}")  # Output: 4.20e+06
