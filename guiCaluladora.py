#!/usr/bin/env python
import calculadora
from Tkinter import *

class Ventana():
	def __init__(self,title="Mi Ventana",resizablex=TRUE,resizabley=TRUE):
		self.root = Tk()
		self.root.title(title)
		self.root.resizable(resizablex,resizabley)
		self.entry = {}

	def start(self):
		self.root.mainloop()

	def addBtn(self,text="",row=0,column=0,columnspan=1,rowspan=1,font="Arial",fSize=16):
		btn = Button(self.root,text=text,font=(font,fSize))
		btn.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan,sticky=W+E+N+S)
		btn.bind("<Button-1>",self.onclick)

	def addEntry(self,entryname,row=0,column=0,columnspan=1,rowspan=1,font="Arial",fSize=16):
		self.value = ""
		self.entry[entryname] = Entry(self.root,textvariable=self.value,font=(font,fSize),bg="white")
		self.entry[entryname].grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, sticky=W+E+N+S)

	def onclick(self,event):
		char  = event.widget.configure("text")[4]
		
		if char == "C":
			self.value = ""
			self.entry['ecuacion'].delete(0,END)
			
		elif char == "=":
			self.value = self.entry['ecuacion'].get()
			c = calculadora.Calculadora(self.value)
			try:
				c.resolver()
				self.entry['ecuacion'].delete(0,END)
				self.entry['ecuacion'].insert(0,c.resultado)
				self.value = ""

			except Exception, e:
				self.entry['ecuacion'].delete(0,END)
				self.entry['ecuacion'].insert(0,"Error!")
				self.value = ""
				
		else :
			self.value = self.entry['ecuacion'].get()
			self.value = self.value + char
			self.entry['ecuacion'].delete(0,END)
			self.entry['ecuacion'].insert(0,self.value)


v = Ventana("Calculadora",FALSE,FALSE)

v.addEntry("ecuacion",0,0,4)

v.addBtn("7",2,0)
v.addBtn("8",2,1)
v.addBtn("9",2,2)
v.addBtn("4",3,0)
v.addBtn("5",3,1)
v.addBtn("6",3,2)
v.addBtn("1",4,0)
v.addBtn("2",4,1)
v.addBtn("3",4,2)
v.addBtn("0",5,0)
v.addBtn(".",5,1)

v.addBtn("C",1,0)
v.addBtn("(",1,1)
v.addBtn(")",1,2)

v.addBtn("+",4,3)
v.addBtn("-",3,3)
v.addBtn("*",2,3)
v.addBtn("/",1,3)

v.addBtn("=",5,2,2)

v.start()