import numpy as np
import scipy.io
import matplotlib.pyplot as plt

def get_data(dataset_name):
    dataset = scipy.io.loadmat('data/' + dataset_name + '.mat')
    Ct = np.array(dataset['Ct'])
    Yt = np.array(dataset['Yt'])
    Cv = np.array(dataset['Cv'])
    Yv = np.array(dataset['Yv'])
    return Ct, Cv, Yt, Yv