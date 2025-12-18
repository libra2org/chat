# chat
The libra2 chatbot explorer

To run:
Set up the libra2 localnet
Get an OpenAI API key add it in a .env file as OPENAI_API_KEY and the API Base in OPENAI_API_BASE

then run

```
pip install -r requirements.txt
uvicorn main:app --reload
```
Then test your queries in the swagger docs at http://127.0.0.1:8000/docs
