"""clase que genera objetos hortalizas a sembrar con sus caracteristicas fenologicas 
    fechas de siembra, cosecha, labores culturales según la epoca del año y según el tamaño del terreno a sembrar,
     establecido por el usuario determine un rendimiento promedio"""


def principal():
        """metodo inicio programa
        Args: eleccion(int): Menú 
        """
        
        temporada=int(input("Por favor seleccione la temporada de la hortaliza a trabajar : \n"
        "1. PRIMAVERA- VERANO\n"
        "2. OTOÑO- INVIERNO\n"))
        return temporada




class horticultura():

    def __init__(self, temporada) -> None:
        
        self.nombreEspecie=""
        self.familia=""
        self.temporada=temporada
        self.fechaSiembra=0
        self.fechaCosecha=0
        self.rendimiento=0
        self.variedad=0
        self.__listaPV= {1:"Albahaca", 2:"Apio", 3:"Brocoli", 4:"Cebolla", 5:"Espinaca", 6:"Oregano", 7:"Pepino",8:"Sandía"}
        self.__listaOI={1:"Acelga",2:"Arveja",3:"Cebolla",4:"Coliflor",5:"Puerro",6:"Radicheta",7:"Ajo",8:"Haba"}


    def setVariedad(self,cambioVar):
        self.variedad=cambioVar

    def getPrimaveraVerano(self):
        return self.__listaPV

    def getOtonoInvierno(self):
        return self.__listaOI
    def getTemporada(self):
        return self.temporada
       
    
    def variedadHortaliza(self,param):
        """función que trae listado de variedades
            Args: eleccion(int): variedades
            """
        if param==1:
            valor=int(input(f"Seleccione la variedad a trabajar: {self.getPrimaveraVerano()}\n"))
            self.variedad=self.__listaPV.get(valor)
            print("------------------")

        elif param==2:
            valor=int(input(f"Seleccione la variedad a trabajar: {self.getOtonoInvierno()}\n"))
            self.variedad=self.__listaOI.get(valor)
            print("------------------")

    
    def menuLabores(self):
        """función que muestra menú labores
        Args: eleccion(int): Menú 2
        """
        while True:
            print("------------------")
            labor=int(input("Seleccione la labor a realizar:\n"
            "1. Siembra\n"
            "2. Abono\n"
            "3. Raleo\n"
            "4. Riego\n"
            "5. Cosecha\n"
            "6. Volver al menú anterior\n"))
            print("---------------------")
            
            if labor==1:
                print("Detalle de siembra")
                print("------------------")
            if labor==2:
                print("Detalle de abono")
                print("------------------")
            if labor==3:
                print("Detalle de raleo")
                print("------------------")
            if labor ==4:
                print("Detalle riego")
                print("------------------")
            if labor ==5:
                print("Detalle cosecha")
                print("------------------")
            if labor==6:   
                self.menuDecision()                 
                #self.menu2()
                break
        
                
            
    
    
    def menuDecision(self):
        """función que muestra accion a realizar
        Args: eleccion(int): Menú 
        """
        print("ACTIVIDADES A REALIZAR PARA EL CULTIVO DE:",  self.variedad , "\n 1. Labores a realizar \n 2. Obtención de Rendimiento \n" 
        " 3. Características del cultivo \n 4. Listado de las hortalizas cargadas en el sistema\n 5. Cambiar de cultivo\n 6. SALIR")
        
    def menu2(self):
        """función que solicita al usuario
        la eleccion de una actividad
        Args: opcionMenu2(int): menu"""

        while True:
            self.menuDecision()

            opcionMenu2=int(input("Seleccione la opción deseada: "))

            if opcionMenu2==1:
                self.menuLabores()
            elif opcionMenu2==2:
                if self.temporada==1:

                    print("     Aqui se calcula el rendimiento promedio del cultivo de: ", self.variedad)
                    print("------------------")
                    
                elif self.temporada==2:
                    print("     Aquí se calcula el rendimiento promedio del cultivo de: ", self.variedad )
                    print("------------------")
                else:
                    print("lanzar excepción")


            elif opcionMenu2==3:
                print("     Características del cultivo de: ", self.variedad)
                print("------------------")
            elif opcionMenu2==4:
                print("     Variedades Otoño-Invierno", self.getOtonoInvierno())
                print("     Variedades Primavera-Verano", self.getPrimaveraVerano())
                print("------------------")
            elif opcionMenu2==5:
               self.variedadHortaliza(principal())

            elif opcionMenu2==6:
                
                print("     Gracias por utilizar la aplicación!")
                break
                
            
        


print("BIENVENIDO A LA HUERTA EN TUS MANOS")
huerta1=horticultura(principal())

huerta1.variedadHortaliza(huerta1.getTemporada())

huerta1.menu2()











