from datetime import date

class Model:
    def __init__(self):
        self.razdelek = ['Želim prebrati', 'Trenutno berem', 'Seznam že prebranih knjig']

class Razdelki:
    def __init__(self, ime):
        self.ime = ime
        self.knjige = []

    def dodaj_knjige(self, knjiga):
        self.knjige.append(knjiga)

class Knjige:
    def __init__(self, naslov, avtor, st_strani, faza_branja, st_prebranih_strani):
        self.naslov = naslov
        self.avtor = avtor
        self.st_strani = st_strani
        self.faza_branja = False
        self.st_prebranih_strani = 0
    
    def zacni_brati(self):
        self.prebrano = None

    def preberi(self):
        self.prebrano = True

    def preberi_n_strani(self, n):
        self.st_prebranih_strani += n
        
testni_model = ['test1']




