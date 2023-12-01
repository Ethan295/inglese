import random

class Controlli:
    def __init__(self, parole_italiano, parole_inglese):
        self.parole_italiano = parole_italiano
        self.parole_inglese = parole_inglese
        self.random = 0
        self.parole_inserite = ""
        self.punti = 0
        self.parole_uscite = []

    def parola_random(self):
        i = 0
        while i < 1:
            self.random = random.randint(0, len(self.parole_italiano) - 1)

            if self.random in self.parole_uscite:
                pass
            else:
                print(self.parole_italiano[self.random])
                i += 1
                self.parole_uscite.append(self.random)

    def controllo(self):
        if self.parole_inglese[self.random] == self.parole_inserite:
            self.punti += 1
            return "Corretto"
        else:
            return f"Sbagliato, la risposta era: {self.parole_inglese[self.random]}"

    def nota(self):
        return self.punti / 10 * 5 + 1


def leggi_da_file(nome_file):
    with open(nome_file, "r", encoding="utf-8") as file:
        return [line.strip() for line in file]


def main():
    parole_inglese = leggi_da_file("C:\\Users\\eindemini\\OneDrive - edu.ti.ch\\Desktop\\Scuola\\Terzo anno\\Inglese\\prog\\inglese\\pastParticiple\\verbs.txt")
    parole_italiano = leggi_da_file("C:\\Users\\eindemini\\OneDrive - edu.ti.ch\\Desktop\\Scuola\\Terzo anno\\Inglese\\prog\\inglese\\pastParticiple\\verbi.txt")

    parole = Controlli(parole_italiano, parole_inglese)

    print("Scrivi la traduzione in inglese delle seguenti parole: \n")

    for _ in range(10):
        parole.parola_random()

        parole_inserite = input()
        parole.parole_inserite = parole_inserite

        print(parole.controllo())
        print("")

    print(f"Hai preso: {parole.nota()}")


if __name__ == "__main__":
    main()
