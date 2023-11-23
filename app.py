from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data analyst',
        'location': 'Seattle, USA',
        'salary': '$90k - $120k'
    },
    {
        'id': 2,
        'title': 'Data scientist',
        'location': 'San Francisco, USA',
        'salary': '$90,000-$120,000'
    },
    {
        'id': 3,
        'title': 'Backend Engineer',
        'location': 'Remote',
        'salary': '$120,000-$170,000'
    },
    {
        'id': 4,
        'title': 'Frontend Engineer',
        'location': 'Portland, Oregon',
        'salary': '$70,000-$110,000'
    },
]


@app.route("/")
def hello_abylay():
  return render_template('home.html', jobs=JOBS, company_name="Abylay")


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run('0.0.0.0', debug=True)
