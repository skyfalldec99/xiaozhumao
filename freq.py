from feon.sa import * 
from feon.tools import pair_wise 
import numpy as np
E = 210e6
G = 84e6
A =0.02
I = [5e-5,10e-5,20e-5]
dens =2
n0 =Node(0,0,0) 
n1 =Node(0,4,0) 
n2 =Node(4,4,0)
n3 =Node(0,4,0)
n4 =Node(0,0,5)
n5 =Node(0,4,5)
n6 =Node(4,4,5)
n7 =Node(0,4,5)
n8 =Node(1,0,5) 
n9 =Node(3,0,5)  
nds1=[n0,n3,n2,n1]  
nds2=[n4,n7,n6,n5]
nds3=[n4,n8,n9,n7,n6,n5 ] 
els=[]
for nd in pair_wise(nds3,True):
    els.append(Beam3D11(nd, E, G, A, I, dens))
for i in range(4):
    els.append(Beam3D11((nds1[i],nds2[i]),E,G,A,I,dens))
s= System()
s.add_nodes(nds1, nds3)
s.add_elements(els)
s.add_fixed_sup([nd.ID for nd in nds1])
#求解函数的参数改为自定义函数名
s.solve(model = "dynamic_eigen_model")
print(s.freq)