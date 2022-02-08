#字典创建
OCdict1={}
OCdict2={}
OCdict3={}
OCdict4={}
MCdict1={}
MCdict2={}
MCdict3={}
MCdict4={}
MCdict5={}
MCdict6={}
Zihdict={}
zvh=[]
import xlrd#引用xlrd库读入表格数据
xl=xlrd.open_workbook(r'《廣韻》形聲表1.2.xlsx')
table=xl.sheets()[1]
for i in range(1,8600):
    j=table.cell(i,11).value
    a=table.cell(i,0).value
    b=table.cell(i,1).value
    c=table.cell(i,2).value
    d=table.cell(i,4).value
    e=table.cell(i,5).value
    f=table.cell(i,6).value
    g=table.cell(i,7).value
    h=table.cell(i,8).value
    m=table.cell(i,9).value
    n=table.cell(i,10).value
    if a!='':
        for u in j:
            zvh.append(u)
            if u!='<' and u!='>':
                OCdict1[u]=a
    if b!='':
        for u in j:
            if u!='<' and u!='>':
                OCdict2[u]=b
    if c!='':
        for u in j:
            if u!='<' and u!='>':
                OCdict3[u]=c
    if d!='':
        for u in j:
            if u!='<' and u!='>':
                OCdict4[u]=d
    if e!='':
        for u in j:
            if u!='<' and u!='>':
                MCdict1[u]=e
    if f!='':
        for u in j:
            if u!='<' and u!='>':
                MCdict2[u]=f
    if g!='':
        for u in j:
            if u!='<' and u!='>':
                MCdict3[u]=g
    if h!='':
        for u in j:
            if u!='<' and u!='>':
                MCdict4[u]=h
    if m!='':
        for u in j:
            if u!='<' and u!='>':
                MCdict5[u]=m
    if n!='':
        for u in j:
            if u!='<' and u!='>':
                MCdict6[u]=n
#功能搭建-简繁转化
def conv(x):
    from zhconv import convert#引用zhconv库
    y=convert(x,'zh-tw')
    return y
#功能搭建-字典查询
def sak_1(x,dic):
    y='%s' %(dic.get(x))
    return y
def sak_2(t,dic):
    import re#将文段分离成单个汉字
    t=re.findall(r'.{1}',t)
    t=' '.join(t)
    u=''
    for i in t:#逐个在字典中查询
        if i in dic:
            u+='%s' %(dic.get(i))
        else:
            u+=i
    return u
def zraa_swin():
    x=ent_11.get()
    p=0
    q=0
    z=''
    tex_11.delete('1.0','end')
    if c1.get()==True:
        x=conv(x)
    if x == '“作者？”':
        tex_11.insert(INSERT,'惟澄爲之。')
        tex_11.insert(END,'')
    else:
        for y in x:
            if y not in zvh:
                p+=1
                q+=1
            elif y not in z and y in zvh:
                a=sak_1(y,OCdict1)
                b=sak_1(y,OCdict2)
                c=sak_1(y,OCdict3)
                d=sak_1(y,OCdict4)
                e=sak_1(y,MCdict1)
                f=sak_1(y,MCdict2)
                g=sak_1(y,MCdict3)
                h=sak_1(y,MCdict4)
                m=sak_1(y,MCdict5)
                n=sak_1(y,MCdict6)
                z=sak_1(y,Zihdict)

                t1='“'+y+'” \n'
                z1='【自定義】'+z+'\n'
                t2='【上古】 \n'
                t3='  【聲符】'+a+' \n'
                t4='  【諧聲域】'+b+' \n'
                t5='  【音節類型】'+c+'類 \n'
                t6='  【擬音】'+d+' \n'
                t7='【中古】 \n'
                t8='  【聲母】'+e+' \n'
                t9='  【等】'+f+'等 \n'
                t10='  【開合】'+g+' \n'
                t11='  【韵母】'+h+' \n'
                t12='  【聲調】'+m+' \n'
                t13='  【切語】'+n+' \n'

                tex_11.insert(INSERT,t1)
                if c5.get()==True:
                    tex_11.insert(INSERT,z1)
                if c6.get()==True:
                    tex_11.insert(INSERT,t2)
                    tex_11.insert(INSERT,t3)
                    tex_11.insert(INSERT,t4)
                    tex_11.insert(INSERT,t5)
                    tex_11.insert(INSERT,t6)
                if c7.get()==True:
                    tex_11.insert(INSERT,t7)
                    tex_11.insert(INSERT,t8)
                    tex_11.insert(INSERT,t9)
                    tex_11.insert(INSERT,t10)
                    tex_11.insert(INSERT,t11)
                    tex_11.insert(INSERT,t12)
                    tex_11.insert(END,t13)
                z+=y
                q+=1
                
        if p==q and q!=0:
            tex_11.insert(INSERT,'未找到符合條件的漢字')
            tex_11.insert(END,'')

