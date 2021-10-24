from model import Model, Razdelek, Knjige, ZELIM_PREBRATI, V_BRANJU, PREBRANE, IZHOD

IME_DATOTEKE = "stanje.json"
try:
    model = Model.preberi_iz_datoteke(IME_DATOTEKE)
except FileNotFoundError:
    model = Model()

ZAMENJAJ_RAZDELEK = 1
DODAJ_KNJIGO = 2
POBRISI_KNJIGO = 3
PREBERI_STRANI = 4
PODROBNOSTI_O_KNJIGI = 5
ZGODOVINA = 6

moznosti_prvic = [(DODAJ_KNJIGO, 'dodaj knjigo v razdelek'),
(PREBERI_STRANI, 'zacni brati knjigo'), 
(POBRISI_KNJIGO, 'izbrisi knjigo iz razdelka'),
(ZAMENJAJ_RAZDELEK, 'pojdi na drug razdelek')]

moznosti_drugic = [(PREBERI_STRANI, 'zabeleži število prebranih strani izbrane knjige'),
(POBRISI_KNJIGO, 'izbrisi knjigo iz razdelka'),
(PODROBNOSTI_O_KNJIGI, 'prikaži podrobnosti o knjigi'),
(ZGODOVINA, 'oglej si zgodovino branja'),
(ZAMENJAJ_RAZDELEK, 'pojdi na drug razdelek')]

moznosti_tretjic = [(POBRISI_KNJIGO, 'izbrisi knjigo iz razdelka'),
(PODROBNOSTI_O_KNJIGI, 'prikaži podrobnosti o knjigi'),
(ZGODOVINA, 'oglej si zgodovino branja'),
(ZAMENJAJ_RAZDELEK, 'pojdi na drug razdelek')]

razdelki = [(ZELIM_PREBRATI , 'seznam knjig, ki jih želim prebrati'), 
(V_BRANJU, 'knjige, ki jih trenutno berem'), 
(PREBRANE, 'seznam že prebranih knjig'),
(IZHOD, 'izhod iz programa')]

def prazen_razdelek(razdelek):
    return razdelek.stevilo_knjig_v_razdelku() == 0

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

def izberi_knjigo(sez_knjig):
    for i in range(len(sez_knjig)):
        print(f"{i + 1} {sez_knjig[i]}")
    while True:
        vnos_stevila = input('> ')
        try:
            int(vnos_stevila)
            if 1 <= int(vnos_stevila) <= len(sez_knjig):
                return sez_knjig[int(vnos_stevila) - 1]
        except ValueError:
            print(f'Vnesti morate celo število med 1 in {len(sez_knjig)}')

def vnos_stevila_strani(): #mgoče ne rabim
    while True:
        n = input('Število strani> ')
        try:
            int(n)
        except ValueError:
            print('Vnesti morate celo število!')
    

def tekstovni_vmesnik():
    prikazi_pozdravno_sporocilo()
    zamenjaj_razdelek()
    while True:
        if model.aktualni_razdelek == ZELIM_PREBRATI: 
            predstavitev_aktualnega_razdelka()
            drugi_ukaz = izberi_moznost(moznosti_prvic)
            if drugi_ukaz == DODAJ_KNJIGO:
                dodaj_knjigo()
            elif drugi_ukaz == POBRISI_KNJIGO:
                pobrisi_knjigo_z_razdelka()
            elif drugi_ukaz == PREBERI_STRANI:
                preberi_strani()
            elif drugi_ukaz == ZAMENJAJ_RAZDELEK:
                zamenjaj_razdelek()
        elif model.aktualni_razdelek == V_BRANJU: 
            predstavitev_aktualnega_razdelka()
            tretji_ukaz = izberi_moznost(moznosti_drugic)
            if tretji_ukaz == PREBERI_STRANI:
                preberi_strani()
            elif tretji_ukaz == POBRISI_KNJIGO:
                pobrisi_knjigo_z_razdelka()
            elif tretji_ukaz == ZAMENJAJ_RAZDELEK:
                zamenjaj_razdelek()
            elif tretji_ukaz == ZGODOVINA:
                prikazi_zgodovino_branja()
            elif tretji_ukaz == PODROBNOSTI_O_KNJIGI:
                prikazi_podrobnosti()
        elif model.aktualni_razdelek == PREBRANE:
            predstavitev_aktualnega_razdelka()
            cetrti_ukaz = izberi_moznost(moznosti_tretjic)
            if cetrti_ukaz == ZAMENJAJ_RAZDELEK:
                zamenjaj_razdelek()
            elif cetrti_ukaz == PODROBNOSTI_O_KNJIGI:
                prikazi_podrobnosti()
            elif cetrti_ukaz == ZGODOVINA:
                prikazi_zgodovino_branja()
            elif cetrti_ukaz == POBRISI_KNJIGO:
                pobrisi_knjigo_z_razdelka()
                cetrti_ukaz
        elif model.aktualni_razdelek == IZHOD:
            model.shrani_v_datoteko(IME_DATOTEKE)
            print('Nasvidenje!')
            break

