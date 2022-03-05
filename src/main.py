import os

from qiskit import QuantumCircuit, transpile
from qiskit.test.mock.backends import FakeBrooklyn
from qiskit.converters import circuit_to_dag, dag_to_circuit
from qiskit.transpiler import CouplingMap

from qCharta import qCharta
from coupling import couplingmap_brooklyn
from support_funcs import get_circuit_cost, get_layout_description_comment, check_equivalence

inputdir = "..\\benchmarks\\"
outputdir = "..\\mapped\\"

seed = 100

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
        transpiler = qCharta(coupling_map, seed)
        
        # convert circuit to dag, transpile and convert back
        dag = circuit_to_dag(circuit)
        mapped_dag = transpiler.run(dag)
        mapped_qc = dag_to_circuit(mapped_dag)

        # check if result is equivalent to original ciruit
        if check_equivalence(circuit,mapped_qc):
            print(name +": result = original")
        else:
            print(name +": result is not equivalent")

        filecontent = mapped_qc.qasm()
        filecontent = filecontent.replace('\n', '\n' + get_layout_description_comment(transpiler.initial_layout, dag) + '\n', 1)

        with open(outputdir+"qCharta\\"+name, "w+") as file:
            file.write(filecontent)
        file.close()

    return [reference_cost,reference_results,own_cost,own_results]

if __name__=="__main__":
    main()