def tronq_waanh1():
    tex_22.delete('1.0','end')
    t_nup=tex_21.get('1.0','end')
    if c2.get()==True:
        t_nup=conv(t_nup)
    if r.get()==1:
        t_khlut=sak_2(t_nup,OCdict4)
    elif r.get()==2:
        t_khlut=sak_2(t_nup,Zihdict)
    tex_22.insert(END,t_khlut)

def tronq_waanh2():
    #SaveFile_1()
    fileSave=SaveFile_1()
    tex_31.delete('1.0','end')
    name=ent_31.get()
    if c32.get()==True and name !='':
        import requests#引用requests库
        from bs4 import BeautifulSoup#引用BeautifulSoup4库
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36'}
        url = "https://so.gushiwen.cn/search.aspx?value={}".format(name)
        req = requests.get(url,headers=headers)
        soup = BeautifulSoup(req.text,'lxml')
        url = "https://so.gushiwen.cn"+soup.select("body>div>div>div>div>p>a")[0].get("href")
        req = requests.get(url,headers=headers)
        soup = BeautifulSoup(req.text,'lxml')
        contents = soup.find("div",class_="contson").find_all("p")
        if not bool(contents):
            contents = soup.find("div",class_="contson")
        text = name+"\n"+soup.find("p",class_="source").text.replace("\n","")+"\n"
        for i in contents:
            text = text+str(i).replace("<br/>","\n").replace("<p>","").replace("</p>","\n")
        with open(fileSave,'w',encoding='utf-8') as fp:#创建写入下载结果的文件
            fp.write(text)
        
        fo1=open(fileSave,'r',encoding='utf-8')#打开写入下载结果的文件
        fo2=open(fileSave[:-4]+'1.txt','w',encoding='utf-8')#创建写入转换结果的文件
        for x in fo1:#同上例
            x=conv(x)
            if r.get()==1:
                y=sak_2(x,OCdict4)
            elif r.get()==2:
                y=sak_2(x,Zihdict)
            y+='\n'
            tex_31.insert(INSERT,y)
            fo2.writelines(y)
        fo1.close()
        fo2.close()
        print('转换成功')

    elif name != '':
        fo1=open(name,'r',encoding='utf-8')#打开写入下载结果的文件
        fo2=open(fileSave,'w',encoding='utf-8')#创建写入转换结果的文件
        for x in fo1:
            if c31.get()==True:
                x=conv(x)
            if r.get()==1:
                y=sak_2(x,OCdict4)
            elif r.get()==2:
                y=sak_2(x,Zihdict)
            y+='\n'
            tex_31.insert(INSERT,y)
            fo2.writelines(y)
        fo1.close()
        fo2.close()
        print('转换成功')

def lhvmq_lot():
    import collections
    tex_41.delete('1.0','end')
    ent_42.delete(0,END)
    ent_43.delete(0,END)
    name=ent_41.get()
    if name != '':
        f=open(name,'r',encoding='utf-8')
        txt1 = f.read()
        txt2=''
        if c4.get()==True:
            txt1=conv(txt1)
        l=[]
        n=0
        m=0
        a=0
        for i in txt1:
            if i in OCdict3:
                txt2+=i
                n+=1
                if sak_1(i,OCdict3)=='A':
                    a+=1
                if i not in l:
                    m+=1
                    l.append(i)
                
        a=(a/n)*100
        A='{:.2f}'.format(a)
        ent_42.insert(INSERT,str(n))
        ent_43.insert(INSERT,str(A)+'%')
        mylist = list(txt2)
        mycount = collections.Counter(mylist)
        for key, val in mycount.most_common(m):  # 有序（返回前m个）
            #print(key, val)
            for k in key:
                if r.get()==1:
                    y=sak_2(k,OCdict4)
                if r.get()==2:
                    y=sak_2(k,Zihdict)
                k=str(val)+' '+k+' '+y+'\n'
                tex_41.insert(INSERT,k)
        
def lhiim_kraaj():
    global lab_53
    name=ent_51.get()
    if name !='':
        fo=open(name,'r',encoding='utf-8')
        for i in fo:
            ls=i.split()
            if len(ls)>=2:
                a=ls[0]
                b=ls[1]
                Zihdict[a]=b
        lab_53.destroy()
        lab_53=Label(top,text=' 自定義方案已添加成功，可更改設置！    ')
        lab_53.config(font=('宋体',14))
        lab_53.grid(row=5,column=5,rowspan=1,columnspan=16)

        
