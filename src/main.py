from weakref import ref
from qiskit import QuantumCircuit, transpile
from qiskit.test.mock.backends import FakeBrooklyn
from qiskit.converters import circuit_to_dag, dag_to_circuit
from qiskit.transpiler import CouplingMap
from qiskit.dagcircuit import DAGCircuit
from qiskit.transpiler import Layout
from qCharta import qCharta
import os
from coupling import couplingmap_brooklyn

inputdir = "..\\benchmarks\\"
outputdir = "..\\mapped\\"

def main():
    # get all qasm files of directory
    files = os.listdir(inputdir)
    files = list(filter(lambda path: path.endswith(".qasm"),files))

    result = do_benchmark(files)

    print("Cost of reference implementation: "+str(result[0]))

def do_benchmark(files, ref_benchmark = False):
    reference_results = []
    own_results = []
    reference_cost = 0
    own_cost = 0
    quantum_circuits = {}

    print("[Step 1: parse qasm files]")
    for filename in files:
        quantum_circuits["filename"]=QuantumCircuit.from_qasm_file(path=inputdir+filename)
    
    if ref_benchmark:
        print("[Step 2: transpile trivial mapping with basic swaps]")
        for name, circuit in quantum_circuits.items():
            transpiled = transpile(circuit, backend=FakeBrooklyn(),routing_method="basic")

            cost = get_circuit_cost(transpiled)
            reference_results.append(cost)
            reference_cost = reference_cost+cost
            
            transpiled.qasm(filename=outputdir+"reference\\"+name)
    else:
        print("[skip Step2]")
    
    print("[Step 3: transpile with qCharta]")
    for name, circuit in quantum_circuits.items():
        # create coupling map
        coupling_map = CouplingMap(couplingmap_brooklyn)

        # create transpiler with coupling map
        transpiler = qCharta(coupling_map,100)
        
        # convert circuit to dag, transpile and convert back
        dag = circuit_to_dag(circuit)
        mapped_dag = transpiler.run(dag)
        mapped_qc = dag_to_circuit(mapped_dag)

        filecontent = mapped_qc.qasm()
        filecontent = filecontent.replace('\n', '\n' + get_layout_description_comment(transpiler.initial_layout, dag) + '\n', 1)

        with open(outputdir+"qCharta\\"+name, "w+") as file:
            file.write(filecontent)
        file.close()

        

    return [reference_cost,reference_results,own_cost,own_results]

# author: Elias Foramitti
def get_circuit_cost(qc: QuantumCircuit) -> int:
    instructions = [i[0] for i in qc]
    cost = 0
    for i, inst in enumerate(instructions):
        if inst.name == 'sx' or inst.name == 'x':
            cost += 1
        elif inst.name == 'cx':
            cost += 10
        elif inst.name == 'swap':
            cost += 30
        elif (inst.name != 'rz' and inst.name != 'measure' and inst.name != 'barrier'):
            print(f"{i}th instruction '{inst.name}' not allowed")
    return cost

# author: Elias Foramitti
def get_layout_description_comment(layout: Layout, dag: DAGCircuit):
    physical_qbits = []
    virtual_bit_mapping = layout.get_virtual_bits()
    # one could directly take layout.get_virtual_bits().values(), 
    # but that would not necessarily preserve the original ordering 
    # of virtual qubits resulting in a wrong layout description
    for qreg in dag.qregs.values():
        for qbit in qreg:
            physical_qbits.append(virtual_bit_mapping[qbit])
    return '// i ' + ' '.join(str(i) for i in physical_qbits)

if __name__=="__main__":
    main()