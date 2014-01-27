class Device:
	def __init__ (self,id_device,user_agent,fall_back):
		self.id = id_device
		self.user = user_agent
		self.fall = fall_back

	def impridevice (self):
                print ('Device: id='+self.id+' user_agent='+self.user+' fall_back='+self.fall)

class Group:
	def __init__ (self,id_group):
		self.id = id_group

	def imprigroup (self):
                print ('Group: id='+self.id)
	
class Capability:
	def __init__ (self,name,value):
		self.name = name
		self.value = value

	def impricapability (self):
                print ('Capability: name='+self.name+' value='+self.value)

class Grupo:
	def __init__ (self,device,group,capability):
		self.device = device
		self.group = group
		self.capability = capability

def quitarBasura(lines):
        newlines = []
        for str in lines:
                newline = str.translate(None,"<>=/\" ")
                newlines.append(newline)
        return newlines
		
with open('test1.xml') as f:
        lines = f.read().splitlines()
lista = quitarBasura(lines)

for line in lista:
	print line



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
