# Notebooks MDF (Measurement Data Format) Analysis.

Cloud based MDF4 file analysis with Jupyter Notebooks, Python 3.8 & asammdf.

- [MDF4 CAN Bus Data Logger (Intro + J1939/OBD2 Samples)](https://www.csselectronics.com/screen/page/mdf4-measurement-data-format/language/en)

- Target Audience: Engineers familiar with MDF analysis, unfamiliar with the Python analysis stack.
- Python experience is suggested but not required.

## Usage:

### Online.

Cloud based examples that run on any modern browser:

| Notebook                             | Binder Link                                                                                                                                                                           |
|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Quickstart                           | [![01_QuickStart](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/AutomotiveDevops/Jupyter_MDF_Analysis/master?filepath=01_QuickStart.ipynb)                         |
| Working With ```asammdf.MDF```       | [![02_Working_With_MDF_Class](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/AutomotiveDevops/Jupyter_MDF_Analysis/master?filepath=02_Working_With_MDF_Class.ipynb) |
| Working With the ```asammdf.Signal``` | [![03_Working_with_Signal](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/AutomotiveDevops/Jupyter_MDF_Analysis/master?filepath=03_Working_with_Signal.ipynb)       |
| ```asammdf``` issue #157             | [![10_asammdf_issue_157](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/AutomotiveDevops/Jupyter_MDF_Analysis/master?filepath=10_asammdf_issue_157.ipynb)           |

### Locally:

Virtual Environments:

Creates virtual environment and launches ```jupyter-notebook```:

```
git clone --depth=1 https://github.com/AutomotiveDevOps/Jupyter_MDF_Analysis.git
cd Jupyter_MDF_Analysis
make venv
make nb
```

[```repo2docker```](https://github.com/jupyter/repo2docker/blob/master/README.md): 

```
repo2docker https://github.com/AutomotiveDevOps/Jupyter_MDF_Analysis.git
```

[Windows support available upon request](https://github.com/AutomotiveDevops/Jupyter_MDF_Analysis/issues).

## Introductions to Jupyter Notebooks:

### Tutorials/Examples

- [How To Use Jupyter Notebooks](https://www.codecademy.com/articles/how-to-use-jupyter-notebooks)

  >> Jupyter Notebooks are a powerful way to write and iterate on your Python code for data analysis. Rather than writing and re-writing an entire program, you can write lines of code and run them one at a time. Then, if you need to make a change, you can go back and make your edit and rerun the program again, all in the same window.
  
#### Keyboard Shortcuts

- https://towardsdatascience.com/jypyter-notebook-shortcuts-bf0101a98330
- https://cheatography.com/weidadeyue/cheat-sheets/jupyter-notebook/

### Articles

- [Beyond Interactive: Notebook Innovation at Netflix](https://towardsdatascience.com/polynote-the-new-jupyter-c7696a321b09)

  >> Data powers Netflix. It permeates our thoughts, informs our decisions, and challenges our assumptions. It fuels experimentation and innovation at unprecedented scale. Data helps us discover fantastic content and deliver personalized experiences for our 130 million members around the world.

  >> Notebooks were first introduced at Netflix to support data science workflows. As their adoption grew among data scientists, we saw an opportunity to scale our tooling efforts. We realized we could leverage the versatility and architecture of Jupyter notebooks and extend it for general data access. In Q3 2017 we began this work in earnest, elevating notebooks from a niche tool to a first-class citizen of the Netflix Data Platform.

### Podcasts:

- [Notebooks at Netflix with Matthew Seal](https://softwareengineeringdaily.com/2019/01/15/notebooks-at-netflix-with-matthew-seal/) [01:05:22]

### Videos:

- [Up and Running: Jupyter Notebook](https://youtu.be/oJ6z02N0Te0) [11:02]
- [PayPal Notebooks: Data science and machine learning at scale, powered by Jupyter](https://youtu.be/KVGrACWVUgE)



