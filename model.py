from datetime import datetime

class Model:
    def __init__(self):
        self.aktualni_razdelek = None

    def zamenjaj_razdelek(self, razdelek):
        self.aktualni_razdelek = razdelek


class Razdelek:
    def __init__(self, ime):
        self.ime = ime
        self.knjige = []

    def __str__(self):
        return self.ime + ': ' + str(self.knjige)

    def dodaj_knjige(self, knjiga):
        self.knjige.append(knjiga)

    def stevilo_knjig_v_razdelku(self):
        return len(self.knjige)

    def naslovi_knjig_v_razdelku(self):
        niz = ''
        for knjiga in self.knjige:
            niz += str(knjiga.naslov) + ', '
        return niz[:-2]



class Knjige:
    def __init__(self, naslov, avtor, st_strani, faza_branja='ZELIM PREBRATI'):
        self.naslov = naslov
        self.avtor = avtor
        self.st_strani = st_strani
        self.faza_branja = faza_branja
        self.st_prebranih_strani = 0
        self.datum = datetime.now()
        self.zgodovina = [(0, self.datum)] #seznam bo opisoval, kdaj sem prebrala koliko strani

    def __str__(self):
        return f"{self.faza_branja}: {self.naslov}, {self.avtor}, prebranih {self.st_prebranih_strani} strani od {self.st_strani}"
    
    def zacni_brati(self):
        self.faza_branja = 'V BRANJU' 
        self.datum = datetime.now()
        self.zgodovina.append((0, self.datum))

    def preberi_n_strani(self, n):
        self.st_prebranih_strani += n
        self.datum = datetime.now()
        if  self.faza_branja == 'ZELIM PREBRATI': 
            self.zacni_brati()
            self.zgodovina.append((self.st_prebranih_strani, self.datum))
        elif self.st_prebranih_strani == self.st_strani:
            self.preberi()
        else:
            self.faza_branja = 'V BRANJU'

    def preberi(self):
        if self.faza_branja == 'ZELIM PREBRATI':
            self.zacni_brati
        self.st_prebranih_strani = self.st_strani
        self.faza_branja = 'PREBRANA'
        self.datum = datetime.now()
        self.zgodovina.append((self.st_prebranih_strani, self.datum))

    def delez_prebrane_knjige(self):
        st_prebranih = self.st_prebranih_strani
        st_strani = self.st_strani
        return int((st_prebranih * 100) // st_strani)

    def kako_dolgo_berem(self): # tudi ne dela
        if self.faza_branja != 'ZELIM PREBRATI':
            zacetek = self.zgodovina[1][1]
            konec = self.zgodovina[-1][1]
            print((zacetek, konec))
            return konec - zacetek

