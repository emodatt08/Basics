import requests as req
from pprint import pprint
import time

class fees:
    """Initialize url"""
    def __init__(self, url):
        self.url = url

    """Hit endpoint"""
    def curl(self):
        hit = req.get(self.url)
        return hit

    """Set session"""
    def setSession(self):
        session = req.Session()
        session.verify = False 
        return session

    """Set sleeper function"""
    def sleepNow(self):
        return time.sleep(10 * 60)   


tfURL = "http://localhost/tf_bank_api/public/tf_settle/jobs/perform.fee.php"
apURL = "http://10.7.1.61/tf_settle/jobs/perform.fee.php"
#Initialize class with url
send = fees(tfURL) 
#set session to false
session = send.setSession()

#while session is true
while True:
    #GET request to endpoint
    data = send.curl()
    #print json response data
    pprint(data.json())  
    #convert raw response data into json 
    response = data.json()
    #print dictionary key value
    pprint(response['count'])
    #check if response is a success
    if response['count'] == 0:
        #close session
        session.close()
        #sleep for ten minutes
        send.sleepNow()
        #set session to false
        
#print raw response
pprint(send.curl().text) 
#session close
session.close()

     
