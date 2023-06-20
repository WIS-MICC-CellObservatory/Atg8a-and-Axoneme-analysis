# Agt8-and-Axon-analysis
We use Arivis pipeline to analyze the distance between agt8 and the Axon
## Overview
We first identified Axon objects using a random forest training algorithm. Then we filtered small roundish objects that were erroneously identified as Axon segments as to be left with the main 1-2 Axon segments in each cell. 

We also used a random forest training algorithm to identify the Agt8 in the cell. To save computation time, we filtered out small Agt8 objects as to be left out with the ones that account for 60% of the total volume (we verified on few files that the smaller objects did not have a different distribution in the cell). 

Once the two types of objects were identified, we measured the combined volume of Agt8 objects in 10 envelopes of 1 micron thick around the Axon (where the 1st envelope captured the Agt8 objects residing no further than 1 micron from the Axon, the 2nd envelope captured the Agt8 objects residing between 1 and 2 microns and so on). We divided these combined volumes by the corresponding envelope volume to get the normalized Agt8 volume  

## Identifying Axons
Fig. 1: Arivis/Pipelines/AxonStringOnly

![fig1](https://github.com/WIS-MICC-CellObservatory/Agt8-and-Axon-analysis/assets/64706090/c88c8ccb-c872-4a2a-9a04-df351452a3c3)

To Identify the Axon within the cell we trained A "Machine Learning Segmenter" (Arivis/Training/rbcn ri2_2022-07-25_11.18.58_F11 Axon training.training).
We then filtered out small roundish identified objects using the Feature filter operation.
At this point we stored the resulting objects as Axon Strings and enabled the user to manualy rule out some of them by visualizing them.

## Identifying Agt8 and calculating Distances
Fig. 2: Arivis/Pipelines/AxonStringOnly FullArivisDistance - import Axon object - volume python script - ri1 F00.zpipeline

![fig2](https://github.com/WIS-MICC-CellObservatory/Agt8-and-Axon-analysis/assets/64706090/5cb83392-9453-4fc7-a76b-cd6fa61f0254)

To Identify the Agt8 within the cell we trained A "Machine Learning Segmenter" (Arivis/Training/rbcn ri2_2022-07-25_11.18.58_F11 Agt8 training.training).
We then filtered out small roundish identified objects using the Feature filter operation.
At this point we stored the resulting objects as Axon Strings and enabled the user to manualy rule out some of them by visualizing them.
