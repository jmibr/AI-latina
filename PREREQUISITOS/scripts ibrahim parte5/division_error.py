while True:
    try:
        dividendo= float(input('Ingrese el dividendo:'))
        divisor= float(input('Ingrese el divisor: '))
        division= dividendo/divisor
        print('La division da: ', division)
    except ZeroDivisionError:
        print('No se puede dividir por cero. Ingrese otro divisor.')
    except ValueError:
        print('No ingreso un numero. Intente nuevamente.') 
   
