import streamlit as st
from tensorflow import keras
import tensorflow as tf
# import numpy as np
# from PIL import Image

def load_model(path):
	model = keras.models.load_model(path)
	model.summary()
	return model

def main():
	st.sidebar.title("Maks is being developed as the 4th semester project for Aditya Shukla, Pushp Paritosh and Shambhavi Chaudhary for their Software Engineering & Project Management class.")
	st.sidebar.markdown("____")
	st.sidebar.title("Made with ❤️ & Streamlit")

	st.title("Maks ~ safety, simplified. 😷")
	st.write("Maks is an AI-based web software that has been trained to uphold COVID-19 safety guidelines. Maks scans the faces of any visitors entering a venue and makes sure that they are wearing a mask. If they are not wearing a mask, the administrator of the system shall disallow entry and also log details of the person who was violating the safety guidelines.")

	# st.markdown("____")

	st.header("_Our Motivation_ 🚀")
	st.write("While the worst is hopefully behind us, it is still imperative for all of us to respect safety guidelines, namely wearing masks. The WHO strongly recommends the enforcing of facemask-wearing in all public places to minimize transmission while also allowing a slow restarting of life.")

	st.write("All-in-all, the proces of ensuring safety for all is non-negotiable, and the inevitable aspect of lax enforcing when it comes to manual checking must be overcome.")
	st.write("Here at Maks, we aim to make this sometimes pains-taking process a nonissue. 😌")
	st.image("dependencies/img1.png")

	st.markdown("____")

	## Why Maks
	st.header("_Why Maks_ 💡")
	st.write("We believe in using the power of technology to make the World around us safer and more secure.")
	st.write("With Maks, you do not need staff monitoring the comings and goings of each person 24x7; Maks does that for you. You need to take action only when it catches a violator. And we don't like to make mistakes. That is why we have worked so hard to make a system that streamlines this process for you without losing the accuracy of a real person.")
	st.image("dependencies/img2.png")

	st.markdown("____")

	## Who We Are
	st.header("_Who We Are_ 👨🏻‍💻👩🏻‍💻")
	st.write("We're a team of 3 computer science sophomores who are powering the show here at Maks. This started as a 4th semester project for our Software Engineering Lab and we hope that it becomes much more than just that! We believe in 3 things:")
	st.write("1. Quality")
	st.write("2. Simplicity")
	st.write("3. Beauty")
	st.write("And we sincerely hope that these ideals of our shine through in our product as well.")
	st.image("dependencies/img3.png")

	st.markdown("____")

	## Request a Demo
	st.header("_Request a demo_ 👷")
	st.write("Enter your details below and we'll contact you for a demonstration of Maks!")
	
	info = st.beta_columns(3)
	name = info[0].text_input("Full Name")
	email = info[1].text_input("Email Address")
	time = info[2].text_input("Date & Time for Demo")


	st.markdown("____")

if __name__ == '__main__':
	main()
