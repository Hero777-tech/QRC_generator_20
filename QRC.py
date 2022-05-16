import pyqrcode 
from pyqrcode import QRCode 
  
# This String will represent the QR code 
s = "https://www.youtube.com/" #or any link
  
# QR code will be generated 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png or my.svg...etc..." 
url.svg("yt.svg", scale = 8)
