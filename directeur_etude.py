import profile
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import right
from PIL import ImageTk, Image as image
from tkinter import filedialog
from all_frame import *
import sqlite3 as sql

app = Tk()
app.config(background='white')
app.geometry('1000x800')
app.title("G-Note")
app.resizable(0,0)
app.config(bg='black')

################################# DECLARING GLOBAL VARIABLES #################
icon = image.open('student.jpg')
icon_1 = image.open('professors.jpg')
icon_2 = image.open('classroom.jpg')
icon_3 = image.open('grades.png')

################# form variable #######################
matricule = IntVar()
st_nom = StringVar()
prenom = StringVar()
numero_p = StringVar()
numero_tutor = StringVar()
student_photo = StringVar()

################# Database functions #################
# def insertStudent():
#     conn = sql.connect("gnote_base.db")
#     myCursor = conn.cursor()
#     matricule = 'Null'
#     nom = st_nom.get()
#     prenom = prenom.get()
#     numero_pa = numero_p.get()
#     numero_tu = numero_tutor.get()
#     photo = student_photo

#     if nom == "" and prenom == "" and numero_pa == ""and numero_tutor == "":
#         print('erreur')
    # myCursor.executemany('INSERT INTO Etudiant VALUES (?, ?, ?, ?, ?, ?);',matricule,nom,prenom,numero_pa,numero_pa,photo)
    # conn.commit()
    # conn.close



####################### DISPLAY FRAME ################################
display_frame = Frame(app, bg='white', width=770, height=795)
display_frame.place(relx=0.235, rely=0.07)

######## HOME FUNCTION
def home():
    home_frame = Frame(display_frame, bg='white', width=770, height=795)
    home_frame.place(relx=0, rely=0.02)
    director_dashbord = Label(display_frame,text='DASHBOARD DIRECTEUR DES ETUDES', bg='white', fg='orange', font=(('Times New Romans'), 20, 'bold'))
    director_dashbord.place(relx=0.05, rely=0.04)

    ################ STUDENTS STATISTICS ###################
    total_student_frame = Frame(display_frame, width=320, height=200, bg='orange')
    total_student_frame.place(relx=0.02, rely=0.15)
    content_lab = Label(total_student_frame, text='STUDENTS', bg='orange', fg='black', font=('Times New Romans', 12, 'bold'))
    content_lab.place(relx=0.1, rely=0.26)
    total_lab = Label(total_student_frame, text=8, bg='orange', fg='black', font=('Times New Romans', 15, 'bold'))
    total_lab.place(relx=0.2, rely=0.5)
    icon_frame1 = Frame(total_student_frame, width=180, height=200, bg='black')
    icon_frame1.place(relx=0.5, rely=0)

    ##################### STUDENT IMAGE SYMBOL ################
    global icon
    icon_resize = icon.resize((180,200))
    new_icon = ImageTk.PhotoImage(icon_resize)
    pic_label = Label(icon_frame1, image=new_icon)
    pic_label.pack()

    ################ PROFESSEURS STATISTICS ###################
    total_professors_frame = Frame(display_frame, width=300, height=200, bg='orange')
    total_professors_frame.place(relx=0.53, rely=0.15)
    content_lab = Label(total_professors_frame, text='PROFESSEURS', bg='orange', fg='black', font=('Times New Romans', 13, 'bold'))
    content_lab.place(relx=0.05, rely=0.26)
    total_lab = Label(total_professors_frame, text=8, bg='orange', fg='black', font=('Times New Romans', 15, 'bold'))
    total_lab.place(relx=0.25, rely=0.5)
    icon_frame_1 = Frame(total_professors_frame, width=180, height=200, bg='gray')
    icon_frame_1.place(relx=0.55, rely=0)

    ##################### STUDENT IMAGE SYMBOL ################
    global icon_1
    icon_1_resize = icon_1.resize((180,200))
    new_icon_1 = ImageTk.PhotoImage(icon_1_resize)
    pic_label = Label(icon_frame_1, image=new_icon_1)
    pic_label.pack()

    ####################### TOTAL CLASS STATISTICS ###########################
    total_class_frame = Frame(display_frame, width=320, height=200, bg='orange')
    total_class_frame.place(relx=0.02, rely=0.46)
    content_lab = Label(total_class_frame, text='CLASSES', bg='orange', fg='black', font=('Times New Romans', 13, 'bold'))
    content_lab.place(relx=0.15, rely=0.26)
    total_lab = Label(total_class_frame, text=8, bg='orange', fg='black', font=('Times New Romans', 15, 'bold'))
    total_lab.place(relx=0.25, rely=0.5)
    icon_frame_2 = Frame(total_class_frame, width=180, height=200, bg='black')
    icon_frame_2.place(relx=0.5, rely=0)

    ########################### CLASS IMAGE SYMBOL ###########################
    global icon_2
    icon_2_resize = icon_2.resize((180,200))
    new_icon_2 = ImageTk.PhotoImage(icon_2_resize)
    pic_label = Label(icon_frame_2, image=new_icon_2)
    pic_label.pack()

    ################################## MATARIALS STATISTICS ######################
    total_materials_frame = Frame(display_frame, width=300, height=200, bg='orange')
    total_materials_frame.place(relx=0.54, rely=0.46)
    content_lab = Label(total_materials_frame, text='GRADES', bg='orange', fg='black', font=('Times New Romans', 13, 'bold'))
    content_lab.place(relx=0.15, rely=0.26)
    total_lab = Label(total_materials_frame, text=8, bg='orange', fg='black', font=('Times New Romans', 15, 'bold'))
    total_lab.place(relx=0.25, rely=0.5)
    icon_frame_3 = Frame(total_materials_frame, width=180, height=200, bg='gray')
    icon_frame_3.place(relx=0.49, rely=0)

    ############################# MATERIALS IMAGE SYMBOL #################
    global icon_3
    icon_3 = image.open('grades.png')
    icon_3_resize = icon_3.resize((180,200))
    new_icon_3 = ImageTk.PhotoImage(icon_3_resize)
    pic_label = Label(icon_frame_3, image=new_icon_3)
    pic_label.pack()

