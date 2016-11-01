## Repaso de probabilidad
 * Teorema de Bayes
 * Estmicación de parámetros
  + Estimador de máxima verosimilitud(MLE)
  + Máximo a posteriori (MAP)
  
## Predicción Probabilística
### Modelos predictivos basados en probabilidades
Son efectivoss en una gran cantidad de casos.
  * **Tipo de método:** Supervisado
  * **Supuestos:** Ejemplos de entrenamiento son representativos
  * Los datos provienen de un proceso que no es totalmente conocido
  * Nosotros lo modelamos como un **proceso estocástico**
     + Por ejemplo: los datos son resultados de volados, los datos son precios de una acción
  * Gracias a que no tenemos toda la información necesaria para descubrir el proceso determinista que lo rige, definimos una variable aleatoria X que pude tomar distintos valores
    + Águila o Sol en el caso de los volados
    + Un número real positivo para las acciones  
  * Deseamos encontrar la probabilidad P(X=valor)
  * En el caso de los volados supongamos que P(X=aguila) =po
    + ¿Qué en P(X=sol)?
    + ¿Cómo calculamos po?
      - Lo estimamos de una muestra  de tamaño N (ejemplos de aprendizaje): p^o=número de aguilas/N

### Modelos predictivos basados en probabilidades
 * Estimar frecuencias
 * Calcular probabilidades
 * Usar regla de Bayes

## Teorema de Bayes
 + Para calcular arg maxC {Pr(C|A1 . . .An)}: repasamos la regla de Bayes y la aplicamos,
   - Pr(C|A1 . . .An) = Pr(A1 . . .An|C) ∗ Pr(C)/Pr(A1 . . .An)
   - El divisor es el mismo para todos los valores de C, por lo cual para encontrar el valor de C que maximiza la probabilidad podemos prescindir de la división.
   - Y ahora suponemos independencia (condicionada a la clase).
   - Pr(A1 . . .An|C) ∗ Pr(C) = Pr(A1|C) ∗ . . . ∗ Pr(An|C) ∗ Pr(C)
 + **Ejemplo**:
   - Supongamos ahora que lo que tenemos es una base de datos de clientes de un banco y deseamos un  modelo para determinar si un cliente nuevo es de alto o bajo riesgo para un préstamo 
   - Supongamos que las variables de interés son la ingreso mensual y su saldo actual
   - Lo que queremos calcular es P(C|X1,X2)
   - Donde C puede ser alto o bajo riesgo y X1 es el valor del ingreso mensual y X2 el saldo actual 
   - De esta manera podemos definir que un cliente es de alto riesgo si P(C=alto|ingreso_cliente, saldo_cliente)>=0.2
   - En este caso es la probabilidad de que el cliente sea de alto riesgo dado que ya observamos su ingreso y saldo P(C|X1,X2) es la probabilidad posterior

|Ingreso|Saldo|Clase|
|---|---|---|
|20|10|alto|
|30|40|bajo|
|30|10|alto|
|10|30|bajo|
|20|10|alto|
|20|10|bajo|
|20|05|alto|
     
Queremos predecir

