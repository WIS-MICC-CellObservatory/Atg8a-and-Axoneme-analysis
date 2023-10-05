# Atg8a-and-Axoneme-analysis
We use Arivis pipeline to analyze the distance between Atg8a and the Axoneme
## Overview
We first identified Axoneme objects using a random forest training algorithm. Then we filtered small roundish objects that were erroneously identified as Axoneme segments as to be left with the main 1-2 Axoneme segments in each cell. 

We also used a random forest training algorithm to identify the Atg8a in the cell. To save computation time, we filtered out small Atg8a objects as to be left out with the ones that account for 60% of the total volume (we verified on few files that the smaller objects did not have a different distribution in the cell). 

Once the two types of objects were identified, we measured the combined volume of Atg8a objects in 10 envelopes of 1 micron thick around the Axoneme (where the 1st envelope captured the Atg8a objects residing no further than 1 micron from the Axoneme, the 2nd envelope captured the Atg8a objects residing between 1 and 2 microns and so on). We divided these combined volumes by the corresponding envelope volume to get the normalized Atg8a volume  

## Identifying Axonemes
<p align="center">

![fig1](https://github.com/WIS-MICC-CellObservatory/Atg8a-and-Axoneme-analysis/assets/64706090/d7ac4e07-017a-4095-a921-8f1b8160883a)

Fig. 1: Arivis/Pipelines/AxonStringOnly
</p>

To Identify the Axoneme within the cell we trained A "Machine Learning Segmenter" (Arivis/Training/rbcn ri2_2022-07-25_11.18.58_F11 Axoneme training.training).
We then filtered out small roundish identified objects using the Feature filter operation.
At this point we stored the resulting objects as Axoneme Strings and enabled the user to manually rule out some of them by visualizing them.

## Identifying Atg8a and calculating Distances

<p align="center">
![fig2](https://github.com/WIS-MICC-CellObservatory/Atg8a-and-Axoneme-analysis/assets/64706090/d2847a84-3e4c-44c7-a5f8-93749bb79094)

Fig. 2: Arivis/Pipelines/AxonStringOnly FullArivisDistance - import Axoneme object - volume python script - ri1 F00.zpipeline
</p>

To Identify the Atg8a within the cell we trained A "Machine Learning Segmenter" (Arivis/Training/rbcn ri2_2022-07-25_11.18.58_F11 Atg8a training.training).
For performance , we then filtered out small identified objects that account for 40% of the total volume leaving the bigger objects that account for the remaining 60% of the total volume. To do that we used a python script operation (Arivis/Python Script/FilterLowPercent.py)

Now we calculated the distance between each of the identified Atg8a objects to the closest Axoneme segment using the Distance operation.
The pipeline continued to calculate the volume of the Axoneme segments as is and also the volume of the Axoneme segments once dilated by 10,20,...100 pixels. We used these volumes to calculate the relative volume Atg8a objects occupied in growing distance from the Axonemes (See next Section)

## Calculating relative Atg8a Volumes
We used an Excel spreadsheet template (Excel/distance analysis.xlsx) to calculate the amount of Atg8a total volumes at growing distances from the Axoneme:
1. We replace the columns A-D in the Excel template with the measurements taken for each Atg8a object (id, name, volume and distance from Axoneme).
2. We replace column J (inflated string volume) with the measurements taken for each of the dilated Axoneme objects (in case there were more than one Axon segment, we summed all segments of the same dilation)
3. The template automatically calculates:
>1. Column F: The total volume of Atg8a objects at 10, 20... 100 pixels distances from the Axoneme (Column E translates pixels to microns)
>2. Column G: The number of Atg8a objects at 10, 20... 100 pixels distances from the >1. Column F: The total volume of Atg8a objects at 10, 20... 100 pixels distances from the Axoneme (Column E translates pixels to microns)
>3. Column H: The average size of objects at 10, 20... 100 pixels distances from the >1. Column F: The total volume of Atg8a objects at 10, 20... 100 pixels distances from the Axoneme (Column E translates pixels to microns)
>4. Column I: The ratio between the volume of the dilated >1. Column F: The total volume of Atg8a objects at 10, 20... 100 pixels distances from the Axoneme (Column E translates pixels to microns) volume and the related Atg8a objects



