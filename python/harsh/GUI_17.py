import pandas as pd
import gdown
import string
from tkinter import *
import random
import math
import telerivet
import datetime
root=Tk()
STUDENR_PROFILE,STUDENT_ACCOUNT,ADMIN_ACCOUNT,ID_PASS,BACKGROUND,BACKGROUND1,CHANGE,ATTENDANCE_NAME,DS,ADE,OOP,MATHEMATICS_3,DS_GT,BACK1='STUDENR_PROFILE', 'STUDENT_ACCOUNT', 'ADMIN_ACCOUNT', 'ID_PASS', 'BACKGROUND', 'BACKGROUND1', 'CHANGE', 'ATTENDANCE_NAME', 'DS', 'ADE', 'OOP', 'MATHEMATICS_3', 'DS_GT', 'BACK'
#====================================================================================================
info1=['Roll No          :','Enrollment No    :','Name of Student  :','Student Mo       :','Parents Mo       :','E-mail           :']
info=['Roll No.','Enrollment No.','Name of Student','Student Mo.','Parents Mo.','E-mail','ID','PASSWORD','SHORT NAME']
#====================================================================================================
try:
    file=pd.read_csv(ATTENDANCE_NAME)
    df = pd.DataFrame(file)
except FileNotFoundError:
    ATTENDANCE_NAME_ID='173CRHoU5VXyZUsQJLEt98Z-cXNHMfFU9'
    ATTENDANCE_NAME_URL=f'https://drive.google.com/uc?id={ATTENDANCE_NAME_ID}'
    gdown.download(ATTENDANCE_NAME_URL, ATTENDANCE_NAME, quiet=False)
    file=pd.read_csv(ATTENDANCE_NAME)
    df = pd.DataFrame(file)
#====================================================================================================
try:
    admin_id_pass=pd.read_csv(ID_PASS)
    df1 = pd.DataFrame(admin_id_pass)
    id_pass=df1.loc[0].tolist()
except FileNotFoundError:
    ID_PASS_ID='1GcjwRr3AsV54iYggRKW3w5hv7056VNKx'
    ID_PASS_URL=f'https://drive.google.com/uc?id={ID_PASS_ID}'
    gdown.download(ID_PASS_URL, ID_PASS, quiet=False)
    admin_id_pass=pd.read_csv(ID_PASS)
    df1 = pd.DataFrame(admin_id_pass)
    id_pass=df1.loc[0].tolist()
