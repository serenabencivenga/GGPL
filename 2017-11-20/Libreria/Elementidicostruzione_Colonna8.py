from larlib import *
from pyplasm import *

def columna(dm,h,h_base):
	cylndr = COMP([JOIN,TRUNCONE([0.5,0.5,1])])(24)
	torus_bot = COMP([JOIN,TORUS([dm/12,dm/2])])([8,24])
	torus_top = COMP([JOIN,TORUS([0.8*(dm/12),0.8*(dm/2)])])([8,24])
	base = COMP([T([1,2])([7*dm/-12,7*dm/-12]),CUBOID])([7*dm/6,7*dm/6,h_base])
	base_top = COMP([T([1,2])([7*dm/-12,7*dm/-12]),CUBOID])([7*dm/6,7*dm/6,dm/6])
	capital = SUM([
        COMP([JOIN,TRUNCONE([0.8*dm/2,1.2 * dm /2, h/8])])(4),
        COMP([R([1,2])(PI/4),JOIN,TRUNCONE([0.8*dm/2,1.2 * dm/2 , h/8])])(4)
    ])
   
	return TOP([TOP([TOP([TOP([TOP([base,torus_bot]),cylndr]),torus_top]),capital]),base_top])




def colonne(dm,h,h_base):
	cylndr = CYLINDER([0.2,4])(24)
	torus_bot = COMP([JOIN,TORUS([dm/12,dm/2])])([8,24])
	torus_top = COMP([JOIN,TORUS([0.8*(dm/12),0.8*(dm/2)])])([8,24])
	base = COMP([T([1,2])([7*dm/-12,7*dm/-12]),CUBOID])([15*dm/6,10*dm/6,h_base])
	base_top = COMP([T([1,2])([7*dm/-12,7*dm/-12]),CUBOID])([15*dm/6,10*dm/6,dm/6])
	capital = SUM([
        COMP([JOIN,TRUNCONE([0.8*dm/2,1.2 * dm /2, h/8])])(4),
        COMP([R([1,2])(PI/4),JOIN,TRUNCONE([0.8*dm/2,1.2 * dm/2 , h/8])])(4)
    ])
   
	return TOP([TOP([TOP([TOP([TOP([base,torus_bot]),cylndr]),torus_top]),capital]),base_top])