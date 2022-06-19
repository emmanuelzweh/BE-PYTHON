
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import right
from PIL import ImageTk, Image as image
from tkinter import filedialog
from all_frame import *


app = Tk()
app.config(background='white')
app.geometry('1000x800')
app.resizable(0,0)

app.config(bg='black')
app.title("G-Note")

################### DECLARING GLOBAL VARIABLE ################################




############################## DASHBOARD MENU ##########################

menu_frame = Frame(app, bg='white', width=230, height=800, border=5)
menu_frame.grid(row=0, column=0)

border_frame_1 = Frame(app, bg='orange', width=5, height=700)
border_frame_1.grid(row=0, column=1)


#################### TOP MENU FRAME
top_bar_frame = Frame(app, width=770, height=50, bg='white')
top_bar_frame.place(relx=0.228, rely=0)

top_bar_left_frame = Frame(app, width=5, height=50, bg='orange')
top_bar_left_frame.place(relx=0.229, rely=0)

####################### DISPLAY FRAME ################################
display_frame = Frame(app, bg='white', width=770, height=795)
display_frame.place(relx=0.235, rely=0.06)


def home():
    home_frame = Frame(display_frame, bg='white', width=770, height=795)
    home_frame.place(relx=0, rely=0.02)
    director_dashbord = Label(display_frame,text='DASHBOARD DIRECTEUR ECOLE', bg='white', fg='orange', font=(('Times New Romans'), 20, 'bold'))
    director_dashbord.place(relx=0.05, rely=0.04)

    ################ STUDENTS STATISTICS ###################
    total_student_frame = Frame(display_frame, width=320, height=200, bg='orange')
    total_student_frame.place(relx=0.02, rely=0.15)
    content_lab = Label(total_student_frame, text='ETUDIANT VALIDE', bg='orange', fg='black', font=('Times New Romans', 8, 'bold'))
    content_lab.place(relx=0.1, rely=0.26)
    total_lab = Label(total_student_frame, text=8, bg='orange', fg='black', font=('Times New Romans', 15, 'bold'))
    total_lab.place(relx=0.2, rely=0.5)
    icon_frame1 = Frame(total_student_frame, width=180, height=200, bg='black')
    icon_frame1.place(relx=0.5, rely=0)

    ##################### STUDENT IMAGE SYMBOL ################
    global icon
    icon = image.open('student.jpg')
    icon_resize = icon.resize((180,200))
    new_icon = ImageTk.PhotoImage(icon_resize)
    pic_label = Label(icon_frame1, image=new_icon)
    pic_label.pack()

    ################ PROFESSEURS STATISTICS ###################
    total_professors_frame = Frame(display_frame, width=300, height=200, bg='orange')
    total_professors_frame.place(relx=0.53, rely=0.15)
    content_lab = Label(total_professors_frame, text='ETUDIANT PAS VALIDE', bg='orange', fg='black', font=('Times New Romans', 8, 'bold'))
    content_lab.place(relx=0.05, rely=0.26)
    total_lab = Label(total_professors_frame, text=8, bg='orange', fg='black', font=('Times New Romans', 15, 'bold'))
    total_lab.place(relx=0.25, rely=0.5)
    icon_frame_1 = Frame(total_professors_frame, width=180, height=200, bg='gray')
    icon_frame_1.place(relx=0.55, rely=0)

    ##################### STUDENT IMAGE SYMBOL ################
    icon_1 = image.open('professors.jpg')
    icon_1_resize = icon_1.resize((180,200))
    new_icon_1 = ImageTk.PhotoImage(icon_1_resize)
    pic_label = Label(icon_frame_1, image=new_icon_1)
    pic_label.pack()
####### SETTING MENU ITEMS #############################################
########################

def notification():
    notfication_frame = Frame(display_frame, bg='white', width=770, height=795)
    notfication_frame.place(relx=0, rely=0.05)

    greeting = Label(notfication_frame, text="LISTES DES NOTIFICATIONS", bg='white', font=('Times New Romans', 13, 'bold'))
    greeting.place(relx=0.3, rely=0.05)

    ################ GETTING NOTIFICATION LISTS #################
    notifcations_listbox = Listbox(notfication_frame, width=80, height=20, bg='white', font=('Times New Romans', 10, 'bold'))
    notifcations_listbox.place(relx=0.13, rely=0.1)

