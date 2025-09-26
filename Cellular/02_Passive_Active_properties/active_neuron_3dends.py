from neuron import h

class ActiveNeuron_3Dend:
    def __init__(self):
        # Create soma
        self.soma = h.Section(name='soma')
        self.soma.L = 20    # micrometers
        self.soma.diam = 20 # micrometers

        # Define all the sections first: soma, dendrites and axon
        # Create a dendrites
        self.soma = h.Section(name="soma")
        self.branch_0 = h.Section(name="branch_0")
        self.branch_1 = h.Section(name="branch_1")
        self.branch_2 = h.Section(name="branch_2")
        self.axon = h.Section(name="axon")

        branchlst = [self.branch_0, self.branch_1, self.branch_2]

        # Branch geometry
        # thick
        self.branch_0.L = 100
        self.branch_0.diam = 30
        # middle
        self.branch_1.L = 100
        self.branch_1.diam = 5
        # thin
        self.branch_2.L = 100
        self.branch_2.diam = 1


        # Passive properties: cell geometry
        # Soma section (black in plot)
        self.soma.L = 20  # length (µm)
        self.soma.diam = 20  # diameter (µm)
        self.soma.Ra = 123.0  # axial resistivity (Ω*cm)
        self.soma.cm = 1  # capacitance (µF/cm^2)

         # Axon section (blue in plot)
        self.axon.diam = 3 # diameter (µm)
        self.axon.L = 100  # length (µm)
        self.axon.nseg = 5  # number of segments
        self.axon.Ra = 123.0  # axial resistivity (Ω*cm)
        self.axon.cm = 1  # capacitance (µF/cm^2)
  

        # Topology or how sections are connected
        self.axon.connect(self.soma(0))
        # Connect dendritic branches
        self.branch_0.connect(self.soma(1))
        self.branch_1.connect(self.soma(1))
        self.branch_2.connect(self.soma(1))
        
        # Passive properties: conductance and reversal potential of leak channels
        self.soma.insert("pas")
        for seg in self.soma:
            seg.pas.g = 0.0003  # Conductance of the leak channels (in S/cm2)
            seg.pas.e = (
                -70
            )  # Leak reversal potential, it influences the steady state membrane potential

        # Insert active properties
        self.soma.insert("hh")
        for seg in self.soma:
            seg.hh.gkbar = 0.1  # Maximal conductance of the potassium channels
            seg.hh.gnabar = 0.4  # Maximal conductance of the sodium channels

        
        self.axon.insert("pas")
        for seg in self.axon:
            seg.pas.g = 0.0003  # Conductance of the leak channels (in S/cm2)
            seg.pas.e = (
                -70
            )  # Leak reversal potential, it influences the steady state membrane potential

        
        for branch in branchlst:
            branch.Ra = 500.0  # axial resistivity (Ω*cm)
            branch.cm = 1  # capacitance (µF/cm^2)
            branch.insert("pas")
        for seg in branch:
            seg.pas.g = 0.0003  # Conductance of the leak channels (in S/cm2)
            seg.pas.e = (
                -70
            )  # Leak reversal potential, it influences the steady state membrane potential




