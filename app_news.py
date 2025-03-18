from flask import Flask
from data import db_session, news_api

db_session.global_init("db/blogs.db")
app = Flask(__name__)
app.register_blueprint(news_api.blueprint)
app.run()