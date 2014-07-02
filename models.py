import rabbitpy

from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Remote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return '<Remote %d>' % self.id


class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    identifier = db.Column(db.Integer)

    remote_id = db.Column(db.Integer, db.ForeignKey('remote.id'))
    remote = db.relationship('Remote',
                             backref=db.backref('devices', lazy='dynamic'))

    def __init__(self, name='', identifier='', remote=None):
        self.name = name
        self.identifier = identifier
        self.remote = remote

    def __repr__(self):
        return '<Device %d:%d>' % (self.remote.id, self.identifier)

    def on(self):
        command = {
            'remote': self.remote.id,
            'device': self.identifier,
            'status': 1
        }
        result = rabbitpy.publish(uri='amqp://ardustick:ardustick@192.168.0.12:5672/%2f',
                                  exchange='ardustick',
                                  routing_key='',
                                  confirm=True,
                                  body=command)

        return {'command': command, 'result': result}

    def off(self):
        command = {
            'remote': self.remote.id,
            'device': self.identifier,
            'status': 0
        }

        result = rabbitpy.publish(uri='amqp://ardustick:ardustick@192.168.0.12:5672/%2f',
                                  exchange='ardustick',
                                  routing_key='',
                                  confirm=True,
                                  body=command)

        return {'command': command, 'result': result}