#====================================================================================================
def fill_presenty(subject):
  global df3,save_attendance
  if subject=='DS':
    subject1=DS
    try:
        save_attendance=pd.read_csv(DS)
        df3=pd.DataFrame(save_attendance)
    except TclError:
        DS_ID='1oHy1mgBmvrcAykXd56RihuWF5UBdWldz'
        DS_URL=f'https://drive.google.com/uc?id={DS_ID}'
        gdown.download(DS_URL, DS, quiet=False)
        save_attendance=pd.read_csv(DS)
        df3=pd.DataFrame(save_attendance)
  elif subject=='DS&GT':
    subject1=DS_GT
    try:
        save_attendance=pd.read_csv(DS_GT)
        df3=pd.DataFrame(save_attendance)
    except TclError:
        DS_GT_ID='1KasAo63yKQxYPA6vg-7eOQYaiuSwHvOx'
        DS_GT_URL=f'https://drive.google.com/uc?id={DS_GT_ID}'
        gdown.download(DS_GT_URL, DS_GT, quiet=False)
        save_attendance=pd.read_csv(DS_GT)
        df3=pd.DataFrame(save_attendance)
  elif subject=='ADE':
    subject1=ADE
    try:
      save_attendance=pd.read_csv(ADE)
      df3=pd.DataFrame(save_attendance)
    except TclError:
      ADE_ID='1aL4Ya38p6AXzs84iox2erJrsrZfoBxkZ'
      ADE_URL=f'https://drive.google.com/uc?id={ADE_ID}'
      gdown.download(ADE_URL, ADE, quiet=False)
      save_attendance=pd.read_csv(ADE)
      df3=pd.DataFrame(save_attendance)
  elif subject=='OOP':
    subject1=OOP
    try:
      save_attendance=pd.read_csv(OOP)
      df3=pd.DataFrame(save_attendance)
    except TclError:
      OOP_ID='1v7aSNYtzhpYpBqFf8Lc_HUuLYclUBCWu'
      OOP_URL=f'https://drive.google.com/uc?id={OOP_ID}'
      gdown.download(OOP_URL, OOP, quiet=False)
      save_attendance=pd.read_csv(OOP)
      df3=pd.DataFrame(save_attendance)
  elif subject=='MATHEMATICES 3':
    subject1=MATHEMATICS_3
    try:
      save_attendance=pd.read_csv(MATHEMATICS_3)
      df3=pd.DataFrame(save_attendance)
    except TclError:
      MATHEMATICS_3_ID='1kfFWyL27fUgCw3CxsPnGdr_cEG1nk7bd'
      MATHEMATICS_3_URL=f'https://drive.google.com/uc?id={MATHEMATICS_3_ID}'
      gdown.download(MATHEMATICS_3_URL, MATHEMATICS_3, quiet=False)
      save_attendance=pd.read_csv(MATHEMATICS_3)
      df3=pd.DataFrame(save_attendance)
  now=datetime.datetime.now()
  send_date=now.strftime('%d-%m-%Y')
  var=[]
  var1=0
  for var2 in range(len(df3)):
    if var2==int(d[var1]) and var1<=len(d):
      e='A'
      var.append(e)
      var1=var1+1
    else:
      e='P'
      var.append(e)
  df3[send_date]=var
  df3.to_csv(subject1,index=False)
#====================================================================================================
def send_message(info11,info12,mobile_no1):
  now=datetime.datetime.now()
  send_date=now.strftime('%d-%m-%Y')
  send_time=now.strftime('%I-%M-%p')
  mobile_no='9822301670'
  api = telerivet.API('sO8Wr_17yEd1S86Bx2AZ9VCGbeKZSrcqNMsQ')
  project = api.initProjectById('PJ82fb59bb562c1a26')
  if info11!='':
    project.sendMessage(to_number=mobile_no,content=f"YOUR OTP TO CHANGE PASSSWORD IS {info11[:3]}-{info11[3:]}")
  else:
    project.sendMessage(to_number=mobile_no,content=f"YOUR CHILD IS NOT PRESENT IN THE LECTURE OF {info12} ON {send_date} {send_time}")
  print("Message sent successfully!")
#====================================================================================================
def subject_code():
  global p5,Subject_code
  for widget in root.winfo_children():
    widget.destroy()
  try:
    p5=PhotoImage(file=CHANGE)
    Label(root,image=p5).place(x=0,y=0)
  except TclError:
    CHANGE_ID='1JxJy69Womo3eDCikqvzz3ZD6F2gvbrBV'
    CHANGE_URL=f'https://drive.google.com/uc?id={CHANGE_ID}'
    gdown.download(CHANGE_URL, CHANGE, quiet=False)
    p5=PhotoImage(file=CHANGE)
    Label(root,image=p5).place(x=0,y=0)
  Subject_code=StringVar()
  Entry(root,textvariable=Subject_code,font="Georgia 15").place(x=200,y=200)
  Button(root,text="START ATTENDANCE",command=presenty).place(x=250,y=250)
  Button(root,font="Georgia 12",image=BACK,command=main).place(x=35,y=320)
