from flask import Flask, render_template, jsonify


app = Flask(__name__,template_folder='template')

JOBS = [
    {
    "id": 1,
    "title": "developer",
    "salary": 50000,
    "location": "Banglore"
    },
    {
    "id": 2,
    "title": "Frontend developer",
    
    "location": "Chennai"
    }]


@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS,company='chools')

@app.route("/jobs")
def job():
  return jsonify(JOBS)
  

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
