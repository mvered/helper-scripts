#!/bin/bash
# Creates new Tableau files from template which use new data sources

# author: Michelle Vered 
# created: 3/28/19

# Requirements to use:
# 1) Template Tableau project file and data source named as template.twb and template.xlsx
# 2) Additional data sources which have the same structure as template.xlsx

for d in newdatasource1 newdatasource2 #replace with names of new data sources here
do
	sed "s/template\.xlsx/${d}\.xlsx/" template.twb > ${d}.twb
	echo "${d} Tableau file generated"
done
