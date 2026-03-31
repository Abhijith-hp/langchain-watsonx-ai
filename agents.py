from langchain_core.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import PromptTemplate

def calculator(expression: str) -> str:
    """A simple calculator that can add, subtract, multiply, or divide two numbers.
    Input should be a mathematical expression like '2 + 2' or '15 / 3'."""
    try:

        result = eval(expressions)
        return result
    except Exception as e:
        return f"Error calculating: {str(e)}"


def format_text(text: str) -> str:
    """Format text to uppercase, lowercase, or title case."""
    try:

        format_type, content = text.split(":", 1)
        format_type = format_type.strip().lower()
        content = content.strip()

        if format_type == "uppercase":
            return content.upper()
        elif format_type == "lowercase":
            return content.lower()
        elif format_type == "titlecase":
            return content.title()
        else:
            return "Invalid format type. Use uppercase, lowercase, or titlecase."
    except Exception as e:
        return f"Error formatting text: {str(e)}"


tools = [
    Tool(
        name="Calculator",
        func=calculator,
        description="Useful for mathematical calculations. Input should be a valid expression like '2 + 2'"
    ),
    Tool(
        name="Text Formatter",
        func=format_text,
        description="Useful for formatting text. Input format: 'uppercase: text' or 'lowercase: text' or 'titlecase: text'"
    )
]

prompt_template = """
You are a helpful assistant who can use tools to help with simple tasks.

You have access to the following tools:
{tools}

Use the following format:

Question: {input}
Thought: think about what to do
Action: one of [{tool_names}]
Action Input: input to the action
Observation: result of the action
... (this can repeat multiple times)
Thought: I now know the final answer
Final Answer: the final answer to the user

{agent_scratchpad}
"""

prompt = PromptTemplate.from_template(prompt_template)


agent = create_react_agent(
    llm=llama_llm,
    tools=tools,
    prompt=prompt
)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True  
)


test_questions = [
    "What is 25 + 63?", 
    "Can you convert 'hello world' to uppercase?",
    "Calculate 15 * 7", 
    "titlecase: langchain is awesome",
]


for question in test_questions:
    print(f"\n===== Testing: {question} =====")
    result = agent_executor.invoke({"input": question})
    print("FINAL ANSWER:", result["output"])