#界面设计
from tkinter import *#引用tkinter库
from tkinter import filedialog
from PIL import Image,ImageTk,Image#引用pillow库

top=Tk()
top.title('古典漢語轉換器1.1')
top.geometry('800x500')

def getLocalFile_1():

    ent_31.delete(0,END)
    
    top0=Toplevel()
    top0.withdraw()

    filePath=filedialog.askopenfilename()

    #print('文件路径：',filePath)
    ent_31.insert(INSERT,filePath)
    return filePath

def getLocalFile_2():

    ent_41.delete(0,END)
    
    top0=Toplevel()
    top0.withdraw()

    filePath=filedialog.askopenfilename()

    #print('文件路径：',filePath)
    ent_41.insert(INSERT,filePath)
    return filePath

def getLocalFile_3():

    ent_51.delete(0,END)
    
    top0=Toplevel()
    top0.withdraw()

    filePath=filedialog.askopenfilename()

    #print('文件路径：',filePath)
    ent_51.insert(INSERT,filePath)
    return filePath

def SaveFile_1():

    top0=Toplevel()
    top0.withdraw()

    fileSave=filedialog.asksaveasfilename(defaultextension='.txt',filetypes=[('文本文档','.txt')])
    return fileSave
    
canvas_1=Canvas(top,width=200,height=600)
im=Image.open('bg.gif').resize((600,900))
ir=ImageTk.PhotoImage(im)
canvas_1.create_image(300,400,image=ir)
canvas_1.grid(row=0,column=0,rowspan=36,columnspan=3)

num=0

lab_01=Label(top,text='古典漢語轉換器')
lab_01.config(font=('隶书',36))
lab_01.grid(row=6,column=4,rowspan=1,columnspan=6)

lab_02=Label(top,text='ka̠ʔ tə̠nʔ n̥ans ŋaʔ tɹonʔ wa̠ns kʰɹəts')
lab_02.config(font=('隶书',22))
lab_02.grid(row=7,column=4,rowspan=1,columnspan=8)

'''lab_03=Label(top,text='  製作：惟澄')
lab_03.config(font=('隶书',16))
lab_03.grid(row=14,column=4,rowspan=1,columnspan=2)'''

def qui(self):
    self.grid_forget()

def qui_0():
    qui(lab_01)
    qui(lab_02)

def qui_1():
    but_01=Button(top,text='字 典',bg='#86775f',fg='white',bd=1,command=zvh_tvvnq)
    but_01.config(font=('隶书',12))
    but_01.grid()
    geenh(but_01,110,120,80,30)
    qui(lab_11)
    qui(ent_11)
    qui(but_11)
    qui(che_11)
    qui(tex_11)
    qui(scr_11)

def qui_2():
    but_02=Button(top,text=' 轉 換 ',bg='#86775f',fg='white',bd=1,command=tronq_waanh)
    but_02.config(font=('隶书',12))
    but_02.grid()
    geenh(but_02,110,180,80,30)
    qui(lab_21)
    qui(tex_21)
    qui(scr_21)
    qui(che_21)
    qui(but_21)
    qui(tex_22)
    qui(scr_22)

def qui_3():
    but_03=Button(top,text=' 文檔轉換 ',bg='#86775f',fg='white',bd=1,command=mvn_taang_tronq_waanh)
    but_03.config(font=('隶书',12))
    but_03.grid()
    geenh(but_03,110,240,80,30)
    qui(lab_31)
    qui(ent_31)
    qui(but_31)
    qui(but_32)
    qui(che_31)
    qui(che_32)
    qui(tex_31)
    qui(scr_31)

def qui_4():
    but_04=Button(top,text=' 文檔審閲 ',bg='#86775f',fg='white',bd=1,command=mvn_taang_lhvmq_lot)
    but_04.config(font=('隶书',12)) 
    but_04.grid()
    geenh(but_04,110,300,80,30)
    qui(lab_41)
    qui(ent_41)
    qui(but_41)
    qui(but_42)
    qui(che_41)
    qui(lab_42)
    qui(tex_41)
    qui(scr_41)
    qui(lab_43)
    qui(ent_42)
    qui(lab_44)
    qui(ent_43)
    

def qui_5():
    but_05=Button(top,text=' 設 置 ',bg='#86775f',fg='white',bd=1,command=nghet_trvs)
    but_05.config(font=('隶书',12)) 
    but_05.grid()
    geenh(but_05,110,420,80,30)
    qui(lab_51)
    qui(lab_52)
    qui(ent_51)
    qui(but_51)
    qui(but_52)
    qui(lab_53)
    qui(lab_54)
    qui(che_51)
    qui(che_52)
    qui(che_53)
    qui(lab_55)
    qui(che_54)
    qui(che_55)

