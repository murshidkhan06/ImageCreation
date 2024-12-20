import os
import openai
import streamlit as st

openai.api_key = os.getenv("OPENAI_API_KEY")

# o2 = openai.Image.create(prompt = "An IPL create match with Arab players", n=2 ,size = "1024x1024" )
st.header("DALL.E2 Image creator")
image_description = st.text_area("Enter your Image description")
button = st.button("Generate Images")


def generate_images(image_description):
    response = openai.Image.create(prompt = image_description, n=2 ,size = "1024x1024" )
    print(response)
    image_url = response['data'][0]['url']
    if image_url:
        st.image(image_url, width=800)

#
if image_description and button :
  with st.spinner(".......Generating images from Dall.e2......."):
    generate_images(image_description)
