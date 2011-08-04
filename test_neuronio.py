#-*- coding:utf-8 -*-
import unittest
from should_dsl import should, should_not

from neuronio import Neuronio

class TestNeuronio(unittest.TestCase):

    def setUp(self):
        w = {'w0': 0, 'w1':0, 'w2': 0}
        self.neuronio = Neuronio(**w)

    def test_neuronio(self):
        self.neuronio.w0 |should| equal_to(0)
        self.neuronio.w1 |should| equal_to(0)
        self.neuronio.w2 |should| equal_to(0)

    def test_treinamento_neuronio_4_padroes_operacao_e(self):
        aprendizagem = 1
        padroes = {
                    'padrao_1': {'x1': 0, 'x2': 0, 'y': 0},
                    'padrao_2': {'x1': 0, 'x2': 1, 'y': 0},
                    'padrao_3': {'x1': 1, 'x2': 0, 'y': 0},
                    'padrao_4': {'x1': 1, 'x2': 1, 'y': 1},
                  }
        w_treinado = self.neuronio.treinar(taxa_de_aprendizagem=aprendizagem, padroes=padroes)
        w_treinado |should| equal_to({'w0': -2, 'w1':1, 'w2': 0})

if __name__ == '__main__':
    unittest.main()
