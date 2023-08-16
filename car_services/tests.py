from django.test import TestCase

# Create your tests here.
import http.client

conn = http.client.HTTPConnection("http://127.0.0.1:8000")

headers = { 'authorization': "Bearer " }

conn.request("GET", "/car_services/car", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))