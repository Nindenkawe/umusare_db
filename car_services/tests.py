from django.test import TestCase

# Create your tests here.
import http.client

conn = http.client.HTTPConnection("http://127.0.0.1:8000")

headers = { 'authorization': "Bearer eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIiwiaXNzIjoiaHR0cHM6Ly9kZXYtOHdhZHNyNmxjaGs2YnIwci51cy5hdXRoMC5jb20vIn0..bYGefcA9zgMIz6rV.fI9aE7ruhTx7BUj7he8CTHEXXceIumUWtOjtjGG1jVnmP1v6qVGXojk6lxiqkgAOghln_PD-QGoI-erRCKc1wFcNn-4iNU8EDMzIv6GUffCA3jSciuNw1ZmLOCrem--Q8q7EWCSnpy07CRfaI-_9rx35cH_YB0ugkOUV-CKKAZfHaw6FSXR5itj1dorxizoN2g-IAXCGMtVgVmyndwRWb1PrRvQOnNYIOHzl1xJ4AG80pHywG9684RFFPSWDUxhozLFXDlOAozzFkOBYM4AmTlQ4ELKiTwgiEpqdWoRYrzDtEXX25v_QJY05Sn31eEB0q2aKGOxSgJUZtPDFRoIHph0YC_x5DP4.eWpfe5qUtiTWX_OWcX14tQ" }

conn.request("GET", "/car_services/user", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))