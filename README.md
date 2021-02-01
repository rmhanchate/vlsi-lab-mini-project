# 8-bit Arithmetic Logic Unit

This project deals with the designing and implementation of an 8 Bit Arithmetic Logic Unit. This arithmetic unit is capable of performing three separate operations namely multiplication, addition and subtraction. The layout for the Arithmetic Unit was cre ated using the MAGIC software. The layout was then tested using the switch level logic simulator IRSIM. 

The designed unit can take in two 8 bit numbers as the input and the output is defined by two pins `sel` and `cin`.

The standard cells that were used in the making of the unit were imported from the vsclib library package. The pharosc technology file was used during the implementation borrowed from Graham Petley s website www.vlsitechnology.org. A scmos parameters file was also obtained. The testing of the design was performed with the assistance of a python script that generates the test vectors, verifies the answer and prints the results, with the failed cases (if any).

![alt text](https://github.com/rmhanchate/vlsi-lab-project/blob/main/alu.png?raw=true)
