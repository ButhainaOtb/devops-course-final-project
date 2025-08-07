import redis
from flask import Flask, redirect, request, url_for

app = Flask(__name__)
r = redis.Redis(host="redis", port=6379)


OPTIONS = ["Buthaina", "Reem"]


@app.route("/", methods=["GET"])
def index():
    votes = {option: int(r.get(option) or 0) for option in OPTIONS}
    return f"""
    <h1>Vote for your favorite Backend Engineer</h1>
    <form method="POST" action="/vote">
        <button type="submit" name="vote" value="Buthaina">Buthaina</button>
        <button type="submit" name="vote" value="Reem">Reem</button>
    </form>
    <h2>Current Results</h2>
    <ul>    
        <li>Buthaina: {votes['Buthaina']}</li>
        <li>Reem: {votes['Reem']}</li>
    </ul>
    """


@app.route("/vote", methods=["POST"])
def vote():
    option = request.form.get("vote")
    if option in OPTIONS:
        r.incr(option)
    return redirect(url_for("index"))
