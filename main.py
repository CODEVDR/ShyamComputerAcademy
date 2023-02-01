import base64
import io
import tkinter.messagebox as msg
from datetime import datetime as dt
from tkinter import *

import mysql.connector as sqlctr
import win32api
from PIL import Image, ImageTk

# For Functions
from module import submit, upload_file

"""
mFrame & mFrame1 are 2 main Frames mFrame For storing data mFrame1 for seeing data 
tmpFrame That Stores Different Buttons With Diff Funcanalities
"""

# Frontend
root = Tk()
root.title("USER INFO | CodeWithVdr")
root.iconbitmap("assets/icon.ico")
root.minsize(600, 790)
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
# CODE
# Heading


def back():
    tmpFrame()


mFrame = Frame(root)
Button(mFrame, text=u"\u25C0 Back", command=back).pack(anchor=W)
Label(mFrame, text="USER APPLICATION", font="impact 19 bold",
      relief=SOLID, borderwidth=3).pack(pady=20)

frame_img = Frame(mFrame)


def upld_file():
    global file
    file = upload_file(image_area)
    if file[0] == 0:
        msg.showwarning("Warning! | CodeWithVdr", "No Image Selected")
    else:
        msg.showinfo("Image | CodeWithVdr", f"{file[1]} selected")


# Setting Image To Button
Label(frame_img, text="IMAGE", relief=SOLID,
      font="Corbel 12 bold underline", fg="purple").pack()
img = Image.open("assets/up_img.png")
r_img = img.resize((200, 200))
image = ImageTk.PhotoImage(r_img)
image_area = Button(frame_img, image=image, width=200,
                    height=200, relief=GROOVE, command=upld_file)
image_area.pack()
frame_img.pack()

frame_fields = Frame(mFrame)
# Variables
name = StringVar()
fname = StringVar()
adhrno = IntVar()
addr = StringVar()
mobno = IntVar()
bldgrp = StringVar()
dob = StringVar()
#Entries and Labels
Label(frame_fields, text="Name",
      relief=SOLID, font="Corbel 12 bold underline", fg="purple").pack(anchor=W)
Entry(frame_fields, textvariable=name,
      relief=SOLID, font="Corbel 15 bold", width=50).pack()

Label(frame_fields, text="Father's Name",
      relief=SOLID, font="Corbel 12 bold underline", fg="purple").pack(anchor=W)
Entry(frame_fields, textvariable=fname,
      relief=SOLID, font="Corbel 15 bold", width=50).pack()

Label(frame_fields, text="Registration Number",
      relief=SOLID, font="Corbel 12 bold underline", fg="purple").pack(anchor=W)
Entry(frame_fields, textvariable=adhrno,
      relief=SOLID, font="Corbel 15 bold", width=50).pack()

Label(frame_fields, text="Address",
      relief=SOLID, font="Corbel 12 bold underline", fg="purple").pack(anchor=W)
Entry(frame_fields, textvariable=addr,
      relief=SOLID, font="Corbel 15 bold", width=50).pack()

Label(frame_fields, text="Mobile Number",
      relief=SOLID, font="Corbel 12 bold underline", fg="purple").pack(anchor=W)
Entry(frame_fields, textvariable=mobno,
      relief=SOLID, font="Corbel 15 bold", width=50).pack()

Label(frame_fields, text="Blood Group",
      relief=SOLID, font="Corbel 12 bold underline", fg="purple").pack(anchor=W)
Entry(frame_fields, textvariable=bldgrp,
      relief=SOLID, font="Corbel 15 bold", width=50).pack()

Label(frame_fields, text="DOB", relief=SOLID, font="Corbel 12 bold underline",
      fg="purple").pack(anchor=W)
Entry(frame_fields, textvariable=dob, relief=SOLID,
      font="Corbel 15 bold", width=50).pack()

# Function For Storing Values


def sub():
    try:
        if name.get() == "" or fname.get() == "" or adhrno.get() == "" or addr.get() == "" or mobno.get() == "" or bldgrp.get() == "" or dob.get() == "" or file == "":
            msg.showerror("Error | CodeWithVdr ", "Fields Cant Be Empty")
        else:
            v = msg.askquestion("Submit | CodeWithVdr",
                                "Do You Want To Submit ?")
            if v == "yes":
                an = submit(hs, us, pw, name.get(), fname.get(), adhrno.get(
                ), addr.get(), mobno.get(), bldgrp.get(), dob.get(), file[0])
                if an != 0:
                    msg.showinfo("Sucess | CodeWithVdr ", "Stored Sucessfully")
                else:
                    msg.showerror(
                        "Error | CodeWithVdr ", "An Unexpected Error Occured We Will Fix it Soon.")
    except:
        msg.showerror("Error | CodeWithVdr", "Please Select an Image.")