def geenh(n,x,y,w,h):#在背景图片上留出窗口
    canvas_1.create_window(x,y,width=w,height=h,window=n)

def zvh_tvvnq():

    global num

    if num==0:
        qui_0()
    elif num==2:
        qui_2()
    elif num==3:
        qui_3()
    elif num==4:
        qui_4()
    elif num==5:
        qui_5()

    num=1
    
    but_01=Button(top,text='字 典',bg='brown',fg='white',bd=1,command=zvh_tvvnq)
    but_01.config(font=('隶书',12))
    but_01.grid()
    geenh(but_01,110,120,80,30)

    lab_11.grid(row=2,column=4,rowspan=1,columnspan=2)

    ent_11.grid(row=3,column=4,rowspan=1,columnspan=24)

    che_11.grid(row=4,column=3,rowspan=1,columnspan=10)

    scr_11.grid(row=5,column=32,rowspan=20,columnspan=2,pady=5,ipady=120)
    tex_11.grid(row=5,column=4,rowspan=20,columnspan=28)

    but_11.grid(row=3,column=28,rowspan=1,columnspan=4)


def tronq_waanh():

    global num

    if num==0:
        qui_0()
    elif num==1:
        qui_1()
    elif num==3:
        qui_3()
    elif num==4:
        qui_4()
    elif num==5:
        qui_5()

    num=2
    
    but_02=Button(top,text=' 轉 換 ',bg='brown',fg='white',bd=1,command=tronq_waanh)
    but_02.config(font=('隶书',12))
    but_02.grid()
    geenh(but_02,110,180,80,30)

    lab_21.grid(row=1,column=4,rowspan=1,columnspan=2)

    scr_21.grid(row=2,column=45,rowspan=6,columnspan=2,pady=5,ipady=30)
    tex_21.grid(row=2,column=4,rowspan=6,columnspan=40)

    che_21.grid(row=8,column=3,rowspan=1,columnspan=10)

    but_21.grid(row=8,column=30,rowspan=1,columnspan=10)

    scr_22.grid(row=9,column=45,rowspan=12,columnspan=2,pady=5,ipady=100)
    tex_22.grid(row=9,column=4,rowspan=12,columnspan=40)

def mvn_taang_tronq_waanh():

    global num

    if num==0:
        qui_0()
    elif num==1:
        qui_1()
    elif num==2:
        qui_2()
    elif num==4:
        qui_4()
    elif num==5:
        qui_5()

    num=3
    
    but_03=Button(top,text=' 文檔轉換 ',bg='brown',fg='white',bd=1,command=mvn_taang_tronq_waanh)
    but_03.config(font=('隶书',12)) 
    but_03.grid()
    geenh(but_03,110,240,80,30)

    lab_31.grid(row=2,column=4,rowspan=1,columnspan=6)

    ent_31.grid(row=3,column=4,rowspan=1,columnspan=20)

    but_31.grid(row=3,column=23,rowspan=1,columnspan=8)

    but_32.grid(row=3,column=31,rowspan=1,columnspan=8)

    che_31.grid(row=4,column=3,rowspan=1,columnspan=10)

    che_32.grid(row=5,column=3,rowspan=1,columnspan=8)

    scr_31.grid(row=6,column=36,rowspan=18,columnspan=2,ipady=100)
    tex_31.grid(row=6,column=4,rowspan=18,columnspan=28,pady=5)

def mvn_taang_lhvmq_lot():

    global num

    if num==0:
        qui_0()
    elif num==1:
        qui_1()
    elif num==2:
        qui_2()
    elif num==3:
        qui_3()
    elif num==5:
        qui_5()

    num=4
    
    but_04=Button(top,text=' 文檔審閲 ',bg='brown',fg='white',bd=1,command=mvn_taang_lhvmq_lot)
    but_04.config(font=('隶书',12)) 
    but_04.grid()
    geenh(but_04,110,300,80,30)

    lab_41.grid(row=2,column=4,rowspan=1,columnspan=6)

    ent_41.grid(row=3,column=4,rowspan=1,columnspan=20)

    but_41.grid(row=3,column=24,rowspan=1,columnspan=8)

    but_42.grid(row=3,column=32,rowspan=1,columnspan=8)

    che_41.grid(row=4,column=3,rowspan=1,columnspan=8)

    lab_42.grid(row=5,column=3,rowspan=1,columnspan=2)

    scr_41.grid(row=6,column=6,rowspan=18,columnspan=2,pady=5,ipady=100)
    tex_41.grid(row=6,column=3,rowspan=18,columnspan=4)

    lab_43.grid(row=6,column=8,rowspan=1,columnspan=2)
    ent_42.grid(row=6,column=10,rowspan=1,columnspan=2)

    lab_44.grid(row=7,column=8,rowspan=1,columnspan=2)
    ent_43.grid(row=7,column=10,rowspan=1,columnspan=2)

