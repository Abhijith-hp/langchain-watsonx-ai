from langchain_core.prompts import PromptTemplate,ChatPromptTemplate


prompt = PromptTemplate.from_template("Tell me one {adjective} joke about {topic}")
input = {"adjective": "funny", "topic": "dogs"}

prompt.invoke(input)

prompt = ChatPromptTemplate.from_messages([
 ("system", "You are a helpful assistant"),
 ("user", "Tell me a joke about {topic}")
])

input_ = {"topic": "cats"}
prompt.invoke(input_)
