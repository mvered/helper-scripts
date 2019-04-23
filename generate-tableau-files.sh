#!/bin/bash
# Creates Tableau files with membership match reports for each partner from template

# author: Michelle Vered <mvered@mtvoices.org>
# created: 3/28/19

# Requirements to use:
# 1) Template Tableau project file, named as test.twb
# 2) Template Tableau project must use data source test.xlsx for membership data
# 3) Data files for individual orgs membership data must be formatted exactly the same as test.xlsx
# 4) Data files must be saved in the same folder as test.xlsx using the naming convention partnername.xlsx

# Instructions:
# 1) Replace partner1name, partner2name, etc. with real partner names.
# Partner names must be written the same as in the excel file names.
# You can list as many partner names as you want. Save and close this file.
# 2) Open a bash shell in the folder your Tableau and data files are saved in and type:
# chmod +x generate-tableau-files.sh
# ./generate-tableau-files.sh
# 3) That's it!

for partner in northernplains #replace with real partner names here
do
	sed "s/testdata\.xlsx/${partner}\.xlsx/" test.twb > ${partner}.twb
	echo "${partner} Tableau file generated"
done
