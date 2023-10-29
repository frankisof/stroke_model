import requests
body = {
    "age":67,
    "hypertension":1,
    "heart_disease":1,
    "avg_glucose_level":228.69,
    "bmi":36.6,
    "stroke":1
}
response = requests.post(url = 'http://127.0.0.1:8000/score',
              json = body)
print (response.json())
# output: {'score': 0.866490130600765}


