# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 00:45:50 2020

@author: Rahul
"""

import os
import sys
import random

def evaluate(eachline, counter, anticounter):

	a0 = eachline[eachline.find('a0') + 3] 
	a1 = eachline[eachline.find('a1') + 3] 
	a2 = eachline[eachline.find('a2') + 3]
	a3 = eachline[eachline.find('a3') + 3]
	a4 = eachline[eachline.find('a4') + 3]
	a5 = eachline[eachline.find('a5') + 3]
	a6 = eachline[eachline.find('a6') + 3]
	a7 = eachline[eachline.find('a7') + 3]
	b0 = eachline[eachline.find('b0') + 3]
	b1 = eachline[eachline.find('b1') + 3]
	b2 = eachline[eachline.find('b2') + 3]
	b3 = eachline[eachline.find('b3') + 3]
	b4 = eachline[eachline.find('b4') + 3]
	b5 = eachline[eachline.find('b5') + 3]
	b6 = eachline[eachline.find('b6') + 3]
	b7 = eachline[eachline.find('b7') + 3]
	cin = eachline[eachline.find('cin') + 4]
	sel = eachline[eachline.find('sel') + 4]
	out0 = eachline[eachline.find('out0') + 5]
	out1 = eachline[eachline.find('out1') + 5]
	out2 = eachline[eachline.find('out2') + 5]
	out3 = eachline[eachline.find('out3') + 5]
	out4 = eachline[eachline.find('out4') + 5]
	out5 = eachline[eachline.find('out5') + 5]
	out6 = eachline[eachline.find('out6') + 5]
	out7 = eachline[eachline.find('out7') + 5]
	out8 = eachline[eachline.find('out8') + 5]
	out9 = eachline[eachline.find('out9') + 5]
	out10 = eachline[eachline.find('out10') + 6]
	out11 = eachline[eachline.find('out11') + 6]
	out12 = eachline[eachline.find('out12') + 6]
	out13 = eachline[eachline.find('out13') + 6]
	out14 = eachline[eachline.find('out14') + 6]
	out15 = eachline[eachline.find('out15') + 6]

	a = int(a7 + a6 + a5 + a4 + a3 + a2 + a1 + a0, 2)
	b = int(b7 + b6 + b5 + b4 + b3 + b2 + b1 + b0, 2)
	
	if (out15 == 'X' or out14 == 'X' or out13 == 'X' or out12 == 'X' or out11 == 'X' or out10 == 'X' or out9 == 'X' or out8 == 'X' or out7 == 'X' or out6 == 'X' or out5 == 'X' or out4 == 'X' or out3 == 'X' or out2 == 'X' or out1 == 'X' or out0 == 'X'):
		print (" Don't Cares present")
		print(out15 + out14 + out13 + out12 + out11 + out10 + out9 + out8 + out7 + out6 + out5 + out4 + out3 + out2 + out1 + out0)
		sys.exit()

	else:

		if(sel=='0'):

			result = int(out15 + out14 + out13 + out12 + out11 + out10 + out9 + out8 + out7 + out6 + out5 + out4 + out3 + out2 + out1 + out0,2)
			product = int(a*b)

			if(result!=product):

				print("******************************************")
				print("Error")
				print(str(a) + "*" + str(b) + " failed")
				print("Obtained " + out15 + out14 + out13 + out12 + out11 + out10 + out9 + out8 + out7 + out6 + out5 + out4 + out3 + out2 + out1 + out0 + " = " + str(result))
				print("Expected " + bin(product)[2:].zfill(16) + " = " + str(product))
				print("******************************************")
				anticounter = anticounter + 1
				#sys.exit()

			else:

				print("Success " +  str(a) + "*" + str(b) + "=" + str(product))
				counter = counter + 1

		else:

			if(cin=='0'):

				result = int(out8 + out7 + out6 + out5 + out4 + out3 + out2 + out1 + out0, 2)
				add = int(a + b)

				if(result!=add):
					print("******************************************")
					print("Error")
					print(str(a) + " + " + str(b) + " failed")
					print("Obtained " + out15 + out14 + out13 + out12 + out11 + out10 + out9 + out8 + out7 + out6 + out5 + out4 + out3 + out2 + out1 + out0 + " = " + str(result))
					print("Expected " + bin(add)[2:].zfill(16) + " = " + str(add))
					print("******************************************")
					anticounter = anticounter + 1
					#sys.exit()

				else:
					print("Success " +  str(a) + " + " + str(b) + "=" + str(add))
					counter = counter + 1

			else:

				result = int(out7 + out6 + out5 + out4 + out3 + out2 + out1 + out0, 2)

				if(out8 == '0'):
					result = result - (1<<8)

				sub = int(a - b)

				if(result!=sub):

					print("******************************************")
					print("Error")
					print(str(a) + " - " + str(b) + " failed")
					print('Obtained ' + out15 + out14 + out13 + out12 + out11 + out10 + out9 + out8 + out7 + out6 + out5 + out4 + out3 + out2 + out1 + out0 + " = " + str(result))
					print("Expected " + bin(sub)[2:].zfill(16) + " = " + str(sub))
					print("******************************************")
					anticounter = anticounter + 1
					#sys.exit()

				else:

					print("Success " +  str(a) + " - " + str(b) + "=" + str(sub))
					counter = counter + 1

	return counter, anticounter

def main():

	if(len(sys.argv)==1):
		print("Error. Please provide the .sim file as command line argument")
	sim_file = sys.argv[1]

	cmdfile = "test.cmd"
	prmfile = "scmos100.prm"
	logfile = "output.log"
	input_vector_1 = "a7 a6 a5 a4 a3 a2 a1 a0"
	input_vector_2 = "b7 b6 b5 b4 b3 b2 b1 b0"
	select_vector = "sel cin"
	product_vector = "p15 p14 p13 p12 p11 p10 p9 p8 p7 p6 p5 p4 p3 p2 p1 p0"
	sum_vector = "s7 s6 s5 s4 s3 s2 s1 s0"
	out = "out15 out14 out13 out12 out11 out10 out9 out8 out7 out6 out5 out4 out3 out2 out1 out0"

	totalnumofvectors = 2**16
	global counter
	counter = 0
	global anticounter
	anticounter = 0
	maxsteppower = 0
	rand = 0

	with open (cmdfile , "w") as file :

		file.write("powlogfile powerlog.log\n")
		file.write("vsupply 5\n")
		file.write("h Vdd\n")
		file.write("l Gnd\n")
		file.write("powtrace Vdd Gnd " + out + " " + select_vector + " " + product_vector + " " + sum_vector + " " + input_vector_1 + " " + input_vector_2 + "\n")
		file.write("logfile " + logfile + " \n")
		file.write("stepsize 34.5\n")
		file.write("w " + out + " " + select_vector + " " + input_vector_1 + " " + input_vector_2 + "\n")
		file.write("vector in " + select_vector + " " + input_vector_1 + " " + input_vector_2 + "\n")
		file.write("powstep \n")
		file.write("set vlist {")

		for j in range(0,4,1):

			for i in range(0,totalnumofvectors,1):

				if (random.randint(1, 256) < 3):

					file.write(str(bin(j)[2:].zfill(2)) + str(bin(i)[2:].zfill(16)) + " ")

		file.write("}\n")
		file.write("foreach vec $vlist {setvector in $vec ; s}\n")
		file.write("powlogfile \n")
		file.write("sumcap \n")
		file.write("logfile \n")
		file.close()

	os.system("irsim " + prmfile + " " + sim_file + " -" + cmdfile + " &")
	input("Press any key after irsim is done evaluating.")

	eachline = " "

	with open (logfile , "r") as fp :

		print ("Log file loaded. Evaluating...")
		line = fp.readline ()

		while line :

			if ('time' in line):

				counter, anticounter = evaluate (eachline, counter, anticounter)
				line = fp.readline ()
				eachline = " "

			elif ('step =' in line) :

				steppower = line [ line.find ('step = ') + 7 : line.find ('step = ') + 14]
				print ("Step power = " + steppower)
				steppower = float(steppower)

				if (steppower > maxsteppower):

					maxsteppower = steppower

				line = fp.readline ()
				eachline = " "

			else :

				eachline = eachline + line
				line = fp.readline ()

		fp.close ()

	print("Accuracy " + str(counter/((counter + anticounter))*100) + "%")
	print("Maximum Dynamic Power Consumed = " + str (maxsteppower) + "mW")
	print("Power report : \n" + eachline)

if __name__ == '__main__':
	main()
	
