import hashlib

class Mensajero:
    
    def __init__(self):
        
        self.lista_direcciones = {'Clave Publica': "",
                                  'Clave Privada': "",
                                  'Monedas': ""}
        
        
    def direccion_publica_crear(self, direccion_publica, direccion_privada, monedas):
        self.lista_direcciones['Clave Publica'] = direccion_publica
        self.lista_direcciones['Clave Privada'] = direccion_privada
        self.lista_direcciones['Monedas'] = monedas

    def cargar_monedas(self, cantidad):
        self.monedas = cantidad
        self.lista_direcciones['Monedas'] = cantidad
        

mensajero1 = Mensajero()
mensajero2 = Mensajero()

mensajero1.direccion_publica_crear(input("Escoja Clave Publica: "), hashlib.sha256(str(input("Escoja Clave Privada: ")).encode()).hexdigest(), "")
mensajero1.cargar_monedas(input("Agrega la cantidad de monedas: "))
mensajero2.direccion_publica_crear(input("Escoja Clave Publica: "), hashlib.sha256(str(input("Escoja Clave Privada: ")).encode()).hexdigest(), "")
mensajero2.cargar_monedas(input("Agrega la cantidad de monedas: "))
lista_general = []
datos = mensajero1.lista_direcciones, mensajero2.lista_direcciones
lista_general.append(datos)
envio = input("Desea relizar algun envio de monedas?")

if envio == "Si":
    print("Lista de Personas")
    print(mensajero1.lista_direcciones['Clave Publica'])
    print(mensajero2.lista_direcciones['Clave Publica'])
    selector_destinatario = input("Escribe el Nombre al que quieres enviar: ")
    if selector_destinatario == mensajero1.lista_direcciones['Clave Publica']:
        print("Enviaras a: "+ mensajero1.lista_direcciones['Clave Publica'])
        selector_remitente = hashlib.sha256(str(input("Escribe tu Clave Privada: ")).encode()).hexdigest()
        clave_privada = mensajero2.lista_direcciones['Clave Privada']
        if selector_remitente == clave_privada:
            agregar = input("Agrega la cantidad de monedas: ")
            mensajero2.cargar_monedas(int(mensajero2.lista_direcciones['Monedas'])-int(agregar))
            mensajero1.cargar_monedas(int(mensajero1.lista_direcciones['Monedas'])+int(agregar))
            print("Se ha enviado correctamente")
        else:
            print("La clave es incorrecta")
    elif selector_destinatario == mensajero2.lista_direcciones['Clave Publica']:
        print("Enviaras a: "+ mensajero2.lista_direcciones['Clave Publica'])
        selector_remitente = hashlib.sha256(str(input("Escriba su Clave Privada: ")).encode()).hexdigest()
        clave_privada = mensajero1.lista_direcciones['Clave Privada']
        if selector_remitente == clave_privada:
            agregar = input("Agrega la cantidad de monedas: ")
            mensajero1.cargar_monedas(int(mensajero1.lista_direcciones['Monedas'])-int(agregar))
            mensajero2.cargar_monedas(int(mensajero2.lista_direcciones['Monedas'])+int(agregar))
            print("Se ha enviado correctamente")
        else:
            print("La clave es incorrecta")
    else: 
        print("La seleccion es incorrecta")
print(datos)


