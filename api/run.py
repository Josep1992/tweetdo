from project import server
from config import Config

if __name__ == "__main__":
    server.run(port=Config.PORT,host="0.0.0.0",debug=True)