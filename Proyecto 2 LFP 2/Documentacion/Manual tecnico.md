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
El Manual Técnico del Analizador Léxico y Sintáctico de BizData proporciona una guía detallada sobre el funcionamiento, la implementación y el uso de esta herramienta destinada a procesar instrucciones en el lenguaje "BizData". Este manual está diseñado para asistir a los desarrolladores y usuarios en la comprensión y la utilización efectiva del analizador léxico y sintáctico.

## Objetivos
* Objetivo General
    * Proporcionar a los desarrolladores y usuarios una guía exhaustiva que explique la implementación, funcionamiento y uso del analizador léxico y sintáctico de BizData, permitiendo así un entendimiento completo de la herramienta y su integración efectiva en proyectos.
* Objetivos Específicos
    * Proporcionar información sobre la organización y estructura del código fuente del analizador léxico y sintáctico, lo que incluye identificar el archivo principal, las dependencias clave y otros elementos relevantes.
    * Describir de manera clara y completa las instrucciones que son compatibles con el analizador, explicando cómo se deben usar, los parámetros necesarios y ejemplos de uso.
    *  Identificar los tipos de errores que el analizador es capaz de manejar, cómo se generan y proporcionar soluciones o sugerencias para solucionarlos, ayudando a los usuarios a depurar eficazmente su código.

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

#### Interfaz gráfica

* Bibliotecas Importadas: El código importa varias bibliotecas, incluyendo tkinter, filedialog, messagebox, webbrowser, y graphviz. Estas bibliotecas se utilizan para crear la interfaz de usuario, manejar archivos, mostrar mensajes de error y generar gráficos, respectivamente.

* Elementos de la Interfaz: Se crean elementos de la interfaz, como botones, áreas de texto y una consola, utilizando el módulo ttk de Tkinter para establecer estilos y configuraciones. Estos elementos permiten cargar un archivo, analizar el código BizData, visualizar resultados y generar informes.

* Funciones del Análisis: El código define varias funciones, incluyendo cargar_archivo, analizar_archivo, generar_reporte_tokens, generar_reporte_errores y generar_arbol_derivación. Estas funciones se activan cuando se hacen clic en los botones correspondientes y se encargan de cargar un archivo, analizar el código, generar informes y mostrar el árbol de derivación.

* Menú de Reportes: Se crea un menú de reportes que permite generar informes de tokens, errores y árbol de derivación. Los informes se generan en archivos HTML y se abren en el navegador.

* Interacción con el Analizador: La interfaz está diseñada para interactuar con un analizador léxico y sintáctico que se importa desde un módulo llamado analizador_lexico_sintactico. Se capturan los resultados, como tokens y errores, y se utilizan para generar informes y visualizar el árbol de derivación.

* Métodos Implementados:

    * cargar_archivo(): Abre una ventana de diálogo para seleccionar un archivo BizData y carga su contenido en el área de texto de la interfaz.

    * analizar_archivo(): Inicia el proceso de análisis del código BizData. Limpia la consola, realiza el análisis léxico y sintáctico, y muestra los resultados, incluyendo los errores, en la consola.

    * generar_reporte_tokens(): Analiza el código para identificar tokens, genera un informe en formato HTML y lo abre en el navegador.

    * generar_reporte_errores(): Analiza el código en busca de errores léxicos y sintácticos, genera un informe en formato HTML y lo abre en el navegador.

    * generar_arbol_derivacion(): Genera y muestra el árbol de derivación del código BizData utilizando la biblioteca Graphviz.

En general, esta interfaz permite cargar, analizar y generar informes sobre el código BizData, lo que facilita a los usuarios comprender y depurar sus programas escritos en este lenguaje.

#### Analizador léxico

El analizador léxico es el primer paso en el proceso de compilación o interpretación de un programa. Su función principal es descomponer el código fuente en tokens, lo que facilita el análisis posterior por parte del analizador sintáctico. También detecta y registra errores léxicos,

* Función analizador_lexico(texto): Esta función toma una cadena de texto (texto) como entrada y realiza el análisis léxico. Algunos aspectos destacados de esta función incluyen:

    * Escanea el texto línea por línea y carácter por carácter para identificar y clasificar los tokens presentes en el código.

    * Utiliza estructuras de datos como listas (tokens) y objetos Error para almacenar los tokens y los errores léxicos detectados durante el análisis.

