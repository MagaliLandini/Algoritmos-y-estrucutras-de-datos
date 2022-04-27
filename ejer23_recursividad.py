laberinto = [[1,0,0], 
            [1,0,0],    
            [1,1,2]]

def salidaLaberinto(matriz,x,y, caminos=[]):
    
    if(x >= 0 and x <= len(matriz)-1) and (y >= 0 and y <= len(matriz[0])-1):
        if (matriz[x][y]== 2 ):
            caminos.append([x,y])
            print("Has salido del laberinto")
            print(caminos)
            caminos.pop()
        elif (matriz[x][y]==1):
            matriz[x][y]=3
            caminos.append([x,y])
            salidaLaberinto(matriz,x,y+1,caminos)
            salidaLaberinto(matriz,x,y-1,caminos)
            salidaLaberinto(matriz,x-1,y,caminos)
            salidaLaberinto(matriz,x+1,y,caminos)
            caminos.pop()
            matriz[x][y]=1

salidaLaberinto(laberinto,0,0)

