from flask import Flask, render_template
from apps.business_cards import bp as business_cards_bp
from apps.billing_statistics import bp as billing_statistics_bp
from apps.servers import bp as servers_bp

app = Flask(__name__)
app.register_blueprint(business_cards_bp)
app.register_blueprint(billing_statistics_bp)
app.register_blueprint(servers_bp)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)
