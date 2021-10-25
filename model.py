from datetime import date
import json

class Model:
    def __init__(self):
        self.aktualni_razdelek = None
        self.razdelki = [ZELIM_PREBRATI, V_BRANJU, PREBRANE, IZHOD]

    def zamenjaj_razdelek(self, razdelek):
        self.aktualni_razdelek = razdelek

    def v_slovar(self): 
        return {"razdelki": [razdelek.v_slovar() for razdelek in self.razdelki]}

    def izpis_aktualnega_razdelka(self):
        if self.aktualni_razdelek.stevilo_knjig_v_razdelku() == 0:
            print(f'Ste na razdelku: {self.aktualni_razdelek.ime}')
            print('V tem razdelku ni vnešene nobene knjige.')
        else:
            print(f'{self.aktualni_razdelek.ime}: ' 
            + self.aktualni_razdelek.naslovi_knjig_v_razdelku())
    
    @staticmethod
    def iz_slovarja(slovar): 
        model = Model()
        model.razdelki = [Razdelek.iz_slovarja(slovar_razdelka) 
        for slovar_razdelka in slovar["razdelki"]]
        model.aktualni_razdelek = ZELIM_PREBRATI
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

    def izbrisi_knjigo(self, knjiga):
        self.knjige.remove(knjiga)

    def stevilo_knjig_v_razdelku(self):
        return len(self.knjige)

    def naslovi_knjig_v_razdelku(self):
        niz = ''
        for knjiga in self.knjige:
            niz += str(knjiga.naslov) + ', '
        return niz[:-2]

    def __str__(self):
        print(f"{self.ime}: {self.naslovi_knjig_v_razdelku()}")

    def prestavitev_razdelka(self):
        return f'{self.ime}'

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
PREBRANE = Razdelek('PREBRANE')
IZHOD = Razdelek('IZHOD')


class Knjige:
    def __init__(self, naslov, avtor, st_strani):
        self.naslov = naslov
        self.avtor = avtor
        self.st_strani = st_strani
        self.st_prebranih_strani = 0
        self.datum = str(date.today)
        self.zgodovina = [(0, self.datum)] 

    def __str__(self):
        return f"{self.naslov}"

    def __repr__(self):
        procent = self.delez_prebrane_knjige()
        datum = self.datum
        if int(self.st_prebranih_strani) == 0:
            return f"{self.naslov}, {self.avtor}: Prebranih 0 strani."
        elif int(self.st_prebranih_strani) < int(self.st_strani):
            return (f"Na dan {datum} prebranih {self.st_prebranih_strani} strani" + 
            f" ({procent}" +"%)" + f" knjige: {self.naslov}, {self.avtor}") 
        elif int(self.st_prebranih_strani) == int(self.st_strani):
            return f"Na dan {datum} prebrana knjiga: {self.naslov}, {self.avtor}" 
        
    def preberi_n_strani(self, n):
        self.st_prebranih_strani += n
        self.datum = str(date.today())
        self.zgodovina.append((self.st_prebranih_strani, self.datum))

    def preberi(self):
        self.st_prebranih_strani = self.st_strani
        self.datum = str(date.today())
        self.zgodovina.append((self.st_prebranih_strani, self.datum, 'PREBRANO'))

    def delez_prebrane_knjige(self): 
        st_prebranih = int(self.st_prebranih_strani)
        st_strani = int(self.st_strani)
        return int((st_prebranih * 100) // st_strani)

    def izpis_zgodovine(self):
        if len(self.zgodovina) > 1:
            niz = f'Na dan {self.datum} dodana knjiga {self.naslov}:'
            if len(self.zgodovina[-1]) == 3:
                for t in self.zgodovina[1:-1]:
                    niz += f'\n Na dan {t[1]} prebranih {t[0]} strani'
                return niz + f'\n Na dan {self.zgodovina[-1][1]} prebrana cela knjiga.'
            else:
                for t in self.zgodovina[1:]:
                    niz += f'\n Na datum {t[1]} prebranih {t[0]} strani'
                return niz
        else:
            return f'Na dan {self.datum} dodana knjiga {self.naslov}.'

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
        k.datum = slovar["datum"]
        k.zgodovina = slovar["zgodovina"]
        return k

