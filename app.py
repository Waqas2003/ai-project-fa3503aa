from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/team')
def team():
    players = [
        {'name': 'Babar Azam', 'role': 'Captain'},
        {'name': 'Mohammad Rizwan', 'role': 'Wicket-Keeper'},
        # Add more players
    ]
    return render_template('team.html', players=players)

@app.route('/schedule')
def schedule():
    matches = [
        {'opponent': 'Australia', 'date': 'March 10, 2023'},
        {'opponent': 'England', 'date': 'April 15, 2023'},
        # Add more matches
    ]
    return render_template('schedule.html', matches=matches)

@app.route('/news')
def news():
    articles = [
        {'title': 'Pakistan Cricket Team Announces Squad for Upcoming Series', 'content': 'Read more...'},
        {'title': 'Babar Azam Named Captain of the Year', 'content': 'Read more...'},
        # Add more news
    ]
    return render_template('news.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)