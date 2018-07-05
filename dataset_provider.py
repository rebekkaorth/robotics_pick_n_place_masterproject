import torch
import numpy as np
import pandas as pd
from torch.utils.data import Dataset
from torchvision import transforms, datasets


class Dataset_provider (Dataset):

    def __init__(self, file, root_dir, transform=None):
        """
        Args:
        csv_file (string): Path to the csv file with annotations.
        root_dir (string): Directory with all the images.
        transform (callable, optional): Optional transform to be applied
        on a sample.
        """

        self.file = pd.read_csv(file)
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

    def get_img_from_dataset(self, datatset_loader, idx):

        color_img = datatset_loader[idx]
        depth_img = datatset_loader[idx]

        return color_img, depth_img


    # def convert_images(self, raw_image):
    #
    #     raw_image = raw_image
    #     im_width = 640
    #     im_height = 480
    #
    #     # resolution = 640 * 480
    #
    #     depth_scale = np.fromstring(raw_image[(9 * 4):(10 * 4)], np.float32)[0]
    #     depth_img = np.fromstring(raw_image[(10 * 4):((10 * 4) + im_width * im_height * 2)], np.uint16).reshape(
    #         im_height, im_width)
    #     color_img = np.fromstring(raw_image[((10 * 4) + im_width * im_height * 2):], np.uint8).reshape(
    #         im_height, im_width, 3)
    #     depth_img = depth_img.astype(float) * depth_scale
    #     color_img = color_img.astype(np.uint8)
    #
    #     return color_img, depth_img, depth_scale
