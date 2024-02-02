"""Să se scrie o clasă Fractie(numarator, numitor) care sa implementeze următoarele metode:
○ __init__ : instanțiem numărător și numitor
○ __str__ : afisam "numărător/numitor"
○ __add__ : returnam o noua fractie care reprezinta adunarea
○ __sub__: returnam o nouă fracție care reprezinta scădearea
○ inverse: returnează o nouă fracție (inversa fracției)
"""


class Fractie:
    def __init__(self, numarator, numitor):
        if numitor == 0:
            raise ValueError("Numitorul nu poate fi zero.")
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):
        return f"{self.numarator}/{self.numitor}"

    def __add__(self, other):
        comun_numitor = self.numitor * other.numitor
        suma_numarator = self.numarator * other.numitor + other.numarator * self.numitor
        return Fractie(suma_numarator, comun_numitor)

    def __sub__(self, other):
        comun_numitor = self.numitor * other.numitor
        diferenta_numarator = self.numarator * other.numitor - other.numarator * self.numitor
        return Fractie(diferenta_numarator, comun_numitor)

    def inverse(self):
        if self.numarator == 0:
            raise ValueError("Nu se poate calcula inversa pentru o fractie cu numaratorul 0.")
        return Fractie(self.numitor, self.numarator)


# Exemplu de utilizare
frac1 = Fractie(1, 2)
frac2 = Fractie(1, 3)

print(f"Fractia 1: {frac1}")
print(f"Fractia 2: {frac2}")

suma = frac1 + frac2
print(f"Suma: {suma}")

diferenta = frac1 - frac2
print(f"Diferenta: {diferenta}")

inversa_frac1 = frac1.inverse()
print(f"Inversa fractiei 1: {inversa_frac1}")
