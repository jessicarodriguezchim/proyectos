class personaje: 
    #Atributos de la clase 
    # nombre = 'Default'
    # fuerza = 0
    # inteligencia= 0
    # defensa = 0
    # vida = 0
  #constructor de la clase
    def __init__ (self, nombre, fuerza, inteligencia, defensa, vida): 
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida
    
    def imprimir_atributos(self):
        print(self.__nombre)
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
        print(self.__nombre, "ha muerto")
        #return self.vida <= 0
        
    def dañar(self, enemigo):
        return max(0, self.fuerza - enemigo.defensa)
    
    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        enemigo.vida = max(0,enemigo.vida - daño)
        print(self.__nombre, "ha realizado", daño, "puntos de daño a", enemigo.__nombre)
        print("vida de ", enemigo.__nombre, "es ", enemigo.vida)
        
    def get_fuerza(self):
        return self.__fuerza
    
    def set_fuerza(self, fuerza):
        if fuerza < 0:
         print("Error, valor negativo")
        else:
            self.__fuerza = fuerza
    
    
    
#Variable del constructo vacío de la clase
mi_personaje = personaje("Dante", 1000, 3, 70, 1000)
#mi_personaje.imprimir_atributos()
mi_enemigo = personaje("Vergil", 70, 30, 70, 100)
#mi_personaje.fuerza
# mi_personaje.fuerza = 0
# mi_enemigo.imprimir_atributos()
#mi_personaje.morir()
print(mi_personaje.get_fuerza())
print(mi_personaje.set_fuerza(-5))

#mi_personaje.atacar(mi_enemigo)
#mi_enemigo.imprimir_atributos()

#print(mi_personaje.dañar(mi_enemigo))
# mi_personaje.subir_nivel(10, 1, 5)
# print("-----------------------------")
# mi_personaje.imprimir_atributos()


#mi_personaje.__nombre = 'JessicaFighter'
#mi_personaje.fuerza = 30
#mi_personaje.inteligencia = 12
#mi_personaje.defensa = 28
#mi_personaje.vida = 3



# print("El nombre del personaje es", mi_personaje.__nombre)
# print("La fuerza del personaje es", mi_personaje.fuerza)
# print("La inteligencia del personaje es", mi_personaje.inteligencia)
# print("La defensa del personaje es", mi_personaje.defensa)
# print("La vida del personaje es", mi_personaje.vida)



