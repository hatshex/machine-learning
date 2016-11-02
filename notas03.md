## Regresión Lineal
  * Método **Supervisado**, siempre nos dan el dato de entrenamiento tiene un valor numérico asociado.
    + (X1, y1), (X2,y2)...
    + Ls yi son valores numéricos y representan el valor de entrenamiento de la función objetivo.
    
  * **Objetivo**: Determinar el valor de y para datos nuevos.
     
  * **Supuestos:** 
    + Atributos numéricos
    + Muestras de datos, i.i.d. -> independientes e idénticamente distribuidas
    + Asume que la función que se intenta estimar V es adecuadamente aproximada por una recta, un plano o un hiperplano.
    + V es una función desconocida que intenta explicar la relación entre las X's y las y.

  * El modelo de regresión lineal, tiene la siguiente forma:
    + $\hat{V}(X)= w_{0} + \sum_{i=1}^n x_{i}w_{i}$  es lo mismo que $\hat{y}= w_{0} + \sum_{i=1}^n x_{i}w_{i} $
    + $\hat{y}$ es la aproximación lineal a y, la función que verdaderamente describe los datos
  
  
### Medidas de ajuste
  * Mínimos cuadrados
  * Menor error cuadrático medio -> LMS -> Widrow Hoff
