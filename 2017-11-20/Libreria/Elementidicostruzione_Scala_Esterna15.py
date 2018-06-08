from larlib import *
from pyplasm import *
from Elementidicostruzione_Colonna8 import *

def scale_esterne():
	scalino = CUBOID([4,0.3,4])
	#VIEW(scalino)
	scale = STRUCT(NN(8)([scalino,T([2,3])([0.3,0.3])]))
	scale = TEXTURE('\windows\system32\Github\Scale.jpg')(scale)

	#VIEW(scale)
	Colonna_Laterale = columna(0.5,8,0.5)
	Colonna_Laterale = T([1,2])([0.1,0.6])(Colonna_Laterale)
	#Colonne = STRUCT(NN(2)([Colonna_Laterale,T([1,3])([16.5,1])]))
	Colonna = T(1)(4)(Colonna_Laterale)
	Colonne = STRUCT([Colonna,Colonna_Laterale])
	Colonne = R([2,3])(PI/2)(Colonne)
	Colonne = R([2,3])(PI/2)(Colonne)
	Colonne = R([2,3])(PI/2)(Colonne)
	Colonne = TEXTURE('\windows\system32\Github\Scale.jpg')(Colonne)

	#Colonne = R([1,3])(PI/2)(Colonne)
	Final = STRUCT([Colonne,scale])
	#VIEW(Final)
	Mura = CUBOID([0.2,4,6])
	Mura = R([2,3])(0)(Mura)
	#Mura = T([1,3])([-1,3])(Mura)
	Mura = TEXTURE('\windows\system32\Github\Muro.jpg')(Mura)
	Mura = T([1,3])([-0.1,-0.1])(Mura)
	Mura_2 = T(1)(4.8)(Mura)
	Mura_2 = TEXTURE('\windows\system32\Github\Muro.jpg')(Mura_2)
	Final_2 = STRUCT([Final,Mura,Mura_2])
	#VIEW(Final_2)
	#Strutt = CUBOID([20,10,10])
	#Parte_Sotto = DIFFERENCE([Strutt,scale])
	#VIEW(STRUCT([Parte_Sotto,Final_2]))
	Muro_Ob = CUBOID([1,6,20])
	Muro_Ob = R([2,3])(11*PI/6)(Muro_Ob)
	Muro_Ob = T([1,2])([-0.1,2.8])(Muro_Ob)
	Mura = DIFFERENCE([Mura,Muro_Ob])
	Mura = TEXTURE('\windows\system32\Github\Muro.jpg')(Mura)

	Muro_Ob_2 = T(1)(4)(Mura)

	Final_2 = STRUCT([Final,Mura,Muro_Ob_2])
	#VIEW(Final_2)
	#VIEW(Final_2)
	#Prato = CUBOID([50,1,50])
	#Prato = TEXTURE('\windows\system32\Github\Prato.jpg')(Prato)
	#Final_3 = STRUCT([Final_2,Prato])
	#VIEW(Final_3)
	#VIEW(Final_3)
	return Final_2