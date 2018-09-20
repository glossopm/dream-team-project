import sys
import flask

from html.html_generator import HtmlGenerator
from user_interface.user_interface import Interface

from flask import Flask
app = Flask(__name__)
# app.config['SERVER_NAME'] = "127.0.0.1:8080"

web = True

@app.route("/")
def main():
    return "Render a template for our runescape-esque homepage."

@app.route('/leaderboard/<group>')
def show_leaderboard(group):
    # show the user profile for that user
    return 'User %s' % group
    # render template

def console_main():
    user_interface = Interface(sys.argv)
    ladder = user_interface.select_ladder()

    try:
        if user_interface.is_get_ladder():
            ladder.print_ladder()

        elif user_interface.is_get_help():
            user_interface.print_help()

        elif user_interface.is_list_ladders():
            ladder.list_ladders()

        elif user_interface.record_result():
            winner_name, loser_name = sys.argv[2], sys.argv[4]

            if winner_name == loser_name:
                print "Error: You have entered the same name twice."
                return False

            if user_interface.validate_input(winner_name) or user_interface.validate_input(loser_name):
                return False

            ladder.add_new_score(winner_name, loser_name)
            ladder.print_ladder()

            html = HtmlGenerator(ladder.ladder_name, ladder.table)
            html.write_html()

        else:
            print "Incorrect parameters. Use `python main.py --help` to view commands"

    except:
        user_interface.print_help()


if __name__ == "__main__":
    if web:
        app.run()
    else:
        console_main()