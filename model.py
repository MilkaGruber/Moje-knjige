from datetime import date
import json

class Model:
    def __init__(self):
        self.aktualni_razdelek = None
        self.razdelki = [ZELIM_PREBRATI, V_BRANJU, PREBRANE, IZHOD]

    def zamenjaj_razdelek(self, razdelek):
        self.aktualni_razdelek = razdelek

    def v_slovar(self): 
        return {
            "razdelki": [razdelek.v_slovar() for razdelek in self.razdelki],
             "aktualni_razdelek": self.razdelki.index(self.aktualni_razdelek)
             if self.aktualni_razdelek
             else None,
            }

    @staticmethod
    def iz_slovarja(slovar): 
        model = Model()
        model.razdelki = [
            Razdelek.iz_slovarja(slovar_razdelka) for slovar_razdelka in slovar["razdelki"]
        ]
        if slovar["aktualni_razdelek"] is not None:
            model.aktualni_razdelek = model.razdelki[slovar["aktualni_razdelek"]]
        return model

    def shrani_v_datoteko(self, ime_datoteke):
        with open(ime_datoteke, 'w') as dat:
            slovar = self.v_slovar()
            json.dump(slovar, dat)
    
    @staticmethod
    def preberi_iz_datoteke(ime_datoteke):
        with open(ime_datoteke) as dat:
            slovar = json.load(dat)
            return Model.iz_slovarja(slovar)



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

    def v_slovar(self):
        return {
            "ime": self.ime,
            "knjige": [knjiga.v_slovar() for knjiga in self.knjige]
        }

    @staticmethod
    def iz_slovarja(slovar):
        razdelek = Razdelek(slovar["ime"])
        razdelek.knjige = [Knjige.iz_slovarja(k) for k in slovar["knjige"]]
        return razdelek

ZELIM_PREBRATI = Razdelek('ZELIM PREBRATI')
V_BRANJU = Razdelek('V BRANJU')
PREBRANE = Razdelek('PREBRANA')
IZHOD = Razdelek('IZHOD')


class Knjige:
    def __init__(self, naslov, avtor, st_strani):
        self.naslov = naslov
        self.avtor = avtor
        self.st_strani = st_strani
        self.st_prebranih_strani = 0
        self.datum = date.today().isoformat()
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
        self.datum = date.today().isoformat()
        self.zgodovina.append((self.st_prebranih_strani, self.datum))

    def preberi(self):
        self.st_prebranih_strani = self.st_strani
        self.datum = date.today().isoformat()
        self.zgodovina.append((self.st_prebranih_strani, self.datum, 'PREBRANO'))

    def delez_prebrane_knjige(self):
        st_prebranih = int(self.st_prebranih_strani)
        st_strani = int(self.st_strani)
        return int((st_prebranih * 100) // st_strani)

    def koliko_casa_berem(self):
        zacetek = self.zgodovina[0][1]
        konec = self.zgodovina[-1][1]
        razlika = date.fromisoformat(konec) - date.fromisoformat(zacetek)
        return razlika.days

    def  v_slovar(self):
        '''Knjigo zapise v slovar'''
        return {
            "naslov": self.naslov,
            "avtor": self.avtor,
            "st_strani": self.st_strani,
            "st_prebranih_strani": self.st_prebranih_strani,
            "datum": self.datum,
            "zgodovina": self.zgodovina
        }

    @staticmethod
    def iz_slovarja(slovar):
        k = Knjige(
            slovar["naslov"], 
            slovar["avtor"], 
            slovar["st_strani"])
        k.st_prebranih_strani = slovar["st_prebranih_strani"]
        k.datum = date.fromisoformat(slovar["datum"])
        k.zgodovina = slovar["zgodovina"]
        return k

k1 = Knjige('Ana Karenina', 'Tolstoj', 1000)
model = Model()
model.zamenjaj_razdelek(ZELIM_PREBRATI)
model.aktualni_razdelek.dodaj_knjige(k1)
sl = Razdelek.v_slovar(model.aktualni_razdelek)