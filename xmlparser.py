'''
Created on 26/01/2014

@author: adrian
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
    
def namecapability(capa):
    return capa.name
    
    
#def buscarfallbacklista(opc,  lista):
 #   print( "buscarfallback"++opc) 
 
def buscarcapabilitylista(opc,base):
    lista=[]
    for x in base:
        iddev= iddevice ( getDevice( x))
        cp= namecapability ( getCapability( x))
        if(opc==cp):
            lista.append(iddev)
    return lista
        
        
    
    
def buscar(lista,imput):
    base=prinicpal(lista)
    imprimirbase(base) # no ejecutar si estas con el archivo grande.. XD
    #print lista
    print ":D"
    print "Archivo cargado."
    if imput==1 :
        print "Ingrese el Fall_back que desea buscar:"
        opc=raw_input("Digite:")
        print  "los device con el fall_back "+opc+" son :"
        #lsta=  buscarfallbacklista(  opc, base)
        
        print ""
        print ("el numero de dispositivos son: " )
    else :
        if imput==2:
            print "Ingrese el Capability que desea buscar:"
            opc=raw_input("Digite:")
            print  "los device con el capability "+opc+" son :"
            lst = buscarcapabilitylista(  opc ,base)
            print lst 
            print ""
            print ("el numero de dispositivos son: ")
            
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
with open('test1.xml') as f:
        lines = f.read().splitlines()
print "cargado de documento exitoso"
l=quitarencabezado(lines)
lista = quitarBasura(l)
#print lista
print "que desea realizar?"
print "1.-buscar device por fall Back"
print "2.-buscar device por capability"
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
