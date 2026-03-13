def build_prompt(context, question, mode):

    if mode == "Concise":

        instruction = "Answer in 2-3 sentences."

    else:

        instruction = "Give a detailed explanation with examples."

    prompt = f"""
You are an intelligent AI assistant.

Context:
{context}

Question:
{question}

Instruction:
{instruction}
"""

    return prompt