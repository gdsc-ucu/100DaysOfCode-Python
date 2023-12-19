class Calculator:
    def add(self, x, y=None):
        if y is None:
            if isinstance(x, list):
                return sum(x)
            else:
                raise ValueError("If only one statement is accounted, it must be a list of numbers.")
        else:
            return x + y

class ScientificCalculator(Calculator):
    def add(self, a, b=None):
        if b is None:
            if isinstance(a, list):
                result = 0
                for num in a:
                    if isinstance(num, str):
                        result += self._parse_scientific_notation(num)
                    else:
                        result += num
                return result
            else:
                raise ValueError("If only one statement is accounted,, it must be a list of numbers or scientific notations.")
        else:
            if isinstance(a, str) or isinstance(b, str):
                return self._parse_scientific_notation(a) + self._parse_scientific_notation(b)
            else:
                return a + b

    def _parse_scientific_notation(self, num_str):
        try:
            parts = num_str.split('e')
            base = float(parts[0])
            exponent = int(parts[1])
            return base * 10 ** exponent
        except ValueError:
            raise ValueError("Invalid scientific notation: " + num_str)

