cd Day1
cd .
ollama --version 
==>ollama pull llama3.2:3b
Questioning
run code
code hello.py--->To create a new file
python ai_query.py
==>pip install ollama 
---------------------GIT COMMANDS------------------------
git init --> Creates a new repos in your project folder
git remote add origin <url> --> connects your local repo to a github rep
git status --> shows the current status of your files
git add .  -->stages all changes to be committed
git commit -m "message" --> Save your changes with a message
git push --> uploads your commits to github
git pull --> downloads the latest changes from the github

-------------------------------------------------------------------
==>python -m pip install streamlit 
==>pip install streamlit
<<<<<<< HEAD
streamlit run file.py

docs.streamlit.io/develop/api-reference 

-------------------------------------------------------------------
git add .
git commit -m "Day 5"
git push 

pip install chromadb
pip install sentence_transformers
-------------------------------------------------------------------
python -c "from sentence_transformers import SentenceTransformer; model = SentenceTransformer('all-MiniLM-L6-v2'); print('Model is loaded.')"
-------------------------------------------------------------------------------
RAG-Retrieve Augmented Generation 
RAG Pipeline:
Steps:
Phase 1:
1.Upload Document
2.Document Loading
3.Text Cleaning
4.Chunking 
5.Embeddings
6.Chromadb(Vector Database)

Phase 2:
1.User Question
2.Question Embedding
3.Search chormadb
4.Retrieve Relevant Chunks
5.Build prompt
6.Ollama/Llama
7.Generate Answer
=======
streamlit run file.py
>>>>>>> 27d61dd9040b6006c393af38834d28d41273e532
