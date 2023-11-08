import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import openai

openai.api_key = "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"

st.title("Text to Image Converter")

text_input = st.text_input("Enter text description:")
if text_input:
    st.write("You entered:", text_input)

    response = openai.Completion.create(
        engine="image-alpha-001",
        prompt=text_input,
        max_tokens=60,
    )
    
    image_url = response.choices[0].text.strip()
    
    st.image(image_url, use_column_width=True)

st.markdown("### Instructions")
st.markdown(
    "1. Enter a text description in the text input box."
    "\n2. Click the 'Convert' button to generate an image from the text."
    "\n3. The generated image will be displayed below."
)
#footer only 
st.markdown("Powered by OpenAI CLIP and Streamlit")

