import os
import streamlit as st
from langchain.prompts import PromptTemplate
# from langchain_community.llms import CTransformers
from langchain_huggingface import HuggingFaceEndpoint

# Save the huggingface token as env variable
hf_token = 'paste_your_token_here'
os.environ['hf_token'] = hf_token

# Huggingface Endpoint - Accessing huggingface models using API
repo_id = "mistralai/Mistral-7B-Instruct-v0.3"

# Function to get response from Mistral model
def getMistralResponse():

    # Initialize the Mistral model
    llm = HuggingFaceEndpoint(repo_id=repo_id, max_length=128, temperature=0.7, token=hf_token)

    # Create prompt template
    template = """
        Write a blog for {blog_style} job profile for a topic {input_text}
        within {no_words} words.
               """
    
    # Create prompt
    prompt = PromptTemplate(input_variables=["blog_style, input_text, no_words"], 
                            template=template)
    
    # Generate response
    response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    # print(response)
    return response


# Configure streamlit page
st.set_page_config(page_title="Blog Generator",
                   page_icon="🤖",
                   layout='centered',
                   initial_sidebar_state='collapsed'
)

st.title("Blog Generator 🤖")

input_text = st.text_input("Enter the Blog Topic")

# Creatings columns for additional fields
col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('Number of Words')
with col2:
    blog_style = st.selectbox('Writing the blog for', ('Researchers', 'Data Scientsts', 'Common People'), index=0)


# Submit
submit = st.button("Generate")

# Final response
if submit:
    st.write(getMistralResponse())
