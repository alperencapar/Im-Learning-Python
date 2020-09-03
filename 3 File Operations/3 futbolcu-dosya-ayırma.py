with open("futbolcular.txt","r",encoding="UTF-8") as file:
    gs = []
    fb = []
    bjk = []


    for satir in file:
        satir = satir[:-1]
        satir_elemanlari = satir.split(",")

        if(satir_elemanlari[1] == "Fenerbahçe"):
            fb.append(satir + "\n")
        elif(satir_elemanlari[1] == "Galatasaray"):
            gs.append(satir + "\n")

        else:
            bjk.append(satir + "\n")
    with open("fb.txt","w",encoding="UTF-8") as file2:
        for i in fb:
            file2.write(i)


    with open("gs.txt","w",encoding="UTF-8") as file3:
        for i in gs:
            file3.write(i)

    with open("bjk.txt","w",encoding="UTF-8") as file4:
        for i in bjk:
            file4.write(i)