|Ingreso|Saldo|Clase|
|---|---|---|
|20|10|?|
|30|40|?|
|20|05|?|

  * P(C | Ingreso, Saldo) = P( C )*P(Ingreso,Saldo|C) / P(Ingreso,Saldo)
  * N = 7
  * Paso 1 - Obtener la Probabilidad de la clase
    + Pr(C=alto)= 4/7 y Pr(C=bajo)= 3/7, la suma debe ser 1.
  * Paso 2 - Obtener la Probabilidad de las variables, dada la clase.
    + Ingreso=20,Saldo=10:
      - Pr(Ingreso=20,Saldo=10|c=alto)=2/4
      - Pr(X1=20,X2=10|C=bajo)= 1/4
    + Ingreso=30,Saldo=40:
      - Pr(Ingreso=30,Saldo=40|c=alto)=0/4
      - Pr(Ingreso=30,Saldo=40|C=bajo)= 1/3
    + Ingreso=20,Saldo=5:
      - Pr(Ingreso=20,Saldo=5|c=alto)=1/4
      - Pr(Ingreso=20,Saldo=5|C=bajo)= 0/3
  * Paso 3 - Obtener la Probabilidad total
    + Pr(Ingreso=20, Saldo|C=alto=10) + Pr(Ingreso=20, Saldo=10|C=bajo)=(4/7)(2/4) + (3/7)(1/3) = 0.428571429
    + Pr(Ingreso=30, Saldo|C=alto=40) + Pr(Ingreso=30, Saldo=40|C=bajo)=(4/7)(0) + (3/7)(1/3) = 0.142857143
    + Pr(Ingreso=20, Saldo|C=alto=5) + Pr(Ingreso=20, Saldo=5|C=bajo)=(4/7)(1/4) + (3/7)(0) = 0.142857143
    
  * Paso 4 - Aplicando la fórmula P(C | Ingreso, Saldo) = P( C )*P(Ingreso,Saldo|C) / P(Ingreso,Saldo), seleccionamos el argumento máximo para cada caso.
    + Ingreso=20,Saldo=10:
      - ** P(C=alto|Ingreso=20, Saldo=10) = (4/7)(2/4)/(4/7)(2/4)+(3/7)(1/3)= 0.666666667**
      - P(C=bajo|Ingreso=20, Saldo=10) = (3/7)(1/3)/(4/7)(2/4)+(3/7)(1/3)= 0.333333333
    + Ingreso=30,Saldo=40:
      - P(C=alto|Ingreso=30, Saldo=40) = (4/7)(0/4)/(4/7)(0/4)+(3/7)(1/3)= 0
      - ** P(C=bajo|Ingreso=30, Saldo=40) = (3/7)(1/3)/(4/7)(0/4)+(3/7)(1/3)= 1**
    + Ingreso=20,Saldo=5:
      - ** P(C=alto|Ingreso=20, Saldo=5) = (4/7)(1/4)/(4/7)(1/4)+(3/7)(0/3)= 1**
      - P(C=bajo|Ingreso=20, Saldo=5) = (3/7)(1/3)/(4/7)(0/4)+(3/7)(1/3)= 0

El resultado sería:

|Ingreso|Saldo|Clase|
|---|---|---|
|20|10|alto|
|30|40|bajo|
|20|05|alto|

### Ejercicios - Casos Contraintuitivos de la Probabilidad
 * **Película "Rosencrantz y Guildenstern han muerto"**
  - En la escena que abre la película, Rosencrantz va lanzando monedas al aire.
  - Si sale cara, la pierde y se la lleva Guildenstern; de lo contrario, se supone que recibe una moneda de Guildenstern.
  - Lleva lanzadas noventa y una. Todas han salido cara (y, por tanto, se las ha llevado Guildenstern).
  - A la próxima vez, la probabilidad de cruz es mayor, ¿no? **Pues, de hecho. . . ¡no!**
  - **_*¡Son eventos independientes!*_**
 
 * **La paradoja de Monty Hall (Catafixia de Chabelo)**
  - Se supone que todos los participantes en el juego conocen las reglas.
  - Detrás de una de las tres puertas está el coche; tú eliges una puerta.
  - Chabelo abre una puerta distinta de la elegida, y te muestra que el coche no está tras ella.
  - Y te pregunta: ¿seguro que no quieres cambiar?
  - ¿Es mejor cambiar? ¿es mejor mantener la elección? ¿da igual?
  - ¡Para que el problema esté bien planteado hemos de acordar qué significa "mejor"!

 * **La paradoja de Simpson**
  - Supongamos que las encuestas nos dicen:
   + En la provincia de C´aceres, los vegetarianos son menos propensos a tener ojeras que los no vegetarianos;
   + Y que en la provincia de Badajoz, los vegetarianos también son menos propensos a tener ojeras que los no vegetarianos.
   + Podemos deducir que esa correlaci´on se da en toda Extremadura,¿no?
   + **_*¡Error!*_** Es posible que, en la población conjunta, la ratio vaya a la inversa.

## Naive Bayes - Bayes ingenuo discreto
  * Supuesto: 
    + Las probabilidades de clase son independientes.
    + Supone que todos los atributos son independientes conocida la variable clase.
    
  * **Dificultades del método**:
    + El número de ejemplos necesarios crece muy rápido con el número de atributos
    + No esta definido para atributos que no se encuentran en el conjunto de entrenamiento. 
    + La estimación de probabilidad que se mencionó no sirve para variables contínuas
    
