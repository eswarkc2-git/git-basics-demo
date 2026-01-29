# import os
# k=os.getenv("git_token")
# print(k)

from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")
k=os.getenv("git_token")
print(k)