#====================================================================================================
def presenty():
  if Subject_code.get() == '1':
    subject = 'DS'
  elif Subject_code.get() == '2':
    subject = 'DS&GT'
  elif Subject_code.get() == '3':
    subject = 'MATHEMATICS 3'
  elif Subject_code.get() == '4':
    subject = 'OOP'
  elif Subject_code.get() == '5':
    subject = 'ADE'
  else:
    return 
  root.destroy()
  def send_alert():
    alert_no=df[info[4]]
    var=0
    otp=''
    for var1 in range(len(alert_no)):
      if var<len(d) and var1==int(d[var]) and alert_no[var1]!='N.A.':
        number=alert_no.get()
        send_message(otp,subject,number)
        var=var+1
        var1=0
    fill_presenty(subject)
  def submit():
    global d
    d=[]
    for index in range (len(b)):
      if b[index].get():
        continue
      else:
        var_info=str(index+1)
        d.append(var_info)
    send_alert()
  def on_mouse_wheel(event):
    if event.delta > 0:
      canvas.yview_scroll(-1, "units")
    else:
      canvas.yview_scroll(1, "units")
  root1 = Tk()
  root1.geometry("400x400")
  var_name = 'box'
  global b
  b = []
  for var in range(0,len(df)):
    var_name_1 = var_name + str(var)
    b.append(var_name_1)
  name = df['SHORT NAME']
  canvas = Canvas(root1)
  canvas.pack(side=LEFT, fill=BOTH, expand=True)
  scrollbar = Scrollbar(root1, orient="vertical", command=canvas.yview)
  scrollbar.pack(side=RIGHT, fill="y")
  canvas.configure(yscrollcommand=scrollbar.set)
  frame = Frame(canvas)
  canvas.create_window((0, 0), window=frame, anchor="nw")
  for var, present in enumerate(range(len(df))):
    b[present] = IntVar()
    Label(frame, text=name[present]).grid(row=var, column=0, sticky="w", padx=10, pady=5)
    Checkbutton(frame, variable=b[present], font="Georgia 12").grid(row=var, column=1, padx=10, pady=5)
  frame.update_idletasks()
  canvas.config(scrollregion=canvas.bbox("all"))
  root1.bind_all("<MouseWheel>", on_mouse_wheel)
  Button(root1, text="SUBMIT \nATTENDANCE", command=submit, font="Georgia 12", relief='solid').place(x=250,y=320)
  root1.mainloop()
#====================================================================================================
def register():
  for widget in root.winfo_children():
    widget.destroy()
  def login():
    def complete():
      a=df[info[6]]
      var_1=0
      var_2=0
      for var in range (len(a)):
        if id.get()==a[var] or id.get()=='':
          Label(root,text='USER NAME IS NOT AVAILABLE',font="Georgia 10",background="white",foreground="red").place(x=200,y=100)
          return
        else:
          Label(root,text='                                                                                  ',font="Georgia 10",background="white").place(x=200,y=100)
          var_1=1
      if password.get()!=conform_password.get() or password.get()=='':
        Label(root,text='PASSWORD NOT MATCH',font="Georgia 12",background="white",foreground="red").place(x=200,y=175)
        return
      else:
        Label(root,text='                                                                                  ',font="Georgia 12",background="white").place(x=200,y=175)
        var_2=1
      if var_1==1 and var_2==1:
        new_a=df[info[1]]
        length=len(new_a)
        new_list=[(length+1)]
        for var in range(5):
          if new[var].get()!='':
            var_info=new[var].get()
          else:
            var_info='N.A.'
          new_list.append(var_info)
        new_list.append(id.get())
        new_list.append(password.get())
        new_list.append('')
        df.loc[length]=new_list
        df.to_csv(ATTENDANCE_NAME,index=False)
        main()
    Label(root,image=p4).place(x=0,y=0)
    Label(root,text='CREATE USER NAME',font="Georgia 12",background="white").place(x=200, y=50)
    id=StringVar()
    Entry(root,textvariable=id,font="Georgia 12").place(x=200,y=75)
    Label(root,text="PASSWORD",font="Georgia 12",background="white").place(x=200, y=125)
    password=StringVar()
    Entry(root,textvariable=password,font="Georgia 12").place(x=200,y=150)
    Label(root,text="CONFORM PASSWORD",font="Georgia 12",background="white").place(x=200, y=200)
    conform_password=StringVar()
    Entry(root,textvariable=conform_password,font="Georgia 12").place(x=200,y=225)   
    Button(root,text='FINISH',command=complete).place(x=200,y=250) 
    Button(root,font="Georgia 12",image=BACK,command=main).place(x=35,y=320)
  global p4,new
  try:
    p4=PhotoImage(file=BACKGROUND1)
    Label(root,image=p4).place(x=0,y=0)
  except TclError:
    BACKGROUND1_ID='1wUqU0ElYD1hDsExtGfk5-ZcWkkSdy7Ay'
    BACKGROUND1_URL=f'https://drive.google.com/uc?id={BACKGROUND1_ID}'
    gdown.download(BACKGROUND1_URL, BACKGROUND1, quiet=False)
    p4=PhotoImage(file=BACKGROUND1)
    Label(root,image=p4).place(x=0,y=0)
  new=['ENROLLMENT NO','NAME','SUTDENT MOBILE NO','PARENTS MOBIME NO','EMAIL ID','ID','PASSWORD']
  for var in range (5):
    Label(root,text=new[i],font="Georgia 12",background="white").place(x=50,y=50+(25*i))
  for var in range (5):
    new[var]=StringVar()
    Entry(root,textvariable=new[i],font="Georgia 12").place(x=250,y=50+(i*25))
  Label(root,text="CAPITAL LETTER ONLY",font="Georgia 8",background="white",foreground="red").place(x=450,y=75)
  Button(root,text="REGISTER",command=login,font="Georgia 12").place(x=200,y=200)
  Button(root,font="Georgia 12",image=BACK,command=main).place(x=35,y=320)
