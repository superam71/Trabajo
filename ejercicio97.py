import json
import decimal
import sys
from collections import OrderedDict
import operator

#nombre=input("ingrese su nombre\n")
#apellido=input("ingrese su apellido\n")
#edad=int(input("ingrese su edad\n"))
#sexo=input("ingrese su sexo. M/F\n")
#ubicaciondisp1=float(input("ingrese la coordenada del primer disparo(x.y)\n"))
#ubicaciondisp2=float(input("ingrese la coordenada del segundo disparo(x.y)\n"))
#ubicaciondisp3=float(input("ingrese la coordenada del tercer disparo(x.y)\n"))

class mostrarpar:
    def __init__(self,nombre,apellido,edad,sexo):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.sexo=sexo

    def __str__(self):
        cadena="Nombre:"+" "+self.nombre+" "+"apellido:"+" "+self.apellido+" "+"edad:"+" "+self.edad+" "+"sexo:"+" "+self.sexo
        return(cadena)

class disparo:
    def __init__(self, nombre,apellido,edad,sexo,ubicaciondisp1,ubicaciondisp2,ubicaciondisp3):
        # Constructor de clase disparo
        # Invoca al constructor de clase mostrar par

        mostrarpar.__init__(self,nombre,apellido,edad,sexo)

        # Nuevos atributos
        self.ubicaciondisp1= ubicaciondisp1
        self.ubicaciondisp2= ubicaciondisp2
        self.ubicaciondisp3= ubicaciondisp3

class concurso:
    def __init__(self,nombre,apellido,edad,sexo,ubicaciondisp1,ubicaciondisp2,ubicaciondisp3):
        # Constructur de clase concurso
        # Invoca al constructor de clase mostrar par

        disparo.__init__(self,nombre,apellido,edad,sexo,ubicaciondisp1,ubicaciondisp2,ubicaciondisp3)
    
    def __str__(self):
        with open("participantes.json","r+") as archivo:
            data=json.load(archivo)
            cantidadpart=str(len(data))
            return("La cantidad de participantes es " + cantidadpart)

class guardardatos:
    def __init__(self,nombre,apellido,edad,sexo,ubicaciondisp1,ubicaciondisp2,ubicaciondisp3):
        with open("participantes.json","r+") as archivo:
            data=json.load(archivo)
            listadisparos=[]
            listadisparos.append(ubicaciondisp1)
            listadisparos.append(ubicaciondisp2)
            listadisparos.append(ubicaciondisp3)
            disparomascercano=min(listadisparos)
            promediodedisparos=sum(listadisparos)/len(listadisparos)
            promediodispredond=round(promediodedisparos,1)
            numeroid=len(data)+1
            numeroidstr=str(numeroid)
            disparomascercano=min(listadisparos)
            data["participante"+numeroidstr]={"id":numeroid,"nombre":nombre,"apellido":apellido,"edad":edad,"sexo":sexo,"ubicaciondisp1":ubicaciondisp1,"ubicaciondisp2":ubicaciondisp2,"ubicaciondisp3":ubicaciondisp3,"disparomascercano":disparomascercano,"promediodedisparos":promediodispredond}
            archivo.seek(0)
            json.dump(data,archivo,indent=4)
            archivo.truncate()
            print("el promedio de los disparos es " + str(promediodispredond))
            print("participante creado")

class listapart:
    def __init__(self):
        with open("participantes.json","r+") as usuarios:
            dicttemp={}
            listaedades=[]
            listanombres=[]
            listaapellidos=[]
            z=0
            r=0
            participantes1=json.load(usuarios)

            for majorkey,subdict in participantes1.items():
                a=subdict["nombre"]
                b=subdict["apellido"]
                c=subdict["edad"]
                dicttemp.update({"nombre":a,"apellido":b,"edad":c})
            for i,y in dicttemp.items():
                print(y)

#disparo(nombre,apellido,edad,sexo,ubicaciondisp1,ubicaciondisp2,ubicaciondisp3)

#print(mostrarpar(nombre,apellido,edad,sexo))

#guardardatos(nombre,apellido,edad,sexo,ubicaciondisp1,ubicaciondisp2,ubicaciondisp3)

#print(concurso(nombre,apellido,edad,sexo,ubicaciondisp1,ubicaciondisp2,ubicaciondisp3))

#Ordena nadamas por key numerica tipo string
#def ordenarpart():
    #with open("participantes","r+") as archivo1:
        #with open("participantestest23.json","w") as archivo2:
            ##data=json.load(archivo1)
            #json.dump(data,archivo2,sort_keys=True,indent=4)

listapart()