Button(frame_fields, text="Submit", relief=SOLID, font="Corbel 12 bold", command=sub, fg="purple",
       activebackground="violet", activeforeground="purple", width=40).pack(pady=10)
frame_fields.pack(pady=30)
# 17-01-2023 02:46 PM
# CODE FROM HERE
#
# =========================================================================================================
mFrame1 = Frame(root)
bk = Button(mFrame1, text=u"\u25C0 Back", command=back)
bk.pack(anchor=W)
# Frame For Getting Required Information To SEarch
# Funtions That Fetchs Data From Server And Responds


def see():
    if name1.get() != "" or adhrno1.get() != "":
        def v():
            try:
                cd_con = sqlctr.connect(
                    host=hs, user=us, password=pw, database="user_data")
                cd = cd_con.cursor()
                q1 = f"select * from data where name='{name1.get()}' && aadno={adhrno1.get()};"
                cd.execute(q1)
                res = cd.fetchall()
                if res == []:
                    return 0, None
                else:
                    return res[0][0], res[0][1], res[0][2], res[0][3], res[0][4], res[0][5], res[0][6], res[0][7]
            except:
                return 2, None
        v = v()
        if v[0] == 0:
            msg.showerror("Error | CodeWithVdr ",
                          "No Such Data is Present in Database")
        elif v[0] == 2:
            msg.showwarning("Warning | CodeWithVdr ",
                            "Please Create Table First")
        else:
            try:
                global image3, image_area, bk_to_see

                bk.pack_forget(), gdata_frame.pack_forget()
                name3, fname3, adhrn3, addr3, mobno3, bldgrp3, dob3 = v[
                    0], v[1], v[2], v[3], v[4], v[5], v[6]

                bsFrame = Frame(mFrame1)
    # -----------      -----------------------------------------------------

                def backtoSee():
                    bsFrame.pack_forget()
                    bk.pack(anchor=W)
                    gdata_frame.pack()
                    bk_to_see.pack_forget()

                bk_to_see = Button(
                    mFrame1, text=u"\u25C0 Back", command=backtoSee)
                bk_to_see.pack(anchor=W)
                Label(bsFrame, text="USER APPLICATION", relief=SOLID, borderwidth=3,
                      font="impact 25 bold underline", fg="purple").pack(pady=100)
                # For Showing Image
                binary_data = base64.b64decode(v[7])
                img = Image.open((io.BytesIO(binary_data)))
                r_img = img.resize((200, 200))
                image3 = ImageTk.PhotoImage(r_img)
                image_area = Button(bsFrame, image=image3, width=200,
                                    height=200, relief=SOLID, borderwidth=3)
                image_area.pack()
                # ``````````````ENDS``````````````
                Label(bsFrame, text=f"Name : {name3}", relief=SOLID,
                      font="Corbel 15 bold underline", fg="purple").pack()
                Label(bsFrame, text=f"Father's Name : {fname3}", relief=SOLID,
                      font="Corbel 15 bold underline", fg="purple").pack()
                Label(bsFrame, text=f"Registration Number : {adhrn3}",
                      relief=SOLID, font="Corbel 15 bold underline", fg="purple").pack()
                Label(bsFrame, text=f"Address : {addr3}", relief=SOLID,
                      font="Corbel 15 bold underline", fg="purple").pack()
                Label(bsFrame, text=f"Mobile Number : {mobno3}", relief=SOLID,
                      font="Corbel 15 bold underline", fg="purple").pack()
                Label(bsFrame, text=f"Blood Group : {bldgrp3}", relief=SOLID,
                      font="Corbel 15 bold underline", fg="purple").pack()
                Label(bsFrame, text=f"DOB : {dob3}", relief=SOLID,
                      font="Corbel 15 bold underline", fg="purple").pack()

                bsFrame.pack()
            except:
                pass
    else:
        msg.showerror("Error | CodeWithVdr ", "Fields Can't Be Empty")