#====================================================================================================
def delete_info():
  global df,i
  for var in range(i,len(df[info[0]])-1):
    df.loc[var]=df.loc[var+1]
    df.loc[var,'Roll No.']=var+1
  df=df.drop(len(df)-1)
  df.to_csv(ATTENDANCE_NAME,index=False)  
#====================================================================================================
def forgot_password_admin():
  id_pass=df1.loc[0].tolist()
  def change_admin_password(otp):
    for widget in root.winfo_children():
      widget.destroy()
    global p5
    try:
        p5=PhotoImage(file=CHANGE)
        Label(root,image=p5).place(x=0,y=0)
    except TclError:
        CHANGE_ID='1JxJy69Womo3eDCikqvzz3ZD6F2gvbrBV'
        CHANGE_URL=f'https://drive.google.com/uc?id={CHANGE_ID}'
        gdown.download(CHANGE_URL, CHANGE, quiet=False)
        p5=PhotoImage(file=CHANGE)
        Label(root,image=p5).place(x=0,y=0)
    Label(text="ENTER OTP",font="Georgia 12 bold",background="#333333",foreground="white").place(x=200,y=130)
    def verify():
      if otp==otp_entry.get():
        def changepassword():
          id_pass[1]=new_password.get()
          df1.loc[0]=id_pass
          df1.to_csv(ID_PASS,index=False)
          admin_login()
        Label(text="ENTER PASSWORD HERE",font="Georgia 12 bold",background="#333333",foreground="white").place(x=200,y=220)
        new_password=StringVar()
        Entry(root,textvariable=new_password,font="Georgia 12 bold").place(x=200,y=250)
        Button(root,text='CHANGE',command=changepassword).place(x=200,y=280)
      else:
        Label(root,text="RE-ENTER OTP",background="#333333",foreground="red",font="Georgia 12 bold").place(x=300,y=190)
    otp_entry=StringVar()
    Entry(root,textvariable=otp_entry,font="Georgia 12 bold").place(x=200,y=160)
    Button(root,text="SUBMIT",command=verify).place(x=200,y=190)
    Button(root,font="Georgia 12",image=BACK,command=admin_login).place(x=35,y=320)
  data='0123456789'
  length=len(data)
  otp=''
  mess=''
  number=''
  for var_unused in range(6):
    otp+=data[math.floor(random.random()*length)]
  send_message(otp,mess,number)
  change_admin_password(otp)