def createStudent():
    create_student_frame = Frame(display_frame, bg='white', width=770, height=795)
    create_student_frame.place(relx=0, rely=0.05)

    greeting = Label(create_student_frame, text=" STUDENTS REGISTRATION FORM", bg='white', font=('Times New Romans', 13, 'bold'))
    greeting.place(relx=0.25, rely=0.05)

     ########################## TAKING STUDENTS INFORMATION
    nom_lab = Label(create_student_frame, text="NOM", font=("Times New Romans", 10, 'bold'), bg='white')
    nom_lab.place(relx=0.1, rely=0.11)
    nom = Entry(create_student_frame, textvariable=st_nom, width=40, fg="black", bg="white", border=5, font=("Microsoft Yahei UI Light", 14, "bold"))
    nom.place(relx=0.2, rely=0.1)

    prenom_lab = Label(create_student_frame, text="PRENOM", font=("Times New Romans", 10, 'bold'), bg='white')
    prenom_lab.place(relx=0.1, rely=0.2)
    prenom = Entry(create_student_frame,textvariable=nom, width=40, fg="black", bg="white", border=5, font=("Microsoft Yahei UI Light", 14, "bold"))
    prenom.place(relx=0.2, rely=0.19)

    parent_lab = Label(create_student_frame, text="PARENT N°", font=("Times New Romans", 10, 'bold'), bg='white')
    parent_lab.place(relx=0.07, rely=0.29)
    parent_num = Entry(create_student_frame, textvariable=numero_p, width=40, fg="black", bg="white", border=5, font=("Microsoft Yahei UI Light", 14, "bold"))
    parent_num.place(relx=0.2, rely=0.28)

    tuteur_lab = Label(create_student_frame, text="TUTEUR N°", font=("Times New Romans", 10, 'bold'), bg='white')
    tuteur_lab.place(relx=0.1, rely=0.39)
    tuteur_num = Entry(create_student_frame, textvariable=numero_tutor, width=40, fg="black", bg="white", border=5, font=("Microsoft Yahei UI Light", 14, "bold"))
    tuteur_num.place(relx=0.21, rely=0.38)

    save_btn = Button(create_student_frame, pady=7, width=15, text="SAVE", bg='orange', fg='black', font=('Times New Romnas', 10, 'bold'))
    save_btn.place(relx=0.1, rely=0.64)

    # cancel_btn = Button(create_student_frame, pady=7, width=15, text="CANCEL", bg='red', fg='black', font=('Times New Romnas', 10, 'bold'))
    # cancel_btn.place(relx=0.3, rely=0.64)

    def add_profile():
        global profile_img
        img = filedialog.askopenfilename(title='Add your profile picture', filetypes=(('png file','*.png'),('jpeg file','*.jpeg'),('jpg file', '*.jpg')))
        profile_img = image.open(img)
        print(profile_img)
        img_resize = profile_img.resize((150,100))
        new_img = ImageTk.PhotoImage(img_resize)
        img_label = Label(pic_btn, image=new_img)
        img_label.pack()

    pic_btn = Button(create_student_frame, width=20, height=7, text='insert photo', bg='white', fg='black', command=add_profile)
    pic_btn.place(relx=0.3, rely=0.45)



