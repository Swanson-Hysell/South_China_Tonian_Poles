# South China Tonian Poles

This repository accompanies the paper:

> Swanson-Hysell, N. L. (2026), Tonian paleomagnetic poles from South China are consistent with progressive tectonic motion over the North Pole, *Geology*, https://doi.org/10.1130/G54035C.1

## Repository information

### Overview

This repository contains the data, code, and reproducible workflows used to evaluate late Tonian paleomagnetic poles from South China and to test whether the available pole database is consistent with progressive plate motion across the geographic North Pole. The analyses emphasize explicit treatment of age uncertainty, inclination-shallowing uncertainty, and pole position uncertainty when interpreting apparent polar wander paths (APWPs).

### Figures

The paper contains a single figure composed of two panels, both generated directly from the code in this repository:

- `South_China_Tonian_poles.pdf`  
  South China Tonian paleomagnetic poles incorporating inclination-shallowing uncertainty.

- `South_China_India_Tonian_poles_reconstructed.pdf`  
  Time-progressive reconstructions showing South China (and India) drifting across the geographic North Pole.

### Repository structure

- `data/`  
  Compiled paleomagnetic poles, ages, and associated uncertainties used in the analysis.

- `code/`  
  Python scripts and notebooks used to:
  - propagate inclination-shallowing uncertainty following Pierce et al. (2022),
  - visualize Tonian pole distributions,
  - generate paleogeographic reconstructions consistent with pole positions.

- `figures/`  
  Generated figure panels used in the paper.

### License

This repository is released under the **BSD-3-Clause** license. Free for re-use with attribution of the repository and the associated Swanson-Hysell (2025) paper.

## Comment text

**Tonian paleomagnetic poles from South China are consistent with progressive plate tectonic motion over the North Pole**

Nicholas L. Swanson-Hysell
Institute for Rock Magnetism, Department of Earth and Environmental Sciences,  
University of Minnesota, Minneapolis, Minnesota 55455, USA

Due to basin development that followed the Jiangnan Orogeny, there is a rich record of late Tonian siliciclastic sedimentary rocks in South China. Arc volcanism delivered ash into sedimentary successions, enabling the development of U-Pb dates. These rocks present the opportunity to develop a high-quality apparent polar wander path (APWP) to advance Neoproterozoic paleogeographic reconstructions. Given the importance of this endeavor, it is excellent to see paleomagnetic and geochronology data continue to be developed from South China as in Jing et al. (2025).

Jing et al. present paleomagnetic data from the Kaijianqiao Formation and argue that Tonian poles from South China require large-scale true polar wander. They further propose that South China and India were in the southern hemisphere on Rodinia’s margin. This comment highlights that, in contrast to how the data are presented in Jing et al., the paleomagnetic database is consistent with South China progressively drifting over the North Pole. While many issues merit discussion, I highlight four complexities: (1) the U-Pb tuff age is a maximum age as it comes from below the paleomagnetic sites; (2) the claim that inclination shallowing has been fully mitigated neglects significant uncertainty; (3) by focusing only on paleolatitudes and disregarding pole positions, the proposed scenarios do not incorporate the constraint that the continent crossed the geographic pole; and (4) the reconstructed southern hemisphere position of India and South China violates constraints on the orientation of the continents.

The U-Pb date of 792.9 ± 5.5 Ma from a tuff 100 m below the lowest paleomagnetic site provides a maximum age, since overlying sites must be younger. Confidently assigning an age requires bracketing dates. An upper bound is important given that dates as young as 715.0 ± 9.8 Ma have been reported from the Kaijianqiao Formation (Jiang et al., 2016). The interpretation that the 60 m interval of sampled strata is close to 792.9 ± 5.5 Ma could be correct. However, available data constrain the sites as bounded by that date below and the 717 Ma Sturtian Snowball Earth onset above.

Even in the best-constrained scenarios there will be uncertainty associated with the inclination shallowing in rocks with detrital remanent magnetization. Jing et al. apply the elongation (E/I) method and then use a single resulting flattening (f) factor to correct the pole. They say that in doing so they have fully mitigated inclination shallowing as an explanation for discrepant pole positions. However, as highlighted in Pierce et al. (2022), this approach neglects that the E/I method returns an uncertainty range of f factors that needs to be considered. No method returns an f factor without uncertainty. In the case of the data presented in Jing et al., the 95% confidence bounds for possible f factors are quite broad. If the f factors returned from the E/I analysis are used to estimate uncertainty instead of taking a singular value, the pole position and paleolatitude are much less certain (Fig. 1). For other sedimentary paleomagnetic poles, the Jing et al. interpretation that they are from primary detrital remanent magnetization and entirely unaffected by inclination shallowing is internally inconsistent.

