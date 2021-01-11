from project import APP
from config import Config

if __name__ == "__main__":
    APP.run(port=Config.PORT,host="0.0.0.0",debug=True)