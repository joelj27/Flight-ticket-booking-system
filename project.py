import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import sqlite3
con=sqlite3.Connection('database')
cur=con.cursor()
cur.execute("create table if not exists database(first_name varchar(20),last_name varchar(20),contact numeric (20),email varchar (20),password varchar(20))")
TITLE_FONT = ("Helvetica", 18, "bold")
class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
    #main window
        self.title("login page")
        self.geometry("1350x700")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
    #show frame
        self.frames = {}
        for F in (Sign_up, Login,Order_and_munch_non_veg,Order_and_munch_veg,Flight_agenda_status,
                  Order_and_munch_bev,Home_page,Reservre_a_ticket_oneway,Reservre_a_ticket_twoway,
                  Flight_agenda,Baggage_domestic,Baggage_international,Add_on_services,
                  Critiques):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Reservre_a_ticket_oneway)
    # it will have all the class and pop each class when its called
    def show_frame(self, c):
        frame = self.frames[c]
        frame.tkraise()
class Sign_up(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
    #Accessing the image file
        logo = tk.PhotoImage(file="re1.png")
        BGlabel = tk.Label(self,image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, relwidth=1, relheight=1)
    #Acessing the lef image file
        left = tk.PhotoImage(file=r"reg1.png")
        bglab=tk.Label(self,image=left)
        bglab.image=left
        bglab.place(x=80, y=100, width=400, height=500)
    #frame created
        frame1=tk.Frame(self)
        frame1.place(x=480,y=100,width=700,height=500)
    #label enroll
        title = tk.Label(frame1, text="ENROLL HERE", font=("times new roman", 20, "bold"), bg="white", fg="orange4").place(
            x=50, y=30)
    #label first name
        f_name = tk.Label(frame1, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="orange4").place(
            x=50, y=100)
    #first name entry
        self.txt_fname = tk.Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_fname.place(x=50, y=130, width=250)
    #last name
        l_name = tk.Label(frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="orange4").place(
            x=370, y=100)
    # last name entry
        self.txt_lname = tk.Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_lname.place(x=370, y=130, width=250)
    #label contact
        contact = tk.Label(frame1, text="Contact No.", font=("times new roman", 15, "bold"), bg="white",
                        fg="orange4").place(x=50, y=170)
    #contact entry
        self.txt_contact =tk.Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_contact.place(x=50, y=200, width=250)
    #label email
        email = tk.Label(frame1, text="Email Id", font=("times new roman", 15, "bold"), bg="white", fg="orange4").place(
            x=370, y=170)
    #email entry
        self.txt_email = tk.Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=370, y=200, width=250)
    #label password
        password = tk.Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="orange4").place(
            x=50, y=240)
    #password entry
        self.txt_password = tk.Entry(frame1, font=("times new roman", 15, "bold"), bg="lightgray", show="*")
        self.txt_password.place(x=50, y=270,width=250)
    #label confirm password
        cpassword = tk.Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white",
                          fg="orange4").place(x=370, y=240)
    #confirm password entry
        self.txt_cpassword = tk.Entry(frame1, font=("times new roman", 15), bg="lightgray", show="*")
        self.txt_cpassword.place(x=370, y=270,width=250)
        #Terms button
        self.ckvalue = tk.IntVar()
        self.bchk = tk.Checkbutton(frame1,variable=self.ckvalue,onvalue=1,offvalue=0, text="I Agree The Terms & Conditions", bg="white",font=("times new roman", 12), fg="orange4")
        self.bchk.place(x=50, y=310)
    #sign in button
        btn_login = tk.Button(frame1, text="Sign In", font=("times new roman", 12), bg="orange4", bd=1,command=lambda :Sign_up.Signup_fun(self,parent,controller),
                           cursor="hand2").place(x=110, y=350, width=200, height=40)
    def wrong_password(self,parent,controller):
        flogin = tk.Frame(self, bg="#d77337")
        flogin.place(x=500, y=150, height=300, width=300)

        lbl_pass = tk.Label(flogin, text="You entered different\npassword", font=("Goudy old style", 15, "bold"), fg="white",
                            bg="#d77337").place(x=80, y=130)
        Login_btn = tk.Button(flogin, command=lambda: flogin.destroy(), text="Close",
                              fg="#d77337", bg="white",
                              font=("times new roman", 18)).place(x=110, y=230, width=80, height=30)
        tk.Button(flogin, command=lambda: flogin.destroy(), text="X",
                  fg="#d77337", bg="white",
                  font=("times new roman", 18)).place(x=280, y=0, width=20, height=20)
    def checkbox(self,parent,controller):
        flogin = tk.Frame(self, bg="#d77337")
        flogin.place(x=500, y=150, height=300, width=300)

        lbl_pass = tk.Label(flogin, text="selsct check box", font=("Goudy old style", 15, "bold"), fg="white",
                            bg="#d77337").place(x=80, y=130)
        Login_btn = tk.Button(flogin, command=lambda: flogin.destroy(), text="Close",
                              fg="#d77337", bg="white",
                              font=("times new roman", 18)).place(x=110, y=230, width=80, height=30)
        tk.Button(flogin, command=lambda: flogin.destroy(), text="X",
                  fg="#d77337", bg="white",
                  font=("times new roman", 18)).place(x=280, y=0, width=20, height=20)
    def nothing(self,parent,controller):
        flogin = tk.Frame(self, bg="#d77337")
        flogin.place(x=500, y=150, height=300, width=300)

        lbl_pass = tk.Label(flogin, text="enter something", font=("Goudy old style", 15, "bold"), fg="white",
                            bg="#d77337").place(x=80, y=130)
        Login_btn = tk.Button(flogin, command=lambda: flogin.destroy(), text="Close",
                              fg="#d77337", bg="white",
                              font=("times new roman", 18)).place(x=110, y=230, width=80, height=30)
        tk.Button(flogin, command=lambda: flogin.destroy(), text="X",
                  fg="#d77337", bg="white",
                  font=("times new roman", 18)).place(x=280, y=0, width=20, height=20)
    def success(self,parent,controller):
        flogin = tk.Frame(self, bg="#d77337")
        flogin.place(x=500, y=150, height=300, width=300)

        lbl_pass = tk.Label(flogin, text="login success", font=("Goudy old style", 15, "bold"), fg="white",
                            bg="#d77337").place(x=80, y=130)
        Login_btn = tk.Button(flogin, command=lambda: [flogin.destroy(),controller.show_frame(Login)], text="Close",
                              fg="#d77337", bg="white",
                              font=("times new roman", 18)).place(x=110, y=230, width=80, height=30)
        tk.Button(flogin, command=lambda: [flogin.destroy(),controller.show_frame(Login)], text="X",
                  fg="#d77337", bg="white",
                  font=("times new roman", 18)).place(x=280, y=0, width=20, height=20)
    def email_taken(self,parent,controller):
        flogin = tk.Frame(self, bg="#d77337")
        flogin.place(x=500, y=150, height=300, width=300)

        lbl_pass = tk.Label(flogin, text="user name is not available", font=("Goudy old style", 15, "bold"), fg="white",
                            bg="#d77337").place(x=80, y=130)
        Login_btn = tk.Button(flogin, command=lambda: flogin.destroy(), text="Close",
                              fg="#d77337", bg="white",
                              font=("times new roman", 18)).place(x=110, y=230, width=80, height=30)
        tk.Button(flogin, command=lambda: flogin.destroy(), text="X",
                  fg="#d77337", bg="white",
                  font=("times new roman", 18)).place(x=280, y=0, width=20, height=20)
    def Signup_fun(self,parents,controller):
        fname = self.txt_fname.get()
        lname=self.txt_lname.get()
        contact=self.txt_contact.get()
        email=self.txt_email.get()
        password=self.txt_password.get()
        cpasword=self.txt_cpassword.get()
        check_button=self.ckvalue.get()
        a1 = cur.execute("SELECT email FROM database WHERE email=?", [email])
        if len(fname) == 0 or len(lname) == 0 or len(contact) == 0 or len(email) == 0 or len(password) == 0 or len(cpasword) == 0:
            Sign_up.nothing(self,controller,parents)
        elif password!=cpasword:
            Sign_up.wrong_password(self, controller, parents)
        elif check_button==0:
            Sign_up.checkbox(self,controller,parents)
        else:
            Sign_up.check_mail(self, controller, parents)
    def check_mail(self,parents,controller):
        fname = self.txt_fname.get()
        lname = self.txt_lname.get()
        contact = self.txt_contact.get()
        email = self.txt_email.get()
        password = self.txt_password.get()
        a1 = cur.execute("SELECT email FROM database WHERE email=?", [email])
        try:
            a1.fetchone()[0]
            Sign_up.email_taken(self, controller,parents)
        except:
            cur.execute("INSERT INTO database(first_name,last_name,contact,email,password)VALUES(?,?,?,?,?)",
                        (fname, lname, contact, email, password))
            Sign_up.success(self, controller, parents)

class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file="flight1.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, relwidth=1, relheight=1)
        Frame_login = tk.Frame(self,bg="white")
        Frame_login.place(x=150, y=150, height=370, width=500)
        title = tk.Label(Frame_login, text="Check In Here", font=("Impact", 35, "bold"), fg="#d77337", bg="white").place(
            x=90,
            y=30)
        desc = tk.Label(Frame_login, text="Passenger Login zone", font=("Goudy old style", 15, "bold"), fg="#d25d17",
                     bg="white").place(x=90, y=100)

        lbl_user = tk.Label(Frame_login, text="User Handle", font=("Goudy old style", 15, "bold"), fg="gray",
                         bg="white").place(x=90, y=140)
        self.txt_user = tk.Entry(Frame_login, font=("times new roman", 15), bg="lightgray")
        self.txt_user.place(x=90, y=170, width=350)

        lbl_pass = tk.Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="gray",
                         bg="white").place(x=90, y=210)
        self.txt_pass = tk.Entry(Frame_login, font=("times new roman", 15), bg="lightgray", show="*")
        self.txt_pass.place(x=90, y=240, width=350, height=35)

        forget_btn = tk.Button(Frame_login, text="Forget Password?", cursor="hand2", bg="white", fg="#d77337", bd=0,
                            font=("times new roman", 12)).place(x=90, y=280)

        Login_btn = tk.Button(Frame_login,command=lambda :Login.fun(self,parent,controller), text="Board In", fg="white", bg="#d77337", bd=2,
                           font=("times new roman", 18)).place(x=220, y=310)
        Login_btn = tk.Button(Frame_login,command=lambda :controller.show_frame(Sign_up), text="Register", fg="white", bg="#d77337", bd=2,
                           font=("times new roman", 18)).place(x=350, y=310)
# if password or user name entry is empy
    def no_pass(self,parent, controller):
        flogin = tk.Frame(self, bg="#d77337")
        flogin.place(x=500, y=150, height=300, width=300)

        lbl_pass = tk.Label(flogin, text="Enter something", font=("Goudy old style", 15, "bold"), fg="white",
                            bg="#d77337").place(x=80, y=130)
        Login_btn = tk.Button(flogin, command=lambda :flogin.destroy(), text="Close",
                              fg="#d77337", bg="white",
                              font=("times new roman", 18)).place(x=110, y=230,width=80,height=30)
        tk.Button(flogin, command=lambda: flogin.destroy(), text="X",
                  fg="#d77337", bg="white",
                  font=("times new roman", 18)).place(x=280, y=0, width=20, height=20)
#if password or usernmae is wrong
    def wrong_user(self,parent, controller):
        flogin = tk.Frame(self, bg="#d77337")
        flogin.place(x=500, y=150, height=300, width=300)

        lbl_pass = tk.Label(flogin, text="user name is wrong\n please try again", font=("Goudy old style", 15, "bold"), fg="white",
                            bg="#d77337").place(x=20, y=130)
        Login_btn = tk.Button(flogin, command=lambda :flogin.destroy(), text="Close",
                              fg="#d77337", bg="white",
                              font=("times new roman", 18)).place(x=110, y=230,width=80,height=30)
        tk.Button(flogin, command=lambda: flogin.destroy(), text="X",
                  fg="#d77337", bg="white",
                  font=("times new roman", 18)).place(x=280, y=0, width=20, height=20)
    def wrong_pass(self,parent, controller):
        flogin = tk.Frame(self, bg="#d77337")
        flogin.place(x=500, y=150, height=300, width=300)

        lbl_pass = tk.Label(flogin, text="password is wrong\n please try again", font=("Goudy old style", 15, "bold"), fg="white",
                            bg="#d77337").place(x=20, y=130)
        Login_btn = tk.Button(flogin, command=lambda :flogin.destroy(), text="Close",
                              fg="#d77337", bg="white",
                              font=("times new roman", 18)).place(x=110, y=230,width=80,height=30)
        tk.Button(flogin, command=lambda: flogin.destroy(), text="X",
                  fg="#d77337", bg="white",
                  font=("times new roman", 18)).place(x=280, y=0, width=20, height=20)
    def fun(self,parent,controller):
        user = self.txt_user.get()
        pas = self.txt_pass.get()
        a1 = cur.execute("SELECT email FROM database WHERE email=?", [user])
        a=True
        if len(user)== 0 or len(pas) == 0:
                     Login.no_pass(self,parent, controller)
        elif a==True:
            try:
                a1.fetchall()[0]
            except:
                Login.wrong_user(self, parent, controller)
            else:
                Login.funcc(self, parent, controller)
    def funcc(self,parent,controller):
        user = self.txt_user.get()
        pas = self.txt_pass.get()
        a11 = cur.execute("SELECT * FROM database WHERE  email=?", [user])
        if a11.fetchall()[0][4]==pas:
            controller.show_frame(Home_page)

        else:
            Login.wrong_pass(self, parent, controller)
