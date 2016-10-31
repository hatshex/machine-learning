# Introducción al Aprendizaje de máquina o Machine Learning

## ¿Para qué hacer que una computadora aprenda?
  * Buscamos entender (relaciones, similitudes, diferencias, invariantes), buscamos predecir
  * Buscamos modelar un fenómeno sin tener el conocimiento explícito del proceso subyacente

Al aprendizaje de máquina consiste de varias técnicas (familias de funciones) para aproximar el proceso que genera lo observado

## ¿Qué es?
  1. **_*Tom Michell*_** - Se dice que un programa de computadora aprende de su experiencia *E* con respecto a una tarea *T* y función de evaluación *F*, si su desempeño en la tarea T (con respecto a la evaluación F) mejora con la experiencia E
  2. **_*Tom Michell*_** - Un programa de computadora se dice que aprende de la experiencia E con respecto a alguna clase de tareas T y P medida de rendimiento, si su desempeño en tareas en T, medido por P, mejora con la experiencia E
  3. **_*Arthur Samuel*_** - El campo de estudio que da a las computadoras la capacidad de aprender sin ser programada de forma explícita
  
En general un problema de aprendizaje debe precisar:
  * La clase de tareas a las que se refiere
  * La función de evaluación 
  * La fuente de experiencia

Ya definido esto podemos seleccionar un modelo (_*función objetivo*_) y ajustarlo para maximizar su desempeño 

## Tipos de problemas
Lo que queremos aprender es una función que dado un ejemplo (un dato) nos entregue un valor
  * Si el valor es numérico se conoce como regresión: El valor de una acción
  * Si el valor es categórico se conoce como clasificación: Si un día es bueno o no para jugar tenis

## Tipos de técnicas
Dependido de si tenemos disponible el valor de la función objetivo para los ejemplos de entrenamiento, las tareas de aprendizaje se dividen en:
  * **Aprendizaje Supervisado**: Se utilizan los datos de entrenamiento y el valor correcto para cada uno de ellos de la función objetivo (la función que intentamos aprender)
    - Árboles de decisión, redes neuronales
  * **Aprendizaje No-supervisado: ** Sólo se le presentan datos, se desconoce el valor objetivo de los ejemplos de entrenamiento
    - Técnicas de agrupamiento (“clustering”)
    - K-medias, EM, redes neuronales
    
## Minado de datos
#### Etapas
  * Limpieza
    - Remover datos ruidosos, inconsistentes, etc.
  * Integración
    - Combinar las diferentes fuentes de datos
  * Selección
    - Seleccionar el subconjunto de los datos relevante para el estudio. Si hay suficientes datos, guardar un subconjunto de estos para probar el modelo resultante
  * Transformación
    - Seleccionar atributos, generar atributos agregados, convertir tipos de variables, etc
  * Minado
    - Utilizar técnicas de clasificación y regresión (una tarea de minado involucra, por lo general, varias técnicas)
  * Evaluación
    - Identificar los resultados (patrones) interesantes (¿Qué es interesante?)
  * Presentación
    - Usar técnicas de visualización para presentar los resultados obtenidos.
    - Generar un sistema o protocolo para repetir el proceso con nuevos datos (de ser necesario)

#### Ejemplo, Caso Netflix
  * Descrición de los datos:
    - Los datos vienen en 1770 archivos de texto, uno por película
    - Cada archivo tiene en la primer línea el id de la película seguido de dos puntos “:”
    - El resto de la líneas tienen el siguiente formato: **_*Id_cliente, calificación, fecha*_**
    
##### **Etapa de PreProceso**
  * Limpieza
    - Los datos en el caso de Netflix están limpios. En otros ejercicios puede ser necesario remover ejemplos con errores, componer errores, llenar campos vacíos, homogeneizar valores (todo en mayúsculas,…), etc.
  * Integración
    - Son 1770 archivos, cómo los cargo todos? ¿Necesito todos?
    - Talvez generar un solo archivo que en cada línea tenga un cliente y, separado por comas, la calificación que da a una película
    - Buscar información adicional en IMDB y integrar
  * Selección
    - Sólo algunos clientes
    - Sólo algunas películas
    - Apartar un subconjuntos de datos para hacer pruebas
    - Remover fechas…
  * Transformación
    - Cambio de escala a calificaciones
    - Generación de variables derivadas

##### **Etapa de Minado**
  * Minado
    - Seleccionar técnicas de aprendizaje eg. C.5 y K-medias
    - Regresar, posiblemente, a la etapa de preproceso para alistar los datos
    - Minar, calcular errores, seleccionar otras técnicas,…

##### **Etapa de Post - Proceso**
  * Evaluación
  - Evaluar resultados. En este caso qué técnicas funcionaron, y que tan bien
  - En otros ejercicios de minado: que patrones interesantes se encontraron, por ejemplo
  * Presentación
    - Powerpoint + documento
    - Medidas de error para cada técnica
    - Tener el sistema listo para predecir
    - Netflix proporciona un archivo con clientes y películas para los cuales hay que generar una predicción. 

**_*Nota:*_** el proceso no es necesariamente lineal pues en ocasiones es necesario regresar a etapas anteriores

 [**  Video Humans Need Not Apply](https://www.youtube.com/watch?v=7Pq-S557XQU)
