import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os

dim1 = 2
dim2 = 5
total_plots = dim1*dim2
fig, axs = plt.subplots(dim1, dim2)
fig.set_size_inches(20, 10)
fig.dpi = 200

nsubs=9

# Make a plot for each ligand
for mol,ax in enumerate(axs.reshape(-1)):
    molid = mol+1
    if os.path.isfile('s1s' + str(molid) + '_crn2ff_qpert.str' ):   
       # Retrieve charge sets
       ff_str = np.genfromtxt('s1s' + str(molid) + '_crn2ff_qpert.str' , dtype=str, skip_header=3, skip_footer=2)
       ff = np.array(ff_str[:, 3], dtype=float)
       crn_str = np.genfromtxt('s1s' + str(molid) + '_ff2crn_qpert.str', dtype=str, skip_header=3, skip_footer=2)
       crn =  np.array(crn_str[:, 3], dtype=float)

       # Paste the two columns side by side
       ff_crn = np.column_stack((ff, crn))

       # Calculate the RMSD
       rmsd = np.sqrt(np.mean((crn - ff) ** 2))

       # Plot them
       ax.scatter(ff,crn,marker='o',linewidth=0.5)
    
       # Plot y=x line
       ax.axline((0, 0), slope=1)
    
       # Axis specs:
       ## Title
       ax.set_title(f'$L_{molid}$ - QRMSD={rmsd:.4f}',fontsize=5)
    
    ## Scale
    #ax.set_xlim(-0.9,0.7)
    #ax.set_ylim(-0.9,0.7)
    
       ## Labels
       if mol%dim2 == 0:
          ax.set_ylabel('Renormalized charges',fontsize=5)
       if mol > total_plots-dim2-1:
          ax.set_xlabel('FF charges',fontsize=5)

    else:
        molid += 1

plt.tight_layout()
plt.show()
quit()
