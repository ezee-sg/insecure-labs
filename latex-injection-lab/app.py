import os
import subprocess
from flask import Flask, render_template, request, send_file
from datetime import datetime

app = Flask(__name__)

# Plantilla LaTeX para el CV
TEX_TEMPLATE = r"""
\documentclass[a4paper,12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage{geometry}
\geometry{top=1in, bottom=1in, left=1in, right=1in}
\usepackage{hyperref}

\title{Currículum Vitae}
\author{USER_NAME}
\date{USER_DATE}

\begin{document}

\maketitle

\section*{Información Personal}
\textbf{Nombre:} USER_NAME \\
\textbf{Dirección:} USER_ADDRESS

\section*{Descripción}
USER_DESCRIPTION

\section*{Experiencia Laboral}
\begin{itemize}
USER_EXPERIENCE
\end{itemize}

\section*{Educación}
\begin{itemize}
USER_EDUCATION
\end{itemize}

\end{document}
"""

# Función para eliminar archivos temporales generados por LaTeX
def cleanup_files():
    """ Elimina archivos temporales generados por LaTeX """
    for file in os.listdir('.'):
        if file.endswith(('.tex', '.pdf', '.aux', '.log')):
            os.remove(file)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Obtener datos del formulario
        user_name = request.form.get("name", "")
        user_address = request.form.get("address", "")
        user_description = request.form.get("description", "")

        # Obtener listas de experiencia y educación
        user_experience_list = request.form.getlist("experience[]")
        user_education_list = request.form.getlist("education[]")

        # Convertir las listas a formato LaTeX de lista no enumerada
        user_experience_tex = "\n".join([f"    \\item {exp}" for exp in user_experience_list if exp.strip()])
        user_education_tex = "\n".join([f"    \\item {edu}" for edu in user_education_list if edu.strip()])

        # Inyectar los datos del formulario en la plantilla LaTeX
        tex_code = (
            TEX_TEMPLATE.replace("USER_NAME", user_name)
                        .replace("USER_DATE", datetime.now().strftime("%d/%m/%Y"))
                        .replace("USER_ADDRESS", user_address)
                        .replace("USER_DESCRIPTION", user_description)
                        .replace("USER_EXPERIENCE", user_experience_tex)
                        .replace("USER_EDUCATION", user_education_tex)
        )

        # Guardar el código LaTeX en un archivo temporal
        with open("output.tex", "w") as f:
            f.write(tex_code)

        try:
            # Compilar el archivo LaTeX con --shell-escape habilitado
            subprocess.run(["pdflatex", "--shell-escape", "output.tex"], timeout=5, check=True)
        except subprocess.CalledProcessError as e:
            return f"Error al compilar LaTeX: {e}", 500

        # Devolver el archivo PDF generado
        return send_file("output.pdf", as_attachment=True)

    return render_template("index.html")

@app.after_request
def after_request(response):
    """ Limpiar los archivos temporales después de enviar la respuesta """
    cleanup_files()
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
