import ollama
<<<<<<< HEAD
response =ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"user",
            "content":"Explain machine learning in 40 words" 
        }
    ]
)
=======
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {"role":"user",
         "content":"Explain machine learning in 40 words"

         }
    ]
)

>>>>>>> 27d61dd9040b6006c393af38834d28d41273e532
print(response["message"]["content"])