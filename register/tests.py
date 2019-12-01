from django.test import TestCase


sm =[]
per=0.0
l= [5000,6000,8000,9000]
for i in l:
    per =i*5/100
    sm.append(per)

print(sm)



