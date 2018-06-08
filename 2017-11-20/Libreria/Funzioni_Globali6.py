

from larlib import *
from Elementidicostruzione_Travi_Porticato2 import *
from Elementidicostruzione_Porta import *
from Elementidicostruzione_Finestra import *
from Elementidicostruzione_Scala_Esterna15 import *
#from Elementidicostruzione_Arco import *
from Elementidicostruzione_Comignolo import *
from Elementidicostruzione_Grate7 import *
from Elementidistrutturainterna2 import *
def finestrella() :
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
    window = CUBOID([1.5,1.5,0.01])
    window = hex_material("#ffffff", "#ffffff",0.6)(window)
    #VIEW(window)
    Finestra = CUBOID([1.5,1.5,0.1])
    Fin = CUBOID([1.3,1.3,0.5])
    Fin = T([1,2])([0.1,0.1])(Fin)
    Base_Finestra = DIFFERENCE([Finestra,Fin])
    Base_Finestra = TEXTURE('\windows\system32\Github\Font_Pareti.jpg')(Base_Finestra)
    #VIEW(Base_Finestra)
    Separatore_Centrale = CUBOID([0.20,1.5,0.01])
    Separatore_Centrale = T([1,2])([0.65,0.01])(Separatore_Centrale)
    Separatore_Centrale = TEXTURE('\windows\system32\Github\Legno.jpg')(Separatore_Centrale)
    Separatore_Orizzontale = CUBOID([1.5,0.20,0.01])
    Separatore_Orizzontale = TEXTURE('\windows\system32\Github\Legno.jpg')(Separatore_Orizzontale)
    Separatore_Orizzontale = STRUCT(NN(1)([T(2)(0.65),Separatore_Orizzontale]))
    #VIEW(STRUCT([Separatore_Centrale,Base_Finestra,Separatore_Orizzontale]))
    Base_Finestra = STRUCT([Separatore_Centrale,Base_Finestra,Separatore_Orizzontale])
    #VIEW(Base_Finestra)
    #VIEW(STRUCT([Base_Finestra,window]))
    Finestra_Completa = STRUCT([Base_Finestra,window])
    #VIEW(STRUCT([Colonna_Laterale,Finestra_Completa]))
    return Finestra_Completa
    
    

def porta_finestra() :
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
    window = CUBOID([1.9,3.9,0.1])
    window = hex_material("#ffffff", "#ffffff",0.6)(window)
    #VIEW(window)
    window = T([1,2])([0.04,0.04])(window)
    Finestra = CUBOID([2,4,0.1])
    Fin = CUBOID([1.9,3.9,0.3])
    Fin = T([1,2])([0.05,0.05])(Fin)
    Base_Finestra = DIFFERENCE([Finestra,Fin])
    Base_Finestra = TEXTURE('\windows\system32\Github\Font_Pareti.jpg')(Base_Finestra)
    #VIEW(Base_Finestra)
    S_P_C = CUBOID([0.2,4,0.1])
    S_P_C = T([1,3])([0.875,-0.1])(S_P_C)
    S_P_C = COLOR([0.3,0.4,0.4])(S_P_C)
    Separatore_Centrale = CYLINDER([0.05,4])(25)
    Separatore_Centrale = R([2,3])((3*PI)/2)(Separatore_Centrale)
    S_P_C_C_C = Separatore_Centrale
    S_P_C_C_C = COLOR([0.3,0.4,0.4])(S_P_C_C_C)
    #Separatore_Centrale = T([1,2,3])([0.95,0.01,0.6])(Separatore_Centrale)
    Separatore_Centrale = STRUCT(NN(7)([T(1)(0.28),Separatore_Centrale]))
    Separatore_Centrale = COLOR([0.3,0.4,0.4])(Separatore_Centrale)
    #VIEW(Separatore_Centrale)
    S_P_C_C = CUBOID([0.8,0.2,0.1])
    S_P_C_C = COLOR([0.3,0.4,0.4])(S_P_C_C)
    S_P_C_C = T([1,2,3])([0.6,1.6,-0.1])(S_P_C_C)
    Maniglia = JOIN(SPHERE(0.1)([18,36]))
    Maniglia = COLOR([0.8,0.6,0.2])(Maniglia)
    #VIEW(Maniglia)
    Maniglia = T([1,2,3])([0.7,1.7,-0.1])(Maniglia)
    S_P_C_C = STRUCT([S_P_C_C,Maniglia])
    #S_P_C_C = COLOR([0,3,0.4,0.4])(S_P_C_C)
    Separatore_Orizzontale = CYLINDER([0.05,2])(25)
    Separatore_Orizzontale = R([1,3])((3*PI)/2)(Separatore_Orizzontale)
    Separatore_Orizzontale = COLOR([0.3,0.4,0.4])(Separatore_Orizzontale)
    Separatore_Orizzontale1 = STRUCT(NN(3)([T(2)(0.2),Separatore_Orizzontale]))
    Separatore_Orizzontale2 = STRUCT(NN(7)([T(2)(0.2),Separatore_Orizzontale]))
    Separatore_Orizzontale2 = T(2)(2.60)(Separatore_Orizzontale2)
    Separatore_Orizzontale3 = STRUCT(NN(2)([T(2)(0.25),Separatore_Orizzontale]))
    Separatore_Orizzontale3 = T(2)(1.35)(Separatore_Orizzontale3)
    Separatore_Orizzontale = STRUCT([Separatore_Orizzontale1,Separatore_Orizzontale2])
    #VIEW(STRUCT([Separatore_Centrale,Base_Finestra,Separatore_Orizzontale]))
    Base_Finestra = STRUCT([Separatore_Centrale,Base_Finestra,Separatore_Orizzontale,S_P_C,S_P_C_C,S_P_C_C_C,Separatore_Orizzontale3])
    #VIEW(Base_Finestra)
    #VIEW(STRUCT([Base_Finestra,window]))
    Finestra_Completa = STRUCT([Base_Finestra,window])
    #VIEW(STRUCT([Colonna_Laterale,Finestra_Completa]))
    return Finestra_Completa