def nghet_trvs():
    
    global num

    if num==0:
        qui_0()
    elif num==1:
        qui_1()
    elif num==2:
        qui_2()
    elif num==3:
        qui_3()
    elif num==4:
        qui_4()

    num=5
    
    but_05=Button(top,text=' 設 置 ',bg='brown',fg='white',bd=1,command=nghet_trvs)
    but_05.config(font=('隶书',12)) 
    but_05.grid()
    geenh(but_05,110,420,80,30)

    lab_51.grid(row=2,column=4,rowspan=1,columnspan=6)

    lab_52.grid(row=3,column=4,rowspan=1,columnspan=4)

    ent_51.grid(row=4,column=4,rowspan=1,columnspan=20)

    but_51.grid(row=4,column=24,rowspan=1,columnspan=8)

    but_52.grid(row=4,column=32,rowspan=1,columnspan=8)

    lab_53.grid(row=5,column=5,rowspan=1,columnspan=16)

    lab_54.grid(row=6,column=3,rowspan=1,columnspan=4)

    che_51.grid(row=7,column=3,rowspan=1,columnspan=6)

    che_52.grid(row=8,column=3,rowspan=1,columnspan=4)

    che_53.grid(row=8,column=7,rowspan=1,columnspan=4)

    lab_55.grid(row=9,column=3,rowspan=1,columnspan=4)

    che_54.grid(row=10,column=3,rowspan=1,columnspan=8)

    che_55.grid(row=11,column=3,rowspan=1,columnspan=6)

    
#菜单
but_1=Button(top,text='字 典',bg='#86775f',fg='white',bd=1,command=zvh_tvvnq)
but_1.config(font=('隶书',12))                     
but_1.grid()
geenh(but_1,110,120,80,30)

but_2=Button(top,text=' 轉 換 ',bg='#86775f',fg='white',bd=1,command=tronq_waanh)
but_2.config(font=('隶书',12)) 
but_2.grid()
geenh(but_2,110,180,80,30)

but_3=Button(top,text=' 文檔轉換 ',bg='#86775f',fg='white',bd=1,command=mvn_taang_tronq_waanh)
but_3.config(font=('隶书',12)) 
but_3.grid()
geenh(but_3,110,240,80,30)

but_4=Button(top,text=' 文檔審閱 ',bg='#86775f',fg='white',bd=1,command=mvn_taang_lhvmq_lot)
but_4.config(font=('隶书',12)) 
but_4.grid()
geenh(but_4,110,300,80,30)

but_5=Button(top,text=' 設 置 ',bg='#86775f',fg='white',bd=1,command=nghet_trvs)
but_5.config(font=('隶书',12)) 
but_5.grid()
geenh(but_5,110,420,80,30)

#字典
lab_11=Label(top,text=' 字典 dzəs_tə̠nʔ')
lab_11.config(font=('宋体',16))

ent_11=Entry(top,width=40,textvariable='x')
ent_11.config(font=('宋体',16))

but_11=Button(top,text='查 詢',bg='#86775f',fg='white',bd=1,command=zraa_swin)
but_11.config(font=('隶书',12))

c1=BooleanVar()
che_11=Checkbutton(top,text='啟用簡繁轉換(如能輸入繁体字則不建議啟用)',variable=c1)
che_11.config(font=('宋体',12))

tex_11=Text(top,height=14,width=45)
tex_11.config(font=('宋体',16))
scr_11=Scrollbar(top)
scr_11.config(command=tex_11.yview)
tex_11.config(yscrollcommand=scr_11.set)

#转换
lab_21=Label(top,text=' 轉換 tɹonʔ wa̠ns')
lab_21.config(font=('宋体',16))

tex_21=Text(top,height=5,width=50)
tex_21.config(font=('宋体',16))
scr_21=Scrollbar(top)
scr_21.config(command=tex_21.yview)
tex_21.config(yscrollcommand=scr_21.set)

c2=BooleanVar()
che_21=Checkbutton(top,text='啟用簡繁轉換(如能輸入繁体字則不建議啟用)',variable=c2)
che_21.config(font=('宋体',12))

but_21=Button(top,text='轉 換',bg='#86775f',fg='white',bd=1,command=tronq_waanh1)
but_21.config(font=('隶书',12))

