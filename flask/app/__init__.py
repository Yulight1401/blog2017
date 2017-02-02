from flask import Flask

app = Flask(__name__)

from app import Blogmodel
from app import Blogcontroler
from app import views
