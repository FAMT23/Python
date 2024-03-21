# Elecciones

def abs(numero):

    if numero >= 0:
        return numero
    else:
        return -1 * numero


class Candidato(object):

    def __init__(self,letra,numVotos):
        self.letra = letra
        self.numVotos = numVotos

    def incrementarVotos(self,votos):
        self.numVotos += votos
        

class Censo(object):

    def __init__(self,listaIDs):
        self.listaIDs = listaIDs


    def estaEnCenso(self,codigo):
        if codigo in self.listaIDs:
            return True
        else:
            return False


    def borrarDelCenso(self,codigo):
        self.listaIDs.remove(codigo)



class Votante(object):

    def __init__(self,codigo,edad,listaVotos):
        self.codigo = codigo
        self.edad = edad
        self.listaVotos = listaVotos

class Elecciones(object):

    def __init__(self,censo):
        self.censo = censo
        self.candidatos = [Candidato('A',0), Candidato('E',0), Candidato('I',0), Candidato('O',0), Candidato('U',0)]
        

    def votar(self,votante):
        if self.comprobarVoto(votante.listaVotos):
            if self.censo.estaEnCenso(votante.codigo):
                self.censo.borrarDelCenso(votante.codigo)

                i = 0
                for voto in votante.listaVotos:
                    self.candidatos[i].incrementarVotos(voto[1])
                    i+=1
                
            else:
                print ('El votante ' + str(votante.codigo) + ' no esta en el censo')
        else:
            print ('El voto de votante ' + str(votante.codigo) + ' supera los 100 puntos')
   


    def comprobarVoto(self,voto):
        # comprueba que los votos sean <= que 100
        numVotos = 0
        for v in voto:
            numVotos += abs(v[1])

        if numVotos <= 100:
            return True
        else:
            return False
            

    def escrutinio(self):
        for c in self.candidatos:
            print (c.letra + ' -> ' + str(c.numVotos))


    def ganador(self):
        maximo = self.candidatos[0].numVotos
        letraMax = self.candidatos[0].letra

        for c in self.candidatos:
            if maximo < c.numVotos:
                maximo = c.numVotos
                letraMax = c.letra

        print ('El ganador es ' + letraMax + ' con ' + str(maximo) + ' puntos')
        

censo = Censo([1,2,3,4,5,6,7,8,9])
elecciones = Elecciones(censo)

vot1 = Votante(4,30,[('A',30),('E',8),('I',50),('O',-2),('U',10)])
vot2 = Votante(7,45,[('A',9),('E',-1),('I',40),('O',20),('U',-30)])

elecciones.votar(vot1)
elecciones.votar(vot2)
elecciones.votar(vot2)

elecciones.escrutinio()
elecciones.ganador()
