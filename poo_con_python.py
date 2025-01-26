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
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada, escudo):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida) #el super ya contiene el self
        self.espada = espada
        self.escudo = escudo
        self.vida_escudo = defensa * escudo
        self.defensa += escudo
        self.inventario_pocimas = {
            "vida": 1,  # Cantidad inicial de pócimas de vida
            "fuerza": 1,  # Cantidad inicial de pócimas de fuerza
            "inteligencia": 1  # Cantidad inicial de pócimas de inteligencia
        }

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
    
    def combate(self, danio):
        if danio < self.vida_escudo:
            print("El daño fue absorbido")
            #vida del escudo debe disminuir menos danio
            self.vida_escudo -= danio
            #imprime la nueva vida del escudo
            print("la nueva vida del escudo es: ", self.vida_escudo)
            
        elif danio > self.vida_escudo:
             # Si el daño recibido es mayor que la vida del escudo:
            # te falta ver si vida_escudo es positivo,
            if danio > self.vida_escudo: 
            #    si es positivo, restarlo hasta dejarlo en 0 y reducir los puntos de vida
           #El escudo será destruido,
             print("Escudo destruido")
            #    del guerrero con el danio restante
            # y el daño restante se aplicará a los puntos de vida del guerrero.
            danio_restante = danio - self.vida_escudo
            self.vida_escudo = 0
            self.vida = self.vida - danio_restante 
            print("la nueva vida del guerrero es: ", self.vida)
            
        elif danio == self.vida_escudo:
            print("El escudo desaparecerá, y el guerrero esta desprotegido para futuros ataques.")
            self.vida_escudo = 0
        #enemigo.vida = enemigo.vida - daño
        #print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        #print("vida de ", enemigo.nombre, "es ", enemigo.vida)

#mago
class Mago(personaje):
    #Sobre escribir constructor de la clase padre
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida) #el super ya contiene el self
        self.libro = libro
        self.inventario_pocimas = {
            "vida": 1,  # Cantidad inicial de pócimas de vida
            "fuerza": 1,  # Cantidad inicial de pócimas de fuerza
            "inteligencia": 1  # Cantidad inicial de pócimas de inteligencia
        }

    #sobre escribir metodo de impresion
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("-Valor del libro:", self.libro)
        
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
 
    def usar_pocima(self):
        print("Elige la pócima que deseas usar: \n (1) Pócima de vida (restaura 20 puntos de vida). \n (2) Pócima de fuerza (aumenta fuerza un 50%). \n (3) Pócima de inteligencia (aumenta inteligencia un 50%).")
    
        opcion = int(input(">>>>>>>>> "))
        
        if opcion == 1:
            if self.inventario_pocimas["vida"] > 0:
                self.vida += 20
                self.inventario_pocimas["vida"] -= 1
                print(f"{self.nombre} usó una pócima de vida. Nueva vida: {self.vida}")
            else:
                print("No tienes pócimas de vida disponibles.")
        elif opcion == 2:
            if self.inventario_pocimas["fuerza"] > 0:
                incremento = self.fuerza * 0.5
                self.fuerza += incremento
                self.inventario_pocimas["fuerza"] -= 1
                print(f"{self.nombre} usó una pócima de fuerza. Nueva fuerza: {self.fuerza}")
            else:
                print("No tienes pócimas de fuerza disponibles.")
        elif opcion == 3:
            if self.inventario_pocimas["inteligencia"] > 0:
                incremento = self.inteligencia * 0.5
                self.inteligencia += incremento
                self.inventario_pocimas["inteligencia"] -= 1
                print(f"{self.nombre} usó una pócima de inteligencia. Nueva inteligencia: {self.inteligencia}")
            else:
                print("No tienes pócimas de inteligencia disponibles.")
        else:
            print("Valor inválido, intente nuevamente.")
            # Lo regresamos a elegir
            self.usar_pocima()    
        
    #escoger navaja
    def escoger_libro(self):
        opcion = int(input("escoge el libro de la sabiduría: \n (1) El principito, daño 10. \n (2) Crepúsculo, daño -10. \n >>>>>>>>"))
        if(opcion == 1):
            self.libro = 10
        elif(opcion == 2):
            self.libro = 6
        else:
            print("Valor inválido, intente nuevamente")
            #lo regresamos a elegir
            self.escoger_libro()
    
#guerrero1 = Guerrero("Tlatuani", 10, 10, 10, 50, 2, 2)
#guerrero2 = Mago("Merlin", 8, 4, 4, 40, 3)

#guerrero1.vida_escudo()

# guerrero2.atacar(guerrero1)           
            
#puesto en comentario el 24/01/2025                
michael_jackson=personaje("Mickael Jackson", 20, 15, 10, 100)           
tlatuani = Guerrero("Tlatuani", 50, 70, 30, 100, 5, 10)
merlin = Mago("Merlin", 20, 15, 10, 100, 5)

#danio = fuerza del guerrero menos defensa del enemigo
#caso 1) danio es menor que vida escudo
#    vida_escudo del guerrero = 30 * 10 = 300
#       --> el danio fue absorvido
tlatuani = Guerrero("Tlatuani", 50, 70, 5, 100, 5, 2)
tlatuani.combate(7)
tlatuani.combate(8)


#caso 2) danio es mayor que vida escudo
#        vida_escudo del 300
#        --> el escudo esta destruido
#tlatuani.combate(350)



#caso 3) danio es igual que vida escudo
#        vida_escudo del guerrero = 300
#        --> el escudo desaparecera
#tlatuani.combate(300)



merlin.usar_pocima()
merlin.imprimir_atributos()

tlatuani.imprimir_atributos()


tlatuani.elegir_arma()
merlin.elegir_arma()
tlatuani.imprimir_atributos()

#24/01/25
#imprimir atributos antes de la tragedia
michael_jackson.imprimir_atributos()
merlin.imprimir_atributos()
tlatuani.imprimir_atributos()

#24/01/25
#Ataques masivos
michael_jackson.atacar(tlatuani)
tlatuani.atacar(merlin)
merlin.atacar(michael_jackson)

#24/01/25
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




