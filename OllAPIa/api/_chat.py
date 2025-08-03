import ollama


def chat(prompt: str):
    response = ollama.chat(model='llama3', messages=[
                          {
                            'role': 'user',
                            f'content': prompt
                          },
                        ])
    return {"prompt": prompt, "response": response}