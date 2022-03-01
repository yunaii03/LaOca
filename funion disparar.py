def disparar
    print("Comandante, dime coordenadas para disparar")
    x=int(input("Dime la fila: "))
    y=int(input("Dime la columna: "))
    t=tablero_J
        if t[x][y]=='O':
            tablero_J [x][y]='X'
