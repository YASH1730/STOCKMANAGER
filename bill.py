from tkinter import *
from copy import deepcopy
from tkinter import ttk as tk
from tkinter import messagebox as msg
import sqlite3 as db
import datetime as d 

#THIS LINE RUN WHEN U RUN THIS CODE FIRST TIME

try:
    cr = db.connect("New.db")
    cr.execute('''CREATE TABLE Items (Product_Id TEXT PRIMARY KEY, Product_Name TEXT , Size TEXT , Price TEXT,Available INT);''') 
    cr.colse()
except Exception as e :
    print(e)    

try:
    cr = db.connect("New.db")
    cr.execute("CREATE TABLE Records (Bill_No TEXT PRIMARY KEY,Bill_Date Text,Bill_Time Text,Product_Id text,Coustmor_Name Text,Payment_Method Text,Toatal_Purchase text);") 
    cr.colse()
except Exception as e :
    print(e)

try:
    cr = db.connect("New.db")
    cr.execute("CREATE TABLE Bill (Bill_No TEXT PRIMARY KEY);") 
    i = '1'
    print(i)
#    cr.execute("INSERT INTO Records (Bill_No,Bill_Date,Bill_Time,Product_Id,Coustmor_Name,Payment_Method,Toatal_Purchase) VALUES ('"+k+"','"+date+"','"+time.strftime('%H:%M')+"','"+products+"','"+namec.get()+"','"+pay+"','"+hole+"')")

    cr.execute("INSERT INTO Bill (Bill_No) VALUES ('"+i+"')")
    cr.commit()
    cr.close()
except Exception as e :
    print(e)


count = 0

#its a binded function which helps to incriment the Sr no
def click(e):
    global count 
    count += 1
    return count
hole = 0

#its helps to add items in list
bro = 0
def search():
        global bro 
        global rain
        global count
        global hole
        cr = db.connect('New.db')
        id = proid.get()
        r =  cr.execute(f'SELECT Product_Id , Product_Name , Size , Price , Available FROM Items WHERE Product_Id = "{id}"')
        res = r.fetchone()
        print(res)
        idp = res[0]
        ina = res[1]
        ins = res[2]
        inp = res[3]
        ava = res[4]
        if bro == 0:
            rain = ava
            bro += 1
        print(ava,'pices left in add')
        if (ava <= 5):
            msg.showerror('Alert',f"Only {rain} is left is stock,u can't order more")            
            count -= 1
            cr.close()
        else:
            #if (rain < a) :
            #   msg.showerror('Alert',"You can't order more")"""
                a = int(peca.get())
                rain -= a
                print(rain)
                b = int(inp)
                c = a*b
                int(hole)
                hole = hole + c
                plist.insert(parent = "",index = END,values = (count,idp,ina,ins,peca.get(),c))
                proid.set('') 
                peca.set('')  
                cr.close()
        #msg.showerror('OPPS!!!',"Enter the correct product ID")    

#Its manage the stock in stor
global reffer
reffer = 1
def stock():
    global reffer
    cr =  db.connect('New.db')
    r = plist.get_children()
    
    for rec in r:
        reffer += 1.0
        j = plist.item(rec,'values')
        print(j[1],'stock')
        id = j[1]
        data = cr.execute(f'SELECT Available FROM Items WHERE Product_Id = "{id}"')
        no = data.fetchone()
        no = int(no[0])-int(j[4])
        cr.execute(f'UPDATE Items set Available = {no} WHERE Product_Id = "{id}"')
        cr.commit()
        if (no <= 5):
            ref = int(reffer)
            screentext.insert(END,f"{ref}. We have only {no} pices of {j[1]} left in stock !!!")
    cr.close()

def notify():
    global reffer
    cr = db.connect('New.db')
    rec = cr.execute('SELECT * FROM Items')
    r = rec.fetchall()
    ref = reffer
    screentext.delete(0,END)
    for i in r:
        j = int(i[4])
        if (j<=5):
            screentext.insert(END,f'Alert :: {ref}. "We have only {i[0]} pices of {j} left in stock !!!"')
            ref += 1
        else:
            pass
    cr.close()
