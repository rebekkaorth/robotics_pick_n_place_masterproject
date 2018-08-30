import unittest
from dataset_provider import Dataset_provider

'''
Unit test to test dataset_provider.py 
'''


class TestDatasetProvider(unittest.TestCase):

    """
    Not yet clear if needed

    def test_transform_dataset(self):
        print('test of dataset provider to transform dataset')

        datset_prov = Dataset_provider('./ycb')
        result = datset_prov.transform_dataset()

    def test_get_img_from_dataset(self):
        print('test of dataset provider to get single image from dataset')

    """

    def test_data_loader(self):
        print('test of dataset provider loading of data')

        '''
        check if download is started/ check is link is correct 
        '''

    def test_get_directoryname_of_downloaded_files(self):
        print('test of dataset porivder to get directory name of downloaded files')

        '''
        check if length of dataset is as long as it is supposed to be
        '''

    def test_get_image(self):
        print('test of datasetprovider to get an image from loaded dataset')

        '''
        check if color_img + depth_img have correct file path/ file name
        '''