#====================================================================================================
def forgot_password_student():
  def change_student_password():
    b=df[info[3]]
    for var in range (len(b)):
      if b[var]==number_entry.get():
        global var1
        var1=var
        a=''
        data='0123456789'
        length=len(data)
        otp=''
        for var_unused in range(0,6):
          otp+=data[math.floor(random.random()*length)]
        number=number_entry.get()
        send_message(otp,a,number)
        break
    for widget in root.winfo_children():
      widget.destroy()
    def verify():
      if otp==otp_entry.get():
        def changepassword():
          df.loc[var1,info[7]]=new_password.get()
          df.to_csv(ATTENDANCE_NAME,index=False)
          student_login()
        Label(text="ENTER PASSWORD HERE",font="Georgia 12 bold",background="#333333",foreground="white").place(x=200,y=220)
        new_password=StringVar()
        Entry(root,textvariable=new_password,font="Georgia 12 bold").place(x=200,y=250)
        Button(root,text='CHANGE',command=changepassword).place(x=200,y=280)
      else:
        Label(root,text="RE-ENTER OTP",background="#333333",foreground="red",font="Georgia 12 bold").place(x=300,y=190)
    Label(root,image=p5).place(x=0,y=0)
    Label(text="ENTER OTP",font="Georgia 12 bold",background="#333333",foreground="white").place(x=200,y=130)
    otp_entry=StringVar()
    Entry(root,textvariable=otp_entry,font="Georgia 12 bold").place(x=200,y=160)
    Button(root,text="SUBMIT",command=verify).place(x=200,y=190)      
    Button(root,font="Georgia 12",image=BACK,command=student_login).place(x=35,y=320)
  for widget in root.winfo_children():
    widget.destroy()
  global p5
  try:
    p5=PhotoImage(file=CHANGE)
    Label(root,image=p5).place(x=0,y=0)
  except TclError:
    CHANGE_ID='1JxJy69Womo3eDCikqvzz3ZD6F2gvbrBV' 
    CHANGE_URL=f'https://drive.google.com/uc?id={CHANGE_ID}'
    gdown.download(CHANGE_URL, CHANGE, quiet=False)
    p5=PhotoImage(file=CHANGE)
    Label(root,image=p5).place(x=0,y=0)
  Label(text="ENTER MOBILE NO",font="Georgia 12 bold",background="#333333",foreground="white").place(x=200,y=130)
  number_entry=StringVar()
  Entry(root,textvariable=number_entry,font="Georgia 12 bold").place(x=200,y=160)
  Button(root,text="SEND OTP",font="Georgia 12 bold",command=change_student_password).place(x=200,y=200)
  Button(root,font="Georgia 12",image=BACK,command=student_login).place(x=35,y=320)
#====================================================================================================
def student_login():
  for widget in root.winfo_children():
    widget.destroy()
  def check():
    global i
    i=-1
    id_search=df[info[6]]
    for index in range (len(id_search)):
      if id.get()==id_search[index]:
        break
    password_search=df.loc[index].tolist()
    if password.get()==password_search[7]:
      for widget in root.winfo_children():
        widget.destroy()
      i=index
      print_info()
      Button(text="EDIT",command=student_edit,font="Georgia 12",background="white").place(x=105,y=190)
      Button(root,font="Georgia 12",image=BACK,command=student_login).place(x=35,y=320)
    else:
      #👇👇
      custom_box = Toplevel(root)
      custom_box.title("Custom Message Box")
      custom_box.geometry("300x90")
      custom_box.resizable(False, False)
      Label(custom_box, text="INCORRECT ID PASSWORD",font="Georgia 12",foreground="red").place(x=40,y=10)
      def custom_action():
        forgot_password_student()  
        custom_box.destroy()
      def cancel_action():
        custom_box.destroy()
      Button(custom_box, text="CHANGE PASSWORD", command=custom_action).place(x=10,y=40)
      Button(custom_box, text="RETRY", command=cancel_action).place(x=220,y=40)
      #☝️☝️
  Label(root,image=photo).place(x=0,y=0)
  global p1
  try:
    p1=PhotoImage(file=STUDENT_ACCOUNT)
    Label(root,image=p1,borderwidth=0).place(x=270,y=75)
  except TclError:
    STUDENT_ACCOUNT_ID='1eI5F5_eZCNwXrf0uwloVOLB77AOBMvav'
    STUDENT_ACCOUNT_URL=f'https://drive.google.com/uc?id={STUDENT_ACCOUNT_ID}'
    gdown.download(STUDENT_ACCOUNT_URL, STUDENT_ACCOUNT, quiet=False)
    p1=PhotoImage(file=STUDENT_ACCOUNT)
    Label(root,image=p1,borderwidth=0).place(x=270,y=75)
  Label(text="STUDENT ID::",font="Georgia 12",background="white").place(x=200, y=200)
  Label(text="PASSWORD::",font="Georgia 12",background="white").place(x=200,y=265)
  id=StringVar()
  password=StringVar()
  identry=Entry(root,textvariable=id,font="Georgia 15",background="white").place(x=200, y=225)
  passentry=Entry(root,textvariable=password,show="•",font="Georgia 15",background="white")
  passentry.place(x=200, y=290)
  Button(root,font="Georgia 12",image=BACK,command=main).place(x=35,y=320)
  def toggle_password():
      if show_password_var.get():
          passentry.config(show="")
          return
      else:
          passentry.config(show="•")
          return
  show_password_var = IntVar()
  Checkbutton(root,variable=show_password_var,background="white",command=toggle_password).place(x=450,y=310)
  Button(text="       LOGIN      ",command=check,font="Georgia 12 bold",background="white").place(x=260,y=330)
