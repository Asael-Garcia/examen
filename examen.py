#examen primer parcial
#by Monico Torres, 2do "A" ISW

class Empleado:
    def __init__(self,nombre,dias,salario,impuestos):
        self._nombre=nombre
        self._diasTrabajados=dias
        self._salario_diario=salario
        self._tasaImpuestos=impuestos
        self._sueldo_a_pagar=0
        self._impuestos=0

    def CalcularSueldo(self):
        self._sueldo_a_pagar=self._salario_diario*self._diasTrabajados
        return self._sueldo_a_pagar
    def CalcularImpuesto(self):
        self._impuestos=self._sueldo_a_pagar*self._tasaImpuestos/100
        return self._impuestos


class Empleados:
    def __init__(self,array):
        self._array=array
    def MostrarListados(self):
        contador_array=0
        bandera='s'
        for i in range(len(self._array)):
            propiedades=self._array[contador_array].__dict__
            llaves=propiedades.keys()
            contador=0
            for propiedad in llaves:
                etiqueta=propiedad[1:len(propiedad)]
                etiqueta=etiqueta.capitalize()
                print(etiqueta+":\n"+" "+str(propiedades[propiedad]))
                contador=contador+1
            print("----------------------------------------------")
            contador_array=contador_array+1

continuar='s'
contador=0
array_objetos=[]
while continuar=='s':
    nombre=input("Dame el nombre del empleado: ")
    dias=int(input("Dime los dias trabajados por "+ nombre+ ": "))
    salario=float(input("Cuanto es lo que gana por dia: "))
    impuestos=float(input("Cual es su taza de impuestos: "))
    objeto=Empleado(nombre,dias,salario,impuestos)
    objeto.CalcularSueldo()
    objeto.CalcularImpuesto()
    array_objetos.append(objeto)
    continuar=input("¿Deseas añadir a alguien mas? s/n: ")
    print("----------------------------------------------")

empleados=Empleados(array_objetos)
empleados.MostrarListados()
