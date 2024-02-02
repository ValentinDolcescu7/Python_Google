# for finding the greatest common divisor of two integer numbers
from math import gcd


class Fractie:

    # Initialize the fraction
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    # Get the fraction as a string
    def __str__(self):
        return f'{self.numarator}/{self.numitor}'

    # Add two fractions
    def __add__(self, other):
        # Get the greatest common divisor of the two denominators
        cmmdc = gcd(self.numitor, other.numitor)
        numarator = self.numarator * \
            (other.numitor // cmmdc) + other.numarator * (self.numitor // cmmdc)
        numitor = self.numitor * other.numitor // cmmdc

        return Fractie.simplify(numarator, numitor)

    # Subtract two fractions
    def __sub__(self, other):
        # Get the greatest common divisor of the two denominators
        cmmdc = gcd(self.numitor, other.numitor)
        numarator = self.numarator * \
            (other.numitor // cmmdc) - other.numarator * (self.numitor // cmmdc)
        numitor = self.numitor * other.numitor // cmmdc

        return Fractie.simplify(numarator, numitor)

    # Get the inverse of the fraction
    def inverse(self):
        return Fractie.simplify(self.numitor, self.numarator)

    # Simplify a fraction
    @staticmethod
    def simplify(numarator, numitor):
        cmmdc = gcd(numarator, numitor)
        return Fractie(numarator // cmmdc, numitor // cmmdc)


def main():

    # Define two different fractions
    f1 = Fractie(1, 12)
    f2 = Fractie(1,4)

    # Print the sum of the two fractions
    print(f'Suma celor doua fractii este:  {f1 + f2}')

    # Print the difference of the two fractions
    print(f'Diferenta celor doua fractii este: {f2 - f1}')

    # Print the inverse of the first fraction
    print(f'Inversa primei fractii este: {f1.inverse()}')


if __name__ == '__main__':
    main()