#----------------------------------------------------------------------------------------------------------#
gdata_frame = Frame(mFrame1)
name1 = StringVar()
adhrno1 = StringVar()
Label(gdata_frame, text="USER APPLICATION", relief=SOLID, borderwidth=3,
      font="impact 25 bold underline", fg="purple").pack(pady=100)
Label(gdata_frame, text="Enter Name", relief=SOLID, font="Corbel 15 bold underline",
      fg="purple").pack(anchor=W)
Entry(gdata_frame, textvariable=name1, relief=SOLID,
      font="Corbel 20 bold", width=50).pack()
gdata_frame.pack()
Label(gdata_frame, text="Enter Registration Number", relief=SOLID, font="Corbel 15 bold underline",
      fg="purple").pack(anchor=W)
Entry(gdata_frame, textvariable=adhrno1, relief=SOLID,
      font="Corbel 20 bold", width=50).pack()
Button(gdata_frame, text="Submit", relief=SOLID, font="Corbel 12 bold", command=see, fg="purple",
       activebackground="violet", activeforeground="purple", width=40).pack(pady=10)
gdata_frame.pack()
# ========================================================================================
# For Payment Window
mFrame2 = Frame(root)
global addFeeStruc, storePayment, seePayment
bkmFrame2 = Button(mFrame2, text=u"\u25C0 Back", command=back)
bkmFrame2.pack(anchor=W)  # For Main Exit


def localBack():
    try:
        addFeeStruc.pack_forget(), storePayment.pack_forget(), seePayment.pack_forget()
    except:
        pass
    bkmFrame2.pack(anchor=W), frmOption.pack()


# Options Code addFeeStruc #DONE
addFeeStruc = Frame(mFrame2)
# For Temp connection


Button(addFeeStruc, text=u"\u25C0 Back", command=localBack).pack(anchor=W)
Label(addFeeStruc, text="USER APPLICATION", relief=SOLID, borderwidth=3,
      font="impact 25 bold underline", fg="purple").pack(pady=100)
# For Adding Fee Stucture
addFeestruc = Frame(addFeeStruc)
# Function That Stores Fee


def storeFee():
    cd = sqlctr.connect(host=hs, user=us, password=pw)
    cur = cd.cursor()
    cur.execute("use user_data;")
    q1 = "create table if not exists feeStruc(cName varchar(30) primary key,cFee varchar(20));"
    cur.execute(q1)
    if cName.get() == "" or cFee.get() == "":
        msg.showerror("Error | CodeWithVdr", "Fields Can't Be Empty")
    else:
        try:
            q2 = f"""insert into feeStruc values("{cName.get()}","{cFee.get()}");"""
            cur.execute(q2)
            msg.showinfo("Sucess | CodeWithVdr", "Data Stored Sucessfully")
        except:
            msg.showerror("Error | CodeWithVdr", "Data Already Exists")
    cd.commit()


# Variables
cName = StringVar()
cFee = StringVar()
Label(addFeestruc, text="Course Name", relief=SOLID, borderwidth=3,
      font="Corbel 15 bold underline", fg="purple").pack(anchor=W)
Entry(addFeestruc, textvariable=cName, relief=SOLID,
      font="Corbel 20 bold", width=50).pack()

Label(addFeestruc, text="Course Fee", relief=SOLID, borderwidth=3,
      font="Corbel 15 bold underline", fg="purple").pack(anchor=W)
Entry(addFeestruc, textvariable=cFee, relief=SOLID,
      font="Corbel 20 bold", width=50).pack()

Button(addFeestruc, text="Submit", relief=SOLID, font="Corbel 12 bold", command=storeFee, fg="purple",
       activebackground="violet", activeforeground="purple", width=40).pack(pady=10)

addFeestruc.pack()
# --------------------------------------------
# Options Code storePayment #DONE
storePayment = Frame(mFrame2)
Button(storePayment, text=u"\u25C0 Back", command=localBack).pack(anchor=W)
Label(storePayment, text="USER APPLICATION", relief=SOLID, borderwidth=3,
      font="impact 25 bold underline", fg="purple").pack(pady=100)


