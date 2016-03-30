#!/usr/bin/python
# https://pythonhelp.wordpress.com/2014/07/25/acessando-apis-rest-com-python/
# https://pythonhelp.wordpress.com/2013/03/21/acessando-conteudo-via-apis-web-baseadas-em-json/ 

import json
import requests

r = requests.get("http://jsonplaceholder.typicode.com/comments/1")
if r.status_code == 200 :
   print "OK"
   reddit_data = json.loads(r.content)

print reddit_data
print reddit_data['body']
