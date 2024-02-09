import os
import streamlit as st
import openai
import time  
import base64
import webbrowser

# Set your OpenAI API key
apikey = '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'
openai.api_key = apikey



# Path to the image file
image_path = 'C:/Users/Haseeb Raza/Desktop/Langchain_ Model_01/bg3.jpg'

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
encoded_image = get_base64_of_bin_file(image_path)

# Custom CSS for background image
st.markdown(
    f"""
    <style>
    body {{
        background-image: url('data:image/jpg;base64,{encoded_image}');
        background-size: cover;
        color: white;
    }}
    .stApp {{
        background-color: transparent;
    }}
    .title {{
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 30px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        font-weight: bold;
    }}
     .stButton>button {{
        font-weight: bold;}}
    </style>
    """,
    unsafe_allow_html=True
)

# Function to open the About Us HTML file
def open_html_file():
    html_file_path = 'C:/Users/Haseeb Raza/Desktop/Langchain/Aboutus.html'
    webbrowser.open_new_tab('file://' + os.path.abspath(html_file_path))

# Function to display the About Us section
def display_about_us():
    st.title("About Us")
    st.write("Welcome to our team! We are a group of passionate individuals dedicated to providing the best services.")
    st.subheader("Meet Our Team:")
    st.markdown("### Haseeb Raza\nCo-founder & CEO")
    st.markdown("### Ibrahim Nadeem\nHead of Operations")
    st.markdown("### Muhammad Bilal Afzal Awan\nChief Technology Officer")

# App framework
st.markdown('<h1 class="title">🦜️🔗 Alpha GPT - Designed By HASEEB RAZA</h1>', unsafe_allow_html=True)
st.markdown('<div class="center">😊😊😊YOU HAVE ONLY FIVE TOKENS😊😊😊</div>', unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Navigation")
st.sidebar.write("Go to:")
about_us_button = st.sidebar.button("About Us")

# Input prompt
prompt = st.text_input('Plug in your prompt here')

# Language Model instantiation
llms = openai.ChatCompletion.create

# Define the topic
topic = "city of New York"  # You can change this to any topic

# Initialize exit button count
exit_button_count = 1

# Continue the conversation until exit
x = 5
y = 1
while y < x:
    # Display the content
    if prompt:
        # Add a spinner while the model is generating a response
        with st.spinner("Generating response..."):
            response = llms(model="gpt-3.5-turbo", temperature=0.9, messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": prompt}])
            time.sleep(2)  # Simulate a delay, you can remove this line in your actual implementation
            st.success("Response generated!")  # Indicate completion
            st.write(response.choices[0].message["content"])
        
    # Add an exit button with a unique key
    exit_button_key = f'exit_button_{exit_button_count}'
    if st.button('Exit', key=exit_button_key):
        break
    
    # Increment exit button count
    exit_button_count += 1
    
    # Get the next prompt from the user with a unique key
    prompt_input_key = f'prompt_input_{exit_button_count}'
    prompt = st.text_input('Continue the conversation...', key=prompt_input_key)
    y += 1

# Check if the "About Us" button is clicked
if about_us_button:
    display_about_us()
    # Hide the "About Us" content after 5 seconds
    time.sleep(5)
    st.experimental_rerun()