#====================================================================================================
def student_edit():
  def submit():
    global entry_vars
    change = []
    for var in range(6):
      var_info = entry_vars[var].get()
      change.append(var_info)
    for var in range(6):
      if change[var] == '':
        change[var] = df.loc[i, info[var]]
    for var in range(6, 9):
      change.append(df.loc[i, info[var]])
    df.loc[i] = change
    df.to_csv(ATTENDANCE_NAME, index=False)
    for widget in root.winfo_children():
      widget.destroy()
    print_info()
    Button(text="CLOSE", command=root.destroy, font="Georgia 12", background="white").grid(row=7, column=1)
    Button(root,font="Georgia 12",image=BACK,command=student_login).place(x=35,y=320)
  global entry_vars
  entry_vars = [StringVar() for _ in range(6)]
  b = df.loc[i].tolist()
  for var in range(6):
    if b[var] == '' or b[var] == 'N.A.' or (var > 1 and var != 4):
      Entry(root, textvariable=entry_vars[var], font="Georgia 10", background="white").place(x=470, y=40 + (25 * var))
  Button(root, text="EDIT INFO", command=submit, font="Georgia 12", background="white").place(x=470, y=190)
  Button(root,font="Georgia 12",image=BACK,command=student_login).place(x=35,y=320)
#====================================================================================================
def print_info():
  global p3,p4
  a=df.loc[i].tolist()
  try:
    p4=PhotoImage(file=BACKGROUND1)
    Label(root,image=p4).place(x=0,y=0)
  except TclError:
    BACKGROUND1_ID='1wUqU0ElYD1hDsExtGfk5-ZcWkkSdy7Ay'
    BACKGROUND1_URL=f'https://drive.google.com/uc?id={BACKGROUND1_ID}'
    gdown.download(BACKGROUND1_URL, BACKGROUND1, quiet=False)
    p4=PhotoImage(file=BACKGROUND1)
    Label(root,image=p4).place(x=0,y=0)
  try:
    p3=PhotoImage(file=STUDENR_PROFILE)
    Label(root,image=p3).place(x=0,y=45)
  except TclError:
    STUDENR_PROFILE_ID='1azPgiH4Yr-h3Z6nqfQs3b1pXSRy0Ob3I'
    STUDENR_PROFILE_URL=f'https://drive.google.com/uc?id={STUDENR_PROFILE_ID}'
    gdown.download(STUDENR_PROFILE_URL, STUDENR_PROFILE, quiet=False)
    p3=PhotoImage(file=STUDENR_PROFILE)
    Label(root,image=p3).place(x=0,y=45)
  for var in range (6):
    Label(text=info1[var],font="Georgia 12",background="white").place(x=105,y=40+(25*var))
    Label(text=a[var],font="Georgia 12",background="white").place(x=230,y=40+(25*var))