################### CREATE CLASS FUNCTION #####################################
def createClass():
    create_class_frame = Frame(display_frame, bg='white', width=770, height=795)
    create_class_frame.place(relx=0, rely=0.05)

    greeting = Label(create_class_frame, text=" CLASS REGISTRATION FORM", bg='white', font=('Times New Romans', 13, 'bold'))
    greeting.place(relx=0.25, rely=0.05)

    class_name_lab = Label(create_class_frame, text="NOM", font=("Times New Romans", 10, 'bold'), bg='white')
    class_name_lab.place(relx=0.1, rely=0.11)
    class_name = Entry(create_class_frame, width=40, fg="black", bg="white", border=5, font=("Microsoft Yahei UI Light", 14, "bold"))
    class_name.place(relx=0.2, rely=0.1)

    salle_lab = Label(create_class_frame, text="SALLE", font=("Times New Romans", 10, 'bold'), bg='white')
    salle_lab.place(relx=0.1, rely=0.2)
    salle = Entry(create_class_frame, width=40, fg="black", bg="white", border=5, font=("Microsoft Yahei UI Light", 14, "bold"))
    salle.place(relx=0.2, rely=0.19)

    save_btn = Button(create_class_frame, pady=7, width=15, text="CREATE", bg='orange', fg='black', font=('Times New Romnas', 10, 'bold'))
    save_btn.place(relx=0.2, rely=0.25) 


    ################### CREATION OF MATERIAL FUNCTION ####################################
def createMaterial():
    create_material_frame = Frame(display_frame, bg='white', width=770, height=795)
    create_material_frame.place(relx=0, rely=0.05)

    greeting = Label(create_material_frame, text=" COURSES REGISTRATION FORM", bg='white', font=('Times New Romans', 13, 'bold'))
    greeting.place(relx=0.25, rely=0.05)

    mat_name_lab = Label(create_material_frame, text="NOM", font=("Times New Romans", 10, 'bold'), bg='white')
    mat_name_lab.place(relx=0.1, rely=0.11)
    mat_name = Entry(create_material_frame, width=40, fg="black", bg="white", border=5, font=("Microsoft Yahei UI Light", 14, "bold"))
    mat_name.place(relx=0.2, rely=0.1)

    save_btn = Button(create_material_frame, pady=7, width=15, text="SAVE", bg='orange', fg='black', font=('Times New Romnas', 10, 'bold'))
    save_btn.place(relx=0.2, rely=0.18)

