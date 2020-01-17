import easygui as g
def getmaterial():
    msg = "材料信息"
    title = "hjx有限元程序"
    fieldNames = ["弹性模量","泊松比"]
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
                errmsg += ("" %fieldNames[i])
        if errmsg == "":
            break
        fieldValues = g.multenterbox(errmsg,title,fieldNames,fieldValues)
    print("输入如下所示:%s" %str(fieldValues))
    E=float(fieldValues[0])
    nu=float(fieldValues[1])
    return E,nu
