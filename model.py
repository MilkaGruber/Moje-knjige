from datetime import date

class Model:
    def __init__(self):
        self.aktualni_razdelek = None

    def zamenjaj_razdelek(self, razdelek):
        self.aktualni_razdelek = razdelek


class Razdelek:
    def __init__(self, ime):
        prvi_razdelek = 'Želim prebrati knjige'
        drugi_razdelek = 'Trenutno berem knjige'
        tretji_razdelek = 'Seznam že prebranih knjig'
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
    
    def zacni_brati(self, datum=None):
        self.faza_branja = None #mogoče to funkcijo zbriši
        self.datum = date.today()

    def preberi_n_strani(self, n, datum=None):
        self.st_prebranih_strani += n
        self.datum = date.today()
        if self.st_prebranih_strani == self.st_strani:
            self.preberi()

    def preberi(self, datum=None):
        self.st_prebranih_strani = self.st_strani
        self.faza_branja = True
        self.datum = date.today()


        
    




