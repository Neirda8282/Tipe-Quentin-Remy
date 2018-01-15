from math import pi
import pylab as pl
import numpy as np

D=0.031

Tm=[1.5+0.1*i for i in range (14)]       #Tours de manivelle par seconde

def Temps(d):
    t=[]
    for i in range(len(Tm)): 
        t.append((d/(D*pi))/Tm[i])
    return(t)
    
def Vitesse(d):
    V=[]
    temps=[]
    T=Temps(d)
    for i in range ((len(T))):
        temps.append(Temps(d[i]))
    for j in range (len(Tm)):
        V.append(d/temps[j])
    return(V)

def Couples(F,d):
    P=[]
    C=[]
    vitesse=[]
    V=Vitesse(d)
    for i in range (len(V)) :
        vitesse.append(Vitesse(d)[i])
    for k in range (len(Tm)):
        P.append(F*vitesse[k])
    for m in range(len(Tm)):
        C.append(P[m]/((Tm[m]*5.2)*(2*pi/360)))
    pl.plot(Tm, C,'b')
    pl.show()
    return()