def createMaterial():
    create_material_frame = Frame(display_frame, bg='white', width=770, height=795)
    create_material_frame.place(relx=0, rely=0.05)

    greeting = Label(create_material_frame, text=" COURSES REGISTRATION FORM", bg='white', font=('Times New Romans', 13, 'bold'))
    greeting.place(relx=0.25, rely=0.05)

    mat_name_lab = Label(create_material_frame, text="NOM", font=("Times New Romans", 10, 'bold'), bg='white')
    mat_name_lab.place(relx=0.1, rely=0.11)
    mat_name = Entry(create_material_frame, width=40, fg="black", bg="white", border=5, font=("Microsoft Yahei UI Light", 14, "bold"))
    mat_name.place(relx=0.2, rely=0.1)

    co_name_lab = Label(create_material_frame, text="COEF", font=("Times New Romans", 10, 'bold'), bg='white')
    co_name_lab.place(relx=0.1, rely=0.18)
    co_value = Entry(create_material_frame, width=40, fg="black", bg="white", border=5, font=("Microsoft Yahei UI Light", 14, "bold"))
    co_value.place(relx=0.2, rely=0.18)

    save_btn = Button(create_material_frame, pady=7, width=15, text="SAVE", bg='orange', fg='black', font=('Times New Romnas', 10, 'bold'))
    save_btn.place(relx=0.2, rely=0.25) 


############################### CREATION DE UE #############################
def createUE():
    create_ue_frame = Frame(display_frame, bg='white', width=770, height=795)
    create_ue_frame.place(relx=0, rely=0.05)

    greeting = Label(create_ue_frame, text=" UE REGISTRATION", bg='white', font=('Times New Romans', 13, 'bold'))
    greeting.place(relx=0.25, rely=0.05)

    ue_name_lab = Label(create_ue_frame, text="NOM", font=("Times New Romans", 10, 'bold'), bg='white')
    ue_name_lab.place(relx=0.1, rely=0.11)
    ue_name = Entry(create_ue_frame, width=40, fg="black", bg="white", border=5, font=("Microsoft Yahei UI Light", 14, "bold"))
    ue_name.place(relx=0.2, rely=0.1)


    tv = ttk.Treeview(create_ue_frame)
    tv['columns'] = ('Matiere')
    tv.column('#0', width=0, stretch=NO)
    tv.column('Matiere', anchor=CENTER, width=430)


    tv.heading('#0', text='', anchor=CENTER)
    tv.heading('Matiere', text='Matiere', anchor=CENTER)
    tv.place(relx=0.2, rely=0.2, height=300)



################################### THE CREATE FUNCTION #######################33
def creer():
    create_frame = Frame(display_frame, bg='white', width=770, height=795)
    create_frame.place(relx=0, rely=0)
    ## create student btn
    std_btn = Button(create_frame, text='STUDENTS',width=8, bg='orange', fg='black', activebackground='orange', font=("Times New Romans", 10, 'bold'), pady=3, padx=4, command=createStudent)
    std_btn.place(relx=0.03, rely=0.01)

    ## create classe btn
    cls_btn = Button(create_frame, text='CLASSE',width=8, bg='orange', fg='black', activebackground='orange', font=("Times New Romans", 10, 'bold'), pady=3, padx=4, command=createClass)
    cls_btn.place(relx=0.14, rely=0.01)

    ## create material btn
    mat_btn = Button(create_frame, text='MATIERE',width=8, bg='orange', fg='black', activebackground='orange', font=("Times New Romans", 10, 'bold'), pady=3, padx=4, command=createMaterial)
    mat_btn.place(relx=0.25, rely=0.01)

    ## create ue btn
    ue_btn = Button(create_frame, text='UE',width=8, bg='orange', fg='black', activebackground='orange', font=("Times New Romans", 10, 'bold'), pady=3, padx=4, command=createUE)
    ue_btn.place(relx=0.36, rely=0.01)

    create_img_frame = Frame(create_frame, width=150, height=100, bg='black')
    create_img_frame.place(relx=0.21,rely=0.21)

    ###### LOGO
    logo = image.open('image.jpg')
    logo_resize = logo.resize((400,400))
    new_logo = ImageTk.PhotoImage(logo_resize)
    pic_label = Label(create_img_frame, image=new_logo)
    pic_label.pack()

