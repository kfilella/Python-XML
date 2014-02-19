'''
Kevin Filella Lok -- 200800084

COMANDOS PARA LA SUSTENTACION

INGRESAR 3 PARA RELEASE DATE
INGRESAR 4 PARA RECORRIDO HASTA EL ROOT

NOTA : EL ARCHIVO XML DE NUESTRO PROYECTO SE LLAMA "device.xml", RENOMBRAR
'''
import sys

class Device:
    def __init__ (self,id_device,user_agent,fall_back):
        self.id = id_device
        self.user = user_agent
        self.fall = fall_back

    def impridevice (self):
                print 'Device: id='+self.id+' user_agent='+self.user+' fall_back='+self.fall

class Group:
    def __init__ (self,id_group):
        self.id = id_group

    def imprigroup (self):
                print 'Group: id='+self.id
    
class Capability:
    def __init__ (self,name,value):
        self.name = name
        self.value = value

    def impricapability (self):
                print 'Capability: name='+self.name+' value='+self.value

class Grupo:
    def __init__ (self,Device,Group,Capability):
        self.device = Device
        self.group = Group
        self.capability = Capability
        
def quitarBasura1(lines):
        newlines = []
        for str in lines:
                newline = str.translate(None,'""')
                newlines.append(newline)
        return newlines


def quitarBasura(lines):
        newlines = []
        for str in lines:
                newline = str.replace('<',' ').replace('>',' ').replace('=',' ').replace('/',' ').split()
                #newline = str.translate(None,'<>=/\""')
                newlines.append(quitarBasura1(newline))
        return newlines

def creardevice(lista):
    id=""
    user=""
    fall=""
    for n in range(len(lista)):
        if lista[n]=='id': 
            id=lista[n+1]
        else :
            if lista[n]=='user_agent': 
                user=lista[n+1]
            else :
                if lista[n]=='fall_back': 
                    fall=lista[n+1]
    return Device(id,user,fall)
    
def creargroup(lista):
    id=""
    for n in range(len(lista)):
        if lista[n]=='id': 
            id=lista[n+1]
    return Group(id)
        

def crearcapability(lista):
    name=""
    value=""
    for n in range(len(lista)):
        if lista[n]=='name': 
            name=lista[n+1]
        else :
            if lista[n]=='value': 
                value=lista[n+1]
    return Capability(name,value)     
                

def prinicpal(lista):
    base =[]
    d=Device("","","")
    g=Group("")
    c=Capability("","")
    gro=Grupo(d,g,c)
    for n in range(len(lista)):
        lis=lista[n]
        for s in range(len(lis)):
            if 'device' in lis[s]:
                d=creardevice(lis)
            if 'group' in lis[s]:
                if len(lis[s])!=1:
                    g=creargroup(lis)
            if 'capability' in lis[s]:
                c=crearcapability(lis)
            gro=Grupo(d,g,c)
            base.append(gro)
    return base


def imprimirbase(lista):
    for n in range(len(lista)):
        print lista[n].device.id
        print lista[n].device.user
        print lista[n].device.fall
        print lista[n].group.id
        print lista[n].capability.name
        print lista[n].capability.value
        
        
def quitarencabezado(lines):
        newl = []
        a=0
        for str in lines:
                if '<devices>' in str:
                    a=1
                if a==1:
                    newl.append(str)
        return newl
    
def getDevice(grup):
    return grup.device
def iddevice(dev):
    return dev.id
def getCapability(gru):
    return gru.capability

def valuecapability(capa):
    return capa.value

def namecapability(capa):
    return capa.name
def fallbackdevice(dev):
    return dev.fall

def buscarfallbacklista(opc,base):
    lista=[]
    for x in base:
        iddev= iddevice ( getDevice( x))
        cp= fallbackdevice( getDevice( x))
        if(opc==cp):
            lista.append(iddev)
    return lista

def agregartododevice(base):
    lista=[]
    for x in base:
        iddev=iddevice(getdevice(x))
        lista.append(iddev)
    return lista

def buscarcaparoot(capa,base):
    for x in base:
        iddev=iddevice(getDevice(x))
        cp= namecapability ( getCapability( x))
        if(iddev=='generic' and cp==capa):
            return True
        else :
            return False
        
