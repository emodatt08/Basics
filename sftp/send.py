import pysftp as sf
from pprint import pprint
from datetime import datetime


class SFTP:
    

    """ Initialize global variables """
    def __init__(self, url, username, password):
        self.username = username
        self.password = password
        self.url = url

    """ SFTP function """
    def sendFile(self):
        try:
            send = sf.Connection(host=self.url, username = self.username, password = self.password)
            remotePath = '/var/www/html/'+ str(datetime.now().year) + '/' + str(datetime.now().strftime('%B')) + '/' + 'flip2.png'
            localPath = '/Users/emodatt08/Desktop/flip2.png'
            send.put(localPath, remotePath)

            send.close()
        
        except Exception, e:
            print str(e)

#pprint('/var/www/html/'+ str(datetime.now().year) + '/' + str(datetime.now().strftime('%B')) + '/' + 'flip2.png')
#set remote server Url
remoteUrl = "156.0.235.14"
#Initialize class with server credentials
sftp = SFTP(remoteUrl, "fone", "KwameIsaBoy19")
#send file to remote server
sftp.sendFile()