* Función eliminar_comentarios(tokens, errores): Esta función se encarga de eliminar los comentarios del código. Los comentarios se identifican y se omiten, ya que no son necesarios para el análisis sintáctico y pueden considerarse ruido. Los comentarios pueden ser de tipo línea o bloque.

* Clase Token: La implementación incluye una clase Token que representa un token y almacena información sobre su tipo, valor, fila y columna en el código fuente.

* Clase Error: Se utiliza una clase Error para representar errores léxicos y almacenar información sobre el tipo de error, el valor que causó el error, la fila y la columna donde se encontró el error.


Los tokens reconocidos por el sistema, sus expresiones regulares y demás información se presenta a continuación:

| No  | Token            | Patrón (ER)                                  |
| --- | ----------------- | -------------------------------------------- |
| 1   | tk_claves         | ("C"\|"c")("L"\|"l")("A"\|"a")("V"\|"v")("E"\|"e")("S"\|"s") |
| 2   | tk_igual          | "="                                          |
| 3   | tk_corchete_abierto | "["                                      |
| 4   | tk_corchete_cerrado | "]"                                    |
| 5   | tk_coma           | ","                                          |
| 6   | tk_cadena         | (comilla)(L(L\|D\|"_")*)(comilla)           |
| 7   | tk_registros      | ("R"\|"r")("E"\|"e")("G"\|"g")("I"\|"i")("S"\|"s")("T"\|"t")("R"\|"r")("O"\|"o")("S"\|"s") |
| 8   | tk_llave_abierta  | "{"                                      |
| 9   | tk_llave_cerrada  | "}"                                      |
| 10  | tk_numero         | ("-"?) d+ ("."?) (d)*                      |
| 11  | tk_numeral        | "#"                                          |
| 12  | tk_comilla_simple  | " ' "                                   |
| 13  | tk_parentesis_abierto | " ( "                              |
| 14  | tk_parentesis_cerrado | " ) "                            |
| 15  | tk_comilla        | " ' "                                     |
| 16  | tk_punto_coma     | " ; "                                     |
| 17  | tk_imprimir       | ("I"\|"i")("M"\|"m")("P"\|"p")("R"\|"r")("I"\|"i")("M"\|"m")("I"\|"i")("R"\|"r") |
| 18  | tk_imprimirLN     | ("I"\|"i")("M"\|"m")("P"\|"p")("R"\|"r")("I"\|"i")("M"\|"m")("I"\|"i")("R"\|"r")("L"\|"l")("N"\|"n") |
| 19  | tk_conteo         | ("C"\|"c")("O"\|"o")("N"\|"n")("T"\|"t")("E"\|"e")("O"\|"o") |
| 20  | tk_promedio       | ("P"\|"p")("R"\|"r")("O"\|"o")("M"\|"m")("E"\|"e")("D"\|"d")("I"\|"i")("O"\|"o") |
| 21  | tk_contarsi       | ("C"\|"c")("O"\|"o")("N"\|"n")("T"\|"t")("A"\|"a")("R"\|"r")("S"\|"s")("I"\|"i") |
| 22  | tk_datos          | ("D"\|"d")("A"\|"a")("T"\|"t")("O"\|"o")("S"\|"s") |
| 23  | tk_sumar          | ("S"\|"s")("U"\|"u")("M"\|"m")("A"\|"a")("R"\|"r") |
| 24  | tk_max            | ("M"\|"m")("A"\|"a")("X"\|"x") |
| 25  | tk_min            | ("M"\|"m")("I"\|"i")("N"\|"n") |
| 26  | tk_exportarreporte | ("E"\|"e")("X"\|"x")("P"\|"p")("O"\|"o")("R"\|"r")("T"\|"t")("A"\|"a")("R"\|"r")("R"\|"r")("E"\|"e")("P"\|"p")("O"\|"o")("R"\|"r")("T"\|"t")("E"\|"e") |


Expresión regular de la grámatica completa:


