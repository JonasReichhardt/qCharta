from qiskit.transpiler.basepasses import TransformationPass
from qiskit.transpiler import Layout
from qiskit import QuantumRegister

import random

from sabre import Sabre
from coupling import distance_dict


class qCharta(TransformationPass):

    def __init__(self,
                 coupling_map, seed,  layout_option = 'trivial'):
        super().__init__()
        self.coupling_map = coupling_map
        self.seed = seed
        self.initial_mapping: Layout
        random.seed(seed)
        self.layout_option = layout_option

    def create_random_layout(self,dag):
        nr_qbits = len(self.coupling_map.physical_qubits)

        layout_arr = list(range(0,nr_qbits))
        random.shuffle(layout_arr)
        layout = Layout.from_intlist(layout_arr,*dag.qregs.values())

        return layout

    def create_heuristic_layout(self,dag):
        neighbor_count = []
        for qbit in self.coupling_map.physical_qubits:
            neighbor_count.append(len(self.coupling_map.neighbors(qbit)))

        # analyse the circuit to indentify the most used logical qbit 
        analysis = {}
        for gate in dag.two_qubit_ops():
            qbit1 = gate.qargs[0].index
            qbit2 = gate.qargs[1].index
            try:
                analysis[qbit1] = analysis[qbit1]+1
            except KeyError:
                analysis[qbit1] = 1
                
            try:
                analysis[qbit2] = analysis[qbit2]+1
            except KeyError:
                analysis[qbit2] = 1
        
        sorted_logical_qbits = sorted(analysis.items(), key=lambda x: x[1],reverse=True)
        
        for distance, dist_values in distance_dict.items():
            print(dist_values)
        #self.hotspot_anaysis(dag, analysis)

    def hotspot_anaysis(self, dag, analysis):
        hot_qbit = max(analysis, key=analysis.get)
        hot_gates = {}
        for gate in dag.two_qubit_ops():
            if(gate.qargs[0].index == hot_qbit):
                try:
                    hot_gates[gate.qargs[1].index] = hot_gates[gate.qargs[1].index]+1
                except KeyError:
                    hot_gates[gate.qargs[1].index] = 1
            if(gate.qargs[1].index == hot_qbit):
                try:
                    hot_gates[gate.qargs[0].index] = hot_gates[gate.qargs[0].index]+1
                except KeyError:
                    hot_gates[gate.qargs[0].index] = 1
        print(hot_qbit)
        print(hot_gates)
        print(analysis)

    def run(self, dag):
        # filll up a "reserve" register
        reg = QuantumRegister(len(self.coupling_map.physical_qubits) - len(dag.qubits), 'r')
        dag.add_qreg(reg)

        if self.layout_option == 'trivial':
            init_layout = Layout.generate_trivial_layout(*dag.qregs.values())
        elif self.layout_option == 'random':
            init_layout = Layout.generate_random_layout(dag)
        elif self.layout_option == 'heuristic':
            init_layout = self.create_heuristic_layout(dag)
        
        self.initial_layout = init_layout.copy()

        sabre = Sabre(self.coupling_map)
        return sabre.sabre_swap(dag.front_layer(), init_layout, dag, self.coupling_map)[0]