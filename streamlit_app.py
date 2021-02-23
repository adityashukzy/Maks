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

	## Styling Elements
	html = """
	<style>
	.sidebar .sidebar-content {
		background-image: linear-gradient(#f5e725, #f56a25);
		color: white;
	}
	</style>
	"""
	st.markdown(html, unsafe_allow_html=True)

	## Sidebar Menu
	menu = ['Welcome', 'Why Maks', 'How it Works']
	
	with st.sidebar.beta_expander("Menu", expanded=False):
		option = st.selectbox('Navigate', menu)
	
	st.sidebar.subheader("Made with ❤️ by Team SAP")

	if option == "Welcome":
		st.image('https://unsplash.com/photos/BCuxVP5WEsU/download?force=true', use_column_width=True)
		st.title("Maks ~ safety, simplified. 😷")

		st.header("Maks is an AI-based web software that has been trained to uphold COVID-19 safety guidelines. Maks scans the faces of any visitors entering a venue and makes sure that they are wearing a mask. If they are not wearing a mask, the administrator of the system shall disallow entry and also log details of the person who was violating the safety guidelines.")

		st.title("Our Motivation 🚀")
		st.subheader("While the worst is hopefully behind us, it is still imperative for all of us to respect safety guidelines, namely wearing masks. The WHO strongly recommends the enforcing of facemask-wearing in all public places to minimize transmission while also allowing a slow restarting of life.")

		st.subheader("All-in-all, the proces of ensuring safety for all is non-negotiable, and the inevitable aspect of lax enforcing when it comes to manual checking must be overcome.")
		st.header("Here at Maks, we aim to make this sometimes pains-taking process a nonissue. 😌")

	elif option == "Why Maks":
		pass

	elif option == "How it Works":
		pass
	
	elif option == "Try Maks":
		model_path = '/Users/adityashukla/Documents/GitHub/Face-Mask-Detection/model/model.h5'
		model = load_model(model_path)

if __name__ == '__main__':
	main()
