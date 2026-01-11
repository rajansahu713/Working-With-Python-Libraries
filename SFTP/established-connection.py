import paramiko
import os
from dotenv import load_dotenv
load_dotenv()

# create ssh client 
ssh_client = paramiko.SSHClient()

host = os.getenv("HOST")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
port = os.getenv("PORT")

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=host,port=port,username=username,password=password)

print('connection established successfully')