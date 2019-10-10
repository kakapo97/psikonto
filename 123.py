#zadanie1
x = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
print(x)
#zadanie2
imie = "igor"
nazwisko = "grzywacz"
litera_1 = x.count(imie[2])
litera_2 = x.count(nazwisko[3])
print("w tekscie jest",litera_1,"liter 'g' i",litera_2,"liter 'z'")
#zadanie3
print('{} {}'.format(1, 2))
print('{1} {0}'.format('one', 'two'))
print('{:>10}'.format('test'))
print('{:_<10}'.format('test'))
print('{:^6}'.format('zip'))
#zadanie4