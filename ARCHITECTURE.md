# Reconstruction architecture

```text
Frequency sweep -> dimensionless resonator bank -> magnitude response -> peak comparison
```

The Python model illustrates frequency-selective resonators. It does not model the original beam geometry, acoustic coupling, tissue, electrodes or clinical hearing response. Fit geometry/materials and validate against measured response before making device claims.

See METHODOLOGY.md for research and evaluation details, and reconstruction/model.py for the executable analytical model.

## Optional SPICE illustration

`reconstruction/resonator-bank.cir` is an ideal three-channel series-RLC analogue with voltage read across each capacitor. Each channel uses L=1 H, C=1/(2*pi*f)^2 and R=2*pi*f/5, giving Q=5 at 500, 1000 and 2000 Hz. The 1 H value is a mathematical normalization, not a proposed implant component. Open the netlist in LTspice, run AC analysis and plot V(c500), V(c1000), V(c2000). It matches the transfer-function form of model.py. LTspice execution was not performed here; these values do not describe recovered beam geometry or actual hearing performance.