tex_22=Text(top,height=14,width=50)
tex_22.config(font=('宋体',16))
scr_22=Scrollbar(top)
scr_22.config(command=tex_22.yview)
tex_22.config(yscrollcommand=scr_22.set)

#文档转换
lab_31=Label(top,text=' 文檔轉換 mən ta̠ŋ tɹonʔ wa̠ns')
lab_31.config(font=('宋体',16))

ent_31=Entry(top,width=45,textvariable='n1')
ent_31.config(font=('宋体',14))

but_31=Button(top,text='瀏 覽',bg='#86775f',fg='white',bd=1,command=getLocalFile_1)
but_31.config(font=('隶书',11))

but_32=Button(top,text='轉 換',bg='#86775f',fg='white',bd=1,command=tronq_waanh2)
but_32.config(font=('隶书',11))

c31=BooleanVar()
che_31=Checkbutton(top,text='啟用簡繁轉換(如能輸入繁体字則不建議啟用)',variable=c31)
che_31.config(font=('宋体',12))

c32=BooleanVar()
che_32=Checkbutton(top,text='輸入篇名並在古詩文網下載(須接入互联網)',variable=c32)
che_32.config(font=('宋体',12))

tex_31=Text(top,height=12,width=48)
tex_31.config(font=('宋体',16))
scr_31=Scrollbar(top)
scr_31.config(command=tex_31.yview)
tex_31.config(yscrollcommand=scr_31.set)

#文档审阅
lab_41=Label(top,text='文檔審閱 mən ta̠ŋ l̥əmʔ lot')
lab_41.config(font=('宋体',16))

ent_41=Entry(top,width=45,textvariable='n2')
ent_41.config(font=('宋体',14))

but_41=Button(top,text='瀏 覽',bg='#86775f',fg='white',bd=1,command=getLocalFile_2)
but_41.config(font=('隶书',11))

but_42=Button(top,text='審 閱',bg='#86775f',fg='white',bd=1,command=lhvmq_lot)
but_42.config(font=('隶书',11))

c4=BooleanVar()
che_41=Checkbutton(top,text='啟用簡繁轉換(如能輸入繁体字則不建議啟用)',variable=c4)
che_41.config(font=('宋体',12))

lab_42=Label(top,text='字頻統計 ')
lab_42.config(font=('宋体',14))

tex_41=Text(top,height=12,width=14)
tex_41.config(font=('宋体',16))
scr_41=Scrollbar(top)
scr_41.config(command=tex_41.yview)
tex_41.config(yscrollcommand=scr_41.set)

lab_43=Label(top,text='漢字總數')
lab_43.config(font=('宋体',14))

ent_42=Entry(top,width=10,textvariable='n3')
ent_42.config(font=('宋体',14))

lab_44=Label(top,text='A 類佔比')
lab_44.config(font=('宋体',14))

ent_43=Entry(top,width=10,textvariable='n4')
ent_43.config(font=('宋体',14))

#设置
lab_51=Label(top,text=' 設置 ŋ̊et tɹəks ')
lab_51.config(font=('宋体',16))

lab_52=Label(top,text='一、自定义方案')
lab_52.config(font=('宋体',14))

ent_51=Entry(top,width=45,textvariable='n5')
ent_51.config(font=('宋体',14))

but_51=Button(top,text='瀏 覽',bg='#86775f',fg='white',bd=1,command=getLocalFile_3)
but_51.config(font=('隶书',11))

but_52=Button(top,text='添 加',bg='#86775f',fg='white',bd=1,command=lhiim_kraaj)
but_52.config(font=('隶书',11))

lab_53=Label(top,text='說明：請將方案製成.txt文件,每行格式如：一  qik')
lab_53.config(font=('宋体',14))

lab_54=Label(top,text='二、 字典設置')
lab_54.config(font=('宋体',14))

c5=BooleanVar()
che_51=Checkbutton(top,text='显示自定義方案',variable=c5)
che_51.config(font=('宋体',14))

c6=BooleanVar()
che_52=Checkbutton(top,text='显示上古',variable=c6)
che_52.config(font=('宋体',14))
che_52.select()

c7=BooleanVar()
che_53=Checkbutton(top,text='显示中古',variable=c7)
che_53.config(font=('宋体',14))
che_53.select()

lab_55=Label(top,text='二、 轉換設置')
lab_55.config(font=('宋体',14))

'''c8=BooleanVar()
che_54=Checkbutton(top,text='使用默認上古漢語擬音',variable=c8)
che_54.config(font=('宋体',14))
che_54.select()
    

c9=BooleanVar()
che_55=Checkbutton(top,text='使用自定義方案',variable=c9)
che_55.config(font=('宋体',14))'''