def prikazi_pozdravno_sporocilo(): 
    print('Pozdravljeni v programu Moje knjige')

def predstavitev_aktualnega_razdelka():  
    if model.aktualni_razdelek.stevilo_knjig_v_razdelku() == 0:
        print(f'Ste na razdelku: {model.aktualni_razdelek.ime}')
        print('V tem razdelku ni vnešene nobene knjige.') 
    else:
        print(f'{model.aktualni_razdelek.ime}: ' + model.aktualni_razdelek.naslovi_knjig_v_razdelku())

def zamenjaj_razdelek(): 
    print("Izberite željen razdelek")
    razdelek = izberi_moznost(razdelki)
    model.zamenjaj_razdelek(razdelek)

def dodaj_knjigo(): 
    """Na aktualni razdelek doda knjigo."""
    print('Vnesite naslednje podatke o knjigi: naslov, avtor, število strani.') 
    naslov = input('Naslov> ')
    avtor = input('Avtor> ') 
    strani = input('Število strani> ') 
    if strani.isnumeric():
        model.aktualni_razdelek.dodaj_knjige(Knjige(naslov, avtor, int(strani)))
    else:
        print('Vnesti morate naravno število!')
        dodaj_knjigo()
    
def pobrisi_knjigo_z_razdelka():  
    """Na razdelku izberemo knjigo in jo zbrišemo."""
    if prazen_razdelek(model.aktualni_razdelek):
        print('Ta razdelek je prazen, dodajte knjigo!')
    else:
        knjiga = izberi_knjigo(model.aktualni_razdelek.knjige)
        (model.aktualni_razdelek.knjige).remove(knjiga)

def preberi_strani(): #popravi 
    if prazen_razdelek(model.aktualni_razdelek):
        print('Ta razdelek je prazen, najprej dodajte knjigo!')
    else:
        print('Izberite knjigo, katero ste brali in vnesite število prebranih strani ali preberi celo')
        knjiga = izberi_knjigo(model.aktualni_razdelek.knjige)
        st_moznih = int(knjiga.st_strani) - int(knjiga.st_prebranih_strani)
        n = input('število prebranih strani ali "cela"> ')
        try:
            if n == 'cela':
                knjiga.preberi()
                PREBRANE.dodaj_knjige(knjiga)
                model.aktualni_razdelek.knjige.remove(knjiga)
            elif int(n) and 0 <= int(n) and int(n) <= st_moznih:
                knjiga.preberi_n_strani(int(n))
                if model.aktualni_razdelek == ZELIM_PREBRATI:
                    ZELIM_PREBRATI.knjige.remove(knjiga) 
                    V_BRANJU.dodaj_knjige(knjiga)
        except ValueError:
            print(f'Neveljaven vnos! Prosim vnesite celo število med 0 in {int(knjiga.st_strani) - int(knjiga.st_prebranih_strani)} ali besedo "cela".')

def prikazi_podrobnosti():
    if prazen_razdelek(model.aktualni_razdelek):
        print('Ta razdelek je prazen, dodajte knjigo!')
    else:
        knjiga = izberi_knjigo(model.aktualni_razdelek.knjige)
        print(knjiga.__repr__()) 

def prikazi_zgodovino_branja():
    if prazen_razdelek(model.aktualni_razdelek):
        print('Ta razdelek je prazen, dodajte knjigo!')
    else:
        knjiga = izberi_knjigo(model.aktualni_razdelek.knjige)
        print(knjiga.zgodovina)
        if len(knjiga.zgodovina[-1]) == 3:
            print(f'Knjigo {knjiga} sem prebral v {knjiga.koliko_casa_berem()} dneh.')
        else:
            print(f'Knjigo {knjiga} berem {knjiga.koliko_casa_berem()} dni.')

#tekstovni_vmesnik()
