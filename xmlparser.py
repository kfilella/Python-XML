'''
Created on 26/01/2014

@author: adrian
'''
import sys
sys.setrecursionlimit(1000000)

class Device:
    def __init__ (self,id_device,user_agent,fall_back,root_):
        self.id = id_device
        self.user = user_agent
        self.fall = fall_back
        self.root= root_
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
    root="false"
    print lista
    print"-----------------------------------"
    for n in range(len(lista)):
        if lista[n]=='id': 
            id=lista[n+1]
        else :
            if lista[n]=='user_agent': 
                user=lista[n+1]
            else :
                if lista[n]=='fall_back': 
                    fall=lista[n+1]
                    if lista[n+1]=="root":
                        root="true"
                else :
                    if lista[n]=='actual_device_root':
                        root=lista[n+1]
    return Device(id,user,fall,root)
    
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
    d=Device("","","","")
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
        print lista[n].device.root
        print lista[n].group.id
        print lista[n].capability.name
        print lista[n].capability.value
        print "--------------------------"
        
        
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
def fallbackdevice(dev):
    return dev.fall
    
    

def buscarfallbacklista(opc,base):
    lista=[]
    for x in base:
        iddev= iddevice ( getDevice( x))
        cp= fallbackdevice( getDevice( x))
        if(opc in cp):
            lista.append(iddev)
    return lista
<<<<<<< HEAD

def agregartododevice(base):
=======
             
def comprobaarroot(lista ,id,opc,i):
    list=[]
    d=i
    for x in range (d,len(lista)):
        d=d+1
        iddev= iddevice(getDevice( lista[x]))
        root=getroot(getDevice(  lista[x]))
        fall=fallbackdevice( getDevice(  lista[x]))
        if(root=="true"):
            if iddev==id:
                
                print  root
                print iddev
                cp= namecapability ( getCapability(  lista[x]))
                if(opc == cp):
                    list.append(iddev)
        #else:
         #   if(root=="false"):
          #      comprobaarroot(lista,fall,opc,d)
    return list
    

def buscarcapabilitylista1(lista,id,opc,ida):
    
    l=[]
    
    for x in lista:
        
        if id==x.device.id and id!="":
            print id
            print x.device.id
            print"-----------------"
            if opc==x.capability.name:
                l.append(id)
                l.append(ida)
               

    return l
            
            
            
        
        
        
        
    
    
def getroot(dev):
    return dev.root
 
def buscarcapabilitylista(opc,base):
>>>>>>> cb8c9f82e0ed5ce82b117de3ab76996e2da5367e
    lista=[]
    idroot=iddevice ( getDevice( base[0]))
    rot=base[0].device.root
    fal=base[0].device.fall
    for x in base:
<<<<<<< HEAD
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
=======
        root=getroot(getDevice( x))
        iddev= iddevice ( getDevice( x))
        fall=fallbackdevice( getDevice( x))
        cp= namecapability ( getCapability( x))
        if idroot !=iddev: 
            if(rot=="false"):
                rot=root
                lista.extend(buscarcapabilitylista1(base,fal,opc,idroot))
                fal=fall
            idroot=iddev
            
        else:
                idroot=iddev
                fal=fall
                rot=root
                if(opc == cp):
                    lista.append(iddev)
                
                    
>>>>>>> cb8c9f82e0ed5ce82b117de3ab76996e2da5367e
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
        
        
        
def imprimirroot(lista):
    list=[]
    for n in range(len(lista)):
        if lista[n].device.root=="true":
            list.append( lista[n].device.id)
    return list
    
    
def buscar(lista,imput):
    base=prinicpal(lista)
<<<<<<< HEAD
=======
    #l=eliminarrepetidos(imprimirroot(base))
    #print l
>>>>>>> cb8c9f82e0ed5ce82b117de3ab76996e2da5367e
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
        print ("el numero de dispositivos son: " +len(str(lsta)))
    else :
        if imput==2:
            print "Ingrese el Capability que desea buscar:"
            opc=raw_input("Digite:")
            print  "los device con el capability "+opc+" son :"
            lst = eliminarrepetidos(buscarcapabilitylista(  opc ,base))
            print lst 
            print ""
            print ("el numero de dispositivos son: "+len(str(lst)))
            
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
