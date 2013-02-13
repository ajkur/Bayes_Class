#!/usr/bin/env python

import subprocess, os, sys

texpath = os.getcwd()

# print 'Making Plots ...'
# os.chdir('Scripts/')
# os.system('python pi_plot.py')
# os.chdir(texpath)

print 'Making Paper ...'
os.system('pdflatex bayes_hw2.tex')
os.system('pdflatex bayes_hw2.tex')

print 'Complete'