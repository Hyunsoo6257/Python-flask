from flask import Flask, render_template, jsonify

app = Flask(__name__)

EXP = [{
    'id': 1,
    'title': 'Waiter',
    'location': 'Outback Steakhouse',
    'salary': '$30,000'
}, {
    'id': 2,
    'title': 'Frontend Developer',
    'location': 'Feield-S',
    'salary': '$50,000'
}, {
    'id': 3,
    'title': 'Sales associate',
    'location': 'hay',
    'salary': '$12,000'
}, {
    'id': 4,
    'title': 'Home protector',
    'location': 'Outback Steakhouse',
    'salary': '$30,000'
}]


@app.route('/')
def hello_world():
  return render_template('home.html', exp=EXP)


# create json file
@app.route("/exps")
def list_exps():
  return jsonify(EXP)


print("Hello, world")
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
