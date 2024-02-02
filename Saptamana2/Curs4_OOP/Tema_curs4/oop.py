class Telefon:
    counter = 0

    def __init__(self, numar):
        self.__numar = numar
        Telefon.counter += 1

    def apelare(self, numar):
        mesaj = f'Apelati {numar}  folosind propriun numar: {self.__numar}'
        return mesaj

    @property
    def numar(self):
        return self.__numar

    @numar.setter
    def numar(self, numar):
        self.__numar = numar

    @numar.deleter
    def numar(self):
        del self.__numar


class TelefonFix(Telefon):
    last_SN = 0

    def __init__(self, numar):
        super().__init__(numar)
        TelefonFix.last_SN += 1
        self.SN = f'TF - {TelefonFix.last_SN}'


class TelefonMobil(Telefon):
    last_SN = 0

    def __init__(self, numar):
        super().__init__(numar)
        TelefonMobil.last_SN += 1
        self.SN = f'TM - {TelefonMobil.last_SN}'


def main():
    print(f'Numar total de device-uri create: {Telefon.counter}')
    print('Crearea a doua device-uri')

    fix = TelefonFix('021 777 00 22')
    mobil = TelefonMobil('0744 332 211')

    print(f'Numar total de deviceuri create: {Telefon.counter}')
    print(f'Numar total al telefoanelor fixe create: {TelefonFix.last_SN}')

    print(fix.apelare('0748 924 664'))
    print(f'Telefoane fixe primite: "{fix.SN}"')
    print(f'Telefoane mobile primite: "{mobil.SN}"')
    print()

    # Using @property decorator
    print(fix.numar)
    fix.numar = '022 000 11 22'
    print(fix.numar)

    del fix.numar

    # print(fix.numar) # Will raise an AttributeError


if __name__ == '__main__':
    main()