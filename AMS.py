# Client Code

from tkinter import *
import tkinter.messagebox
import time
import sys
import socket

# Login Screen

get=None

user=None

student_login_frame=None
student_password_entry=None
student_username_entry=None

display_frame=None
dashboard_button_1=None

def show_student_record():
    showrecord_frame=Frame(display_frame, width=650, height=500,bg='#FFFFFF')
    showrecord_frame.place(x=0,y=0)
    showrecord_frame.tkraise()
    headings=Label(showrecord_frame,bg='white',text="Attendance Summary\n"+user[0]+" - "+user[1],justify=LEFT)
    headings.place(x=0,y=0)
    t="storage/student_records/"+user[1].rstrip()+".csv"
    print(t)
    subjects={}
    p = Listbox(showrecord_frame, width=100, height=327, bd=0, bg='black', fg='white', font="Candara 12 bold")
    fr=open(t,'r')
    for l in fr:
        line=l.split(",")
        if(line[0] not in subjects):
            subjects[line[0]]=[0,0]
        subjects[line[0]][1]+=1
        if(line[2].rstrip()=='P'):
            subjects[line[0]][0]+=1
    p.place(x=0, y=45)

    for key,value in subjects.items():
        perc=value[0]/value[1]*100
        perc_s=str(round(perc,2))+"%"
        line2 = str(key)+"\t"+str(value[0])+"/"+str(value[1])+"\t"+perc_s
        p.insert(END,line2)    
    
    fr.close()
    
    #back = Button(showrecord_frame, image=img20, command=home,highlightthickness=0)
    #back.place(x=560, y=-10)
    #tkinter.messagebox.showerror("ERROR","File is Empty")

def student_portal():
    dashboard_frame=Frame(student_login_frame,width=250,height=500,bg='#1C2739')
    dashboard_frame.place(x=0,y=0)
    dashboard_frame.tkraise()
    dashboard_label=Label(dashboard_frame,image=img5,bg='#1C2739')
    dashboard_label.place(x=5,y=5)
    divider_logo=Label(dashboard_frame,image=img9,bg='#1C2739')
    divider_logo.place(x=0,y=60)
    dashboard_button_2 = Button(dashboard_frame, image=img7,bd=0,bg='#1C2739', command=show_student_record)
    dashboard_button_2.place(x=-30, y=150)
    dashboard_button_3 = Button(dashboard_frame, image=img8,bd=0,bg='#1C2739', command=student_login)
    dashboard_button_3.place(x=10, y=220)
    global display_frame
    display_frame=Frame(student_login_frame,width=650,height=500,bg='#EBF2F8')
    display_frame.place(x=250,y=0)
    display_frame.tkraise()
    ned_logo=Label(display_frame,image=img3,bg='#EBF2F8')
    ned_logo.place(x=-180,y=-200)
    sp_logo=Label(display_frame,image=img4,bg='#EBF2F8')
    sp_logo.place(x=150,y=175)

    #Student password validation
def student_authorize(event):
    '''fr = open('storage/student_db.csv', 'r')
    flag=0
    for student in fr:
        sd = student.split(",")
        print(sd)
        if student_username_entry.get() == sd[1] and student_password_entry.get()==sd[2].rstrip():
            flag = 1
            break
    if flag == 1:
        global user
        user=sd
        student_portal()
    fr.close()
    '''
    global user
    user=['Yash Pradhan','PES1201700262','pass']
    student_portal()


