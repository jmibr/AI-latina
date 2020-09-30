from other_functions.class_functions import funciones
numero= float(input ('Ingrese el numero: ')  )
numero2= float(input('Ingrese el divisor para la calcular el modulo: '))
pow2=numero
pow3=numero
mod2=numero
mod1=numero2
resultado=funciones(pow2,pow3,mod2,mod1)
escoger=1
while escoger!=0:
    print('0. Salir','\n', '1. Elevar al cuadrado', '\n','2. Elevar al cubo', '\n', ' 3. Calcular el modulo')
    escoger=int(input('Ingrese su seleccion: '))
    if escoger ==0:
        print('Saliendo', )
    elif escoger==1:
        print('Resultado: ', resultado.cuadrado(pow2))
    elif escoger==2:
        print('Resultado: ', resultado.tercero(pow3))
    elif escoger==3:
        print('Resultado: ', resultado.modulo(mod2, mod1))

print()