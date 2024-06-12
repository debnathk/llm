# Blog Generator 🤖

This Streamlit application generates blog content using the Mistral-7B-Instruct-v0.3 model from Hugging Face. You can input a blog topic, specify the target audience, and set the desired word count to generate a blog post.

## Features

- Input a blog topic.
- Choose the target audience for the blog (Researchers, Data Scientists, Common People).
- Specify the number of words for the blog.
- Generate the blog content using the Hugging Face Mistral-7B-Instruct-v0.3 model.

### Create environemnt
Create a conda environment:

```
conda create -p venv python==3.9
```

### Install Dependencies
Install the required Python packages using pip:

```
pip install -r requirements.txt
```

### Clone the Repository

```
git clone https://github.com/debnathk/llm.git
cd blog-generator
```

### Set Up Hugging Face API Token
You need a Hugging Face API token to access the model. Follow these steps to create one:
1. Go to the Hugging Face website.
2. If you don't have an account, sign up for a new account.
3. Log in to your account.
4. Navigate to your account settings by clicking on your profile picture in the top-right corner and selecting "Settings".
5. In the settings menu, click on "Access Tokens".
6. Click on the "New Token" button.
7. Give your token a descriptive name, select the scope (e.g., read), and click "Generate".
8. Copy the generated token.
9. Replace the placeholder token in the code with your actual Hugging Face API token.

### Run the application

```
streamlit run app.py
```
