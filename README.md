# Bayer_compounds_msld
Following is the directory structure.
```
HNE directory:
    amber-gaff2:
          antechamber: ligands mol2, rtf and prm files (original FF charges)
          compound_1-2:   protein - MSLD prep and run files for the complex side (ligands - renormalized charges)
                          water - MSLD prep and run files for the water side (ligands - renormalized charges)
          compounds_2-11: protein - MSLD prep and run files for the complex side (ligands - renormalized charges)
                          water - used result from corresponding **PR3** calculations
          
    charmm-cgenff:
          cgenff: ligands mol2, rtf and prm files (original FF charges)
          compound_1-2:   protein - MSLD prep and run files for the complex side (ligands - renormalized charges)
                          water - MSLD prep and run files for the water side (ligands - renormalized charges)
          compounds_2-11: protein - MSLD prep and run files for the complex side (ligands - renormalized charges)
                          water - MSLD prep and run files for the water side (ligands - renormalized charges)

    opls-opls:
          ligpargen: protein mol2, pdb, rtf and prm files (original FF charges)
          compound_1-2:   protein - MSLD prep and run files for the complex side (ligands - renormalized charges)
                          water - MSLD prep and run files for the water side (ligands - renormalized charges)
          compound_2-10:  protein - MSLD prep and run files for the complex side (ligands - renormalized charges)
                          water - MSLD prep and run files for the water side (ligands - renormalized charges)
          compounds_2-11: protein - MSLD prep and run files for the complex side (ligands - renormalized charges)
                          water - MSLD prep and run files for the water side (ligands - renormalized charges)

    charmm-opls:
          compound_1-2:   protein - MSLD prep and run files for the complex side (ligands - renormalized charges)
                          water - MSLD prep and run files for the water side (ligands - renormalized charges)
          compound_2-10:  protein - MSLD prep and run files for the complex side (ligands - renormalized charges)
          compounds_2-11: protein - MSLD prep and run files for the complex side (ligands - renormalized charges)
                          water - MSLD prep and run files for the water side (ligands - renormalized charges)


PR3 directory:
    amber-gaff2:
          antechamber: ligands mol2, rtf and prm files (original FF charges)
          compound_1-2:   protein - MSLD prep and run files for the complex side (ligands - renormalized charges)
                          water - used result from corresponding **HNE** calculations
          compounds_2-11: protein - MSLD prep and run files for the complex side (ligands - renormalized charges)
                          water - MSLD prep and run files for the water side (ligands - renormalized charges)
          
    charmm-cgenff:
          cgenff: ligands mol2, rtf and prm files (original FF charges)
          compound_1-2:   protein - MSLD prep and run files for the complex side (ligands - renormalized charges)
                          water - used result from corresponding **HNE** calculations
          compounds_2-11: protein - MSLD prep and run files for the complex side (ligands - renormalized charges)
                          water - used result from corresponding **HNE** calculations

    opls-opls:
          ligpargen: protein mol2, pdb, rtf and prm files (original FF charges)
          compound_1-2:   protein - MSLD prep and run files for the complex side (ligands - renormalized charges)
                          water - used result from corresponding **HNE** calculations
          compound_2-10:  protein - MSLD prep and run files for the complex side (ligands - renormalized charges)
                          water - used result from corresponding **HNE** calculations
          compounds_2-11: protein - MSLD prep and run files for the complex side (ligands - renormalized charges)
                          water - used result from corresponding **HNE** calculations

    charmm-opls:
          compound_1-2:   protein - MSLD prep and run files for the complex side (ligands - renormalized charges)
                          water - used result from corresponding **HNE** calculations
          compound_2-10:  protein - MSLD prep and run files for the complex side (ligands - renormalized charges)
                          water - MSLD prep and run files for the water side (ligands - renormalized charges)
          compounds_2-11: protein - MSLD prep and run files for the complex side (ligands - renormalized charges)
                          water - used result from corresponding **HNE** calculations
                          

Charge_correction: CHARMM input files for book-ending correction, MBAR analysis scripts.
                   see also - (https://github.com/Vilseck-Lab/msld-py-prep/tree/main/bookending_corrections)

run_files: CHARMM, ALF, and bash scripts for running MSLD simulations.

> FF - Force Field
> ALF - Adaptive Landscape Flattening

Compounds numbering:
-------------------
| Publication |  RawData |
| ----------  | --------   |
| 1  | mol22 |
| 2  | mol46 |
| 3  | mol48 | 
| 4  | mol49 |
| 5  | mol50 |
| 6  | mol51 |
| 7  | mol53 |
| 8  | mol54 |
| 9  | mol55 |
| 10 | mol56 |
| 11 | mol58 |

