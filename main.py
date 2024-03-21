from flask import Flask, render_template, redirect, url_for
import random

app = Flask(__name__)

facts_list = [
    "La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos",
    "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.",
    "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna",
    "Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo",
    "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo",
    "Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos",
    "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas"
]

@app.route("/")
def hello_world():
    return f"<h1>Hello, World!</h1><a href= '{url_for('random_fact')}'>¡Ver un dato aleatorio!</a>           <a href= '{url_for('gen_pasw')}'>¡Generar una contraseña aleatorea!</a>"

@app.route("/random_fact")
def random_fact():
    return f'<p>{random.choice(facts_list)}</p><a href="/">Volver a la página principal</a>'

@app.route("/gen_pasw")
def gen_pasw():
    password = gen_pass()
    return f'<p>{password}</p><a href="/">Volver a la página principal</a>    <a href= "{url_for('gen_pasw')}">¡Otra!</a>'


def gen_pass():
    pass_length = random.randint(5, 15)
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

if __name__ == '__main__':
    app.run(debug=True)
