def posada():
    for x in range(2):
        p=2
        p=p-1
        #tirada maquina
        z=dado()
        movement(z)
        #tirada jugador
        print("El jugador 1 se queda 2 turnos sin tirar",p,"turnos restantes")

