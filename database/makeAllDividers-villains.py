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
    extensions = ["AS1","AS2","AS1S2","CP1","CB1","SGS1","ESV","GGR","RBP","TA","S6","IG","CP2","CB2","SGS2","BT","DFP","DP","FC","GT","HA","FF","PF","XF"]
    extensionsFull=["All-in S1","All-in S2","All-in S1 S2","Core pledge S1","Core Box S1","SG S1","Enter the Spider-Verse","Guardians of the Galaxy Remix","Rise of the Blanck Panther","Tales of Asgard",'Return of the Sinister Six','The Infinity Gauntlet',"Core pledge S2","Core Box S2","SG S2","Blue Team","Days of the Future Past","Deadpool","First Class","Gold Team","The Horsemen of Apocalypse","Fantastic Four","Phoenix Five","X-Force"]
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
                    os.system('./make-dividers-villains.py -l {} -o {} -m {} -e {} >> outDivider'.format(lang,orientation,marker,extensionShort))
                    os.system('mv dividers-villains-{}-{}-{}-{}.pdf {}/{}/{}/{}/'.format(extensionShort,lang,drawFilename,orientation,extension,lang,orientation,drawFilename))

