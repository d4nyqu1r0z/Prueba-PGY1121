

from itertools import cycle


def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11


class RegistroPersona:
    def __init__(self, rut, nombre, edad, pais, ciudad, estado_civil=None):
        self.rut = rut
        self.nombre = nombre
        self.edad = edad
        self.pais = pais
        self.ciudad = ciudad
        self.estado_civil = estado_civil


# Opción 1
def registrar_datos():
      rut = int(input("Ingrese el DNI (sin el dígito verificador): "))
      nombre = input("Ingrese el nombre: ")
      edad = int(input("Ingrese la edad: "))
      pais = input("Ingrese el país de nacimiento: ")
      ciudad = input("Ingrese la ciudad de nacimiento: ")

      if len(nombre) >= 8 and edad >= 0:
          if edad >= 18:
              estado_civil = input("Ingrese su estado civil: ")
          else:
              estado_civil = None

          registro = RegistroPersona(rut, nombre, edad, pais, ciudad, estado_civil)
          info_persona.append(registro)
          print("Registro guardado exitosamente.")
      else:
          print("Los datos ingresados no son válidos.")





# Opción 2
def buscar_persona():
    rut= input("Ingrese el DNI de la persona a buscar (sin el dígito): ")

    persona_encontrada = False

    for registro in info_persona:
        if registro.rut == int(rut):
            persona_encontrada = True
            print("Información de la persona:")
            print(f"DNI:", registro.rut,"-",digito_verificador(rut))
            print("Nombre:", registro.nombre)
            print("Edad:", registro.edad)
            print("País de nacimiento:", registro.pais)
            print("Ciudad de nacimiento:", registro.ciudad)

            if registro.pais.lower() == "argentina":
                print("La persona pertenece a Argentina.")
            else:
                print("La persona NO pertenece a Argentina.")
            break

    if not persona_encontrada:
        print("No se encontró a ninguna persona con ese DNI.")



# Opción 3
def validar_certificado(pais):
    for registro in info_persona:
        if registro.pais.lower() == "argentina":
            pass
            if registro.estado_civil == "casado":
              break
        else:
          print("Credenciales no válidas para imprimir un certificado: La persona no es de Argentina")



def imprimir_certificado():
    rut = input("Ingrese el DNI de la persona (sin el dígito verificador): ")
    persona_encontrada = False

    for registro in info_persona:
        if registro.rut == int(rut):
            persona_encontrada = True
            validar_certificado(registro.pais)
            break

    if persona_encontrada:
        fecha_nacimiento = input("Ingrese la fecha de nacimiento (dd/mm/yyyy): ")
        if len(fecha_nacimiento) == 10 and fecha_nacimiento[2] == "/" and fecha_nacimiento[5] == "/":
            print("----- Certificado de Nacimiento -----")
            print("Nombre:", registro.nombre)
            print(f"DNI:", registro.rut,"-",digito_verificador(rut))
            print("País de Nacimiento:", registro.pais)
            print("Ciudad de Nacimiento:", registro.ciudad)
            print("Fecha de Nacimiento:", fecha_nacimiento)
            print("Estado Civil:", registro.estado_civil)
            if registro.estado_civil == "casado":
                nombre_conyuge = input("Ingrese el nombre del/la cónyuge: ")
                print("Nombre del/la Cónyuge:", nombre_conyuge)
    else:
        print("No se encontró a ninguna persona con ese rut.")



#Opción 4
def eliminar_persona():
    rut = input("Ingrese el DNI de la persona a eliminar (sin el dígito verificador): ")

    registro_eliminado = False

    for i, registro in enumerate(info_persona):
        if registro.rut == int(rut):
            del info_persona[i]
            registro_eliminado = True
            print("Persona eliminada exitosamente.")
            break

    if not registro_eliminado:
        print("No se encontró a ninguna persona con ese DNI.")

def mostrar_menu():
    print("--- Menú ---")
    print("1. Registrar Persona")
    print("2. Buscar Persona")
    print("3. Imprimir Certificado")
    print("4. Eliminar")
    print("5. Salir")


info_persona = []

while True:
    mostrar_menu()
    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        print("1. Registrar Persona")
        registrar_datos()
    elif opcion == 2:
        print("2. Buscar Persona")
        buscar_persona()
    elif opcion == 3:
        print("3. Imprimir Certificado")
        imprimir_certificado()
    elif opcion == 4:
        print("4. Eliminar")
        eliminar_persona()
        continue
    elif opcion == 5:
        print("5. Salir")
        break
