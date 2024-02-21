# DesPD
Machine learning Descriptors for Phase Diagram prediction

# Requirements
Python >= 3.7

pandas >= 1.2.5

# Usage
A detailed discussion can be found in: "G. Deffrennes, K. Terayama, T. Abe, R. Tamura, A machine learning-based classification approach for phase diagram prediction, Materials & Design 215 (2022) 110497. https://doi.org/10.1016/j.matdes.2022.110497".

For each point of interest, the script simply requires the composition of the elements and the temperature (see the example input file for the formatting).

## Thermodynamic properties
Descriptors are obtained from the composition and the thermodynamic properties of the pure elements.

The underlying data are from the SGTE PURE database in its version 5.0 (Alan Dinsdale, SGTE Data for Pure Elements, Calphad Vol 15(1991) pp. 317-425).

**The elements currently supported are Al, Cu, Mg, Si, Zn.**

**The minimum and maximum temperatures are 300K and 3000K, respectively.**

## Excess thermodynamic properties (CALPHAD extrapolations from the binaries)
Descriptors are obtained from the binary interaction parameters assessed in various work (references can be found in "Binary_interaction_parameters.csv") based on the Muggianu formalism.

**The elements currently supported are Al, Cu, Mg, Si, Zn.**

**Only the liquid phase is currently included.**

**Calculations can be performed at any temperature or composition, but note that extrapolations in regions where the phase is metastable or where data are lacking are unreliable.**

# License
This project is licensed under the terms of the MIT license.
