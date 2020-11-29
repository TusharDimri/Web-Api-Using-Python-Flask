from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/armstrong/<int:n>")
def armstrong(n):
    sum = 0
    order = len(str(n))
    copy_n = n
    while(n>0):
        digit = n%10
        sum += digit ** order
        n = n//10
    if(sum==copy_n):
        # return f"{copy_n} is an Armstrong Number"
        result = {
            "Number" : copy_n,
            "Armstrong" : True
        }
    else:
        # return f"{copy_n} is an not Armstrong Number"
        result = {
            "Number": copy_n,
            "Armstrong": False
        }

    return jsonify(result) # This converts the dictionary result to JSON and returns a JSON response

if __name__=="__main__":
    app.run(debug=True)