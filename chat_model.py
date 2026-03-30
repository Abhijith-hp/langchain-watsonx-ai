from ibm_watson_machine_learning.foundation_models.extensions.langchain import WatsonxLLM
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from app.main import model

llama_llm = WatsonxLLM(model=model)
print(llama_llm.invoke("Who is man's best friend?"))

msg = llama_llm.invoke(
    [
        SystemMessage(content="You are a helpful AI bot that assists a user in choosing the perfect book to read in one short sentence"),
        HumanMessage(content="I enjoy mystery novels, what should I read?")
    ]
)