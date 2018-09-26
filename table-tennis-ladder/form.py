from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class AddLeaderboardForm(FlaskForm):
    leaderboard = StringField('Leaderboard',
                           validators=[DataRequired(), Length(min=2, max=14)])
    submit1 = SubmitField('Add Leaderboard')

class RecordMatchForm(FlaskForm):
    winner = StringField('Winner', validators=[DataRequired(), Length(min=2, max=14)])
    loser = StringField('Loser', validators=[DataRequired(), Length(min=2, max=14)])
    submit2 = SubmitField('Record Match')
    
class AddPlayerForm(FlaskForm):
    player = StringField('Player',
                           validators=[DataRequired(), Length(min=2, max=14)])
    submit3 = SubmitField('Add Player')

