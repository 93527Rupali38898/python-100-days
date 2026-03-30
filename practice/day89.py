# request module
import requests
response=requests.get("https://www.google.com/")
print(response)   #status
print()
print(response.text)