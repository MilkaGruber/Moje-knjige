from datetime import date

class Model:

    def __init__(self):
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

    def naslovi_knjig_v_razdelku(self):
        niz = ''
        for knjiga in self.knjige:
            niz += str(knjiga.naslov) + ', '
        return niz[:-2]


class Knjige:
    def __init__(self, naslov, avtor, st_strani):
        self.naslov = naslov
        self.avtor = avtor
        self.st_strani = st_strani
        self.st_prebranih_strani = 0
        self.datum = date.today()
        self.zgodovina = [(0, self.datum)] 

    def __str__(self):
        return f"{self.naslov}"

    def __repr__(self):
        procent = self.delez_prebrane_knjige()
        datum = self.datum.strftime("%B %d, %Y")
        if int(self.st_prebranih_strani) == 0:
            return f"{self.naslov}, {self.avtor}: Prebranih 0 strani."
        elif int(self.st_prebranih_strani) < int(self.st_strani):
            return f"Na dan {datum} prebranih {self.st_prebranih_strani} strani"+ f" ({procent}" +"%)" + f" knjige: {self.naslov}, {self.avtor}" 
        elif int(self.st_prebranih_strani) == int(self.st_strani):
            return f"Na dan {datum} prebrana knjiga: {self.naslov}, {self.avtor}" 
        
    def preberi_n_strani(self, n):
        self.st_prebranih_strani += n
        self.datum = date.today()
        self.zgodovina.append((self.st_prebranih_strani, self.datum))

    def preberi(self):
        self.st_prebranih_strani = self.st_strani
        self.datum = date.today()
        self.zgodovina.append((self.st_prebranih_strani, self.datum, 'PREBRANO'))

    def delez_prebrane_knjige(self):
        st_prebranih = int(self.st_prebranih_strani)
        st_strani = int(self.st_strani)
        return int((st_prebranih * 100) // st_strani)

    def koliko_casa_berem(self):
        zacetek = self.zgodovina[0][1]
        konec = self.zgodovina[-1][1]
        razlika = konec - zacetek
        return razlika.days

