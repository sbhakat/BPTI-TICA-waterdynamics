#!/usr/bin/env python
import pandas as pd 
import mdtraj as md 
from msmbuilder.dataset import dataset
from msmbuilder.utils import load
from msmbuilder.featurizer import ContactFeaturizer
from msmbuilder.featurizer import RawPositionsFeaturizer
from tica_metadynamics.plumed_writer import render_tic

#python imports
import os,glob
import numpy as np
import pickle


ds = dataset("../Conv-BPTI-all-*.dcd",  #38943.xtc",
              topology='prot_maeconv.pdb')


#define our featurizer
feat = RawPositionsFeaturizer(atom_indices=np.array([84,103,118,132,146,167,181,188,202,212,234,244,268,287,306,330,351,371,392,406,416,438,448,455,474,484,501,515,535,551,572,579,586,596,620,630,652,676,690,704,724,746,757,767,782,794,804,821,845,859,869])-1, ref_traj=md.load('../Conv-BPTI-all-0000.dcd', top='prot_maeconv.pdb'))

top = md.load('prot_maeconv.pdb')
# this basically maps every feature to atom indices. 
df = pd.DataFrame(feat.describe_features(ds[0]))

tica_mdl = load("tica_mdl_rawpos.pkl")

#Then to render tIC 0
print(render_tic(df,tica_mdl, 4))
