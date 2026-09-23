import ollama
response=ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"user",
            "content":"what is AI and types of AI,each type give two examples with in 10 lines in table formate "
        }
        
    ]
)
print(response["message"]["content"])