```sh
(("C"|"c")("L"|"l")("A"|"a")("V"|"v")("E"|"e")("S"|"s"))|("=")|("[")|("]")|(",")|((comilla)(L(L|D|"_")*)(comilla))|(("R"|"r")("E"|"e")("G"|"g")("I"|"i")("S"|"s")("T"|"t")("R"|"r")("O"|"o")("S"|"s"))|("{")|("}")|(("-")? d+ (".")? (d)*)|("#")|(" ' ")|(" ( ")|(" ) ")|(' " ' )|(" ; ")|(("I"|"i")("M"|"m")("P"|"p")("R"|"r")("I"|"i")("M"|"m")("I"|"i")("R"|"r"))|(("I"|"i")("M"|"m")("P"|"p")("R"|"r")("I"|"i")("M"|"m")("I"|"i")("R"|"r")("L"|"l")("N"|"n"))|(("C"|"c")("O"|"o")("N"|"n")("T"|"t")("E"|"e")("O"|"o"))|(("P"|"p")("R"|"r")("O"|"o")("M"|"m")("E"|"e")("D"|"d")("I"|"i")("O"|"o"))|(("C"|"c")("O"|"o")("N"|"n")("T"|"t")("A"|"a")("R"|"r")("S"|"s")("I"|"i"))|(("D"|"d")("A"|"a")("T"|"t")("O"|"o")("S"|"s"))|(("S"|"s")("U"|"u")("M"|"m")("A"|"a")("R"|"r"))|(("M"|"m")("A"|"a")("X"|"x"))|(("M"|"m")("I"|"i")("N"|"n"))|(("E"|"e")("X"|"x")("P"|"p")("O"|"o")("R"|"r")("T"|"t")("A"|"a")("R"|"r")("R"|"r")("E"|"e")("P"|"p")("O"|"o")("R"|"r")("T"|"t")("E"|"e"))

```

El código completo de esta implementación, debido a su extensión, no se presenta en este contexto, pero se encuentra disponible en el repositorio público de GitHub en el siguiente enlace: https://github.com/Fercho9134/LFP_S2_2023_Proyecto2_202200349 Los interesados pueden acceder al repositorio para obtener el código fuente completo y explorar su funcionamiento en detalle.

#### Analizador sintáctico
Las funciones que se detallan a continuación del analizador sintáctico, trabajan en conjunto para verificar la estructura y sintaxis de un programa Bizdata. Construyen un árbol de derivación que representa la jerarquía del programa y registran cualquier error sintáctico que se encuentre. La información generada por estas funciones es esencial para identificar y corregir problemas en el código fuente de Bizdata.

* analizar_cuerpo(tokens, errores, consola, matriz, dot, parent):

    **Descripción Detallada:** Esta función es responsable de analizar el cuerpo principal de un programa Bizdata. Comienza examinando la estructura general del programa. Luego, analiza cada sentencia y expresión dentro del cuerpo. Al encontrar sentencias de impresión (e.g., "IMPRIMIR"), conteo (e.g., "CONTEO"), promedio (e.g., "PROMEDIO"), o cualquier otra instrucción específica de Bizdata, realiza una validación adicional según las reglas de sintaxis del lenguaje.
    
    **Trabajo Realizado:** Esta función examina cada token en la lista de tokens, asegurándose de que las sentencias y expresiones estén correctamente estructuradas y coincidan con la gramática de Bizdata. Crea un árbol de derivación que representa la estructura del programa y agrega nodos correspondientes a las sentencias, expresiones y otros elementos sintácticos. También identifica errores sintácticos y los agrega a la lista de errores para su posterior notificación.
    
    **Resultado Devuelto:** La función no devuelve ningún valor específico, ya que trabaja principalmente mediante efectos secundarios. Construye el árbol de derivación, actualiza la lista de errores sintácticos y, si es necesario, muestra mensajes en la consola de la interfaz gráfica de usuario.
    
* analizar_claves(tokens, errores, dot, parent):

    **Descripción Detallada:** Esta función se encarga de analizar y validar la sección de definición de claves en un programa Bizdata. Verifica que las claves estén correctamente definidas siguiendo la sintaxis del lenguaje. Las claves son cadenas como "CLAVES = [clave1, clave2, ...]".
    
    **Trabajo Realizado:** La función inicia el análisis buscando el patrón "CLAVES =", seguido de una lista de claves entre corchetes. Cada clave se valida para asegurarse de que cumple con las reglas de nomenclatura de claves (e.g., caracteres permitidos). A medida que analiza, construye el árbol de derivación y agrega nodos correspondientes a las claves y sus nombres. Los errores sintácticos, si se encuentran, se almacenan en la lista de errores.
    
    **Resultado Devuelto:** Similar a analizar_cuerpo, esta función no devuelve un valor específico. En lugar de eso, trabaja principalmente generando un árbol de derivación y actualizando la lista de errores sintácticos.
    
