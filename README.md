# Atg8a-and-Axoneme-analysis
## Overview
<ins>Atg8a recruitment</ins>: To determine Atg8a recruitment levels to the sperm flagellum, we used an Arivis Vision4D pipeline to analyze the relative volume of Atg8a as a function of the distance from the axoneme, in 0–1-hour AEL embryos immunostained to reveal the axoneme and Atg8a. First, the axoneme was identified using a random forest pixel classifier. False-positive axoneme objects were manually removed. Then, the Atg8a signal was identified using a random forest pixel classifier. To save computation time and avoid background signal, the smallest 40% Atg8a objects were filtered out from each file, such that only 60% of the total Atg8a volume was further analyzed. We verified on a subset of the data that we get the same spatial distribution of the Atg8a objects when analyzing all the objects or just the bigger ones as described. Next, total Atg8a object volume was measured in 10 envelopes of 1 µm thick around the identified axoneme (the first envelope captures Atg8a objects with less than 1 µm distance from the axoneme, the second envelope captures Atg8a objects residing between 1 and 2 µm distance and so on). Then, the normalized Atg8a volume was obtained by dividing the total Atg8a volume within an envelope by the corresponding envelope volume.

<ins>Sperm plasma membrane analysis</ins>: To determine sperm membrane volume, we used an Arivis Vision4D pipeline to analyze the sperm plasma membrane signal in proximity (touching) the axoneme, in 0–1-hour AEL embryos immunostained to reveal the axoneme and the sperm plasma membrane. First, the axoneme was identified using a random forest pixel classifier. False-positive axoneme objects were manually removed. Then, the sperm plasma membrane signal was identified using a random forest pixel classifier. The normalized sperm plasma membrane volume was obtained by dividing the total sperm plasma membrane volume with the corresponding axoneme volume.

<ins>Rubicon vesicles and hCD63 analysis</ins>: To determine the correlation between Rubicon and hCD63 signal within Rubicon vesicles, we used an Arivis Vision4D pipeline, applied on live images of 0–15-minutes AEL embryos, dually expressing Rubicon-EGFP and hCD63-tdTomato. First, Rubicon vesicles were identified using a random forest pixel classifier. Only Objects with a volume between 0.5 µm and 15 µm were considered. hCD63 mean intensity value was determined as follows: First, hCD63 mean intensity signal was measured within each Rubicon vesicle. To evaluate hCD63 background intensity values, two surrounding envelopes were generated around each vesicle. To separate between a vesicle and its background, a first 200 nm thick envelope (within which hCD63 signal was not measured) was generated around the identified vesicle. Then, an additional 300 µm thick envelope was generated. hCD63 background signal was determined as the mean intensity of the third envelopes. Then, to obtain the normalized hCD63 mean intensity value of each vesicle, the total mean intensity values of the background was extracted from each vesicle. Vesicles in which the fluorescent signal was lower compared to the engulfing envelopes signal, were disregarded, and discarded from further analysis. Rubicon vesicles that exhibit hCD63 signal above background were considered hCD63 positive.

<ins>EGFP-hCD63 signal analysis</ins>: To determine the EGFP-hCD63 signal levels on the paternal mitochondrial derivative (MD), we used an Arivis Vision4D pipeline, applied on live images of 0–15-minutes AEL embryos, expressing EGFP-hCD63 and fertilized with red-MD labeled males. First, the MD was identified using a random forest pixel classifier. Then, EGFP-hCD63 mean intensity signal within the MD was measured. To separate between the MD and its background, a first 0.5 µm thick envelope (within which hCD63 signal was not measured) was generated. Then, an additional 1 µm thick envelope was generated, and its mean intensity was considered as background. The EGFP-hCD63 mean intensity of the second envelope was calculated (background) and extracted from the corresponding MD, to get the normalized hCD63 mean intensity value.


## Identifying Axonemes
![fig1](https://github.com/WIS-MICC-CellObservatory/Atg8a-and-Axoneme-analysis/assets/64706090/b76066ce-9ee8-403e-a682-fe6bdda37015)

Fig. 1: Arivis/Pipelines/AxonStringOnly

To Identify the Axoneme within the cell we trained A "Machine Learning Segmenter" (Arivis/Training/rbcn ri2_2022-07-25_11.18.58_F11 Axoneme training.training).
We then, filtered out small roundish identified objects using the Feature filter operation.
At this point we stored the resulting objects as Axoneme Strings and enabled the user to manually rule out some of them by visualizing them.

## Identifying Atg8a and calculating Distances
![fig2](https://github.com/WIS-MICC-CellObservatory/Atg8a-and-Axoneme-analysis/assets/64706090/d2847a84-3e4c-44c7-a5f8-93749bb79094)

Fig. 2: Arivis/Pipelines/AxonStringOnly FullArivisDistance - import Axoneme object - volume python script - ri1 F00.zpipeline

To Identify the Atg8a within the cell we trained A "Machine Learning Segmenter" (Arivis/Training/rbcn ri2_2022-07-25_11.18.58_F11 Atg8a training.training).
For performance , we then filtered out small identified objects that account for 40% of the total volume leaving the bigger objects that account for the remaining 60% of the total volume. To do that we used a python script operation (Arivis/Python Script/FilterLowPercent.py)

We then, calculated the distance between each of the identified Atg8a objects to the closest Axoneme segment using the Distance operation.
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

## Identifying touching axoneme's membrane
![SpermMembranePipeline](https://github.com/WIS-MICC-CellObservatory/Atg8a-and-Axoneme-analysis/assets/64706090/0b54fdd6-b32e-4eb7-9493-f3b2ce51405d)

Fig. 3: Arivis/Pipelines/Identify sperm membrane Pipeline.pipeline

To Identify the sperm's membrane within the cell we trained A "Machine Learning Segmenter" (Arivis/Training/rubicon ri x dj CPV_2024-01-24_11.59.38_F00 Sperm membrane training.training) and then filtered those of volume less than 1 µm<sup>3</sup>. 
We then, identified the touching membrane by looking at the distance between the membrane and the sperm surfaces.

## Rubicon vesicles and hCD63 analysis
![VesiclePipeline](https://github.com/WIS-MICC-CellObservatory/Atg8a-and-Axoneme-analysis/assets/64706090/685425ab-5006-4850-970d-fda500705a2e)

Fig. 4: Arivis/Pipelines/Vesicle analysis.pipeline

To Identify the Rubicon vesicles we trained A "Machine Learning Segmenter" (Arivis/Training/Vesicle Training.training) and then filtered those of volume less than 1 µm<sup>3</sup>, and then filtered those of volume less than 0.5 µm<sup>3</sup> or more than 15 µm<sup>3</sup>. To Create the rings around each vesicle, we dilated them by 2 and 5 pixels. in each ring we extracted the hCD63 mean intensity.

## EGFP-hCD63 signal analysis
![MitochondriaPipeline](https://github.com/WIS-MICC-CellObservatory/Atg8a-and-Axoneme-analysis/assets/64706090/8a4d1dc4-4ea8-43b5-b721-3cd8c9145b7c)

Fig. 5: Arivis/Pipelines/Mitochondria analysis new names.pipeline

To Identify the Mitochondria we trained A "Machine Learning Segmenter" (Arivis/Training/MitochondriaTraining.training). To Create the rings around it, we dilated them by 5 and 10 pixels. in each ring we extracted the EGFP-hCD63 mean intensity.
