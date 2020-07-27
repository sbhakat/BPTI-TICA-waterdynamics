# BPTI-TICA-waterdynamics
The core of a protein is held together by hydrogen bond interactions involving backbone amides. Local fluctuations or complete unfolding of a protein breaks the hydrogen bonds involving backbone amides (NH) and allows water penetration. This allows hydrogen exchange (HX) between NH and the hydrogen atoms of the solvent water molecules. Thus, the HX rates, which can be measured by NMR spectroscopy or mass spectrometry, can give valuable information about the local stability of the protein structure as well as conformational changes and folding pathways.

BPTI is like a rock. The local fluctuation in the loop region opens up the cavity which enables HDX between Ile18NH and water. However, this is a very slow process. In millisecond long MD simulation of DESRES (within M1 ensemble) the loop fluctuation has very few sampling. In this project I have used TIC to capture the slow degrees of freedom associated with this loop motion. The TIC combined with PT-Metad-WTE enables better sampling of the conformational space.

Our proposed called HDX mechanism

![bpti-hdx](/hdx-mechanism.png)

The following Figure shows the Loop region in BPTI. Local fluctuations in the loop motion breaks the H-bond interactions which allows solvent penetration.

![bpti](/local-fluctuation.png)

The following Figure shows what I meant by FW and SW in the Jupyter Notebooks

![bpti-water](/water-bpti-fwsw.png)

The following Figure shows the so called 'spectral gap' along a RC (TICs). Keep an eye on the timescale (in this case frames) seperation.

![tic-seperation](/left-righttic.png)

Timescale of the process (Zero indexed)

![tica-timescale](/timescale-sgoop.png)

Sampling of the solvated state (DESRES vs Metadynamics): using TIC CV combined with PT-Metad-WTE

![metaddesres-timescale](/desres-metad.png)

Notes:

1. See Analysis folder to see how I generated the TICA.

2. See Table S2 in the paper entitled 'Transient access to the protein interior: Simulation vs NMR' by Persson and Halle to see the definition of M1 state.

3. See 'How amide hydrogens exchage in native proteins' to see how one can calculate HDX from molecular simulation using simple cutoff distance.

4. Check the attached Figure to see what I meant by loop motion.
