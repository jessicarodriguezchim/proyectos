class personaje: 
    #Atributos de la clase 
    # nombre = 'Default'
    # fuerza = 0
    # inteligencia= 0
    # defensa = 0
    # vida = 0
  #constructor de la clase
    def __init__ (self, nombre, fuerza, inteligencia, defensa, vida): 
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    
    def imprimir_atributos(self):
        print(self.nombre)
        print("-Fuerza:" , self.fuerza)
        print("-Inteligencia:" , self.inteligencia)
        print("-Defensa:" , self.defensa)
        print("-Vida:" , self.vida)
        
    def subir_nivel(self, fuerza, inteligencia, defensa):
       #self.fuerza =+ self.fuerza
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
        
    def esta_vivo(self):
        return self.vida > 0 
    
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")
        #return self.vida <= 0
        
    def dañar(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        print("vida de ", enemigo.nombre, "es ", enemigo.vida)
        
class Guerrero(personaje):
    #Sobre escribir constructor de la clase padre
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida) #el super ya contiene el self
        self.espada = espada

    #sobre escribir metodo de impresion
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("-Espada:", self.espada)
        
    def elegir_arma(self):
        opcion = int (input("Elige un arma: \n(1) Lanza de obsidiana, daño 10\n(2) Lanza de chaya, daño 6\n>>>>>"))
        if opcion == 1:
            self.espada = 10
        elif opcion ==2:
            self.espada = 6
        else:
            print("Error, opción no válida")
            #Regresar a dar otra opcion
            self.elegir_arma()
            
    #sobre escribir cálculo de daño
    def daño(self, enemigo):
        return self.fuerza*self.espada - enemigo.defensa

#mago
class Mago(personaje):
    #Sobre escribir constructor de la clase padre
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida) #el super ya contiene el self
        self.libro = libro

    #sobre escribir metodo de impresion
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("-Libro:", self.libro)
        
    def elegir_arma(self):
        opcion = int (input("Elige un arma: \n(1) Hechizos de programación, daño 10\n(2) Recetario de chaya, daño 6\n>>>>>"))
        if opcion == 1:
            self.libro = 10
        elif opcion ==2:
            self.libro = 6
        else:
            print("Error, opción no válida")
            #Regresar a dar otra opcion
            self.elegir_arma()
            
    #sobre escribir cálculo de daño
    def daño(self, enemigo):
        return self.inteligencia*self.libro - enemigo.defensa
            
            
            
            
michael_jackson=personaje("Mickael Jackson", 20, 15, 10, 100)           
tlatuani = Guerrero("Apocalipto", 50, 70, 30, 100, 5)
merlin = Mago("Merlin", 20, 15, 10, 100, 5)


#tlatuani.elegir_arma()
#merlin.elegir_arma()
#tlatuani.imprimir_atributos()

#imprimir atributos antes de la tragedia
michael_jackson.imprimir_atributos()
merlin.imprimir_atributos()
tlatuani.imprimir_atributos()

#Ataques masivos
michael_jackson.atacar(tlatuani)
tlatuani.atacar(merlin)
merlin.atacar(michael_jackson)

#imprimir atributos despues de la tragedia
michael_jackson.imprimir_atributos()
merlin.imprimir_atributos()
tlatuani.imprimir_atributos()



#Variable del constructo vacío de la clase
# mi_personaje = personaje("Dante", 100, 3, 70, 100)
# mi_personaje.imprimir_atributos()
# mi_enemigo = personaje("Vergil", 70, 30, 70, 100)
# mi_personaje.atacar(mi_enemigo)
# mi_enemigo.imprimir_atributos()

# # Antes del ataque
# print("Antes del ataque:")
# mi_personaje.imprimir_atributos()
# mi_enemigo.imprimir_atributos()

# # Ataque
# print("\nDurante el ataque:")
# mi_personaje.atacar(mi_enemigo)

# # Después del ataque
# print("\nDespués del ataque:")
# mi_personaje.imprimir_atributos()
# mi_enemigo.imprimir_atributos()

#print(mi_personaje.dañar(mi_enemigo))
# mi_personaje.subir_nivel(10, 1, 5)
# print("-----------------------------")
# mi_personaje.imprimir_atributos()


#mi_personaje.nombre = 'JessicaFighter'
#mi_personaje.fuerza = 30
#mi_personaje.inteligencia = 12
#mi_personaje.defensa = 28
#mi_personaje.vida = 3



# print("El nombre del personaje es", mi_personaje.nombre)
# print("La fuerza del personaje es", mi_personaje.fuerza)
# print("La inteligencia del personaje es", mi_personaje.inteligencia)
# print("La defensa del personaje es", mi_personaje.defensa)
# print("La vida del personaje es", mi_personaje.vida)




