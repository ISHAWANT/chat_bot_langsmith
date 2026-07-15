from langchain_core.messages import BaseMessage,HumanMessage
from langchain_groq import ChatGroq 
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph.message import add_messages 
from langgraph.graph import StateGraph,START,END
from typing import TypedDict, Annotated 
import sqlite3

from dotenv import load_dotenv

load_dotenv() 

llm = ChatGroq(model_name='llama-3.1-8b-instant') 

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage],add_messages] 


def chat_node(state: ChatState):
    messages = state['messages'] 
    response = llm.invoke(messages) 

    return {'messages': [response]} 


conn = sqlite3.connect(database='chatbot.db',check_same_thread=False)
#check pointer
check_pointer = SqliteSaver(conn=conn)

graph = StateGraph(ChatState) 

graph.add_node('chat_node',chat_node) 
graph.add_edge(START,'chat_node') 
graph.add_edge('chat_node',END) 


chatbot = graph.compile(checkpointer=check_pointer) 

# #Test

# CONFIG = {'configurable': {'thread_id':'thread-1'}}
# chatbot = graph.compile(checkpointer=check_pointer) 

# res = chatbot.invoke(
#                 {'messages': [HumanMessage(content='Hi')]},
#                 config= CONFIG,

#             )

# print(res)

def retrieve_all_threads():
    all_threads = set()
    for each_check_point in check_pointer.list(None):
        all_threads.add(each_check_point.config['configurable']['thread_id']) 

    return list(all_threads)