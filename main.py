import os
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
#from community_func 
import community_louvain as community

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)


# make folder
oldpath='unprocessed/edges.shp'
if not os.path.exists(oldpath):
    print ('graph must be in the following folder "unprocessed/edges.shp" to process')
    
    
# load the graph
G=nx.read_shp('unprocessed/edges.shp')
DG=nx.to_undirected(G)
DG2=nx.line_graph(DG)

# run modularity on the dual graph
def community_modularity(DG):
    dendo = community.generate_dendrogram(DG)
    for i in np.arange(0,len(dendo),1):
        partition=community.partition_at_level(dendo, i)
        nx.set_edge_attributes(DG,dict(partition),'mod_'+str(i))
    return dendo

communities=community_modularity(DG2)

# make folder
newpath='processed'
if not os.path.exists(newpath):
    os.makedirs(newpath)
    print ('processed folder created')

# visualise the processed maps
pos={}
for k,v in enumerate(DG.nodes()):
    pos[v]=v
    
for i in np.arange(0,len(communities),1):
    fig,ax=plt.subplots(figsize=(10,10))
    colors=list(nx.get_edge_attributes(DG,'mod_'+str(i)).values())
    nx.draw_networkx(DG,pos,with_labels=False,node_size=0,edge_color=colors,cmap=plt.cm.Pastel2)
    filepath=newpath+'/'+'partition_'+str(i)+'.png'
    plt.savefig(filepath)

# clear graph
#ttrib_list=['Json','Wkb','Wkt','from','to','key']
for (n1, n2, d) in DG.edges(data=True):
    for att in list(d):
        if 'mod_' not in att: 
            d.pop(att, None)
    #for att in attrib_list:
        #d.pop(att,None)
    #for att in list(d):
        #if 'mod_' not in att: #or 'id' not in att:
            #d.pop(att, None)
    #d.clear()
    
# save the processed map
nx.write_shp(DG,newpath+'/')
print ('finished')

#def main():
#    result = do_stuff()
#    return result

#if __name__ == "__main__":
#    main()

# calculate modularity at the district level


# 