# StreetNetworkLocalArea
This repository contains the code for my PhD and subsequent publication in Law (2017). The paper applies modularity optimisation on the street network dual graph to identify street based local areas or street neighbourhoods. The repository contains code borrows/adapts from https://github.com/taynaud/python-louvain which is the python implementation for the louvain algorithm (Blondel et al 2008). 

# Setup 
The repository have been tested using the standard version of Anaconda Individual Edition which is the recommended way to setup a Python Environment for the first time. https://docs.anaconda.com/anaconda/install/index.html
Alternatively, you can create your own environment (eg. miniconda) to run the code. After setting up the python environment, clone the repository locally.

# Running the script
In the cloned repository, you can run the code with the Nicosia city graph that had been downloaded from open street maps which takes the graph in the unprocessed folder and puts the processed graph in the processed folder: 
```
main.py()
```

If you want to run the code with your own graph, please exchange the graph in the unprocessed folder. (i/o will change in the near future).

# Dependencies for running locally
* os
* numpy
* networkx
* matplotlib (for visualisation)

# Citations
Aynaud, T. (2008). Louvain Community Detection Github repository. https://github.com/taynaud/python-louvain 

Law, S. (2017). Defining Street-based Local Area and measuring its effect on house price using a hedonic price approach: The case study of Metropolitan London. Cities

Blondel, V. D., Guillaume, J. L., Lambiotte, R., & Lefebvre, E. (2008). Fast unfolding of communities in large networks. Journal of statistical mechanics: theory and experiment, 2008(10), P10008.

# License

The MIT License (MIT)

Copyright (c) 2017-2021, Stephen Law <stephen.law@ucl.ac.uk>

Copyright (c) 2009, Thomas Aynaud <thomas.aynaud@lip6.fr>