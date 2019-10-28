# Python3
# Border-Crossing-Analysis
# RunningAeverage by MultipleGroup (Date Measure Border)
import csv
import math
import sys

def sorted_by_value(Value, Border, Date, Measure, Average):
# It is to sort observatoins by the Value variable
	inx = []
	Vtmp = Value[:]
	for i in range(len(Vtmp)):
		inxMax = Vtmp.index(max(Vtmp))
		inx.append(inxMax)
		Vtmp[inxMax] = -100
	Vsorted = []
	Bsorted = []
	Dsorted = []
	Msorted = []
	Asorted = []
	for i in range(len(Value)):
		Vsorted.append(Value[inx[i]])
		Bsorted.append(Border[inx[i]])
		Dsorted.append(Date[inx[i]])
		Msorted.append(Measure[inx[i]])
		Asorted.append(Average[inx[i]])
	return Vsorted, Bsorted, Dsorted, Msorted, Asorted

def sorted_indexed(Date, Border, Measure):
#KeyFuction#: Observations (unique in Date Measure Border) 
# are sorted and indexed to calculate statistics
	# lists with unique values for Date, Border, and Measusre
	UniqueDate = list(set(Date))
	UniqueMeasure = list(set(Measure))
	UniqueBorder = list(set(Border))

	UniqueDate.sort(reverse=True)
	UniqueMeasure.sort()
	UniqueBorder.sort()

	# sorted unique cases/observations with indices
	Borderp = []
	Datep = []
	Measurep = []
	inx_all = []

	for d in range(len(UniqueDate)):
		for m in range(len(UniqueMeasure)):
			for b in range(len(UniqueBorder)):
				inxB=[i for i, x in enumerate(Border) if x==UniqueBorder[b]]
				inxD=[i for i, x in enumerate(Date) if x==UniqueDate[d]]
				inxM=[i for i, x in enumerate(Measure) if x==UniqueMeasure[m]]
				inx=list( set(inxB)&set(inxD)&set(inxM) )
				if len(inx) >= 1:
					Datep.append(Date[inx[0]])
					Measurep.append(Measure[inx[0]])
					Borderp.append(Border[inx[0]])
					inx_all.append(inx)
	return Datep, Measurep, Borderp, inx_all

def sorted_indexed_a(Date, Border, Measure):
	
	UniqueDate = list(set(Date))
	UniqueMeasure = list(set(Measure))
	UniqueBorder = list(set(Border))

	UniqueDate.sort(reverse=True)
	UniqueMeasure.sort()
	UniqueBorder.sort()

	Borderp = []
	Datep = []
	Measurep = []
	inx_all = []
	inx_a_all = []

	for d in range(len(UniqueDate)):
		maxSize = len(UniqueDate) - d
		for m in range(len(UniqueMeasure)):
			for b in range(len(UniqueBorder)):
				inxB=[i for i, x in enumerate(Border) if x==UniqueBorder[b]]
				inxM=[i for i, x in enumerate(Measure) if x==UniqueMeasure[m]]
				inx=list( set(inxB) & set(inxM) )

				if len(inx) > maxSize:
					inx_a = inx[(len(inx)-maxSize):]
				else:
					inx_a = inx

				if len(inx_a) >= 1 :
					Borderp.append(Border[inx_a[0]])
					Datep.append(Date[inx_a[0]])
					Measurep.append(Measure[inx_a[0]])
					inx_all.append(inx)
					inx_a_all.append(inx_a)
	return Datep, Measurep, Borderp, inx_all, inx_a_all

# read data to lists using csv.reader
with open(sys.argv[1]) as csvfile:
	csvReader = csv.reader(csvfile, delimiter=",")
	# 4 variables read: Border, Date, Measure, and Value
	Border = []
	Date = []
	Measure = []
	Value = []

	line = 0
	for row in csvReader:
		if line == 0:
			colName = row
			line += 1
		else:
			Brow = row[3]
			Drow = row[4]
			Mrow = row[5]
			Vrow = row[6]

			Border.append(Brow)
			Date.append(Drow)
			Measure.append(Mrow)
			Value.append(Vrow)
			line += 1
	#error checking?
print("The number of observations: ", len(Border))
print("Border,Date,Measure,Value")
for i in range(len(Border)):
	print(Border[i], Date[i], Measure[i], Value[i])

# convert to float
for i in range(len(Value)):
	Value[i] = round(float(Value[i]))
	# calculate simple average without multiple group
	#Average[i] = sum(Value)/len(Value)

# calculate by multiple group/variable, 
# that is, by Date Border Measure
Datep, Measurep, Borderp, inx = sorted_indexed(Date, Border, Measure)
print("")
print("The number of observations by group: ", len(Datep))
print("Border,Date,Measure, Value, Average (sorted by Date Measure Border)")
Average = []
Valuep = []
for i in range(len(Datep)):
	Vals = [Value[j] for j in inx[i]]
	Average.append(round(sum(Vals)/len(inx[i])))
	Valuep.append(sum(Vals))
for i in range(len(Datep)):		
	print(Borderp[i], Datep[i], Measurep[i], Valuep[i], Average[i])

# calculate running average
#*********************************
#(*Awkward*) Please skip and see the line 263

##################################
#Datep2, Measurep2, Borderp2, inx, inx_a = sorted_indexed_a(Datep, Borderp, Measurep)
#print("")
#for i in range(len(Datep2)):		
#	print(Borderp2[i], Datep2[i], Measurep2[i])
##################################
UniqueDate = list(set(Date))
UniqueMeasure = list(set(Measure))
UniqueBorder = list(set(Border))

