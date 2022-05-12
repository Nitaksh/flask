from flask import Flask , request 

app = Flask(__name__)

student = {
    "1" : {"Name" : "Jagadeesh","RollNo" : "21pd13"},
    "2" : {"Name" : "Nithish","RollNo" : "21pd23" },
    "3" : {"Name" : "Rohith","RollNo" : "21pd38"}
    }

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/student")
def display():
    return student

@app.route("/student/<id>")
def search(id):
    return student[id]

@app.route("/student/search/<id>")
def search1(id):
    for i in student :
        if student[i]["RollNo"]==id :
            return student[i]["Name"]
    return "<p>ID NOT FOUND !!!</p>"

@app.route("/insert",methods = ["POST"])
def insert():
    if request.method == "POST" :
        for key,value in request.json.items() :
            print (key,value)
            student[key]=value
    return student 

if __name__ == "__main__" :
    app.run()