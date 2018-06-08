from larlib import *
from pyplasm import *
def bottomArv(d):
    return BEZIER(S1)([[0,0],[0,2*d/3],[d,2*d/3],[d,0]])

def topArc (d) :
    return BEZIER (S1)([[0,2*d/3],[d,2*d/3]])
def arc2D (d) :
    return BEZIER(S2)([bottomArv(d),topArc(d)])

def arc3D (d) :
    def arc3D1(w):
        return COMP([T(2)(w),R([2,3])(PI/2)])(PROD([MAP(arc2D(d))(PROD([INTERVALS(1)(8),INTERVALS(1)(1)])),QUOTE([w])]))
    return arc3D1
def Interarc (d1,d2):
    def Interarc1(w):
        return CUBOID([1,1,1])
    return Interarc1

def Xarc(d1,d2):
    def Xarc1(w):
        return RIGHT([RIGHT([Interarc(d1,d2)(w),arc3D(d2)(w)]),Interarc(d1,d2)(w)])
    return Xarc1

def CurvedArc():
    sx = (1/SizeArc)* arcAngle
    sz = sx * (r2-2)
    return COMP([cylMap,MKPOL,UKPOL,T(2)(r2 - 0.75),S([1,3])([sx,sz])])(TheArc)

def Column(argomenti):
    w,h = argomenti
    basis = CUBOID([w,w,w])
    trunk = CYLINDER ([w/2*0.85, 7])(8)
    capitel = CUBOID([w,w,w/2])
    return TOP([TOP([trunk,basis]),capitel])


def CourtWall1():
    w =0.7
    TripleHole = TOP([STRUCT([Column([w,2]),T(1)(2+w),Column([w,2])]),Xarc(2,2)(1)])
    #VIEW(TripleHole)

        #LeftWall = PROD([COMP([QUOTE,N(n1)])(d1/n1),CUBOID([1,h])])
        #RightWall = PROD([COMP([QUOTE,N(n2)])(d2/n2),CUBOID([1,h])])
        #return op([LeftWall,op([TripleHole,RightWall])])
        #return LeftWall OP TripleHole OP RightWall
    return TripleHole

def ColumnP(argomenti):
    w,h = argomenti
    basis = CUBOID([w,w,w/3])
    trunk = CYLINDER ([w/1.30, h - w])(5)
    capitel = CUBOID([w,w,w/3])
    return TOP([TOP([trunk,basis]),capitel])

