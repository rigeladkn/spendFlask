from flask import Flask
app = Flask(__name__)

app.secret_key=b'_dzsde\nrf&123gthgf'

from app import routes


# app.run(debug=True)