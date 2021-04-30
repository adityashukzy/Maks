import os
import requests
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO
from functools import partial
from dotenv import load_dotenv
from tkinter import messagebox
import mongo_auth

def validateLogin(email_id, password):
	email = email_id.get()
	pwd = password.get()
	
	if mongo_auth.verifyLogin(email, pwd):
		load_dotenv() # loading AWS keys from .env
		aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID')
		aws_secret_access_key=os.getenv('AWS_ACCESS_KEY_SECRET')

		# Rewriting the .env file along with the new added credentials
		with open(".env", "w") as f:
			f.seek(0)
			f.write(f"AWS_ACCESS_KEY_ID={aws_access_key_id}")
			f.write(f"\nAWS_ACCESS_KEY_SECRET={aws_secret_access_key}")
			f.write(f"\nEMAIL_ADDRESS={email}")
			f.write(f"\nPASSWORD={pwd}")

		messagebox.showinfo(title="Login successful!", message="Login successful! Welcome to Maks!")
		window.destroy()
	else:
		# wrongLabel = Label(window, text="Wrong Credentials!").place(x=240, y=600)
		messagebox.showerror(title="Wrong credentials!", message="Incorrect email or password!")

# Window
window = Tk()
window.geometry('580x700')
window.title('Login | Maks - safety, simplified.')


# Maks logo
url = "https://maks-images-aws-bucket.s3.ap-south-1.amazonaws.com/maks-logo.png"

# http = PoolManager()
# r = http.request('GET', url)
response = requests.get(url)

img = Image.open(BytesIO(response.content))
logo = ImageTk.PhotoImage(img)
logoLabel = Label(window, image=logo)
logoLabel.place(x=50)

# Email label and text entry box
emailLabel = Label(window, text="Email Address").place(x=100, y=480)
email = StringVar()
emailEntry = Entry(window, textvariable=email).place(x=230, y=480)

# Password label and password entry box
passwordLabel = Label(window,text="Password").place(x=100, y=530)
password = StringVar()
passwordEntry = Entry(window, textvariable=password, show='*').place(x=230, y=530)

validateLogin = partial(validateLogin, email, password)

# Login button
loginButton = Button(window, text="Login", height=2, width=12, command=validateLogin).place(x=240, y=610)

# Mainloop
window.mainloop()