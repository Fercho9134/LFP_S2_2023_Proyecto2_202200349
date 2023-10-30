# Lenguajes formales y de programación
## Proyecto 2
### 4to Semestre
```js
Universidad San Carlos de Guatemala
Programador: Irving Fernando Alvarado Asensio
Carne: 202200349
Correo: 3291590461103@ingenieria.usac.edu.gt
```
---
## Descripción
BizData (Business Data Analysis) es una plataforma diseñada para permitir a las pequeñas empresas tomar decisiones fundamentadas y estratégicas basadas en el análisis profundo de sus datos comerciales. Para lograr esto, BizData proporciona una herramienta de análisis léxico y sintáctico que permite a las empresas cargar y analizar datos estructurados en un formato especializado con extensión ".bizdata". Este manual te guiará a través del uso de la aplicación y sus características.

## Objetivos
* Objetivo General
    *  El objetivo general de este manual de usuario es proporcionar a los usuarios una guía completa y detallada sobre cómo utilizar la aplicación BizData para realizar análisis léxico y sintáctico de datos en formato ".bizdata", así como generar informes y reportes en formato HTML.
* Objetivos Específicos
    * Proporcionar instrucciones claras y paso a paso para cargar archivos ".bizdata" en la aplicación y realizar un análisis léxico y sintáctico con éxito.
    * Explicar en detalle las características de la interfaz gráfica de BizData, incluyendo la funcionalidad de los componentes como el área de texto, la consola y el menú de reportes.
    * Guiar a los usuarios en la generación de informes en formato HTML, incluyendo reportes de tokens, reportes de errores y la creación de árboles de derivación, para que puedan aprovechar al máximo la capacidad de análisis de la aplicación.


---
## Descripción del proyecto
BizData es una innovadora plataforma diseñada para proporcionar a las pequeñas empresas una herramienta poderosa de análisis de datos que les permita tomar decisiones fundamentadas y estratégicas basadas en una comprensión profunda de su información comercial. Esta plataforma se centra en la gestión y análisis de datos estructurados en un formato especializado con la extensión ".bizdata".

Funciones Clave de BizData:
* Análisis Léxico y Sintáctico: BizData incluye un analizador léxico y sintáctico desarrollado en Python. Este analizador permite a las empresas cargar archivos ".bizdata" y analizar la estructura de los datos de manera eficiente. Puede reconocer las secciones de claves y registros, lo que facilita la interpretación de los datos.

* Generación de Informes: Los usuarios pueden ejecutar una variedad de instrucciones de reportería en BizData. Esto incluye la generación de informes de tokens, informes de errores y la creación de árboles de derivación. Estos informes ayudan a los usuarios a comprender y visualizar los datos de una manera más significativa.

* Interfaz Gráfica de Usuario (GUI): BizData ofrece una interfaz gráfica amigable que simplifica la interacción con la plataforma. Los usuarios pueden cargar archivos, editar el código ".bizdata", realizar análisis y generar informes a través de esta interfaz intuitiva.

##### Requisitos del Sistema

###### Requisitos de Hardware

1. **Computadora:** Se requiere una computadora con un procesador y memoria RAM suficientes para ejecutar Python y las operaciones de análisis de datos.

2. **Almacenamiento:** Espacio en disco suficiente para almacenar los archivos de datos y los informes generados.

3. **Conexión a Internet:** Se recomienda una conexión a Internet para acceder a recursos en línea y actualizar las bibliotecas y módulos necesarios.

###### Requisitos de Software

1. **Sistema Operativo:** BizData es compatible con sistemas operativos Windows, macOS y Linux.

2. **Python:** La aplicación BizData está escrita en Python. Asegúrate de tener Python instalado en tu sistema. Se recomienda la versión 3.x de Python.

