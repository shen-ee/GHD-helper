import os
import cv2
import numpy as np

# Read imgs from test-classes folders as an array
def load_data(path, print_file_read = True):
    '''
    :param path(str): root path of dataset, e.g."/Users/shenyi/Desktop/Gamepipe/trainset/"
    :param print_file_read(bool): show current processing file names
    :return np.array(imgs): numpy format array of images, with shape (num_of_pictures, width, length, channels)
            ap.array(labels): numpy format array of labels
    '''
    imgs = []
    labels = []
    cates = next(os.walk(path))[1]
    folders = [path + x for x in cates if os.path.isdir(path + x)]

    for idx, folder in enumerate(folders):
        i = 1
        for root, subFolers, files in os.walk(folder):
            for file in files:
                if (os.path.splitext(file)[1] in ['.jpg', '.bmp', '.png', 'jpeg']):
                    img_path = os.path.join(root, file)
                    if (print_file_read):
                        print('Reading image %d:%s' % (i, img_path))
                    img = cv2.imread(img_path)
                    imgs.append(img)
                    labels.append(idx)

    return np.array(imgs), np.array(labels)


def main():
    load_data("/Users/shenyi/Desktop/Gamepipe/trainset/")

if __name__ == '__main__':
    main()