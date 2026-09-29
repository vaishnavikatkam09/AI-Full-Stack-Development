import ollama
<<<<<<< HEAD
response =ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"user",
            "content":"What is AI in 6 lines?" 
        }
    ]
)
=======
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {"role":"user",
         "content":"Explain ai in 6 lines?"

         }
    ]
)

>>>>>>> 27d61dd9040b6006c393af38834d28d41273e532
print(response["message"]["content"])