#====================================================================================================
def admin_login():
  for widget in root.winfo_children():
    widget.destroy()
  def check():
    if id.get()==id_pass[0] and password.get()==id_pass[1]:
      for widget in root.winfo_children():
        widget.destroy()
      edit()
    else:
      custom_box = Toplevel(root)
      custom_box.title("Custom Message Box")
      custom_box.geometry("300x90")
      custom_box.resizable(False, False)
      Label(custom_box, text="INCORRECT ID PASSWORD",font="Georgia 12",foreground="red").place(x=40,y=10)
      def custom_action():
        forgot_password_admin()  
        custom_box.destroy()
      def cancel_action():
        custom_box.destroy()
      Button(custom_box, text="CHANGE PASSWORD", command=custom_action).place(x=10,y=40)
      Button(custom_box, text="RETRY", command=cancel_action).place(x=220,y=40)
  Label(root,image=photo).place(x=0,y=0)
  global p2
  try:
    p2=PhotoImage(file=ADMIN_ACCOUNT)
    Label(root,image=p2,borderwidth=0).place(x=270,y=75)
  except TclError:
    ADMIN_ACCOUNT_ID='1NvOv3PxQXBfPKrBny2dW7XNzQtl-T0ak'
    ADMIN_ACCOUNT_URL=f'https://drive.google.com/uc?id={ADMIN_ACCOUNT_ID}'
    gdown.download(ADMIN_ACCOUNT_URL, ADMIN_ACCOUNT, quiet=False)   
    p2=PhotoImage(file=ADMIN_ACCOUNT)
    Label(root,image=p2,borderwidth=0).place(x=270,y=75)
  Label(text="USER ID::",font="Georgia 12",background="white").place(x=205, y=200)
  Label(text="PASSWORD::",font="Georgia 12",background="white").place(x=205,y=265)
  id=StringVar()
  password=StringVar()
  identry=Entry(root,textvariable=id,font="Georgia 15",relief='solid',borderwidth=2).place(x=205, y=225)
  passentry=Entry(root,textvariable=password,show="•",font="Georgia 15",relief='solid',borderwidth=2)
  passentry.place(x=205, y=290)
  def toggle_password():
    if show_password_var.get():
        passentry.config(show="")
        return
    else:
        passentry.config(show="•")
        return
  show_password_var = IntVar()
  Checkbutton(root,variable=show_password_var,background="white",command=toggle_password).place(x=455,y=310)
  Button(text="       LOGIN      ",command=check,font="Georgia 12 bold",relief='solid').place(x=260,y=330)
  Button(root,font="Georgia 12",image=BACK,command=main).place(x=35,y=320)
