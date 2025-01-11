import json
import time
import streamlit as st
import streamlit.components.v1 as components
import openai  # Correct library import

#######################################
# PREREQUISITES
#######################################

st.set_page_config(
    page_title="Strum Buddy",
    page_icon="strum-buddy-logo.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Initialize the OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

#######################################
# SESSION STATE SETUP
#######################################

conversation_state = "conversation"

if conversation_state not in st.session_state:
    st.session_state[conversation_state] = []


#######################################
# HELPERS
#######################################

def get_chat_response(prompt):
    """Send a message to OpenAI Chat API and retrieve the response."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Replace with the desired model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        st.error(f"Error: {e}")
        return None


def on_text_input():
    """Handle user input and update the conversation."""
    user_input = st.session_state["input_user_msg"]
    if not user_input.strip():
        return

    # Append user message to conversation
    st.session_state[conversation_state].append(("user", user_input))

    # Get response from OpenAI
    response = get_chat_response(user_input)
    if response:
        st.session_state[conversation_state].append(("assistant", response))


def on_reset_conversation():
    """Reset the conversation."""
    st.session_state[conversation_state] = []


#######################################
# SIDEBAR
#######################################

with st.sidebar:
    st.header("Debug")
    st.write(st.session_state.to_dict())

    st.button("Reset Conversation", on_click=on_reset_conversation)


#######################################
# MAIN
#######################################

# CSS to hide developer options when deployed
st.markdown(
    """
    <style>
    header {display: none !important}
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
    .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
    [data-testid="collapsedControl"] {
        display: none
    }
    .st-emotion-cache-z5fcl4 {padding-top: 0 !important}
    .viewerBadge_text__1JaDK {
        display: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

left_col, right_col = st.columns(2)

with left_col:
    st.image("strum-buddy-logo.png", use_column_width="auto")

with right_col:
    st.subheader("Don't you want Strum Buddy to love?")
    st.write(
        "Strum Buddy is an intelligent assistant who can help you locate all of the online resources needed to learn how to play new songs on guitar."
    )
    st.write(
        "Simply provide a song title and artist, and Strum Buddy will provide you with links to video tutorials and other helpful information from a variety of different websites."
    )

    # Display conversation history
    for role, message in st.session_state[conversation_state]:
        with st.chat_message(role):
            st.write(message)

# Input box for user messages
st.chat_input(
    placeholder="Provide a song name and artist",
    key="input_user_msg",
    on_submit=on_text_input,
)
