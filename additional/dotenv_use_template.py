from dotenv import load_dotenv
import os

load_dotenv()
x = os.getenv('pat')
q = os.getenv('paz')
print(x)
print(q)