
class Device:
	def __init__(self, name, connectedBy):
		self.Name = name
		self.ConnectedBy = connectedBy
		self.connected = True

	def __str__(self):
		return f"Device {self.Name} is connected by {self.ConnectedBy}"

	def disconnect(self):
		self.connected = False
		print("Device is disconnected")
	
class Scanner(Device):
	def __init__(self, name, connectedBy, resolution):
		super().__init__(name, connectedBy)
		self.Resolution = resolution

	def __self__(self):
		return f"{super().__str__(self)} and the resolution is {self.Resolution}"
		
	def scan(self, document):
		if not self.connected:
			print(f"The scanner {self.Name} is not connected")
		else:
			print(f"The scanner {self.Name} is scanning {document} at {self.Resolution} resulotion")

scan = Scanner("scani w7f", "Wifi", 1800)
print(scan)
scan.scan("Passport")
scan.disconnect()
scan.scan("card")