3. **Bibliotecas Python:**
   - **Tkinter:** Para utilizar la interfaz gráfica de usuario (GUI) de BizData, es necesario que Python tenga instalada la biblioteca Tkinter. La mayoría de las distribuciones de Python incluyen Tkinter de forma predeterminada.
   - **Graphviz:** La generación de árboles de derivación en BizData se basa en Graphviz. Debes instalar la biblioteca Graphviz en tu sistema. Puedes hacerlo mediante herramientas como "pip" en Python.

4. **Navegador Web:** Para visualizar los informes generados en formato HTML, se necesita un navegador web compatible.

**Nota:** Asegúrate de que las bibliotecas Python, como Tkinter y Graphviz, estén configuradas correctamente en tu entorno de desarrollo. La falta de estas bibliotecas o configuraciones incorrectas puede afectar el funcionamiento de BizData.

#### Interfaz de Usuario

La interfaz de usuario de BizData es intuitiva y fácil de usar, diseñada para simplificar la carga, análisis y generación de informes a partir de archivos ".bizdata". A continuación, se describen los componentes clave de la interfaz:

![Imagen 1](https://i.ibb.co/0ttvG2H/Gui-1.png)

##### Cargar Archivo

El botón "Cargar archivo" te permite seleccionar y cargar un archivo con extensión ".bizdata" desde tu sistema de archivos. Una vez cargado, el contenido del archivo se mostrará en el área de texto para su visualización y, si es necesario, edición.

##### Área de Texto

El área de texto es un espacio de edición y visualización donde puedes ver y modificar el código "bizdata". Puedes realizar cambios en el código antes de realizar el análisis.

##### Analizar Archivo

El botón "Analizar archivo" inicia el proceso de análisis del código "bizdata" que has cargado en el área de texto. La aplicación verificará la estructura y mostrará cualquier error encontrado en la consola.

##### Consola

La consola es un área de texto que muestra los resultados de las instrucciones de reportería y cualquier mensaje de error. Esta área no es editable y se utiliza para visualizar los resultados generados por las instrucciones ejecutadas.

##### Menú Reportes

El menú "Reportes" te permite generar informes en formato HTML. Los tipos de reportes disponibles incluyen:

- **Reporte de Tokens:** Muestra una tabla con todos los tokens analizados, indicando el tipo de token, su lexema, fila y columna en el código fuente.

![Imagen 1](https://i.ibb.co/TMs8cCG/Reporte-tokens.png)

- **Reporte de Errores:** Genera una tabla con todos los errores léxicos y sintácticos encontrados, indicando el carácter o token leído, la fila y la columna en la que ocurrió el error.

![Imagen 1](https://i.ibb.co/GpKqqnw/Reporte-errores.png)

- **Árbol de Derivación:** Genera un árbol de derivación que representa la estructura sintáctica del código fuente. Este árbol se crea utilizando la herramienta Graphviz.

![Imagen 1](https://i.ibb.co/XFyg4tg/Arbol-Derivacion-gv.png)

La interfaz de usuario de BizData proporciona una experiencia cómoda y efectiva para interactuar con la aplicación, cargar archivos, realizar análisis de datos y generar informes en formato HTML. Esto facilita la toma de decisiones basadas en datos y la comunicación de resultados a las partes interesadas.

#### Funciones del Lenguaje

A continuación se describen las funciones disponibles en el lenguaje "BizData" y su uso:

###### 1. `imprimir(cadena):`
- **Descripción:** Imprime el valor proporcionado como argumento en la consola.
- **Uso:** `imprimir("Mensaje a imprimir")`

###### 2. `imprimirln(cadena):`
- **Descripción:** Imprime el valor proporcionado como argumento en la consola, seguido de un salto de línea.
- **Uso:** `imprimirln("Mensaje a imprimir")`

###### 3. `conteo():`
- **Descripción:** Imprime la cantidad de registros en el archivo ".bizdata".
- **Uso:** `conteo()`

###### 4. `promedio("campo"):`
- **Descripción:** Calcula el promedio de los valores en el campo especificado y lo imprime.
- **Uso:** `promedio("nombre_del_campo")`

###### 5. `contarsi("campo", valor):`
- **Descripción:** Imprime la cantidad de registros en los que el campo especificado es igual al valor proporcionado.
- **Uso:** `contarsi("nombre_del_campo", valor_a_comparar)`

###### 6. `datos():`
- **Descripción:** Imprime todos los registros leídos.
- **Uso:** `datos()`

###### 7. `sumar("campo"):`
- **Descripción:** Calcula la suma de los valores en el campo especificado y lo imprime.
- **Uso:** `sumar("nombre_del_campo")`

###### 8. `max("campo"):`
- **Descripción:** Encuentra el valor máximo en el campo especificado y lo imprime.
- **Uso:** `max("nombre_del_campo")`

###### 9. `min("campo"):`
- **Descripción:** Encuentra el valor mínimo en el campo especificado y lo imprime.
- **Uso:** `min("nombre_del_campo")`

###### 10. `exportarReporte("titulo"):`
- **Descripción:** Genera un archivo HTML con una tabla de registros y utiliza el título proporcionado como nombre del archivo.
- **Uso:** `exportarReporte("titulo_del_reporte")`

###### 9. `claves(lista_de_claves):`
- **Descripción:** Define las claves o campos por los que están construidos los registros en el archivo ".bizdata".
- **Uso:** `claves = ["clave1", "clave2", "clave3"]`

###### 10. `registros(lista_de_registros):`
- **Descripción:** Detalla los registros que se desean analizar en el archivo ".bizdata".
- **Uso:** `registros = [{valor1, valor2, valor3} {valor4, valor5, valor6}]`

Estas funciones son esenciales para realizar operaciones de análisis y generación de informes en el lenguaje "BizData". Puedes utilizarlas para trabajar con datos estructurados y tomar decisiones fundamentadas en tu negocio.

#### Guía de Uso

La aplicación "BizData" te permite cargar, analizar y generar informes a partir de archivos ".bizdata". Sigue estos pasos para utilizar la aplicación de manera efectiva:

1. Cargar un Archivo ".bizdata"

    Haz clic en el botón "Cargar archivo" para seleccionar y cargar un archivo con extensión ".bizdata" desde tu sistema de archivos.
    Una vez cargado, el contenido del archivo se mostrará en el área de texto de la aplicación.
    Puedes editar el código "bizdata" en el área de texto si es necesario.

2. Analizar el Archivo

    Presiona el botón "Analizar archivo" para iniciar el proceso de análisis del código "bizdata".

* La aplicación verificará la estructura del código y mostrará cualquier error encontrado en la consola.

* Los errores léxicos y sintácticos se informarán en la consola, lo que te permitirá corregirlos antes de continuar.

3. Utilizar las Funciones de Reportería

    Puedes utilizar las funciones del lenguaje "BizData" para realizar análisis de datos y generar informes. Por ejemplo:
    * Utiliza conteo() para conocer la cantidad de registros en el archivo.
    * Usa promedio("campo") para calcular el promedio de un campo numérico.
    * Emplea exportarReporte("titulo") para generar informes en formato HTML.
    
4. Generar Informes en Formato HTML

    En el menú "Reportes", encontrarás tres opciones para generar informes en formato HTML:
* Reporte de Tokens: Muestra una tabla con todos los tokens analizados en el código.

* Reporte de Errores: Genera una tabla con los errores léxicos y sintácticos encontrados.

* Árbol de Derivación: Crea un árbol de derivación que representa la estructura sintáctica del código.

5. Visualizar Resultados en la Consola

    La consola de la aplicación mostrará los resultados de las instrucciones ejecutadas y cualquier mensaje de error.

    Utiliza la consola para verificar los resultados de las funciones y los informes generados.
    
La aplicación "BizData" proporciona una interfaz intuitiva y potentes herramientas para trabajar con datos comerciales y tomar decisiones informadas. Sigue estos pasos para cargar, analizar y generar informes a partir de tus archivos ".bizdata".
