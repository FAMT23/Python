

def seguridad(autenticado):

    def _seguridad(metodo):

        def inner(*args, **kwargs):
            if not autenticado:
                raise Exception("El usuario no esta autenticado")
            else:
                print("ok vamos a ejecutar", metodo.__name__)
                metodo(*args, **kwargs)

        return inner
    
    return _seguridad


@seguridad(True)
def funcion(ob, op=None, *args, **kwargs):
    print("Ejecutando funcion")
    print(ob, op, args, kwargs)


@seguridad(True)
def grabar(nombre):
    print("grabas ",nombre)    


if __name__ == "__main__":
    
    try:
        grabar("Jose")
        funcion(1,2,3,4,5,6,7,n=0,m=10)        
    except Exception as e:
        print("ERROR",e)