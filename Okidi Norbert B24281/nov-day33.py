class Calculator:
    def add(self, *args):
        if len(args) ==2:
            return args[0] + args[1]
        elif len(args) == 1 and isinstance(args[0], list):
            return sum(args[0])
        else:
            raise ValueError("Unsupported arguments for addition")
    
class ScientificCalculator(Calculator):
    def add(self, *args):
        total = super().add(*args)
        return f"Result: {total: .2e}"

calc = Calculator()

result1 = calc.add(5, 7)
print(f"Result(two numbers): {result1}")


result2 = calc.add([2, 4, 6])
print(f"Result (List of numbers): {result2}")


scientific_calc = ScientificCalculator()

result3 = scientific_calc.add(1e6,2e7)
print(result3)