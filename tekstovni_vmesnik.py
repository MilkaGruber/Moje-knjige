from model import Model, Razdelek, Knjige

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

RAZDELEK1 = model.razdelki[0]  # RAZDELEK Zelim prebrati
RAZDELEK2 = model.razdelki[1]  # RAZDELEK V branju
RAZDELEK3 = model.razdelki[2]  # RAZDELEK Prebrane
RAZDELEK4 = model.razdelki[3]  # RAZDELEK Izhod

moznosti_prvic = [(DODAJ_KNJIGO,
                   'dodaj knjigo v razdelek ZELIM PREBRATI'),
                  (PREBERI_STRANI,
                   'zacni brati knjigo z razdelka ZELIM PREBRATI'),
                  (POBRISI_KNJIGO,
                   'izbrisi knjigo z razdelka ZELIM PREBRATI'),
                  (ZAMENJAJ_RAZDELEK,
                   'odpri drug razdelek')]

moznosti_drugic = [(PREBERI_STRANI,
                    'zabeleži število prebranih strani izbrane knjige'),
                   (POBRISI_KNJIGO,
                    'izbrisi knjigo z razdelka V BRANJU'),
                   (PODROBNOSTI_O_KNJIGI,
                    'prikaži podrobnosti o knjigi'),
                   (ZGODOVINA,
                    'oglej si zgodovino branja izbrane knjige'),
                   (ZAMENJAJ_RAZDELEK,
                    'odpri drug razdelek')]

moznosti_tretjic = [(POBRISI_KNJIGO,
                     'izbrisi knjigo z razdelka PREBRANO'),
                    (PODROBNOSTI_O_KNJIGI,
                     'prikaži podrobnosti o izbrani knjigi'),
                    (ZGODOVINA,
                     'oglej si zgodovino branja izbrane knjige'),
                    (ZAMENJAJ_RAZDELEK,
                     'odpri drug razdelek')]


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


def izberi_razdelek(sez):
    for i in range(len(sez)):
        print(f"{i + 1} {sez[i].prestavitev_razdelka()}")
    while True:
        vnos_stevila = input('> ')
        try:
            int(vnos_stevila)
            if 1 <= int(vnos_stevila) <= len(sez):
                return sez[int(vnos_stevila) - 1]
        except ValueError:
            print(f'Vnesti morate celo število med 1 in {len(sez)}')


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


def tekstovni_vmesnik():
    prikazi_pozdravno_sporocilo()
    zamenjaj_razdelek()
    while True:
        if model.aktualni_razdelek == RAZDELEK1:
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
        elif model.aktualni_razdelek == RAZDELEK2:
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
        elif model.aktualni_razdelek == RAZDELEK3:
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
        elif model.aktualni_razdelek == RAZDELEK4:
            model.shrani_v_datoteko(IME_DATOTEKE)
            print('Nasvidenje!')
            break


def prikazi_pozdravno_sporocilo():
    print('Pozdravljeni v programu Moje knjige')


def predstavitev_aktualnega_razdelka():
    model.izpis_aktualnega_razdelka()


def zamenjaj_razdelek():
    print("Izberite željen razdelek")
    razdelek = izberi_razdelek(model.razdelki)
    model.zamenjaj_razdelek(razdelek)


def dodaj_knjigo():
    """Na aktualni razdelek doda knjigo."""
    print('Vnesite naslednje podatke o knjigi: naslov, avtor, število strani.')
    naslov = input('Naslov> ')
    avtor = input('Avtor> ')
    strani = input('Število strani> ')
    if strani.isnumeric():
        model.aktualni_razdelek.dodaj_knjige(
            Knjige(naslov, avtor, int(strani)))
    else:
        print('Vnesti morate pozitivno, celo število!')
        dodaj_knjigo()


def pobrisi_knjigo_z_razdelka():
    """Na razdelku izberemo knjigo in jo zbrišemo."""
    if prazen_razdelek(model.aktualni_razdelek):
        print('Ta razdelek je prazen, dodajte knjigo!')
    else:
        knjiga = izberi_knjigo(model.aktualni_razdelek.knjige)
        model.aktualni_razdelek.knjige.remove(knjiga)


def preberi_strani():
    '''Nepraznemu razdelku izberemo knjigo in ji dodamo št. prebranih strani.
    skladno s vnosom se knjiga prestavi na ustrezen razdelek.'''
    if prazen_razdelek(model.aktualni_razdelek):
        print('Ta razdelek je prazen, najprej dodajte knjigo!')
    else:
        print('Izberite knjigo in zabeležite,' +
              ' če ste knjigo že prebrali ali število prebranih strani.')
        knjiga = izberi_knjigo(model.aktualni_razdelek.knjige)
        st_moznih = int(knjiga.st_strani) - int(knjiga.st_prebranih_strani)
        while True:
            try:
                n = int(input('št. prebranih strani ali "cela"> '))
                1 / (0 <= int(n) <= st_moznih)
                break
            except ValueError:
                print(f'Neveljaven vnos! Vnesti morate število med ' +
                      '0 in {st_moznih} ali besedo "cela".')
            except ZeroDivisionError:
                print(f'Neveljaven vnos! Vnesti morate število med ' +
                      '0 in {st_moznih} ali besedo "cela".')
        if 0 <= int(n) < st_moznih:
            knjiga.preberi_n_strani(int(n))
            if model.aktualni_razdelek == RAZDELEK1:
                RAZDELEK1.knjige.remove(knjiga)
                RAZDELEK2.dodaj_knjige(knjiga)
        else:
            knjiga.preberi()
            RAZDELEK3.dodaj_knjige(knjiga)
            model.aktualni_razdelek.knjige.remove(knjiga)


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
        print(knjiga.izpis_zgodovine())


tekstovni_vmesnik()
