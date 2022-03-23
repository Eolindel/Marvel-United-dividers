#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script to make dividers for Marvel United Season 1 and 2
"""

# Importation des librairies

import csv
import os
import argparse
# Definition des fonctions





# Programme principal
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    langs = ['FR','UK']
    orientations = ['vertical','horizontal']
    markers = [True,False]
    #markers = [False]
    extensions = ["AS1S2"]
    extensionsFull=["Extra"]
    for i,extensionShort in enumerate(extensions):
        extension = extensionsFull[i].replace(' ','-')
        if not os.path.exists('./'+extension):
            os.mkdir(extension)
        for lang in langs:
            if not os.path.exists('./{}/{}'.format(extension,lang)):
                os.mkdir('{}/{}'.format(extension,lang))
            for orientation in orientations:
                if not os.path.exists('./{}/{}/{}'.format(extension,lang,orientation)):
                    os.mkdir('{}/{}/{}'.format(extension,lang,orientation))
                for marker in markers:
                    if marker == True:
                        drawFilename = 'Lines'
                    else:
                        drawFilename = 'Ticks'
                    if not os.path.exists('./{}/{}/{}/{}'.format(extension,lang,orientation,drawFilename)):
                        os.mkdir('{}/{}/{}/{}'.format(extension,lang,orientation,drawFilename))
                    os.system('./make-dividers-extra.py -l {} -o {} -m {} -e {} >> outDivider'.format(lang,orientation,marker,extensionShort))
                    os.system('mv dividers-extra-{}-{}-{}-{}.pdf {}/{}/{}/{}/'.format(extensionShort,lang,drawFilename,orientation,extension,lang,orientation,drawFilename))