########################### CREATION OF ATTRIBUTION OF CLASS ####################
def attribuerStudent():
    attribuer_class_frame = Frame(display_frame, bg='white', width=770, height=795)
    attribuer_class_frame.place(relx=0, rely=0.05)

    greeting = Label(attribuer_class_frame, text="ATTRIBUER UNE CLASSE", bg='white', font=('Times New Romans', 13, 'bold'))
    greeting.place(relx=0.25, rely=0.05)

    all_classes = ["Class 1", "Class 2", "Class 3", "Class 4"]
    select_class_label = Label(attribuer_class_frame, text='CLASSE', font=("Times New Romans", 10, 'bold'), bg='white')
    select_class_label.place(relx=0.1, rely=0.11)
    select_class_options = ttk.Combobox(attribuer_class_frame,value=all_classes, width=50)
    select_class_options.place(relx=0.2, rely=0.11)

    students_list_lab = Label(attribuer_class_frame, text="STUDENTS", font=("Times New Romans", 10, 'bold'), bg='white')
    students_list_lab.place(relx=0.1, rely=0.2)

    tv = ttk.Treeview(attribuer_class_frame)
    tv['columns'] = ('Matricule', 'Name', 'Prenom')
    tv.column('#0', width=0, stretch=NO)
    tv.column('Matricule', anchor=CENTER, width=120)
    tv.column('Name', anchor=CENTER, width=120)
    tv.column('Prenom', anchor=CENTER, width=120)


    tv.heading('#0', text='', anchor=CENTER)
    tv.heading('Matricule', text='Matricule', anchor=CENTER)
    tv.heading('Name', text='Name', anchor=CENTER)
    tv.heading('Prenom', text='Prenom', anchor=CENTER)


    tv.place(relx=0.2, rely=0.2)

    save_btn = Button(attribuer_class_frame, pady=7, width=15, text="SAVE", bg='orange', fg='black', font=('Times New Romnas', 10, 'bold'))
    save_btn.place(relx=0.2, rely=0.65)

########################### CREATION OF ATTRIBUTION OF PROFESSORS ####################
def attribuerProf():
    attribuer_prof_frame = Frame(display_frame, bg='white', width=770, height=795)
    attribuer_prof_frame.place(relx=0, rely=0.05)

    greeting = Label(attribuer_prof_frame, text="ATTRIBUER UN PROFESSEUR", bg='white', font=('Times New Romans', 13, 'bold'))
    greeting.place(relx=0.25, rely=0.05)

    all_classes = ["Classe 1", "Classe 2", "Classe 3", "Classe 4"]
    select_classe_label = Label(attribuer_prof_frame, text='CLASSE', font=("Times New Romans", 10, 'bold'), bg='white')
    select_classe_label.place(relx=0.15, rely=0.11)
    select_classe_options = ttk.Combobox(attribuer_prof_frame,value=all_classes, width=50)
    select_classe_options.place(relx=0.25, rely=0.11)


    tv = ttk.Treeview(attribuer_prof_frame)
    tv['columns'] = ('Professeurs')
    tv.column('#0', width=0, stretch=NO)
    tv.column('Professeurs', anchor=CENTER, width=300)


    tv.heading('#0', text='', anchor=CENTER)
    tv.heading('Professeurs', text='Professeurs', anchor=CENTER)
    tv.place(relx=0.3, rely=0.2, height=300)

    save_btn = Button(attribuer_prof_frame, pady=7, width=15, text="SAVE", bg='orange', fg='black', font=('Times New Romnas', 10, 'bold'))
    save_btn.place(relx=0.2, rely=0.65)

