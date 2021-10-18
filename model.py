from datetime import date

class Model:
    def __init__(self):
        self.razdelek = ['Želim prebrati', 'Berem', 'Že prebrano']
        self.aktualni_razdelek = None

    def zamenjaj_razdelek(self, razdelek):
        self.aktualni_razdelek = razdelek


class Razdelek:
    def __init__(self, ime):
        self.ime = ime
        self.knjige = []

    def dodaj_knjige(self, knjiga):
        self.knjige.append(knjiga)

    def stevilo_knjig_v_razdelku(self):
        return len(self.knjige)


class Knjige:
    def __init__(self, naslov, avtor, st_strani, faza_branja=False):
        self.naslov = naslov
        self.avtor = avtor
        self.st_strani = st_strani
        self.faza_branja = False
        self.st_prebranih_strani = 0
    
    def zacni_brati(self):
        self.faza_branja = None

    def preberi_n_strani(self, n):
        self.st_prebranih_strani += n

    def preberi(self):
        self.st_prebranih_strani = self.st_strani
        self.faza_branja = True

        
    




