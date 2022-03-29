from datetime import datetime

def imprimeVarsRequest(request):
    print('------------GET----------------')
    print(request.GET)
    print('------------POST----------------')
    print(request.POST)



def guardaEnDebug(cosa_a_guardar, nombre_guardar, extension='.txt'):
    dirDebug = '/home/javier/Documents/TODO_APP_2/debugs'
    archFinal = dirDebug + '/' + nombre_guardar + extension
    with open(archFinal, 'w') as arch:
        # arch.write(datetime.now().strptime())
        arch.write(f'{datetime.now()}\n\n\n')
        arch.write(cosa_a_guardar)

