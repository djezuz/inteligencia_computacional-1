#-*- coding:utf-8 -*-

class Neuronio(object):

    def __init__(self, **kwargs):
        self.w0 = kwargs['w0']
        self.w1 = kwargs['w1']
        self.w2 = kwargs['w2']
