from feon. sa import * 
import numpy as np 
import meshio
import os 
import easygui
import easygui as g
import matplotlib.tri as tri 
import matplotlib.pyplot as plt 
from matplotlib.patches import Polygon 
from matplotlib.collections import PatchCollection 
from typein import typeinformation
def calcu(ns,es,x,y,E,nu,ty):
    nds=[]
    els=[]
    a=ty[0]
    b=ty[1]
    c=ty[2]
    d=ty[3]
    e=ty[4]
    f=ty[5]
    g=ty[6]
    print(len(c))
    a1=[]
    b1=[]
    c1=[]
    d1=[]
    e1=[]
    f1=[]
    g1=[]
    for i in range(len(a)):        
        if len(a)!=0:
            a1.append(int(a[i]))
    for i in range(len(b)):       
        if len(b)!=0:
            b1.append(int(b[i]))
    if len(c[0])!=0:
        for i in range(len(c)):         
            c1.append(int(c[i]))
    if len(d[0])!=0:
        for i in range(len(d)):        
            d1.append(int(d[i]))
    if len(e)!=0:
        for i in range(len(e)):
            e1.append(int(e[i]))
    for i in range(len(f)):
        
        if len(f)!=0:
            f1.append(float(f[i]))
    for i in range(len(g)):
        
        if len(g)!=0:
            g1.append(float(g[i]))
    for v,nd in enumerate(ns): 
        n=Node((x[v] ,y[v])) 
        nds.append(n) 
    for v, el in enumerate(es):
        i,j,k= int(el[3]),int(el[4]),int(el[5]) 
        n1,n2,n3 = nds[i],nds[j],nds[k]
        ee =Tri2D11S((n1,n2,n3),E,nu) 
        els.append(ee) 
    #建系统并将节点和单元加入到系统中
    s=System() 
    s.add_nodes(nds) 
    s.add_elements(els)
    nids =[nds[i].ID for i in a1]
    #施加边界条件
    nids1=[nds[i].ID for i in b1]
    nids2=[nds[i].ID for i in c1]
    nids3=[nds[i].ID for i in d1]
    nids4=[]
    s.add_fixed_sup(nids) 
    s.add_hinged_sup(nids1) 
    for nd in nids2:
        s.add_rolled_sup(nd,"x")
    for nd in nids3:
        s.add_rolled_sup(nd,"x")
    for i in range(len(e1)):
        nids4.append(nds[e1[i]].ID)
        s.add_node_force(nds[e1[i]].ID,Fx=f1[i]) 
        s.add_node_force(nds[e1[i]].ID,Fy=g1[i]) 
    #求解
    s.solve()
    return s