#finestra superiore posteriore formata con la funzione hex_material per il vetro

def finestrella_posteriore() :
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
    window = CUBOID([1.9,1.9,0.1])
    window = hex_material("#ffffff", "#ffffff",0.6)(window)
    window = T([1,2])([0.05,0.05])(window)
    #VIEW(window)
    Finestra = CUBOID([2,2,0.1])
    Fin = CUBOID([1.9,1.9,0.2])
    Fin = T([1,2])([0.05,0.05])(Fin)
    Base_Finestra = DIFFERENCE([Finestra,Fin])
    Base_Finestra = TEXTURE('\windows\system32\Github\Font_Pareti.jpg')(Base_Finestra)
    #VIEW(Base_Finestra)
    Separatore_Centrale = CYLINDER([0.05,2])(25)
    Separatore_Centrale = COLOR([0.3,0.4,.4])(Separatore_Centrale)
    Separatore_Centrale = STRUCT(NN(5)([T(1)(0.4),Separatore_Centrale]))
    Separatore_Centrale = T([1,2])([-0.2,0.01])(Separatore_Centrale)
    Separatore_Centrale = R([2,3])((3*PI)/2)(Separatore_Centrale)
    #Separatore_Centrale = TEXTURE('\windows\system32\Github\Legno.jpg')(Separatore_Centrale)
    Separatore_Orizzontale = CYLINDER([0.05,2])(25)
    Separatore_Orizzontale = COLOR([0.3,0.4,0.4])(Separatore_Orizzontale)
    #Separatore_Orizzontale = TEXTURE('\windows\system32\Github\Legno.jpg')(Separatore_Orizzontale)
    Separatore_Orizzontale = STRUCT(NN(5)([T(2)(0.4),Separatore_Orizzontale]))
    Separatore_Orizzontale = R([1,3])((3*PI)/2)(Separatore_Orizzontale)
    Separatore_Orizzontale = T(2)(-0.2)(Separatore_Orizzontale)
    #VIEW(STRUCT([Separatore_Centrale,Base_Finestra,Separatore_Orizzontale]))
    Base_Finestra = STRUCT([Separatore_Centrale,Base_Finestra,Separatore_Orizzontale])
    #VIEW(Base_Finestra)
    #VIEW(STRUCT([Base_Finestra,window]))
    Finestra_Completa = STRUCT([Base_Finestra,window])
    #VIEW(STRUCT([Colonna_Laterale,Finestra_Completa]))
    return Finestra_Completa
    


#finestra laterale posteriore formato con hex_material per il vetro



