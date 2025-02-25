from flask import Flask, render_template, request, make_response, render_template_string
import pdfkit

app = Flask(__name__)

PDFKIT_CONFIG = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        factura = {
            'cliente': request.form.get('cliente', 'Cliente Desconocido'),
            'direccion': request.form.get('direccion', 'Sin dirección'),
            'producto': request.form.get('producto', 'Producto Genérico'),
            'cantidad': int(request.form.get('cantidad', '1')),
            'precio': float(request.form.get('precio', '0.00')),
            # 🚨 Campo vulnerable a SSTI
            'descripcion': render_template_string(request.form.get('descripcion', 'Sin descripción'))
        }

        rendered_html = render_template('factura.html', factura=factura)
        pdf = pdfkit.from_string(rendered_html, False, configuration=PDFKIT_CONFIG)

        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename=factura.pdf'
        return response

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
