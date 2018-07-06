import torch
import numpy as np
import pandas as pd
from torch.utils.data import Dataset
from torchvision import transforms, datasets
import ycb_downloader


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

    def data_loader(self, root_dir):
        files = [[]]
        from os import walk
        for (dirpath, dirname, filenames) in walk(root_dir):
            files.extend(dirname)

            for imgNames in walk(root_dir + '/' + dirname + '/' + dirname + '_1'):
                files[dirname].extend(imgNames)

        return files


date = Dataset_provider('rgbd-dataset')
# print(date.get_img_from_dataset(date.root_dir, date.data_loader(date.root_dir), 11))
print(date.data_loader('rgbd-dataset'))
