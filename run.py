from web_app import app
import os

app.secret_key = os.urandom(24)
app.run(debug=True)