def finestra_posteriore() :
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
    window = CUBOID([1.5,4.8,0.01])
    window = hex_material("#ffffff", "#ffffff",0.6)(window)
    #VIEW(window)
    Finestra = CUBOID([1.5,5,0.1])
    Fin = CUBOID([1.3,4.5,0.5])
    Fin = T([1,2])([0.1,0.3])(Fin)
    Base_Finestra = DIFFERENCE([Finestra,Fin])
    Base_Finestra = TEXTURE('\windows\system32\Github\Font_Pareti.jpg')(Base_Finestra)
    #VIEW(Base_Finestra)
    Fin2 = CUBOID([2,5.5,0.1])
    Fin2 = T([1,2])([-0.25,-0.15])(Fin2)
    Fin2 = DIFFERENCE([Fin2,Fin])
    Fin2 = T(3)(-0.11)(Fin2)
    Fin2 = TEXTURE('\windows\system32\Github\Font_Pareti_Ombreggiatura.jpg')(Fin2)
    Base_Finestra = STRUCT([Base_Finestra, Fin2])
    Separatore_Centrale = CUBOID([0.20,4.7,0.01])
    Separatore_Centrale = T([1,2])([0.68,0.2])(Separatore_Centrale)
    Separatore_Centrale = TEXTURE('\windows\system32\Github\Legno.jpg')(Separatore_Centrale)
    Separatore_Orizzontale = CUBOID([1.5,0.20,0.01])
    Separatore_Orizzontale = TEXTURE('\windows\system32\Github\Legno.jpg')(Separatore_Orizzontale)
    Separatore_Orizzontale = STRUCT(NN(5)([T(2)(0.85),Separatore_Orizzontale]))
    #VIEW(STRUCT([Separatore_Centrale,Base_Finestra,Separatore_Orizzontale]))
    Base_Finestra = STRUCT([Separatore_Centrale,Base_Finestra,Separatore_Orizzontale])
    #VIEW(Base_Finestra)

    #VIEW(STRUCT([Base_Finestra,window]))
    Finestra_Completa = STRUCT([Base_Finestra,window])
    return Finestra_Completa







#funzione globale per la creazione delle stanze della villa

def stanza(x,y,z):
    Stanza = CUBOID([x,y,z])
    Differenza_Stanza = CUBOID([x-1,y,z-1])
    Differenza_Stanza = T([1,3])([0.5,0.5])(Differenza_Stanza)
    Stanza_Completa = DIFFERENCE([Stanza,Differenza_Stanza])
    return Stanza_Completa

def scale_int(x,y,z):
    Scale = CUBOID([x,y,z])
    Scale = STRUCT(NN(9)([T([2,3])([0.4,0.5]),Scale]))
    return Scale
    
#funzione che mi permette di creare i fori per l'inserimento delle finestre.


def forofinestrelle_laterali(Struttura):
    Foro_Finestrelle = CUBOID([1.5,1.5,1.5])
    Foro_Finestrelle = T(2)(2)(Foro_Finestrelle)
    Foro_Finestrelle = STRUCT(NN(3)([T(3)(7.9),Foro_Finestrelle]))
    Foro_Finestrelle2 = T([2,3])([3,-2])(Foro_Finestrelle)
    Foro_Finestrelle3 = T([2,3])([6,3.5])(Foro_Finestrelle)
    Foro_Finestrelle = STRUCT([Foro_Finestrelle,Foro_Finestrelle2,Foro_Finestrelle3])
    #VIEW(DIFFERENCE([Costruzione,Foro_Finestrelle]))



    Foro_Finestrelle2 = R([1,3])(PI)(Foro_Finestrelle)
    Foro_Finestrelle2 = T([1,3])([-15.5,30])(Foro_Finestrelle2)
    Foro_Finestrelle3 = T(1)(40)(Foro_Finestrelle2)
    Foro_Finestrelle2 = STRUCT([Foro_Finestrelle2,Foro_Finestrelle3])
    Foro_Finestrelle2 = T(1)(16)(Foro_Finestrelle2)
    #Foro_Finestrelle2 = STRUCT([Struttura,Foro_Finestrelle2])
    Foro_Finestrelle2 = DIFFERENCE([Struttura,Foro_Finestrelle2])
    return Foro_Finestrelle2
#funzioni globali 