#Student login
def student_login():
    global student_login_frame
    student_login_frame = Frame(student_admin_frame, width=900, height=500, bg='#EBF2F8')
    student_login_frame.place(x=0, y=0)
    student_login_frame.tkraise()
    student_icon = Label(student_login_frame, image=img15, bd=0, bg='#EBF2F8')
    student_icon.place(x=370, y=10)
    username_label = Label(student_login_frame, text='Username', font=('Berlin Sans FB', 16), bg='#EBF2F8')
    username_label.place(x=405, y=200)
    global student_username_entry
    student_username_entry = Entry(student_login_frame, bg='white', relief='sunken', highlightcolor='#D2E0F1',highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    student_username_entry.place(x=350, y=240)
    password_label = Label(student_login_frame, text='Password', font=('Berlin Sans FB', 16), bg='#EBF2F8')
    password_label.place(x=405, y=280)
    global student_password_entry
    student_password_entry = Entry(student_login_frame, bg='white', show='*', relief='sunken', highlightcolor='#D2E0F1',highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    student_password_entry.place(x=350, y=320)
    student_password_entry.bind('<Return>', student_authorize)
    login_button = Button(student_login_frame, image=img24, bd=0, bg='#EBF2F8')
    login_button.bind('<Button-1>',student_authorize)
    login_button.place(x=357, y=380)
    cancel_button = Button(student_login_frame, image=img14, bd=0, bg='#EBF2F8', command=student_exit)
    cancel_button.place(x=357, y=430)


var3=None
checks=None

#Update Attendance
def update_attendance():
    global checks
    s = socket.socket()
    s.connect(("localhost",9999))
    for check in checks:
        fname="storage/student_records/"+check[0].rstrip()+'.csv'
        #fw=open(fname,'a+')
        if(check[1].get()):
            # Course_Code,Date,P/A
            #with open(fname,'a+',encoding='utf-8') as fw:
            #    fw.write(user[2]+","+time.strftime("%Y-%m-%d")+","+"P"+"\n")
            msg=user[2]+","+time.strftime("%Y-%m-%d")+","+"P"+"\n"
            msg=fname+";"+msg+";;"
            s.send(msg.rstrip().encode())
        else:
            msg=user[2]+","+time.strftime("%Y-%m-%d")+","+"A"+"\n"
            msg=fname+";"+msg+";;"
            s.send(msg.rstrip().encode())
    s.close()
    checks = None
    admin_portal()
    

#Mark students
def admin_attendance_mark():
    admin_attendance_mark=Frame(admin_display_frame, width=650, height=500)
    admin_attendance_mark.place(x=0,y=0)
    global var3
    sec=var3.get()+" Sec"
    lb1 = Label(admin_attendance_mark,text=sec)
    lb1.place(x=0,y=0)
    fname="storage/class_records/"+var3.get()+"_section.csv"
    fp = open(fname)
    x1=0
    y1=30
    global checks
    checks=[]
    for student in fp:
        cvar = IntVar()
        s=student.split(",")
        #s_label=Label(admin_attendance_mark,text=s[0]+" - "+s[1],font=('Berlin Sans FB',16),bg='#EBF2F8')
        #s_label.place(x=x1,y=y1)
        c = Checkbutton(admin_attendance_mark,text=s[1]+" "+s[0]+"\n",variable=cvar)
        c.place(x=x1,y=y1)
        checks.append((s[1],cvar))
        y1+=60
    write_attendance=Button(admin_attendance_mark,text="Submit",command=update_attendance,bd=0,bg='#EBF2F8')
    write_attendance.place(x=0,y=y1)

#Admin Choose Section
def admin_record():
    admin_record_frame=Frame(admin_display_frame, width=650, height=500)
    admin_record_frame.place(x=0,y=0)
    global var3
    optionList = ('G', 'H')
    lb1 = Label(admin_record_frame,text="Record attendance for a class")
    lb1.place(x=0,y=0)
    lb2 = Label(admin_record_frame,text="Choose Section")
    lb2.place(x=0,y=30)
    var3 = StringVar()
    var3.set(optionList[0])
    d_menu = OptionMenu(admin_record_frame, var3, *optionList)
    d_menu.config(font=('calibri', (20)), width=20, fg='blue', indicatoron=0, bd=0,bg='#EBF2F8')
    d_menu.place(x=0, y=50)
    get_admin_record=Button(admin_record_frame,text="Go",command=admin_attendance_mark,bd=0,bg='#EBF2F8')
    get_admin_record.place(x=0,y=80)


admin_display_frame=None

#Admin Home Screen
def admin_portal():
    admin_dashboard_frame = Frame(admin_login_frame, width=250, height=500, bg='#1C2739')
    admin_dashboard_frame.place(x=0, y=0)
    admin_dashboard_frame.tkraise()
    dashboard_label = Label(admin_dashboard_frame, image=img5, bg='#1C2739')
    dashboard_label.place(x=5, y=5)
    divider_logo = Label(admin_dashboard_frame, image=img9, bg='#1C2739')
    divider_logo.place(x=0, y=60)
    dashboard_button_1 = Button(admin_dashboard_frame, image=img6, bd=0, bg='#1C2739', command=admin_record)
    dashboard_button_1.place(x=0, y=120)
    dashboard_button_2 = Button(admin_dashboard_frame, image=img8, bd=0, bg='#1C2739', command=admin_login)
    dashboard_button_2.place(x=10, y=200)
    global admin_display_frame
    admin_display_frame = Frame(admin_login_frame, width=650, height=500)
    admin_display_frame.place(x=250, y=0)
    admin_display_frame.tkraise()
    pes_logo = Label(admin_display_frame, image=img3)
    wlcm_msg="Welcome "+user[4]+"!\n\n"+"Course Code: "+user[2]+"\n"+"Course Title: "+user[3]
    cc = Label(admin_display_frame,text=wlcm_msg)
    cc.place(x=150,y=10)
    pes_logo.place(x=0, y=30)
    admin_logo = Label(admin_display_frame, image=img19)
    admin_logo.place(x=200, y=230)


#For pressing back
def student_exit():
    main_window()

def admin_exit():
    main_window()

#Username and password fields for admin
admin_username_entry=None 
admin_password_entry=None 

def admin_authorize(event):
    fr = open('storage/admin_db.csv', 'r')
    flag=0
    for admin in fr:
        ad = admin.split(",")
        if admin_username_entry.get() == ad[0] and admin_password_entry.get()==ad[1]:
            flag = 1
            break
    if flag == 1:
        global user
        user=ad
        admin_portal()
    fr.close()
    
admin_login_frame=None

def admin_login():
    global admin_login_frame
    admin_login_frame=Frame(student_admin_frame,width=900,height=500,bg='#EBF2F8')
    admin_login_frame.place(x=0,y=0)
    admin_login_frame.tkraise()
    admin_icon=Label(admin_login_frame,image=img13,bd=0,bg='#EBF2F8')
    admin_icon.place(x=370,y=10)
    username_label=Label(admin_login_frame,text='Username',font=('Berlin Sans FB',16),bg='#EBF2F8')
    username_label.place(x=405,y=200)
    global admin_username_entry
    admin_username_entry=Entry(admin_login_frame,bg='white',relief='sunken',highlightcolor='#D2E0F1',highlightthickness=1,highlightbackground='#D8D6D7',font=('Tw Cen MT',14))
    admin_username_entry.place(x=350,y=240)
    password_label = Label(admin_login_frame, text='Password', font=('Berlin Sans FB', 16), bg='#EBF2F8')
    password_label.place(x=405, y=280)
    global admin_password_entry
    admin_password_entry = Entry(admin_login_frame, bg='white',show='*', relief='sunken', highlightcolor='#D2E0F1',highlightthickness=1,highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    admin_password_entry.place(x=350, y=320)
    admin_password_entry.bind('<Return>',admin_authorize)
    login_button=Button(admin_login_frame,image=img24,bd=0,bg='#EBF2F8')
    login_button.bind('<Button-1>',admin_authorize)
    login_button.place(x=357,y=380)
    cancel_button=Button(admin_login_frame,image=img14,bd=0,bg='#EBF2F8',command=admin_exit)
    cancel_button.place(x=357,y=430)


student_admin_frame=None

def main_window():
    global student_admin_frame
    student_admin_frame = Frame(root, width=900, height=500,bg="#EBF2F8")
    student_admin_frame.place(x=0, y=0)
    main_logo_image=Label(student_admin_frame,image=img23,bg='#EBF2F8')
    main_logo_image.place(x=200,y=50)
    black_button_student = Button(student_admin_frame,image=img11, bd=0, command=student_login,bg="#EBF2F8")
    black_button_student.place(x=100, y=300)
    black_button_teacher = Button(student_admin_frame,image=img12, bd=0, command=admin_login,bg="#EBF2F8")
    black_button_teacher.place(x=500, y=300)



# Starting the Window

root=Tk()
root.geometry("900x500")
root.title("Student Attendance System")

img1= PhotoImage(file='assets/media/black-button-student.png')
img2= PhotoImage(file='assets/media/black-button-teacher.png')
img3=PhotoImage(file='assets/media/pes_logo_trans.png')
img4=PhotoImage(file='assets/media/student_portal-logo.png')
img5=PhotoImage(file='assets/media/dashboard-logo.png')
img6=PhotoImage(file='assets/media/attendance-logo.png')
img7=PhotoImage(file='assets/media/view-records-logo.png')
img8=PhotoImage(file='assets/media/logout-logo.png')
img9=PhotoImage(file='assets/media/divider-logo.png')
img10=PhotoImage(file='assets/media/heading-seperator.png')
img11=PhotoImage(file='assets/media/student-login.png')
img12=PhotoImage(file='assets/media/admin-login.png')
img20=PhotoImage(file='assets/media/back-button2.png')
img21=PhotoImage(file='assets/media/show-record-button.png')
img22=PhotoImage(file='assets/media/main-logo.png')
img23=PhotoImage(file='assets/media/logo-eAttendance.png')
img24=PhotoImage(file='assets/media/login-button.png')
img13=PhotoImage(file='assets/media/admin-icon.png')
img14=PhotoImage(file='assets/media/cancel-button.png')
img15=PhotoImage(file='assets/media/student-icon.png')
img16=PhotoImage(file='assets/media/dropdown.png')
img17=PhotoImage(file='assets/media/take-attendance.png')
img18=PhotoImage(file='assets/media/back-button.png')
img19=PhotoImage(file='assets/media/admin-portal-logo.png')
photo=PhotoImage(file='assets/media/test.png')

main_window()

root.mainloop()
