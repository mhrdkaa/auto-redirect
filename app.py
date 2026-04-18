from flask import Flask, Response

app = Flask(__name__)

@app.route("/test")
def test():
    resp = Response("""
    <script>
        top.location = "https://google.com";
    </script>
    """, mimetype="text/html")
    resp.headers["Content-Security-Policy"] = "sandbox allow-top-navigation allow-scripts"
    return resp

app.run(host="0.0.0.0", debug=True)