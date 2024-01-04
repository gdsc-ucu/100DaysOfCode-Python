from flask import Flask, render_template

app = Flask(__name__)

bot_metrics = {
    'total_bots': 50,
    'active_bots': 25,
    'inactive_bots': 25,
    'uptime_percentage': 87,
}

bot_configuration = {
    'refresh_interval': 60,
    'max_threads': 10,
    'log_level': 'INFO',
}

@app.route('/')
def index():
    return render_template('dashboard.html', metrics=bot_metrics, configuration=bot_configuration)

if __name__ == '__main__':
    app.run(debug=True)