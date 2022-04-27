mochila = [ "linterna","galletitas","sable de luz","celular","agua","tunica"]

def usarLaFuerza(objeto,indice):
    if (indice == len(mochila)):
        return 0
    elif (mochila[indice] == "sable de luz"):
        return 0
    else:
        return 1 + usarLaFuerza(objeto, indice +1)
    

el = usarLaFuerza("sable de luz", 0)

if (el == len(mochila)):
    print("no se enocntro el sable de luz")
else:
    print("se encontro el sable de luz despues de sacar ", el, " objetos")