################################ CREATION OF ATTRIBUTION OF MATERIALS TO PROFS
def attribuerMaterial():
    attribuer_material_frame = Frame(display_frame, bg='white', width=770, height=795)
    attribuer_material_frame.place(relx=0, rely=0.05)

    greeting = Label(attribuer_material_frame, text="ATTRIBUER DES MATTIERES", bg='white', font=('Times New Romans', 13, 'bold'))
    greeting.place(relx=0.25, rely=0.05)

    all_professors = ["Professeur 1", "Professeur 2", "Professeur 3", "Professeur 4"]
    select_professor_label = Label(attribuer_material_frame, text='PROFESSEUR', font=("Times New Romans", 10, 'bold'), bg='white')
    select_professor_label.place(relx=0.1, rely=0.11)
    select_professor_options = ttk.Combobox(attribuer_material_frame,value=all_professors, width=50)
    select_professor_options.place(relx=0.25, rely=0.11)

    tv = ttk.Treeview(attribuer_material_frame)
    tv['columns'] = ('Matiere')
    tv.column('#0', width=0, stretch=NO)
    tv.column('Matiere', anchor=CENTER, width=430)


    tv.heading('#0', text='', anchor=CENTER)
    tv.heading('Matiere', text='Matiere', anchor=CENTER)
    tv.place(relx=0.2, rely=0.2, height=300)

    save_btn = Button(attribuer_material_frame, pady=7, width=15, text="SAVE", bg='orange', fg='black', font=('Times New Romnas', 10, 'bold'))
    save_btn.place(relx=0.2, rely=0.65)

################################### THE ATTRIBUER FUNCTION #######################33
def attribuer():
    attribuer_frame = Frame(display_frame, bg='white', width=770, height=795)
    attribuer_frame.place(relx=0, rely=0)
    ## attribuer student btn
    std_btn = Button(attribuer_frame, text='STUDENTS',width=10, bg='orange', fg='black', activebackground='orange', font=("Times New Romans", 10, 'bold'), pady=3, padx=4, command=attribuerStudent)
    std_btn.place(relx=0.03, rely=0.01)

    ## attribuer classe btn
    cls_btn = Button(attribuer_frame, text='PROFESSEURS',width=11, bg='orange', fg='black', activebackground='orange', font=("Times New Romans", 10, 'bold'), pady=3, padx=4, command=attribuerProf)
    cls_btn.place(relx=0.17, rely=0.01)

    ## attribuer material btn
    mat_btn = Button(attribuer_frame, text='MATIERES',width=10, bg='orange', fg='black', activebackground='orange', font=("Times New Romans", 10, 'bold'), pady=3, padx=4, command=attribuerMaterial)
    mat_btn.place(relx=0.32, rely=0.01)

    create_img_frame = Frame(attribuer_frame, width=150, height=100, bg='black')
    create_img_frame.place(relx=0.21,rely=0.21)

    ###### LOGO
    logo = image.open('image.jpg')
    logo_resize = logo.resize((400,400))
    new_logo = ImageTk.PhotoImage(logo_resize)
    pic_label = Label(create_img_frame, image=new_logo)
    pic_label.pack()

####################### SEE STUDENTS FUNCTION #######################
def voirStudent():
    see_students_frame = Frame(display_frame, bg='white', width=770, height=795)
    see_students_frame.place(relx=0, rely=0.05)

    greeting = Label(see_students_frame, text="VOIR CLASSES", bg='white', font=('Times New Romans', 13, 'bold'))
    greeting.place(relx=0.25, rely=0.05)

    all_classes = ["Classe 1", "Classe 2", "Classe 3", "Classe 4"]
    select_class_label = Label(see_students_frame, text='CLASSE', font=("Times New Romans", 10, 'bold'), bg='white')
    select_class_label.place(relx=0.1, rely=0.11)
    select_class_options = ttk.Combobox(see_students_frame,value=all_classes, width=50)
    select_class_options.place(relx=0.1, rely=0.11)

    ################ GETTING STUDENTS LISTS #################
    tv = ttk.Treeview(see_students_frame)
    tv['columns'] = ('Matricule', 'Name', 'Prenom', 'Parent #', 'Tuteur #', 'Photo')
    tv.column('#0', width=0, stretch=NO)
    tv.column('Matricule', anchor=CENTER, width=120)
    tv.column('Name', anchor=CENTER, width=120)
    tv.column('Prenom', anchor=CENTER, width=120)
    tv.column('Parent #', anchor=CENTER, width=120)
    tv.column('Tuteur #', anchor=CENTER, width=120)
    tv.column('Photo', anchor=CENTER, width=120)

    tv.heading('#0', text='', anchor=CENTER)
    tv.heading('Matricule', text='Matricule', anchor=CENTER)
    tv.heading('Name', text='Name', anchor=CENTER)
    tv.heading('Prenom', text='Prenom', anchor=CENTER)
    tv.heading('Parent #', anchor=CENTER, text='Parents #')
    tv.heading('Tuteur #', anchor=CENTER, text='Tuteur #')
    tv.heading('Photo', anchor=CENTER, text= 'Photo')

    tv.place(relx=0.02, rely=0.2)


