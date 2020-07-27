#!/usr/bin/env python
#msmbuilder imports 
from msmbuilder.dataset import dataset
from msmbuilder.featurizer import ContactFeaturizer
from msmbuilder.featurizer import RawPositionsFeaturizer
from msmbuilder.decomposition import tICA
from msmbuilder.cluster import MiniBatchKMeans
from msmbuilder.msm import ContinuousTimeMSM
from msmbuilder.utils import verbosedump,verboseload
from msmbuilder.cluster import KCenters
from msmbuilder.utils import load
from msmbuilder.featurizer import ContactFeaturizer
from msmbuilder.featurizer import RawPositionsFeaturizer


#other imports
import os,glob,shutil
import numpy as np
import mdtraj as md
import pandas as pd 
import pickle


ds = dataset("../Conv-BPTI-all-*.dcd",  
              topology='prot_maeconv.pdb')


ds0 = dataset("prot_maeconv.pdb",
              topology='prot_maeconv.pdb')

#define our featurizer
feat = RawPositionsFeaturizer(atom_indices=np.array([84,103,118,132,146,167,181,188,202,212,234,244,268,287,306,330,351,371,392,406,416,438,448,455,474,484,501,515,535,551,572,579,586,596,620,630,652,676,690,704,724,746,757,767,782,794,804,821,845,859,869])-1, ref_traj=md.load('../Conv-BPTI-all-0000.dcd', top='prot_maeconv.pdb'))
#shutil.rmtree("res_contact_rawpos/") 
ds_contact=ds.fit_transform_with(feat, "res_contact_rawpos/",fmt='dir-npy')
#we can load the features using
#ds_contact = dataset("./res_contact_rawpos/")

#shutil.rmtree("res_contact_rawpos0/")
ds0_contact=ds0.fit_transform_with(feat, "res_contact_rawpos0/",fmt='dir-npy')
#ds0_contact = dataset("./res_contact_rawpos0/")

#print(ds_contact[0][0,:])
#print(ds0_contact[0][0,:])
#ds_contact[0]-=ds0_contact[0]
print(ds_contact[0][0,:])
print(ds_contact[0]-ds0_contact[0])
for i in range(len(ds_contact)):
    np.save("./subtracted/%08d.npy"%i, ds_contact[i]-ds0_contact[0])
ds_contact = dataset("./subtracted/")
print(len(ds_contact))
print(ds_contact[0])




#see how many trajectories were retained during featurization
#print(len(ds_contact),len(ds))

from msmbuilder.io import load_trajs, save_trajs, save_generic
from msmbuilder.io.sampling import sample_dimension
from msmbuilder.io import load_trajs, save_generic, preload_top, backup

ncomp = 5

#define our tica model
tica_mdl = tICA(lag_time=100,n_components=ncomp, kinetic_mapping=False)

#transform the dataset with tica
#shutil.rmtree("reg_ticas_10lt_4tics_rawpos/")
tica_features = ds_contact.fit_transform_with(tica_mdl, out_ds = 'reg_ticas_10lt_4tics_rawpos//')

#load the features
tica_features = dataset("./reg_ticas_10lt_4tics_rawpos/")

#for each feature from our contact we now have 4 tICs
#for each feature from our contact we now have 4 tICs
verbosedump(tica_mdl,"tica_mdl_rawpos.pkl")