class Home_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.color = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}
        logo = tk.PhotoImage(file="re1.png")
        BGlabel = tk.Label(self, image=logo, bg='grey')
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, relwidth=1, relheight=1)
        self.btnState = False
        self.navIcon = tk.PhotoImage(file=r"menu (1).png")
        self.closeIcon = tk.PhotoImage(file=r"close (1).png")
        # top Navigation bar:
        self.topFrame = tk.Frame(self, bg=self.color["orange"])
        self.topFrame.pack(side="top", fill=tk.X)

        # Header label text:
        self.homeLabel = tk.Label(self.topFrame, text="Welcome onboard", font="Bahnschrift 15", bg=self.color["orange"],
                                  fg="gray17",
                                  height=2, padx=20)
        self.homeLabel.pack(side="right")

        # Navbar button:
        self.navbarBtn = tk.Button(self.topFrame, image=self.navIcon, bg=self.color["orange"],
                                   activebackground=self.color["orange"], bd=0,
                                   padx=20, command=lambda: Home_page.switch(self))
        self.navbarBtn.place(x=10, y=10)

        # setting Navbar frame:
        self.navRoot = tk.Frame(self, bg="gray17", height=1000, width=300)
        self.navRoot.place(x=-300, y=0)
        tk.Label(self.navRoot, font="Bahnschrift 15", bg=self.color["orange"], fg="black", height=2, width=300,
                 padx=20).place(
            x=0, y=0)

        # set y-coordinate of Navbar widgets:
        y = 80
        # option in the navbar:
        options = ["Reserve a ticket", "Clocking in", "Flight Ranking", "Flight Agenda", "Order and munch",
                   "Baggage norms", "Critiques"]

        b1 = tk.Button(self.navRoot, command=lambda: controller.show_frame(Reservre_a_ticket_oneway),
                       text="Reserve a ticket", font="BahnschriftLight 15", bg="gray17", fg=self.color["orange"],
                       activebackground="gray17", activeforeground="white", bd=0).place(x=25, y=80)
        b2 = tk.Button(self.navRoot, command=lambda: controller.show_frame(Flight_agenda), text="Flight Agenda",
                       font="BahnschriftLight 15", bg="gray17", fg=self.color["orange"],
                       activebackground="gray17", activeforeground="white", bd=0).place(x=25, y=120)
        b3 = tk.Button(self.navRoot, command=lambda: controller.show_frame(Order_and_munch_veg), text="Order and munch",
                       font="BahnschriftLight 15", bg="gray17", fg=self.color["orange"],
                       activebackground="gray17", activeforeground="white", bd=0).place(x=25, y=160)
        b4 = tk.Button(self.navRoot, command=lambda: controller.show_frame(Baggage_domestic), text="Baggage norms",
                       font="BahnschriftLight 15", bg="gray17", fg=self.color["orange"],
                       activebackground="gray17", activeforeground="white", bd=0).place(x=25, y=200)
        b5 = tk.Button(self.navRoot, text="Add on services", command=lambda: controller.show_frame(Add_on_services),
                       font="BahnschriftLight 15", bg="gray17", fg=self.color["orange"],
                       activebackground="gray17", activeforeground="white", bd=0).place(x=25, y=240)
        b6 = tk.Button(self.navRoot, text="Critiques", command=lambda: controller.show_frame(Critiques),
                       font="BahnschriftLight 15", bg="gray17", fg=self.color["orange"],
                       activebackground="gray17", activeforeground="white", bd=0).place(x=25, y=280)
        b7 = tk.Button(self.navRoot, text="Log out", command=lambda: controller.show_frame(Login),
                       font="BahnschriftLight 15", bg="gray17", fg=self.color["orange"],
                       activebackground="gray17", activeforeground="white", bd=0).place(x=25, y=320)

        closeBtn = tk.Button(self.navRoot, image=self.closeIcon, bg=self.color["orange"],
                             activebackground=self.color["orange"], bd=0,
                             command=lambda: Home_page.switch(self))
        closeBtn.place(x=250, y=10)

    def switch(self):
        if self.btnState is True:
            # create animated Navbar closing:
            for x in range(301):
                self.navRoot.place(x=-x, y=0)
                self.topFrame.update()

            # resetting widget colors:
            self.homeLabel.config(bg=self.color["orange"])
            self.topFrame.config(bg=self.color["orange"])
            self.config(bg="gray17")

            # turning button OFF:
            self.btnState = False
        else:
            # make root dim:
            self.homeLabel.config(bg=self.color["nero"])
            self.topFrame.config(bg=self.color["nero"])
            self.config(bg=self.color["nero"])

            # created animated Navbar opening:
            for x in range(-300, 0):
                self.navRoot.place(x=x, y=0)
                self.topFrame.update()

            # turing button ON:
            self.btnState = True
