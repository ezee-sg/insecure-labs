from flask import Flask, request, render_template, jsonify
import base64
from lxml import etree

app = Flask(__name__)

reports = []
next_id = 1

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route("/submit_report", methods=["POST"])
def submit_report():
    try:
        data = request.get_json()
        xml_base64 = data.get("report")

        if not xml_base64:
            return jsonify({"error": "No se ha recibido el XML codificado en Base64"}), 400

        xml_data = base64.b64decode(xml_base64).decode("utf-8")

        xml_bytes = xml_data.encode('utf-8')

        parser = etree.XMLParser(resolve_entities=True)
        root = etree.fromstring(xml_bytes, parser=parser)

        name = root.find("name").text
        email = root.find("email").text
        description = root.find("description").text

        global next_id
        report_id = next_id
        next_id += 1

        reports.append({
            "report_id": report_id,
            "name": name,
            "email": email,
            "description": description
        })

        return jsonify({"message": "Reporte enviado correctamente."}), 200

    except Exception as e:
        return jsonify({"error": f"Error procesando el reporte: {str(e)}"}), 400

@app.route("/reports")
def view_reports():
    return render_template("reports.html", reports=reports)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