####################### SEE NOTIDFCATION FUNCTION #######################
def notification():
    notfication_frame = Frame(display_frame, bg='white', width=770, height=795)
    notfication_frame.place(relx=0, rely=0.05)

    greeting = Label(notfication_frame, text="LISTES DES NOTIFICATIONS", bg='white', font=('Times New Romans', 13, 'bold'))
    greeting.place(relx=0.3, rely=0.05)

    ################ GETTING NOTIFICATION LISTS #################
    notifcations_listbox = Listbox(notfication_frame, width=80, height=20, bg='white', font=('Times New Romans', 10, 'bold'))
    notifcations_listbox.place(relx=0.13, rely=0.1)



    

################################### THE CREATE FUNCTION #######################33
def autre():
    autre_frame = Frame(display_frame, bg='white', width=770, height=795)
    autre_frame.place(relx=0, rely=0)
    ## see student btn
    std_btn = Button(autre_frame, text='VOIR ETUDIANT',width=11, bg='orange', fg='black', activebackground='orange', font=("Times New Romans", 10, 'bold'), pady=3, padx=4, command=voirStudent)
    std_btn.place(relx=0.03, rely=0.01)

    ## notification btn
    cls_btn = Button(autre_frame, text='NOTIFICATION',width=11, bg='orange', fg='black', activebackground='orange', font=("Times New Romans", 10, 'bold'), pady=3, padx=4, command=notification)
    cls_btn.place(relx=0.17, rely=0.01)

    create_img_frame = Frame(autre_frame, width=150, height=100, bg='black')
    create_img_frame.place(relx=0.21,rely=0.21)

    ###### LOGO
    global logo
    logo = image.open('image.jpg')
    logo_resize = logo.resize((400,400))
    new_logo = ImageTk.PhotoImage(logo_resize)
    pic_label = Label(create_img_frame, image=new_logo)
    pic_label.pack()


############################## DASHBOARD MENU ##########################

menu_frame = Frame(app, bg='white', width=230, height=800, border=5)
menu_frame.grid(row=0, column=0)

border_frame_1 = Frame(app, bg='orange', width=5, height=700)
border_frame_1.grid(row=0, column=1)




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

mail_btn = Button(top_bar_frame, text='EMAIL', width=8, bg='orange', fg='black', activebackground='orange', font=('Times New Romans', 10, 'bold'), pady=3, padx=4)
mail_btn.place(relx=0.50,rely=0.28)

home_btn = Button(top_bar_frame, text='HOME',width=8, bg='orange', fg='black', activebackground='orange', font=("Times New Romans", 10, 'bold'), pady=3, padx=4,command=home)
home_btn.place(relx=0.37, rely=0.28)
####### SETTING MENU ITEMS #############################################


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
create_btn = Button(menu_frame, text='CREER',width=15, bg='orange', fg='black', activebackground='orange', font=("Times New Romans", 10, 'bold'), pady=5, padx=4, command=creer)
create_btn.place(relx=0.23, rely=0.13)

attribution_btn = Button(menu_frame, text='ATTRIBUER',width=15, bg='orange', fg='black', activebackground='orange', font=("Times New Romans", 10, 'bold'), pady=5, padx=4, command=attribuer)
attribution_btn.place(relx=0.23, rely=0.19)

autre_btn = Button(menu_frame, text='AUTRE',width=15, bg='orange', fg='black', activebackground='orange', font=("Times New Romans", 10, 'bold'), pady=5, padx=4, command=autre)
autre_btn.place(relx=0.23, rely=0.25)



######################### DISPLY FRAME PROPERTIES
display_top_border_frame = Frame(display_frame, bg='orange', width=770, height=3)
display_top_border_frame.place(relx=0, rely=0)



########### CALLING HOME FUNCTION #####################
home()


app.mainloop()