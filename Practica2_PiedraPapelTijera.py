# Armar el "Juego Piedra, papel o tijera"
# Falta agregar que en caso que ingrese una opcion incorrecta, deje ingresar uno correcto para avanzar
# Falta agregar que puedan jugar mas de una vez.

nombre1 = str.upper(input("Ingresa tu nombre:  "))
nombre2 = str.upper(input("Ingresa tu nombre:  "))

jugador1 = str.lower(input("Elige la entre las opciones: Piedra, Papel o Tijeras:  "))
jugador2 = str.lower(input("Elege la entre las opciones: Piedra, Papel o Tijeras:  "))

condicion1 = jugador1 == "piedra" and jugador2 == "tijeras" 
condicion2 = jugador1 == "papel" and jugador2 == "piedra" 
condicion3 = jugador1 == "tijeras" and jugador2 == "papel"
condicion4 = jugador2 == "piedra" and jugador1 == "tijeras" 
condicion5 = jugador2 == "papel" and jugador1 == "piedra" 
condicion6 = jugador2 == "tijeras" and jugador1 == "papel"


if jugador1 == jugador2:
    print (nombre1 +" y " + nombre2 +" empataron.")    
elif condicion1 or condicion2 or condicion3:
    print (nombre1 + " gano el juego")

elif condicion4 or condicion5 or condicion6:
    print (nombre2 + " gano el juego")
   
else:
    print ("Por favor verificar las opciones elegidas")
        



