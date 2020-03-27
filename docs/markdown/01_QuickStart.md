# ```asammdf``` Quick Start & Reference.

A one page introduction to ```asammdf``` for Measurement Data Format (MDF) data analysis.

For engineers wanting to drink from a fire hose or already experienced with Python data analysis.

Replaces some or all of the functionality of these tools with a fullly opensource, free, analysis stack:

- [AVL CONCERTO 5™](https://www.avl.com/web/guest/-/avl-concerto-5-)
- [MathWorks® Vehicle Network Toolbox™](https://www.mathworks.com/products/vehicle-network.html)
- [ETAS Measure Data Analyzer (MDA V8)](https://www.etas.com/en/company/realtimes_2019_2020-quick-and-intuitive-analysis-of-measurement-data.php)
- [National Instruments DIAdem](https://www.ni.com/en-us/shop/data-acquisition-and-control/application-software-for-data-acquisition-and-control-category/what-is-diadem.html)
- [Vector CANape & vSignalyzer](https://www.vector.com/int/en/products/application-areas/ecu-calibration/analyzing-evaluating-measurement-data/)


```python
%matplotlib inline
import asammdf
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
```

# Create MDF File

- Create a [0, 10)s time vector with 100Hz sampling rate (10 ms raster)
- Create a simple MDF file with two channels:
    - "EngineSpeedCmd" 0.5 Hz sinewave with amplitude=10, & dc offset=600.
    - "EngineSpeed" 0.5 Hz sinewave with amplitude=5, phi=pi/8, & dc offset=600.


### Generate Engine Speed signals


```python
# Time Vector
t0=0  # [s]
tf=10 # [s]
f_sample = 100 # [Hz]
dT = 1/f_sample # [s]
timestamps = np.arange(t0, tf, dT)
# Engine Speed
A = 10
f_signal = 0.5
dc_offset = 600
engine_speed_cmd = A*np.sin(2*np.pi*f_signal*timestamps)+dc_offset
engine_speed = A*0.5*np.sin(2*np.pi*f_signal*(timestamps-0.25))+dc_offset
```

### Plot engine speed signal.

Direct plotting with [matplotlib](https://matplotlib.org/) & [seaborn](https://seaborn.pydata.org/).


```python
sns.set(
    rc={
        "figure.figsize": (11.69, 8.27), # A4 paper size.
        "figure.facecolor": "w",
        "figure.edgecolor": "k",
        "axes.labelsize": 18,
        "axes.titlesize": 18,
        "legend.fontsize": 18,
    }
)
plt.plot(timestamps, engine_speed_cmd, timestamps, engine_speed)
plt.xlabel("Time [s]")
plt.ylabel("Engine Speed [rpm]")
plt.title("Engine Speed vs Time")
plt.legend(
    {"Engine Speed Cmd", "Engine Speed"},
    loc='upper right'
);
plt.savefig(
    "EngineSpeedPlot.png",
    transparent=False,
    bbox_inches='tight'
);
```


![png](docs/markdown/01_QuickStart_files/docs/markdown/01_QuickStart_6_0.png)


## Generate ```asammdf```.```Signal``` & save ```MDF``` file.

Convert the ```numpy``` arrays into ```asammdf.Signal```s & save.

### ```Signal``` Object


```python
asammdf.Signal?
```


```python
engine_speed_cmd_sig = asammdf.Signal(
    samples=engine_speed_cmd,
    timestamps=timestamps,
    unit='rpm',
    name='EngineSpeedCmd',
    conversion=None,
    comment='Swept sine plant identification, X(t)',
    raw=True,
    master_metadata=None,
    display_name='Engine Speed Command',
    attachment=(),
    source=None,
    bit_count=None,
    stream_sync=False,
    invalidation_bits=None,
    encoding=None,
)
engine_speed_sig = asammdf.Signal(
    samples=engine_speed,
    timestamps=timestamps,
    unit='rpm',
    name='EngineSpeed',
    conversion=None,
    comment='Swept sine plant identification, Y(t)',
    raw=True,
    master_metadata=None,
    display_name='Engine Speed',
    attachment=(),
    source=None,
    bit_count=None,
    stream_sync=False,
    invalidation_bits=None,
    encoding=None,
)
signals = [
    engine_speed_cmd_sig,
    engine_speed_sig,
]
```

### ```MDF``` Object


```python
asammdf.MDF?
```

Write the file directly in and out of a context manager.


```python
with asammdf.MDF(version="4.10") as mdf:
    mdf.append(signals, "Created by Python") 
    # save new file
    mdf.save("quickstart_example.mf4", overwrite=True)
```


```python
mdf = asammdf.MDF(version="4.10")
mdf.append(signals, "Created by Python") 
    # save new file
mdf.save("quickstart_example.mf4", overwrite=True)
mdf.close()
```

```fsspec``` example.

> Filesystem Spec is a project to unify various projects and classes to work with remote filesystems and file-system-like abstractions using a standard pythonic interface.
> - https://filesystem-spec.readthedocs.io/en/latest/

This allows reading & writing directly from S3, Azure Datalakes, Google Storage, and others.


```python
import fsspec
with fsspec.open("quickstart_example_fs.mf4", "wb") as fid:
    with asammdf.MDF(version="4.10") as mdf:
        mdf.append(signals, "Created by Python") 
        # save new file
        mdf.save(fid, overwrite=True)
```

# Read & Analyze MDF



```python
%matplotlib inline
import asammdf
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
```

Open a file with and without ```fsspec```.


```python
with fsspec.open("quickstart_example_fs.mf4", "rb") as fid:
    mdf = asammdf.MDF(fid)
```


```python
mdf = asammdf.MDF("quickstart_example.mf4")
```

List the channels in the database.


```python
mdf.channels_db
```




    {'time': ((0, 0),), 'EngineSpeedCmd': ((0, 1),), 'EngineSpeed': ((0, 2),)}




```python
mdf.get_channel_unit("EngineSpeedCmd")
```




    'rpm'




```python
mdf.get_channel_comment("EngineSpeedCmd")
```




    'Swept sine plant identification, X(t)'




```python
sns.set(
    rc={
        "figure.figsize": (11.69, 8.27), # A4 paper size.
        "figure.facecolor": "w",
        "figure.edgecolor": "k",
        "axes.labelsize": 18,
        "axes.titlesize": 18,
        "legend.fontsize": 18,
    }
)
for channel in mdf.iter_channels():
    channel.plot()
```

    WARNING:root:Signal plotting requires pyqtgraph or matplotlib



![png](docs/markdown/01_QuickStart_files/docs/markdown/01_QuickStart_27_1.png)


    WARNING:root:Signal plotting requires pyqtgraph or matplotlib



![png](docs/markdown/01_QuickStart_files/docs/markdown/01_QuickStart_27_3.png)


### Export to [```pandas```.```DataFrame```](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html):


```python
df = mdf.to_dataframe()
```


```python
df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>EngineSpeedCmd</th>
      <th>EngineSpeed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>1000.000000</td>
      <td>1000.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>600.000000</td>
      <td>600.000000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>7.074606</td>
      <td>3.537303</td>
    </tr>
    <tr>
      <th>min</th>
      <td>590.000000</td>
      <td>595.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>592.928932</td>
      <td>596.464466</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>600.000000</td>
      <td>600.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>607.071068</td>
      <td>603.535534</td>
    </tr>
    <tr>
      <th>max</th>
      <td>610.000000</td>
      <td>605.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>EngineSpeedCmd</th>
      <th>EngineSpeed</th>
    </tr>
    <tr>
      <th>timestamps</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0.00</th>
      <td>600.000000</td>
      <td>596.464466</td>
    </tr>
    <tr>
      <th>0.01</th>
      <td>600.314108</td>
      <td>596.577264</td>
    </tr>
    <tr>
      <th>0.02</th>
      <td>600.627905</td>
      <td>596.693441</td>
    </tr>
    <tr>
      <th>0.03</th>
      <td>600.941083</td>
      <td>596.812880</td>
    </tr>
    <tr>
      <th>0.04</th>
      <td>601.253332</td>
      <td>596.935465</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>9.95</th>
      <td>598.435655</td>
      <td>595.954915</td>
    </tr>
    <tr>
      <th>9.96</th>
      <td>598.746668</td>
      <td>596.049225</td>
    </tr>
    <tr>
      <th>9.97</th>
      <td>599.058917</td>
      <td>596.147434</td>
    </tr>
    <tr>
      <th>9.98</th>
      <td>599.372095</td>
      <td>596.249445</td>
    </tr>
    <tr>
      <th>9.99</th>
      <td>599.685892</td>
      <td>596.355157</td>
    </tr>
  </tbody>
</table>
<p>1000 rows × 2 columns</p>
</div>



Reset Index

Convert the 'timestamps' index back into a column for direct plotting from ```pandas```.


```python
# Convert the 
df.reset_index(inplace=True)
```


```python
df.plot(x="timestamps", y={"EngineSpeed", "EngineSpeedCmd"})
plt.ylabel("Engine Speed [rpm]")
plt.xlabel("Timestamps [s]");
```


![png](docs/markdown/01_QuickStart_files/docs/markdown/01_QuickStart_34_0.png)


# Export

```asammdf``` natively supports:

- csv
- hdf5
- mat
- parquet


```python
mdf.export?
```


```python
mdf.export(fmt="csv")
!ls *.csv
```

    quickstart_example.ChannelGroup_0.csv



```python
pd.read_csv("quickstart_example.ChannelGroup_0.csv")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>timestamps</th>
      <th>EngineSpeedCmd</th>
      <th>EngineSpeed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.00</td>
      <td>600.000000</td>
      <td>596.464466</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.01</td>
      <td>600.314108</td>
      <td>596.577264</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.02</td>
      <td>600.627905</td>
      <td>596.693441</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.03</td>
      <td>600.941083</td>
      <td>596.812880</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.04</td>
      <td>601.253332</td>
      <td>596.935465</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>995</th>
      <td>9.95</td>
      <td>598.435655</td>
      <td>595.954915</td>
    </tr>
    <tr>
      <th>996</th>
      <td>9.96</td>
      <td>598.746668</td>
      <td>596.049225</td>
    </tr>
    <tr>
      <th>997</th>
      <td>9.97</td>
      <td>599.058917</td>
      <td>596.147434</td>
    </tr>
    <tr>
      <th>998</th>
      <td>9.98</td>
      <td>599.372095</td>
      <td>596.249445</td>
    </tr>
    <tr>
      <th>999</th>
      <td>9.99</td>
      <td>599.685892</td>
      <td>596.355157</td>
    </tr>
  </tbody>
</table>
<p>1000 rows × 3 columns</p>
</div>




```python
mdf.export(fmt="hdf5")
!ls *.hdf
```

    quickstart_example.hdf



```python
mdf.export(fmt="mat")
!ls *.mat
```

    quickstart_example.mat

