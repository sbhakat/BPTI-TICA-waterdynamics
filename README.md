# BPTI-TICA-waterdynamics
The core of a protein is held together by hydrogen bond interactions involving backbone amides. Local fluctuations or complete unfolding of a protein breaks the hydrogen bonds involving backbone amides (NH) and allows water penetration. This allows hydrogen exchange (HX) between NH and the hydrogen atoms of the solvent water molecules. Thus, the HX rates, which can be measured by NMR spectroscopy or mass spectrometry, can give valuable information about the local stability of the protein structure as well as conformational changes and folding pathways.

BPTI is like a rock. The local fluctuation in the loop region opens up the cavity which enables HDX between Ile18NH and water. However, this is a very slow process. In millisecond long MD simulation of DESRES (within M1 ensemble) the loop fluctuation has very few sampling. In this project I have used TIC to capture the slow degrees of freedom associated with this loop motion. The TIC combined with PT-Metad-WTE enables better sampling of the conformational space.

![bpti](/local-fluctuation.png)

Notes:

1. See Analysis folder to see how I generated the TICA.

2. See Table S2 in the paper entitled 'Transient access to the protein interior: Simulation vs NMR' by Persson and Halle to see the definition of M1 state.

3. See 'How amide hydrogens exchage in native proteins' to see how one can calculate HDX from molecular simulation using simple cutoff distance.

4. Check the attached Figure to see what I meant by loop motion.
