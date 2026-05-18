from flask import Flask, render_template,request
import requests
import time 

app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    result=None
    if request.method=="POST" :
        url = request.form["url"]
        if not url.startswith(("https://")):
            url = "https://" + url
        try:
            start = time.time()
            headers = {
                   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36",
                    "Accept-Language": "en-US,en;q=0.9",
                    "Accept": "text/html,application/xhtml+xml",
                    "Connection": "keep-alive"
            }
            response = requests.get(url,headers=headers, timeout=5)
            end = time.time()

            result = {
                "url": url,
                "status": "Online" if response.status_code <500 else "Issue",
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
    app.run()
