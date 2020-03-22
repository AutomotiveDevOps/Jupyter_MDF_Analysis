```python
from asammdf import Signal
import numpy as np
```


```python
# create 3 Signal objects with different time stamps

# unit8 with 100ms time raster
timestamps = np.array([0.1 * t for t in range(5)], dtype=np.float32)
s_uint8 = Signal(samples=np.array([t for t in range(5)], dtype=np.uint8),
                 timestamps=timestamps,
                 name='Uint8_Signal',
                 unit='u1')
```


```python
s_uint8.plot()
```

    WARNING:root:Signal plotting requires pyqtgraph or matplotlib



    ---------------------------------------------------------------------------

    Exception                                 Traceback (most recent call last)

    <ipython-input-3-5d1c358dd80f> in <module>
    ----> 1 s_uint8.plot()
    

    /projects/asammdf/asammdf/signal.py in plot(self, validate)
        167             from .gui.plot import plot
        168 
    --> 169             plot(self, validate=True)
        170             return
        171 


    /projects/asammdf/asammdf/gui/plot.py in plot(signals, title, validate)
         58     else:
         59         logging.warning("Signal plotting requires pyqtgraph or matplotlib")
    ---> 60         raise Exception("Signal plotting requires pyqtgraph or matplotlib")
    

    Exception: Signal plotting requires pyqtgraph or matplotlib



```python
import IPython.display as display
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
import seaborn as sns
```


```python
mpl.rc_file_defaults()
plt.plot(s_uint8.timestamps, s_uint8.samples)
```




    [<matplotlib.lines.Line2D at 0x7f6d5c65a130>]




![png](markdown/81_-_Working_with_Signal_files/markdown/81_-_Working_with_Signal_4_1.png)



```python
mpl.rc_file_defaults()
sns.set()
plt.plot(s_uint8.timestamps, s_uint8.samples)
```




    [<matplotlib.lines.Line2D at 0x7f6d5bf9a910>]




![png](markdown/81_-_Working_with_Signal_files/markdown/81_-_Working_with_Signal_5_1.png)



```python
mpl.rc_file_defaults()
sns.set(
    rc={
        "figure.figsize": (11.69, 8.27), # A4
        "figure.facecolor": "w",
        "figure.edgecolor": "k",
        "axes.labelsize": 18,
        "axes.titlesize": 18,
    }
)

plt.plot(s_uint8.timestamps, s_uint8.samples)
```




    [<matplotlib.lines.Line2D at 0x7f6d5befd670>]




![png](markdown/81_-_Working_with_Signal_files/markdown/81_-_Working_with_Signal_6_1.png)



```python
mpl.rc_file_defaults()
sns.set(
    rc={
        "figure.figsize": (11.69, 8.27), # A4
        "figure.facecolor": "w",
        "figure.edgecolor": "k",
        "axes.labelsize": 18,
        "axes.titlesize": 18,
    }
)
with plt.xkcd():
    fig1 = plt.plot(s_uint8.timestamps, s_uint8.samples, marker="P", markersize=18)
    plt.xlabel("Time (s)")
    plt.ylabel("Uint8 Signal [uint8]")
    plt.title("Uint8 XKCD Plot")
```

    WARNING:matplotlib.font_manager:findfont: Font family ['xkcd', 'xkcd Script', 'Humor Sans', 'Comic Neue', 'Comic Sans MS'] not found. Falling back to DejaVu Sans.
    WARNING:matplotlib.font_manager:findfont: Font family ['xkcd', 'xkcd Script', 'Humor Sans', 'Comic Neue', 'Comic Sans MS'] not found. Falling back to DejaVu Sans.



![png](markdown/81_-_Working_with_Signal_files/markdown/81_-_Working_with_Signal_7_1.png)