class Reservre_a_ticket_oneway(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # one way
        logo = tk.PhotoImage(file="flight1.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, relwidth=1, relheight=1)
        Frame_login = tk.Frame(self, bg="white")
        Frame_login.place(x=150, y=150, height=400, width=900)
        lbl_user = tk.Label(Frame_login, text="Starting destination", font=("Goudy old style", 15, "bold"), fg="gray",
                            bg="white").place(x=90, y=65)
        course = ["Bombay","Chennai","Bengaluru","Dubai","Coimbatore","Delhi","Singapore","Pune","Cochin"]
        widget_var1 = tk.StringVar()
        self.cmb1 = ttk.Combobox(Frame_login,textvariable=widget_var1,state="readonly", value=course, width=30, height=30)
        self.cmb1.place(x=90, y=95, width="350", height="35")

        lbl_user = tk.Label(Frame_login, text="Ending destination", font=("Goudy old style", 15, "bold"), fg="gray",
                            bg="white").place(x=500, y=65)
        widget_var2 = tk.StringVar()
        self.cmb2 = ttk.Combobox(Frame_login,textvariable=widget_var2,state="readonly", value=course, width=30, height=30)
        self.cmb2.place(x=500, y=95, width="350", height="35")

        lbl_pass = tk.Label(Frame_login, text="Starting date", font=("Goudy old style", 15, "bold"), fg="gray",
                            bg="white").place(x=90, y=150)
        self.start_date = DateEntry(Frame_login, background="tomato", foreground='white', borderwidth=1, bordercolor="black")
        self.start_date.place(x=90, y=180, width=350, height=35)

        lbl_pass = tk.Label(Frame_login, text="Passenger name", font=("Goudy old style", 15, "bold"), fg="gray",
                            bg="white").place(x=500, y=150)
        self.name = tk.Entry(Frame_login, font=("times new roman", 15), bg="white")
        self.name.place(x=500, y=180, width=350, height=35)

        Login_btn = tk.Button(Frame_login, command=lambda: Reservre_a_ticket_oneway.funct(self,controller,parent), text="Search flights",
                              fg="white", bg="#d77337", bd=2,
                              font=("times new roman", 18)).place(x=380, y=350)
        tk.Button(self, width=18, height=2, text='O N E W A Y', pady=4,
                  command=lambda: controller.show_frame(Reservre_a_ticket_oneway), border=0, bg='#d77337',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=150, y=150)
        # signup()
        tk.Button(self, width=18, command=lambda: controller.show_frame(Reservre_a_ticket_twoway), height=2,
                  text='R O U N D T R I P', pady=4, border=0, bg='grey',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=280, y=150)
    def same_dec(self,parent,controller):
        flogin = tk.Frame(self, bg="#d77337")
        flogin.place(x=500, y=150, height=300, width=300)

        lbl_pass = tk.Label(flogin, text="you dont have flight\n for same place", font=("Goudy old style", 15, "bold"), fg="white",
                            bg="#d77337").place(x=80, y=130)
        Login_btn = tk.Button(flogin, command=lambda: flogin.destroy(), text="Close",
                              fg="#d77337", bg="white",
                              font=("times new roman", 18)).place(x=110, y=230, width=80, height=30)
        tk.Button(flogin, command=lambda: flogin.destroy(), text="X",
                  fg="#d77337", bg="white",
                  font=("times new roman", 18)).place(x=280, y=0, width=20, height=20)
    def fill_all(self,parent,controller):
        flogin = tk.Frame(self, bg="#d77337")
        flogin.place(x=500, y=150, height=300, width=300)

        lbl_pass = tk.Label(flogin, text="fill all the coloumn", font=("Goudy old style", 15, "bold"), fg="white",
                            bg="#d77337").place(x=80, y=130)
        Login_btn = tk.Button(flogin, command=lambda: flogin.destroy(), text="Close",
                              fg="#d77337", bg="white",
                              font=("times new roman", 18)).place(x=110, y=230, width=80, height=30)
        tk.Button(flogin, command=lambda: flogin.destroy(), text="X",
                  fg="#d77337", bg="white",
                  font=("times new roman", 18)).place(x=280, y=0, width=20, height=20)
    def no_flight(self,parent,controller):
        flogin = tk.Frame(self, bg="#d77337")
        flogin.place(x=500, y=150, height=300, width=300)

        lbl_pass = tk.Label(flogin, text="no flight avaliable on this rout", font=("Goudy old style", 15, "bold"), fg="white",
                            bg="#d77337").place(x=80, y=130)
        Login_btn = tk.Button(flogin, command=lambda: flogin.destroy(), text="Close",
                              fg="#d77337", bg="white",
                              font=("times new roman", 18)).place(x=110, y=230, width=80, height=30)
        tk.Button(flogin, command=lambda: flogin.destroy(), text="X",
                  fg="#d77337", bg="white",
                  font=("times new roman", 18)).place(x=280, y=0, width=20, height=20)
    def funct(self,controller,parent):
        star_dec_1 = self.cmb1.get()
        star_dec_2 = self.cmb2.get()
        global cus_date
        cus_date=self.start_date .get()
        global cus_name
        cus_name=self.name.get()
        a11 = cur.execute("SELECT * FROM flight WHERE  from_flight=? and to_flight=?", [star_dec_1, star_dec_2])
        a = a11.fetchall()

        if len(cus_date)==0 or len(cus_name)==0 or len(star_dec_1)==0 or len(star_dec_2)==0:
            Reservre_a_ticket_oneway.fill_all(self, parent, controller)
        elif star_dec_1==star_dec_2:
            Reservre_a_ticket_oneway.same_dec(self,parent,controller)
        elif len(a)==0:
            Reservre_a_ticket_oneway.no_flight(self, parent, controller)


        else:
            Reservre_a_ticket_oneway.flight(self,parent,controller)
    def flight(self,parent,controller):
        star_dec_1 = self.cmb1.get()
        star_dec_2 = self.cmb2.get()
        date = self.start_date.get()
        name = self.name.get()
        a11 = cur.execute("SELECT * FROM flight WHERE  from_flight=? and to_flight=?", [star_dec_1, star_dec_2])
        a = a11.fetchall()
        logo = tk.PhotoImage(file="flight_agenda.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, relwidth=1, relheight=1)
        # frame created
        Frame_login = tk.Frame(self, bg="white")
        Frame_login.place(x=100, y=50, height=600, width=1000)
        global sel11
        self.sel1 = tk.IntVar()
        if len(a)==1:
            tk.Label(Frame_login, text="SL.NO", font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=0, y=0, height=50, width=100)
            tk.Label(Frame_login, text="FLIGHT NAME", font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=100, y=0, height=50, width=100)
            tk.Label(Frame_login, text="FLIGHT ID", font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=200, y=0, height=50, width=100)
            tk.Label(Frame_login, text="DEPARTURE", font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=300, y=0, height=50, width=100)
            tk.Label(Frame_login, text="ARRIVAL", font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=400, y=0, height=50, width=100)
            tk.Label(Frame_login, text="DEPARTURE TIME", font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=500, y=0, height=50, width=100)
            tk.Label(Frame_login, text="ARRIVAL TIME", font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=600, y=0, height=50, width=100)
            tk.Label(Frame_login, text="ECONOMY", font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=700, y=0, height=50, width=100)
            tk.Label(Frame_login, text="BUSINESS", font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=800, y=0, height=50, width=100)

            tk.Label(Frame_login, text="1", font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=0, y=50, height=50, width=100)
            tk.Label(Frame_login, text=a[0][0], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=100, y=50, height=50, width=100)
            tk.Label(Frame_login, text=a[0][1], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=200, y=50, height=50, width=100)
            tk.Label(Frame_login, text=a[0][2], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=300, y=50, height=50, width=100)
            tk.Label(Frame_login, text=a[0][3], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=400, y=50, height=50, width=100)
            tk.Label(Frame_login, text=a[0][4], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=500, y=50, height=50, width=100)
            tk.Label(Frame_login, text=a[0][5], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=600, y=50, height=50, width=100)

            v1 = tk.Radiobutton(Frame_login, text="ECONOMY\n₹4470", font=("times new roman", 10, "bold"), fg="tomato",
                                bg="white")
            v1.config(variable=self.sel1, value=a[0][6])
            v1.place(x=700, y=50, height=50, width=100)
            v1 = tk.Radiobutton(Frame_login, text="BUSINESS\n₹4987", font=("times new roman", 10, "bold"), fg="tomato",
                                bg="white")
            v1.config(variable=self.sel1, value=a[0][7])
            v1.place(x=800, y=50, height=50, width=100)
        elif len(a)==2:
            tk.Label(Frame_login, text="SL.NO", font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=0, y=0, height=50, width=100)
            tk.Label(Frame_login, text="FLIGHT NAME", font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=100, y=0, height=50, width=100)
            tk.Label(Frame_login, text="FLIGHT ID", font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=200, y=0, height=50, width=100)
            tk.Label(Frame_login, text="DEPARTURE", font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=300, y=0, height=50, width=100)
            tk.Label(Frame_login, text="ARRIVAL", font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=400, y=0, height=50, width=100)
            tk.Label(Frame_login, text="DEPARTURE TIME", font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=500, y=0, height=50, width=100)
            tk.Label(Frame_login, text="ARRIVAL TIME", font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=600, y=0, height=50, width=100)
            tk.Label(Frame_login, text="ECONOMY", font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=700, y=0, height=50, width=100)
            tk.Label(Frame_login, text="BUSINESS", font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=800, y=0, height=50, width=100)

            tk.Label(Frame_login, text="1", font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=0, y=50, height=50, width=100)
            tk.Label(Frame_login, text=a[0][0], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=100, y=50, height=50, width=100)
            tk.Label(Frame_login, text=a[0][1], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=200, y=50, height=50, width=100)
            tk.Label(Frame_login, text=a[0][2], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=300, y=50, height=50, width=100)
            tk.Label(Frame_login, text=a[0][3], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=400, y=50, height=50, width=100)
            tk.Label(Frame_login, text=a[0][4], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=500, y=50, height=50, width=100)
            tk.Label(Frame_login, text=a[0][5], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=600, y=50, height=50, width=100)

            v1 = tk.Radiobutton(Frame_login, text="ECONOMY\n₹4470", font=("times new roman", 10, "bold"), fg="tomato",
                                bg="white")
            v1.config(variable=self.sel1, value=a[0][6])
            v1.place(x=700, y=50, height=50, width=100)
            v1 = tk.Radiobutton(Frame_login, text="BUSINESS\n₹4987", font=("times new roman", 10, "bold"), fg="tomato",
                                bg="white")
            v1.config(variable=self.sel1, value=a[0][7])
            v1.place(x=800, y=50, height=50, width=100)

            tk.Label(Frame_login, text="2", font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=0, y=100, height=50, width=100)
            tk.Label(Frame_login, text=a[1][0], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=100, y=100, height=50, width=100)
            tk.Label(Frame_login, text=a[1][1], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=200, y=100, height=50, width=100)
            tk.Label(Frame_login, text=a[1][2], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=300, y=100, height=50, width=100)
            tk.Label(Frame_login, text=a[1][3], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=400, y=100, height=50, width=100)
            tk.Label(Frame_login, text=a[1][4], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=500, y=100, height=50, width=100)
            tk.Label(Frame_login, text=a[1][5], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=600, y=100, height=50, width=100)

            v1 = tk.Radiobutton(Frame_login, text="ECONOMY\n₹4673", font=("times new roman", 10, "bold"), fg="tomato",
                                bg="white")
            v1.config(variable=self.sel1, value=a[1][6])
            v1.place(x=700, y=100, height=50, width=100)
            v1 = tk.Radiobutton(Frame_login, text="BUSINESS\n₹4833", font=("times new roman", 10, "bold"), fg="tomato",
                                bg="white")
            v1.config(variable=self.sel1, value=a[1][7])
            v1.place(x=800, y=100, height=50, width=100)
        elif len(a)==3:
            tk.Label(Frame_login, text="SL.NO", font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=0, y=0, height=50, width=100)
            tk.Label(Frame_login, text="FLIGHT NAME", font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=100, y=0, height=50, width=100)
            tk.Label(Frame_login, text="FLIGHT ID", font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=200, y=0, height=50, width=100)
            tk.Label(Frame_login, text="DEPARTURE", font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=300, y=0, height=50, width=100)
            tk.Label(Frame_login, text="ARRIVAL", font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=400, y=0, height=50, width=100)
            tk.Label(Frame_login, text="DEPARTURE TIME", font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=500, y=0, height=50, width=100)
            tk.Label(Frame_login, text="ARRIVAL TIME", font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=600, y=0, height=50, width=100)
            tk.Label(Frame_login, text="ECONOMY", font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=700, y=0, height=50, width=100)
            tk.Label(Frame_login, text="BUSINESS", font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=800, y=0, height=50, width=100)

            tk.Label(Frame_login, text="1", font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=0, y=50, height=50, width=100)
            tk.Label(Frame_login, text=a[0][0], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=100, y=50, height=50, width=100)
            tk.Label(Frame_login, text=a[0][1], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=200, y=50, height=50, width=100)
            tk.Label(Frame_login, text=a[0][2], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=300, y=50, height=50, width=100)
            tk.Label(Frame_login, text=a[0][3], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=400, y=50, height=50, width=100)
            tk.Label(Frame_login, text=a[0][4], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=500, y=50, height=50, width=100)
            tk.Label(Frame_login, text=a[0][5], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=600, y=50, height=50, width=100)

            v1 = tk.Radiobutton(Frame_login, text="ECONOMY\n₹4470", font=("times new roman", 10, "bold"), fg="tomato",
                                bg="white")
            v1.config(variable=self.sel1, value=a[0][6])
            v1.place(x=700, y=50,height=50, width=100 )
            v1 = tk.Radiobutton(Frame_login, text="BUSINESS\n₹4987", font=("times new roman", 10, "bold"), fg="tomato",
                                bg="white")
            v1.config(variable=self.sel1, value=a[0][7])
            v1.place(x=800, y=50,height=50, width=100 )

            tk.Label(Frame_login, text="2", font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=0, y=100, height=50, width=100)
            tk.Label(Frame_login, text=a[1][0], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=100, y=100, height=50, width=100)
            tk.Label(Frame_login, text=a[1][1], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=200, y=100, height=50, width=100)
            tk.Label(Frame_login, text=a[1][2], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=300, y=100, height=50, width=100)
            tk.Label(Frame_login, text=a[1][3], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=400, y=100, height=50, width=100)
            tk.Label(Frame_login, text=a[1][4], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=500, y=100, height=50, width=100)
            tk.Label(Frame_login, text=a[1][5], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=600, y=100, height=50, width=100)

            v1 = tk.Radiobutton(Frame_login, text="ECONOMY\n₹4673", font=("times new roman", 10, "bold"), fg="tomato",
                                bg="white")
            v1.config(variable=self.sel1, value=a[1][6])
            v1.place(x=700, y=100, height=50, width=100)
            v1 = tk.Radiobutton(Frame_login, text="BUSINESS\n₹4833", font=("times new roman", 10, "bold"), fg="tomato",
                                bg="white")
            v1.config(variable=self.sel1, value=a[1][7])
            v1.place(x=800, y=100, height=50, width=100)

            tk.Label(Frame_login, text="3", font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=0, y=150, height=50, width=100)
            tk.Label(Frame_login, text=a[2][0], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=100, y=150, height=50, width=100)
            tk.Label(Frame_login, text=a[2][1], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=200, y=150, height=50, width=100)
            tk.Label(Frame_login, text=a[2][2], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=300, y=150, height=50, width=100)
            tk.Label(Frame_login, text=a[2][3], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=400, y=150, height=50, width=100)
            tk.Label(Frame_login, text=a[2][4], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=500, y=150, height=50, width=100)
            tk.Label(Frame_login, text=a[2][5], font=("Goudy old style", 10, "bold"), fg="gray", bg="white") \
                .place(x=600, y=150, height=50, width=100)

            v1 = tk.Radiobutton(Frame_login, text=a[2][6], font=("times new roman", 10, "bold"), fg="tomato",
                                bg="white")
            v1.config(variable=self.sel1, value=a[2][6])
            v1.place(x=700, y=150, height=50, width=100)
            v1 = tk.Radiobutton(Frame_login, text="BUSINESS\n₹4788", font=("times new roman", 10, "bold"), fg="tomato",
                                bg="white")
            v1.config(variable=self.sel1, value=a[2][7])
            v1.place(x=800, y=150, height=50, width=100)
        else:
            pass

        Login_btn = tk.Button(Frame_login, text="next", command=lambda:Reservre_a_ticket_oneway.flight_fun(self,parent,controller) ,
                              fg="white", bg="grey", bd=1,
                              font=("times new roman", 18)).place(x=580, y=550, width=100, height=30)
    def no_flig_seleced(self,parent,controller):
        flogin = tk.Frame(self, bg="#d77337")
        flogin.place(x=500, y=150, height=300, width=300)

        lbl_pass = tk.Label(flogin, text="selsect any one flight", font=("Goudy old style", 15, "bold"), fg="white",
                            bg="#d77337").place(x=80, y=130)
        Login_btn = tk.Button(flogin, command=lambda: flogin.destroy(), text="Close",
                              fg="#d77337", bg="white",
                              font=("times new roman", 18)).place(x=110, y=230, width=80, height=30)
        tk.Button(flogin, command=lambda: flogin.destroy(), text="X",
                  fg="#d77337", bg="white",
                  font=("times new roman", 18)).place(x=280, y=0, width=20, height=20)
    def flight_fun(self,parent,controller):
        sel11 = self.sel1.get()
        self.add=0
        self.add += sel11
        if sel11!=0:

            Reservre_a_ticket_oneway.foodveg(self,parent,controller)
        elif sel11==0:
            Reservre_a_ticket_oneway.no_flig_seleced(self, parent, controller)
        else:
            pass
##################################################################################################
    def foodveg(self,parent,controller):
        logo = tk.PhotoImage(file=r"image/foo.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, relwidth=1, relheight=1)
        # frame created
        Frame_login = tk.Frame(self, bg="white")
        Frame_login.place(x=150, y=70, height=800, width=900)
        load = Image.open(r"image/san.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=190, y=170)

        self.VEG_sel1 = tk.IntVar()
        self.VEG_sel2 = tk.IntVar()
        self.VEG_sel3 = tk.IntVar()
        self.VEG_sel4 = tk.IntVar()
        self.VEG_sel5 = tk.IntVar()
        self.VEG_sel6 = tk.IntVar()
        self.VEG_sel7 = tk.IntVar()
        self.r1 = tk.Radiobutton(self, text="sandwich\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        self.r1.config(variable=self.VEG_sel1, value=250)
        self.r1.place(x=190, y=310)
        self.r2 = tk.Radiobutton(self, text="burger\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato", bg="white")
        self.r2.config(variable=self.VEG_sel2, value=250)
        self.r2.place(x=380, y=310)
        self.r3 = tk.Radiobutton(self, text="pizza\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato", bg="white")
        self.r3.config(variable=self.VEG_sel3, value=250)
        self.r3.place(x=580, y=310)
        self.r4 = tk.Radiobutton(self, text="noodles\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        self.r4.config(variable=self.VEG_sel4, value=250)
        self.r4.place(x=780, y=310)
        self.r5 = tk.Radiobutton(self, text="salad\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato", bg="white")
        self.r5.config(variable=self.VEG_sel5, value=250)
        self.r5.place(x=190, y=540)
        self.r6 = tk.Radiobutton(self, text="pancake\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        self.r6.config(variable=self.VEG_sel6, value=250)
        self.r6.place(x=380, y=540)
        self.r7 = tk.Radiobutton(self, text="pasta\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato", bg="white")
        self.r7.config(variable=self.VEG_sel7, value=250)
        self.r7.place(x=580, y=540)

        load = Image.open(r"image/burg.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=390, y=170)

        load = Image.open(r"image/pizzaa.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=590, y=170)

        load = Image.open(r"image/n.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=790, y=170)

        load = Image.open(r"image/salad.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=190, y=405)

        load = Image.open(r"image/pancake.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=390, y=405)

        load = Image.open(r"image/pasta.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=590, y=405)


        Login_btn = tk.Button(Frame_login, text="add", command=lambda:Reservre_a_ticket_oneway.fooveg(self,parent,controller),
                              fg="white", bg="#d77337", bd=1,
                              font=("times new roman", 18)).place(x=740, y=440, width=100, height=30)
        Login_btn = tk.Button(Frame_login, text="skip", command=lambda:Reservre_a_ticket_oneway.fooskip(self,parent,controller) ,
                              fg="white", bg="#d77337", bd=1,
                              font=("times new roman", 18)).place(x=620, y=440, width=100, height=30)

        tk.Button(self, width=18, height=2, text='V E G', pady=4,
                  command=lambda: Reservre_a_ticket_oneway.foodveg(self,parent,controller), border=0, bg='grey',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=150, y=70)
        # signup()
        tk.Button(self, width=18, height=2, text='N O N V E G', pady=4,
                  command=lambda:  Reservre_a_ticket_oneway.foodnveg(self,parent,controller), border=0, bg='#d77337',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=280, y=70)
        # bev()
        tk.Button(self, width=18, height=2, text='B E V', pady=4,
                  command=lambda:  Reservre_a_ticket_oneway.foodbev(self,parent,controller), border=0, bg='#d77337',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=410, y=70)
    def fooskip(self,parent,controller):
        self.r1.deselect()
        self.r2.deselect()
        self.r3.deselect()
        self.r4.deselect()
        self.r5.deselect()
        self.r6.deselect()
        self.r7.deselect()
        Reservre_a_ticket_oneway.foodnveg(self, parent, controller)
    def fooveg(self,parent,controller):
        veg = self.VEG_sel1.get() + self.VEG_sel2.get() + self.VEG_sel3.get() + self.VEG_sel4.get() + self.VEG_sel5.get() + self.VEG_sel6.get() + self.VEG_sel7.get()
        self.add += veg
        Reservre_a_ticket_oneway.foodnveg(self, parent, controller)
#############################################################################################
    def foodnveg(self, parent, controller):
        logo = tk.PhotoImage(file=r"image/foo.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, relwidth=1, relheight=1)
        # frame created
        Frame_login = tk.Frame(self, bg="white")
        Frame_login.place(x=150, y=70, height=800, width=900)
        load = Image.open(r"image/san.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=190, y=170)

        self.NVEG_set1 = tk.IntVar()
        self.NVEG_set2 = tk.IntVar()
        self.NVEG_set3 = tk.IntVar()
        self.NVEG_set4 = tk.IntVar()
        self.NVEG_set5 = tk.IntVar()
        self.NVEG_set6 = tk.IntVar()
        self.NVEG_set7 = tk.IntVar()

        self.s1 = tk.Radiobutton(self, text="chicken pizza\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        self.s1.config(variable=self.NVEG_set1, value=250)
        self.s1.place(x=190, y=310)
        self.s2 = tk.Radiobutton(self, text="chicken pizza\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        self.s2.config(variable=self.NVEG_set2, value=250)
        self.s2.place(x=380, y=310)
        self.s3 = tk.Radiobutton(self, text="chicken burger\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        self.s3.config(variable=self.NVEG_set3, value=250)
        self.s3.place(x=580, y=310)
        self.s4 = tk.Radiobutton(self, text="chcken sausage\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        self.s4.config(variable=self.NVEG_set4, value=250)
        self.s4.place(x=780, y=310)
        self.s5 = tk.Radiobutton(self, text="shawarma\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        self.s5.config(variable=self.NVEG_set5, value=250)
        self.s5.place(x=190, y=540)
        self.s6 = tk.Radiobutton(self, text="chicken sandwich\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        self.s6.config(variable=self.NVEG_set6, value=250)
        self.s6.place(x=380, y=540)
        self.s7 = tk.Radiobutton(self, text="lasagna\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        self.s7.config(variable=self.NVEG_set7, value=250)
        self.s7.place(x=580, y=540)

        load = Image.open(r"image\chicken pizza.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=390, y=170)

        load = Image.open(r"image\chicken burger.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=590, y=170)

        load = Image.open(r"image\chicken sausage.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=790, y=170)

        load = Image.open(r"image\shawarma.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=190, y=405)

        load = Image.open(r"image\chicken sandwich.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=390, y=405)

        load = Image.open(r"image\lasagna.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=590, y=405)

        Login_btn = tk.Button(Frame_login, text="add", command=lambda: Reservre_a_ticket_oneway.nfooveg(self,parent, controller),
                              fg="white", bg="#d77337", bd=1,
                              font=("times new roman", 18)).place(x=740, y=440, width=100, height=30)
        Login_btn = tk.Button(Frame_login, text="skip", command=lambda: Reservre_a_ticket_oneway.nfooskip(self,parent, controller),
                              fg="white", bg="#d77337", bd=1,
                              font=("times new roman", 18)).place(x=620, y=440, width=100, height=30)


        tk.Button(self, width=18, height=2, text='V E G', pady=4,
                  command=lambda: Reservre_a_ticket_oneway.foodveg(self, parent, controller), border=0, bg='#d77337',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=150, y=70)
        # signup(
        tk.Button(self, width=18, height=2, text='N O N V E G', pady=4,
                  command=lambda: Reservre_a_ticket_oneway.foodnveg(self, parent, controller), border=0, bg='grey',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=280, y=70)
        # bev()

        tk.Button(self, width=18, height=2, text='B E V', pady=4,
                  command=lambda: Reservre_a_ticket_oneway.foodbev(self, parent, controller), border=0, bg='#d77337',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=410, y=70)
    def nfooskip(self,parent,controller):
        self.s1.deselect()
        self.s2.deselect()
        self.s3.deselect()
        self.s4.deselect()
        self.s5.deselect()
        self.s6.deselect()
        self.s7.deselect()
        Reservre_a_ticket_oneway.foodbev(self, parent, controller)
    def nfooveg(self,parent,controller):
        nveg = self.NVEG_set1.get() + self.NVEG_set2.get() + self.NVEG_set3.get() + self.NVEG_set4.get() + self.NVEG_set5.get() + self.NVEG_set6.get() + self.NVEG_set7.get()
        self.add += nveg
        Reservre_a_ticket_oneway.foodbev(self, parent, controller)
##############################################################################################
    def foodbev(self,parent,controller):
        logo = tk.PhotoImage(file=r"image/foo.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, relwidth=1, relheight=1)
        # frame created
        Frame_login = tk.Frame(self, bg="white")
        Frame_login.place(x=150, y=70, height=800, width=900)
        load = Image.open(r"image/san.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=190, y=170)

        self.BEV_sel1 = tk.IntVar()
        self.BEV_sel2 = tk.IntVar()
        self.BEV_sel3 = tk.IntVar()
        self.BEV_sel4 = tk.IntVar()
        self.BEV_sel5 = tk.IntVar()
        self.BEV_sel6 = tk.IntVar()
        self.BEV_sel7 = tk.IntVar()

        self.t1 = tk.Radiobutton(self, text="masala tea\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        self.t1.config(variable=self.BEV_sel1, value=250)
        self.t1.place(x=190, y=310)
        self.t2 = tk.Radiobutton(self, text="coco-cola\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        self.t2.config(variable=self.BEV_sel2, value=250)
        self.t2.place(x=380, y=310)
        self.t3 = tk.Radiobutton(self, text="green tea\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        self.t3.config(variable=self.BEV_sel3, value=250)
        self.t3.place(x=580, y=310)
        self.t4 = tk.Radiobutton(self, text="non-alcoholic beer\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        self.t4.config(variable=self.BEV_sel4, value=250)
        self.t4.place(x=780, y=310)
        self.t5 = tk.Radiobutton(self, text="paper boat\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        self.t5.config(variable=self.BEV_sel5, value=250)
        self.t5.place(x=190, y=540)
        self.t6 = tk.Radiobutton(self, text="cappuccino\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                                 bg="white")
        self.t6.config(variable=self.BEV_sel6, value=250)
        self.t6.place(x=380, y=540)
        self.t7 = tk.Radiobutton(self, text="cold coffee\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        self.t7.config(variable=self.BEV_sel7, value=250)
        self.t7.place(x=580, y=540)

        load = Image.open(r"image\coco-cola.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=390, y=170)

        load = Image.open(r"image\green tea.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=590, y=170)

        load = Image.open(r"image\non-alcoh"
                          r"olic beer.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=790, y=170)

        load = Image.open(r"image\paper boat.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=190, y=405)

        load = Image.open(r"image\cappuccino.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=390, y=405)

        load = Image.open(r"image\cold coffee.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=590, y=405)

        Login_btn = tk.Button(Frame_login, text="add", command=lambda: Reservre_a_ticket_oneway.bfooveg(self,parent,controller), fg="white",
                              bg="#d77337", bd=1,
                              font=("times new roman", 18)).place(x=740, y=440, width=100, height=30)
        Login_btn = tk.Button(Frame_login, text="skip", command=lambda: Reservre_a_ticket_oneway.bfooskip(self,parent,controller),
                              fg="white", bg="#d77337", bd=1,
                              font=("times new roman", 18)).place(x=620, y=440, width=100, height=30)


        tk.Button(self, width=18, height=2, text='V E G', pady=4,
                  command=lambda:  Reservre_a_ticket_oneway.foodveg(self,parent,controller), border=0, bg='#d77337',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=150, y=70)
        # signup()
        tk.Button(self, width=18, height=2, text='N O N V E G', pady=4,
                  command=lambda:  Reservre_a_ticket_oneway.foodnveg(self,parent,controller), border=0, bg='#d77337',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=280, y=70)
        # bev()
        tk.Button(self, width=18, height=2, text='B E V', pady=4,
                  command=lambda:  Reservre_a_ticket_oneway.foodbev(self,parent,controller), border=0, bg='grey',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=410, y=70)
    def bfooskip(self,parent,controller):
        self.t1.deselect()
        self.t2.deselect()
        self.t3.deselect()
        self.t4.deselect()
        self.t5.deselect()
        self.t6.deselect()
        self.t7.deselect()
        Reservre_a_ticket_oneway.bag(self, parent, controller)
    def bfooveg(self,parent,controller):
        bveg = self.BEV_sel1.get() + self.BEV_sel2.get() + self.BEV_sel3.get() + self.BEV_sel4.get() + self.BEV_sel5.get() + self.BEV_sel6.get() + self.BEV_sel7.get()
        self.add += bveg
        Reservre_a_ticket_oneway.bag(self, parent, controller)
##################################################################################################
    def bag(self,parent,controller):
        logo = tk.PhotoImage(file=r"image/za.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, relwidth=1, relheight=1)
        # frame created
        Frame_login = tk.Frame(self, bg="white")
        Frame_login.place(x=150, y=70, height=800, width=900)
        lbl_user = tk.Label(Frame_login, text="Add On Services", font=("Goudy old style", 20, "bold"), fg="skyblue4",
                            bg="white").place(x=40, y=35)
        txt_user = tk.Entry(Frame_login, font=("times new roman", 15), relief="ridge", bg="white")

        load = Image.open(r"image\seat.png")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=190, y=170)

        self.BAG_sel1 = tk.IntVar()
        self.BAG_sel2 = tk.IntVar()
        self.BAG_sel3 = tk.IntVar()
        self.BAG_sel4 = tk.IntVar()
        self.BAG_sel5 = tk.IntVar()
        self.BAG_sel6 = tk.IntVar()
        self.BAG_sel7 = tk.IntVar()



        self.u1 = tk.Radiobutton(self, text="Seat Plus\n₹150", font=("times new roman", 14, "bold"), fg="skyblue4",
                            bg="white")
        self.u1.config(variable=self.BAG_sel1, value=150)
        self.u1.place(x=190, y=310)
        self.u2 = tk.Radiobutton(self, text="Excess Baggage\n₹2000", font=("times new roman", 14, "bold"), fg="skyblue4",
                           bg="white")
        self.u2.config(variable=self.BAG_sel2, value=2000)
        self.u2.place(x=380, y=310)
        self.u3 = tk.Radiobutton(self, text="Travel Assistance\n₹159", font=("times new roman", 14, "bold"), fg="skyblue4",
                            bg="white")
        self.u3.config(variable=self.BAG_sel3, value=159)
        self.u3.place(x=580, y=310)
        self.u4 = tk.Radiobutton(self, text="Blanket\n₹120", font=("times new roman", 14, "bold"), fg="skyblue4", bg="white")
        self.u4.config(variable=self.BAG_sel4, value=120)
        self.u4.place(x=780, y=310)
        self.u5 = tk.Radiobutton(self, text="Eye shade\n₹80", font=("times new roman", 14, "bold"), fg="skyblue4",
                            bg="white")
        self.u5.config(variable=self.BAG_sel5, value=80)
        self.u5.place(x=190, y=540)
        self.u6 = tk.Radiobutton(self, text="sports equipment\n₹250", font=("times new roman", 14, "bold"), fg="skyblue4",
                            bg="white")
        self.u6.config(variable=self.BAG_sel6, value=250)
        self.u6.place(x=380, y=540)
        self.u7 = tk.Radiobutton(self, text="fast forward\n₹250", font=("times new roman", 14, "bold"), fg="skyblue4",
                            bg="white")
        self.u7.config(variable=self.BAG_sel7, value=250)
        self.u7.place(x=580, y=540)

        load = Image.open(r"image\exc.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=390, y=170)

        load = Image.open(r"image\trav.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=590, y=170)

        load = Image.open(r"image\bla.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=790, y=170)

        load = Image.open(r"image\bla.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=190, y=405)

        load = Image.open(r"image\sports.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=390, y=405)

        load = Image.open(r"image\fast.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=590, y=405)
        Login_btn = tk.Button(Frame_login, text="add", command=lambda: Reservre_a_ticket_oneway.bagadd(self,parent,controller), fg="white",
                              bg="skyblue4", bd=1,
                              font=("times new roman", 18)).place(x=740, y=440, width=100, height=30)
        Login_btn = tk.Button(Frame_login, text="skip", command=lambda: Reservre_a_ticket_oneway.bagskip(self,parent,controller), fg="white",
                              bg="skyblue4", bd=1,
                              font=("times new roman", 18)).place(x=620, y=440, width=100, height=30)
    def bagskip(self,parent,controller):
        self.u1.deselect()
        self.u2.deselect()
        self.u3.deselect()
        self.u4.deselect()
        self.u5.deselect()
        self.u6.deselect()
        self.u7.deselect()
        Reservre_a_ticket_oneway.seat(self)
    def bagadd(self,parent,controller):
        bag = self.BAG_sel1.get() + self.BAG_sel2.get() + self.BAG_sel3.get() + self.BAG_sel4.get() + self.BAG_sel5.get() + self.BAG_sel6.get() + self.BAG_sel7.get()
        self.add += bag
        Reservre_a_ticket_oneway.seat(self)
################################################################################################
    def seat(self):
        logo = tk.PhotoImage(file=r"image/insidee.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, relwidth=1, relheight=1)

        Frame_login = tk.Frame(self, bg="white")
        Frame_login.place(x=150, y=70, height=800, width=500)

        # Add Image
        logo1 = tk.PhotoImage(file=r"image/ro.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo1

        # Create button and image

        lbl_user = tk.Label(Frame_login, text="<- Exit", font=("Goudy old style", 15, "bold"), fg="skyblue4",
                            bg="white").place(x=20, y=35)
        lbl_user = tk.Label(Frame_login, text="Exit ->", font=("Goudy old style", 15, "bold"), fg="skyblue4",
                            bg="white").place(x=430, y=35)

        lbl_user = tk.Label(Frame_login, text=self.add, font=("Goudy old style", 15, "bold"), fg="skyblue4",
                            bg="white").place(x=250, y=85)

        lbl_user = tk.Label(Frame_login, text="2", font=("Goudy old style", 15, "bold"), fg="skyblue4",
                            bg="white").place(x=250, y=130)

        lbl_user = tk.Label(Frame_login, text="3", font=("Goudy old style", 15, "bold"), fg="skyblue4",
                            bg="white").place(x=250, y=175)

        lbl_user = tk.Label(Frame_login, text="4", font=("Goudy old style", 15, "bold"), fg="skyblue4",
                            bg="white").place(x=250, y=220)

        lbl_user = tk.Label(Frame_login, text="5", font=("Goudy old style", 15, "bold"), fg="skyblue4",
                            bg="white").place(x=250, y=265)

        lbl_user = tk.Label(Frame_login, text="6", font=("Goudy old style", 15, "bold"), fg="skyblue4",
                            bg="white").place(x=250, y=310)

        lbl_user = tk.Label(Frame_login, text="7", font=("Goudy old style", 15, "bold"), fg="skyblue4",
                            bg="white").place(x=250, y=355)

        lbl_user = tk.Label(Frame_login, text="8", font=("Goudy old style", 15, "bold"), fg="skyblue4",
                            bg="white").place(x=250, y=400)

        lbl_user = tk.Label(Frame_login, text="9", font=("Goudy old style", 15, "bold"), fg="skyblue4",
                            bg="white").place(x=250, y=445)

        lbl_user = tk.Label(Frame_login, text="<- Exit", font=("Goudy old style", 15, "bold"), fg="skyblue4",
                            bg="white").place(x=20, y=495)
        lbl_user = tk.Label(Frame_login, text="Exit ->", font=("Goudy old style", 15, "bold"), fg="skyblue4",
                            bg="white").place(x=430, y=495)
        self.seat_sel1 = tk.IntVar()
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=490, y=156)
        self.v1 = tk.Radiobutton(self , fg="skyblue4",
                                 bg="white")
        self.v1.config(variable=self.seat_sel1, value=(4,))
        self.v1.place(x=490, y=170)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=540, y=156)
        self.v1 = tk.Radiobutton(self, fg="skyblue4",
                                 bg="white")
        self.v1.config(variable=self.seat_sel1, value=(5,))
        self.v1.place(x=540, y=170)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=590, y=156)
        self.v1 = tk.Radiobutton(self, fg="skyblue4",
                                 bg="white")
        self.v1.config(variable=self.seat_sel1, value=(6,))
        self.v1.place(x=590, y=170)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=190, y=156)
        self.v1 = tk.Radiobutton(self, fg="skyblue4",
                                 bg="white")
        self.v1.config(variable=self.seat_sel1, value=(""))
        self.v1.place(x=190, y=170)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=240, y=156)
        self.v1 = tk.Radiobutton(self, fg="skyblue4",
                                 bg="white")
        self.v1.config(variable=self.seat_sel1, value=(2,))
        self.v1.place(x=240, y=170)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=290, y=156)
        self.v1 = tk.Radiobutton(self, fg="skyblue4",
                                 bg="white")
        self.v1.config(variable=self.seat_sel1, value=(3,))
        self.v1.place(x=290, y=170)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=190, y=196)
        self.v1 = tk.Radiobutton(self, fg="skyblue4",
                                 bg="white")
        self.v1.config(variable=self.seat_sel1, value=(10,))
        self.v1.place(x=190, y=210)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=240, y=196)
        self.v1 = tk.Radiobutton(self, fg="skyblue4",
                                 bg="white")
        self.v1.config(variable=self.seat_sel1, value=(11,))
        self.v1.place(x=240, y=210)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=290, y=196)
        self.v1 = tk.Radiobutton(self, fg="skyblue4",
                                 bg="white")
        self.v1.config(variable=self.seat_sel1, value=(12,))
        self.v1.place(x=290, y=210)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=490, y=196)
        self.v1 = tk.Radiobutton(self, fg="skyblue4",
                                 bg="white")
        self.v1.config(variable=self.seat_sel1, value=(7,))
        self.v1.place(x=490, y=210)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=540, y=196)
        self.v1 = tk.Radiobutton(self, fg="skyblue4",
                                 bg="white")
        self.v1.config(variable=self.seat_sel1, value=(8,))
        self.v1.place(x=540, y=210)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=590, y=196)
        self.v1 = tk.Radiobutton(self, fg="skyblue4",
                                 bg="white")
        self.v1.config(variable=self.seat_sel1, value=(9,))
        self.v1.place(x=590, y=210)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=190, y=236)
        self.v1 = tk.Radiobutton(self, fg="skyblue4",
                                 bg="white")
        self.v1.config(variable=self.seat_sel1, value=(16,))
        self.v1.place(x=190, y=250)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=240, y=236)
        self.v1 = tk.Radiobutton(self, fg="skyblue4",
                                 bg="white")
        self.v1.config(variable=self.seat_sel1, value=(17,))
        self.v1.place(x=240, y=250)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=290, y=236)
        self.v1 = tk.Radiobutton(self, fg="skyblue4",
                                 bg="white")
        self.v1.config(variable=self.seat_sel1, value=(18,))
        self.v1.place(x=290, y=250)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=490, y=236)
        self.v1 = tk.Radiobutton(self, fg="skyblue4",
                                 bg="white")
        self.v1.config(variable=self.seat_sel1, value=(13,))
        self.v1.place(x=490, y=250)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=540, y=236)
        self.v1 = tk.Radiobutton(self, fg="skyblue4",
                                 bg="white")
        self.v1.config(variable=self.seat_sel1, value=(14,))
        self.v1.place(x=540, y=250)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=590, y=236)
        self.v1 = tk.Radiobutton(self, fg="skyblue4",
                                 bg="white")
        self.v1.config(variable=self.seat_sel1, value=(15,))
        self.v1.place(x=590, y=250)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=190, y=276)
        self.v1 = tk.Radiobutton(self, fg="skyblue4",
                                 bg="white")
        self.v1.config(variable=self.seat_sel1, value=(15,))
        self.v1.place(x=190, y=290)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=240, y=276)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=290, y=276)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=490, y=276)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=540, y=276)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=590, y=276)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=190, y=316)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=240, y=316)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=290, y=316)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=490, y=316)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=540, y=316)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=590, y=316)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=190, y=356)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=240, y=356)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=290, y=356)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=490, y=356)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=540, y=356)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=590, y=356)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=190, y=396)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=240, y=396)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=290, y=396)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=490, y=396)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=540, y=396)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=590, y=396)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=190, y=436)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=240, y=436)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=290, y=436)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=490, y=436)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=540, y=436)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=590, y=436)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=190, y=486)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=240, y=486)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=290, y=486)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=490, y=486)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=540, y=486)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=590, y=486)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=190, y=526)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=240, y=526)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=290, y=526)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=490, y=526)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=540, y=526)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=590, y=526)
        Login_btn = tk.Button(self, text="Next", command= lambda :Reservre_a_ticket_oneway.seatcon(self), fg="white",
                              bg="skyblue4", bd=1,
                              font=("times new roman", 18)).place(x=370, y=590, width=100, height=30)
    def seatcon(self):
        cur.execute("create table if not exists seat(seat_num numeric(20))")
        self.s = self.seat_sel1.get()
        p = cur.execute("SELECT seat_num FROM seat where seat_num=?", [self.s])
        b = p.fetchall()

        if self.s in b:
            Reservre_a_ticket_oneway.seattaken(self)
        else:
            cur.execute("INSERT INTO seat(seat_num) VALUES(?)", str(self.s))
            Reservre_a_ticket_oneway.detail(self)
    def seattaken(self):
        flogin = tk.Frame(self, bg="#d77337")
        flogin.place(x=500, y=150, height=300, width=300)

        lbl_pass = tk.Label(flogin, text="seat is taken", font=("Goudy old style", 15, "bold"),
                            fg="white",
                            bg="#d77337").place(x=80, y=130)
        Login_btn = tk.Button(flogin, command=lambda: flogin.destroy(), text="Close",
                              fg="#d77337", bg="white",
                              font=("times new roman", 18)).place(x=110, y=230, width=80, height=30)
        tk.Button(flogin, command=lambda: flogin.destroy(), text="X",
                  fg="#d77337", bg="white",
                  font=("times new roman", 18)).place(x=280, y=0, width=20, height=20)

    def detail(self):
        bg = tk.PhotoImage(file=r"image/ro.png")

        tk.Label(self, image=bg).place(x=0, y=0, relwidth=1, relheight=1)
        # ====Login Frame=====
        Frame_login = tk.Frame(self, bg="white")
        Frame_login.place(x=150, y=150, height=400, width=900)
        ## TO ADD LABELS##

        lbl_user = tk.Label(Frame_login, text=self.s, font=("Goudy old style", 15, "bold"), fg="tomato",
                         bg="white").place(x=90, y=65)
        txt_user = tk.Entry(Frame_login, font=("times new roman", 15), relief="ridge", bg="white")
        txt_user.place(x=90, y=95, width=350, height=35)

        lbl_user = tk.Label(Frame_login, text="Last Name", font=("Goudy old style", 15, "bold"), fg="tomato",
                         bg="white").place(x=500, y=65)
        txt_user = tk.Entry(Frame_login, font=("times new roman", 15), relief="ridge", bg="white")
        txt_user.place(x=500, y=95, width=350, height=35)

        lbl_pass = tk.Label(Frame_login, text="Date of Birth", font=("Goudy old style", 15, "bold"), fg="tomato",
                         bg="white").place(x=90, y=150)

        lbl_pass = tk.Label(Frame_login, text="Email Id", font=("Goudy old style", 15, "bold"), fg="tomato",
                         bg="white").place(x=500, y=150)
        txt_user = tk.Entry(Frame_login, font=("times new roman", 15), bg="white", relief="ridge")
        txt_user.place(x=500, y=180, width=350, height=35)

        lbl_pass = tk.Label(Frame_login, text="Contact No.", font=("Goudy old style", 15, "bold"), fg="tomato",
                         bg="white").place(x=90, y=230)
        txt_pass = tk.Entry(Frame_login, font=("times new roman", 15), bg="white", relief="ridge")
        txt_pass.place(x=90, y=260, width=350, height=35)

        lbl_user = tk.Label(Frame_login, text="Gender", font=("Goudy old style", 15, "bold"), fg="tomato",
                         bg="white").place(x=500, y=230)
        cal = DateEntry(Frame_login, background="tomato", foreground='white', borderwidth=1, bordercolor="black")
        cal.place(x=90, y=180, width=350, height=35)
        sel = tk.IntVar()
        sel.set(1)
        r1 = tk.Radiobutton(self, text="Male", font=("times new roman", 14, "bold"), fg="tomato", bg="white")
        r1.config(variable=sel, value=1)
        r1.place(x=650, y=410)
        r2 = tk.Radiobutton(self, text="Female", font=("times new roman", 14, "bold"), fg="tomato", bg="white")
        r2.config(variable=sel, value=2)
        r2.place(x=740, y=410)
        r3 = tk.Radiobutton(self, text="Genderqueer", font=("times new roman", 14, "bold"), fg="tomato", bg="white")
        r3.config(variable=sel, value=3)
        r3.place(x=830, y=410)


        Login_btn = tk.Button(Frame_login, text="Proceed", fg="white", bg="tomato", bd=3,command=lambda:Reservre_a_ticket_oneway.payment(self),
                           font=("times new roman", 18)).place(x=380, y=330, width=200)
    def payment(self):
        self.bg = tk.PhotoImage(file=r"image/re1.png")
        tk.Label(self, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        ##Login Frame##

        Frame_login = tk.Frame(self, bg="white")

        Frame_login.place(x=150, y=150, height=370, width=500)

        ## TO ADD LABELS ##

        title = tk.Label(Frame_login, text="Payment Method", font=("Impact", 35, "bold"), fg="#d77337", bg="white").place(
            x=30, y=30)

        Login_btn = tk.Button(Frame_login, text="Credit Card", fg="white", bg="#d77337", bd=2,command=lambda :Reservre_a_ticket_oneway.net(self),
                           font=("times new roman", 18)).place(x=90, y=121, width="230", height="35")
        Login_btn = tk.Button(Frame_login, text="Debit Card", fg="white", bg="#d77337", bd=2,
                           font=("times new roman", 18)).place(x=90, y=171, width="230", height="35")
        Login_btn = tk.Button(Frame_login, text="UPI Payment", fg="white", bg="#d77337", bd=2,
                           font=("times new roman", 18)).place(x=90, y=221, width="230", height="35")
        Login_btn = tk.Button(Frame_login, text="Net banking", fg="white", bg="#d77337", bd=2,
                              font=("times new roman", 18)).place(x=90, y=271,  width="230", height="35")
    def net(self):
        bg = tk.PhotoImage(file=r"image/re1.png")
        bg_image = tk.Label(self, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        ##Login Frame##

        Frame_login = tk.Frame(self, bg="white")
        Frame_login.place(x=150, y=150, height=390, width=700)

        ## TO ADD LABELS ##

        title = tk.Label(Frame_login, text="Credit Card", font=("times new roman", 25, "bold"), fg="salmon4",
                      bg="white").place(x=30, y=30)

        lbl_user = tk.Label(Frame_login, text="Credit card Number", font=("Goudy old style", 15, "bold"), fg="salmon4",
                         bg="white").place(x=50, y=95)
        txt_user = tk.Entry(Frame_login, font=("times new roman", 15), relief="ridge", bg="white")
        txt_user.place(x=50, y=125, width=280, height=35)
        lbl_user = tk.Label(Frame_login, text="Expiry/validity date", font=("Goudy old style", 15, "bold"), fg="salmon4",
                         bg="white").place(x=50, y=175)
        txt_user = tk.Entry(Frame_login, font=("times new roman", 15), relief="ridge", bg="white")
        txt_user.place(x=50, y=205, width=280, height=35)
        lbl_user = tk.Label(Frame_login, text="Full Name on Card", font=("Goudy old style", 15, "bold"), fg="salmon4",
                         bg="white").place(x=50, y=255)
        txt_user = tk.Entry(Frame_login, font=("times new roman", 15), relief="ridge", bg="white")
        txt_user.place(x=50, y=285, width=280, height=35)

        lbl_user = tk.Label(Frame_login, text="cvv", font=("Goudy old style", 15, "bold"), fg="salmon4",
                         bg="white").place(x=370, y=175)
        txt_user = tk.Entry(Frame_login, font=("times new roman", 15), relief="ridge", bg="white")
        txt_user.place(x=370, y=205, width=280, height=35)
        Login_btn = tk.Button(Frame_login, text="Make Payment", fg="white", bg="salmon4", bd=2,
                           font=("times new roman", 16)).place(x=250, y=340, width="200")
class Reservre_a_ticket_twoway(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logo = tk.PhotoImage(file="flight1.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, relwidth=1, relheight=1)
        Frame_login = tk.Frame(self, bg="white")
        Frame_login.place(x=150, y=150, height=400, width=900)
        lbl_user = tk.Label(Frame_login, text="Starting destination", font=("Goudy old style", 15, "bold"), fg="gray",
                            bg="white").place(x=90, y=65)
        course = ["Bombay","Chennai","Bengaluru","Dubai","Coimbatore","Delhi","Singapore","Pune","Cochin"]
        widget_var1 = tk.StringVar()
        self.cmb = ttk.Combobox(Frame_login,textvariable=widget_var1,state="readonly", value=course, width=30, height=30)
        self.cmb.place(x=90, y=95, width="350", height="35")

        lbl_user = tk.Label(Frame_login, text="Ending destination", font=("Goudy old style", 15, "bold"), fg="gray",
                            bg="white").place(x=500, y=65)
        widget_var2 = tk.StringVar()
        self.cmb = ttk.Combobox(Frame_login,textvariable=widget_var2,state="readonly", value=course, width=30, height=30)
        self.cmb.place(x=500, y=95, width="350", height="35")

        lbl_pass = tk.Label(Frame_login, text="Starting date", font=("Goudy old style", 15, "bold"), fg="gray",
                            bg="white").place(x=90, y=150)
        txt_pass = tk.Entry(Frame_login, font=("times new roman", 15), bg="white")
        txt_pass.place(x=90, y=180, width=350, height=35)

        lbl_pass = tk.Label(Frame_login, text="Return date", font=("Goudy old style", 15, "bold"), fg="gray",
                            bg="white").place(x=500, y=150)
        txt_pass = tk.Entry(Frame_login, font=("times new roman", 15), bg="white")
        txt_pass.place(x=500, y=180, width=350, height=35)

        lbl_pass = tk.Label(Frame_login, text="Passenger(s)", font=("Goudy old style", 15, "bold"), fg="gray",
                            bg="white").place(x=90, y=230)
        txt_pass = tk.Entry(Frame_login, font=("times new roman", 15), bg="white")
        txt_pass.place(x=90, y=260, width=350, height=35)
        Login_btn = tk.Button(Frame_login, command=lambda: Reservre_a_ticket_twoway.flight(self), text="Search flights",
                              fg="white", bg="#d77337", bd=2,
                              font=("times new roman", 18)).place(x=380, y=350)
        tk.Button(self, width=18, height=2, text='O N E W A Y', pady=4,
                  command=lambda: controller.show_frame(Reservre_a_ticket_oneway), border=0, bg='grey',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=150, y=150)
        # signup()
        tk.Button(self, width=18, height=2, text='R O U N D T R I P', pady=4,
                  command=lambda: controller.show_frame(Reservre_a_ticket_twoway), border=0, bg='#d77337',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=280, y=150)

    def flight(self):
        logo = tk.PhotoImage(file="flight1.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, relwidth=1, relheight=1)
        Frame_login = tk.Frame(self, bg="white")
        Frame_login.place(x=150, y=150, height=400, width=900)
        ## TO ADD LABELS##

        lbl_user = tk.Label(Frame_login, text="Indigo\n6E 5365", font=("Goudy old style", 15, "bold"), fg="tomato",
                            bg="white").place(x=90, y=65)
        lbl_user = tk.Label(Frame_login, text="BOM - MAA", font=("Goudy old style", 15, "bold"), fg="tomato",
                            bg="white").place(x=220, y=65)
        lbl_user = tk.Label(Frame_login, text="11:45 - 13:45", font=("Goudy old style", 15, "bold"), fg="tomato",
                            bg="white").place(x=390, y=65)
        sel = tk.IntVar()
        sel.set(1)
        r1 = tk.Radiobutton(self, text="5343", font=("times new roman", 14, "bold"), fg="tomato", bg="white")
        r1.config(variable=sel, value=1)
        r1.place(x=680, y=210)
        r2 = tk.Radiobutton(self, text="6220", font=("times new roman", 14, "bold"), fg="tomato", bg="white")
        r2.config(variable=sel, value=2)
        r2.place(x=790, y=210)
        r3 = tk.Radiobutton(self, text="5343", font=("times new roman", 14, "bold"), fg="tomato", bg="white")
        r3.config(variable=sel, value=3)
        r3.place(x=680, y=285)
        r4 = tk.Radiobutton(self, text="6220", font=("times new roman", 14, "bold"), fg="tomato", bg="white")
        r4.config(variable=sel, value=4)
        r4.place(x=790, y=285)

        lbl_user = tk.Label(Frame_login, text="Air India\nAI 671", font=("Goudy old style", 15, "bold"), fg="tomato",
                            bg="white").place(x=90, y=135)
        lbl_user = tk.Label(Frame_login, text="BOM - MAA", font=("Goudy old style", 15, "bold"), fg="tomato",
                            bg="white").place(x=220, y=135)
        lbl_user = tk.Label(Frame_login, text="11:45 - 13:45", font=("Goudy old style", 15, "bold"), fg="tomato",
                            bg="white").place(x=390, y=135)

        Login_btn = tk.Button(Frame_login, command=lambda: Reservre_a_ticket_twoway.order_veg(self), text="Proceed",
                              fg="white", bg="tomato", bd=3,
                              font=("times new roman", 18)).place(x=630, y=330, width=200)

    def order_veg(self):
        logo = tk.PhotoImage(file=r"image/foo.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, relwidth=1, relheight=1)
        # frame created
        Frame_login = tk.Frame(self, bg="white")
        Frame_login.place(x=150, y=70, height=800, width=900)
        load = Image.open(r"image/san.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=190, y=170)

        sel1 = tk.IntVar()
        sel2 = tk.IntVar()
        sel3 = tk.IntVar()
        sel4 = tk.IntVar()
        sel5 = tk.IntVar()
        sel6 = tk.IntVar()
        sel7 = tk.IntVar()

        r1 = tk.Radiobutton(self, text="sandwich\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        r1.config(variable=sel1, value=1)
        r1.place(x=190, y=310)
        r2 = tk.Radiobutton(self, text="burger\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato", bg="white")
        r2.config(variable=sel2, value=2)
        r2.place(x=380, y=310)
        r3 = tk.Radiobutton(self, text="pizza\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato", bg="white")
        r3.config(variable=sel3, value=3)
        r3.place(x=580, y=310)
        r4 = tk.Radiobutton(self, text="noodles\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        r4.config(variable=sel4, value=4)
        r4.place(x=780, y=310)
        r5 = tk.Radiobutton(self, text="salad\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato", bg="white")
        r5.config(variable=sel5, value=5)
        r5.place(x=190, y=540)
        r6 = tk.Radiobutton(self, text="pancake\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        r6.config(variable=sel6, value=6)
        r6.place(x=380, y=540)
        r7 = tk.Radiobutton(self, text="pasta\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato", bg="white")
        r7.config(variable=sel7, value=7)
        r7.place(x=580, y=540)

        load = Image.open(r"image/burg.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=390, y=170)

        load = Image.open(r"image/pizzaa.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=590, y=170)

        load = Image.open(r"image/n.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=790, y=170)

        load = Image.open(r"image/salad.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=190, y=405)

        load = Image.open(r"image/pancake.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=390, y=405)

        load = Image.open(r"image/pasta.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=590, y=405)

        Login_btn = tk.Button(Frame_login, text="add", command=lambda: Reservre_a_ticket_twoway.order_non_veg(self),
                              fg="white", bg="#d77337", bd=1,
                              font=("times new roman", 18)).place(x=740, y=440, width=100, height=30)
        Login_btn = tk.Button(Frame_login, text="skip", command=lambda: Reservre_a_ticket_twoway.order_non_veg(self),
                              fg="white", bg="#d77337", bd=1,
                              font=("times new roman", 18)).place(x=620, y=440, width=100, height=30)

        tk.Button(self, width=18, height=2, text='V E G', pady=4,
                  command=lambda: Reservre_a_ticket_twoway.order_veg(self), border=0, bg='grey',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=150, y=70)
        # signup()
        tk.Button(self, width=18, height=2, text='N O N V E G', pady=4,
                  command=lambda: Reservre_a_ticket_twoway.order_non_veg(self), border=0, bg='#d77337',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=280, y=70)
        # bev()
        tk.Button(self, width=18, height=2, text='B E V', pady=4,
                  command=lambda: Reservre_a_ticket_twoway.order_bev(self), border=0, bg='#d77337',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=410, y=70)

    def order_non_veg(self):
        # Accessing the image file
        logo = tk.PhotoImage(file=r"image/foo.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, relwidth=1, relheight=1)
        # frame created
        Frame_login = tk.Frame(self, bg="white")
        Frame_login.place(x=150, y=70, height=800, width=900)
        load = Image.open(r"image/san.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=190, y=170)

        set1 = tk.IntVar()
        set2 = tk.IntVar()
        set3 = tk.IntVar()
        set4 = tk.IntVar()
        set5 = tk.IntVar()
        set6 = tk.IntVar()
        set7 = tk.IntVar()
        r1 = tk.Radiobutton(self, text="chicken nuggets\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        r1.config(variable=set1, value=1)
        r1.place(x=190, y=310)
        r2 = tk.Radiobutton(self, text="chicken pizza\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        r2.config(variable=set2, value=2)
        r2.place(x=380, y=310)
        r3 = tk.Radiobutton(self, text="chicken burger\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        r3.config(variable=set3, value=3)
        r3.place(x=580, y=310)
        r4 = tk.Radiobutton(self, text="chcken sausage\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        r4.config(variable=set4, value=4)
        r4.place(x=780, y=310)
        r5 = tk.Radiobutton(self, text="shawarma\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        r5.config(variable=set5, value=5)
        r5.place(x=190, y=540)
        r6 = tk.Radiobutton(self, text="chicken sandwich\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        r6.config(variable=set6, value=6)
        r6.place(x=380, y=540)
        r7 = tk.Radiobutton(self, text="lasagna\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        r7.config(variable=set7, value=7)
        r7.place(x=580, y=540)

        load = Image.open(r"image\chicken pizza.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=390, y=170)

        load = Image.open(r"image\chicken burger.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=590, y=170)

        load = Image.open(r"image\chicken sausage.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=790, y=170)

        load = Image.open(r"image\shawarma.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=190, y=405)

        load = Image.open(r"image\chicken sandwich.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=390, y=405)

        load = Image.open(r"image\lasagna.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=590, y=405)

        Login_btn = tk.Button(Frame_login, text="add", command=lambda: Reservre_a_ticket_twoway.order_bev(self),
                              fg="white", bg="#d77337", bd=1,
                              font=("times new roman", 18)).place(x=740, y=440, width=100, height=30)
        Login_btn = tk.Button(Frame_login, text="skip", command=lambda: Reservre_a_ticket_twoway.order_bev(self),
                              fg="white", bg="#d77337", bd=1,
                              font=("times new roman", 18)).place(x=620, y=440, width=100, height=30)
        tk.Button(self, width=18, height=2, text='V E G', pady=4,
                  command=lambda: Reservre_a_ticket_twoway.order_veg(self), border=0, bg='#d77337',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=150, y=70)
        # signup()
        tk.Button(self, width=18, height=2, text='N O N V E G', pady=4,
                  command=lambda: Reservre_a_ticket_twoway.order_non_veg(self), border=0, bg='grey',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=280, y=70)
        # bev()
        tk.Button(self, width=18, height=2, text='B E V', pady=4,
                  command=lambda: Reservre_a_ticket_twoway.order_bev(self), border=0, bg='#d77337',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=410, y=70)

    def order_bev(self):
        # Accessing the image file
        logo = tk.PhotoImage(file=r"image/foo.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, relwidth=1, relheight=1)
        # frame created
        Frame_login = tk.Frame(self, bg="white")
        Frame_login.place(x=150, y=70, height=800, width=900)
        load = Image.open(r"image/san.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=190, y=170)

        sel1 = tk.IntVar()
        sel2 = tk.IntVar()
        sel3 = tk.IntVar()
        sel4 = tk.IntVar()
        sel5 = tk.IntVar()
        sel6 = tk.IntVar()
        sel7 = tk.IntVar()
        r1 = tk.Radiobutton(self, text="masala tea\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        r1.config(variable=sel1, value=1)
        r1.place(x=190, y=310)
        r2 = tk.Radiobutton(self, text="coco-cola\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        r2.config(variable=sel2, value=2)
        r2.place(x=380, y=310)
        r3 = tk.Radiobutton(self, text="green tea\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        r3.config(variable=sel3, value=3)
        r3.place(x=580, y=310)
        r4 = tk.Radiobutton(self, text="non-alcoholic beer\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        r4.config(variable=sel4, value=4)
        r4.place(x=780, y=310)
        r5 = tk.Radiobutton(self, text="paper boat\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        r5.config(variable=sel5, value=5)
        r5.place(x=190, y=540)
        r6 = tk.Radiobutton(self, text="cappuccino\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        r6.config(variable=sel6, value=6)
        r6.place(x=380, y=540)
        r7 = tk.Radiobutton(self, text="cold coffee\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        r7.config(variable=sel7, value=7)
        r7.place(x=580, y=540)

        load = Image.open(r"image\coco-cola.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=390, y=170)

        load = Image.open(r"image\green tea.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=590, y=170)

        load = Image.open(r"image\non-alcoholic beer.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=790, y=170)

        load = Image.open(r"image\paper boat.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=190, y=405)

        load = Image.open(r"image\cappuccino.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=390, y=405)

        load = Image.open(r"image\cold coffee.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=590, y=405)

        Login_btn = tk.Button(Frame_login, text="add", command=lambda: Reservre_a_ticket_twoway.add_on_sev(self),
                              fg="white",
                              bg="#d77337", bd=1,
                              font=("times new roman", 18)).place(x=740, y=440, width=100, height=30)
        Login_btn = tk.Button(Frame_login, text="skip", command=lambda: Reservre_a_ticket_twoway.add_on_sev(self),
                              fg="white", bg="#d77337", bd=1,
                              font=("times new roman", 18)).place(x=620, y=440, width=100, height=30)

        tk.Button(self, width=18, height=2, text='V E G', pady=4,
                  command=lambda: Reservre_a_ticket_twoway.order_veg(self), border=0, bg='#d77337',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=150, y=70)
        # signup()
        tk.Button(self, width=18, height=2, text='N O N V E G', pady=4,
                  command=lambda: Reservre_a_ticket_twoway.order_non_veg(self), border=0, bg='#d77337',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=280, y=70)
        # bev()
        tk.Button(self, width=18, height=2, text='B E V', pady=4,
                  command=lambda: Reservre_a_ticket_twoway.order_bev(self), border=0, bg='grey',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=410, y=70)

    def add_on_sev(self):
        logo = tk.PhotoImage(file=r"image/za.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, relwidth=1, relheight=1)
        # frame created
        Frame_login = tk.Frame(self, bg="white")
        Frame_login.place(x=150, y=70, height=800, width=900)
        lbl_user = tk.Label(Frame_login, text="Add On Services", font=("Goudy old style", 20, "bold"), fg="skyblue4",
                            bg="white").place(x=40, y=35)
        txt_user = tk.Entry(Frame_login, font=("times new roman", 15), relief="ridge", bg="white")

        load = Image.open(r"image\seat.png")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=190, y=170)

        sel1 = tk.IntVar()
        sel2 = tk.IntVar()
        sel3 = tk.IntVar()
        sel4 = tk.IntVar()
        sel5 = tk.IntVar()
        sel6 = tk.IntVar()
        sel7 = tk.IntVar()

        r1 = tk.Radiobutton(self, text="Seat Plus\n₹150", font=("times new roman", 14, "bold"), fg="skyblue4",
                            bg="white")
        r1.config(variable=sel1, value=1)
        r1.place(x=190, y=310)
        r2 = tk.Radiobutton(self, text="Excess Baggage\n₹2000", font=("times new roman", 14, "bold"), fg="skyblue4",
                            bg="white")
        r2.config(variable=sel2, value=2)
        r2.place(x=380, y=310)
        r3 = tk.Radiobutton(self, text="Travel Assistance\n₹159", font=("times new roman", 14, "bold"), fg="skyblue4",
                            bg="white")
        r3.config(variable=sel3, value=3)
        r3.place(x=580, y=310)
        r4 = tk.Radiobutton(self, text="Blanket\n₹120", font=("times new roman", 14, "bold"), fg="skyblue4", bg="white")
        r4.config(variable=sel4, value=4)
        r4.place(x=780, y=310)
        r5 = tk.Radiobutton(self, text="Eye shade\n₹80", font=("times new roman", 14, "bold"), fg="skyblue4",
                            bg="white")
        r5.config(variable=sel5, value=5)
        r5.place(x=190, y=540)
        r6 = tk.Radiobutton(self, text="sports equipment\n₹250", font=("times new roman", 14, "bold"), fg="skyblue4",
                            bg="white")
        r6.config(variable=sel6, value=6)
        r6.place(x=380, y=540)
        r7 = tk.Radiobutton(self, text="fast forward\n₹250", font=("times new roman", 14, "bold"), fg="skyblue4",
                            bg="white")
        r7.config(variable=sel7, value=7)
        r7.place(x=580, y=540)

        load = Image.open(r"image\exc.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=390, y=170)

        load = Image.open(r"image\trav.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=590, y=170)

        load = Image.open(r"image\bla.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=790, y=170)

        load = Image.open(r"image\bla.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=190, y=405)

        load = Image.open(r"image\sports.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=390, y=405)

        load = Image.open(r"image\fast.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=590, y=405)

        Login_btn = tk.Button(Frame_login, text="add", command=lambda: Reservre_a_ticket_twoway.seat(self), fg="white",
                              bg="skyblue4", bd=1,
                              font=("times new roman", 18)).place(x=740, y=440, width=100, height=30)
        Login_btn = tk.Button(Frame_login, text="skip", command=lambda: Reservre_a_ticket_twoway.seat(self), fg="white",
                              bg="skyblue4", bd=1,
                              font=("times new roman", 18)).place(x=620, y=440, width=100, height=30)

    def seat(self):
        logo = tk.PhotoImage(file=r"image/insidee.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, relwidth=1, relheight=1)

        Frame_login = tk.Frame(self, bg="white")
        Frame_login.place(x=150, y=70, height=800, width=500)

        # Add Image
        logo1 = tk.PhotoImage(file=r"image/ro.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo1

        # Create button and image

        lbl_user = tk.Label(Frame_login, text="<- Exit", font=("Goudy old style", 15, "bold"), fg="skyblue4",
                            bg="white").place(x=20, y=35)
        lbl_user = tk.Label(Frame_login, text="Exit ->", font=("Goudy old style", 15, "bold"), fg="skyblue4",
                            bg="white").place(x=430, y=35)

        lbl_user = tk.Label(Frame_login, text="1", font=("Goudy old style", 15, "bold"), fg="skyblue4",
                            bg="white").place(x=250, y=85)

        lbl_user = tk.Label(Frame_login, text="2", font=("Goudy old style", 15, "bold"), fg="skyblue4",
                            bg="white").place(x=250, y=130)

        lbl_user = tk.Label(Frame_login, text="3", font=("Goudy old style", 15, "bold"), fg="skyblue4",
                            bg="white").place(x=250, y=175)

        lbl_user = tk.Label(Frame_login, text="4", font=("Goudy old style", 15, "bold"), fg="skyblue4",
                            bg="white").place(x=250, y=220)

        lbl_user = tk.Label(Frame_login, text="5", font=("Goudy old style", 15, "bold"), fg="skyblue4",
                            bg="white").place(x=250, y=265)

        lbl_user = tk.Label(Frame_login, text="6", font=("Goudy old style", 15, "bold"), fg="skyblue4",
                            bg="white").place(x=250, y=310)

        lbl_user = tk.Label(Frame_login, text="7", font=("Goudy old style", 15, "bold"), fg="skyblue4",
                            bg="white").place(x=250, y=355)

        lbl_user = tk.Label(Frame_login, text="8", font=("Goudy old style", 15, "bold"), fg="skyblue4",
                            bg="white").place(x=250, y=400)

        lbl_user = tk.Label(Frame_login, text="9", font=("Goudy old style", 15, "bold"), fg="skyblue4",
                            bg="white").place(x=250, y=445)
        lbl_user = tk.Label(Frame_login, text="10", font=("Goudy old style", 15, "bold"), fg="skyblue4",
                            bg="white").place(x=250, y=445)

        lbl_user = tk.Label(Frame_login, text="<- Exit", font=("Goudy old style", 15, "bold"), fg="skyblue4",
                            bg="white").place(x=20, y=495)
        lbl_user = tk.Label(Frame_login, text="4", font=("Goudy old style", 15, "bold"), fg="skyblue4",
                            bg="white").place(x=430, y=495)

        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=490, y=156)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=540, y=156)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=590, y=156)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=190, y=156)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=240, y=156)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=290, y=156)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=190, y=196)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=240, y=196)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=290, y=196)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=490, y=196)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=540, y=196)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=590, y=196)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=190, y=236)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=240, y=236)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=290, y=236)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=490, y=236)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=540, y=236)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=590, y=236)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=190, y=276)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=240, y=276)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=290, y=276)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=490, y=276)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=540, y=276)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=590, y=276)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=190, y=316)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=240, y=316)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=290, y=316)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=490, y=316)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=540, y=316)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=590, y=316)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=190, y=356)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=240, y=356)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=290, y=356)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=490, y=356)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=540, y=356)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=590, y=356)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=190, y=396)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=240, y=396)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=290, y=396)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=490, y=396)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=540, y=396)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=590, y=396)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=190, y=436)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=240, y=436)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=290, y=436)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=490, y=436)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=540, y=436)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=590, y=436)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=190, y=486)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=240, y=486)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=290, y=486)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=490, y=486)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=540, y=486)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=590, y=486)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=190, y=526)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=240, y=526)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=290, y=526)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=490, y=526)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=540, y=526)
        img = tk.Button(self, image=BGlabel.image,
                        borderwidth=0).place(x=590, y=526)
        Login_btn = tk.Button(self, text="Next", command="y", fg="white",
                              bg="skyblue4", bd=1,
                              font=("times new roman", 18)).place(x=370, y=590, width=100, height=30)
