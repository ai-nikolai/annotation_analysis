# coding=utf-8


##########################
# Import
##########################
from setuptools import setup, find_packages

setup(
    #
    # SETUP
    #
      name          ='annotation_analysis',
      version       ='0.0.0.1',
      description   ='Annotation Analysis',
      url           ='https://github.com/ai-nikolai/annotation_analysis',
      author        ='Nikolai Rozanov',
      author_email  ='nikolai.rozanov@gmail.com',
      license       ='GPL 2.0',
    #
    # Actual packages, data and scripts
    #

      packages      =find_packages(),
      # scripts       =[
      #                   'bin/anas'
      #               ],
    #
    # Requirements
    #
      install_requires=[]
      )
