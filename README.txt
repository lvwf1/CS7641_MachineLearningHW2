This file contains the instructions for how to run the code for Assignment 2

Important Notes
1) This project is run under Python Environment in PyCharm IDE Professional
2) This project uses a modified version of ABAGAIL, located in the ABAGAIL sub-folder
3) The folders NNOUTPUT, CONTPEAKS, FLIPFLOP and TSP must be created in the same folder as the Jython code before running it.
4) The files SeasonsStats_test.csv, SeasonsStats_trg.csv and SeasonsStats_val.csv must be in the same folder as the NN*.py files
5) To run NN*.py, you must follow these steps:
1. Download ABAGAIL folder from https://github.com/pushkar/ABAGAIL
2. Installed jdk, jre, ant, jython and set environment variables for jdk, jre and ant
3. Build the path in Pycharm Console with "cd ABAGAIL" and "ant" command
4. Set the project interpreter as jython, and add the #YOUR_PROJECT_PATH#\ABAGAIL\ABAGAIL.jar as the path for jython intepretor
6) To run the plot.py and plot2.py, switch the project intepretor as Python 3.6 with numpy, pandas, matplotlib and scipy installed
7) Code in this assignment and this README file were modified from those written by Jonathan Tay (https://github.com/JonathanTay)

Report:
1) wlyu6-analysis.pdf - Assignment 2 report

Code Files: 
1) NN0.py - Code for Backpropagation training of neural network
2) NN1.py - Code for Randomized Hill Climbing training of neural network
3) NN2.py - Code for Simulated Annleaing training of neural network
4) NN3.py - Code for Genetic Algorithm training of neural network
5) continuouspeaks.py - Code to use Randomised Optimisation to solve the Continuous Peaks problem
5) flip flop.py - Code to use Randomised Optimisation to solve the Flip Flop problem
6) tsp.py - Code to use Randomised Optimisation to solve the Traveling Salesman Problem
7) shuffle.py - Code to preprocess the dataset SeasonsStats.csv to train, test, validation set
8) plot.py - Code for plotting all the randomized optimization figures
9) plot2.py - Code for plotting all the randomized optimization problems figures

There are also a number of folders
1) Datasets - contains the code to generate the datasets for this assignment from the original files from the UCI ML Repository
2) NNOUTPUT - output folder for the Neural Network experiments
3) CONTPEAKS - output folder for the Continuous Peaks experiments
4) FLIPFLOP - output folder for the Flip Flop experiments
5) TSP - output folder for the Traveling Salesman Problem experiments
6) PLOT - folder with all analysis plots
7) ABAGAIL - folder with source, ant build file, and jar for ABAGAIL

Data Files
1) SeasonsStats_test_test.csv - The test set
2) SeasonsStats_test_trg.csv - The training set
3) SeasonsStats_test_val.csv - The validation set

The assignment code is written in Python 3.6.3. Library dependencies are: 
numpy: 1.15.2
pandas: 0.23.4
matplotlib: 3.0.0
scipy: 1.1.0

Java code was built with ant 1.10.2 on java 1.8.0_152. 
The code files in the code files section were written in Jython 2.7.0. 

Within the output folders, the data files are csv files (with .txt extensions). The file names correspond to experiments:
<ALGORITHM><PARAMETERS>_LOG.txt
*in the case of NN, the number of nodes per layer was added at the end of the filename.