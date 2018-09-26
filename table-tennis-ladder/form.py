from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class AddLeaderboardForm(FlaskForm):
    leaderboard = StringField('Leaderboard',
                           validators=[DataRequired(), Length(min=2, max=20)])
    submit1 = SubmitField('Add Leaderboard')
    recaptcha1 = RecaptchaField()

class RecordMatchForm(FlaskForm):
    winner = StringField('Winner', validators=[DataRequired(), Length(min=2, max=20)])
    loser = StringField('Loser', validators=[DataRequired(), Length(min=2, max=20)])
    submit2 = SubmitField('Record Match')
    recaptcha2 = RecaptchaField()
    
class AddPlayerForm(FlaskForm):
    player = StringField('Player',
                           validators=[DataRequired(), Length(min=2, max=20)])
    submit3 = SubmitField('Add Player')

