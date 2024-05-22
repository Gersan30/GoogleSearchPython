import http.client
import json

conn = http.client.HTTPSConnection("google.serper.dev")
payload = json.dumps({
  "q": "Software"
})
headers = {
  'X-API-KEY': 'e34bb48c572af7ef00c8fbe2aa55038b887e3ec1',
  'Content-Type': 'application/json'
}
conn.request("POST", "/search", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))