from flask import Flask
import logging
logging.basicConfig(filename='logs/wall-e.log', filemode='w', level=logging.WARNING)

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

from webapp import routes