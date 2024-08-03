import time
import logging

# Configuración del logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#Aqui estoy creando una nueva clase con el nombre planeta y todos sus itens cada que cree una nueva clase llano repitiria el mismo procedimiento 
#solo pondria los itens
class Planeta:
    def __init__(self, nombre, tipo, radio, distancia_al_Sol):
        self.nombre = nombre
        self.tipo = tipo
        self.radio = radio
        self.distancia_al_Sol = distancia_al_Sol

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Tipo: {self.tipo}, Radio: {self.radio}, Distancia al Sol: {self.distancia_al_Sol}"

#Aqui estoy creando una nueva clase con el nombre planeta terrestre y llamando ala clase planeta
class PlanetaTerrestre(Planeta):
    def __init__(self, nombre, radio, distancia_al_Sol):
        super().__init__(nombre, "Terrestre", radio, distancia_al_Sol)

#Aqui estoy creando una nueva clase con el nombre planetaGaseoso y llamando ala clase planeta 
class PlanetaGaseoso(Planeta):
    def __init__(self, nombre, radio, distancia_al_Sol):
        super().__init__(nombre, "Gaseoso", radio, distancia_al_Sol)

planetas = []
# Aqui estoy haciendo un crud con condiciones si pongo unos de los literales del 1 al 5 sera correcto si pon un 6 me saldra error 
while True:
    print("BIENVENIDOS MENU PRINCIPAL")
    time.sleep(2)
    print("1. CREAR NUEVO PLANETA")
    print("2. LEER Y MOSTRAR PLANETAS")
    print("3. ACTUALIZAR PLANETAS")
    print("4. BORRAR PLANETA")
    print("5. SALIR")

    opcion = input("SELECCIONE OPCION: ")
# match opcion aqui estoy creando las opciones una ves que alguien precione unos de las opciones anteriores aqui se abrira el siguiente paso 
    match opcion:
        case '1':
            nombre = input("INGRESE NOMBRE: ")
            tipo = input("INGRESE TIPO DE PLANETA (Terrestre/Gaseoso): ")
            radio = input("INGRESE RADIO DE PLANETA: ")
            distancia_al_Sol = input("INGRESE DISTANCIA AL SOL: ")
            
            # if es como es verdad que el platena es terrestre y elif es como si el planeta no es trerreste es osea le da la opcion de elegir otra categoria 
            if tipo.lower() == "terrestre":
                planeta = PlanetaTerrestre(nombre, radio, distancia_al_Sol)
            elif tipo.lower() == "gaseoso":
                planeta = PlanetaGaseoso(nombre, radio, distancia_al_Sol)
            
            #else es como la parte contraria si no es ninguna de las obciones no es valido 
            else:
                print("Tipo de planeta no válido.")
                logging.warning("Intento de crear un planeta con tipo no válido: %s", tipo)
                continue
            
            planetas.append(planeta)
            # logging es un controlador de errores con tiempo en la hora real 
            logging.info("Planeta creado: %s", planeta.mostrar_info())
        
        # case es como una capsula donde van los itens de los literale elegidos
        case '2':
            
            if planetas:
               
                for planeta in planetas:
                    print(planeta.mostrar_info())
                logging.info("Se mostraron los planetas registrados.")
            else:
                print("No hay planetas registrados.")
                logging.info("Intento de mostrar planetas, pero no hay registros.")
        
        case '3':
            nombre_actualizar = input("INGRESE NOMBRE DEL PLANETA A ACTUALIZAR: ")
            for planeta in planetas:
                if planeta.nombre == nombre_actualizar:
                    planeta.tipo = input("INGRESE NUEVO TIPO DE PLANETA (Terrestre/Gaseoso): ")
                    planeta.radio = input("INGRESE NUEVO RADIO DE PLANETA: ")
                    planeta.distancia_al_Sol = input("INGRESE NUEVA DISTANCIA AL SOL: ")
                    print("Planeta actualizado.")
                    logging.info("Planeta actualizado: %s", planeta.mostrar_info())
                    break
            else:
                print("Planeta no encontrado.")
                logging.warning("Intento de actualizar un planeta que no existe: %s", nombre_actualizar)
        
        case '4':
            nombre_borrar = input("INGRESE NOMBRE DEL PLANETA A BORRAR: ")
            for planeta in planetas:
                if planeta.nombre == nombre_borrar:
                    planetas.remove(planeta)
                    print("Planeta borrado.")
                    logging.info("Planeta borrado: %s", nombre_borrar)
                    break
            else:
                print("Planeta no encontrado.")
                logging.warning("Intento de borrar un planeta que no existe: %s", nombre_borrar)
        
        case '5':
            print("Saliendo del programa...")
            logging.info("El programa ha sido cerrado.")
            break
        
        case _:
            print("Opción incorrecta.")
            logging.warning("Opción incorrecta seleccionada: %s", opcion)
