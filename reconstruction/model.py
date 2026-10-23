"""New reconstruction, 2026-10-23. Demo inputs are synthetic, not historical results."""
import math,cmath
def response(frequency,resonance,q=5,gain=1):
    if frequency<0 or resonance<=0 or q<=0:raise ValueError('Invalid oscillator')
    ratio=frequency/resonance
    return gain/(1-ratio*ratio+1j*ratio/q)
def sweep(resonances,frequencies):
    return [{'frequency_hz':f,**{f'channel_{r}_hz':abs(response(f,r)) for r in resonances}} for f in frequencies]
def demo():
    assert abs(abs(response(1000,1000))-5)<1e-9
    return {'model':'dimensionless second-order oscillator, not recovered beam geometry','synthetic_response':sweep([500,1000,2000],[100,500,1000,2000])}

if __name__ == "__main__":
    import json
    print(json.dumps(demo(), indent=2))
