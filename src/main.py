from qiskit import QuantumCircuit, transpile
from qiskit.test.mock.backends import FakeBrooklyn

path = '..\\benchmarks\\adder-3.qasm'
qc = QuantumCircuit.from_qasm_file(path=path)
qc_transpiled = transpile(qc, backend=FakeBrooklyn())
filename = '..\\mapped\\adder-3.qasm'
qc_transpiled.qasm(filename=filename)