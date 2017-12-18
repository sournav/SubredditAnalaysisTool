from tkinter import *
import praw
import threading
import ast
from threading import Thread
import sentiment_mod as s
client_id_user=''
client_s_user=''
name_user=''
pwd=''
n=0
k=0
words='a'
t=0
state=0
state2=0
kvar=1
    


#window
def window0():
    def click():
        
        if var1.get()==1:
            file=open('login_info.txt').read().splitlines()
            file[0]="1"
            if textentry.get()!="":
                file[1]=textentry.get()
            if textentry2.get()!="":
                file[2]=textentry2.get()
            if textentry3.get()!="":
                file[3]=textentry3.get()
            if textentry4.get()!="":
                file[4]=textentry4.get()
            print(var1)
            open('login_info.txt','w').write('\n'.join(file))
        if var1.get()==0:
            file=open('login_info.txt').read().splitlines()
            file[0]="0"
            open('login_info.txt','w').write('\n'.join(file))
        global client_id_user
        client_id_user=textentry.get()
        global client_s_user
        client_s_user=textentry2.get()
        global name_user
        name_user=textentry3.get()
        global pwd
        pwd=textentry4.get()
        global n
        n=1
        global k
        k=1
        window0.destroy()
    
    window0=Tk();
    window0.title("Subreddit Analsys for Mods")
    window0.minsize(width=400, height=400)
    #entry
    
    
    Label(window0,text="Client ID:  ").grid(row=0)
    textentry = Entry(window0,width=20, bg="white")
    textentry.grid(row=0,column=1,sticky=W)
    Label(window0,text="Client Secret:  ").grid(row=1)
    textentry2= Entry(window0,width=20, bg="white")
    textentry2.grid(row=1,column=1,sticky=W)
    Label(window0,text="Username:  ").grid(row=2)
    textentry3= Entry(window0,width=20, bg="white")
    textentry3.grid(row=2,column=1,sticky=W)
    Label(window0,text="Password:  ").grid(row=3)
    textentry4= Entry(window0,width=20, bg="white")
    textentry4.config(show="*")
    textentry4.grid(row=3,column=1,sticky=W)
    #Button 1
    button1=Button(window0,text="SUBMIT",width=6, command=click)
    button1.grid(row=4,column=1,sticky=W,pady=4)
    text=open('login_info.txt').read().splitlines();
    
    if text[0]=="1":
        textentry.insert(0,text[1])
        textentry2.insert(0,text[2])
        textentry3.insert(0,text[3])
        textentry4.insert(0,text[4])
    
    var1=IntVar()
    remember=Checkbutton(window0, text="Remember me", variable=var1)
    remember.grid(row=5,column=1, sticky=W)

    mainloop()
    print(client_id_user)
def window2():
    if k==1:
        
        mainloop()
def window1():
    if k==1:
        def click2():
            words=textentry.get()
            file=open('Data_SAMs.txt','w')
            file.write("bob")
            file.close()
            lines = open('Data_SAMs.txt').read().splitlines()
            
            lines[0]=words
            open('Data_SAMs.txt','w').write('\n'.join(lines))
        def click3():
            global t
            t=1
            lines = open('Data_SAMs.txt').read().splitlines()
            
            lines[0]='bobdededededeeddddeee'
            open('Data_SAMs.txt','w').write('\n'.join(lines))
            window2.destroy()
            window1.destroy()
                   
        window1=Tk();
        window1.title("Subreddit Analsys for Mods")
        window1.minsize(width=400, height=300)
        global textentry_w1
        textentry = Entry(window1,width=20, bg="white")
        textentry.grid(row=0,column=1,sticky=W)
        
        
        button1=Button(window1,text="SUBMIT",width=6, command=click2)
        button1.grid(row=4,column=1,sticky=W,pady=4)
        button2=Button(window1,text="Exit",width=6, command=click3)
        button2.grid(row=1,column=2,sticky=W,pady=4)

        window2=Tk();
        window2.title("Live Sentiment Monitor")
        window2.minsize(width=400, height=400)
        i=50
        status_rect1=Canvas(window2, width=i, height=i)
        status_rect1.place(x=125,y=120,width=i,height=i)
        status_rect2=Canvas(window2, width=i, height=i)
        status_rect2.place(x=225,y=120,width=i,height=i)
        Label(window2,text=" Subredit\nMonitor").place(x=117,y=80)
        Label(window2,text="Word\nMonitor").place(x=219,y=80)
        textout1=Text(master=window2)
        textout1.place(x=125,y=175,width=50,height=20)
        textout1.config(state=DISABLED)
        textout2=Text(master=window2)
        textout2.place(x=225,y=175,width=50,height=20)
        textout2.config(state=DISABLED)
        file2 = open('Data_SAMs2.txt','r')
        state=file2.read().splitlines()
        

            
       
        def uper():
            
            global state
            textout1.config(state=NORMAL)
            textout1.delete(1.0, END)
            textout1.insert(1.0,state)
            textout1.config(state=DISABLED)
            if state<0:
               status_rect1.create_rectangle(0, 0, 50, 50, fill="red")
               
            else:
               status_rect1.create_rectangle(0, 0, 50, 50, fill="green")

            global state2
            textout2.config(state=NORMAL)
            textout2.delete(1.0, END)
            textout2.insert(1.0,state2)
            textout2.config(state=DISABLED)

            if state2<0:
               
               status_rect2.create_rectangle(0, 0, 50, 50, fill="red")
            else:
               
               status_rect2.create_rectangle(0, 0, 50, 50, fill="green")


            window1.after(590,uper)
        uper()
        
        mainloop()
            
       

def stream():
        reddit=praw.Reddit(client_id=client_id_user,
                       client_secret=client_s_user,
                       username=name_user,
                       password=pwd,
                       user_agent='bob1')
        subreddit=reddit.subreddit('all')
        cnt=1
        
        while 1>0:
            
            for comment in subreddit.stream.comments():
                    
                    try:
                              
                        
                            file = open('Data_SAMs.txt','r')
                            text = file.read()
                            file.close()
                            if text=='bobdededededeeddddeee':
                                kvar=2
                            else:
                                kvar=1
                            text2=''+text+''
                            global state
                            sentiment_val,confidence = s.sentiment(comment.body)
                            if sentiment_val=='neg':
                                
                                state-=1
                                
                            else:
                                
                                state+=1
                            
                                
                            if kvar==1:
                                if any(s in comment.body for s in (text,text2)):
                                       global state2
                                       if sentiment_val=='neg':
                                           state2-=1
                                       else:
                                           state2+=1
                                       print(text);
                                       print(state2)
                                       print(comment.body)
                                       continue
                    except Exception as e:
                        pass

if __name__ == '__main__':
    

    window0()
  
    Thread(target = window1).start()
    Thread(target = stream).start()
    
