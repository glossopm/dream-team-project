from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class AddLeaderboardForm(FlaskForm):
    leaderboard = StringField('Leaderboard',
                           validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Add Leaderboard')


class AddPlayerForm(FlaskForm):
    player = StringField('Player',
                           validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Add Player')