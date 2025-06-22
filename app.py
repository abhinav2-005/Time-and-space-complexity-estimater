from flask import Flask, render_template, request,url_for
from backend_api import analyze_code_with_gemini

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")  # ✅ Flask will find this in templates/

@app.route("/analyze", methods=["POST"])
def analyze():
    code = request.form["code"]
    try:
        result = analyze_code_with_gemini(code)
    except Exception as e:
        result = f"Error while analyzing: {str(e)}"
    img_url = url_for('static', filename='Time and space complexity graph.jpg')

    return f"""
<html style="background-color:#0d0d0d; color:white; font-family:Arial, sans-serif; height:100vh; margin:0; display:flex; justify-content:center; align-items:center;">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <body style="display:flex; flex-direction:column; align-items:center; justify-content:center; width:100%; padding:20px; box-sizing:border-box;">
    
    <div style="max-width:800px; width:90%; background-color:#1a1a1a; padding:30px; border-radius:15px; box-shadow:0 0 20px rgba(0,0,0,0.5); text-align:left;">
      <h2 style="text-align:center; margin-bottom:20px;">Result</h2>
      <pre style="background-color:#111; padding:20px; border-radius:10px; white-space:pre-wrap; font-size:16px; line-height:1.6;">{result}</pre>
    </div>

    <a href="/" style="margin-top:25px; padding:12px 24px; background-color:white; color:black; border-radius:8px; text-decoration:none; font-weight:bold; box-shadow:0 2px 5px rgba(255,255,255,0.2); transition:0.3s;">
       Back
    </a>
    <img src="{img_url}" alt="Time and space complexity graph" style="margin-top:25px; height:400px;">
  </body>
</html>
"""

if __name__ == "__main__":
    app.run(debug=True)
