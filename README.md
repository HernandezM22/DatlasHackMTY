Zeif
OhMyCode()

Nuestro proyecto consiste en darle significado a la base de datos que
nos proporcionó la empresa de DATLAS para poder visualizar un mapa donde se puede apreciar la problemática de los accidentes automovilísticos, de igual manera plataforma está construida con Machine Learning para poder
predecir posibles accidentes.

Comenzando 🚀
Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.
Mira Deployment para conocer como desplegar el proyecto.

Pre-requisitos 📋
IDE para poder correr Python y sus respectivas librerías de Pandas,
al igual que para poder editar CSS, HTML, JSX y React.
Contar con un archivo tipo json.
Para utilizar un archivo csv, es necesario convertirlo en un json por medio del archivo convert.js.

Da un ejemplo
Instalación 🔧

Para poder correr la plataforma donde se ven los puntos con mayor incidencia y
otras predicciones, utilizar un IDE donde esté instalada la paquetería de webpack-dev-server.
Instalar deck.gl, se puede instalar todo el paquete o únicamente los paquetes que vamos a utilizar los cuales son: core, google-maps, layers, aggregation-layers.
Para poder ejecutar la plataforma es necesario correr en la terminal el  archivo index.js con el comando 'npm start' dentro del repositorio.

Para poder correr el programa de Machine Learning únicamente necesitamos el entorno de programación para Python 8.2 e importar las librerías.

Da un ejemplo
Despliegue 📦
1- Clonar el repositorio
2- Ingresar a la carpeta real-data
3- Importar un archivo json a la carpeta public
(Puede importarse un archivo csv, modificar convert.js con el nombre de los archivos correspondientes, y correrlo con 'node convert.js')
4- Modificar linea 6 de src/index.js, con el nombre de su archivo json
const dataD = './original.json'
5- Correr el programa con 'npm start'

Construido con 🛠️

Menciona las herramientas que utilizaste para crear tu proyecto
Python (numpy, pandas, sklearn)
Scikit-Learn para las predicciones.
Vanilla Javascript
Deck.gl para visualización de datos

Contribuyendo 🖇️
Solicitar un Pull Request o mandar mensajes a los autores para obtener información relacionada con contribuciones al proyecto

Autores ✒️
Mauricio Hernández López        - Python Backend and Data Predictions
Julio Antonio Cabrera Yañez     - Python Backend and Data Predictions
María Teresa Angulo Tello       - Frontend
Paola Montserrat Vega Ortega    - Frontend and Visuals
