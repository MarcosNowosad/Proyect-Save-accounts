from tkinter import *
#Colors (gris #ccd6f6, azul (#0a192f) letras(#64ffda))

def send_data():
    user_data= username.get()
    password_data= str(password.get())
    email_data= fullname.get()
    game_data= str(age.get())

    print("New user registered: \n Name: {} \n Email: {} \n Game: {}".format(user_data,email_data, game_data))

    archive= open("database.txt", "a")
    archive.write("User: " + user_data)
    archive.write("\t")
    archive.write("Password: " + password_data)
    archive.write("\t")
    archive.write("Email: " + email_data)
    archive.write("\t")
    archive.write("Game: " + game_data)
    archive.write("\n")
    archive.close()


    user_entry.delete(0, END)
    password_entry.delete(0, END)
    email_entry.delete(0, END)
    game_entry.delete(0, END)

root= Tk()


root.geometry("350x400")

root.title("  Register Users")
root.resizable(False,False)
root.iconbitmap("joystick.ico")
root.config(background="#0a192f")

#main_title= Label(text= "Python Registration Users", font=("Cambria", 19), fg="#64ffda", bg="green", width="350", height="1", pady=10)
main_title= Label(text="Python Registration Users ", font=("Cambria",15), bg="#ccd6f6", fg="black", width="550", height="2",)
main_title.pack()
#ccd6f6         #56CD63
miFrame=Frame(root, width=250, height=350, background="#0a192f")
miFrame.pack()


#Ahora vamos a hacer que los datos introducidos se guarden en un lado

username= StringVar()
password= StringVar()
fullname= StringVar()
age= StringVar()

user_entry= Entry(miFrame,textvariable=username, width= 24, justify="center", border="4")
user_entry.grid(row=0,column=1, pady=10)

password_entry= Entry(miFrame,textvariable=password, width= 24, show= "*", justify="center", border="4")
password_entry.grid(row=1,column=1, pady=10)

email_entry= Entry(miFrame,textvariable=fullname, width= 24, justify="center", border="4")
email_entry.grid(row=2, column=1, pady=10)

game_entry= Entry(miFrame,textvariable=age, width= 24, justify="center",border="4")
game_entry.grid(row=3, column=1, pady=10)


nombre_Label=Label(miFrame, text="Username", font=("Cambria", 14), fg="black", border="1", bg="#ccd6f6", width=8)
nombre_Label.grid(row=0, column=0, sticky="e", padx=10, pady=15)

password_Label=Label(miFrame, text="Password", font=("Cambria", 14), fg="black", border="1", bg="#ccd6f6", width=8)
password_Label.grid(row=1, column=0, sticky="e", padx=10, pady=15)

email_Label=Label(miFrame, text="Email", font=("Cambria", 14), fg="black", border="1", bg="#ccd6f6", width=8)
email_Label.grid(row=2, column=0, sticky="e", padx=10, pady=15)

game_Label=Label(miFrame, text="Game", font=("Cambria", 14), fg="black", border="1", bg="#ccd6f6", width=8)
game_Label.grid(row=3, column=0, sticky="e", padx=10, pady=15)

#AGREGAMOS UN BOTON PARA ENVIAR LOS DATOS

submit_btn= Button(miFrame, text="SUBMIT", command=send_data, width="13", height="1", bg="#ccd6f6", font=("Cambria",15))
submit_btn.grid(row=4,column=1)



#Colors (gris #ccd6f6, azul (#0a192f) letras(#64ffda))


root.mainloop()