####################### SEE STUDENTS FUNCTION #######################
def voirMoy():
    see_students_frame = Frame(display_frame, bg='white', width=770, height=795)
    see_students_frame.place(relx=0, rely=0.05)

    greeting = Label(see_students_frame, text="VOIR CLASSES", bg='white', font=('Times New Romans', 13, 'bold'))
    greeting.place(relx=0.25, rely=0.05)

    all_classes = ["Classe 1", "Classe 2", "Classe 3", "Classe 4"]
    select_class_label = Label(see_students_frame, text='CLASSE', font=("Times New Romans", 10, 'bold'), bg='white')
    select_class_label.place(relx=0.02, rely=0.11)
    select_class_options = ttk.Combobox(see_students_frame,value=all_classes, width=50)
    select_class_options.place(relx=0.15, rely=0.11)



    tv = ttk.Treeview(see_students_frame)
    tv['columns'] = ('Matricule', 'Name', 'Prenom', 'Moyenne')
    tv.column('#0', width=0, stretch=NO)
    tv.column('Matricule', anchor=CENTER, width=120)
    tv.column('Name', anchor=CENTER, width=120)
    tv.column('Prenom', anchor=CENTER, width=120)
    tv.column('Moyenne', anchor=CENTER, width=120)
    

    tv.heading('#0', text='', anchor=CENTER)
    tv.heading('Matricule', text='Matricule', anchor=CENTER)
    tv.heading('Name', text='Name', anchor=CENTER)
    tv.heading('Prenom', text='Prenom', anchor=CENTER)
    tv.heading('Moyenne', anchor=CENTER, text='Moyenne #')

    tv.place(relx=0.02, rely=0.2)


right_menu_border = tin_menu_border(menu_frame)
right_menu_border.place(relx=0.03, rely=0.1)

logo_frame = Frame(menu_frame, width=80, height=60, bg='black')
logo_frame.place(relx=0.01,rely=0.01)

###### LOGO
logo = image.open('image.jpg')
logo_resize = logo.resize((80,60))
new_logo = ImageTk.PhotoImage(logo_resize)
pic_label = Label(logo_frame, image=new_logo)
pic_label.pack()

dashbord = Label(menu_frame, text='DASHBOARD', fg='orange', bg='white', font=('andriod', 13, 'bold'))
dashbord.place(relx=0.4, rely=0.04)

############### menu buttons
create_btn = Button(menu_frame, text='NOTIFICATION',width=15, bg='orange', fg='black', activebackground='orange', font=("Times New Romans", 10, 'bold'), pady=5, padx=4, command=notification)
create_btn.place(relx=0.23, rely=0.13)

attribution_btn = Button(menu_frame, text='VOIR MOYENNES',width=15, bg='orange', fg='black', activebackground='orange', font=("Times New Romans", 10, 'bold'), pady=5, padx=4, command=voirMoy)
attribution_btn.place(relx=0.23, rely=0.19)



#################### TOP MENU FRAME
top_bar_frame = Frame(app, width=770, height=50, bg='white')
top_bar_frame.place(relx=0.228, rely=0)

############### TOP BAR FRAME CONTENTS
profile_frame = Frame(top_bar_frame, width=70, height=50, bg='white')
profile_frame.place(relx=0.9,rely=0)

####### PROFILE PICTURE
profile = image.open('profile.jpg')
profile_resize = profile.resize((70,50))
new_profile = ImageTk.PhotoImage(profile_resize)
pic_label = Label(profile_frame, image=new_profile)
pic_label.pack()

################ username
username_lab = Label(top_bar_frame, text='USERNAME', bg='white', fg='orange', font=('Times New Romans', 12, 'bold'))
username_lab.place(relx=0.73, rely=0.3)

top_bar_left_frame = Frame(app, width=5, height=50, bg='orange')
top_bar_left_frame.place(relx=0.229, rely=0)

strict_line = Frame(top_bar_frame, width=2, height=30, bg='orange')
strict_line.place(relx=0.68, rely=0.28)

mail_btn = Button(top_bar_frame, text='Home', width=8, bg='orange', fg='black', activebackground='orange', font=('Times New Romans', 10, 'bold'), pady=3, padx=4,command=home)
mail_btn.place(relx=0.50,rely=0.28)


############################ CALLING HOME ###############################
home()




display_top_border_frame = Frame(display_frame, bg='orange', width=770, height=3)
display_top_border_frame.place(relx=0, rely=0)


app.mainloop()