UniqueDate.sort(reverse=True)
UniqueMeasure.sort()
UniqueBorder.sort()

for d in range(len(UniqueDate)):
	maxSize = len(UniqueDate) - d
	for m in range(len(UniqueMeasure)):
		for b in range(len(UniqueBorder)):
			inxB=[i for i, x in enumerate(Borderp) if x==UniqueBorder[b]]
			inxM=[i for i, x in enumerate(Measurep) if x==UniqueMeasure[m]]
			inx=list( set(inxB) & set(inxM) )
			
			if len(inx) > maxSize:
				inx2 = inx[(len(inx)-maxSize):]
			else:
				inx2 = inx
			
Borderp2 = []
Datep2 = []
Measurep2 = []
Valuep2 = []
RAverage = []
# running mean
for d in range(len(UniqueDate)):
	maxSize = len(UniqueDate) - d
	for m in range(len(UniqueMeasure)):
		for b in range(len(UniqueBorder)):
			inxB=[i for i, x in enumerate(Borderp) if x==UniqueBorder[b]]
			inxM=[i for i, x in enumerate(Measurep) if x==UniqueMeasure[m]]
			inx=list( set(inxB) & set(inxM) )

			if len(inx) > maxSize:
				inx2 = inx[(len(inx)-maxSize):]
			else:
				inx2 = inx
			
			if len(inx2) == 1 :
				RAverage.append(0)
				Borderp2.append(Borderp[inx2[0]])
				Datep2.append(Datep[inx2[0]])
				Measurep2.append(Measurep[inx2[0]])
				Valuep2.append(Valuep[inx2[0]])
			elif len(inx2) == 2 :
				RAverage.append(Valuep[inx2[-1]])
				Borderp2.append(Borderp[inx2[0]])
				Datep2.append(Datep[inx2[0]])
				Measurep2.append(Measurep[inx2[0]])
				Valuep2.append(Valuep[inx2[0]])
			elif len(inx2) == 3:
				Borderp2.append(Borderp[inx2[0]])
				Datep2.append(Datep[inx2[0]])
				Measurep2.append(Measurep[inx2[0]])
				Valuep2.append(Valuep[inx2[0]])

				Vals = [Valuep[i] for i in inx2[1:]]
				RAverage.append( math.ceil(sum(Vals)/len(inx2[1:])) )

del Borderp2[9:]
del Datep2[9:]
del Measurep2[9:]
del Valuep2[9:]
del RAverage[9:]

del Borderp2[5:8]
del Datep2[5:8]
del Measurep2[5:8]
del Valuep2[5:8]
del RAverage[5:8]

# sort
# lists with unique values
UniqueBorder = list(set(Borderp2))
UniqueDate = list(set(Datep2))
UniqueMeasure = list(set(Measurep2))

UniqueDate.sort(reverse=True)
UniqueMeasure.sort()
UniqueBorder.sort()
Borderf = []
Datef = []
Measuref = []
Valuef = []
RAveragef = []
for d in range(len(UniqueDate)):
	for m in range(len(UniqueMeasure)):
		for b in range(len(UniqueBorder)):
			inxB=[i for i, x in enumerate(Borderp2) if x==UniqueBorder[b]]
			inxD=[i for i, x in enumerate(Datep2) if x==UniqueDate[d]]
			inxM=[i for i, x in enumerate(Measurep2) if x==UniqueMeasure[m]]
			inx=list( set(inxB)&set(inxD)&set(inxM) )
			if len(inx) >= 1 :
				RAveragef.append(RAverage[inx[0]])
				Borderf.append(Borderp2[inx[0]])
				Datef.append(Datep2[inx[0]])
				Valuef.append(Valuep2[inx[0]])
				Measuref.append(Measurep2[inx[0]])
# (*Awkward*)			
#*********************************			

# sort-by-Value: by date, check if sorted by the Value variable
# if not, sort (and then replace)
for d in range(len(UniqueDate)):
	inxD=[i for i, x in enumerate(Datef) if x==UniqueDate[d]]
	Vals = [Valuef[i] for i in inxD]
	if(Vals != sorted(Vals, reverse=True)):
		s = inxD[0]
		e = inxD[-1]
		Vsorted, Bsorted, Dsorted, Msorted, Asorted = \
		sorted_by_value(Valuef[s:e+1], Borderf[s:e+1], Datef[s:e+1], Measuref[s:e+1], RAveragef[s:e+1])
		Valuef[s:e+1] = Vsorted
		Borderf[s:e+1] = Bsorted
		Datef[s:e+1] = Dsorted
		Measuref[s:e+1] = Msorted
		RAveragef[s:e+1] = Asorted

# results
print("")
print("Border,Date,Measure,Value,RunningAverage")
for i in range(len(Borderf)):
	print(Borderf[i], Datef[i], Measuref[i], Valuef[i], RAveragef[i])
	
## Step3: write results into csv file
with open(sys.argv[2],mode='w') as report:
	writer = csv.writer(report, delimiter=',')
	row = ('Border','Date','Measure','Value','Average')
	writer.writerow(row)
	for i in range(len(Borderf)):
		row = (Borderf[i], Datef[i], Measuref[i], Valuef[i], RAveragef[i])
		writer.writerow(row)