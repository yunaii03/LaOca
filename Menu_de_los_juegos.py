#Imprimimos el menu en pantalla
print("""
    1) La Oca    3) La serpiente
    2) Q&Q       4) Batalla Naval
    """)

#Leemos lo que diga el usuario
elige=input("Selecciona un juego: ")

#ejecutamos
if elige=="1":
    print("¡¡La Oca, que empieze el juego!!")
elif elige=="2":
    print("¡¡Bienvenido al Quien es quien!!")
elif elige=="3":
    print("¡¡La serpiente, que comienze la partida!!")
elif elige=="4":
    print("¡¡¡Batalla Naval, a destruir barcos!!!")
else:
    print("Lo siento, este juego no esta. :(")
