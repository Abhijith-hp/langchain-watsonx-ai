# langchain-watsonx-ai
Hands-on implementation of LangChain with IBM Watsonx AI, covering prompt engineering, RAG pipelines, and LLM orchestration.
# LangChain + IBM Watsonx AI Lab

This repository contains hands-on experiments and implementations using **LangChain** integrated with **IBM Watsonx AI**. It demonstrates core concepts of Generative AI including prompt engineering, chaining, retrieval-augmented generation (RAG), and output parsing.

---

## Overview

This project is focused on building practical understanding of:

* LangChain architecture
* LLM orchestration
* Prompt templates and chaining
* Output parsing and structured responses
* Vector databases and embeddings
* Integration with IBM Watsonx AI models

---

## Tech Stack

* Python 🐍
* LangChain
* IBM Watsonx AI
* ChromaDB (Vector Database)
* PyPDF (Document Processing)


## Getting Started

### Clone the repository

```bash
git clone https://github.com/your-username/langchain-ibm-ai-lab.git
cd langchain-ibm-ai-lab
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

### Set up environment variables

Create a `.env` file:

```env
IBM_WATSONX_API_KEY=your_api_key
IBM_WATSONX_URL=your_service_url
```

---
###  Run notebooks

```bash
jupyter notebook
```

---

##  Example Use Cases

* Generate structured outputs using output parsers
* Build multi-step LLM pipelines using SequentialChain
* Use LCEL (`|`) for chaining components
* Implement simple RAG pipelines
* Work with IBM foundation models

---

##  Sample Workflow

```
User Input → PromptTemplate → LLM → OutputParser → Final Output
```

---

##  Key Concepts Covered

* LLM vs ChatModel
* PromptTemplate & ChatPromptTemplate
* FewShotPromptTemplate
* SystemMessage & HumanMessage
* RunnableSequence (`|`)
* RunnableParallel (`{}`)
* Output Parsers
* Vector Databases

---

##  Notes

* Ensure you have valid IBM Watsonx credentials
* Restart kernel after installing dependencies
* Some features may require internet access

---

##  Future Improvements

* Add LangGraph workflows
* Build AI agents with tool calling
* Integrate real-world datasets
* Deploy as an API using FastAPI

---

##  Contributing

Contributions are welcome! Feel free to fork and improve.

---

##  License

This project is for learning purposes.

---

## Acknowledgements

* LangChain
* IBM Watsonx AI
* Open-source community
