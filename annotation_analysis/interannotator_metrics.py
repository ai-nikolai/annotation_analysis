####################################################
#
# This Work is written by Nikolai Rozanov <nikolai>
#
# Contact:  nikolai.rozanov@gmail.com
#
# Copyright (C) 2018-Present Nikolai Rozanov
#
####################################################

####################################################
# IMPORT STATEMENTS
####################################################

# >>>>>>  Native Imports  <<<<<<<
import json
import os
from typing import List, Optional, Any


# >>>>>>  Package Imports <<<<<<<
import numpy as np
# import sklearn.metrics
# import seaborn
# import pandas as pd
# import matplotlib.pyplot as plt

import krippendorff as kd
from statsmodels.stats import inter_rater as irr

# >>>>>>  Local Imports   <<<<<<<


####################################################
# CODE
####################################################
class Vocab:
    def __init__(self):
        self.token2index={}
        self.index2token={}
        self.unique_elements=0

    def add(self,token):
        """Add Element"""
        if not(token in self.token2index):
            self.index2token[self.unique_elements]=token
            self.token2index[token]=self.unique_elements
            self.unique_elements += 1
        return self.token2index.get(token)

    def t2i(self,token):
        """Return index from token"""
        return self.token2index.get(token)

    def i2t(self,index):
        """Return token from index"""
        return self.index2token.get(index)

    def fit(self, input_matrix):
        """Builds Vocab from list of lists of values."""
        for x in input_matrix:
            for y in x:
                self.add(y)

    def forward(self,input_matrix, as_numpy=False):
        """Forward pass on Matrix"""
        out_matrix = []
        for idx,x in enumerate(input_matrix):
            out_matrix.append( [self.t2i(y) for y in x] )

        if as_numpy:
            return np.array(out_matrix)
        else:
            return out_matrix

def krippendorff_alpha(annotations:List[Any], labels:Optional[List]=None, ignore:Optional[List]=None) -> float:
    """
    Arguments:
        - annotations:
            - The list of annotations, assumed to be one "row" per annotator (i.e. annotations[0] is annotator #1).
            - Number of Columns represents the number of datapoints.
            - Important: at this stage only hashable values are allowed.
            - E.g. with labels ["A","B"], and three datapoints and 2 annotators the following would be the valid structure:
            - [["A","B","A"],["A","B","B"]],
                - Annotator #1 (index=0) -> ["A","B","A"]
                - Annotator #2 (index=1) -> ["A","B","B"]

        - labels:
            - Represents the optional list of valid labels.
            - Important: at this stage only hashable values are allowed.

        - ignore:
            - Represents a list of optional labels that should be ignored
            - I.e. If this is non-empty then for any datapoint, if any of the annotators has the ignored label, the data point with all annotators is ignored

    Return:
        - Krippendorff Alpha score for all annotators.
    """
    vocab = Vocab()
    vocab.fit(annotations)
    numerical_annotations = vocab.forward(annotations, as_numpy=True)

    krippendorff = kd.alpha(numerical_annotations, level_of_measurement='nominal')
    return krippendorff


def fleiss_kappa(annotations:List[Any], labels:Optional[List]=None, ignore:Optional[List]=None) -> float:
    """
    Arguments:
        - annotations:
            - The list of annotations, assumed to be one "row" per annotator (i.e. annotations[0] is annotator #1).
            - Number of Columns represents the number of datapoints.
            - Important: at this stage only hashable values are allowed.
            - E.g. with labels ["A","B"], and three datapoints and 2 annotators the following would be the valid structure:
            - [["A","B","A"],["A","B","B"]],
                - Annotator #1 (index=0) -> ["A","B","A"]
                - Annotator #2 (index=1) -> ["A","B","B"]

        - labels:
            - Represents the optional list of valid labels.
            - Important: at this stage only hashable values are allowed.

        - ignore:
            - Represents a list of optional labels that should be ignored
            - I.e. If this is non-empty then for any datapoint, if any of the annotators has the ignored label, the data point with all annotators is ignored

    Return:
        - Fleiss Kappa score for all annotators.
    """
    vocab = Vocab()
    vocab.fit(annotations)
    numerical_annotations = vocab.forward(annotations, as_numpy=True)

    xT = numerical_annotations.transpose()
    agg = irr.aggregate_raters(xT)
    fleiss_kappa = irr.fleiss_kappa(agg[0], method='fleiss')
    return fleiss_kappa




####################################################
# MAIN
####################################################


# EOF
