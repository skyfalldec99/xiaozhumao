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
def showpic(s):
    nx = [nd.x for nd in s.get_nodes()] 
    ny =[nd.y for nd in s.get_nodes()]
#获取节点 ID
    nID = [[nd. ID for nd in el] for el in s. get_elements()]
    tr = tri. Triangulation(nx,ny,nID)
    #取节点位移
    ux = [nd.disp["Ux"]for nd in s.get_nodes()]
    uy = [nd.disp["Uy"]for nd in s.get_nodes()]
    #获取单元应力 
    sx=np.array([el.stress["sx"][0][0] for el in s.get_elements()])
    sy=np.array([el.stress["sy"][0][0] for el in s.get_elements()]) 
    sxy=np.array([el.stress["sxy"][0][0] for el in s.get_elements()])
    #建图 1 、2
    figl,fig2 =plt.figure(),plt.figure()
    #建坐标轴 1 、2
    ax1,ax2 = figl.add_subplot(111) ,fig2.add_subplot(111)
    #图 1 中绘制位移云图
    ncb=ax1.tricontourf(tr,ux,cmap="jet" )
    figl.colorbar(ncb) 
    #在图2中绘制应力云图
    patches= [] 
    for el in s.get_elements():
        ex,ey=[ ],[ ]
        for nd in el.nodes: 
            ex.append(nd.x) 
            ey.append(nd.y)
        zipped=zip(ex,ey)
        d=list(zipped)
        polygon=Polygon(d,True) 
        patches.append(polygon) 
    pc=PatchCollection(patches, edgecolor = "w", alpha =0.4) 
    pc.set_array(sx) 
    ax2.add_collection(pc)
    ax2.set_aspect("equal")
    fig2.colorbar(pc) 
    #显示绘图
    plt.show() 
    return