class Forma:

    def __lt__(self, other):
        return self.aria() < other.aria()

    def __gt__(self, other):
        return self.aria() > other.aria()

    def __eq__(self, other):
        return self.aria() == other.aria()

    def aria(self):
        return 0

    def __hash__(self):
        return int(self.aria())

    def __del__(self):
        print('deallocation')

class Cerc(Forma):
    PI = 3.14

    def __init__(self, raza):
        self.raza = raza

    def aria(self):
        return self.PI*(self.raza **2)



class Dreptunghi(Forma):
    def __int__(self, lungime, latime):
        self.lungime = lungime
        self.latime = latime

    def aria(self):
        return self.lungime * self.latime

    @staticmethod
    def e_patrat(lungime, latime):
        return lungime == latime


