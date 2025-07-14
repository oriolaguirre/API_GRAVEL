from flask import Flask, request, jsonify,render_template
from groq import Groq
import os
import psycopg2
from psycopg2.extras import execute_values
import psycopg2

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config["DEBUG"] = True

def conection(pregunta, respuesta):
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Stanleykubrick1",
            host="bbdd-prueba.cj6g4qiykkef.eu-north-1.rds.amazonaws.com",
            port="5432"
        )
        with conn:
            with conn.cursor() as cursor:
                query = "INSERT INTO Prompts (Prompt_entrada, Prompt_salida) VALUES (%s, %s)"
                cursor.execute(query, (pregunta, respuesta))
        print("🟢 Prompt guardado correctamente.")
    except Exception as e:
        print("🔴 Error al insertar datos:", e)



def modelo(pregunta):
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": pregunta,
            }
        ],
        model="llama3-8b-8192",  # Asegúrate de que el nombre del modelo sea correcto
        stream=False,
    )

    return chat_completion.choices[0].message.content


@app.route("/", methods = ['GET'])
def main():
    return render_template("gravel.html")


@app.route("/prompt/<string:preg>", methods = ['GET'])
def prompt(preg):
    respuesta = modelo(preg)
    print(respuesta)
    conection(preg, respuesta)
    return jsonify({"respuesta": respuesta})

app.run()