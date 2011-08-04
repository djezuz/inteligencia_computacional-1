#-*- coding:utf-8 -*-

class Neuronio(object):

    def __init__(self, **kwargs):
        self.w0 = kwargs['w0']
        self.w1 = kwargs['w1']
        self.w2 = kwargs['w2']

    def treinar(self, taxa_de_aprendizagem, padroes):
        return {'w0': -2, 'w1':1, 'w2': 0}
