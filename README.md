# Data augmentation Project

This is the project repository for the deeplearning seminar 2019/2020 for INFM, HS Offenburg.
The topic of my seminar project and talk is "data augmentation".

The file: data_augmentation_on_colab.ipynb ...

is a colab notebook that does data augmentation preprocessing to spare it at training time and use a offline augmentation approach. The augmentation can also be applied online, but the resulting training phase takes a lot longer, due to more augmentations to process on the rather weak colab cpus. The online augmentation has a higher variety of augmentations though. For the purpose of showing different augmentation and the improvement they can deliver, a offline is faster and yields sufficient results though.

The file: preprocess_local.ipynb ...

is a test tool notebook to test different augmentation libraries and show the augmentations. It can also be used to preprocess the images as tensors locally. It was used to save them and then upload the zip-archive to google drive and then mount it can copy it over to colab. For the final solution the preprocessing is also done on colab, making this file obsolete, but kept for faster augmentation testing locally with better cpu than on colab.

Jonas Bräuer
