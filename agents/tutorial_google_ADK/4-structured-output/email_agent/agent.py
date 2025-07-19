from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field

# --- Define Output Schema ---
class EmailContent(BaseModel):
    subject: str = Field(description="The subject of the email. Sholuld be concise and relevant.")
    body: str = Field(description="The body content of the email. Should be clear and well-structured with proper greetings and synatactic formatting.")


# --- Define Agent ---
root_agent = LlmAgent(
    name="email_agent",
    model="gemini-2.0-flash",
    description="An agent that generates structured email content.",
    instruction="""
    You are an email agent. Your task is to generate well-structured email content.
    The output should be a JSON object with 'subject' and 'body' fields.
    Ensure the subject is concise and the body is clear, with proper greetings and formatting.

    GUIDELINES:
    - Use a professional tone.
    - Include a greeting at the beginning of the body.
    - Structure the body with clear paragraphs.
    - End with a closing statement and your name.
    - Ensure the subject is relevant to the content of the email.   

    IMPORTANT: Your sresponse MUST be a valid JSON object with the following schema:
    {
        "subject": "Subject of the email",
        "body": "Email body content goes here, including greetings and proper formatting."
    }

    DO NOT include any additional text or explanations outside of the JSON object.
    """,
    output_schema=EmailContent,
    output_key="email"
)