### Getting Started With Flask
from flask import Flask     
app = Flask(__name__)   # Flask constructor 
  
# A decorator used to tell the application 
# which URL is associated function 
@app.route('/')       
def hello(): 
    return 'HELLO'
  
if __name__=='__main__': 
   #app.run() 
    app.run(host='127.0.0.1', port=5000, debug=True)