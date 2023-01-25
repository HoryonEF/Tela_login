import customtkinter
from tkinter import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("700x400")
janela.title("sistema de login")
janela.iconbitmap("icon.ico")
janela.resizable(False, False)

#tratando imagem
img = PhotoImage(file="HEF.png")
Label_img = customtkinter.CTkLabel(master=janela, image=img)
Label_img.place(x=3, y=25)

label_tt = customtkinter.CTkLabel(master=janela, text="Entre na sua conta", font=("Arial", 20), text_color="#00B0F0").place(x=10, y=10)

#frame
frame = customtkinter.CTkFrame(master=janela, width=350, height=396)
frame.pack(side=RIGHT)

#frame widgets
label = customtkinter.CTkLabel(master=frame, text="Sistema de Login", font=("Arial", 20))
label.place(x=25, y=5)
#campos usuario
entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Nome de usuario", width=300, font=("Arial", 14)).place(x=25, y=105)
label1= customtkinter.CTkLabel(master=frame, text="*O campo nome de usuario é obrigatorio", text_color="green", font=("Arial", 8)).place(x=25, y=135)
#campos senha
entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Senha de usuario", width=300, font=("Arial", 14)).place(x=25, y=175)
label2= customtkinter.CTkLabel(master=frame, text="*O campo Senha de usuario é obrigatorio", text_color="green", font=("Arial", 8)).place(x=25, y=205) 

chekbox = customtkinter.CTkCheckBox(master = frame, text="Lembra-se de mim sempre").place(x=25, y=235)

button = customtkinter.CTkButton(master=frame, text="login", width=300).place(x=25, y=285) 

janela.mainloop()