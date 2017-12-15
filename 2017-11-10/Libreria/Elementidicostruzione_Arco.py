from larlib import *
from pyplasm import *

def ArchSurface(rr,w,h):
	Circle0 = lambda p : rr*cos(p[0])
	Circle00= lambda p : rr*sin(p[0])
	Circle1 = lambda p : (rr-w)*cos(p[0])
	Circle11 = lambda p : (rr-w)*sin(p[0])
	z = lambda p : h
	Circle0 = BEZIER(S1)([CONS([Circle0,Circle00,z])])
	Circle1 = BEZIER(S2)([CONS([Circle1,Circle11,z])])
	return BEZIER(S2)([Circle0,Circle1])
	
def Arch(length,w,depth,angle):
	radius = (length/2)/cos(angle/2)
	domain2D = PROD([T(1)(angle/2)(INTERVALS(PI-angle)(16)),QUOTE([1])])
	domain3D = PROD([domain2D,QUOTE([1])])
	ArchSurf2D0 = ArchSurface(radius,w,0)
	ArchSurf2D1 = ArchSurface(radius,w,depth)
    
	SolidMap = BEZIER(S3)([ArchSurf2D0,ArchSurf2D1])
	return MAP(SolidMap)(domain3D)