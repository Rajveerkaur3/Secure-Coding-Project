from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return open("index.html").read()

@app.route("/submit", methods=["POST"])
def submit():
    title = request.form.get("title")
    body = request.form.get("body")

    # 🚨 Security Issues:
    # - No sanitization (XSS risk)
    # - No authentication
    # - Saving raw input (data leakage)

    with open("notes.txt", "a") as f:
        f.write(f"Title: {title}\nNote: {body}\n---\n")

    return redirect("/")
    
if __name__ == "__main__":
    app.run(debug=True)