Tomando el ejemplo anterior, qué pasaría si además de Ingreso y Saldo, ¿tuviéramos más atributos?, probabilidad de la clase la calcularíamos como: 
  * Pr(C=alto|X1...Xn)=Pr(C=alto)Pr(X1|C=alto)....Pr(Xn|C=alto)
  * Asumiendo independencia condicional
    + Pr(C=alto|X1...Xn)=Pr(C=alto)∏Pr(Xi|C=alto)
  * Ejemplo:
    + P(C=alto|Ingreso=30, Saldo=5)= Pr(C=alto)Pr(Ingreso=30|C=alto)Pr(Saldo=5|C=alto)= (4/7)(1/4)(1/4)=0.03571429
    + P(C=bajo|Ingreso=30, Saldo=5)= Pr(C=bajo)Pr(Ingreso=30|C=bajo)Pr(Saldo=5|C=bajo)= (3/7)(1/3)(0)=0
    + P(C=alto|Ingreso=20, Saldo=10)= Pr(C=alto)Pr(Ingreso=20|C=alto)Pr(Saldo=10|C=alto)= 0.3214286
    + P(C=bajo|Ingreso=20, Saldo=10)= Pr(C=bajo)Pr(Ingreso=20|C=bajo)Pr(Saldo=10|C=bajo)= (3/7)(1/3)(1/3)=0.04761905

### Algunos valores no existen en el set de datos actual, por lo que su probabilidad nos da 0, para mitigar este punto usamos el Suavizamiento de Laplace:
    + Sumar un término en el numerador y en el denominador
    + P^(C)= (|C|+1)/(numdatos + numCat)
      - donde C es una categoría y |C| es el número de datos con categoría C.
      - Ejemplo: 
        + P(C=alto)= 4 + 1 / 7 + 1 * 2 =0.5556
        + P(C=bajo)= 3 + 1 / 7 + 1 * 2= 0.4444
        
    + P^(x|C)= (1+|x^C|)/(|C|+unique(C))
      - donde |x^C| es el número de veces que x tiene una categoría C y unique(C) es el número de datos diferentes con categoría C.

  * Para clasificar un nuevo valor
    + C^<-arg max P(C=alto)=Pr(C=alto)∏Pr(Xi_nuevo|C=alto)
    
## Gaussian Naive Bayes
  * Se utiliza para valores continuos.
  * Supone que los datos se distribuyen de acuerdo a una distribución, en base a esto calculamos las probabilidades de clase, generalmente se utiliza la normal.
  * Se utiliza la función de densidad.
    + No da una probabilidad, recordemos que la probabilidad de una variable continua es 0 por definición.
    + Lo que nos da es la **altura** de la función en un punto, para calcular las probabilidades necistaríamos definir una base(para aproximar base * altura)
    + Ejemplo de clasificación de spam de una base de datos de correos.
      - Paso 1 - Obtenemos la media (p) y la desviación estándar(st) de los datos.
      - Paso 2 - Recordemos que suponemos independiencia condicional, Pr(C=Spam|A1...An)=Pr(C=Spa,)∏Pr(Xi|C=alto), pero es mucho mas fácil para la computadora(y para nosotros) utilizar logaritmo, por que aplicando logaritmo la multiplicación se convierte en sumatoria:
        - Pr(C=Spam|A1, A2,...,An)= Log(C=Spam) + ∑log(Pr(Ai|C=Spam))
        - Pr(C= NoSpam|A1, A2,...,An)= Log(C=NoSpam) + ∑log(Pr(Ai|C=NoSpam))
      - Paso 3 - Para predecir si es Spam o no, nos falta utilizamos la función de densidad de la normal para realizar el cálculo:
        - Pr(X|C) = arg max Log(C) + ∑log( fd_normal( p,st, Pr(Ai|C))
        


## Material Adicional
  * [Andrew Moore's Basic Probability Tutorial](http://www.autonlab.org/tutorials/prob.html)
  * [Bishop: Pattern Recognition and Machine Learning: Ch. 1 thru 1.2.3, Ch 2 thru 2.2](https://drive.google.com/file/d/0B60o2E1S5j6rTVl2WlJsa09WTDQ/view?usp=sharing)
  * [José L. Balcázar: Minería de Datos](http://www.mavir.net/docs/jlb-MineriaDatos.pdf)
