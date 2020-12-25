from pydo import app
from pydo.config import Config

if __name__ == "__main__":
    app.run(port=Config.PORT,host="0.0.0.0",debug=True)