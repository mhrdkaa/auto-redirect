from flask import Flask, Response

app = Flask(__name__)

@app.route("/test")
def test():
    resp = Response("""
    <script>
        setTimeout(function() {
            top.location = "https://google.com";
        }, 2000);
    </script>
    """, mimetype="text/html")
    # resp.headers["Content-Security-Policy"] = "sandbox allow-top-navigation allow-scripts"
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)