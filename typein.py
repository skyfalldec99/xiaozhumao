import easygui as g
import numpy as np
def typeinformation():
    msg = "荷载和约束信息"
    title = "hjx有限元程序"
    fieldNames = ["固端支座节点坐标","铰支座节点坐标","x方向滑动支座","y方向滑动支座","施加荷载节点","x方向力","y方向作用力"]
    fieldValues = []
    fieldValues = g.multenterbox(msg,title,fieldNames)
    #print(fieldValues)
    c=[]
    while True:
        if fieldValues == None :
            break
        errmsg = ""
        for i in range(len(fieldNames)):
            option = fieldNames[i].strip()
            if fieldValues[i].strip() == "" and option[0] == "*":
                errmsg += ("【%s】为必填项   " %fieldNames[i])
        if errmsg == "":
            break
        fieldValues = g.multenterbox(errmsg,title,fieldNames,fieldValues)
    print("输入如下所示:%s" %str(fieldValues))
    for i in range(7):
        d=fieldValues[i]
        m=str(d)
        m=m.split(' ')
        c.append(m)
    len1=len(c[4])
    len2=len(c[5])
    len3=len(c[6])
    if (len1!=len2) or (len3!=len2) or (len1!=len3):
        print("输入荷载节点数量有误，请重新输入")
    return c
