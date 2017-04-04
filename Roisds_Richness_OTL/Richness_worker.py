#! /usr/bin/env python
#this script goes through each line, adding family names to each of species under such family and then will calculate:

#how many species in each genus

#Open the file contains the data
InFileName = "superrosids_name_OTL_clean.txt"
InFile = open(InFileName, 'r')

HeaderLine = 'Order, Family, Genus, Species_Count'
HeaderLine1 = 'Order, Family, Genus, Species'

SpeciesRichiFile = "superrosids_Richness_OTL.csv"
NoSpeciesFile = "superrosids_Nospecies_OTL.csv"
NewNameFile = "superrosids_OTL_new.csv"

OutSpecisRich = open(SpeciesRichiFile, 'w')
OutSpecisRich.write(HeaderLine + '\n')
OutNoSpecies = open(NoSpeciesFile, 'w')
OutNoSpecies.write(HeaderLine + '\n')
OutNewName = open(NewNameFile, 'w')
OutNewName.write(HeaderLine1 + '\n')

LineNumber = 0
Species_Count=0
Genus=""

# Loop through each line in the file
for Line in InFile:
	if LineNumber > 0:
		#Remove the line ending character
		Line=Line.strip('\n')
		#parsing the strings of each line
		LineList=Line.split(',')
		Rank = str(LineList[0]) # getting the rank value
		Signal = str(LineList[1]) # getting the rank signal for downstream analyses
		if Signal== "order":
			Order = Rank
		elif Signal == "family":
			Family=Rank
			#print Family
		elif Signal=="genus":
			if Species_Count != 0:
				OutList=[str(Order), str(Family), str(Genus), str(Species_Count)] #output list
				OutSpecisRich.write(",".join(OutList)+"\n")
			else: #output all those genera lables that don't contain any species
				OutList=[str(Order), str(Family), str(Genus), str(Species_Count)]
				OutNoSpecies.write(",".join(OutList)+"\n")
			Genus=Rank
			Species_Count=0
		elif Signal == "species": #counting species
			New_Name = Family + '_' + Rank
			OutList2=[str(Order), str(Family), str(Genus), str(New_Name)]
			OutNewName.write(",".join(OutList2)+"\n")
			Species_Count+=1
	LineNumber = LineNumber + 1

#Output last species information
OutList=[str(Order), str(Family), str(Genus), str(Species_Count)]#output list
OutSpecisRich.write(",".join(OutList)+"\n")

InFile.close()
OutSpecisRich.close()
OutNoSpecies.close()
OutNewName.close()