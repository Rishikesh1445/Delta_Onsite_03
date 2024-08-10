from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:rishi1234@localhost/sleva_trade'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .routes.sell import sell as sell_blueprint
    app.register_blueprint(sell_blueprint)

    from .routes.buy import buy as buy_blueprint
    app.register_blueprint(buy_blueprint)

    from .routes.createItem import createItem as createItem_blueprint
    app.register_blueprint(createItem_blueprint)

    from .routes.availableToSell import availableToSell as availableToSell_blueprint
    app.register_blueprint(availableToSell_blueprint)

    from .routes.availableToBuy import availableToBuy as availableToBuy_blueprint
    app.register_blueprint(availableToBuy_blueprint)

    from .routes.newUser import newUser as newUser_blueprint
    app.register_blueprint(newUser_blueprint)

    from .routes.coins import coinss as coins_blueprint
    app.register_blueprint(coins_blueprint)

    return app
