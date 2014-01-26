class Device:
	def __init__ (self,id_device,user_agent,fall_back):
		self.id = id_device
		self.user = user_agent
		self.fall = fall_back

	def impridevice (self)
                print 'ID: '+self.id+' User_Agent: '+self.user+' Fall_Back: '+self.fall

class Group:
	def __init__ (self,id_group):
		self.id = id_group
	
class Capability:
	def __init__ (self,name,value):
		self.name = name
		self.value = value
	
class Grupo:
	def __init__ (self,device,group,capability):
		self.device = device
		self.group = group
		self.capability = capability

lista = open("device.xml",'r')