def buscarcapabilitylista(opc,base):
    lista=[]
    if(buscarcaparoot(opc,base)==True):
        lista.append(agregartododevice(base))
    else :
        for x in base:
            iddev= iddevice ( getDevice( x))
            cp= namecapability ( getCapability( x))
            if(opc==cp):
                lista.append(iddev)
    return lista

def eliminarrepetidos(lista):
    list=[]
    list.append(lista[0])
    y=0
    for x in range(len(lista)):
        if lista[x]!=list[y]:
            y=y+1
            list.append(lista[x])
    return list

####################################
####################################
########## EJERCICIO 1 #############
####################################
####################################

# ESTADO - FUNCIONAL
# NOTAS - La funcion compara el 'name' del capability para que sea "release_date", si se cumple esto,
#         verifica el 'value' de este capability para que empiece con el anio ingresado por el usuario,
#         si se cumple, se agrega a una lista. Al final, retorna la lista con los ID de los devices.
def buscarreleasedate(opc,base):
    list=[]
    for x in base:
        iddev = iddevice(getDevice(x))
        namecp = namecapability(getCapability(x))
        valuecp = valuecapability(getCapability(x))
        if (namecp=="release_date" and (opc in valuecp)):
            list.append(iddev)
    return list

####################################
####################################
########## EJERCICIO 2 #############
####################################
####################################

# ESTADO - INCOMPLETO
# NOTAS - La recursion se vuelve infinita y excede el limite de recursion de Python (14000), asi que se intento hacer una version iterativa.
def recorridoericsson(base,opc):
    list=[]
    for x in base:
        iddev = iddevice(getDevice(x))
        falldev = fallbackdevice(getDevice(x))
        if((iddev.startswith(opc) and falldev.startswith(opc)) or (iddev.startswith(opc) and falldev.startswith("generic")) or ((opc in iddev) and ("generic" in falldev)) or (iddev == "generic") or (iddev=="generic_xhtml") or (iddev=="generic_mobile")):
            list.append(iddev)
    return list
    
def buscar(lista,imput):
    base=prinicpal(lista)
    #imprimirbase(base) # no ejecutar si estas con el archivo grande.. XD
    #print lista
    print ":D"
    print "Archivo cargado."
    if imput==1 :
        print "Ingrese el Fall_back que desea buscar:"
        opc=raw_input("Digite:")
        print  "los device con el fall_back "+opc+" son :"
        lsta= eliminarrepetidos( buscarfallbacklista( opc, base))
        
        print lsta
        
        print ""
        print ("el numero de dispositivos son: " )
    if imput==2:
        print "Ingrese el Capability que desea buscar:"
        opc=raw_input("Digite:")
        print  "los device con el capability "+opc+" son :"
        lst = eliminarrepetidos(buscarcapabilitylista(  opc ,base))
        print lst 
        print ""
        print ("el numero de dispositivos son: " )
    if imput==3:
        print "Ingrese el release date: "
        opc=raw_input("Digite: ")
        print  "los devices con release date "+opc+" son :"
        lst1 = eliminarrepetidos(buscarreleasedate(opc,base))
        print lst1
        print ""
        print ("el numero de devices es: "+str(len(lst1)))
    if imput==4:
        print "Ingrese el ID para recorrido: "
        opc=raw_input("Digite: ")
        print "Los fall_backs que cumplen con la condicion son: "
        lst2 = eliminarrepetidos(recorridoericsson(base,opc))
        print lst2
    else :
        sys.exit(1)
    
    
    
print ""
print ""
print "**********Parser xml**********"
print "*************************************"
print "*Integrantes:                       *"
print "*             Adrian Aguilar        *"
print "*             Kevin Filella         *"
print "*             Edison Sanchez        *"
print "*                                   *"
print "*************************************"
print ""
print ("Leyendo el archivo device.xml")
with open('device.xml') as f:
        lines = f.read().splitlines()
print "cargado de documento exitoso"
l=quitarencabezado(lines)
lista = quitarBasura(l)
#print lista
print "que desea realizar?"
print "1.-buscar device por fall Back"
print "2.-buscar device por capability"
print "3.-RELEASE DATE"
print "4.-ROOT"
print "3.-salir"
n = input("Digite:")
print n
buscar( lista, n)







"""

a = Device ("id dev","user dev","fall dev")
a.impridevice()
b = Group ("id group")
b.imprigroup()
c = Capability ("name capa","value capa")
c.impricapability()
g = Grupo(a,b,c)
"""
