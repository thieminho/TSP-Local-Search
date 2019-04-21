from time import process_time
#funkcja liczaca odleglosc miedzy 2 wierzcholkami
def distance(p1, p2):
    dist = (((p2[1] - p1[1]) ** 2) + ((p2[2] - p1[2]) ** 2)) ** .5
    return dist
#funkcja liczaca dlugosc pomiedzy wierzcholkami listy, ktora jest jej argumentem
def dlugosctrasy(trasa):
    dltrasy = 0
    dl = len(trasa)
    for i in range(dl-1):
        dltrasy += distance(trasa[i], trasa[i+1])
    return dltrasy

def localsearch(wierzcholki):
    #obliczenie dlugosci trasy w kolejnosci wejsciowej
    odleglosc = dlugosctrasy(wierzcholki)
    #przypisanie zmiennym poczatkowych wartosci
    najkrotszaodleglosc = odleglosc
    najkrodl = odleglosc
    najlepszadroga = wierzcholki
    start = process_time()
    #ustawienie improved jako prawda, zeby moc rozpoczac wykonywanie petli
    improved = True
    while(improved):
        #petla jest wykonywana do momentu, gdy odnajdywane jest ulepszone rozwiazanie albo gdy skonczy sie czas
        improved = False
        #2 petle for, ktore "przechodza" po liscie wierzcholkow zeby potem zamieniane byly 2 krawedzie w grafie przez odwrocenie fragmentu listy od i do j
        for i in range(1, len(wierzcholki) - 2):
            for j in range(i + 1, len(wierzcholki)-1):
                #jesli czas przekroczy 59.9s funkcja zwraca najlepsza obecnie droge
                if process_time() - start > 59.9:
                    return najlepszadroga
                if j - i == 1: continue #bo taka zamiana nic nie da
                #utworzenie nowej listy, w ktorej, ktora ma zamieniony fragment wierzcholkow na pozycjach od i do j (jest on odwrocony)
                nowa = wierzcholki[:]
                temp = wierzcholki[i:j+1]
                temp2 = temp[::-1]
                nowa[i:j+1] = temp2
                nowaodleglosc = 0
                #obliczenie dlugosci nowej kolejnosci wierzcholkow (zeby nie liczyc calego dystansu od nowa, odejmuje od poprzedniej dlugosci 2 krawedzie, ktore
                #zostaly usuniete przez odwrocenie i dodanie 2, ktore powstaly
                nowaodleglosc = najkrodl - distance(wierzcholki[i-1], wierzcholki[i]) + distance(nowa[i-1], nowa[i]) - distance(wierzcholki[j], wierzcholki[j+1]) + distance(nowa[j], nowa[j+1])
                #jesli nowa odleglosc jest krotsza od obecnie najkrotszej, to znaleziona droga staje sie najlepszym rozwiazaniem
                if nowaodleglosc < najkrotszaodleglosc:
                    najlepszadroga = nowa
                    najkrotszaodleglosc = nowaodleglosc
                    #print(najlepszadroga, najkrotszaodleglosc)
                    improved = True
        wierzcholki = najlepszadroga
        najkrodl = najkrotszaodleglosc
    return najlepszadroga

#utworzenie listy i wpisanie do niej wierzcholkow
wierzcholki = []
while True:
    try:
        line = input()
        s = line
        s1, s2, s3 = s.split()
        n = s.split()
        v1 = int(s1)
        v2 = float(s2)
        v3 = float(s3)
        t = [v1, v2, v3]
        wierzcholki.append(t)
    except EOFError:
        break
    a = line.find(str(n))
    if a != -1:
        print(line)
    if line == '':
        break


najkrgreedy = localsearch(wierzcholki)
#wyswietlenie indeksow w kolejnosci zwroconej przez funkcje
for i in range(len(najkrgreedy)):
    print(najkrgreedy[i][0])
