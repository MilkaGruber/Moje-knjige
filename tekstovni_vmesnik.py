from model import Model, Razdelek, Knjige

dat = "stanje.json"

try:
    model = Model.preberi_iz_datoteke(dat)
except FileNotFoundError:
    model = Model()

ZAMENJAJ_RAZDELEK = 1
DODAJ_KNJIGO = 2
ZACNI_BRATI_KNJIGO = 3
PREBERI_KNJIGO = 4
PREBERI_STRANI = 5
IZHOD = 6

moznosti = [(ZAMENJAJ_RAZDELEK, 'zamenjaj razdelek'), 
(DODAJ_KNJIGO, 'dodaj knjigo v razdelek'), 
(ZACNI_BRATI_KNJIGO,'dodaj knjigo v razdelek "V BRANJU"'), 
(PREBERI_KNJIGO, 'preberi celo knjigo'),
(PREBERI_STRANI, 'zabeleži koliko strani si prebral' ),
(IZHOD, 'izhod iz programa')]


def izberi_moznost(moznosti):
    for i in range(len(moznosti)):
        print(f"{i + 1} {moznosti[i][1]}")
    while True:
        vnos_stevila = input('> ')
        try:
            int(vnos_stevila)
            if 1 <= int(vnos_stevila) <= len(moznosti):
                return moznosti[int(vnos_stevila) - 1]
        except ValueError:
            print(f'Vnesti morate celo število med 1 in {len(moznosti)}')

def prikaz_knjig_v_razdelku(razdelek):
    return f'{razdelek.ime}: ' + str(razdelek.naslovi_knjig_v_razdelk())

def prikaz_knjige(knjiga):
    return f"{knjiga.faza_branja}: {knjiga.naslov}, {knjiga.avtor}, prebranih {knjiga.st_prebranih_strani} strani od {knjiga.st_strani}"

seznam_zelja = Razdelek('ZELIM PREBRATI')
v_branju = Razdelek('V BRANJU')
prebrane = Razdelek('PREBRANA')

razdelki = [(seznam_zelja, 'seznam knjig, ki jih želim prebrati'), 
(v_branju, 'knjige, ki jih trenutno berem'), 
(prebrane, 'seznam že prebranih knjig')]

def izberi_razdelek(razdelki):
    return izberi_moznost(razdelki)

def tekstovni_vmesnik():
    prikazi_pozdravno_sporocilo()
    while True:
        osnovni_zaslon()
        ukaz = izberi_moznost()
        if ukaz == ZAMENJAJ_RAZDELEK:
            zamenjaj_razdelek()
        elif ukaz == DODAJ_KNJIGO:
            dodaj_knjigo()
        elif ukaz == ZACNI_BRATI_KNJIGO:
            zacni_brati_knjigo()
        elif ukaz == PREBERI_STRANI:
            preberi_strani()
        elif ukaz == PREBERI_KNJIGO:
            preberi_knjigo()
        elif ukaz == IZHOD:
            print('Nasvidenje!')
            break


def prikazi_pozdravno_sporocilo():
    print('Pozdravljeni v programu Moje knjige')

def osnovni_zaslon():
    if model.aktualni_razdelek == None:
        print('izberite enega izmed razdelkov')
        zamenjaj_razdelek()
    print(prikaz_knjig_v_razdelku(model.aktualni_razdelek))

def zamenjaj_razdelek():
    print("Izberite željen razdelek")
    razdelek = izberi_razdelek(razdelki)
    model.zamenjaj_razdelek(razdelek)

def dodaj_knjigo():
    print('Vnesite naslednje podatke o knjigi: naslov, avtor, število strani')
    naslov = input('Naslov> ')
    avtor = input('Avtor> ')
    strani = input('Število strani> ')
    dodana_knjiga = Knjige(naslov, avtor, strani)
    seznam_zelja.dodaj_knjige(dodana_knjiga)
    print(prikaz_knjige(dodana_knjiga))

def zacni_brati_knjigo():
    print('Vnesite 0, če ste začeli brati knjigo, ki še ni na vašem seznamu želja \n ali pritisnite 1, če ste začeli brati knjigo s seznama')
    vrednost = input('> ')
    if vrednost == 0:
        dodaj_knjigo()
    elif vrednost == 1:
        print('Izberite katero knjigo ste brali')
        print(prikaz_knjig_v_razdelku(v_branju))

def preberi_strani():
    print('Koliko strani ste prebrali?')
    n = input('> ')
    try:
        if int(n) == n:
            model.preberi_n_strani(n)
    except ValueError:
        print('Neveljaven vnos! Prosim vnesite celo število.')

def preberi_knjigo():
    model.preberi()



