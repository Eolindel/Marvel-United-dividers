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
    with open('Extra-S1-S2.csv', newline='') as f:
        parser = argparse.ArgumentParser()
        parser.add_argument("-l", "--lang", type=str, default = 'UK', help="possible values : FR or UK")
        parser.add_argument("-o", "--orientation", type=str, default = 'vertical',help="possible values : horizontal or vertical")
        parser.add_argument("-m", "--markers", type=str, default = 'True', help="Draw Lines (True) or Ticks (False)")
        parser.add_argument("-e", "--extensions", type=str, default = 'AS1S2', help="""Which extensions : 
AS1	All-in S1
AS2	All-in S2
AS1S2	All-in S1 S2

CP1     Core pledge S1
CB1	Core Box S1
SGS1	SG S1
ESV	Enter the Spider-Verse
GGR	Guardians of the Galaxy Remix
RBP	Rise of the Blanck Panther
TA	Tales of Asgard
S6      Return of the Sinister Six
IG      The Infinity Gauntlet


CP2     Core pledge S2
CB2	Core Box S2
SGS2	SG S2
BT	Blue Team
DFP	Days of the Future Past
DP	Deadpool
FC	First Class
GT	Gold Team
HA	The Horsemen of Apocalypse
FF	Fantastic Four
PF	Phoenix Five
XF	X-Force
""")
        args = parser.parse_args()

        if args.extensions == 'AS1S2':
            extensions = ['All-in S1','SG S1','Core Box S1','Tales of Asgard','Rise of the Blanck Panther','Guardians of the Galaxy Remix','Enter the Spider-Verse','First Class','The Horsemen of Apocalypse','Gold Team','Blue Team','Core Box S2','SG S2','Deadpool','X-Force','Fantastic Four','Phoenix Five','Days of the Future Past','All-in S2','Return of the Sinister Six','The Infinity Gauntlet','Extra']
        elif args.extensions =='AS1':
            extensions = ['All-in S1','SG S1','Core Box S1','Tales of Asgard','Rise of the Blanck Panther','Guardians of the Galaxy Remix','Enter the Spider-Verse','Return of the Sinister Six','The Infinity Gauntlet']
        elif args.extensions == 'AS2':
            extensions = ['First Class','The Horsemen of Apocalypse','Gold Team','Blue Team','Core Box S2','SG S2','Deadpool','X-Force','Fantastic Four','Phoenix Five','Days of the Future Past','All-in S2']
        elif args.extensions =='CP1':
            extensions = ['SG S1','Core Box S1']
        elif args.extensions == 'CP2':
            extensions = ['Core Box S2','SG S2']
        else:
            shortExtensions = ["CB1","SGS1","ESV","GGR","RBP","TA","S6","IG","CB2","SGS2","BT","DFP","DP","FC","GT","HA","FF","PF","XF"]
            longExtensions = ["Core Box S1","SG S1","Enter the Spider-Verse","Guardians of the Galaxy Remix","Rise of the Blanck Panther","Tales of Asgard",'Return of the Sinister Six','The Infinity Gauntlet',"Core Box S2","SG S2","Blue Team","Days of the Future Past","Deadpool","First Class","Gold Team","The Horsemen of Apocalypse","Fantastic Four","Phoenix Five","X-Force"]
            extensions = [longExtensions[shortExtensions.index(args.extensions)]]


        print(extensions)
        #language = 'FR'
        #language = 'UK'
        language = args.lang
        #orientation = 'vertical'
        #orientation = 'horizontal'
        orientation = args.orientation


        #draw contour of dividers
        #drawLines = False
        #drawLines = True
        drawLines = args.markers 

        #filename
        if drawLines == 'True':
            drawFilename = 'Lines'
        else:
            drawFilename = 'Ticks'
        outFile = 'dividers-extra-{}-{}-{}-{}.tex'.format(args.extensions,language,drawFilename,orientation)

        if orientation == 'vertical':
            cardsRow = 2
            cardsCol = 4
            #cards dimension in cm
            cardsWidth = 6.35
            cardsHeight = 9.5
        else:
            cardsRow=4
            cardsCol=2
            #cards dimension in cm
            cardsWidth = 8.8
            cardsHeight = 7.05


        headers = next(f) 
        reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        out = open(outFile,'w')
        #printing the header of the xelatex file
        if orientation == 'vertical':
            out.write(r"""\documentclass[twoside,a4paper,12pt,landscape]{article}
\usepackage[a4paper,twoside,top=10mm,bottom=5mm,inner=10mm,outer=10mm]{geometry}
""")
        else:
            out.write(r"""\documentclass[twoside,a4paper,12pt]{article}
\usepackage[a4paper,twoside,top=5mm,bottom=5mm,inner=5mm,outer=5mm]{geometry}
""")
        out.write(r"""\usepackage{tikz}
\usepackage{amssymb}
\date{}
\pagestyle{empty}
\usepackage{fontspec}
\setmainfont{OrgovanBrush}
\newfontfamily\myfont{Interstate Condensed}
    \newcommand{\move}{\raisebox{-2pt}{\includegraphics[height=12pt]{move.pdf}}}
    \newcommand{\heroic}{\raisebox{-2pt}{\includegraphics[height=12pt]{heroic.pdf}}}
    \newcommand{\attack}{\raisebox{-2pt}{\includegraphics[height=12pt]{hit.pdf}}}
    \newcommand{\wild}{\raisebox{-2pt}{\includegraphics[height=12pt]{wildcard.pdf}}}
    \newcommand{\thug}{\raisebox{-2pt}{\includegraphics[height=12pt]{thug.pdf}}}
    \newcommand{\threat}{\raisebox{-2pt}{\includegraphics[height=12pt]{threat.pdf}}}
    \newcommand{\civilians}{\raisebox{-2pt}{\includegraphics[height=12pt]{civilian.pdf}}}
    \newcommand{\crisis}{\raisebox{-2pt}{\includegraphics[height=12pt]{crisis.pdf}}}
    \newcommand{\bam}{\raisebox{-2pt}{\includegraphics[height=16pt]{bam.pdf}}}
\begin{document}

\begin{center}""")
        i=0
        #for row in reader:
        #     print(row)
        for row in reader:
            if row[2] in extensions:
                #print(i)
                #print(row)
                #printing each block of eight cards
                if i%8 == 0:
                    out.write(r"""\begin{tikzpicture}[x=1cm,y=1cm,every node/.style={inner sep=0,outer sep=0}]
\coordinate     (cardsWidth) at (6.35,0);
\coordinate     (cardsHeight) at (0,9.5);
""")

                        
                    if drawLines == 'True':
                        for k in range(cardsRow+1):
                            out.write('\\draw[line width=0.01mm] (-0.,{:.2f})--({:.2f},{:.2f});\n'.format(-k*cardsHeight,cardsWidth*cardsCol,-k*cardsHeight))
                        for k in range(cardsCol+1):
                            out.write('\\draw[line width=0.01mm] ({:.2f},0)--({:.2f},{:.2f});\n'.format(k*cardsWidth,k*cardsWidth,-cardsRow*cardsHeight))
                    else:
                        for k in range(cardsRow+1):
                            out.write('\\draw[line width=0.01mm] (-0.,{:.2f})--(-0.2,{:.2f});\n'.format(-k*cardsHeight,-k*cardsHeight))
                            out.write('\\draw[line width=0.01mm] ({:.2f},{:.2f})--({:.2f},{:.2f});\n'.format(cardsCol*cardsWidth,-k*cardsHeight,cardsCol*cardsWidth+0.2,-k*cardsHeight))
                        for k in range(cardsCol+1):
                            out.write('\\draw[line width=0.01mm] ({:.2f},0)--({:.2f},0.2);\n'.format(k*cardsWidth,k*cardsWidth))
                            out.write('\\draw[line width=0.01mm] ({:.2f},{:.2f})--({:.2f},{:.2f});\n'.format(k*cardsWidth,-cardsHeight*cardsRow,k*cardsWidth,-cardsHeight*cardsRow-0.2))

                #printing data for each villain
                out.write('\\begin{{scope}}[shift={{({:.2f},{:.2f})}}]'.format(0.+float(i%cardsCol * cardsWidth),0.-float((i%8)//cardsCol*cardsHeight)))
                #if orientation == 'vertical':
                #    out.write('\\node[anchor=north west] at (0,0) {{\includegraphics[height=9.5cm]{{unique-blank-test.pdf}}}};'.format()+'\n')
                #else:
                #    out.write('\\node[anchor=north west] at (0,0) {{\includegraphics[height=6.85cm]{{unique-blank-test-horizontal.pdf}}}};'.format()+'\n')
                #villain name
                row[0] = row[0].replace('(1st Class)','{\\tiny(1st Class)}')
                row[0] = row[0].replace('(Phoenix Five)','{\\tiny(Phoenix Five)}')
                row[0] = row[0].replace('Horsemen of the Apocalypse','{\\scriptsize Horsemen of the Apocalypse}')
                row[0] = row[0].replace('Scarlet Witch/Quicksilver','{\\small Scarlet Witch/Quicksilver}')
                out.write('\\node[anchor=text] at (0.25,-0.48) {{ {}  }};'.format(row[0])+'\n')

                if orientation !='vertical':
                    out.write('\\begin{scope}[shift={(2.45,0)}]')

                ##attack
                #if row[9]!='':
                #    out.write('\\node[anchor=base east] at (4.55,-0.24) {{\\tiny \\textcolor{{gray}}{{ {} }} }};'.format(row[9])+'\n')
                #out.write('\\node[anchor=base east] at (4.1,-0.24) {{\\tiny {} }};'.format(row[5])+'\n')
                ##move
                #if row[7]!='':
                #    out.write('\\node[anchor=base east] at (4.55,-0.55) {{\\tiny \\textcolor{{gray}}{{ {} }} }};'.format(row[7])+'\n')
                #out.write('\\node[anchor=base east] at (4.1,-0.55) {{\\tiny {} }};'.format(row[3])+'\n')
                ##heroic
                #if row[8]!='':
                #    out.write('\\node[anchor=base east] at (5.5,-0.24) {{\\tiny \\textcolor{{gray}}{{ {} }} }};'.format(row[8])+'\n')
                #out.write('\\node[anchor=base east] at (5.15,-0.24) {{\\tiny {} }};'.format(row[4])+'\n')
                ##wild
                #if row[10]!='':
                #    out.write('\\node[anchor=base east] at (5.5,-0.55) {{\\tiny \\textcolor{{gray}}{{ {} }} }};'.format(row[10])+'\n')
                #out.write('\\node[anchor=base east] at (5.15,-0.55) {{\\tiny {} }};'.format(row[6])+'\n')
                
                #Season
                out.write('\\node[anchor=base east] at (6.2,-0.29) {{\\scriptsize {} }};'.format(row[1])+'\n')
                
                
                if orientation !='vertical':
                    out.write('\\end{scope}')

                ##playstyle
                #if language=='UK':
                #    playstyle = row[12]
                #else:
                #    playstyle = row[11]
                #playstyle = playstyle.replace('[thug]','\\thug{}')
                #playstyle = playstyle.replace('[civilians]','\\civilians{}')
                #playstyle = playstyle.replace('[heroic]','\\heroic{}')
                #playstyle = playstyle.replace('[move]','\\move{}')
                #playstyle = playstyle.replace('[attack]','\\attack{}')
                #playstyle = playstyle.replace('[wild]','\\wild{}')
                #playstyle = playstyle.replace('[threat]','\\threat{}')
                #playstyle = playstyle.replace('[crisis]','\\crisis{}')
                #playstyle = playstyle.replace('[bam]','\\bam{}')
                #playstyle = playstyle.replace('$','\\newline ')
                #out.write('\\node[anchor=text,align=left,text width=5.7cm] at (0.5,-2) {{\\myfont \\small {}}};'.format(playstyle)+'\n')
                #box
                #out.write('\\node[anchor=base west] at (0.25,-1) {{\\scriptsize {} }};'.format(row[2])+'\n')
                out.write('\\end{scope} \n\n')



                
                #ending the block of eight cards
                if i%8 == 7:
                    out.write(r"""\end{tikzpicture}\newpage""")
                i+=1
        if i%8!=0:
            out.write(r"""\end{tikzpicture}\newpage""")

        out.write(r"""\end{center}\end{document}""")
        out.close()
        os.system('xelatex {}'.format(outFile))

