logfile = "emunpi.log"

warnings = 0
requests = 0
sends = 0
with open(logfile) as file:
	data = file.readlines()

for line in data:
	if "LOOP" in line:
		requests = requests + 1
	if "WUN" in line:
		sends = sends + 1
	if "WARNING:__main__:Recepcion incorrecta de la informacion" in line:
		warnings = warnings + 1
porc_error = 100 - (float(warnings)/float(requests))*100

print ("# Pedidos a la consola: " + str(requests))
print ("# Datos no recibidos: " + str(warnings))
print ("Porcentaje de exito: " + str("%.2f" % porc_error) + "%")
print ("# de envios a WUN: " + str(sends))