def storeFeeServ():
    cd = sqlctr.connect(host=hs, user=us, password=pw)
    cur = cd.cursor()
    cur.execute("use user_data;")
    q1 = "create table if not exists studFee(regNo varchar(30),cName varchar(40),amtFee varchar(20),date varchar(90));"
    cur.execute(q1)
    if regno.get() == "" or amtFee.get() == "":
        msg.showerror("Error | CodeWithVdr", "Fields Can't Be Empty")
        cd.commit()
    else:
        q2 = f"""select * from data where aadno={regno.get()};"""
        cur.execute(q2)
        res = cur.fetchall()
        if res == []:
            msg.showerror("Error | CodeWithVdr",
                          "No Such Registration Number Found In Database")
            cd.commit()
        else:
            q3 = f"""select * from feeStruc where cName="{csName.get()}";"""
            cur.execute(q3)
            res1 = cur.fetchall()
            if res1 == []:
                msg.showerror("Error | CodeWithVdr", "Fee Struc Not Defined")
                cd.commit()
            else:
                s=str(dt.now()).split(" ")
                q4 = f"""insert into studFee values("{regno.get()}","{csName.get()}","{amtFee.get()}","{s[0]}");"""
                cur.execute(q4)

                # For Remaining Fee
                ttlFee = int(res1[0][1])
                cur.execute(
                    f"select * from studfee where regNo='{regno.get()}';")
                v = cur.fetchall()
                fPaid = 0
                for i in v:
                    fPaid += int(i[2])
                remFee = ttlFee-fPaid
                if remFee <= 0:
                    amtrem["text"] = "Total Fee Paid"
                    msg.showinfo("Sucess | CodeWithVdr", "Total Fee Paid")
                else:
                    amtrem["text"] = f"Remaining Fee {remFee}"
                    msg.showinfo("Sucess | CodeWithVdr",
                                 "Data Stored Sucessfully")

                amtFee.set("")
                cd.commit()


# Variables
regno = StringVar()
csName = StringVar()
amtFee = StringVar()
Label(storePayment, text="Registration Number", relief=SOLID, borderwidth=3,
      font="Corbel 15 bold underline", fg="purple").pack(anchor=W)
Entry(storePayment, textvariable=regno, relief=SOLID,
      font="Corbel 20 bold", width=50).pack()

Label(storePayment, text="Course Name", relief=SOLID, borderwidth=3,
      font="Corbel 15 bold underline", fg="purple").pack(anchor=W)
Entry(storePayment, textvariable=csName, relief=SOLID,
      font="Corbel 20 bold", width=50).pack()

Label(storePayment, text="Amount Paid", relief=SOLID, borderwidth=3,
      font="Corbel 15 bold underline", fg="purple").pack(anchor=W)
Entry(storePayment, textvariable=amtFee, relief=SOLID,
      font="Corbel 20 bold", width=50).pack()

amtrem = Label(storePayment, text="", relief=SOLID, borderwidth=3,
               font="Corbel 15 bold underline", fg="purple")
amtrem.pack(anchor=W)

Button(storePayment, text="Submit", relief=SOLID, font="Corbel 12 bold", command=storeFeeServ, fg="purple",
       activebackground="violet", activeforeground="purple", width=40).pack(pady=10)

# --------------------------------------------
# Options Code seePayment (Includes Printing Of Data also)
seePayment = Frame(mFrame2)
bksp = Button(seePayment, text=u"\u25C0 Back", command=localBack)
bksp.pack(anchor=W)
head = Label(seePayment, text="USER APPLICATION", relief=SOLID, borderwidth=3,
             font="impact 25 bold underline", fg="purple")
head.pack(pady=50)
# ------------------------------A Frame To See Payment History--------------------------------


