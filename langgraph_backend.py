from langchain_core.messages import BaseMessage,HumanMessage
from langchain_groq import ChatGroq 
from langgraph.checkpoint.memory import InMemorySaver 
from langgraph.graph.message import add_messages 
from langgraph.graph import StateGraph,START,END
from typing import TypedDict, Annotated 


from dotenv import load_dotenv

load_dotenv() 

llm = ChatGroq(model_name='llama-3.1-8b-instant') 

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage],add_messages] 


def chat_node(state: ChatState):
    messages = state['messages'] 
    response = llm.invoke(messages) 

    return {'messages': [response]} 


check_pointer = InMemorySaver() 

graph = StateGraph(ChatState) 

graph.add_node('chat_node',chat_node) 
graph.add_edge(START,'chat_node') 
graph.add_edge('chat_node',END) 

chatbot = graph.compile(checkpointer=check_pointer) 

# for message_chunk, metadata in chatbot.stream(
#     {'messages':[HumanMessage(content='what is the capital of india')]},
#     config = {'configurable':{'thread_id':'thread-1'}},
#     stream_mode='messages'
# ):

#     if message_chunk.content:
#         print(message_chunk.content,end=' ',flush=True)


# CONFIG = {'configurable':{'thread_id': 'thread-1'}}


# response = chatbot.invoke(
#                 {'messages':[HumanMessage(content='Hi')]},
#                 config = CONFIG,
#                 stream_mode='messages'
#             )

# chatbot.get_state(config=CONFIG).values['messages'] 