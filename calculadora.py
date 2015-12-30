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
	
	def calcular(self,operacion,contador):
		while contador > 0:
			pos = self.array_resultado.index(operacion);
			nro1 = float(self.array_resultado[pos-1])
			nro2 = float(self.array_resultado[pos+1])

			if operacion == "*":
				resultado = nro1 * nro2
			if operacion == "/":
				resultado = nro1 / nro2
			if operacion == "+":
				resultado = nro1 + nro2
			if operacion == "-":
				resultado = nro1 - nro2

			self.array_resultado[pos-1:pos+2] = [str(resultado)]
			contador = contador-1
			print self.array_resultado
		
	def resolver(self):
		array_ecuacion = self.get_array_ecuacion(self.ecuacion)
		self.array_resultado = array_ecuacion
		resultado = 0

		contador = self.array_resultado.count("*")
		self.calcular("*",contador)

		contador = self.array_resultado.count("/")
		self.calcular("/",contador)

		contador = self.array_resultado.count("+")
		self.calcular("+",contador)

		contador = self.array_resultado.count("-")
		self.calcular("-",contador)


# ------------------------------------------------
ecuacion = raw_input("Ingrese ecuacion: ")
c = Calculadora(ecuacion);
c.resolver()