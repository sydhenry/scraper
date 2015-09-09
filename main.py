from flask import url_for, Flask
app = Flask(__name__)

@app.route("/fingerprint/", methods=["POST"])
def fingerprint():
    time = request.form["time"]
    fingerprint = request.form["fingerprint"]
    args = request.form["args"]
    f = open('fingerprint.csv', 'a')
    f.write(",".join([time, fingerprint, args] + ";\n"))
    f.close()
    return ('', 204)

@app.route("/keypress/", methods=["POST"])
def keypress():
    time = request.form["time"]
    fingerprint = request.form["fingerprint"]
    key = request.form["key"]
    f = open('keypress.csv', 'a')
    f.write(",".join([time, fingerprint, key] + ";\n"))
    f.close()
    return ('', 204)

if __name__ == "__main__":
    app.run()
