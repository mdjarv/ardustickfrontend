from flask import Flask, render_template, abort, jsonify
import flask.ext.restless
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView

from models import db, Device

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db.init_app(app)

manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Device, methods=['GET'])

admin = Admin(app)
admin.add_view(ModelView(Device, db.session))

@app.route('/')
def index():
    return render_template('index.html', devices=Device.query.all())

@app.route('/device/<id>/<cmd>')
def device(id, cmd):
    dev = Device.query.get(id)

    if cmd not in ['on', 'off'] or dev is None:
        abort(404)

    if cmd == 'on':
        result = dev.on()
    else:
        result = dev.off()

    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)