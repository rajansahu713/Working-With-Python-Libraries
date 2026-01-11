import paramiko

# create ssh client 
ssh_client = paramiko.SSHClient()
import os
from dotenv import load_dotenv
load_dotenv()

host = os.getenv("HOST")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
port = os.getenv("PORT")

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=host,port=port,username=username,password=password)

ftp = ssh_client.open_sftp()

files = ftp.open("Excel-Automation-With-Python/README.md")
print(files.read().decode())

ftp.close()
ssh_client.close()