#its help to remove the item frome the list

def remove():
    global rain
    global count
    x = plist.selection()
    try:
        i = 0
        for rec in x:
            i += 1
            plist.delete(rec)
        count = 0
        records = plist.get_children()
        for r in records:
            j = plist.item(r,'values')
            h = list(j)
            count += 1
            h[0] = count
            rain = rain + int(h[4])
            print(rain,h[4])
            j = tuple(h)
            plist.delete(r)
            plist.insert(parent = "",index = END,values = (j))
    except Exception as e :
        print(e)
        msg.showerror('OPPS!!!',"First Select the product which you want to delete.")    
        
# its genrate a bill nimber

def genbill(e):
    cr = db.connect('New.db')
    rec = cr.execute("SELECT * FROM Bill")
    r  = rec.fetchall()
    k = ''
    for i in r :
        k = i[0]
    print(k,' i am printed because u clicked on reset')
    genrallabel = Label(lside,borderwidth =0,text = f'Date :- {date}       Bill No. :- {k}        Time :- {time.strftime("%H:%M")}' , font = 'arial 15',bg = "#3d4c51",fg = 'white')
    genrallabel.place(x= 80,y=70)

# its genrate the bill no

def billcount():
    global date
    global hole
    global billn
    cr = db.connect('New.db')

    rec = cr.execute("SELECT Bill_No FROM Bill")
    j = rec.fetchall()
    for k  in j :
        l = k[0]
        print(l,'i am frome loop')
    billn = l
    r =  plist.get_children()
    products = ''
    
    for i in r:
        j = plist.item(i,'values')
        products += j[2] + ','

    print('I am bill no.',billn)

    date = str(date)
    hole = str(hole)
    
    p = var.get()
    
    if (p == 1):
            pay = 'Cash'
    elif (p == 2):
            pay = "Online"
    elif (p == 3):
            pay = "Card" 
    
    cr.execute("INSERT INTO Records (Bill_No,Bill_Date,Bill_Time,Product_Id,Coustmor_Name,Payment_Method,Toatal_Purchase) VALUES ('"+billn+"','"+date+"','"+time.strftime('%H:%M')+"','"+products+"','"+namec.get()+"','"+pay+"','"+hole+"')")
    print('error 1 ')
    cr.commit()
    
    new  = int(billn)
    new += 1 
    print('error 2')
    billn = str(new)
    print(l)
    cr.execute("INSERT INTO Bill (Bill_No) VALUES  ('"+billn+"')")
    cr.commit()
    cr.close()    


#This function use to append the data exiting database

