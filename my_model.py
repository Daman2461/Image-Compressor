import numpy as np
import random





def closest(X,cen):
    clo=np.zeros(X.shape[0], dtype=int)
    for i in range(X.shape[0]):
        m=[]
        for j in range(cen.shape[0]):
            m.append(np.sum((X[i]-cen[j])**2))
        m=np.array(m)
        clo[i]=m.argmin()
    return clo


def recompute_cen(x,cen,clo):
    for i in range(cen.shape[0]):
        p=x[i==clo]
        if(p.shape[0]>0):
            cen[i]=np.sum(p,axis=0)/p.shape[0]
    return cen



def compress(im,n=20,iterations=10,ok=0):

    a = np.asarray(im)
    
    
    a=a/255.0
    
    original=a.shape
    
    if len(a.shape) < 3 or a.shape[2] <= 3:
        return None, False  # Return None and False to indicate failure
        
    x  =np.reshape(a, (a.shape[0] * a.shape[1], 3))
    
    cen=[]
    
    ok=1
    for i in range(n):
        r=random.randint(0,x.shape[0])
        cen.append(x[r])
        
    
    cen=np.array(cen)
    
    
    for i in range(iterations):
        clo=closest(x,cen);
        cen=recompute_cen(x, cen, clo)
        print('Iteration '+str(i))
    
    x_compressed = cen[clo]
    x_compressed = x_compressed.reshape( original)
    
   
    
    
    x_compressed = (x_compressed * 255).astype(np.uint8)
    
   
    return x_compressed,ok


