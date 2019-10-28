Insight Coding Challenge
by Donghwan Kim, 28 Oct 2019

It is my coding challenge of border crossing analysis from Insight. Crossing Border is becoming an emerging social issue. Using the BTS (Bureau of Transportation Statistics) data which is publicily available, it analyzes how many people and vehicles are crossing the U.S. borders.

Using Python3 with three basic modules (sys, csv, and math), the analysis program (Named RunningAverage_MultipleVariables.py) calculates statistics by multiple variables (Date, Border, and Measure) and reports the results with well-organized one (sorted by Date, Value, Border, and Measure) since we might want to know border crossing by a meaningful way by date, by Border, and by Measure where

Date: 03/01/2019, 02/01/2019, 01/01/2019
Border: U.S.-Canadian, U.S.-Mexican
Measure: Pedestrians, Truck Containers Full, Truck Containers Empty, train

and the Value variable is the number of crossing. The main function in the program, among others, is the sorted_indexed function (lines 29 - 59). It is my way with iteration and index to calculate group average (that is, average by Date, Border, and Measure) with observations reduced uniquly and sorted (note that there are more than one observations by the three variables since there are multiple ports of border).

The Python3 script passed your test. I think it is clean and scalable but for a limited time as you mentioned it has lines awkward which need to be improved. Please contact me with dh3kim@gmail.com if you have any problems with the program. 