def data():    
    cr = db.connect('New.db')
    def printt():
        try :
            temp  = pname.get()
            temp = temp[:3]
            for i in range(1,4):
                a = temp
                temp += '0'+str(i)

                Id = str(temp)
                                
                if (i == 1):
                    cr.execute("INSERT INTO Items (Product_Id,Product_Name,Size,Price,Available)  VALUES ('"+Id+"','"+pname.get()+"','250','"+p250.get()+"','"+avas.get()+"')")
                    cr.commit()
                elif (i == 2):
                    cr.execute("INSERT INTO Items (Product_Id,Product_Name,Size,Price,Available)  VALUES ('"+Id+"','"+pname.get()+"','500','"+p500.get()+"','"+avas.get()+"')")
                    cr.commit()
                else :
                    cr.execute("INSERT INTO Items (Product_Id,Product_Name,Size,Price,Available)  VALUES ('"+Id+"','"+pname.get()+"','1000','"+p1000.get()+"','"+avas.get()+"')")
                    cr.commit()
                temp = a
            msg.showinfo('Done',f'Product Id Genrated Successfully {Id}')
            dataw.destroy()
            data()
        except Exception as e:
            print(e)
            msg.showerror('OPPS!!!',"Fill the entries before submiting.")
       
    
    dataw = Toplevel()
    dataw.geometry('330x240')
    dataw.title('Data Entry')
    dataw.config(bg = "#3d4c51")  
    
    xvar = 20
    yvar = 30
    
    pname = StringVar()
    p250 = StringVar()
    p500 = StringVar()
    p1000 = StringVar()
    avas = StringVar()
    

    prolab = Label(dataw,fg = 'white',bg = "#3d4c51",text = 'Product Name')
    prolab.place(x=xvar,y=yvar)

    proen = Entry(dataw,textvariable = pname)
    proen.place(x= xvar+120 , y= yvar )

    pack250  = Label(dataw,fg = 'white',bg = "#3d4c51",text = '250 g/ml Price')
    pack250.place(x = xvar,y = yvar+30)
    
    pack250e  = Entry(dataw,textvariable = p250)
    pack250e.place(x = xvar+120,y = yvar+30)
    
    pack500  = Label(dataw,fg = 'white',bg = "#3d4c51",text = '500 g/ml Price')
    pack500.place(x=xvar,y = yvar+60)
    
    pack500e  = Entry(dataw,textvariable = p500)
    pack500e.place(x=xvar+120,y = yvar+60)

    pack1000  = Label(dataw,fg = 'white',bg = "#3d4c51",text = '1000 kg/l Price')
    pack1000.place(x=xvar,y = yvar+90)

    pack1000e  = Entry(dataw,textvariable = p1000)
    pack1000e.place(x=xvar+120,y = yvar+90)
    
    avapack = Label(dataw,fg = 'white',bg = "#3d4c51",text = 'Available Stock')
    avapack.place(x=xvar , y = yvar+120)

    avaen = Entry(dataw,textvariable = avas)
    avaen.place(x=xvar+120,y = yvar+120)       

    Button(dataw,text = "More",command  = printt).place(x=xvar+120,y = yvar + 150)
    Button(dataw,text = "Exit",command = dataw.destroy).place(x=xvar+225,y = yvar + 150)
    
    dataw.mainloop()
    cr.close()

# this helps to evalueate the total bill

def ecvate():
    try:
        global hole
        d = int(di.get())
        pe = (int(hole))/100*d
        #print(pe)
        hole = hole - pe
        #print(hole)
        to = int(hole/100*int(gs.get()))
        #print(to)
        hole += to
        #print(hole)
        int(hole)
        totalentry = Label(lside,text = hole,bg = 'white',font = 'arial 12')
        totalentry.place(x=320,y=640)
        billcount()
        stock()
    except Exception as e:
        print(e)
        msg.showerror('OPPS!!!',"Fill all entries before submit the bill.")

#this helps to create a ricpt

def makearicipt():
   rictext.insert(0.0,'\n                          A TO Z SHOP') 
   rictext.insert(5.0,'\n\n      -----------------------RICITP-----------------------') 
   rictext.insert(11.0,f'\n\n      Bill No. :{billn} \t   Date : {date} \t   Time : {time.strftime("%H:%M")}')
   rictext.insert(15.0,f"\n\n      Name :{namec.get()}")
   pay = ''
   p = var.get()
   if (p == 1):
            pay = 'Cash'
   elif (p == 2):
            pay = "Online"
   elif (p == 3):
            pay = "Card"
   rictext.insert(17.0,f"\n      Payment Mode :{pay}")
   rictext.insert(20.0,f"\n      ----------------------------------------------------\n")
   #rictext.insert(19.0,f"\n      Sr No. |   Product Name   |  Size  | Peice | Price")
   rec = plist.get_children()
   i = 26.0
   for r in rec:
       j = plist.item(r,'values')
       print(j)
       rictext.insert(i,f"\n      {j[0]}.    {j[2]}  |  {j[3]} G/Ml  |  {j[4]} peice  | {j[5]} Rs")
       i += 1.0
   i += 1.0
   rictext.insert(i,f"\n\n      ----------------------------------------------------\n")
   i += 2.0
   rictext.insert(i,f"\n      DISCOUNT : {di.get()}%")
   i += 1.0
   rictext.insert(i,f"\n      GST      : {gs.get()}%")
   i += 1.0
   rictext.insert(i,f"\n      TOTAL    : {hole} Rs.")
   i += 1.0
   rictext.insert(i,'\n\n                 ****THANK YOU AND VISIT AGIAN****') 

