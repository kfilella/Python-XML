'''
Created on 26/01/2014

@author: adrian
'''

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
                if lista[n]=='user_agent': 
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
            if 'devices' in lis[s]:
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
        
with open('device.xml') as f:
        lines = f.read().splitlines()
l=quitarencabezado(lines)
lista = quitarBasura(l)
base=prinicpal(lista)
imprimirbase(base) # no ejecutar si estas con el archivo grande.. XD
#print lista
print ":D"
print "Archivo cargado."
"""

a = Device ("id dev","user dev","fall dev")
a.impridevice()
b = Group ("id group")
b.imprigroup()
c = Capability ("name capa","value capa")
c.impricapability()
g = Grupo(a,b,c)
"""
