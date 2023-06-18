# Agt8-and-Axon-analysis
We use Arivis pipeline to analyze the distance between agt8 and the Axon
## Overview
We first identified Axon objects using a random forest training algorithm. Then we filtered small roundish objects that were erroneously identified as Axon segments as to be left with the main 1-2 Axon segments in each cell. 

We also used a random forest training algorithm to identify the Agt8 in the cell. To save computation time, we filtered out small Agt8 objects as to be left out with the ones that account for 60% of the total volume (we verified on few files that the smaller objects did not have a different distribution in the cell). 

Once the two types of objects were identified, we measured the combined volume of Agt8 objects in 10 envelopes of 1 micron thick around the Axon (where the 1st envelope captured the Agt8 objects residing no further than 1 micron from the Axon, the 2nd envelope captured the Agt8 objects residing between 1 and 2 microns and so on). We divided these combined volumes by the corresponding envelope volume to get the normalized Agt8 volume  

## Identifying Axons
