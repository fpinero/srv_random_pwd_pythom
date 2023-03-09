import secrets
import string
from flask import Flask
import logging

app = Flask(__name__)

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

characters = string.ascii_letters + string.digits + string.punctuation
length = 16


@app.route('/')
def home():
    logging.info("Handling home request.")
    return "Welcome to the secure password generator!"


@app.route('/password')
def password():
    logging.info("Handling password request.")
    return generate_password()


def generate_password():
    password = "".join(secrets.choice(characters) for i in range(length))
    logging.info(f"Generated new password: {password}")
    return password


# Ejecución del servidor
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
    logging.info("Service started successfully.")