* analizar_registros(tokens, errores, matriz, contador_claves, dot, parent):

    **Descripción Detallada:** Esta función se encarga de analizar y validar la sección de definición de registros en un programa Bizdata. Verifica que los registros estén correctamente definidos siguiendo la sintaxis del lenguaje. Los registros están asociados con las claves definidas previamente.
    
    **Trabajo Realizado:** La función inicia el análisis buscando el patrón "REGISTROS =", seguido de una lista de registros con sus respectivos campos y valores. Se valida la estructura de cada registro, incluyendo la asignación de valores a campos específicos. Durante el análisis, la función también actualiza una matriz que almacena información relevante sobre las claves y registros, lo que permite la asociación de registros con claves. Los errores sintácticos se registran en la lista de errores.

    **Resultado Devuelto:** Al igual que las funciones anteriores, esta función no devuelve un valor específico. Su principal función es construir el árbol de derivación, mantener la matriz de información de registros y claves, y registrar los errores sintácticos.
    
La grámatica de tipo dos que se utilizó para trabajar este analizador sintactico se representa a continuación:


```sh
Terminales: {tk_claves, tk_igual, tk_corchete_abierto, tk_corchete_cerrado, tk_coma, tk_cadena, tk_registros, tk_llave_abierta, tk_llave_cerrada, tk_numero, tk_numeral, tk_comilla_simple, tk_parentesis_abierto, tk_parentesis_cerrado, tk_comilla, tk_punto_coma, tk_imprimir, tk_imprimirLN, tk_conteo, tk_promedio, tk_contarsi, tk_datos, tk_sumar, tk_max, tk_min, tk_exportarreporte}

No terminales:{ <Inicio>,  <Claves>, <Contenido_claves>, <continuacion>, <Registros>, <contenido_registros>, <datos_registros>, <final_registros>, <Otras_ins>, <Imprimir>, <Imprimirln>, <conteo>, <promedio>, <contarsi>, <datos>, <sumar>, <max>, <min>, <exportarReporte>}

Inicio = <Inicio>


Producciones:
<Inicio>::= <Claves> | <Otras_ins>

<Claves>::= tk_claves tk_igual tk_corchete_abierto <Contenido_claves>

<Contenido_claves>::= tk_cadena <continuación> 

<continuación>::= tk_coma <Contenido_claves> | tk_corchete_cerrado <Registros>

<Registros>::= tk_registros tk_igual tk_corchete_abierto <contenido_registros>

<contenido_registros>::= tk_llave_abierta <datos_registros> | <Otras_ins>

<datos_registros>::= tk_cadena <final_registros> | tk_numero <final_registros>

<final_registros>::= tk_coma <datos_registros> | tk_llave_cerrada <contenido_registros>

<Otras_ins>::= tk_ imprimir <Imprimir> | tk_imprimirLN <Imprimirln> | tk_conteo <conteo> | tk_promedio <promedio> | tk_contarsi <contarsi> | tk_datos <datos> | tk_sumar <sumar> | tk_max <max> | tk_min <min> | tk_exportarreporte <exportarReporte> | Ɛ

<Imprimir>::= tk_parentesis_abierto tk_comillas tk_cadena tk_comillas tk_parentesis_cerrado tk_punto_coma <Otras_ins>

<Imprimirln>::= tk_parentesis_abierto tk_comillas tk_cadena tk_comillas tk_parentesis_cerrado tk_punto_coma <Otras_ins>

<conteo>::= tk_parentesis_abierto tk_parentesis_cerrado tk_punto_coma <Otras_ins>

<promedio>::= tk_parentesis_abierto tk_comillas tk_cadena tk_comillas tk_parentesis_cerrado tk_punto_coma <Otras_ins>

<contarsi>::= tk_parentesis_abierto tk_comillas tk_cadena tk_comillas tk_coma tk_numero tk_parentesis_cerrado tk_punto_coma <Otras_ins>

<datos>::= tk_parentesis_abierto tk_parentesis_cerrado tk_punto_coma <Otras_ins>

<sumar>::= tk_parentesis_abierto tk_comillas tk_cadena tk_comillas tk_parentesis_cerrado tk_punto_coma <Otras_ins>

<max>::= tk_parentesis_abierto tk_comillas tk_cadena tk_comillas tk_parentesis_cerrado tk_punto_coma <Otras_ins>

<min>::= tk_parentesis_abierto tk_comillas tk_cadena tk_comillas tk_parentesis_cerrado tk_punto_coma <Otras_ins>

<exportarReporte>::= tk_parentesis_abierto tk_comillas tk_cadena tk_comillas tk_parentesis_cerrado tk_punto_coma <Otras_ins>



```
