from Filmclass import Film
film_list=[]
def beolvas():
    i=0
    fajlom=open("film.txt","r", encoding="utf-8")
    fajlom.readline()
    tartalom=fajlom.readlines()
    fajlom.close()
    while i < len(tartalom):
        sor=tartalom[i].strip().split(";")
        film_list.append(Film(sor))
        i+=1
    #print(film_list[1])
    print(f"A txt fájl sorainak száma(cím nélkül): {len(film_list)}")
def legrovidebb():
    i=0
    shortfilm=0
    while i<len(film_list):
        if film_list[i].perc < film_list[shortfilm].perc:
            shortfilm=i
        i+=1
    print(film_list[shortfilm].cim)
def szaz10percesek():
    i=0
    db=0
    while i <len(film_list):
        if film_list[i].perc> 110:
            db+=1
        i+=1
    print(db)


def ajanlas():
    beker=input("Színész neve: ")
    i=0
    vane=""
    idx=-1
    while i<len(film_list) and idx==-1:
        if film_list[i].foszereplo==beker :
            vane=film_list[i].cim
            idx+=i
        else:
            vane="Sajnos nincs ilyen szereplős film"
        i+=1
    print(vane)
    fajl=open("ajanlott.txt","w",encoding="utf-8")
    fajl.write(f"{vane}")
