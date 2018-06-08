from larlib import *
from pyplasm import *

def finestra() :
#Finestre

#Vetro
	def hex_material(color, light, trasparence):

		def hex_to_rgb(value):
			value = value.lstrip('#')
			lv = len(value)
			return map(lambda x: x/255., list(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3)))

		params = hex_to_rgb(color) + [.1] + \
				hex_to_rgb(light) + [trasparence] +\
				hex_to_rgb(light) + [.1] +\
				hex_to_rgb("#000000") + [.1] +\
				[100]

		return MATERIAL(params)
	window = CUBOID([1.5,3.8,0.01])
	window = hex_material("#ffffff", "#ffffff",0.6)(window)
	#VIEW(window)
	Finestra = CUBOID([1.5,4,0.1])
	Fin = CUBOID([1.3,3.5,0.5])
	Fin = T([1,2])([0.1,0.3])(Fin)
	Base_Finestra = DIFFERENCE([Finestra,Fin])
	Base_Finestra = TEXTURE('\windows\system32\Github\Font_Pareti.jpg')(Base_Finestra)
	#VIEW(Base_Finestra)
	Fin2 = CUBOID([2,4.5,0.1])
	Fin2 = T([1,2])([-0.25,-0.3])(Fin2)
	Fin2 = DIFFERENCE([Fin2,Fin])
	Fin2 = T(3)(-0.11)(Fin2)
	Fin2 = TEXTURE('\windows\system32\Github\Font_Pareti_Ombreggiatura.jpg')(Fin2)
	Base_Finestra = STRUCT([Base_Finestra, Fin2])
	Separatore_Centrale = CUBOID([0.20,3.8,0.01])
	Separatore_Centrale = T([1,2])([0.68,0.2])(Separatore_Centrale)
	Separatore_Centrale = TEXTURE('\windows\system32\Github\Legno.jpg')(Separatore_Centrale)
	Separatore_Orizzontale = CUBOID([1.5,0.20,0.01])
	Separatore_Orizzontale = TEXTURE('\windows\system32\Github\Legno.jpg')(Separatore_Orizzontale)
	Separatore_Orizzontale = STRUCT(NN(3)([T(2)(0.85),Separatore_Orizzontale]))
	#VIEW(STRUCT([Separatore_Centrale,Base_Finestra,Separatore_Orizzontale]))
	Base_Finestra = STRUCT([Separatore_Centrale,Base_Finestra,Separatore_Orizzontale])
	#VIEW(Base_Finestra)

	#VIEW(STRUCT([Base_Finestra,window]))
	Finestra_Completa = STRUCT([Base_Finestra,window])
	#VIEW(STRUCT([Colonna_Laterale,Finestra_Completa]))
	hCol = 4.75
	def Column(argomenti):
		w,h = argomenti
		basis = CUBOID([w,w,2*w/3])
		trunk = CYLINDER ([w/2*0.85, h - w])(4)
		capitel = CUBOID([w,w,w/3])
		return TOP([TOP([trunk,basis]),capitel])
	MyColumn  = COMP([MKPOL,UKPOL,Column])([0.5,hCol])
	MyColumn = R([2,3])((3*PI)/2)(MyColumn)
	MyColumn = T([1,2])([-0.35,-0.28])(MyColumn)
	MyColumn = TEXTURE('\windows\system32\Github\Font_Pareti_Ombreggiatura.jpg')(MyColumn)
	MyColumn2 = T(1)(2.3)(MyColumn)
	#VIEW(STRUCT([Finestra_Completa,MyColumn,MyColumn2]))
	Finestra = STRUCT([Finestra_Completa,MyColumn,MyColumn2])
	Barretta = CUBOID([1.9,0.30,0.1])
	Barretta = T([1,2])([-0.1,4.17])(Barretta)
	Barretta = TEXTURE('\windows\system32\Github\Font_Pareti_Ombreggiatura.jpg')(Barretta)
	Finestra = STRUCT([Finestra,Barretta])
	#VIEW(Finestra)
	Sbarra = CYLINDER([0.09,3.5])(12)
	Sbarra = R([2,3])((3*PI)/2)(Sbarra)
	Sbarra = R([1,2])((3*PI)/2)(Sbarra)
	Sbarra = T([1,2])([-0.9,4.50])(Sbarra)
	Sbarra = TEXTURE('\windows\system32\Github\Font_Pareti_Ombreggiatura.jpg')(Sbarra)
	Sbarra2 = T(2)(0.09)(Sbarra)
	#VIEW(STRUCT([Finestra,Sbarra,Sbarra2]))
	Sbarre = STRUCT([Sbarra,Sbarra2])
	Sbarre_Inferiori = T(2)(-4.95)(Sbarre)
	Finestre = STRUCT([Finestra,Sbarra,Sbarra2,Sbarre_Inferiori])
	Canc = CUBOID([2,3.8,1])
	Canc = T([1,2,3])([-0.16,6.28,-0.10])(Canc)
	Sbarre = R([1,2])(PI/4)(Sbarre)
	Sbarre = T([1,2])([2.9,2])(Sbarre)
	Canc = CUBOID([2,3.8,1])
	Canc = T([1,2,3])([-0.16,6.28,-0.10])(Canc) 
	#VIEW(STRUCT([Finestre,Sbarre,Sbarra,Sbarra2,Sbarrette,Canc]))
	Prova1 = DIFFERENCE([Sbarre,Canc])
	Sbarrette = T(1)(3.7)(Sbarre)
	#VIEW(Sbarrette)
	Sbarrette = R([1,2])(-(3*PI)/2)(Sbarrette)
	Sbarrette = T([1,2])([7,1.8])(Sbarrette)
	Prova2 = DIFFERENCE([Sbarrette,Canc])
	Prova2 = TEXTURE('\windows\system32\Github\Font_Pareti_Ombreggiatura.jpg')(Prova2)
	Prova1 = TEXTURE('\windows\system32\Github\Font_Pareti_Ombreggiatura.jpg')(Prova1)
	#VIEW(STRUCT([Finestre,Prova1,Sbarra,Sbarra2,Prova2]))
	Finale = 	STRUCT([Finestre,Prova1,Sbarra,Sbarra2,Prova2])
	return Finale