#====================================================================================================
def edit():
  def change1():
    change=[]
    for h in range (6):
      b=entry1[h].get()
      change.append(b)
    for h in range(6):
      if change[h]=='':
        change[h]=df.loc[i,info[h]]   
    for l in range(6,9):
      change.append(df.loc[i,info[l]])
    df.loc[i]=change
    df.to_csv(ATTENDANCE_NAME,index=False)
    for widget in root.winfo_children():
      widget.destroy()
    print_info()
    Button(root,font="Georgia 12",image=BACK,command=edit).place(x=35,y=320)
    Button(root,text="COLSE",command=root.destroy,font="Georgia 12",background="white").place(x=355,y=190)
  def searching(option):
    search=df[info[option]]
    global i
    i=-1
    for index in range (len(search)):
      if ((var_info.lower()) in (search[index].lower()) or var_info==search[index]) :
        i=index
        print_info()
        break
    if i!=-1:
      Button(root,text="EDIT",command=admin_change,font="Georgia 12",background="white").place(x=105,y=190)
      Button(root,text="DELETE",command=delete_info,font="Georgia 12",background="white").place(x=355,y=190)
      Button(root,font="Georgia 12",image=BACK,command=edit).place(x=35,y=320)
    else:
      print("not found")
  def find():
    global var_info
    for var in range(6):
      if entry[var].get()!='':
        var_info=entry[var].get()
        for widget in root.winfo_children():
          widget.destroy()
        searching(var)
  for widget in root.winfo_children():
    widget.destroy()
  global p4
  try:
    p4=PhotoImage(file=BACKGROUND1)
    Label(root,image=p4).place(x=0,y=0)
  except TclError:
    BACKGROUND1_ID='1wUqU0ElYD1hDsExtGfk5-ZcWkkSdy7Ay'
    BACKGROUND1_URL=f'https://drive.google.com/uc?id={BACKGROUND1_ID}'
    gdown.download(BACKGROUND1_URL, BACKGROUND1, quiet=False)
    p4=PhotoImage(file=BACKGROUND1)
    Label(root,image=p4).place(x=0,y=0)
  for var in range (6):
    Label(text=f"SEARCH BY {info1[var]}",font="Georgia 12",background="white").place(x=105,y=40+(25*var))
  Label(text='SEARCH STUDENT BY FOLLOWING OPTION',font="Georgia 12 bold",background="white").grid(row=0,column=1)
  global entry
  entry=['rool_no','en_no','name','student_number','parent_number','email']
  for var in range (6):
    entry[var]=StringVar()
    Entry(root,textvariable=entry[var],font="Georgia 10",background="white").place(x=370,y=40+(25*var))
  Button(root,text="SEARCH",command=find,font="Georgia 12",background="white").place(x=370,y=190)
  Button(root,font="Georgia 12",image=BACK,command=main).place(x=35,y=320)
  def admin_change():
    global entry1
    entry1=['rool_no1','en_no1','name1','student_number1','parent_number1','email1']
    for var in range (6):
      entry1[var]=StringVar()
      Entry(root,textvariable=entry1[var],font="Georgia 10",background="white").place(x=470,y=40+(25*var))
    Button(root,text="APPLY",command=change1,font="Georgia 12",background="white").place(x=470,y=190)  
#====================================================================================================
def main():
  for widget in root.winfo_children():
    widget.destroy()
  root.geometry("650x400")
  global photo,BACK
  try:
    photo=PhotoImage(file=BACKGROUND)
    Label(root,image=photo).place(x=0,y=0)
  except TclError:
    BACKGROUND_ID='1sHX34MwZq0iqUSxbNp36kkt6eHqMFJWX'
    BACKGROUND_URL=f'https://drive.google.com/uc?id={BACKGROUND_ID}'
    gdown.download(BACKGROUND_URL, BACKGROUND, quiet=False)
  root.title("Project Report: Attendance Management System")
  Button(text="  ADMIN  LOGIN  \nEDIT THE INFORMATION(ADMIN)",font="Georgia 12",command=admin_login,background="skyblue",relief='solid').place(x=180,y=100)
  Button(text="STUDENT LOGIN \n EDIT THE INFORMATIOM(STUDENT)",font="Georgia 12",command=student_login,background="skyblue",relief='solid').place(x=165,y=160)
  Button(text="           REGESTER           ",font="Georgia 12",command=register,background="skyblue",relief='solid').place(x=220,y=220)
  Button(text="           ATTENDACE           ",font="Georgia 12",command=subject_code,background="skyblue",relief='solid').place(x=215,y=265)
  try:
    BACK=PhotoImage(file=BACK1)
    Button(root,font="Georgia 12",image=BACK,command=root.destroy).place(x=35,y=320)
  except TclError:
    BACK_ID='1SsLBuo1v0JdqPEjOzY0I6UfILjaDqtfE'
    BACK_URL=f'https://drive.google.com/uc?id={BACK_ID}'
    gdown.download(BACK_URL,BACK1, quiet=False)
    BACK=PhotoImage(file=BACK1)
    Button(root,font="Georgia 12",image=BACK,command=root.destroy).place(x=35,y=320)
  root.minsize(650,400)
if __name__ == "__main__":
    main()
root.mainloop()