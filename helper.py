from qiskit import *
from qiskit.tools.visualization import plot_histogram

import numpy as np

def show( name ):
    from IPython.display import Image
    display(Image('images/'+name))

def set_output ( program, qubit, bit, type='Z' ):
    
    if type=='X':
        program.h(qubit)
        
    program.measure(qubit,bit)

    
def display_outputs ( program, hist=True ):
    
    job = execute(program,Aer.get_backend('qasm_simulator'))
    results = job.result().get_counts()
    if hist:
        qiskit.tools.visualization.plot_histogram(results)
    for string in results:
        print ('Output is ',string,' with probability',results[string]/1024)