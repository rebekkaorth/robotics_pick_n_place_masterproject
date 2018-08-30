import unittest
from trainer import Trainer

'''
Unit test to test trainer.py 
'''


class TestTrainer(unittest.TestCase):

    def test_trainer_init(self):
        print('test of trainer init method')

        is_testing = True
        load_snapshot = 'test'
        snapshot_file = 'test'
        force_cpu = True

        trainer = Trainer(is_testing, load_snapshot, snapshot_file, force_cpu)

    def test_trainer_preload(self):
        print('test of trainer preload method')

        is_testing = True
        load_snapshot = 'test'
        snapshot_file = 'test'
        force_cpu = True

        trainer = Trainer(is_testing, load_snapshot, snapshot_file, force_cpu)

    def test_trainer_forward(self):
        print('test of trainer forward method')

        is_testing = True
        load_snapshot = 'test'
        snapshot_file = 'test'
        force_cpu = True

        trainer = Trainer(is_testing, load_snapshot, snapshot_file, force_cpu)

        forward_result = trainer.forward()  # parameters need to be filled in

    def test_trainer_get_label_value(self):
        print('test of trainer get label value method')

        is_testing = True
        load_snapshot = 'test'
        snapshot_file = 'test'
        force_cpu = True

        trainer = Trainer(is_testing, load_snapshot, snapshot_file, force_cpu)

        label_value = trainer.get_label_value()  # parameters need to be filled in

    def test_trainer_backprop(self):
        print('test of trainer backprop method')

        is_testing = True
        load_snapshot = 'test'
        snapshot_file = 'test'
        force_cpu = True

        trainer = Trainer(is_testing, load_snapshot, snapshot_file, force_cpu)

        '''
        To test backprop: 
            test how weights have changed before and after the function has finished
        '''

    def test_trainer_get_prediction_vis(self):
        print('test of trainer get prediction vis method')

        is_testing = True
        load_snapshot = 'test'
        snapshot_file = 'test'
        force_cpu = True

        trainer = Trainer(is_testing, load_snapshot, snapshot_file, force_cpu)

        canvas = trainer.get_prediction_vis()  # parameters need to be filled in

    def test_trainer_push_heuristic(self):
        print('test of trainer push heuristic')

        is_testing = True
        load_snapshot = 'test'
        snapshot_file = 'test'
        force_cpu = True

        trainer = Trainer(is_testing, load_snapshot, snapshot_file, force_cpu)

        push_heuristic = trainer.push_heuristic()  # parameter needs to be filled in

    def test_trainer_grasp_heuristic(self):
        print('test of trainer grasp heuristic')

        is_testing = True
        load_snapshot = 'test'
        snapshot_file = 'test'
        force_cpu = True

        trainer = Trainer(is_testing, load_snapshot, snapshot_file, force_cpu)

        grasp_heuristic = trainer.grasp_heuristic()  # parameter needs be filled in
