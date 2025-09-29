import csv
import matplotlib.pyplot as plt
from neuron import h
import instantiate_neuron as IN

# Defining a function for: cell instantiation and simulation and safe in file
def SquarePulses_stim(stim_ampl, morph_filename, output_filename):
    # Empty list to safe in file
    #list_t = []
    #list_i = []
    #list_v = []
    data = {}
    
    cell = IN.NEURON(morph_filename)
    
    # Define plots
    fig, ax = plt.subplots(2, 1, figsize = (15, 9))
    
    ax[0].set_title('Soma voltage')
    ax[0].set_xlabel('t (ms)')
    ax[0].set_ylabel('V (mV)')
    fig.suptitle('%s' %morph_filename)

    ax[1].set_title('Current injection')
    ax[1].set_xlabel('t (ms)')
    ax[1].set_ylabel('I (nA)')

    # Stimulation
    i = 0
    for sa in stim_ampl:  
        # Place a stimulation electrode in the middle of the soma
        stim = h.IClamp(cell.somatic[0](0.5))         
        stim.delay = 100   # stim delay (ms)
        stim.dur = 300     # stim duration (ms)
        stim.amp = sa    # stim amplitude (nA)    
        # Initialize NEURON vectors to record time, voltage and current
        # time vector
        rec_t = h.Vector()
        rec_t.record(h._ref_t)
        # membrame potential vector
        rec_v_soma = h.Vector()
        rec_v_soma.record(cell.somatic[0](0.5)._ref_v)
        # current
        rec_i = h.Vector()
        rec_i.record(stim._ref_i)

        # Initialize and run a simulation
        h.load_file('stdrun.hoc')
        h.finitialize(-65)
        h.continuerun(500)
        
        # Fill in lists
        #list_t.append(list(rec_t))
        #list_i.append(list(rec_i))
        #list_v.append(list(rec_v_soma))
        data['time_%s' %i] = list(rec_t)
        data['current_%s' %i] = list(rec_i)
        data['voltage_%s' %i] = list(rec_v_soma)
        
        # Plot
        ax[0].plot(rec_t, rec_v_soma)
        ax[1].plot(rec_t, rec_i)
        
        i = i + 1
        
    zd = zip(*data.values())
    with open(output_filename, 'w') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(data.keys())
        writer.writerows(zd)