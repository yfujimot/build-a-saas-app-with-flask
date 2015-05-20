from collections import OrderedDict

from catwatch.lib.sqlalchemy import ResourceMixin
from catwatch.extensions import db


class Issue(ResourceMixin, db.Model):
    STATUS = OrderedDict([
        ('unread', 'Unread'),
        ('open', 'Open'),
        ('contacted', 'Contacted'),
        ('closed', 'Closed')
    ])

    LABEL = OrderedDict([
        ('login', 'I cannot access my account'),
        ('signup', 'I have a question before I sign up'),
        ('billing', 'I have a billing question'),
        ('email', 'I am not receiving e-mails'),
        ('request', 'I want to request a feature'),
        ('other', 'Other')
    ])

    __tablename__ = 'issues'
    id = db.Column(db.Integer, primary_key=True)

    status = db.Column(db.Enum(*STATUS.keys(), name='status_types'),
                       index=True, nullable=False, server_default='unread')
    label = db.Column(db.Enum(*LABEL.keys(), name='label_types'),
                      index=True, nullable=False, server_default='login')
    email = db.Column(db.String(255), index=True, nullable=False,
                      server_default='')
    question = db.Column(db.Text())