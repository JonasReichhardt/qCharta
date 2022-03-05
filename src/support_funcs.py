from qiskit import QuantumCircuit
from qiskit.dagcircuit import DAGCircuit
from qiskit.transpiler import Layout
from mqt import qcec

# DISCLAIMER
# Big thanks to Elias Foramitti for providing the support functions below

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

# author: Elias Foramitti
def check_equivalence(qc1: QuantumCircuit, qc2: QuantumCircuit) -> bool:
    config = qcec.Configuration()
    config.transform_dynamic_circuit = True
    result = qcec.verify(qc, mapped_qc, config)
    return (result.equivalence == qcec.Equivalence.equivalent)