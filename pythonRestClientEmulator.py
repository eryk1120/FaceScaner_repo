import requests

keys = ["systemup", "systemdown", "camegatrigger", "chairlefths", "chairrighths", "chairleftls", "chairrightls", "movenextpos"]
#for k in keys:
response = requests.post(f"http://localhost:8002/hardwareServer", data='{"message":"movenextpos"}',
   headers={
      'Accept': 'application/json, text/plain, */*',
      'Content-Type': 'application/json'
   }

)
print(response.json()) # "OK"

# nagłówek odpowiedzi na POST
#headers={
#    "Allow": "GET, POST, OPTIONS",
#    "Access-Control-Allow-Origin": "*",
#    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
#    "Access-Control-Allow-Headers": "Content-Type"
#}


# nagłówek odpowiedzi na OPTIONS
#headers={
#    "Allow": "GET, POST, OPTIONS",
#    "Access-Control-Allow-Origin": "*",
#    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
#    "Access-Control-Allow-Headers": "*"
#}

