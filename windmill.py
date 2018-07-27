#rotation of windmill
# -*- coding: utf-8 -*-
from tkinter import *
from math import sin, cos, radians, pi
import time

def rotation(x,y):

	Rot = 	[[cos(theta), -sin(theta), (xr*(1 - cos(theta))) + (yr*(sin(theta)))],
      		[sin(theta), cos(theta),  (yr*(1 - cos(theta))) - (xr*(sin(theta)))],
      		[0,              0,                    1                           ]]

	P =     [[x],
		[y],
		[1]]

	result = [[0],
	  	 [0],
	   	 [0]]


	#Matrix multiplication result=Rot.P
	# iterate through rows of Rot
	for i in range(len(Rot)):
		# iterate through columns of P
		for j in range(len(P[0])):
			# iterate through rows of P
			for k in range(len(P)):
				result[i][j] += Rot[i][k] * P[k][j]

	return result[0][0], result[1][0]

master=Tk()
canvas_width=master.winfo_screenwidth()
canvas_height=master.winfo_screenheight()
w=Canvas(master,width=canvas_width,height=canvas_height)
w.pack()

#origin
ox,oy=canvas_width/2,canvas_height/2
xr,yr=(ox+400,oy-375) #center of windmill fan
a1,b1,a2,b2 = ox+415, oy-300, ox+480, oy-340
c1,d1,c2,d2 = ox+470, oy-420, ox+420, oy-465
e1,f1,e2,f2 = ox+330, oy-430, ox+315, oy-375

while True:
	w.delete("all")
	w.create_line(canvas_width/2,0,canvas_width/2,canvas_height)
	w.create_line(0,canvas_height/2,canvas_width,canvas_height/2)
	theta = radians(1)
	a1,b1 = rotation(a1,b1)
	a2,b2 = rotation(a2,b2)
	c1,d1 = rotation(c1,d1)
	c2,d2 = rotation(c2,d2)
	e1,f1 = rotation(e1,f1)
	e2,f2 = rotation(e2,f2)
	#drawing windmill
	points1 = [xr,yr, a1,b1,a2,b2]
	points2 = [xr,yr, c1,d1,c2,d2]
	points3 = [xr,yr, e1,f1,e2,f2]
	points4 = [xr,yr, ox+370, oy-100, ox+430, oy-100]
	w.create_polygon(points1,fill='#7f7fff')
	w.create_polygon(points2,fill='#7f7fff')
	w.create_polygon(points3,fill='#7f7fff')
	w.create_polygon(points4,fill='#800000')
	master.update()
	time.sleep(0.005)

mainloop()




     



