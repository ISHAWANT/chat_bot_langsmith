import streamlit as st 

# st.session_state-> dict -> 
CONFIG = {'configurable':{'thread_id':'thread-1'}}

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = [] 

# message_hostory = []

#loading conversation history 

for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

# {'role':'user','content':'Hi'}
# {'role':'assistant','content':'HI'}

user_input = st.chat_input('Type here')

if user_input:
    # first add the message to message history 
    st.session_state['message_history'].append({'role':'user','content':user_input})

    with st.chat_message('user'):
        st.text(user_input)

    # first add the message to message history 
    st.session_state['message_history'].append({'role':'assiatant','content':user_input})

    with st.chat_message('assistant'):
        st.text(user_input)