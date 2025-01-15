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
        

#Variable del constructo vacío de la clase
mi_personaje = personaje("Dante", 100, 3, 70, 100)
mi_personaje.imprimir_atributos()
mi_enemigo = personaje("Vergil", 70, 30, 70, 100)
mi_personaje.atacar(mi_enemigo)
mi_enemigo.imprimir_atributos()

# Antes del ataque
print("Antes del ataque:")
mi_personaje.imprimir_atributos()
mi_enemigo.imprimir_atributos()

# Ataque
print("\nDurante el ataque:")
mi_personaje.atacar(mi_enemigo)

# Después del ataque
print("\nDespués del ataque:")
mi_personaje.imprimir_atributos()
mi_enemigo.imprimir_atributos()

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