def seeFeeServ():
    # Frame For See Payment History
    pmWndw = Frame(seePayment)
    # Function For Back

    def back2fmTemp():
        pmWndw.pack_forget(), btnbk.pack_forget()
        bksp.pack(anchor=W), head.pack(pady=50), fmTemp.pack()
    global image_area1, image4
    cd_con = sqlctr.connect(
        host=hs, user=us, password=pw, database="user_data")
    cd = cd_con.cursor()
    q1 = f"select * from data where name='{nm.get()}' && aadno={regno1.get()};"
    cd.execute(q1)
    res10 = cd.fetchall()
    if res10 == []:
        msg.showerror("Error | CodeWithVdr", "No Data Found")
    else:
      try:
        btnbk = Button(pmWndw, text=u"\u25C0 Back", command=back2fmTemp)
        btnbk.pack(anchor=W)
        Label(pmWndw, text="USER APPLICATION", relief=SOLID, borderwidth=3,
              font="impact 25 bold underline", fg="purple").pack(pady=50)
        bksp.pack_forget(), fmTemp.pack_forget(), head.pack_forget()
        name4, fname4, adhrn4, addr4, mobno4, bldgrp4, dob4 = res10[0][0], res10[
            0][1], res10[0][2], res10[0][3], res10[0][4], res10[0][5], res10[0][6]
        Label(pmWndw, text=f"Image", relief=SOLID,
              font="Corbel 15 bold underline", fg="purple").pack()
        # For Showing Image
        binary_data = base64.b64decode(res10[0][7])
        img = Image.open((io.BytesIO(binary_data)))
        r_img = img.resize((200, 200))
        image4 = ImageTk.PhotoImage(r_img)
        image_area1 = Button(pmWndw, image=image4, width=200,
                             height=200, relief=SOLID, borderwidth=3)
        image_area1.pack()

        txtArea = Text(pmWndw, height=15, width=80,
                       bg="light cyan", relief=SOLID, font="Corbel 12 bold")
        # For insertion
        # For cource
        cd.execute(f"select * from studfee where regno='{res10[0][2]}';")
        result = cd.fetchall()
        s1 = f"""
\t\t\tSHAYAM COMPUTER ACADEMY
\t\tNAME           : {res10[0][0]}
\t\tCOURSE         : {result[0][1]}
\t\tREGISTRATION NUMBER : {adhrn4}

\t\tBILL DATE :   {result[0][3]}          AMOUNT : {result[-1][2]}     \t

\t\t**THIS IS AN COMPUTER GENERATED BILL
"""
# For Print
        v = u"\u2702"
        s2 = f"""
            SHAYAM COMPUTER ACADEMY
NAME           : {res10[0][0]}
COURSE         : {result[0][1]}
REGISTRATION NUMBER : {adhrn4}

BILL DATE : {result[0][3]}     AMOUNT : {result[-1][2]}

**THIS IS AN COMPUTER GENERATED BILL
{v}---------------------------------------
"""
        txtArea.insert(INSERT, s1)
        txtArea.pack(pady=20)
        # Function to print

        def printf():
            with open("temp.txt", "w", encoding="utf-8") as f:
                f.write(s2)
                f.close()
            file_to_print = "temp.txt"
            if file_to_print:
                win32api.ShellExecute(0, "print", file_to_print, None, ".", 0)
        Button(pmWndw, text="🖨️Print", command=printf, relief=SOLID, font="Corbel 12 bold", fg="purple",
               activebackground="violet", activeforeground="purple", width=40).pack(pady=10)
      except:
            msg.showerror("Error | CodeWithVdr","Please Create Table First")
    pmWndw.pack()


# --------------------------------------------------------------------------------------------
fmTemp = Frame(seePayment)
# Variables
nm = StringVar()
regno1 = StringVar()
Label(fmTemp, text="Name", relief=SOLID, borderwidth=3,
      font="Corbel 15 bold underline", fg="purple").pack(anchor=W)
Entry(fmTemp, textvariable=nm, relief=SOLID,
      font="Corbel 20 bold", width=50).pack()

Label(fmTemp, text="Registration Number", relief=SOLID, borderwidth=3,
      font="Corbel 15 bold underline", fg="purple").pack(anchor=W)
Entry(fmTemp, textvariable=regno1, relief=SOLID,
      font="Corbel 20 bold", width=50).pack()

Button(fmTemp, text="Submit", relief=SOLID, font="Corbel 12 bold", command=seeFeeServ, fg="purple",
       activebackground="violet", activeforeground="purple", width=40).pack(pady=10)
fmTemp.pack(pady=50)
# --------------------------------------------
# options Fuction


def addfeeStruc():
    frmOption.pack_forget(), bkmFrame2.pack_forget()
    addFeeStruc.pack()


def storepayment():
    frmOption.pack_forget(), bkmFrame2.pack_forget()
    storePayment.pack()


def seepayment():
    frmOption.pack_forget(), bkmFrame2.pack_forget()
    seePayment.pack()


frmOption = Frame(mFrame2)
Label(frmOption, text="USER APPLICATION", relief=SOLID, borderwidth=3,
      font="impact 25 bold underline", fg="purple").pack(pady=100)
Button(frmOption, text="Add Course Structure", command=addfeeStruc, relief=SOLID, font="Corbel 12 bold", fg="purple",
       activebackground="violet", activeforeground="purple", width=40).pack(pady=10)