class Flight_agenda(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Accessing the image file
        logo = tk.PhotoImage(file="flight_agenda.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, relwidth=1, relheight=1)
        # frame created
        Frame_login = tk.Frame(self, bg="white")
        Frame_login.place(x=150, y=150, height=390, width=700)
        title = tk.Label(Frame_login, text="Flight Status", font=("times new roman", 25, "bold"), fg="burlywood4",
                         bg="white").place(x=30, y=30)

        lbl_user = tk.Label(Frame_login, text="Departing", font=("Goudy old style", 15, "bold"), fg="burlywood4",
                            bg="white").place(x=50, y=95)
        txt_user = tk.Entry(Frame_login, font=("times new roman", 15), relief="ridge", bg="white")
        txt_user.place(x=50, y=125, width=280, height=35)
        lbl_user = tk.Label(Frame_login, text="Arriving", font=("Goudy old style", 15, "bold"), fg="burlywood4",
                            bg="white").place(x=50, y=175)
        txt_user = tk.Entry(Frame_login, font=("times new roman", 15), relief="ridge", bg="white")
        txt_user.place(x=50, y=205, width=280, height=35)
        lbl_user = tk.Label(Frame_login, text="Flight Number", font=("Goudy old style", 15, "bold"), fg="burlywood4",
                            bg="white").place(x=50, y=255)
        txt_user = tk.Entry(Frame_login, font=("times new roman", 15), relief="ridge", bg="white")
        txt_user.place(x=50, y=285, width=280, height=35)

        lbl_user = tk.Label(Frame_login, text="Select date", font=("Goudy old style", 15, "bold"), fg="burlywood4",
                            bg="white").place(x=370, y=175)
        txt_user = tk.Entry(Frame_login, font=("times new roman", 15), relief="ridge", bg="white")
        txt_user.place(x=370, y=205, width=280, height=35)
        Login_btn = tk.Button(Frame_login, text="check status",
                              command=lambda: controller.show_frame(Flight_agenda_status), fg="white", bg="burlywood4",
                              bd=2,
                              font=("times new roman", 16)).place(x=250, y=340, width="200")
class Flight_agenda_status(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Accessing the image file
        logo = tk.PhotoImage(file="flight_agenda.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, relwidth=1, relheight=1)
        # frame created
        Frame_login = tk.Frame(self, bg="white")
        Frame_login.place(x=100, y=50, height=600, width=1199)
        treev = ttk.Treeview(Frame_login, selectmode='browse')

        # Calling pack method w.r.to treeview

        treev.pack(side='left')

        # Constructing vertical scrollbar
        # with treeview

        verscrlbar = ttk.Scrollbar(Frame_login,

                                   orient="horizontal",

                                   command=treev.yview)

        # Calling pack method w.r.to verical
        # scrollbar

        verscrlbar.pack(side='left', fill='x')

        # Configuring treeview

        treev.configure(xscrollcommand=verscrlbar.set)

        # Defining number of columns

        treev["columns"] = ("1", "2", "3", "4", "5")

        # Defining heading

        treev['show'] = 'headings'

        # Assigning the width and anchor to  the
        # respective columns

        treev.column("1", width=200, anchor='se')

        treev.column("2", width=200, anchor='se')

        treev.column("3", width=200, anchor='se')

        treev.column("4", width=200, anchor='se')

        treev.column("5", width=200, anchor='se')

        # Assigning the heading names to the
        # respective columns

        treev.heading("1", text="Flight Id")

        treev.heading("2", text="To")

        treev.heading("3", text="Departure")

        treev.heading("4", text="Arrival")

        treev.heading("5", text="Status")

        # Inserting the items and their features to the
        # columns built

        treev.insert("", 'end', text="L1",

                     values=("6E 5365", "BOM -> MAA", "13:40", "19:15", "On time"))

        treev.insert("", 'end', text="L2",

                     values=("6E 5365", "BOM -> MAA", "13:40", "19:15", "On time"))

        treev.insert("", 'end', text="L3",

                     values=("6E 5365", "BOM -> MAA", "13:40", "19:15", "On time"))

        treev.insert("", 'end', text="L4",

                     values=("6E 5365", "BOM -> MAA", "13:40", "19:15", "On time"))

        treev.insert("", 'end', text="L5",

                     values=("6E 5365", "BOM -> MAA", "13:40", "19:15", "On time"))

        treev.insert("", 'end', text="L6",

                     values=("SpiceJet", "SG-521", "4221", "4975"))
        Login_btn = tk.Button(Frame_login, text="Close", command=lambda: controller.show_frame(Home_page),
                              fg="white", bg="grey", bd=1,
                              font=("times new roman", 18)).place(x=580, y=550, width=100, height=30)
class Order_and_munch_veg(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Accessing the image file
        logo = tk.PhotoImage(file=r"image/foo.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, relwidth=1, relheight=1)
        # frame created
        Frame_login = tk.Frame(self, bg="white")
        Frame_login.place(x=150, y=70, height=800, width=900)
        load = Image.open(r"image/san.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=190, y=170)

        sel1 = tk.IntVar()
        sel2 = tk.IntVar()
        sel3 = tk.IntVar()
        sel4 = tk.IntVar()
        sel5 = tk.IntVar()
        sel6 = tk.IntVar()
        sel7 = tk.IntVar()

        r1 = tk.Radiobutton(self, text="sandwich\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        r1.config(variable=sel1, value=1)
        r1.place(x=190, y=310)
        r2 = tk.Radiobutton(self, text="burger\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato", bg="white")
        r2.config(variable=sel2, value=2)
        r2.place(x=380, y=310)
        r3 = tk.Radiobutton(self, text="pizza\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato", bg="white")
        r3.config(variable=sel3, value=3)
        r3.place(x=580, y=310)
        r4 = tk.Radiobutton(self, text="noodles\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        r4.config(variable=sel4, value=4)
        r4.place(x=780, y=310)
        r5 = tk.Radiobutton(self, text="salad\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato", bg="white")
        r5.config(variable=sel5, value=5)
        r5.place(x=190, y=540)
        r6 = tk.Radiobutton(self, text="pancake\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        r6.config(variable=sel6, value=6)
        r6.place(x=380, y=540)
        r7 = tk.Radiobutton(self, text="pasta\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato", bg="white")
        r7.config(variable=sel7, value=7)
        r7.place(x=580, y=540)

        load = Image.open(r"image/burg.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=390, y=170)

        load = Image.open(r"image/pizzaa.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=590, y=170)

        load = Image.open(r"image/n.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=790, y=170)

        load = Image.open(r"image/salad.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=190, y=405)

        load = Image.open(r"image/pancake.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=390, y=405)

        load = Image.open(r"image/pasta.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=590, y=405)

        Login_btn = tk.Button(Frame_login, text="add", command=lambda: controller.show_frame(Order_and_munch_non_veg),
                              fg="white", bg="#d77337", bd=1,
                              font=("times new roman", 18)).place(x=740, y=440, width=100, height=30)
        Login_btn = tk.Button(Frame_login, text="skip", command=lambda: controller.show_frame(Order_and_munch_non_veg),
                              fg="white", bg="#d77337", bd=1,
                              font=("times new roman", 18)).place(x=620, y=440, width=100, height=30)
        Login_btn = tk.Button(Frame_login, text="Close", command=lambda: controller.show_frame(Home_page),
                              fg="white", bg="#d77337", bd=1,
                              font=("times new roman", 18)).place(x=680, y=480, width=100, height=30)

        tk.Button(self, width=18, height=2, text='V E G', pady=4,
                  command=lambda: controller.show_frame(Order_and_munch_veg), border=0, bg='grey',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=150, y=70)
        # signup()
        tk.Button(self, width=18, height=2, text='N O N V E G', pady=4,
                  command=lambda: controller.show_frame(Order_and_munch_non_veg), border=0, bg='#d77337',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=280, y=70)
        # bev()
        tk.Button(self, width=18, height=2, text='B E V', pady=4,
                  command=lambda: controller.show_frame(Order_and_munch_bev), border=0, bg='#d77337',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=410, y=70)
class Order_and_munch_non_veg(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Accessing the image file
        logo = tk.PhotoImage(file=r"image/foo.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, relwidth=1, relheight=1)
        # frame created
        Frame_login = tk.Frame(self, bg="white")
        Frame_login.place(x=150, y=70, height=800, width=900)
        load = Image.open(r"image/san.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=190, y=170)

        set1 = tk.IntVar()
        set2 = tk.IntVar()
        set3 = tk.IntVar()
        set4 = tk.IntVar()
        set5 = tk.IntVar()
        set6 = tk.IntVar()
        set7 = tk.IntVar()
        r1 = tk.Radiobutton(self, text="chicken nuggets\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        r1.config(variable=set1, value=1)
        r1.place(x=190, y=310)
        r2 = tk.Radiobutton(self, text="chicken pizza\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        r2.config(variable=set2, value=2)
        r2.place(x=380, y=310)
        r3 = tk.Radiobutton(self, text="chicken burger\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        r3.config(variable=set3, value=3)
        r3.place(x=580, y=310)
        r4 = tk.Radiobutton(self, text="chcken sausage\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        r4.config(variable=set4, value=4)
        r4.place(x=780, y=310)
        r5 = tk.Radiobutton(self, text="shawarma\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        r5.config(variable=set5, value=5)
        r5.place(x=190, y=540)
        r6 = tk.Radiobutton(self, text="chicken sandwich\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        r6.config(variable=set6, value=6)
        r6.place(x=380, y=540)
        r7 = tk.Radiobutton(self, text="lasagna\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        r7.config(variable=set7, value=7)
        r7.place(x=580, y=540)

        load = Image.open(r"image\chicken pizza.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=390, y=170)

        load = Image.open(r"image\chicken burger.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=590, y=170)

        load = Image.open(r"image\chicken sausage.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=790, y=170)

        load = Image.open(r"image\shawarma.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=190, y=405)

        load = Image.open(r"image\chicken sandwich.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=390, y=405)

        load = Image.open(r"image\lasagna.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=590, y=405)

        Login_btn = tk.Button(Frame_login, text="add", command=lambda: controller.show_frame(Order_and_munch_bev),
                              fg="white", bg="#d77337", bd=1,
                              font=("times new roman", 18)).place(x=740, y=440, width=100, height=30)
        Login_btn = tk.Button(Frame_login, text="skip", command=lambda: controller.show_frame(Order_and_munch_bev),
                              fg="white", bg="#d77337", bd=1,
                              font=("times new roman", 18)).place(x=620, y=440, width=100, height=30)
        Login_btn = tk.Button(Frame_login, text="Close", command=lambda: controller.show_frame(Home_page),
                              fg="white", bg="#d77337", bd=1,
                              font=("times new roman", 18)).place(x=680, y=480, width=100, height=30)

        tk.Button(self, width=18, height=2, text='V E G', pady=4,
                  command=lambda: controller.show_frame(Order_and_munch_veg), border=0, bg='#d77337',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=150, y=70)
        # signup()
        tk.Button(self, width=18, height=2, text='N O N V E G', pady=4,
                  command=lambda: controller.show_frame(Order_and_munch_non_veg), border=0, bg='grey',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=280, y=70)
        # bev()
        tk.Button(self, width=18, height=2, text='B E V', pady=4,
                  command=lambda: controller.show_frame(Order_and_munch_bev), border=0, bg='#d77337',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=410, y=70)
class Order_and_munch_bev(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Accessing the image file
        logo = tk.PhotoImage(file=r"image/foo.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, relwidth=1, relheight=1)
        # frame created
        Frame_login = tk.Frame(self, bg="white")
        Frame_login.place(x=150, y=70, height=800, width=900)
        load = Image.open(r"image/san.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=190, y=170)

        sel1 = tk.IntVar()
        sel2 = tk.IntVar()
        sel3 = tk.IntVar()
        sel4 = tk.IntVar()
        sel5 = tk.IntVar()
        sel6 = tk.IntVar()
        sel7 = tk.IntVar()
        r1 = tk.Radiobutton(self, text="masala tea\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        r1.config(variable=sel1, value=1)
        r1.place(x=190, y=310)
        r2 = tk.Radiobutton(self, text="coco-cola\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        r2.config(variable=sel2, value=2)
        r2.place(x=380, y=310)
        r3 = tk.Radiobutton(self, text="green tea\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        r3.config(variable=sel3, value=3)
        r3.place(x=580, y=310)
        r4 = tk.Radiobutton(self, text="non-alcoholic beer\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        r4.config(variable=sel4, value=4)
        r4.place(x=780, y=310)
        r5 = tk.Radiobutton(self, text="paper boat\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        r5.config(variable=sel5, value=5)
        r5.place(x=190, y=540)
        r6 = tk.Radiobutton(self, text="cappuccino\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        r6.config(variable=sel6, value=6)
        r6.place(x=380, y=540)
        r7 = tk.Radiobutton(self, text="cold coffee\n₹250/$3", font=("times new roman", 14, "bold"), fg="tomato",
                            bg="white")
        r7.config(variable=sel7, value=7)
        r7.place(x=580, y=540)

        load = Image.open(r"image\coco-cola.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=390, y=170)

        load = Image.open(r"image\green tea.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=590, y=170)

        load = Image.open(r"image\non-alcoholic beer.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=790, y=170)

        load = Image.open(r"image\paper boat.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=190, y=405)

        load = Image.open(r"image\cappuccino.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=390, y=405)

        load = Image.open(r"image\cold coffee.jpeg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=590, y=405)

        Login_btn = tk.Button(Frame_login, text="add", command=lambda: controller.show_frame(Home_page), fg="white",
                              bg="#d77337", bd=1,
                              font=("times new roman", 18)).place(x=740, y=440, width=100, height=30)
        Login_btn = tk.Button(Frame_login, text="skip", command=lambda: controller.show_frame(Home_page),
                              fg="white", bg="#d77337", bd=1,
                              font=("times new roman", 18)).place(x=620, y=440, width=100, height=30)
        Login_btn = tk.Button(Frame_login, text="Close", command=lambda: controller.show_frame(Home_page),
                              fg="white", bg="#d77337", bd=1,
                              font=("times new roman", 18)).place(x=680, y=480, width=100, height=30)

        tk.Button(self, width=18, height=2, text='V E G', pady=4,
                  command=lambda: controller.show_frame(Order_and_munch_veg), border=0, bg='#d77337',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=150, y=70)
        # signup()
        tk.Button(self, width=18, height=2, text='N O N V E G', pady=4,
                  command=lambda: controller.show_frame(Order_and_munch_non_veg), border=0, bg='#d77337',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=280, y=70)
        # bev()
        tk.Button(self, width=18, height=2, text='B E V', pady=4,
                  command=lambda: controller.show_frame(Order_and_munch_bev), border=0, bg='grey',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=410, y=70)
class Baggage_domestic(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Accessing the image file
        logo = tk.PhotoImage(file=r"image/re1.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=1000, y=0, relwidth=1, relheight=1)
        # frame created
        Frame_login = tk.Frame(self, bg="#d77337")
        Frame_login.place(x=0, y=0, height=43, width=1450)
        Frame1_login = tk.Frame(self, bg="white")
        Frame1_login.place(x=0, y=43, height=700, width=1000)
        quote = ["Domestic baggage norms", ]
        quote = """
        Domestic baggage norms
        IndiGo reserves the right to refuse carriage of Baggage with certain restricted items.
        A description of such items is set out below:
        a) Items which are not properly packed in suitcases or other suitable containers;
        b) Items which are likely to endanger the aircraft or persons or property on-board the aircraft, as specified 
        in the International Civil Aviation Organization (ICAO) Technical Instructions for the Safe Transport of 
        Dangerous Goods by Air, the International Air Transport Association (IATA) Dangerous Goods Regulations and 
        dangerous goods as per local laws and applicable regulations and as per IndiGo’s terms and conditions;
        c) Items, the carriage of which is prohibited by applicable laws, regulations or orders;
        d) Except as expressly permitted in the Conditions of Carriage, explosives, fireworks and flares,  fireworks, 
        pistol caps, swords, knives and similar items;
        e) Gases such as compressed gases, liquefied gases, refrigerated liquefied gases, dissolved gases, 
        adsorbed gases, flammable, non-flammable and poisonous gases such as butane oxygen and liquid nitrogen, 
        avalanche rescue backpacks and medical oxygen etc.;
        f) Flammable liquids and solids such as lighter refills, lighter fuel, flammable paints, thinners, used camping 
        stoves or fuel containers, used internal combustion or fuel cell engines, matches, fire-lighters, lighters that 
        are required to be inverted before ignition or are powered by lithium batteries, copra, sodium, potassium etc.;
        g) Oxidizing substances and organic peroxides such as bleaches, aluminium nitrate etc.;
        h) Toxic and infectious substances such as pesticides, insecticides, weed-killers, potassium cyanide, samples 
        for testing of infectious diseases etc.;
        i) Radioactive material;
        j) Corrosives such as acids, alkalis, mercury and wet cell batteries and apparatus containing mercury;
        Other dangerous substances and articles including environmentally hazardous substances such as magnetised 
        materials, materials with narcotic, noxious, offensive or irritating properties, e-cigarettes etc.;

        """
        text2 = tk.Label(Frame1_login, text=quote, font=("Goudy old style", 10, "bold"), fg="gray",
                         bg="white")
        text2.place(x=0, y=0, height=600, width=980)
        tk.Button(self, width=18, height=2, text='D O M E S T I C', pady=4,
                  command=lambda: controller.show_frame(Baggage_domestic), border=0, bg='grey',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=0, y=0)
        # signup()
        tk.Button(self, width=18, height=2, text='I N T E R N A T I O N A L', pady=4,
                  command=lambda: controller.show_frame(Baggage_international), border=0,
                  bg='#d77337',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=130, y=0)
        tk.Button(Frame1_login, width=18, text='Close',
                  command=lambda: controller.show_frame(Home_page),
                  bg='#d77337',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=470, y=550)
class Baggage_international(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Accessing the image file
        logo = tk.PhotoImage(file=r"image/re1.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=1000, y=0, relwidth=1, relheight=1)
        # frame created
        Frame_login = tk.Frame(self, bg="#d77337")
        Frame_login.place(x=0, y=0, height=43, width=1450)
        Frame1_login = tk.Frame(self, bg="white")
        Frame1_login.place(x=0, y=43, height=700, width=1000)
        quote = """
        International Baggage Norms
        We reserves the right to refuse carriage of such Baggage or such items found in the Baggage as stated below. 
        a) Items which are not properly packed in suitcases or other suitable containers in order to ensure safe carr
        iage with ordinary care and handling,
        b) Items which are likely to endanger the aircraft or persons or property on board the aircraft such as those
         specified in the International Civil Aviation Organization (ICAO) Technical Instructions for the Safe Transport
          of Dangerous Goods by Air, the International Air Transport Association (IATA) Dangerous Goods Regulations,
           Dangerous Goods as per local laws and applicable regulations and as per our own Terms and Conditions,
        c) Items, the carriage of which is prohibited by applicable laws, regulations or orders,
        d) Compressed gasses: deeply refrigerated, flammable, non-flammable and poisonous such as butane oxygen,
         liquid nitrogen, aqualung cylinders and compressed gas cylinders,
        e) Corrosives items such as acids, alkalis, mercury and wet cell batteries and apparatus containing mercury,
        f) Explosives, munitions, fireworks and flares, ammunition including blank cartridges, handguns, ireworks, 
        pistol caps, swords, knives and similar items,
        g) Small lithium battery-powered vehicles such as airwheels, solowheels, hoverboards, mini-segways and balance wheels,
        h) Flammable liquids and solids such as lighter refills, lighter fuel, matches, paints, thinners, fire-lighters,
         lighters that need inverting before ignition, matches (these may be carried on the person), radioactive material, 
         briefcases and attaché case with installed alarm devices,
        i) Oxidizing materials such as bleaching powder and peroxides,
        j) Poisons and infectious substances such as insecticides, weed-killers and live virus materials,
        k) Fish (including, sea food), animals, birds, insects in any form, whether live and/or dead and/or frozen and/or dried,
        l) Anything that possesses and/or is capable of possessing and/or emitting a conspicuous and/or offensive odour,
        m) Other dangerous articles such as magnetized materials, offensive or irritating materials,
        n) Human or animal remains,
        o) Live or dead animals,
        p) Items, which, in our reasonable opinion, are unsuitable for carriage by reason of their weight, shape, size or character.
        q) Lithium Batteries can cause safety hazards. Accordingly, batteries will not be allowed in checked-in baggage.
         Customers, may be permitted, subject to airport security clearance, to carry a maximum of two (2) spare lithium 
         batteries with a maximum of 8gms lithium content and 160 Wh, in hand baggage only, provided that they are packaged 
         in their original retail packaging or each is packaged in separate plastic bags with the exposed terminals taped.
        """

        text2 = tk.Label(Frame1_login, text=quote, font=("Goudy old style", 10, "bold"), fg="gray",
                         bg="white")
        text2.place(x=0, y=0, height=600, width=980)
        tk.Button(self, width=18, height=2, text='D O M E S T I C', pady=4,
                  command=lambda: controller.show_frame(Baggage_domestic), border=0, bg='#d77337',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=0, y=0)
        # signup()
        tk.Button(self, width=18, height=2, text='I N T E R N A T I O N A L', pady=4,
                  command=lambda: controller.show_frame(Baggage_international), border=0,
                  bg='grey',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=130, y=0)
        tk.Button(Frame1_login, width=18, text='Close',
                  command=lambda: controller.show_frame(Home_page),
                  bg='#d77337',
                  fg='white', activebackground='grey', activeforeground='grey').place(x=470, y=570)
class Add_on_services(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Accessing the image file
        logo = tk.PhotoImage(file=r"image/za.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, relwidth=1, relheight=1)
        # frame created
        Frame_login = tk.Frame(self, bg="white")
        Frame_login.place(x=150, y=70, height=800, width=900)
        lbl_user = tk.Label(Frame_login, text="Add On Services", font=("Goudy old style", 20, "bold"), fg="skyblue4",
                            bg="white").place(x=40, y=35)
        txt_user = tk.Entry(Frame_login, font=("times new roman", 15), relief="ridge", bg="white")

        load = Image.open(r"image\seat.png")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=190, y=170)

        sel1 = tk.IntVar()
        sel2 = tk.IntVar()
        sel3 = tk.IntVar()
        sel4 = tk.IntVar()
        sel5 = tk.IntVar()
        sel6 = tk.IntVar()
        sel7 = tk.IntVar()

        r1 = tk.Radiobutton(self, text="Seat Plus\n₹150", font=("times new roman", 14, "bold"), fg="skyblue4",
                            bg="white")
        r1.config(variable=sel1, value=1)
        r1.place(x=190, y=310)
        r2 = tk.Radiobutton(self, text="Excess Baggage\n₹2000", font=("times new roman", 14, "bold"), fg="skyblue4",
                            bg="white")
        r2.config(variable=sel2, value=2)
        r2.place(x=380, y=310)
        r3 = tk.Radiobutton(self, text="Travel Assistance\n₹159", font=("times new roman", 14, "bold"), fg="skyblue4",
                            bg="white")
        r3.config(variable=sel3, value=3)
        r3.place(x=580, y=310)
        r4 = tk.Radiobutton(self, text="Blanket\n₹120", font=("times new roman", 14, "bold"), fg="skyblue4", bg="white")
        r4.config(variable=sel4, value=4)
        r4.place(x=780, y=310)
        r5 = tk.Radiobutton(self, text="Eye shade\n₹80", font=("times new roman", 14, "bold"), fg="skyblue4",
                            bg="white")
        r5.config(variable=sel5, value=5)
        r5.place(x=190, y=540)
        r6 = tk.Radiobutton(self, text="sports equipment\n₹250", font=("times new roman", 14, "bold"), fg="skyblue4",
                            bg="white")
        r6.config(variable=sel6, value=6)
        r6.place(x=380, y=540)
        r7 = tk.Radiobutton(self, text="fast forward\n₹250", font=("times new roman", 14, "bold"), fg="skyblue4",
                            bg="white")
        r7.config(variable=sel7, value=7)
        r7.place(x=580, y=540)

        load = Image.open(r"image\exc.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=390, y=170)

        load = Image.open(r"image\trav.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=590, y=170)

        load = Image.open(r"image\bla.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=790, y=170)

        load = Image.open(r"image\bla.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=190, y=405)

        load = Image.open(r"image\sports.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=390, y=405)

        load = Image.open(r"image\fast.jpg")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.place(x=590, y=405)

        Login_btn = tk.Button(Frame_login, text="add", command=lambda: controller.show_frame(Home_page), fg="white",
                              bg="skyblue4", bd=1,
                              font=("times new roman", 18)).place(x=740, y=440, width=100, height=30)
        Login_btn = tk.Button(Frame_login, text="skip", command=lambda: controller.show_frame(Home_page), fg="white",
                              bg="skyblue4", bd=1,
                              font=("times new roman", 18)).place(x=620, y=440, width=100, height=30)
        Login_btn = tk.Button(Frame_login, text="Close", command=lambda: controller.show_frame(Home_page), fg="white",
                              bg="skyblue4", bd=1,
                              font=("times new roman", 18)).place(x=680, y=480, width=100, height=30)
class Critiques(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Accessing the image file
        logo = tk.PhotoImage(file=r"image/za.png")
        BGlabel = tk.Label(self, image=logo)
        BGlabel.image = logo
        BGlabel.place(x=0, y=0, relwidth=1, relheight=1)
        # frame created
        Frame_login = tk.Frame(self, bg="white")
        Frame_login.place(x=100, y=50, height=590, width=700)
        course = ["Appreciation", "Suggestion", "Complaint", "Request", "Enquiry"]

        ## TO ADD LABELS ##

        title = tk.Label(Frame_login, text="Critiques", font=("times new roman", 25, "bold"), fg="burlywood4",
                         bg="white").place(x=30, y=30)

        lbl_user = tk.Label(Frame_login, text="Name", font=("Goudy old style", 15, "bold"), fg="burlywood4",
                            bg="white").place(x=50, y=95)
        txt_user = tk.Entry(Frame_login, font=("times new roman", 15), relief="ridge", bg="white")
        txt_user.place(x=50, y=125, width=280, height=35)
        lbl_user = tk.Label(Frame_login, text="Mail Id", font=("Goudy old style", 15, "bold"), fg="burlywood4",
                            bg="white").place(x=370, y=95)
        txt_user = tk.Entry(Frame_login, font=("times new roman", 15), relief="ridge", bg="white")
        txt_user.place(x=370, y=125, width=280, height=35)
        lbl_user = tk.Label(Frame_login, text="Orgin", font=("Goudy old style", 15, "bold"), fg="burlywood4",
                            bg="white").place(x=50, y=175)
        txt_user = tk.Entry(Frame_login, font=("times new roman", 15), bg="white")
        txt_user.place(x=50, y=205, width=280, height=35)
        lbl_user = tk.Label(Frame_login, text="Enter your feedback", font=("Goudy old style", 15, "bold"),
                            fg="burlywood4",
                            bg="white").place(x=50, y=365)
        txt_user = tk.Entry(Frame_login, font=("times new roman", 15), relief="groove", bg="white")
        txt_user.place(x=50, y=405, width=350, height=85)

        lbl_user = tk.Label(Frame_login, text="kind of feedback", font=("Goudy old style", 15, "bold"), fg="burlywood4",
                            bg="white").place(x=50, y=265)
        cmb = ttk.Combobox(self, value=course, width=30, height=30)
        cmb.grid(row=10, column=10, padx=30, pady=350)
        cmb.place(x=150, y=345, width="287", height="40")
        lbl_user = tk.Label(Frame_login, text="Destination", font=("Goudy old style", 15, "bold"), fg="burlywood4",
                            bg="white").place(x=370, y=175)
        txt_user = tk.Entry(Frame_login, font=("times new roman", 15), relief="ridge", bg="white")
        txt_user.place(x=370, y=205, width=280, height=35)
        Login_btn = tk.Button(Frame_login, text="Send", command=lambda: controller.show_frame(Home_page), fg="white",
                              bg="burlywood4",
                              font=("times new roman", 16)).place(x=200, y=500, height=50, width=150)
        Login_btn = tk.Button(Frame_login, text="Close", command=lambda: controller.show_frame(Home_page), fg="white",
                              bg="burlywood4", bd=2,
                              font=("times new roman", 16)).place(x=400, y=500, height=50, width="150")

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
con.commit()