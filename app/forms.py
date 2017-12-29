from flask_wtf import Form
from wtforms import TextField, SubmitField
from wtforms.validators import InputRequired, Length, URL
from flask.ext.pagedown.fields import PageDownField


# frontend thread form
class ThreadForm(Form):

    subreddit = TextField('Subreddit', validators=[InputRequired()])

    title = TextField(
        'Title',
        validators=[
            InputRequired(),
            Length(
                max=300,
                message="Title cannot be longer than 300 characters"
            )
        ]
    )

    body = PageDownField(
        'Body',
        validators=[
            InputRequired(),
            Length(
                max=40000,
                message="Description cannot be longer than 10,000 characters"
            )
        ]
    )

    submit = SubmitField('Preview')


# delete thread form
class DeleteThreadForm(Form):
    submit = SubmitField('Confirm Delete')


# captcha form
class CaptchaForm(Form):
    captcha_response = TextField(
        '',
        validators=[
            InputRequired()
        ]
    )
    submit = SubmitField('Submit AMA')
