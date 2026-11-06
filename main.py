from paciente import Paciente
from medico import Medico
from cita import Cita
from atencion import crear_atencion, resumen_atencion

lista_pacientes = []
lista_medicos = []
lista_citas = []
lista_atenciones = []

def buscar_por_codigo(codigo):
    colecciones = [lista_pacientes, lista_medicos, lista_citas, lista_atenciones]
    for coleccion in colecciones:
        resultado = list(filter(
            lambda obj: obj["codigo"] == codigo if isinstance(obj, dict) else obj.codigo == codigo, 
            coleccion
        ))
        if resultado:
            return resultado[0]
    return None

def registrar_paciente():
    print("\n---REGISTRAR PACIENTE---")
    codigo = input("Ingrese el código del paciente: ")
    if buscar_por_codigo(codigo):
        print(f"Error: El código '{codigo}' ya está registrado.")
        return

    nombre = input("Ingrese el nombre del paciente: ")
    edad_str = input("Ingrese la edad del paciente: ")

    if edad_str.isdigit() == False:
        print("Error: La edad ingresada debe ser un número.")
        return

    edad = int(edad_str)

    if edad <= 0 or edad >= 120:
        print("Error: La edad debe estar en el rango de 0 a 120.")
        return

    paciente = Paciente(codigo, nombre, edad)
    lista_pacientes.append(paciente)
    print("Paciente registrado")
    print(f"Paciente: {paciente.resumen()}")

def registrar_medico():
    print("\n---REGISTRAR MÉDICO---")
    codigo = input("Ingrese el código del médico: ")
    if buscar_por_codigo(codigo):
        print(f"Error: El código '{codigo}' ya está registrado.")
        return

    nombre = input("Ingrese el nombre del médico: ")
    especialidad = input("Ingrese la especialidad: ")

    medico = Medico(codigo, nombre, especialidad)
    lista_medicos.append(medico)
    print("Médico registrado")
    print(f"Médico {medico.resumen()}")

def programar_cita():
    print("\n---PROGRAMAR CITA---")
    codigo_cita = input("Ingrese el código de la cita: ")
    if buscar_por_codigo(codigo_cita):
        print(f"Error: El código de cita '{codigo_cita}' ya existe.")
        return

    codigo_p = input("Ingrese el código del paciente existente: ")
    paciente = buscar_por_codigo(codigo_p)
    if isinstance(paciente, Paciente) == False:
        print("Error: Referencia inválida. El paciente no existe.")
        return

    codigo_m = input("Ingrese el código del médico existente: ")
    medico = buscar_por_codigo(codigo_m)
    if isinstance(medico, Medico) == False:
        print("Error: Referencia inválida. El médico no existe.")
        return

    fecha = input("Ingrese la fecha (DD/MM/AAAA): ")

    cita = Cita(codigo_cita, paciente, medico, fecha)
    lista_citas.append(cita)
    print("Cita programada")
    print(f"Cita: {cita.resumen()}")

def buscar_y_mostrar():
    print("\n---BUSCAR POR CÓDIGO---")
    codigo = input("Ingrese el código a buscar (Paciente, Médico, Cita o Atención): ")
    encontrado = buscar_por_codigo(codigo)
    if encontrado:
        if isinstance(encontrado, dict) == True:
            print(f"Objeto encontrado -> {resumen_atencion(encontrado)}")
        else:
            print(f"Objeto encontrado -> {encontrado.resumen()}")
    else:
        print("No se encontró ningún registro con ese código.")

def registrar_atencion():
    print("\n---REGISTRAR ATENCIÓN---")
    codigo_atencion = input("Ingrese el código para esta atención: ")
    if buscar_por_codigo(codigo_atencion):
        print(f"Error: El código de atención '{codigo_atencion}' ya existe.")
        return

    codigo_cita = input("Ingrese el código de la cita atendida: ")
    cita = buscar_por_codigo(codigo_cita)
    if isinstance(cita, Cita) == False:
        print("Error: Referencia inválida. La cita no existe.")
        return

    atencion = crear_atencion(codigo_atencion, cita)
    lista_atenciones.append(atencion)
    print("Atención registrada")
    print(f"Atención: {resumen_atencion(atencion)}")

def menu():
    while True:
        print("\n====================================")
        print("---SISTEMA MÉDICO---")
        print("====================================")
        print("1. Registrar Paciente")
        print("2. Registrar Médico")
        print("3. Buscar por Código")
        print("4. Programar Cita")
        print("5. Registrar Atención")
        print("6. Salir")
        
        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            registrar_paciente()
        elif opcion == "2":
            registrar_medico()
        elif opcion == "3":
            buscar_y_mostrar()
        elif opcion == "4":
            programar_cita()
        elif opcion == "5":
            registrar_atencion()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()