def resetit():
  global hole
  global count
  nameentry.delete(0,END)
  pidentry.delete(0,END)
  pecentry.delete(0,END)
  count = 0
  disentry.delete(0,END)
  gstentry.delete(0,END)
  rec = plist.get_children()
  for r in rec:
      plist.delete(r)
  totalentry = Label(lside,text = '                            ',bg = 'white',font = 'arial 12')
  totalentry.place(x=320,y=640)      
  hole = 0
  totalentry = Label(lside,text = int(hole),bg = 'white',font = 'arial 12')
  totalentry.place(x=320,y=640)      

#this is help you see the remaining in stock vertuilly

def showstock():
    
    # this is window code of it 
    showst = Toplevel()
    showst.geometry('676x480')
    showst.title('Stock Data')
    secid = StringVar()
    Label(showst,fg = 'White', text = "Product Id  :-",font = 'arial 15',bg = '#3d4c51').place(x= 100,y=50)

    serentry = Entry(showst,textvariable = secid)
    serentry.place(x=260,y=50)


    col = ('Sr_No.','Product Id','Product Name','Size','Price','Available') 

    pframe = Frame(showst,borderwidth = 2,relief=SUNKEN,bg = 'black',width = 676,height = 550)
    pframe.place(x=0,y=120)
    
    scrollbar = Scrollbar(pframe)
    scrollbar.pack( side = RIGHT, fill=Y)

    plist = tk.Treeview(pframe,yscrollcommand = scrollbar.set,height=14,show ='headings',columns = col )
    plist.column('Sr_No.',width=70,anchor=CENTER)
    plist.column('Product Id',width=110,anchor=CENTER)
    plist.column('Product Name',width=190,anchor=CENTER)
    plist.column('Size',width=90,anchor = CENTER)
    plist.column('Price',width= 90,anchor = CENTER)
    plist.column('Available', width = 100 , anchor = CENTER)

    plist.heading('Sr_No.',text = 'Sr No.')
    plist.heading('Product Id',text = 'Product Id')
    plist.heading('Product Name',text = 'Product Name')
    plist.heading('Size' ,text = 'Size')
    plist.heading('Price',text= 'Price')
    plist.heading('Available' ,text = 'Available')
    plist.pack(side = LEFT)
    scrollbar.config(command = plist.yview)
    
    Button(showst,text = 'Exit',command = showst.destroy).place(x = 610,y = 430)   
    showst.config(bg = '#3d4c51')
    
    def edit():
    
        ed = Toplevel()
        ed.geometry('330x170')
        ed.title('Edit')
        ed.config(bg = "#3d4c51")  
        xvar = 20
        yvar = 30
        id  = secid.get()
        namp = StringVar()
        pri = StringVar()
        avas = StringVar()

        namp.set(id)
        pri.set('0')
        avas.set('0')
       
        Label(ed,fg = 'white',bg = "#3d4c51",text = f'Product_ID').place(x=xvar,y=yvar)
        Entry(ed,textvariable = namp).place(x=xvar+120,y=yvar)

        pack250  = Label(ed,fg = 'white',bg = "#3d4c51",text = 'Price')
        pack250.place(x = xvar,y = yvar+30)
        
        pack250e  = Entry(ed,textvariable = pri)
        pack250e.place(x = xvar+120,y = yvar+30)
                
        avapack = Label(ed,fg = 'white',bg = "#3d4c51",text = 'Available Stock')
        avapack.place(x=xvar , y = yvar+60)

        avaen = Entry(ed,textvariable = avas)
        avaen.place(x=xvar+120,y = yvar+60)       

        
        def done(): 
           cr = db.connect('New.db')
           id  = namp.get()
           a = 0 
           b = 0
           a = int(avas.get())
           b = int(pri.get())
           
           if (a != 0):
                cr.execute(f'UPDATE Items set Available = {avas.get()} WHERE Product_Id = "{id}"')
                cr.commit()
    
           if (b != 0):
               cr.execute(f'UPDATE Items set Price = {pri.get()} WHERE Product_Id = "{id}"')
               cr.commit()
           msg.showinfo('Done','Stock Updated Successfullu !!!')
           cr.close()
        
        Button(ed,text = "Exit",command = ed.destroy).place(x=xvar+230,y = yvar+100)
        Button(ed,text = "Done",command  = done).place(x=xvar+120,y = yvar + 100)
        ed.mainloop()

    
    def refresh():
        c = 0
        cr = db.connect('New.db')
    
        child = plist.get_children()
    
        for j in child:
            plist.delete(j)
        
        r =  cr.execute(f'SELECT * FROM Items')
        rec = r.fetchall()
        for i in rec:
            c+=1
            plist.insert(parent = "",index = END,values = (c,i[0],i[1],i[2],i[3],i[4]))
        cr.close()
    refresh()
    
    def sec():
        id = secid.get()
        print(id)
        child = plist.get_children()
        for i in child:
            j = plist.item(i,'values')
            print(j)
            if j[1] == id:
               k = j
               for j in child:
                   plist.delete(j)
               plist.insert(parent = "",index = END,values = (k[0],k[1],k[2],k[3],k[4],k[5]))

    Button(showst,text = 'Search',command = sec).place(x=470,y = 49)
    Button(showst,text = 'Refresh',command =refresh).place(x = 10,y = 430)
    Button(showst,text = 'Edit',command = edit).place(x=310,y = 430)

    showst.mainloop()

