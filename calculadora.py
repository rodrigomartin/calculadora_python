class Calculadora:
	def __init__(self,ecuacion):
		self.ecuacion = ecuacion
		self.array_resultado = []
		self.pos_multiplicacion = 0

	
	def get_array_ecuacion(self,ecuacion):
		nro = ""
		array_ecuacion = []
		for caracter in self.ecuacion:
			if caracter.isdigit():
				nro = nro + caracter
			else:
				array_ecuacion.append(nro)
				array_ecuacion.append(caracter)
				nro = ""

		array_ecuacion.append(nro)
		return array_ecuacion
	

	def multiplicar(self):
		resp = True
		i=0

		for elemento in self.array_resultado:
			if not elemento.isdigit():
				if elemento == "*":
					nro1 = int(self.array_resultado[i-1])
					nro2 = int(self.array_resultado[i+1])
					resultado = nro1 * nro2
					self.array_resultado[i-1:i+2] = [str(resultado)]
					resp = False
					break
			i=i+1
		return resp

	def dividir(self):
		resp = True
		i=0

		for elemento in self.array_resultado:
			if not elemento.isdigit():
				if elemento == "/":
					nro1 = int(self.array_resultado[i-1])
					nro2 = int(self.array_resultado[i+1])
					resultado = nro1 / nro2
					self.array_resultado[i-1:i+2] = [str(resultado)]
					resp = False
					break
			i=i+1
		return resp

	def restar(self):
		resp = True
		i=0

		for elemento in self.array_resultado:
			if not elemento.isdigit():
				if elemento == "/":
					nro1 = int(self.array_resultado[i-1])
					nro2 = int(self.array_resultado[i+1])
					resultado = nro1 / nro2
					self.array_resultado[i-1:i+2] = [str(resultado)]
					resp = False
					break
			i=i+1
		return resp
	
	def sumar(self):
		resp = True
		i=0

		for elemento in self.array_resultado:
			if not elemento.isdigit():
				if elemento == "+":
					nro1 = int(self.array_resultado[i-1])
					nro2 = int(self.array_resultado[i+1])
					resultado = nro1 + nro2
					self.array_resultado[i-1:i+2] = [str(resultado)]
					resp = False
					break
			i=i+1
		return resp

	def resolver(self):
		array_ecuacion = self.get_array_ecuacion(self.ecuacion)
		self.array_resultado = array_ecuacion
		resultado = 0


		while self.dividir() is False:
			print self.array_resultado

		while self.multiplicar() is False:
			print self.array_resultado

		while self.sumar() is False:
			print self.array_resultado

		while self.restar() is False:
			print self.array_resultado

# ------------------------------------------------
ecuacion = raw_input("Ingrese ecuacion: ")
c = Calculadora(ecuacion);
c.resolver()

# en rama optimizacion