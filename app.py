# importing required libraries
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage,SystemMessage,AIMessage
import os



# loading and secrete values from .env file and exporting them into env variables
from dotenv import load_dotenv,dotenv_values

def reload_env_vars():
    env_vars = dotenv_values('.env')
    for key, value in env_vars.items():
        os.environ[key] = value
    
reload_env_vars()


# Streamlit UI
st.set_page_config(page_title="Conversational QA chatbot")
st.header("Hey, let's have a chat")


# checking if the this is a new session
if 'flowmessages' not in st.session_state:

    # creating the session and initializing it with system_message (instruction for LLM)
    st.session_state['flowmessages'] = [ SystemMessage(content="You are a Helpful assistant Chatbot")]


# creating the chat llm
chat_llm = ChatOpenAI(temperature=0.5)


# defining a function to get the response from OpenAI
def get_openai_response(question):

    # appending the user asked question to the context (session_state)
    st.session_state['flowmessages'].append(HumanMessage(content=question))

    # giving the context to the LLM and getting the answer
    answer = chat_llm(st.session_state['flowmessages'])

    # converting  the answer into AI Message and appending it to the session state for context
    st.session_state['flowmessages'].append(AIMessage(content=question))

    return answer.content





input_ = st.text_input("Input: ",key="input")
response = get_openai_response(input_)

submit = st.button("Generate")

# if button is clicked
if submit:
    st.subheader("The response is")
    st.write(response)



    