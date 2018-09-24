import sys
from user_interface.user_interface import Interface
from database.db_controller import Database
from ladder.ladder import Ladder

from flask import Flask, render_template
from flask_nav import Nav
from flask_nav.elements import Navbar, Subgroup, View, Link, Text, Separator


from flask import Flask, render_template, url_for, flash, redirect
from form import AddLeaderboardForm, AddPlayerForm

app = Flask(__name__, template_folder='static/html', static_url_path='/static')
# app.config['SERVER_NAME'] = "127.0.0.1:8080"
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
# secret key to protect

nav = Nav(app)
# Nav(app) initialised the navigation on the app.

nav.register_element('my_navbar', Navbar('thenav',
                                         View('About Us', 'main'),
                                         View('Leaderboards', 'show_leaderboard', group='global'),
                                         View('Rules', 'show_leaderboard', group='global'),
                                         View('FAQ', 'show_leaderboard', group='global')))


web = True

@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template('home.html')


@app.route('/leaderboard/<group>', methods=['GET', 'POST'])
def show_leaderboard(group):
    table = Ladder(group, Database(group)).table
    players = []
    names = Database().get_leaderboards()
    lboardform = AddLeaderboardForm()
    playerform = AddPlayerForm()
    print lboardform.validate_on_submit()
    print lboardform
    #print lboardform.leaderboard.data
    if lboardform.validate_on_submit():
        print 'success'
        Database().create_league_table(lboardform.leaderboard.data)
        return redirect('/leaderboard/%s' % lboardform.leaderboard.data)
        
    for name in table:
        players.append({'name': name,
                        'rank': table.index(name) + 1})
    return render_template('ladder_template.html', players=players, group=group, names=names, 
        lboardform=lboardform, playerform=playerform)


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

            # html = HtmlGenerator(ladder.ladder_name, ladder.table)
            # html.write_html()

        else:
            print "Incorrect parameters. Use `python main.py --help` to view commands"

    except:
        user_interface.print_help()


if __name__ == "__main__":
    if web:
        app.run()
    else:
        console_main()
