from qiskit import QuantumCircuit, transpile
from qiskit.test.mock.backends import FakeBrooklyn
from qiskit.converters import circuit_to_dag
from qiskit.transpiler import CouplingMap, PassManager

import os
from qCharta import qCharta
from sabre import Sabre
from coupling import couplingmap_brooklyn, coupling
from support_funcs import get_circuit_cost, get_layout_description_comment, check_equivalence

inputdir = "..\\benchmarks\\"
outputdir = "..\\mapped\\"
coupling_map = CouplingMap(coupling)
seed = 100

def main():
    # get all qasm files of directory
    files = os.listdir(inputdir)
    files = list(filter(lambda path: path.endswith(".qasm"),files))

    quantum_circuits = {}
    print("Parsing .qasm files")
    for filename in files:
        quantum_circuits[filename]=QuantumCircuit.from_qasm_file(path=inputdir+filename)

    mean = 0

    for i in range(100):
        result = do_benchmark(quantum_circuits)

        #print("Cost of reference implementation: "+str(result[0]))
        #print("Cost of own implementation: "+str(result[2]))
        print(result[2])
        mean = mean + result[2]
    
    print(mean/100)

def do_benchmark(quantum_circuits, ref_benchmark = False, check_eq = False):
    reference_results = []
    own_results = []
    reference_cost = 0
    own_cost = 0

    if ref_benchmark:
        print("[Step 2: transpile trivial mapping with basic swaps]")
        for name, circuit in quantum_circuits.items():
            print("---"+name)
            transpiled = transpile(circuit, backend=FakeBrooklyn(),routing_method="basic")

            cost = get_circuit_cost(transpiled)
            reference_results.append(cost)
            reference_cost = reference_cost+cost

            print("cost: "+str(cost))
            
            transpiled.qasm(filename=outputdir+"reference\\"+name)
    
    #print("[Step 3: transpile with qCharta]")
    for name, circuit in quantum_circuits.items():
        #print("---"+name)
        # create transpiler with coupling map
        transpiler = qCharta(coupling_map, seed)

        # create pass manager and append transformation pass
        pass_manager = PassManager()
        pass_manager.append(transpiler)

        # run transformation pass
        mapped_qc = pass_manager.run(circuit)

        cost = get_circuit_cost(mapped_qc)
        own_results.append(cost)
        own_cost = own_cost+cost

        #print("cost: "+str(cost))

        if check_eq:
            # check if result is equivalent to original ciruit
            if check_equivalence(circuit,mapped_qc):
                print(name +": result = original")
            else:
                print(name +": result is not equivalent")

        filecontent = mapped_qc.qasm()
        filecontent = filecontent.replace('\n', '\n' + get_layout_description_comment(transpiler.initial_layout, circuit_to_dag(mapped_qc)) + '\n', 1)

        with open(outputdir+"qCharta\\"+name, "w+") as file:
            file.write(filecontent)
        file.close()

    return [reference_cost,reference_results,own_cost,own_results]

if __name__=="__main__":
    main()