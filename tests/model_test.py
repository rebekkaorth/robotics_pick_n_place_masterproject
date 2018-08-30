import unittest
from model import reactive_net

'''
Unit test to test model.py 
'''


class TestModelMethod(unittest.TestCase):

    def test_reactive_net_init(self):
        print('test of reactive net init function')
        model = reactive_net(use_cuda=True)

        self.assertEqual(model.use_cuda, True)
        print(model.graspnet)

    def test_reactive_net_forward(self):
        print('test of reactive_net function forward')
        model = reactive_net(use_cuda=True)
        input_color_data = 0
        input_depth_data = 0
        is_volatile = False
        specific_rotation = -1

        result = model.forward(input_color_data, input_depth_data, is_volatile, specific_rotation)

        self.assertTrue(0 <= result <= 1)
