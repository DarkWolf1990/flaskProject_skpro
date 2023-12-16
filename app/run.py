from flask import Flask

# Импортируем блюпринт / Import blueprint
from app.main.views import main_blueprint

# Создаём экземпляр Flask / Create a Flask Instance
app = Flask(__name__)

# Регистрируем первый блюпринт / Registering the first blueprints
app.register_blueprint(main_blueprint)

# Запускаем сервер только, если файл запущен, а не импортирован  / Start the server only if the file is started and
# not imported
if __name__ == "__main__":
    app.run()

