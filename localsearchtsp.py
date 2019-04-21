from time import process_time
def distance(p1, p2):
    dist = (((p2[1] - p1[1]) ** 2) + ((p2[2] - p1[2]) ** 2)) ** .5
    return dist

def dlugosctrasy(trasa):
    dltrasy = 0
    dl = len(trasa)
    for i in range(dl-1):
        dltrasy += distance(trasa[i], trasa[i+1])
    return dltrasy

def localsearch(wierzcholki):
    odleglosc = dlugosctrasy(wierzcholki)
    najkrotszaodleglosc = odleglosc
    najkrodl = odleglosc
    najlepszadroga = wierzcholki
    start = process_time()
    improved = True
    while(improved):
        improved = False
        for i in range(1, len(wierzcholki) - 2):
            for j in range(i + 1, len(wierzcholki)-1):
                if process_time() - start > 59.9:
                    return najlepszadroga
                if j - i == 1: continue 
                nowa = wierzcholki[:]
                temp = wierzcholki[i:j+1]
                temp2 = temp[::-1]
                nowa[i:j+1] = temp2
                nowaodleglosc = 0
                nowaodleglosc = najkrodl - distance(wierzcholki[i-1], wierzcholki[i]) + distance(nowa[i-1], nowa[i]) - distance(wierzcholki[j], wierzcholki[j+1]) + distance(nowa[j], nowa[j+1])
                if nowaodleglosc < najkrotszaodleglosc:
                    najlepszadroga = nowa
                    najkrotszaodleglosc = nowaodleglosc
                    improved = True
        wierzcholki = najlepszadroga
        najkrodl = najkrotszaodleglosc
    return najlepszadroga

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
for i in range(len(najkrgreedy)):
    print(najkrgreedy[i][0])
