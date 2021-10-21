from model import Model, Razdelek, Knjige

#dat = "stanje.json"
model = Model()
#try:
#    model = Model.preberi_iz_datoteke(dat)
#except FileNotFoundError:
#    model = Model()

ZAMENJAJ_RAZDELEK = 1
VRNI_NA_ZACETNI_ZASLON = 2
DODAJ_KNJIGO = 3
POBRISI_KNJIGO = 4
ZACNI_BRATI_KNJIGO = 5
PREBERI_KNJIGO = 6
PREBERI_STRANI = 7
IZHOD = 8

moznosti_osnovni_zaslon = [(ZAMENJAJ_RAZDELEK, 'zamenjaj razdelek'), 
(IZHOD, 'izhod iz programa')]

moznosti_prvic = [(VRNI_NA_ZACETNI_ZASLON, 'vrni se na začetni zaslon'), 
(DODAJ_KNJIGO, 'dodaj knjigo v razdelek'), 
(POBRISI_KNJIGO, 'izbrisi knjigo iz razdelka'),
(ZACNI_BRATI_KNJIGO, 'začni brati knjigo')]

moznosti_drugic = [(VRNI_NA_ZACETNI_ZASLON, 'vrni se na začetni zaslon'),
(PREBERI_STRANI, 'zabeleži koliko strani si prebral'),
(PREBERI_KNJIGO, 'preberi celo knjigo'),
(POBRISI_KNJIGO, 'izbrisi knjigo iz razdelka')]

moznosti_tretjic = [(VRNI_NA_ZACETNI_ZASLON, 'vrni se na začetni zaslon'),
(POBRISI_KNJIGO, 'izbrisi knjigo iz razdelka')]

def izberi_moznost(moznosti):
    for i in range(len(moznosti)):
        print(f"{i + 1} {moznosti[i][1]}")
    while True:
        vnos_stevila = input('> ')
        try:
            int(vnos_stevila)
            if 1 <= int(vnos_stevila) <= len(moznosti):
                return moznosti[int(vnos_stevila) - 1][0]
        except ValueError:
            print(f'Vnesti morate celo število med 1 in {len(moznosti)}')

ZELIM_PREBRATI = Razdelek('ZELIM PREBRATI')
V_BRANJU = Razdelek('V BRANJU')
PREBRANE = Razdelek('PREBRANA')

razdelki = [(ZELIM_PREBRATI , 'seznam knjig, ki jih želim prebrati'), (V_BRANJU, 'knjige, ki jih trenutno berem'), (PREBRANE, 'seznam že prebranih knjig')]


def tekstovni_vmesnik():
    prikazi_pozdravno_sporocilo()
    while True:
        prvi_ukaz = izberi_moznost(moznosti_osnovni_zaslon)
        if prvi_ukaz == ZAMENJAJ_RAZDELEK:
            zamenjaj_razdelek()
            if model.aktualni_razdelek == ZELIM_PREBRATI:
                prikazi_aktualni_razdelek()
                drugi_ukaz = izberi_moznost(moznosti_prvic)
                if drugi_ukaz == VRNI_NA_ZACETNI_ZASLON:
                    osnovni_zaslon()
                elif drugi_ukaz == DODAJ_KNJIGO:
                    dodaj_knjigo()
                elif drugi_ukaz == POBRISI_KNJIGO:
                    pobrisi_knjigo()
                elif drugi_ukaz == ZACNI_BRATI_KNJIGO:
                    zacni_brati_knjigo()
            elif model.aktualni_razdelek == V_BRANJU:
                prikazi_aktualni_razdelek()
                tretji_ukaz = izberi_moznost(moznosti_drugic)
                if tretji_ukaz == VRNI_NA_ZACETNI_ZASLON:
                    osnovni_zaslon()
                elif tretji_ukaz == PREBERI_STRANI:
                    preberi_strani()
                elif tretji_ukaz == PREBERI_KNJIGO:
                    preberi_knjigo()
                elif tretji_ukaz == POBRISI_KNJIGO:
                    pobrisi_knjigo()
            elif model.aktualni_razdelek == PREBRANE:
                prikazi_aktualni_razdelek()
                cetrti_ukaz = izberi_moznost(moznosti_tretjic)
                if cetrti_ukaz == VRNI_NA_ZACETNI_ZASLON:
                    osnovni_zaslon()
                elif cetrti_ukaz == POBRISI_KNJIGO:
                    pobrisi_knjigo()
        elif prvi_ukaz == IZHOD:
            print('Nasvidenje!')
            break

def prikazi_pozdravno_sporocilo():
    print('Pozdravljeni v programu Moje knjige')

def prikazi_aktualni_razdelek():
    if model.aktualni_razdelek == None:
        print('Ta razdelek je prazen.')
        zamenjaj_razdelek()
    else:
        print(model.aktualni_razdelek.prikaz_knjig_v_razdelku())

def osnovni_zaslon():
    print('Izberite razdelek ali zapustite program')
    print('PRINT TEST')
    return izberi_moznost(moznosti_osnovni_zaslon)

def zamenjaj_razdelek(): # tu moram poskrbeti še za prazne zavihke
    print("Izberite željen razdelek")
    razdelek = izberi_moznost(razdelki)
    model.zamenjaj_razdelek(razdelek)
    print(razdelek.prikaz_knjig_v_razdelku())

def dodaj_knjigo():
    print('Vnesite naslednje podatke o knjigi: naslov, avtor, število strani.')
    naslov = input('Naslov> ')
    avtor = input('Avtor> ')
    strani = input('Število strani> ')
    dodana_knjiga = Knjige(naslov, avtor, strani)
    V_BRANJU.dodaj_knjige(dodana_knjiga)
    return V_BRANJU.prikaz_knjig_v_razdelku()

def zacni_brati_knjigo():
    #Uporabnik izbere knjigo iz razdelka ZELIM_PREBRATI
    if len(V_BRANJU) >= 1:
        knjiga = izberi_moznost(V_BRANJU.knjige())
        return knjiga.zacni_brati()

def preberi_strani():
    print('Izberite knjigo, katero ste brali in vnesite število prebranih strani')
    knjiga = izberi_moznost(V_BRANJU.knjige())
    n = input('> ')
    try:
        if int(n) == n:
            knjiga.preberi_n_strani(n)
    except ValueError:
        print('Neveljaven vnos! Prosim vnesite celo število.')

def preberi_knjigo():
    print('Izberite knjigo, ki ste jo prebrali do konca.')
    knjiga = izberi_moznost(V_BRANJU.knjige())
    knjiga.preberi()

def pobrisi_knjigo():
    pass

tekstovni_vmesnik()