r=IntVar()
che_54=Radiobutton(top,text='使用默認上古漢語擬音',value=1,variable=r)
che_54.config(font=('宋体',14))
che_54.select()
che_55=Radiobutton(top,text='使用自定義方案',value=2,variable=r)
che_55.config(font=('宋体',14))


#11
def callback1_11(event=None):
    global top
    ent_11.event_generate('<<Cut>>')
    
def callback2_11(event=None):
    global top
    ent_11.event_generate('<<Copy>>')
    
def callback3_11(event=None):
    global top
    ent_11.event_generate('<<Paste>>')
    
'''创建一个弹出菜单'''
menu_11 = Menu(top,
            tearoff=False,
            #bg="black",
            )
menu_11.add_command(label="剪切", command=callback1_11)
menu_11.add_command(label="复制", command=callback2_11)
menu_11.add_command(label="粘贴", command=callback3_11)

def popup(event):
    menu_11.post(event.x_root, event.y_root)   # post在指定的位置显示弹出菜单
ent_11.bind("<Button-3>", popup)   # 绑定鼠标右键,执行popup函数

#12
def callback1_12(event=None):
    global top
    tex_11.event_generate('<<Cut>>')
    
def callback2_12(event=None):
    global top
    tex_11.event_generate('<<Copy>>')
    
def callback3_12(event=None):
    global top
    tex_11.event_generate('<<Paste>>')
    
'''创建一个弹出菜单'''
menu_12 = Menu(top,
            tearoff=False,
            #bg="black",
            )
menu_12.add_command(label="剪切", command=callback1_12)
menu_12.add_command(label="复制", command=callback2_12)
menu_12.add_command(label="粘贴", command=callback3_12)

def popup(event):
    menu_12.post(event.x_root, event.y_root)   # post在指定的位置显示弹出菜单
tex_11.bind("<Button-3>", popup)   # 绑定鼠标右键,执行popup函数

#21
def callback1_21(event=None):
    global top
    tex_21.event_generate('<<Cut>>')
    
def callback2_21(event=None):
    global top
    tex_21.event_generate('<<Copy>>')
    
def callback3_21(event=None):
    global top
    tex_21.event_generate('<<Paste>>')
    
'''创建一个弹出菜单'''
menu_21 = Menu(top,
            tearoff=False,
            #bg="black",
            )
menu_21.add_command(label="剪切", command=callback1_21)
menu_21.add_command(label="复制", command=callback2_21)
menu_21.add_command(label="粘贴", command=callback3_21)

def popup(event):
    menu_21.post(event.x_root, event.y_root)   # post在指定的位置显示弹出菜单
tex_21.bind("<Button-3>", popup)   # 绑定鼠标右键,执行popup函数

#22
def callback1_22(event=None):
    global top
    tex_22.event_generate('<<Cut>>')
    
def callback2_22(event=None):
    global top
    tex_22.event_generate('<<Copy>>')
    
def callback3_22(event=None):
    global top
    tex_22.event_generate('<<Paste>>')
    
'''创建一个弹出菜单'''
menu_22 = Menu(top,
            tearoff=False,
            #bg="black",
            )
menu_22.add_command(label="剪切", command=callback1_22)
menu_22.add_command(label="复制", command=callback2_22)
menu_22.add_command(label="粘贴", command=callback3_22)

def popup(event):
    menu_22.post(event.x_root, event.y_root)   # post在指定的位置显示弹出菜单
tex_22.bind("<Button-3>", popup)   # 绑定鼠标右键,执行popup函数
#31
def callback1_31(event=None):
    global top
    ent_31.event_generate('<<Cut>>')
    
def callback2_31(event=None):
    global top
    ent_31.event_generate('<<Copy>>')
    
def callback3_31(event=None):
    global top
    ent_31.event_generate('<<Paste>>')
    
'''创建一个弹出菜单'''
menu_31 = Menu(top,
            tearoff=False,
            #bg="black",
            )
menu_31.add_command(label="剪切", command=callback1_31)
menu_31.add_command(label="复制", command=callback2_31)
menu_31.add_command(label="粘贴", command=callback3_31)

def popup(event):
    menu_31.post(event.x_root, event.y_root)   # post在指定的位置显示弹出菜单
ent_31.bind("<Button-3>", popup)   # 绑定鼠标右键,执行popup函数
#32
def callback1_32(event=None):
    global top
    tex_31.event_generate('<<Cut>>')
    
def callback2_32(event=None):
    global top
    tex_31.event_generate('<<Copy>>')
    
def callback3_32(event=None):
    global top
    tex_31.event_generate('<<Paste>>')
    
