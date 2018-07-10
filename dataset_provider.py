import torch
import numpy as np
from PIL import Image
from torch.utils.data import Dataset
from torchvision import transforms, datasets
import ycb_downloader
import os
from pyntcloud import io  # https://github.com/daavoo/pyntcloud (10/07/2018)


class Dataset_provider (Dataset):

    def __init__(self, root_dir, transform=None):
        """
        Args:
        csv_file (string): Path to the csv file with annotations.
        root_dir (string): Directory with all the images.
        transform (callable, optional): Optional transform to be applied
        on a sample.
        """

        self.root_dir = root_dir
        self.transform = transform

    def __len__(self):
        return len(self.file)

    """
    images are not always the same size. 
        -> images are scaled
        -> images are cropped randomly 
        -> images are converted from numpy images to torch images 
    images are therefor pre-processed 
    """
    def transform_dataset(self):
        data_transform = transforms.Compose([
            transforms.RandomSizedCrop(224),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])

        hymenoptera_dataset = datasets.ImageFolder(root='hymenoptera_data/train', transform=data_transform)
        dataset_loader = torch.utils.data.DataLoader(hymenoptera_dataset, batch_size=4, shuffle=True, num_workers=4)

        return dataset_loader

    def get_img_from_dataset(self, root_dir, datatset_loader, idx):

        load_tensor = datatset_loader[2][idx]
        depth_img = np.load(str(root_dir) + '/' + str(load_tensor))['arr_0'][478]
        color_img = 0

        return depth_img

    # Download dataset
    def data_loader(self):
        ycb_downloader.download_files()

    def get_directory_name_from_downloaded_files(self):
        path = './ycb/'
        object_directories = []

        for object_directory in os.listdir(path):
            object_directories.append(object_directory)

        return object_directories

    def get_images(self, idx):

        # self.data_loader()
        # load object directory based on given index
        object_dir = self.get_directory_name_from_downloaded_files()[idx]
        print(object_dir)

        # load content directory into array to make it accessible
        color_img = Image.open('./ycb/' + object_dir + '/NP1_0.jpg')
        print(color_img)
        depth_img = Image.open('./ycb/' + object_dir + '/masks/NP1_0_mask.pbm')

        cloud_file = io.read_ply('./ycb/' + object_dir + '/clouds/merged_cloud.ply')

        return color_img, depth_img, cloud_file


dataset = Dataset_provider('ycb')
dataset.get_images(0)

