Respuesta = "si"

while Respuesta == "si": #Mientras la respuesta sea "si", se ejecutará el siguiente bloque de código
    
    Primer_numero = float(input("Ingresa el primer número: ")) #Pide el primero número

    Segundo_numero = float(input("Ingresa el segundo número: ")) #Pide el segundo número
    #Pregunta que operación va a realizar con los dos anteriore números
    Operacion = input("¿Qué operación deseas realizar? (suma, resta, multiplicación, división): ").lower()
    
    while Operacion not in ["suma", "resta", "multiplicación", "división", "multiplicacion", "division"]: #Mientras la operación no sea válida, se le pedirá al usuario que ingrese una operación válida
            print("Operación no válida. Por favor, elige suma, resta, multiplicación o división.")
            Operacion = input("¿Qué operación deseas realizar? (suma, resta, multiplicación, división): ").lower()

    if Operacion == "suma":
        Calculo = Primer_numero + Segundo_numero
    elif Operacion == "resta":
        Calculo = Primer_numero - Segundo_numero
    elif Operacion == "multiplicación" or Operacion == "multiplicacion":
        Calculo = Primer_numero * Segundo_numero
    elif Operacion == "división" or Operacion == "division":
        if Segundo_numero == 0:
            print("Error: No se puede dividir entre cero.")
            calculo = None
            
        else:
            Calculo = Primer_numero / Segundo_numero
        
    #Muestra el resultado de la operación segú  la opción elegida
    if calculo is not None:
        print("El resultado de la operación es: ", Calculo)

    Respuesta = input("¿Deseas continuar? (si/no): ").lower()
    
    while Respuesta not in ["si", "no"]: #Mientras la respuesta no sea "si" o "no", se le pedirá al usuario que ingrese una respuesta válida
            print("Respuesta no válida. Por favor, ingresa 'si' o 'no'.")
            Respuesta = input("¿Deseas continuar? (si/no): ").lower()
    

print("Gracias por usar la calculadora. ¡Hasta luego!")