'''创建一个弹出菜单'''
menu_32 = Menu(top,
            tearoff=False,
            #bg="black",
            )
menu_32.add_command(label="剪切", command=callback1_32)
menu_32.add_command(label="复制", command=callback2_32)
menu_32.add_command(label="粘贴", command=callback3_32)

def popup(event):
    menu_32.post(event.x_root, event.y_root)   # post在指定的位置显示弹出菜单
tex_31.bind("<Button-3>", popup)   # 绑定鼠标右键,执行popup函数
#41
def callback1_41(event=None):
    global top
    ent_41.event_generate('<<Cut>>')
    
def callback2_41(event=None):
    global top
    ent_41.event_generate('<<Copy>>')
    
def callback3_41(event=None):
    global top
    ent_41.event_generate('<<Paste>>')
    
'''创建一个弹出菜单'''
menu_41 = Menu(top,
            tearoff=False,
            #bg="black",
            )
menu_41.add_command(label="剪切", command=callback1_41)
menu_41.add_command(label="复制", command=callback2_41)
menu_41.add_command(label="粘贴", command=callback3_41)

def popup(event):
    menu_41.post(event.x_root, event.y_root)   # post在指定的位置显示弹出菜单
ent_41.bind("<Button-3>", popup)   # 绑定鼠标右键,执行popup函数
#42
def callback1_42(event=None):
    global top
    tex_41.event_generate('<<Cut>>')
    
def callback2_42(event=None):
    global top
    tex_41.event_generate('<<Copy>>')
    
def callback3_42(event=None):
    global top
    tex_41.event_generate('<<Paste>>')
    
'''创建一个弹出菜单'''
menu_42 = Menu(top,
            tearoff=False,
            #bg="black",
            )
menu_42.add_command(label="剪切", command=callback1_42)
menu_42.add_command(label="复制", command=callback2_42)
menu_42.add_command(label="粘贴", command=callback3_42)

def popup(event):
    menu_42.post(event.x_root, event.y_root)   # post在指定的位置显示弹出菜单
tex_41.bind("<Button-3>", popup)   # 绑定鼠标右键,执行popup函数
#43
def callback1_43(event=None):
    global top
    ent_42.event_generate('<<Cut>>')
    
def callback2_43(event=None):
    global top
    ent_42.event_generate('<<Copy>>')
    
def callback3_43(event=None):
    global top
    ent_42.event_generate('<<Paste>>')
    
'''创建一个弹出菜单'''
menu_43 = Menu(top,
            tearoff=False,
            #bg="black",
            )
menu_43.add_command(label="剪切", command=callback1_43)
menu_43.add_command(label="复制", command=callback2_43)
menu_43.add_command(label="粘贴", command=callback3_43)

def popup(event):
    menu_43.post(event.x_root, event.y_root)   # post在指定的位置显示弹出菜单
ent_42.bind("<Button-3>", popup)   # 绑定鼠标右键,执行popup函数
#44
def callback1_44(event=None):
    global top
    ent_43.event_generate('<<Cut>>')
    
def callback2_44(event=None):
    global top
    ent_43.event_generate('<<Copy>>')
    
def callback3_44(event=None):
    global top
    ent_43.event_generate('<<Paste>>')
    
'''创建一个弹出菜单'''
menu_44 = Menu(top,
            tearoff=False,
            #bg="black",
            )
menu_44.add_command(label="剪切", command=callback1_44)
menu_44.add_command(label="复制", command=callback2_44)
menu_44.add_command(label="粘贴", command=callback3_44)

def popup(event):
    menu_44.post(event.x_root, event.y_root)   # post在指定的位置显示弹出菜单
ent_43.bind("<Button-3>", popup)   # 绑定鼠标右键,执行popup函数
#51
def callback1_51(event=None):
    global top
    ent_51.event_generate('<<Cut>>')
    
def callback2_51(event=None):
    global top
    ent_51.event_generate('<<Copy>>')
    
def callback3_51(event=None):
    global top
    ent_51.event_generate('<<Paste>>')
    
'''创建一个弹出菜单'''
menu_51 = Menu(top,
            tearoff=False,
            #bg="black",
            )
menu_51.add_command(label="剪切", command=callback1_51)
menu_51.add_command(label="复制", command=callback2_51)
menu_51.add_command(label="粘贴", command=callback3_51)

def popup(event):
    menu_51.post(event.x_root, event.y_root)   # post在指定的位置显示弹出菜单
ent_51.bind("<Button-3>", popup)   # 绑定鼠标右键,执行popup函数

top.mainloop

#x=input('lhonvp gaaimvt lvq nhuusthut')
