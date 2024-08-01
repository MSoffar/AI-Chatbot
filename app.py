import streamlit as st
import openai
import time

# Set the OpenAI API key from secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Role description for the assistant
role_description = """
In this scenario, you will be a chat agent named Sally working for maids․cc, designed to help clients to
issue a visa for their maids. You, as Sally, a friendly and welcoming agent must engage the client chatting
with you and try to sell them a visa for their maid. Sally will also be answering any questions or inquiries
the client might have regarding the maid’s visa service. Throughout the conversation, your primary goal is
to answer the prospect inquiries and try to sell them our maid visa service by making the client provide us
with their Emirates ID Photo and IBAN Number.
Condition #1: If the client shows an intent of getting a visa or is inquiring about the maid’s visa. You must
rely on the Questions and Answers provided within the prompt to answer their inquiries.
Condition #2: This condition aims to cover all the cases that can't be covered in condition #1. Which
means that if the client makes a statement or asks a question, and the information provided is not found
within the database of questions and answers I provided you within this prompt to cover condition #1, or
if the context is unclear or unfamiliar based on your training for condition #1, reply by saying: "As per my
current training, expertise, and knowledge, I do not have enough information to answer this question. To
know more about this, please visit maids.cc/support".
"""

# Initialize conversation history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": role_description}]

# Function to simulate typing effect
def simulate_typing(response_text, chat_placeholder, delay=0.03):
    typed_text = ""
    for char in response_text:
        typed_text += char
        # Update the chat history with the live response
        chat_placeholder.markdown(assemble_chat(st.session_state.messages, typed_text))
        time.sleep(delay)

# Function to assemble chat history
def assemble_chat(messages, current_response=""):
    chat_history = ""
    for message in messages:
        if message["role"] == "user":
            chat_history += f"**You:** {message['content']}\n\n"
        elif message["role"] == "assistant":
            chat_history += f"**Sally:** {message['content']}\n\n"
    if current_response:
        chat_history += f"**Sally:** {current_response}"
    return chat_history

# Streamlit UI
st.set_page_config(page_title="Maids.cc Chatbot", layout="centered")

# Custom CSS for dark theme and layout
st.markdown(
    """
    <style>
    .main {
        background-color: #1E1E1E;
        color: #E1E1E1;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stTextInput {
        background-color: #323232;
        color: #fff;
    }
    .stButton button {
        background-color: #0056b3;
        color: #fff;
        border: none;
        padding: 5px 15px;
        font-size: 14px;
        border-radius: 5px;
        margin: 5px 0;
    }
    .stMarkdown {
        color: #fff;
    }
    .chat-history {
        border-radius: 10px;
        padding: 20px;
        background-color: #2B2B2B;
        max-height: 400px;
        overflow-y: auto;
        margin-bottom: 10px;
    }
    .logo {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the logo centered using st.image
st.image("logo.png", width=150)

st.title("Maids.cc")
st.subheader("Chat with Sally, your virtual assistant.")

# Placeholder for chat history
chat_placeholder = st.empty()

# Display initial chat history
chat_placeholder.markdown(assemble_chat(st.session_state.messages))

# Function to process user input and reset the input field
def process_input():
    user_input = st.session_state.user_input.strip()
    if user_input:
        # Add user message to the conversation history
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Update chat history with the user's message
        chat_placeholder.markdown(assemble_chat(st.session_state.messages))

        # Get model response
        try:
            completion = openai.chat.completions.create(
                model="ft:gpt-4o-mini-2024-07-18:mcc-4::9r6ZXXKU",
                messages=st.session_state.messages
            )

            # Extract assistant message
            assistant_message = completion.choices[0].message.content.strip()

            # Simulate typing effect before adding to the history
            simulate_typing(assistant_message, chat_placeholder)

            # Append the assistant's message to the conversation history
            st.session_state.messages.append({"role": "assistant", "content": assistant_message})

            # Update chat history with the full message after typing simulation
            chat_placeholder.markdown(assemble_chat(st.session_state.messages))

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

        # Reset the input field
        st.session_state.user_input = ""

# User input with a placeholder only (no label)
st.text_input("", placeholder="Type your message here...", key="user_input", on_change=process_input)

# Function to handle quick questions
def handle_quick_question(user_message):
    # Add user message to conversation history
    st.session_state.messages.append({"role": "user", "content": user_message})

    # Update chat history with the user's message
    chat_placeholder.markdown(assemble_chat(st.session_state.messages))

    # Get model response
    try:
        completion = openai.chat.completions.create(
            model="ft:gpt-4o-mini-2024-07-18:mcc-4::9r6ZXXKU",
            messages=st.session_state.messages
        )

        # Extract assistant message
        assistant_message = completion.choices[0].message.content.strip()

        # Simulate typing effect before adding to the history
        simulate_typing(assistant_message, chat_placeholder)

        # Append the assistant's message to the conversation history
        st.session_state.messages.append({"role": "assistant", "content": assistant_message})

        # Update chat history with the full message after typing simulation
        chat_placeholder.markdown(assemble_chat(st.session_state.messages))

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Quick access buttons in a smaller box
st.markdown("### Quick Questions")
col1, col2 = st.columns(2)
with col1:
    if st.button("Maid's Nationality"):
        handle_quick_question("Can you issue visas for any nationality?")

with col2:
    if st.button("Salary"):
        handle_quick_question("What is the maid's salary?")

# Add a session reset button
if st.button("Reset Conversation"):
    # Clear the conversation history
    st.session_state.messages = [{"role": "system", "content": role_description}]
    # Refresh the chat history display
    chat_placeholder.markdown(assemble_chat(st.session_state.messages))

# Sidebar with Help/FAQ
st.sidebar.title("Help / FAQ")
st.sidebar.markdown(
    """
    **Common Questions**
    - **Visa Requirements**: Details on what is needed to apply for a maid visa.
    - **Pricing**: Information on the costs involved.

    **Contact Support**
    - Visit [maids.cc/support](https://maids.cc/support) for further assistance.
    """
)