Button(frmOption, text="Store Payment", command=storepayment, relief=SOLID, font="Corbel 12 bold", fg="purple",
       activebackground="violet", activeforeground="purple", width=40).pack(pady=10)
Button(frmOption, text="Payment History", command=seepayment, relief=SOLID, font="Corbel 12 bold", fg="purple",
       activebackground="violet", activeforeground="purple", width=40).pack(pady=10)
frmOption.pack()
# =========================================================================================
# NOTICE
"""
CONTROL OVER FRAMES
"""


def tmpFrame():
    # Temporary Frame
    tFrame = Frame(root)
    try:
        mFrame.pack_forget(), mFrame1.pack_forget(), mFrame2.pack_forget()
    except:
        pass

    Label(tFrame, text="USER APPLICATION", relief=SOLID, borderwidth=3,
          font="impact 25 bold underline", fg="purple").pack(pady=100)
    # Functions

    def storeData():
        tFrame.pack_forget()
        mFrame.pack()

    def seeData():
        tFrame.pack_forget()
        mFrame1.pack()

    def paymentWindow():
        tFrame.pack_forget()
        mFrame2.pack()
        #msg.showinfo("Under Development | CodeWithVdr","The Window Was Under Development....")

    def EXIT():
        root.destroy()
    # Adding Diffrent Buttons For Diffeent Work
    Button(tFrame, text="Store Data", relief=SOLID, font="Corbel 12 bold", fg="purple",
           activebackground="violet", activeforeground="purple", command=storeData, width=40).pack(pady=10)
    Button(tFrame, text="See Data", relief=SOLID, font="Corbel 12 bold", fg="purple",
           activebackground="violet", activeforeground="purple", command=seeData, width=40).pack(pady=10)
    tFrame.pack()
    Button(tFrame, text="Payment Window", relief=SOLID, font="Corbel 12 bold", fg="purple",
           activebackground="violet", activeforeground="purple", command=paymentWindow, width=40).pack(pady=10)
    tFrame.pack()
    Button(tFrame, text="EXIT", relief=SOLID, font="Corbel 12 bold", fg="purple",
           activebackground="violet", activeforeground="purple", command=EXIT, width=40).pack(pady=10)
    tFrame.pack()
    # ========================================================================

# Starts From Here Login Window


def pw_get():
    global hs, us, pw, tFrame

    try:
        cs = sqlctr.connect(
            host=f"{host.get()}", user=f"{user.get()}", password=f"{password.get()}")
        cs_cur = cs.cursor()
        cs_cur.execute("create database if not exists user_data;")
        cs_cur.execute("use user_data;")
        hs, us, pw = host.get(), user.get(), password.get()
        msg.showinfo("Sucess | CodeWithVdr", "Logged In Sucessfully")
        frame.pack_forget()
        tmpFrame()
    except ModuleNotFoundError:
        msg.showerror("Error | CodeWithVdr",
                      "Might Sql is not installed or You Are Using The\nOlder version of My Sql Please Install My Sql")
    except:
        msg.showerror("Error | CodeWithVdr", "Incorrect Credentials")


frame = Frame(root)
Label(frame, text="USER APPLICATION", relief=SOLID, borderwidth=3,
      font="impact 25 bold underline", fg="purple").pack(pady=100)
host = StringVar()
user = StringVar()
password = StringVar()
Label(frame, text="Enter Host", relief=SOLID, font="Corbel 15 bold underline",
      fg="purple").pack(anchor=W)
Entry(frame, textvariable=host, relief=SOLID,
      font="Corbel 20 bold", width=50).pack()
Label(frame, text="Enter User", relief=SOLID, font="Corbel 15 bold underline",
      fg="purple").pack(anchor=W)
Entry(frame, textvariable=user, relief=SOLID,
      font="Corbel 20 bold", show="*", width=50).pack()
Label(frame, text="Enter Server Password",
      relief=SOLID, font="Corbel 15 bold underline", fg="purple").pack(anchor=W)
Entry(frame, textvariable=password,
      relief=SOLID, font="Corbel 20 bold", show="*", width=50).pack()
Button(frame, text="Submit", relief=SOLID, font="Corbel 12 bold", command=pw_get, fg="purple",
       activebackground="violet", activeforeground="purple", width=40).pack(pady=10)
frame.pack()
root.mainloop()
#Created by CodeWithVdr
#Copyrighted content