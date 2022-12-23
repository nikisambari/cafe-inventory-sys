from tkinter import*
import mysql.connector
from datetime import datetime
from PIL import Image, ImageTk
import time
root=Tk()
root.configure(bg="white")
root.geometry("700x500")   
textin=StringVar()
operator=""

con=mysql.connector.connect(host='localhost',user="root",passwd='root',database="coffee")
cur=con.cursor()

item=[]
x=0
price=[]
text1=IntVar()
d = datetime.now()
dt = d.strftime("%m/%d/%Y   %H:%M %p")
date=d.strftime("%m/%d/%Y")
tym=d.strftime("%H:%M %p")
t=str(tym)

def clickbut(number):  
     global operator
     operator=operator+str(number)
     pascod=str(number)
     textin.set(operator)
     if operator=="1234":
          b1.configure(state="active")
          b2.configure(state="active")
          b3.configure(state="active")
          b4.configure(state="active")
          b5.configure(state="active")
          b6.configure(state="active")

    
    
def clear():
     global operator
     operator=""
     textin.set(operator)
     

def  cl():
          data=Toplevel()
          data.configure(bg="white")
          data.geometry("440x230")
          textin=IntVar()
          
          f1=Frame(data,width=440,height=230,bg='ghostwhite')
          f1.pack(side=LEFT,anchor="se")
          l1=Label(data,text="ORDER NO.",font=("Courier New",16,'bold'),fg="white",bg="black")
          l1.place(x=40,y=40)

          t1=Entry(f1,font=("Courier New",16,'bold'),textvariable=textin,width=9)
          t1.place(x=200,y=40)
          def cancel():
               from tkinter import messagebox
               h=0
               no=textin.get()
               
               que1=("select orno from orders")
               cur.execute(que1)
               
               row=cur.fetchone()
               while row is not None:
                    if no==row[0]:
                         h=1
                    row=cur.fetchone()    
               if h==1:
                    delque="delete from orders where orno = %d"%(no)
                    cur.execute(delque)
                    messagebox.showinfo("ord","Order Cancelled..")
                    con.commit()
               else:
                    messagebox.showinfo("ord","Enter valid Order number")
                    
                    
          x1=Button(data,width=9,height=2,text="Cancel",bg='black',fg='white',font=("Courier New",13,'bold'),command=cancel)
          x1.place(x=170,y=140)
          
          data.mainloop()



     
