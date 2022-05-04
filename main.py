import random
import threading
import time


# TODO - simular atraso de rede e depois ack das mensagens para ordenação total
class Processo(threading.Thread):

    def __init__(self, num_processo, outro_processo=None):
        super(Processo, self).__init__()
        self.num_processo = num_processo
        self.outro_processo = outro_processo
        self.relogio = 0
        self.codigo_mensagem = 0

    def enviar_mensagem(self):
        self.relogio += 1
        self.codigo_mensagem += 1
        mensagem = 'm' + self.num_processo + '-' + str(self.codigo_mensagem)
        print('p' + self.num_processo, 'enviando:', mensagem)
        self.outro_processo.receber_mensagem(mensagem, self.relogio)

    def receber_mensagem(self, mensagem, relogio):
        self.relogio = 1 + max(relogio, self.relogio)
        print('p' + self.num_processo, 'recebeu:', mensagem)

    def run(self):
        while True:
            time.sleep(random.randrange(0, 3))
            self.enviar_mensagem()


print('== Relógio Lógico de Lamport ===')
print('mx-y -> x representa o número do processo; y o número da mensagem no processo')
print('obs.: ainda não faz ordenação total, e não há simulação de atraso em rede')
p1 = Processo('1')
p2 = Processo('2', p1)
p1.outro_processo = p2

p1.start()
p2.start()
