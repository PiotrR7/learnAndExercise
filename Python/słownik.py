kontakty = {}

kontakty = {
    "Piotr" : 600123456,
    "Tomek" : 634524236,
    "Jacek" : 254343724,
    "Jan" : 723648253,
    "Oliwer" : 348725872,
    "Dawid" : 534097809,
    "Antek" : 123123541,
    "Mikołaj" : 172263522,
    "Kamil" : 342348283,
    "Andrzej" : 723548623,
    "Kuba" : 734583483
}

kontakty["Nauczyciel"] = 748521005

for imie, numer in kontakty.items():
    print("%s ma numer telefonu: %d " % (imie, numer))