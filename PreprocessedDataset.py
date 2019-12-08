import os
import torch
from torch.utils.data import Dataset

#Loads the preprocessed batches
class PreprocessedDataset(Dataset):
    def __init__(self, path):
        self.path = path


    def __len__(self):
        fdir = self.path
        flist = os.listdir(fdir) # dir is your directory path
        number_files = len(flist)
        return number_files
        
        
    def __getitem__(self, idx):
        if(idx >= self.__len__()):
            raise StopIteration
        return torch.load(self.path + '/{}'.format(idx))
    