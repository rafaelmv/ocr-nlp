# OCR-NLP 🐝

Con estas líneas de código es posible encontrar texto en imágenes para poder analizarlo después para obtener datos interesantes acerca del sentimiento y las entidades del documento.

Dado que es un proyecto pensado para un hackathon, se utilizan librerías externas para su fácil implementación, estás librerías son de [Google Cloud](https://cloud.google.com): [Vision API](https://cloud.google.com/vision/) y [Natural Language API](https://cloud.google.com/natural-language/). En las páginas de dichos productos se podrá encontrar más código y documentación a fondo de las herramientas.

## Instalación y uso

Para hacer uso de estos scripts son necesarios unos pasos previos.

1. Verificar que tengo instalado _python_ en mi computador. Esto lo hacemos abriendo una ventana de terminal y escribiendo `python`, si muestra un error hay que instalarlo: [https://www.python.org/downloads/](https://www.python.org/downloads/) 😅.

2. Una vez que tenemos Python en nuestro computador, tenemos que verificar que tengamos también instalado _PIP_ el cuál es el proveedor de librerías de Python, esto lo hacemos con el comando `pip` si nos dice que no está instalado o no encuetra el comando es necesario instalarlo con [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

3. Instalamos un entorno virtual, el cuál funciona como una burbuja en la que nuestras librerías están aisladas y me funcionan para la aplicación que estoy construyendo, sin tener problemas de versiones o algo similar, lo puedo instalar usando algo como `pip install virtualenv`, [aquí más información](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#installing-virtualenv).

4. Ahora es necesario crear nuestro entorno virtual e instalar los paquetes necesarios para mi aplicación; tranquile, ya casi acabamos. Esto lo hacemos con los siguientes comandos:
	- Creación de entorno virtual: `virtualenv venv -p python3` esto generará una carpeta llamada `venv` con Python 3 instalado.
	- Activación del entorno virtual: `source venv/bin/activate` esto ejecuta un script que activa mi entorno y a partir de aquí, todo lo que instale estará dentro de él, nótese que uso `venv` el nombre de mi entorno.
	- Instalación de los paquetes necesarios: `pip install -r requirements.txt` este comando usará pip para leer todo lo que esté en el documento `requirements.txt` y los instalará dentro del entorno

5. Creación de una cuenta de Google Cloud.
	- Google Cloud nos permite crear una cuenta **gratuita** en su plataforma en: [https://cloud.google.com/free/](https://cloud.google.com/free/) y además otorgan $300 USD para el uso de sus tecnologías

6. Autenticar mi cuenta de Google:
	- Una vez que cree mi cuenta es necesario realizar la autenticación desde mi computador para poder hacer uso de las herramientas, esto lo hago con una _service account_. En este manual se explica bastante bien los pasos para crear una, descargar la llave y configurarla, son 3 pasos sencillos [https://cloud.google.com/docs/authentication/getting-started](https://cloud.google.com/docs/authentication/getting-started). 

7. Al cumplir los 6 pasos anteriores necesito solo un úlitmo paso: correr el comando `python ocr-nlp.py` esto ejectutará el script de ejemplo que se utilizó, no es necesario para la instalación o el uso de las herramientas, es solo para validar que todo funcionó.

## Colaboradores

* [Rafa Miranda](mailto:rafayotuel@gmail.com) - [@rafaelyotu](https://twitter.com/rafaelyotu)

No dudes en escribirme o buscarme si tienes dudas o si notas algún error en todo esto. Happy Hacking! 🐝