def resetric():
    rictext.delete(0.0,END)

def billrecords():
    
    # this is window code of it 
    showst = Toplevel()
    showst.geometry('800x480')
    showst.title('Records')
    secid = StringVar()
    Label(showst,fg = 'White', text = "Bill No.  :-",font = 'arial 15',bg = '#3d4c51').place(x= 200,y=50)

    serentry = Entry(showst,textvariable = secid)
    serentry.place(x=320,y=50)


    col = ('Bill No.','Date','Time','Product Id','Coustmer Name','Pay Mode','Total') 

    pframe = Frame(showst,borderwidth = 2,relief=SUNKEN,bg = 'black',width = 676,height = 550)
    pframe.place(x=0,y=120)
    
    scrollbar = Scrollbar(pframe)
    scrollbar.pack( side = RIGHT, fill=Y)

    plist = tk.Treeview(pframe,yscrollcommand = scrollbar.set,height=14,show ='headings',columns = col )
    plist.column('Bill No.',width=60,anchor=CENTER)
    plist.column('Date',width=100,anchor=CENTER)
    plist.column('Time',width=80,anchor=CENTER)
    plist.column('Product Id',width=190,anchor='w')
    plist.column('Coustmer Name',width=190,anchor = 'w')
    plist.column('Pay Mode',width= 80,anchor = CENTER)
    plist.column('Total', width = 80 , anchor = CENTER)

    plist.heading('Bill No.',text = 'Bill No.')
    plist.heading('Date',text = 'Date')
    plist.heading('Time',text = 'Time')
    plist.heading('Product Id',text = 'Product Id')
    plist.heading('Coustmer Name' ,text = 'Coustmer Name')
    plist.heading('Pay Mode',text= 'Pay Mode')
    plist.heading('Total' ,text = 'Total')
    plist.pack(side = LEFT)
    scrollbar.config(command = plist.yview)
    
    showst.config(bg = '#3d4c51')
    
    def refresh():
        c = 0
        cr = db.connect('New.db')
    
        child = plist.get_children()
    
        for j in child:
            plist.delete(j)
        
        r =  cr.execute(f'SELECT * FROM Records')
        rec = r.fetchall()
        for i in rec:
            
            plist.insert(parent = "",index = END,values = (i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        cr.close()
    refresh()
    
    def sec(): 
        id = secid.get()
        child = plist.get_children()
        for i in child:
            j = plist.item(i,'values')
            if j[0] == id:
               k = j
               for j in child:
                   plist.delete(j)
               plist.insert(parent = "",index = END,values = (k[0],k[1],k[2],k[3],k[4],k[5],k[6]))

    Button(showst,text = 'Search',command = sec).place(x=520,y = 49)
    Button(showst,text = 'Exit',command = showst.destroy).place(x = 735,y = 430)   
    Button(showst,text = 'Refresh',command =refresh).place(x = 10,y = 430)
    showst.mainloop()

# THIIS IS OUR MAIN WINDOW CODE
 
root = Tk()
root.geometry("1366x768")
root.title("Billing system")
#image = PhotoImage('3.ico')
##root.iconphoto(False,image)
var  = IntVar()
proid = StringVar()
peca = StringVar()
di = StringVar()
gs = StringVar()
namec = StringVar()

menu = Menu(root)
root.config(menu = menu)

men2 = Menu(menu,tearoff = 0)
menu.add_cascade(label = 'File',menu = men2)
men2.add_command(label="Show My Stock", command = showstock)
men2.add_command(label="Bill Records", command = billrecords)

men = Menu(menu,tearoff = 0)
menu.add_cascade(label = 'Edit',menu = men)
men.add_command(label="Data Entry", command = data)
menu.add_command(label  ='Exit',command = quit)



#Left side frame


date = d.date.today()
time = d.datetime.now()

lside = Frame(root, bg = '#3d4c51',borderwidth = 2, height = 700, width = 683,relief = SUNKEN)
lside.grid(row = 0,column= 0)

billlabel  = Label(lside,text = "Bill Calculator",bg='#3d4c51',font = "arial 20 bold",fg = 'White')
billlabel.place( x = 260, y=5)


namelabel = Label(lside,fg = 'White', text = "Name Of Coustomer",font = 'arial 15',bg = '#3d4c51')
namelabel.place(x= 80,y=130)

nameentry = Entry(lside,textvariable = namec)
nameentry.place(x=320,y=133)

moplabel = Label(lside,fg = 'White', text='Mode Of Payment',font ='arial 15',bg = '#3d4c51')
moplabel.place(x=80,y=170)


Radiobutton(lside,fg = 'black',activebackground = '#3d4c51',borderwidth = 2,bg =  'light grey',variable = var,value = 1,text= 'Cash',highlightthickness = 0,font='arial 12',relief = SUNKEN).place(x=320,y=170)

Radiobutton(lside,fg = 'black',activebackground = '#3d4c51',borderwidth = 2, text='Online',variable = var,value = 2,highlightthickness = 0,font='arial 12 ',bg = 'lightgrey',relief = SUNKEN).place(x=400,y=170)

Radiobutton(lside,fg = 'black',activebackground = '#3d4c51',borderwidth = 2,text= 'Card',variable = var,value = 3,highlightthickness = 0,font = 'arial 12 ',bg = 'lightgrey',relief = SUNKEN).place(x=490,y = 170)

pid = Label(lside,fg = 'White',text='Product Id',font ='arial 15',bg = '#3d4c51')
pid.place(x=80,y=210)

pidentry = Entry(lside,borderwidth= 1,textvariable = proid)
pidentry.place(x= 320,y=213 )

pec = Label(lside,fg = 'White',text='Piece',font ='arial 15',bg = '#3d4c51')
pec.place(x=80,y=243)

pecentry = Entry(lside,borderwidth= 1,textvariable = peca)
pecentry.place(x= 320,y=248 )


addb = Button(lside, text='+',command = search)
addb.bind('<Button-1>',click)
addb.place(x=500,y=225)

subb = Button(lside, text= '-',command = remove)
#subb.bind('<Button-1>',click2)
subb.place(x=545,y=225)


pframe = Frame(lside,borderwidth = 2,relief=SUNKEN,bg = 'white',width = 676,height = 350)
pframe.place(x=1,y=280)

col = ('Sr_No.','Product Id','Product Name','Size','Piece','Price') 

scrollbar = Scrollbar(pframe)
scrollbar.pack( side = RIGHT, fill=Y)
plist = tk.Treeview(pframe,yscrollcommand = scrollbar.set,height=12,show ='headings',columns = col )


plist.column('Sr_No.',width=70,anchor=CENTER)
plist.column('Product Id',width=112,anchor=CENTER)
plist.column('Product Name',width=190,anchor=CENTER)
plist.column('Size',width=119,anchor = CENTER)
plist.column('Piece', width = 70 , anchor = CENTER)
plist.column('Price',width= 113,anchor = CENTER)

plist.heading('Sr_No.',text = 'Sr No.')
plist.heading('Product Id',text = 'Product Id')
plist.heading('Product Name',text = 'Product Name')
plist.heading('Size' ,text = 'Size')

plist.heading('Piece' ,text = 'Piece')
plist.heading('Price',text= 'Price')
plist.pack(side = LEFT)
scrollbar.config(command = plist.yview)

dislable = Label(lside,fg = 'White', text = 'Discount (At whole bill)',bg = '#3d4c51',font = 'arial 15')
dislable.place(x = 80,y = 560 )

disentry = Entry(lside ,textvariable = di)
disentry.place(x=320,y=560)

gstlabel = Label(lside,fg = 'White', text = 'GST (At whole bill)',bg = '#3d4c51',font = 'arial 15')
gstlabel.place(x=80,y = 600)

gstentry = Entry(lside,textvariable = gs)
gstentry.place(x=320,y=600)

totallabel = Label(lside,fg = 'White',text = 'Total Bill',bg ='#3d4c51',font = 'arial 15')
totallabel.place(x=80, y = 640)

e = ''
genbill(e)

submit = Button(lside,text = 'Submit',command = ecvate)
submit.place(x=550,y= 610)

reset = Button(lside,text = 'Reset',width = 6,command = resetit)
reset.bind('<Button-1>',genbill)
reset.place(x= 550 ,y= 570)



#Right side frame
rside = Frame(root, bg = 'black',borderwidth = 2, height = 700, width = 683,relief = SUNKEN)
rside.grid(row= 0,column= 801)

#ricipt modul

ricframe = Frame(rside,bg = '#3d4c51',height = 400,width = 680)
ricframe.place(x=0,y=0)

textf = Frame(ricframe,bg = 'black',height = 300 , width = 655)
textf.place(x=14,y=10)

scrollbartext = Scrollbar(textf)
scrollbartext.pack(side = RIGHT,fill = Y)

scrollbartexth = Scrollbar(textf,orient = HORIZONTAL)
scrollbartexth.pack(side = BOTTOM,fill=X)

rictext = Text(textf,height = 18,width = 63,font = 'Courier 12',bg = '#B0DFE5',xscrollcommand = scrollbartexth.set,yscrollcommand = scrollbartext.set)
rictext.pack()

scrollbartext.config(command = rictext.yview)
scrollbartexth.config(command = rictext.xview)

Button(ricframe, text = 'Genrate Ricipt',font = 'arial 12' ,command = makearicipt).place(x= 15,y=350)
Button(ricframe, text = 'Reset',font = 'arial 12' ,command = resetric).place(x= 590,y=350)

#notifyer

notf  = Frame(rside,bg = '#3d4c51',height = 300,width = 680)
notf.place(x=0,y=401)

screennotf = Frame(notf,bg = 'black',height = 300 , width = 655)
screennotf.place(x=13,y=10)

sscrollbartext = Scrollbar(screennotf)
sscrollbartext.pack(side = RIGHT,fill = Y)

s2scrollbartexth = Scrollbar(screennotf,orient = HORIZONTAL)
s2scrollbartexth.pack(side = BOTTOM,fill=X)

screentext = Listbox(screennotf,font = 'arial 12 italic',fg = '#cf352e',height = 10,width = 70,xscrollcommand = s2scrollbartexth.set,yscrollcommand = sscrollbartext.set)
screentext.pack()
screentext.config(bg = '#fbceb1')



Button(rside,text = 'Refesh',command = notify,font = 'arial 12').place(x = 310 ,y =640)

sscrollbartext.config(command = screentext.yview)
s2scrollbartexth.config(command = screentext.xview)












#bottom bar
bside = Frame(root, bg ="light grey",borderwidth = 1, height = 20,width = 1366,relief = SUNKEN)  
bside.place(x = 0,y = 690)

ready = Label(bside,text = 'Ready...')
ready.place(x=0,y = 0)

root.mainloop()
