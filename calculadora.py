class Calculadora:
	def __init__(self,ecuacion):
		self.ecuacion_original = ecuacion
		self.ecuacion = self.get_array_ecuacion(ecuacion)
		self.ini = 0
		self.fin = 0
	
	def get_array_ecuacion(self,ecuacion):
		nro = ''
		array_ecuacion = []

		for char in ecuacion:
			if char.isdigit():
				nro = nro + char
			else:
				if nro != '':
					array_ecuacion.append(nro)
					nro = ''
				array_ecuacion.append(char)
			
		if nro != '':
			array_ecuacion.append(nro)

		return array_ecuacion

	def get_ecuacion(self):
		ecuacion = []
		aux = []
		if self.ecuacion.count(')'):
			i = self.ecuacion.index(')')
			self.fin = i+1
		
			while i > 0:
				i = i-1
				if self.ecuacion[i] == '(':
					self.ini = i
					break
				else:
					ecuacion.append(self.ecuacion[i])
			ecuacion.reverse()
		else:
			self.ini = 0
			self.fin = len(self.ecuacion)
			ecuacion = self.ecuacion
		return ecuacion
	
	def actualizar_ecuacion(self,ecuacion):
		self.ecuacion[self.ini:self.fin] = ecuacion

	def calcular(self,ecuacion,operacion,contador):
		while contador > 0:
			pos = ecuacion.index(operacion);
			nro1 = float(ecuacion[pos-1])
			nro2 = float(ecuacion[pos+1])

			if operacion == '*':
				resultado = nro1 * nro2
			if operacion == '/':
				resultado = nro1 / nro2
			if operacion == '+':
				resultado = nro1 + nro2
			if operacion == '-':
				resultado = nro1 - nro2

			ecuacion[pos-1:pos+2] = [str(resultado)]
			contador = contador-1
		return ecuacion
		
	def resolver(self):
		ecuaciones = self.ecuacion.count(')')

		while ecuaciones >= 0:
			ecuaciones = ecuaciones-1
			ecuacion = self.get_ecuacion()

			contador = ecuacion.count('*')
			ecuacion = self.calcular(ecuacion,'*',contador)

			contador = ecuacion.count('/')
			ecuacion = self.calcular(ecuacion,'/',contador)

			contador = ecuacion.count('+')
			ecuacion = self.calcular(ecuacion,'+',contador)

			contador = ecuacion.count('-')
			ecuacion = self.calcular(ecuacion,'-',contador)

			self.actualizar_ecuacion(ecuacion)
		
		resultado = ecuacion[0]
		print "Resultado " + str(resultado)


# ------------------------------------------------
ecuacion = raw_input('Ingrese ecuacion: ')
c = Calculadora(ecuacion);
c.resolver()