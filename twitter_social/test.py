from requests import request

r = request("GET", "http://127.0.0.1:8000/register/twitter/")
print(r.status_code)