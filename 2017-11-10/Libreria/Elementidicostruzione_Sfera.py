from larlib import * 

def HalfSphere(r): 
    fx= lambda k : r*-(sin(k[1])*cos(k[0])) 
    fy= lambda k : r*cos(k[0])*cos(k[1])
    fz= lambda k : r*sin(k[0])
    return CONS([fx,fy,fz])


def Dome(n):
    def Dome1(length,w,angle):
        radius=length/(2*cos(angle))
        #celing=MIN(3)(Dome1(length,w,angle)) 
        Surf3D0=HalfSphere(radius) 
        Surf3D1=HalfSphere(radius-w)
        SolidMap= BEZIER(S3)([Surf3D0,Surf3D1])
        domain2D=PROD([COMP([T(1)(angle),INTERVALS(PI - angle)])(12),INTERVALS(2*PI)(n)])
        domain3D= PROD([domain2D,Q(1)])
        return COMP([T(3)(-3),MAP(SolidMap)])(domain3D) 
    return Dome1