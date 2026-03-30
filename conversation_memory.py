
from langchain.chains import ConversationChain
from langchain_core.messages import HumanMessage, AIMessage
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watson_machine_learning.foundation_models.extensions.langchain import WatsonxLLM


model_id = 'meta-llama/llama-4-maverick-17b-128e-instruct-fp8'
parameters = {
    GenParams.MAX_NEW_TOKENS: 256,
    GenParams.TEMPERATURE: 0.2,
}
credentials = {"url": "https://us-south.ml.cloud.ibm.com"}
project_id = "skills-network"


model_id = 'meta-llama/llama-3-405b-instruct' 

parameters = {
    GenParams.MAX_NEW_TOKENS: 256,  
    GenParams.TEMPERATURE: 0.2, 
}

credentials = {
    "url": "https://us-south.ml.cloud.ibm.com"
  
}

project_id = "skills-network"

model = ModelInference(
    model_id=model_id,
    params=parameters,
    credentials=credentials,
    project_id=project_id
)

llm =WatsonxLLM(model = model)


history = ChatMessageHistory()


history.add_user_message("Hello, my name is Alice.")
history.add_ai_message("hi alice How can I help you?")


print(history.messages)


memory = ConversationBufferMemory()
conversation = ConversationChain(
    verbose = True,
    memory = memory,
    llm = llm
    
)

def chat_simulation(conversation, inputs):
    """Run a series of inputs through the conversation chain and display responses"""
    print("\n=== Beginning Chat Simulation ===")
    
    for i, user_input in enumerate(inputs):
        print(f"\n--- Turn {i+1} ---")
        print(f"Human: {user_input}")
        
    
        response = conversation.invoke(input=user_input)

        print(f"AI: {response['response']}")
    
    print("\n=== End of Chat Simulation ===")

test_inputs = [
    "My favorite color is blue.",
    "I enjoy hiking in the mountains.",
    "What activities would you recommend for me?",
    "What was my favorite color again?",
    "Can you remember both my name and my favorite color?"
]

chat_simulation(conversation, test_inputs)

print("\nFinal Memory Contents:")
for msg in conversation.memory.chat_memory.messages:
    print(f"{msg.type}: {msg.content}")
    


from langchain.memory import ConversationSummaryMemory

summary_memory = ConversationSummaryMemory(llm =llm)
conversation_summary = ConversationChain(llm=llm,memory=summary_memory,verbose=True)
chat_simulation(conversation_summary, test_inputs)
print("\nSummary Memory Contents:")
print(conversation_summary.memory.buffer)