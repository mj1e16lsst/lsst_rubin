import numpy as np

def findWeight(l,b,r):
    rogrim,rtgrim,rdgrim,rzgrim,rmgrim,gamma,Rc,q = 1.,1.9,3.5,0.41,6.5,1.8,2.8,0.6
    milkyWayRadius = 15.
    scaleHeight = 3.5
    bSphere = 7.669
    ebv=[]
    Rd = 3 

    radius = r * np.cos(np.deg2rad(b))
    thickness = r * np.sin(np.deg2rad(b))
                   
    xlen = (((radius*np.sin(np.deg2rad(l)))))
    ylen = ((radius*np.cos(np.deg2rad(l)))-8.364)
    dist = ((xlen**2)+(ylen**2))**0.5
    rad = ((dist**2)+(thickness**2))**0.5
    
    Bulge = (((((dist**2)+((thickness**2)/(q**2)))**0.5)/rogrim)**(-gamma))*np.exp(-(((dist**2)+((thickness**2)/(q**2)))/rtgrim**2))
    Disc = (np.exp((-rmgrim/rdgrim)-(dist/rdgrim)-(abs(thickness)/rzgrim)))
    Sphere = (np.exp(-bSphere*((rad/Rc)**0.25)))/((rad/Rc)**(7./8.))
    
    results = {}
    results[0] = [xlen,ylen,thickness]
    results[5] = [Bulge,Disc,Sphere]
    
    return results
