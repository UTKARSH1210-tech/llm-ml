from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
import google.generativeai as genai
from IPython.display import Markdown
import re
import pandas as pd
import random
import datetime

os.environ['GOOGLE_API_KEY'] = "Your Api key"
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

prompt = '''Assume you are user then what types of questions will you ask from the salesman about the product its usage price and everything'''
res = model.generate_content(prompt).text

questions = re.findall(r'\* (.+?)\n', res)

conversation = []

products = ["Smartphone", "Laptop", "Fitness Tracker", "Smart Watch", "Headphones" , "Tablets"]


for i in range(len(products)):
    for j in range(len(questions)):
        question_prompt = f'''Assume you have a {products[i]} now you went to the shop and ask the shopkepper that , {questions[j]}'''
        start = datetime.datetime.now()
        message = model.generate_content(question_prompt).text
        # print(products[i] , questions[j])
        # message = question_prompt
        end = datetime.datetime.now()
        timestamp = (end - start)
        conversation.append({"User": questions[j] , "Salesman": message, "Timestamp": timestamp})

df = pd.DataFrame(conversation)


df.to_csv("Submission.csv")   