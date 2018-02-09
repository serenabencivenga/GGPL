from larlib import *
from pyplasm import *

def comignolo() :
	Caminetto = CUBOID([3,4,3])
	Cubetto = CUBOID([3,2,3])
	Cubetto = T(2)(4)(Cubetto)
	Asta = CUBOID([0.40,1.5,10])
	Asta = T([1,2])([0.15,4.25])(Asta)
	Asta = STRUCT(NN(5)([Asta,T(1)(0.75)]))
	Cubetto = DIFFERENCE([Cubetto,Asta])
	Asta = R([1,3])(PI/2)(Asta)
	Asta = T(1)(3)(Asta)
	Cubetto = DIFFERENCE([Cubetto,Asta])
	Caminetto = STRUCT([Caminetto,Cubetto])
	Camin = CUBOID([2,10,2])
	Camin = T([1,3])([0.5,0.5])(Camin)
	Caminetto = DIFFERENCE([Caminetto,Camin])
	Cubetto = DIFFERENCE([Cubetto,Camin])
	Cubetto = TEXTURE('\windows\system32\Github\images.jpg')(Cubetto)
	Caminetto = STRUCT([Caminetto,Cubetto])
	#VIEW(Caminetto)
	Parte_Superiore = CUBOID([3.05,1.5,3])
	Tetto = CUBOID([3,1.5,3])
	Tetto1 = R([1,2])(PI/4)(Tetto)
	Tetto2 = CUBOID([3,2.5,3])
	Tetto2 = R([1,2])(PI/4)(Tetto2)
	Tetto2 = T(1)(3)(Tetto2)
	Parte_Superiore = DIFFERENCE([Parte_Superiore,Tetto1])
	Parte_Superiore = DIFFERENCE([Parte_Superiore,Tetto2])
	#VIEW(Parte_Superiore)
	Tettino = CUBOID([2.2,0.2,3])
	Tettino = R([1,2])(PI/4)(Tettino)
	Tettino = TEXTURE('\windows\system32\Github\Muro.jpg')(Tettino)
	################
	Final2 = STRUCT([Parte_Superiore,Tettino])
	#VIEW(Final2)
	Tettino = T(1)(3)(Tettino)
	Tettino = R([1,2])(PI/2)(Tettino)
	Tettino = T([1,2])([3.1,-2.98])(Tettino)
	Tetto_Superiore = STRUCT([Final2,Tettino])
	Tetto_Superiore = T(2)(6)(Tetto_Superiore)
	Camino_Completo = STRUCT([Tetto_Superiore,Caminetto])
	return Camino_Completo

	
	