Incorporating positional uncertainty and temporal uncertainty leads to late Tonian paleomagnetic poles for South China that can readily be interpreted as a progressive APWP associated with the block transiting over the North Pole at rates of ~6–9 cm/yr (Fig. 1). While Jing et al. show no scenarios with a pole transit, it is required unless vertical-axis rotations of 180° are invoked. While smaller rotations are feasible and can explain some dispersion, ones that large would require oroclines that are not observed.

When a paleomagnetic pole polarity is inverted, the continent is reconstructed to the opposite hemisphere and rotated by 180°. Jing et al.’s preferred “inverted” reconstruction violates the orientation constraints of India’s ca. 760 Ma Malani pole and the Liantuo poles for South China. At 760 Ma, Jing et al. position the blocks in the southern hemisphere, but with the orientation implied by a northern hemisphere reconstruction (Fig. 1).

<img width="800" alt="South_China_Tonian_Poles_figure" src="https://github.com/user-attachments/assets/7a9c5fcc-675a-44d6-a7aa-daa2717df127" />

> (A) South China paleomagnetic poles incorporating inclination shallowing uncertainty using the method of Pierce et al. (2022). See Park et al. (2021) and Jing et al. (2025) for citations to poles and ages. Minor vertical-axis rotation can result in agreement between the Kaijianqiao and Liantuo poles, and these poles could be similar in age given chronostratigraphic constraints. (B) A reconstruction that honors these poles by South China drifting over geographic north. Pole positions require the continent to cross the spin axis—a scenario not explored in the paleolatitude analysis of Jing et al. The poles are rotated along with South China (shown with a hypothesized India and Oman connection) in 10 m.y. intervals. The Malani pole that constrains the latitude and orientation of India ca. 760 Ma is also shown. A northern hemisphere position for India sets the stage for subsequent Gondwana assembly. The code that generated this figure is available in this repository.

Uncertainties associated with age assignments, vertical-axis rotations, and inclination shallowing can all play a role in the dispersion of individual paleomagnetic poles from APWPs, as is commonly observed for Cenozoic paleomagnetic poles (Vaes et al., 2022). These realities are cautionary for inferences of motion that are made between individual pole pairs. The importance of the paleogeography and geodynamic hypotheses is motivating for researchers to continue to develop abundant high-quality paleomagnetic and geochronologic data constrained in a rigorous geological context.

**References**

Jiang, Z.-F., Cui, X.-Z., Jiang, X.-S., Wang, J., Zhuo, J.-W., Xiong, G.-Q., Lu, J.-Z.,
Wu, H., and Wei, Y.-N., 2016, New zircon U-Pb ages of the pre-Sturtian rift
successions from the western Yangtze Block, South China and their
geological significance: *International Geology Review*, v. 58, p. 1064–1075,
https://doi.org/10.1080/00206814.2016.1141719.

Jing, X., et al., 2025, Tonian true polar wander events recorded by paleolatitudinal
variations of South China and its Southern Hemispheric position in Rodinia:
*Geology*, https://doi.org/10.1130/G53710.1.

Park, Y., Swanson-Hysell, N.L., Xian, H., Zhang, S., Condon, D.J., Fu, H., and
Macdonald, F.A., 2021, A consistently high latitude South China from 820 to
780 Ma: Implications for exclusion from Rodinia and the feasibility of large-
scale true polar wander: *Journal of Geophysical Research: Solid Earth*, v. 126,
https://doi.org/10.1029/2020JB021541.

Pierce, J., Zhang, Y., Hodgin, E.B., and Swanson-Hysell, N.L., 2022, Quantifying
inclination shallowing and representing flattening uncertainty in sedimentary
paleomagnetic poles: *Geochemistry, Geophysics, Geosystems*,
https://doi.org/10.1029/2022GC010682.

Vaes, B., Gallo, L.C., and van Hinsbergen, D.J.J., 2022, On pole position: Causes
of dispersion of the paleomagnetic poles behind apparent polar wander
paths: *Journal of Geophysical Research: Solid Earth*,
https://doi.org/10.1029/2022JB02395.
