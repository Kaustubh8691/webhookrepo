from flask import json
# from crypt import methods
import json
from flask import Flask, request
app=Flask(__name__)
@app.route("/")
def api_root():
    return "welcome"

@app.route('/github',methods=['POST'])
def api_message():
    if request.headers['Content-Type']=='application/json':
        my_imfo=  json.dumps(request.json)
        # print my_imfo
        print("data")
        print (my_imfo)
        return my_imfo

if __name__=='__main__':
    app.run(debug=True)
