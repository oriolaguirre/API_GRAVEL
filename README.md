# API
Es un proyecto de consulta al LLM sobre componentes gravel
# Chat Gravel – Flask + Groq + PostgreSQL 🚴‍♂️

Aplicación web desarrollada en Flask que permite realizar preguntas relacionadas con el mundo **gravel** (componentes, ciclismo, etc.) usando la **API Groq** y guardar cada intercambio en una base de datos PostgreSQL. También permite visualizar el historial de preguntas.

---

## 🚀 Tecnologías utilizadas

- **Python 3.11**
- **Flask** como framework principal
- **Groq API** (modelo `llama3-8b-8192`)
- **PostgreSQL** en AWS RDS
- **Docker + Render** para el despliegue
- **HTML/CSS/JS** con marcado dinámico en frontend
- **Gunicorn** como servidor de producción

---

## 📦 Estructura del proyecto


---

## 🌐 Endpoints disponibles

| Ruta             | Método | Descripción                                     |
|------------------|--------|-------------------------------------------------|
| `/`              | GET    | Carga la página principal con la interfaz chat |
| `/prompt/<preg>` | GET    | Consulta a Groq y guarda el resultado en BBDD  |
| `/historial`     | GET    | Devuelve todos los prompts guardados en BBDD   |

---

## 🛠️ Instalación local

1. Clona el repo  
   ```bash
   git clone https://github.com/tu-usuario/chat-gravel.git
   cd chat-gravel
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
GROQ_API_KEY=TU_CLAVE_GROQ
python app.py
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
CREATE TABLE Prompts (
  id SERIAL PRIMARY KEY,
  Prompt_entrada TEXT,
  Prompt_salida TEXT
);
🎨 Interfaz
Fondo personalizado con imagen gravel

Input dinámico con respuesta en Markdown

Botones para:

Enviar pregunta

Ver historial

Ocultar historial
✍️ Autor
Desarrollado por Oriol 🚲 Pasión por el gravel, el código y el arte digital.
