import math

#Name: read()
#Purpose: To read input file and process accordingly
#Processing: 1) Read input file name 'dataInput'
#	     2) Read first line of input file and create fixed array with zeroes for carLot and motorcycleLot
#            3) Read next line of input file
#	     4) If 'Enter' is matched, loop through carLot/motorcycleLot array and check for first zero and return the positionIndex
#	     4.1)  set positionIndex to 1
# 	     4.2)  write to file name 'record' in this format : motorcyle/car platenumber timestamp positionIndexInArray
#  	     4.3)  print Accept MotorcycleLot/CarLot positionIndex+1
#            4.4)  If fixed array is filled with ones, print reject
#            5) If 'Exit' is matched, get platenumber and timestamp
#	     5.1)  Open file name 'record', match platenumber with motorcycle/car and get timestamp and positionIndex
#	     5.2)  Base on the positionIndex in 5.1, set fixed motorcycle/car array to 0
#	     5.3)  Calculate Final Time = (exitTime - enterTime) / 3600
#            5.4)  Set FinalTime * 1 for motorcyle and FinalTime * 2 for car
#            5.5)  print in this format : MotorcycleLot/CarLot[positionIndex] price

def read():
	# Read Input File
	file = open('dataInput', 'r')
	lines = file.readlines()

	firstLineFlag = 0
	
	#Loop through Input File
	for line in lines:
		if firstLineFlag == 0 :
			
			#Create Fixed Arrays base on Input File
			carLot = [0] * int(line[0])
			motorcycleLot = [0] * int(line[2])
			firstLineFlag = 1

		#Checking for 'Enter' 
		if 'Enter' in line:
			#Checking for 'motorcycle'
			if 'motorcycle' in line:
				#Open record file
				file1 = open('record', 'a')

				positionIndex = 0

				#Check for zero in array
				if 0 in motorcycleLot:
					for i in motorcycleLot:
						if i == 0 :
							#Set first zero encounter to 1
							motorcycleLot[positionIndex] = 1
							break
						positionIndex = positionIndex + 1
					#Write to record file
					file1.write('motorcycle ' + line.split()[2] + ' ' + line.split()[3] + ' ' + str(positionIndex) + '\n')
					print('Accept ' + 'MotorcycleLot' + str(positionIndex + 1))
				else:
					#If array is all filled with ones (Lots are fully occupied)
					print('Reject')
				file1.close()
			else:
				#Open record file
                                file1 = open('record', 'a')
				positionIndex = 0
				
				#Check for zero in array
				if 0 in carLot:
					for i in carLot:
						if i == 0 :
							#Set first zero encounter to 1
							carLot[positionIndex] = 1
							break
						positionIndex = positionIndex + 1
					#Write to record file
					file1.write('car ' + line.split()[2] + ' ' + line.split()[3] + ' ' + str(positionIndex) + '\n')
					print('Accept ' + 'CarLot' + str(positionIndex + 1))
				else:
					#If array is all filled with ones (Lots are fully occupied)
					print('Reject')
				file1.close()

		#Checking for 'Exit' 
		else:
			array = []
			array.append(line)
			array = line.split()
			
			#Get PlateNumber
			tmpCarPlateNumber = line.split()[1]

			#Open record file
			with open('record', 'r') as read_obj:
				for line in read_obj:
					#Check for PlateNumber in record file
					if tmpCarPlateNumber in line:
						if line.split()[0] == 'motorcycle':
							#Set positionIndex of motorcyclelot array to zero
							motorcycleLot[int(line.split()[3])] = 0

							#Calculate Float Final Time in hours
							finalTime = (float(array[-1]) - float(line.split()[2])) / 3600
							print('MotorcycleLot' + str(int(line.split()[3]) + 1) + ' ' + str(int(math.ceil(finalTime) * 1)))
						else:
							#Set positionIndex of carlot array to zero
							carLot[int(line.split()[3])] = 0

							#Calculate Float Final Time in hours
							finalTime = (float(array[-1]) - float(line.split()[2])) / 3600
							print('CarLot' + str(int(line.split()[3]) + 1) + ' ' + str(int(math.ceil(finalTime) * 2)))

				
					
							
	
			
if __name__ == "__main__":
	open('record', 'w').close()
	read()