billitems=[]
billprice=[]
total=0
amount=0
gst=0
dsc=0
def  ord():
          data=Toplevel()    
          data.configure(bg="gray22")
          data.geometry("1350x650")
          global text1
          global item
          global total
          
          global price,billitems,billprice,date,tym
          
            

          def add(str1,p):           #####add to cart #######
                  global total,c      

                  
                  item.append(str(text1.get())+"  "+str1)        
                  val=text1.get()
                  
                  p=p*val
                  lsbp.insert(END,p)
                  price.append(p)
                  total=sum(price)
                  lsb.insert(END,str(text1.get())+" "+str1)        
                  
          def re():                 ### remove item #####
                  global billprice,billitems,total
                  
                  a=lsb.index(ANCHOR)  
                  #for i in a:                
                  lsb.delete(a)
                  
                  
                  lsbp.delete(a)
                  
                                    
                  item.__delitem__(a)
                  
                  
                  
                  price.__delitem__(a)
                  
                  total=sum(price)
                  
          def saving():        ### click on save button to store items in bill ##
               global billitems,billprice  
               billitems=item.copy()
               
               billprice=price.copy()
               
             
          def sending():         #####send to kitchen ###
                 
                 s=Toplevel()
                 s.configure(bg="gray22")
                 s.geometry("250x100")
                 def close():
                      s.destroy()
                 Label(s,text="Sending to kitchen..",font=("Courier New",10,'bold'),fg="white",bg="gray22").place(x=45,y=35)
               
                 Button(s,text="OK",command=close,width=10,height=1,bg="gray22",fg="white",font=("Courier New",9,'bold')).place(x=160,y=70)
          def go_to_home():
               global item,price
               lsb.delete(0,END)
               lsb.delete(0,END)
               item.clear()
               price.clear()
               data.destroy()
           
            ### MENU #########     
              
              
          def coffee():
                 
                  def win1():     
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)       
                      text1.set("1")
                      l1=Label(f3,text="Espresso           ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      89/-    ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Espresso  -Regular           ",89),relief=FLAT)
                      r1.place(x=650,y=90)
                      r2=Button(f3,text=" Medium      119/-    ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Espresso  -Medium           ",119),relief=FLAT)
                      r2.place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                     
                     
                      
                      
                  def win2():
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                      l1=Label(f3,text="Latte               ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      95/-    ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Latte    -Regular            ",95),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium      126/-    ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Latte    -Medium            ",126),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      
                                    
                      
                    

                  def win3():
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                 
                      l1=Label(f3,text="Mocha                ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      70/-    ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Mocha    -Regular            ",70),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium      112/-    ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Mocha    -Medium            ",112),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                     
                  def win4():

                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                      
                      l1=Label(f3,text="Double Espresso      ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)    
                      r1=Button(f3,text=" Regular      91/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Double Espresso -Regular     ",91),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium      134/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Double Espresso -Medium     ",134),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      
                  def win5():
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
            
                      l1=Label(f3,text="Americano            ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      68/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Americano  -Regular          ",68),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium      123/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Americano  -Medium          ",123),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      
                  def win6():      
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                      l1=Label(f3,text="Black Coffee         ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      73/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Black Coffee  -Regular       ",73),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium      103/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Black Coffee  -Medium       ",103),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                     
                  def win7():    
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
               
                      l1=Label(f3,text="Flat White            ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      88/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Flat White  -Regular         ",88),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium      104/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Flat White   -Medium        ",104),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                     
                  def win8():      
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                
                      l1=Label(f3,text="Cold Coffee           ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      69/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Cold Coffee -Regular         ",69),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium      111/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Cold Coffee  -Medium        ",111),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      
                  def win9():     
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                 
                      l1=Label(f3,text="Frappe             ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      76/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Frappe  -Regular             ",76),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium      112/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Frappe  -Medium             ",112),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                     

                  def win10():      
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                
                      l1=Label(f3,text="Cappuccino          ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      69/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Cappuccino  -Regular         ",69),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium      149/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Cappuccino  -Medium         ",149),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      
                  
                  
                  butf1=Button(f3,text="Espresso                                ",width=45,height=1,command=win1,font=("Courier New",16,'bold'),bg="white")
                  butf1.place(x=5,y=5)
                  butf2=Button(f3,text="Latte                                   ",width=45,height=1,command=win2,font=("Courier New",16,'bold'),bg="white")
                  butf2.place(x=5,y=45)
                  butf3=Button(f3,text="Mocha                                   ",width=45,height=1,command=win3,font=("Courier New",16,'bold'),bg="white")
                  butf3.place(x=5,y=85)
                  butf4=Button(f3,text="Double Espresso                        ",width=45,height=1,command=win4,font=("Courier New",16,'bold'),bg="white")
                  butf4.place(x=5,y=125)
                  butf5=Button(f3,text="Americano                               ",width=45,height=1,command=win5,font=("Courier New",16,'bold'),bg="white")
                  butf5.place(x=5,y=165)
                  butf6=Button(f3,text="Black Coffee                            ",width=45,height=1,command=win6,font=("Courier New",16,'bold'),bg="white")
                  butf6.place(x=5,y=205)
                  butf7=Button(f3,text="Flat White                              ",width=45,height=1,command=win7,font=("Courier New",16,'bold'),bg="white")
                  butf7.place(x=5,y=245)
                  butf8=Button(f3,text="Cold Coffee                             ",width=45,height=1,command=win8,font=("Courier New",16,'bold'),bg="white")
                  butf8.place(x=5,y=285)
                  butf9=Button(f3,text="Frappe                                  ",width=45,height=1,command=win9,font=("Courier New",16,'bold'),bg="white")
                  butf9.place(x=5,y=325)
                  butf10=Button(f3,text="Cappuccino                              ",width=45,height=1,command=win10,font=("Courier New",16,'bold'),bg="white")
                  butf10.place(x=5,y=365)

          def tea():
               
                  def win1():
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                 
                      l1=Label(f3,text="Black Tea             ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      42/-      ",font=("Courier New",16,'bold',),relief=FLAT,bg="white",command=lambda :add("Black Tea  -Regular          ",42)).place(x=650,y=90)
                      r2=Button(f3,text=" Medium       69/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Black Tea  -Medium           ",69),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      
                              
                  def win2():       
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
               
                      l1=Label(f3,text="Herbal Tea            ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      40/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Herbal Tea  -Regular         ",40),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium       50/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Herbal Tea  -Medium          ",50),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      
                      

                  def win3():     
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                 
                      l1=Label(f3,text="Peppermint Tea         ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      29/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Peppermint Tea  -Regular     ",29),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium       49/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Peppermint Tea  -Medium      ",49),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                    
                  def win4():      
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                
                      l1=Label(f3,text="Lemon Tea             ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      69/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Lemon Tea  -Regular          ",69),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium       89/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Lemon Tea  -Medium           ",89),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                     
                  def win5():       
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1") 
                      l1=Label(f3,text="Mint Tea",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      29/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Mint Tea  -Regular           ",29),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium       39/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Mint Tea  -Medium            ",39),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                     
                  def win6(): 
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")        
                      l1=Label(f3,text="Masala Tea              ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      38/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Masala Tea  -Regular         ",38),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium       52/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Masala Tea  -Medium          ",52),relief=FLAT).place(x=650,y=90)

                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170).place(x=650,y=90)

                  def win7():      
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                
                      l1=Label(f3,text="Ginger Tea             ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      36/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Ginger Tea  -Regular         ",36),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium       59/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Ginger Tea  -Medium          ",59),relief=FLAT).place(x=650,y=90)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      

                  def win8():     
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                 
                      l1=Label(f3,text="Ice Tea              ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      39/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Ice Tea  -Regular            ",39),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium       47/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Ice Tea  -Medium             ",47),relief=FLAT).place(x=650,y=90)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                     
                  def win9():     
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                      l1=Label(f3,text="Cinnamon Tea          ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      29/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Cinnamon Tea  -Regular       ",29),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium       49/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Cinnamon Tea  -Medium        ",49),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      
                  def win10():    
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                 
                      l1=Label(f3,text="Matcha Tea             ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      25/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Matcha Tea  -Regular         ",25),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium       40/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Matcha Tea  -Medium          ",40),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      

                  butf1=Button(f3,text="Black Tea                               ",width=45,height=1,command=win1,font=("Courier New",16,'bold'),bg="white")
                  butf1.place(x=5,y=5)
                  butf2=Button(f3,text="Herbal Tea                              ",width=45,height=1,command=win2,font=("Courier New",16,'bold'),bg="white")
                  butf2.place(x=5,y=45)
                  butf3=Button(f3,text="Peppermint Tea                          ",width=45,height=1,command=win3,font=("Courier New",16,'bold'),bg="white")
                  butf3.place(x=5,y=85)
                  butf4=Button(f3,text="Lemon Tea                               ",width=45,height=1,command=win4,font=("Courier New",16,'bold'),bg="white")
                  butf4.place(x=5,y=125)
                  butf5=Button(f3,text="Mint Tea                                ",width=45,height=1,command=win5,font=("Courier New",16,'bold'),bg="white")
                  butf5.place(x=5,y=165)
                  butf6=Button(f3,text="Masala Tea                              ",width=45,height=1,command=win6,font=("Courier New",16,'bold'),bg="white")
                  butf6.place(x=5,y=205)
                  butf7=Button(f3,text="Ginger Tea                              ",width=45,height=1,command=win7,font=("Courier New",16,'bold'),bg="white")
                  butf7.place(x=5,y=245)
                  butf8=Button(f3,text="Ice Tea                                 ",width=45,height=1,command=win8,font=("Courier New",16,'bold'),bg="white")
                  butf8.place(x=5,y=285)
                  butf9=Button(f3,text="Cinnamon Tea                            ",width=45,height=1,command=win9,font=("Courier New",16,'bold'),bg="white")
                  butf9.place(x=5,y=325)
                  butf10=Button(f3,text="Matcha Tea                              ",width=45,height=1,command=win10,font=("Courier New",16,'bold'),bg="white")
                  butf10.place(x=5,y=365)

          def pizza():
                  def win1():        
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                      l1=Label(f3,text="Margherita             ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      79/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Margherita  -Regular         ",79) ,relief=FLAT) .place(x=650,y=90)
                      r2=Button(f3,text=" Medium      159/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Margherita  -Medium         ",159),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      

                  def win2():         
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                      l1=Label(f3,text="Chilli Pepper             ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      69/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Chilli Pepper  -Regular      ",69),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium      139/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Chilli Pepper  -Medium      ",139),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                     

                  def win3():          
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                      l1=Label(f3,text="Mexican              ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      68/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Mexican  -Regular            ",68),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium      122/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Mexican  -Medium            ",112),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                    
                  def win4():       
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                      l1=Label(f3,text="Farmhouse             ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      99/-     ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Farmhouse  -Regular          ",99),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium      129/-     ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Farmhouse  -Medium          ",129),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      
                  def win5():  
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                    
                      l1=Label(f3,text="Chicken Deluxe            ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      139/-    ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Chicken Deluxe  -Regular   ",139),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium       229/-    ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Chicken Deluxe  -Medium    ",229) ,relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      
                  def win6():    
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
               
                      l1=Label(f3,text="Pepper Barbecue",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      67/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Pepper Barbecue  -Regular    ",67),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium      149/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Pepper Barbecue  -Medium     ",149),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      
                  def win7():      
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
             
                      l1=Label(f3,text="Mushroom            ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      77/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Mushroom  -Regular           ",77),relief=FLAT ).place(x=650,y=90)
                      r2=Button(f3,text=" Medium      140/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Mushroom  -Regular          ",140) ,relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      
                  def win8():         
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
             
                      l1=Label(f3,text="Fresh Delight             ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      59/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Fresh Delight  -Regular      ",59),relief=FLAT ).place(x=650,y=90)
                      r2=Button(f3,text=" Medium      149/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Fresh Delight  -Medium      ",149),relief=FLAT ).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      

                  def win9():        
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
              
                      l1=Label(f3,text="Roasted Chicken           ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      89/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Roasted Chicken  -Regular    ",89),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium      159/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Roasted Chicken  -Medium    ",159),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      
                  def win10():  
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                    
                      l1=Label(f3,text="Double Cheese             ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      79/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Double Cheese  -Regular      ",79),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium      129/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Double Cheese  -Medium      ",129),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      
                  butf1=Button(f3,text="Margherita                             ",width=45,height=1,command=win1,font=("Courier New",16,'bold'),bg="white")
                  butf1.place(x=5,y=5)
                  butf2=Button(f3,text="Chilli Pepper                          ",width=45,height=1,command=win2,font=("Courier New",16,'bold'),bg="white")
                  butf2.place(x=5,y=45)
                  butf3=Button(f3,text="Mexican                                ",width=45,height=1,command=win3,font=("Courier New",16,'bold'),bg="white")
                  butf3.place(x=5,y=85)
                  butf4=Button(f3,text="Farmhouse                              ",width=45,height=1,command=win4,font=("Courier New",16,'bold'),bg="white")
                  butf4.place(x=5,y=125)
                  butf5=Button(f3,text="Chicken Deluxe                         ",width=45,height=1,command=win5,font=("Courier New",16,'bold'),bg="white")
                  butf5.place(x=5,y=165)
                  butf6=Button(f3,text="Pepper Barbecue                        ",width=45,height=1,command=win6,font=("Courier New",16,'bold'),bg="white")
                  butf6.place(x=5,y=205)
                  butf7=Button(f3,text="Mushroom                               ",width=45,height=1,command=win7,font=("Courier New",16,'bold'),bg="white")
                  butf7.place(x=5,y=245)
                  butf8=Button(f3,text="Fresh Delight                          ",width=45,height=1,command=win8,font=("Courier New",16,'bold'),bg="white")
                  butf8.place(x=5,y=285)
                  butf9=Button(f3,text="Roasted Chicken                        ",width=45,height=1,command=win9,font=("Courier New",16,'bold'),bg="white")
                  butf9.place(x=5,y=325)
                  butf10=Button(f3,text="Double Cheese                          ",width=45,height=1,command=win10,font=("Courier New",16,'bold'),bg="white")
                  butf10.place(x=5,y=365)

          def burger():
                  def win1():  
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                      l1=Label(f3,text="McAloo Tikki            ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      42/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("McAloo Tikki  -Regular       ",42),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium      119/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("McAloo Tikki  -Medium       ",119),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      
                     
                  def win2(): 
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                      l1=Label(f3,text="Mexican            ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      45/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Mexican  -Regular            ",45),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium       79/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Mexican  -Medium            ",79),relief=FLAT ).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      

                  def win3():   
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                      l1=Label(f3,text="Chicken Kebab         ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      59/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Chicken Kebab  -Regular      ",59),relief=FLAT ).place(x=650,y=90)
                      r2=Button(f3,text=" Medium      169/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Chicken Kebab  -Medium      ",169),relief=FLAT ).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      
                      
                  def win4():  
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                      l1=Label(f3,text="American Cheese       ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      59/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("American Cheese  -Regular    ",59),relief=FLAT ).place(x=650,y=90)
                      r2=Button(f3,text=" Medium      129/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("American Cheese  -Medium    ",129),relief=FLAT ).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      
                  def win5():  
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                      l1=Label(f3,text="McSpicy Paneer           ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      69/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("McSpicy Paneer  -Regular     ",69),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium      149/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("McSpicy Paneer  -Medium     ",149),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                     
                  def win6():   
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                      l1=Label(f3,text="McSpicy Chicken           ",font=("Courier New",16,'bold')).place(x=650,y=40)
                      r1=Button(f3,text=" Regular      89/-       ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("McSpicy Chicken  -Regular    ",89),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium      139/-       ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("McSpicy Chicken  -Medium    ",139),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      
                  def win7():    
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                      l1=Label(f3,text="Maharaja               ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      110/-     ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Maharaja  -Regular          ",110),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium       220/-     ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Maharaja  -Medium          ",220),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      
                  def win8():        
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                      l1=Label(f3,text="McVeggie              ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular        79/-    ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("McVeggie  -Regular           ",79),relief=FLAT ).place(x=650,y=90)
                      r2=Button(f3,text=" Medium        140/-    ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("McVeggie  -Medium           ",140),relief=FLAT ).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      

                  def win9():  
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                      l1=Label(f3,text="Classic         ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      49/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Classic  -Regular            ",49),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium       99/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Classic  -Medium            ",99),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                     
                  def win10():   
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                      l1=Label(f3,text="Fusion          ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      69/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Fusion  -Regular             ",69),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium      159/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Fusion  -Medium             ",159),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      

                  butf1=Button(f3,text="McAloo Tikki                           ",width=45,height=1,command=win1,font=("Courier New",16,'bold'),bg="white")
                  butf1.place(x=5,y=5)
                  butf2=Button(f3,text="Mexican                                ",width=45,height=1,command=win2,font=("Courier New",16,'bold'),bg="white")
                  butf2.place(x=5,y=45)
                  butf3=Button(f3,text="Chicken Kebab                          ",width=45,height=1,command=win3,font=("Courier New",16,'bold'),bg="white")
                  butf3.place(x=5,y=85)
                  butf4=Button(f3,text="American Cheese Supreme                ",width=45,height=1,command=win4,font=("Courier New",16,'bold'),bg="white")
                  butf4.place(x=5,y=125)
                  butf5=Button(f3,text="McSpicy Paneer                         ",width=45,height=1,command=win5,font=("Courier New",16,'bold'),bg="white")
                  butf5.place(x=5,y=165)
                  butf6=Button(f3,text="McSpicy Chicken                        ",width=45,height=1,command=win6,font=("Courier New",16,'bold'),bg="white")
                  butf6.place(x=5,y=205)
                  butf7=Button(f3,text="Maharaja                               ",width=45,height=1,command=win7,font=("Courier New",16,'bold'),bg="white")
                  butf7.place(x=5,y=245)
                  butf8=Button(f3,text="McVeggie                               ",width=45,height=1,command=win8,font=("Courier New",16,'bold'),bg="white")
                  butf8.place(x=5,y=285)
                  butf9=Button(f3,text="Classic                                ",width=45,height=1,command=win9,font=("Courier New",16,'bold'),bg="white")
                  butf9.place(x=5,y=325) 
                  butf10=Button(f3,text="Fusion                                 ",width=45,height=1,command=win10,font=("Courier New",16,'bold'),bg="white")
                  butf10.place(x=5,y=365)
          def desert():
                  def win1():  
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                      l1=Label(f3,text="Cheese Cake                   ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      30/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Cheese Cake  -Regular        ",30),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium       49/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Cheese Cake  -Medium         ",49),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                     
                    
                  def win2():  
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                      l1=Label(f3,text="Berry Crumble           ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular       25/-     ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Berry Crumble -Regular     ",25),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium        39/-     ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Berry Crumble -Medium      ",39),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      

                  def win3():     
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                      l1=Label(f3,text="Choco Bannoffee          ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      110/-     ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Choco Bannoffee -Regular ",110),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium       125/-     ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Choco Bannoffee -Medium  ",125),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      
                  def win4():
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                      l1=Label(f3,text="Hot Chocolate                ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      32/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Hot Chocolate -Regular   ",32),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium       49/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Hot Chocolate -Medium    ",49),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                 
                  def win5():  
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                      l1=Label(f3,text="Choco Pudding         ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      35/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Choco Pudding -Regular   ",35),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium       67/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Choco Pudding -Medium    ",67),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                  def win6():  
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                      l1=Label(f3,text="Chocolate Mousse             ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      49/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Chocolate Mousse -Regular ",49),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium       52/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Chocolate Mousse -Medium  ",52),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      
                  def win7(): 
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                      l1=Label(f3,text="Snickers Roll               ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      45/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Snickers Roll -Regular     ",45),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium       69/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Snickers Roll -Medium      ",69),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      
                  def win8():
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                      l1=Label(f3,text="Chocolate Brownie               ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      50/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Chocolate Brownie -Regular ",50),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium       79/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Chocolate Brownie -Medium  ",79),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                     
                  def win9():
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                      l1=Label(f3,text="Magnum Truffle                  ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      79/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Magnum Truffle -Regular    ",79) ,relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium      105/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Magnum Truffle -Medium     ",105),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      
                  def win10():
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
           
                      l1=Label(f3,text="Black Forest    ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text="Chocolate       86/-    ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Black Forest  -Chocolate  ",86),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text="Dark Choco     139/-    ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Black Forest  -Dark Choco ",139),relief=FLAT ).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      
                  butf1=Button(f3,text="Cheese Cake                             ",width=45,height=1,command=win1,font=("Courier New",16,'bold'),bg="white")
                  butf1.place(x=5,y=5)
                  butf2=Button(f3,text="AppleBerry Crumble                      ",width=45,height=1,command=win2,font=("Courier New",16,'bold'),bg="white")
                  butf2.place(x=5,y=45)
                  butf3=Button(f3,text="Choco Bannoffee Pie                     ",width=45,height=1,command=win3,font=("Courier New",16,'bold'),bg="white")
                  butf3.place(x=5,y=85)
                  butf4=Button(f3,text="Hot Chocolate                           ",width=45,height=1,command=win4,font=("Courier New",16,'bold'),bg="white")
                  butf4.place(x=5,y=125)
                  butf5=Button(f3,text="Molten Chocolate Pudding                ",width=45,height=1,command=win5,font=("Courier New",16,'bold'),bg="white")
                  butf5.place(x=5,y=165)
                  butf6=Button(f3,text="Chocolate Musse                         ",width=45,height=1,command=win6,font=("Courier New",16,'bold'),bg="white")
                  butf6.place(x=5,y=205)
                  butf7=Button(f3,text="Snickers Roll                           ",width=45,height=1,command=win7,font=("Courier New",16,'bold'),bg="white")
                  butf7.place(x=5,y=245)
                  butf8=Button(f3,text="Chocolate Brownie                       ",width=45,height=1,command=win8,font=("Courier New",16,'bold'),bg="white")
                  butf8.place(x=5,y=285)
                  butf9=Button(f3,text="Magnum Truffle                          ",width=45,height=1,command=win9,font=("Courier New",16,'bold'),bg="white")
                  butf9.place(x=5,y=325)
                  butf10=Button(f3,text="Black Forest Pastery                    ",width=45,height=1,command=win10,font=("Courier New",16,'bold'),bg="white")
                  butf10.place(x=5,y=365)

          def addons():
                  def win1():
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
               
                      l1=Label(f3,text="French Fries             ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular        30/-    ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("French Fries  -Regular     ",30),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Cheese Dip     80/-    ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("French Fries  -Cheese Dip  ",80),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                     
                  def win2():
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
              
                      l1=Label(f3,text="Masala Wedges               ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular         25/-   ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Masala Wedges -Regular    ",25),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Cheese          45/-   ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Masala Wedges -Cheese     ",45),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      
                  def win3():
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
              
                      l1=Label(f3,text="Chicken Strips             ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" 3(Pcs)        69/-     ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Chicken Strips  -3(Pcs)  ",69),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" 6(Pcs)        99/-     ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Chicken Strips  -6(Pcs)  ",99),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      
                  def win4():
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
              
                      l1=Label(f3,text="Garlic Bread               ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular         45/-   ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Garlic Bread -Regular      ",45),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Cheese Stuff    59/-   ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Garlic Bread -Cheese       ",59),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      

                  def win5():            
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")

                      l1=Label(f3,text="Pasta                       ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" White Sauce   120/-    ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Pasta -White Sauce         ",120),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Red Sauce     120/-    ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Pasta -Red Sauce           ",120),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      
                  def win6():            
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")

                      l1=Label(f3,text="Zingy Parcel               ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Veg           39/-     ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Zingy Parcel -Veg          ",39),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" NonVeg        60/-     ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Zingy Parcel -NonVeg       ",60),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      
                  def win7():            
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
                      l1=Label(f3,text="Taco Mexicano              ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Veg           65/-     ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Taco Mexicano -Veg       ",65),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" NonVeg        72/-     ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Taco Mexicano -NonVeg    ",72),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)

                  def win8():
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")
              
                      l1=Label(f3,text="Coke Float                  ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      35/-     ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Coke Float -Regular        ",35),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium       45/-     ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Coke Float -Medium         ",45),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                       
                  def win9():            
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")

                      l1=Label(f3,text="Aloo Wrap                ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      59/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Aloo Wrap  -Regular        ",59),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Cheese       69/-      ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Aloo Wrap  -Cheese         ",69),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                      
                  def win10():
                      qe=Entry(f3,font=("Courier New",16,'bold'),width=6,textvariable=text1).place(x=800,y=170)
                      text1.set("1")    
                      l1=Label(f3,text="Oreo Shake            ",font=("Courier New",16,'bold'),bg="white").place(x=650,y=40)
                      r1=Button(f3,text=" Regular      110/-     ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Oreo Shake -Regular      ",110),relief=FLAT).place(x=650,y=90)
                      r2=Button(f3,text=" Medium       190/-     ",font=("Courier New",16,'bold'),bg="white",command=lambda :add("Oreo Shake -Medium       ",190),relief=FLAT).place(x=650,y=120)
                      q=Label(f3,text="Party Size",font=("Courier New",16,'bold'),bg="white").place(x=650,y=170)
                    

                  butf1=Button(f3,text="French Fries                            ",width=45,height=1,command=win1,font=("Courier New",16,'bold'),bg="white")
                  butf1.place(x=5,y=5)
                  butf2=Button(f3,text="Masala Wedges                           ",width=45,height=1,command=win2,font=("Courier New",16,'bold'),bg="white")
                  butf2.place(x=5,y=45)
                  butf3=Button(f3,text="Chicken Strips                          ",width=45,height=1,command=win3,font=("Courier New",16,'bold'),bg="white")
                  butf3.place(x=5,y=85)
                  butf4=Button(f3,text="Garlic Bread                            ",width=45,height=1,command=win4,font=("Courier New",16,'bold'),bg="white")
                  butf4.place(x=5,y=125)
                  butf5=Button(f3,text="Pasta                                   ",width=45,height=1,command=win5,font=("Courier New",16,'bold'),bg="white")
                  butf5.place(x=5,y=165)
                  butf6=Button(f3,text="Zingy Parcel                            ",width=45,height=1,command=win6,font=("Courier New",16,'bold'),bg="white")
                  butf6.place(x=5,y=205)
                  butf7=Button(f3,text="Taco Mexicano                           ",width=45,height=1,command=win7,font=("Courier New",16,'bold'),bg="white")
                  butf7.place(x=5,y=245)
                  butf8=Button(f3,text="Coke Float                              ",width=45,height=1,command=win8,font=("Courier New",16,'bold'),bg="white")
                  butf8.place(x=5,y=285)
                  butf9=Button(f3,text="Aloo Wrap                               ",width=45,height=1,command=win9,font=("Courier New",16,'bold'),bg="white")
                  butf9.place(x=5,y=325)
                  butf10=Button(f3,text="Oreo Shake                              ",width=45,height=1,command=win10,font=("Courier New",16,'bold'),bg="white")
                  butf10.place(x=5,y=365)




          f2=Frame(data,width=340,height=650,bg='white')
          f2.pack(side=RIGHT,anchor="ne")

          f3=Frame(data,width=955,height=500,bg='white')
          f3.pack(side=LEFT,anchor="sw")

          but1=Button(data,width=67,height=59,bg='white',command=coffee)
          img1=Image.open("D:\COFFEE SHOP\coffee.png")
          pic1=ImageTk.PhotoImage(img1)
          but1.config(image=pic1)
          but1.place(x=220,y=5)
          i1=Label(data,text="Coffee",bg="gray22",font=("Courier New",12,'bold'),fg="white")
          i1.place(x=223 ,y=70)

          but2=Button(data,width=67,height=59,bg='white',command=tea)
          img2=Image.open('D:\COFFEE SHOP\chai.png')
          pic2=ImageTk.PhotoImage(img2)
          but2.config(image=pic2)
          but2.place(x=305,y=5)
          i2=Label(data,text="Tea",bg="gray22",font=("Courier New",12,'bold'),fg="white")
          i2.place(x=322 ,y=70)

          but3=Button(data,width=67,height=59,bg='white',command=pizza)
          img3=Image.open("D:\COFFEE SHOP\pizza.png")
          pic3=ImageTk.PhotoImage(img3)
          but3.config(image=pic3)
          but3.place(x=392,y=5)
          i3=Label(data,text="Pizza",bg="gray22",font=("Courier New",12,'bold'),fg="white")
          i3.place(x=395 ,y=70)

          but4=Button(data,width=67,height=59,bg='white',command=burger)
          img4=Image.open("D:\\COFFEE SHOP\\burgericon.png")
          pic4=ImageTk.PhotoImage(img4)
          but4.config(image=pic4)
          but4.place(x=477,y=5)
          i4=Label(data,text="Burger",bg="gray22",font=("Courier New",12,'bold'),fg="white")
          i4.place(x=479 ,y=70)

          but5=Button(data,width=67,height=59,bg='white',command=desert)
          img5=Image.open("D:\COFFEE SHOP\dessert.png")
          pic5=ImageTk.PhotoImage(img5)
          but5.config(image=pic5)
          but5.place(x=563,y=5)
          i5=Label(data,text="Deserts",bg="gray22",font=("Courier New",12,'bold'),fg="white")
          i5.place(x=566 ,y=70)

          but6=Button(data,width=67,height=59,bg='white',command=addons)
          img6=Image.open("D:\COFFEE SHOP\coc.png")
          pic6=ImageTk.PhotoImage(img6)
          but6.config(image=pic6)
          but6.place(x=650,y=6)
          i6=Label(data,text="Add Ons",bg="gray22",font=("Courier New",12,'bold'),fg="white")
          i6.place(x=650 ,y=70)


          home=Button(f3,width=70,height=52,command=go_to_home)
          h1=Image.open("D:\COFFEE SHOP\home.png")
          hpic=ImageTk.PhotoImage(h1)
          home.config(image=hpic)
          home.place(x=5,y=437)

          send=Button(f3,width=40,height=3,fg="white",bg="gray25",command=sending).place(x=84,y=437)
          s=Label(f3,text="Send",bg="gray25",font=("Courier New",16,'bold'),fg="white")
          s.place(x=200 ,y=450)

          save=Button(f3,width=40,height=3,fg="white",bg="gray25",command=saving).place(x=374,y=437)
          sv=Label(f3,text="Save",bg="gray25",font=("Courier New",16,'bold'),fg="white")
          sv.place(x=480 ,y=450)

          remove=Button(f3,width=40,height=3,bg="gray25",command=re).place(x=664,y=437)
          rm=Label(f3,text="Remove Item(s)",bg="gray25",font=("Courier New",16,'bold'),fg="white")
          rm.place(x=695 ,y=450)

          dt=Label(f2,text=("Date:  "+date),bg="white",font=("Courier New",16,'bold'))
          dt.place(x=1 ,y=589)
          t=Label(f2,text=("Time:   "+tym),bg="white",font=("Courier New",16,'bold'))
          t.place(x=1 ,y=615)
         
          lsb=Listbox(f2,width=30,height=25,bg="white",font=("Courier New",12,'bold'))
          lsb.place(x=0,y=0)
          lsbp=Listbox(f2,width=4,height=25,bg="white",font=("Courier New",12,'bold'))
          lsbp.place(x=290,y=0)
          
          data.mainloop()
     


      


b=""
bp=""
oid=0
orderno=""

def  bill():########### bill page ######
    
          data=Toplevel()
          data.configure(bg="white")
          data.geometry("470x600")
          textin=StringVar()
          global total,amount,gst,dt
          global billprice,billitems
          global dsc
          f1=Frame(data,width=500,height=600,bg='ghostwhite')
          f1.pack(side=LEFT,anchor="se")
          
          
          
          listi=Listbox(f1,width=45,height=15,bg="white",font=("Courier New",12,'bold'),relief=FLAT)
          listi.place(x=0,y=70)
          listp=Listbox(f1,width=4,height=15,bg="white",font=("Courier New",12,'bold'),relief=FLAT)
          listp.place(x=425,y=70)
          lt1=Label(f1,text=" ",font=("Courier New",16,'bold'),fg="black",bg="ghostwhite")
          lt1.place(x=30,y=370)
          lt2=Label(f1,text=" ",font=("Courier New",16,'bold'),fg="black",bg="ghostwhite")
          lt2.place(x=30,y=400)
          lt3=Label(f1,text=" ",font=("Courier New",16,'bold'),fg="black",bg="ghostwhite")
          lt3.place(x=30,y=430)
          lt4=Label(f1,text=" ",font=("Courier New",16,'bold'),fg="black",bg="ghostwhite")
          lt4.place(x=30,y=460)
         
          for i in billitems:
               listi.insert(END,i)
          for j in billprice:
               listp.insert(END,j)
          lt1.configure(text="SUBTOTAL                     "+str(total)) 
          gst=7.75
          amount=total+gst
          amount=amount-(amount*(dsc/100))
          lt2.configure(text="GST(2.5%)                   "+str(gst))
          lt3.configure(text="DISCOUNT                      "+str(dsc)+"%")
          lt4.configure(text="TOTAL                     "+str(round(amount,2)))

          dcount=str(dsc)+"%" 
          q1="insert into orders(TIME,subtotal,discount,GST,total)values('%s','%s','%s','%s','%s')"%(str(tym),str(total),dcount,str(gst),str(round(amount,2)))
          cur.execute(q1)
          con.commit()
          
          
          ##########################################################
          def receipt():  #REci ####
               r=Toplevel()
               r.configure(bg="white")
               r.geometry("450x600")
               
               global billitems,billprice,total,gst,amount,b,bp,oid,orderno,dsc
               q2=("select orno from orders ORDER by orno DESC LIMIT 1")
               cur.execute(q2)
               oid=cur.fetchone()
               orderno=str(oid[0])
               for i in billitems:
                          b=b+"\n"+i
               for j in billprice:
                          bp=bp+"\n"+str(j)
               
               
               rec1=Label(r,text=("CAFE COFFEE BEANS\nG-4,Survey No 207,Phoenix MarketCity,\nViman Nagar,\nPune,Maharashtra-411014\n91-9876788324\nOrder No."+orderno+"\n"+dt),font=("courier new",11),bg="white").place(x=55,y=30)
               rec2=Label(r,text=b,font=("courier new",11),bg="white",justify=LEFT).place(x=55,y=170)             
               rec3=Label(r,text=bp,font=("courier new",11),bg="white",justify=RIGHT).place(x=360,y=170)
               Label(r,text="----------------------------------------",font=("courier new",11),bg="white",justify=RIGHT).place(x=55,y=350)
               rec4=Label(r,text="Subtotal\nGST(2.5%)\nDiscount\nTotal",font=("courier new",11),bg="white",justify=LEFT).place(x=55,y=370)
               rec5=Label(r,text=(str(total)+"\n"+str(gst)+"\n"+str(dsc)+"%"+"\n"+str(round(amount,2))),font=("courier new",11),bg="white",justify=RIGHT).place(x=359,y=370)
               rec4=Label(r,text="THANK YOU!",font=("courier new",11),bg="white",justify=CENTER).place(x=170,y=520)
               Button(r,text="PRINT RECEIPT",font=("courier new",11,"bold"),bg="medium purple",fg="white",relief=RAISED,command=lambda:r.destroy()).place(x=300,y=550)
           
               r.mainloop()
               
          #####################################################     
          def pay():         
                 from tkinter import messagebox
                 messagebox.showinfo("payy","PAYING BILL...")
                 
                 
          def close():
               global billitems,billprice,total,dsc,amount,b,bp
               billitems.clear()
               billprice.clear()
               listi.delete(0,END)
               listi.delete(0,END)
               b=bp=""
               total=amount=dsc=0
               data.destroy()
               
                     
                   
          ###################################################### 
         
          #button for save
          s1=Button(data,width=12,height=2,text="SAVE",bg='black',fg='white',command=receipt)
          s1.place(x=50,y=520) 
          #button for PAY
          e1=Button(data,width=12,height=2,text="PAY",bg='black',fg='white',command=pay)
          e1.place(x=320,y=520)
          #button for going to home page (x)
          x1=Button(data,width=47,height=45,command=close,relief=RAISED) 
          ex=Image.open('D:\\COFFEE SHOP\\exit.png')
          ex1=ImageTk.PhotoImage(ex)
          x1.config(image=ex1)
          x1.place(x=416,y=0)
        

          data.mainloop()



def endofday():
     from tkinter import ttk
     import tkinter 
     o=Toplevel()    
     o.configure(bg="white")
     o.geometry("1230x450")
    
     
     colheading=['ORDER NO.','TIME','SUBTOTAL','DISCOUNT','GST','TOTAL']
     
     tree =ttk.Treeview(o,columns=colheading, show="headings")
     tree.place(x=10,y=70)
     style=ttk.Style()
     style.configure("Treeview.Heading",font=("Courier New",12,'bold'))
     style.configure("Treeview",rowheight=30)
     cur.execute("select * from orders")
     records=cur.fetchall()
     for col in colheading:
                 tree.heading(col,text=col.title())
     for row in records:
                 tree.insert('','end',values=(row[0],row[1],row[2],row[3],row[4],row[5]))
               
              
     
                         
     Label(o,text=str(date)+"                                                                                                     ",font=("Courier New",13,'bold'),bg="royal blue",fg="white",width=120,justify=LEFT).place(x=10,y=30)
     o.mainloop()

    
def customer():
     from tkinter import ttk
     import tkinter 
     cus=Toplevel()    
     cus.configure(bg="white")
     cus.geometry("450x370")
     colheading=['MOBILE NO.','NAME']
     cur.execute("select * from customer")
     records=cur.fetchall()
     tree =ttk.Treeview(cus,columns=colheading, show="headings")
     tree.place(x=20,y=20)
     style=ttk.Style()
     style.configure("Treeview.Heading",font=("Courier New",12,'bold'))
     style.configure("Treeview",rowheight=30)
     
     for col in colheading:
                 tree.heading(col,text=col.title())
     for row in records:
                tree.insert('','end',values=(row[0],row[1]))
     
     
   
     cus.mainloop()

def register():
    
     reg=Toplevel()
     reg.configure(bg="white")
     reg.geometry("440x230")
     var1=IntVar()
     var2=StringVar()
   
     Label(reg,text="Mobile No. ",font=("Courier New",13,'bold'),bg="white").place(x=10,y=30)
     Entry(reg,font=("Courier New",16,'bold'),textvariable=var1,width=15).place(x=140,y=30)
     
     Label(reg,text="Name  ",font=("Courier New",13,'bold'),bg="white").place(x=10,y=90)
     Entry(reg,font=("Courier New",16,'bold'),textvariable=var2,width=15).place(x=140,y=90)
     
     def search():
               
               from tkinter import messagebox
               sea=0
               global dsc
               que1=("select Mno from customer")
               cur.execute(que1)
               
               row=cur.fetchone()
               while row is not None:
                    if var1.get()==row[0]:
                         sea=1
                    row=cur.fetchone()    

               if sea==1:
                    cur.execute("select *from customer where Mno= %d"%var1.get())
                    result=cur.fetchone()
                    con.commit()
                    dsc=30
                    messagebox.showinfo("Delaitls","CUSTOMER NAME : "+str(result[1])+"\nMOBILE NUMBER : "+str(result[0]))
               else:
                    messagebox.showinfo("cust","NOT REGISTERED")
               
     def regis():
           from tkinter import messagebox
           query="insert into customer(Mno,Name)values(%d,'%s')"%(var1.get(),var2.get())
           cur.execute(query)
           con.commit()
           messagebox.showinfo("reg","REGISTERED SUCCESSFULLY!!")
          
                 
     
     Button(reg,width=9,height=2,text="SEARCH",bg='black',fg='white',font=("Courier New",13,'bold'),command=search).place(x=290,y=140)
     Button(reg,width=9,height=2,text="REGISTER",bg='black',fg='white',font=("Courier New",13,'bold'),command=regis).place(x=35,y=140)

     reg.mainloop()
     
img=Image.open('D:\COFFEE SHOP\logo.png')
pic=ImageTk.PhotoImage(img)
p=Label(image=pic)
p.image=pic
p.place(x=0,y=0)

l1=Label(root,text="CAFE COFFEE BEANS",font=("Courier New",40,'bold italic'),fg="tomato4",bg="white")
l1.place(x=135,y=0)
l2=Label(root,text="G-4,Survey No 207,Phoenix MarketCity,\nViman Nagar,\nPune,Maharashtra-411014",font=("Courier New",12,"bold"),fg="MediumPurple4",bg="white")
l2.place(x=190,y=70)

f1=Frame(root,width=215,height=340,bg='BLACK')
f1.pack(side=RIGHT,anchor="se")
f2=Frame(root,width=480,height=340,bg='BLACK')
f2.pack(side=LEFT,anchor="sw")
   
t1=Entry(f1,font=("Courier New",20,'bold'),textvar=textin,width=7,show="*")
t1.place(x=25,y=15)
         

but1=Button(f1,padx=15,pady=14,bd=5,bg='black',fg="white",command=lambda:clickbut(1),text="1",font=("Courier New",12,'bold'))
but1.place(x=25,y=70)

but2=Button(f1,padx=15,pady=14,bd=5,bg='black',fg="white",command=lambda:clickbut(4),text="4",font=("Courier New",12,'bold'))
but2.place(x=25,y=127)

but3=Button(f1,padx=15,pady=14,bd=5,bg='black',fg="white",command=lambda:clickbut(7),text="7",font=("Courier New",12,'bold'))
but3.place(x=25,y=184)

but4=Button(f1,padx=15,pady=14,bd=5,bg='black',fg="white",command=lambda:clickbut(2),text="2",font=("Courier New",12,'bold'))
but4.place(x=80,y=70)

but5=Button(f1,padx=15,pady=14,bd=5,bg='black',fg="white",command=lambda:clickbut(5),text="5",font=("Courier New",12,'bold'))
but5.place(x=80,y=127)

but6=Button(f1,padx=15,pady=14,bd=5,bg='black',fg="white",command=lambda:clickbut(8),text="8",font=("Courier New",12,'bold'))
but6.place(x=80,y=184)

but7=Button(f1,padx=15,pady=14,bd=5,bg='black',fg="white",command=lambda:clickbut(3),text="3",font=("Courier New",12,'bold'))
but7.place(x=135,y=70)

but8=Button(f1,padx=15,pady=14,bd=5,bg='black',fg="white",command=lambda:clickbut(6),text="6",font=("Courier New",12,'bold'))
but8.place(x=135,y=127)

but9=Button(f1,padx=15,pady=14,bd=5,bg='black',fg="white",command=lambda:clickbut(9),text="9",font=("Courier New",12,'bold'))
but9.place(x=135,y=184)

but0=Button(f1,padx=15,pady=14,bd=5,bg='black',fg="white",command=lambda:clickbut(0),text="0",font=("Courier New",12,'bold'))
but0.place(x=80,y=243)

butb=Button(f1,padx=15,pady=14,bd=4,bg='white',fg="white",command=clear,font=("Courier New",12,'bold'),width=40,relief=FLAT)
back=Image.open('D:\\COFFEE SHOP\\back.png')
back1=ImageTk.PhotoImage(back)
butb.config(image=back1)
butb.place(x=141,y=16)







b1=Button(f2,height=80,width=100,padx=2,pady=1,bg="white",command=ord,relief=RAISED,state="disabled")
img1=Image.open('D:\COFFEE SHOP\qorder.png')
pic1=ImageTk.PhotoImage(img1)
b1.config(image=pic1)
b1.place(x=40,y=45)

l1=Label(f2,text=" QUICK ORDER ",padx=3,pady=1,font=("Courier New",9,'bold'),bg="DeepPink3")
l1.place(x=42,y=47)
                

b2=Button(f2,height=80,width=100,text="OPEN ORDER",padx=2,pady=1,bg="white",command=bill,relief=RAISED,state=DISABLED)
img2=Image.open('D:\COFFEE SHOP\editorder.png')
img2.putalpha(190)
pic2=ImageTk.PhotoImage(img2)
b2.config(image=pic2)
b2.place(x=175,y=45)

l2=Label(f2,text=" OPEN ORDER ",padx=4,pady=1,font=("Courier New",8,'bold'),bg="white")
l2.place(x=177,y=46)


b3=Button(f2,height=80,width=100,text="END OF\nTHE DAY",padx=2,pady=1,bg="white",relief=RAISED,state=DISABLED,command=endofday)
img3=Image.open('D:\COFFEE SHOP\dailyorders.png')
img3.putalpha(190)
pic3=ImageTk.PhotoImage(img3)
b3.config(image=pic3)
b3.place(x=315,y=45)

l3=Label(f2,text=" END OF DAY",padx=3,pady=1,font=("Courier New",9,'bold'),bg="white")
l3.place(x=317,y=47)


b4=Button(f2,height=80,width=100,text="CANCEL ORDER",padx=2,pady=1,bg="white",command=cl,relief=RAISED,state=DISABLED)
img4=Image.open('D:\COFFEE SHOP\cancel.png')
img4.putalpha(190)
pic4=ImageTk.PhotoImage(img4)
b4.config(image=pic4)
b4.place(x=40,y=155)


l4=Label(f2,text=" CANCEL ORDER",padx=4,pady=0,font=("Courier New",9,'bold'),bg="white")
l4.place(x=40,y=220)

b5=Button(f2,height=80,width=100,text="CUSTOMER",padx=2,pady=1,bg="white",relief=RAISED,state=DISABLED,command=customer)
img5=Image.open('D:\COFFEE SHOP\cust.png')
img5.putalpha(190)
pic5=ImageTk.PhotoImage(img5)
b5.config(image=pic5)
b5.place(x=175,y=155)

l5=Label(f2,text="   CUSTOMER  ",padx=4,pady=0,font=("Courier New",8,'bold'),bg="white")
l5.place(x=177,y=220)

b6=Button(f2,height=80,width=100,text="CONFIG REG",padx=2,pady=1,bg="white",relief=RAISED,state=DISABLED,command=register)
img6=Image.open('D:\COFFEE SHOP\data.png')
img6.putalpha(190)
pic6=ImageTk.PhotoImage(img6)
b6.config(image=pic6)
b6.place(x=315,y=155)

l6=Label(f2,text="CONGIFURE REGISTER",padx=3,pady=1,font=("Courier New",7,'bold'),bg="white")
l6.place(x=317,y=220)


     
root.mainloop()
