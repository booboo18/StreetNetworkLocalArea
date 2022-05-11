# StreetNetworkLocalArea 
This is a basic working repository that contains the script to apply modularity optimisation on the street network dual graph to identify street based local areas (Law 2017). The repository contains code which borrows/adapts from [Python-Louvain](https://github.com/taynaud/python-louvain)  a python implementation for the louvain algorithm (Blondel et al 2008). 

# Setup 
The repository have been tested with the standard install of Anaconda Distribution which is a popular open source Python distribution platform. [Anaconda](https://docs.anaconda.com/anaconda/install/index.html)
After setting up the python environment, clone the repository locally.

# Dependencies for running locally
* os
* numpy
* networkx
* matplotlib (for visualisation)

# Running the script
You can play with the script using the jupyter notebook entitled ```Street based Local Area.ipynb```
The code requires a street network shapefile (*.shp) as input and produces neighbourhood cluster using the Louvain algorithm. The street network of Nicosia can be found in the unprocessed folder. Please replaces this with your own data. For better control of the visualisation, we suggest loading the shapefile into QGIS and plotting the graph. 

This is a working repository so we hope to improve the I/O and the visualisation in the near future.

# Citations
Aynaud, T. (2008). Louvain Community Detection Github repository. https://github.com/taynaud/python-louvain 

Law, S. (2017). Defining Street-based Local Area and measuring its effect on house price using a hedonic price approach: The case study of Metropolitan London. Cities

Blondel, V. D., Guillaume, J. L., Lambiotte, R., & Lefebvre, E. (2008). Fast unfolding of communities in large networks. Journal of statistical mechanics: theory and experiment, 2008(10), P10008.

# License

The MIT License (MIT)

Copyright (c) 2017-2021, Stephen Law <stephen.law@ucl.ac.uk>

Copyright (c) 2009, Thomas Aynaud <thomas.aynaud@lip6.fr>
