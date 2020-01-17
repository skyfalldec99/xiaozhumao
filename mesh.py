import meshio
import os 
import easygui as g
import numpy as np 
def gettxt():
    title = g.msgbox(msg="选择的存放节点和单元信息文件的文件夹为",title="hjx有限元程序",ok_button="OK")
    file_path1=g.diropenbox(default="*")
    print('选择的存放节点和单元信息文件的文件夹为：'+str(file_path1))    
    c=str(file_path1)+'\\eles7.txt'
    d=str(file_path1)+'\\nodes7.txt'
    title = g.msgbox(msg="请打开生成的.msh文件",title="hjx有限元程序",ok_button="OK")
    file_path2=g.fileopenbox(default=".msh")
    mesh = meshio.read(file_path2)
    points = mesh.points
    cells = mesh.cells
    point_data = mesh.point_data
    cell_data = mesh.cell_data
    # Element data
    eles = cells["triangle"]
    els_array = np.zeros([eles.shape[0], 6], dtype=int)
    els_array[:, 0] = range(eles.shape[0])
    els_array[:, 1] = 3
    els_array[:, 3::] = eles
    # Nodes
    nodes_array = np.zeros([points.shape[0], 5])
    nodes_array[:, 0] = range(points.shape[0])
    nodes_array[:, 1:3] = points[:, :2]
    # Create files
    np.savetxt(c, els_array, fmt="%d")
    np.savetxt(d, nodes_array,fmt=("%d", "%.4f", "%.4f", "%d", "%d"))
    return c,d
