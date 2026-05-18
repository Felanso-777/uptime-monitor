from flask import Flask, render_template, request
import requests
import time 

app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    result=None
    if request.method=="POST" :
        url = request.form["url"]
        try:
            start = time.time()
            response = requests.get(url, timeout=5)
            end = time.time()

            result = {
                "url": url,
                "status": "Online" if response.status_code == 200 else "Issue",
                "code": response.status_code,
                "time": round((end - start) * 1000, 2)
            }
        except:
            result ={
                "url":url,
                "status":"Down",
                "error":"connection-failed"
            }
    return render_template("index.html",result=result)
if __name__ =="__main__":
    app.run(debug="True")
