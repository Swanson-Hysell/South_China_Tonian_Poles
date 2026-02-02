# South China Tonian_Poles

This repository accompanies the paper:

> Swanson-Hysell, N. L. (2026), Tonian paleomagnetic poles from South China are consistent with progressive tectonic motion over the North Pole, *Geology*, https://doi.org/10.1130/G54035C.1

## Overview

This repository contains the data, code, and reproducible workflows used to evaluate late Tonian paleomagnetic poles from South China and to test whether the available pole database is consistent with progressive plate motion across the geographic North Pole. The analyses emphasize explicit treatment of age uncertainty, inclination-shallowing uncertainty, and pole position uncertainty when interpreting apparent polar wander paths (APWPs).

## Figures

The paper contains a single figure composed of two panels, both generated directly from the code in this repository:

- `South_China_Tonian_poles.pdf`  
  South China Tonian paleomagnetic poles incorporating inclination-shallowing uncertainty.

- `South_China_India_Tonian_poles_reconstructed.pdf`  
  Time-progressive reconstructions showing South China (and India) drifting across the geographic North Pole.

## Repository structure

- `data/`  
  Compiled paleomagnetic poles, ages, and associated uncertainties used in the analysis.

- `code/`  
  Python scripts and notebooks used to:
  - propagate inclination-shallowing uncertainty following Pierce et al. (2022),
  - visualize Tonian pole distributions,
  - generate paleogeographic reconstructions consistent with pole positions.

- `figures/`  
  Generated figure panels used in the paper.

## License

This repository is released under the **BSD-3-Clause** license. Free for re-use with attribution of the repository and the associated Swanson-Hysell (2025) paper.
