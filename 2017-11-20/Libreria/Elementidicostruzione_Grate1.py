from larlib import *
from pyplasm import *

def grate():
	Grate  = CYLINDER([0.05,1.4])(12)
	Finestrella = CUBOID([1,1.5,0.5])
	Centro_Finestrella = CUBOID([0.90,1.30,0.5])
	Centro_Finestrella = T([1,2])([0.05,0.10])(Centro_Finestrella)
	#VIEW(DIFFERENCE([Finestrella,Centro_Finestrella]))
	Finestra = DIFFERENCE([Finestrella,Centro_Finestrella])
	Finestra = TEXTURE('\windows\system32\Github\Font_Pareti_Ombreggiatura.jpg')(Finestra)
	Grate = R([2,3])((3*PI)/2)(Grate)
	Grate = T([2,3])([0.05,0.25])(Grate)
	Grate = STRUCT(NN(2)([T(1)(0.35),Grate]))
	Grate = COLOR([0,0,0])(Grate)
	#VIEW(STRUCT([Finestra,Grate]))
	Finestra1 = STRUCT([Finestra,Grate])
	Grate2 = CYLINDER([0.05,0.95])(12)
	Grate2 = R([1,3])((3*PI)/2)(Grate2)
	Grate2 = T([1,3])([0.03,0.25])(Grate2)
	Grate2 = COLOR([0,0,0])(Grate2)
	Grate2 = STRUCT(NN(3)([T(2)(0.35),Grate2]))
	#VIEW(Grate2)
	#VIEW(STRUCT([Finestra1,Grate2]))
	Grate_Complete = STRUCT([Finestra1,Grate2])
	return Grate_Complete 