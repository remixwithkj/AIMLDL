# Don't Guess: Let Customer Behaviour Decide Your Segments (Part 3)

Code for the aimldl.io post "Segment Sharply, Target Effectively, Unearth Insights and Maximise ROI: Don't Guess, Let Customer Behaviour Find Your Segments".

Parts 1 and 2 segmented customers and trade partners with rules. Part 3 lets the data form the groups: unsupervised clustering on mixed data (numbers and categories side by side) with k-prototypes, then turns the clusters into named personas with actions.

## What's inside
- `Unsupervised_Clustering_mixed_datatypes.ipynb`: settings, input check, scaling, choosing the number of clusters, the final k-prototypes model, cluster profiles (with an index heatmap), a spend vs age view and the export.
- `customer_clustered_segments.csv`: the output, one row per customer with its cluster number and the columns used.
- `charts/`: the elbow curve, spend vs age by cluster, the persona table, the three kinds of customer data, and the path from RFM to clustering.

## Data
[Customer Personality: Clean Data for Segmentation](https://www.kaggle.com/datasets/krjynt/customer-personality-clean-data-for-segmentation): 2,240 customers of a food and wine retailer, 17 numeric and 9 categorical columns, cleaned and imputed from [Customer Personality Analysis](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis). Licence CC0: Public Domain. Used as an illustration of the approach, not as evidence.
The notebook pulls the data with kagglehub.

## Run it on your own data
- `pip install pandas numpy matplotlib scikit-learn kmodes kagglehub`, then run all cells (Colab, Kaggle or locally).
- One row per customer, no missing values. Point `DATA_PATH` at your CSV and list your ID, numeric and categorical columns in the **Settings** cell. Nothing else needs changing.
- The input check stops with a plain-language message if a listed column is missing, has blanks or holds the wrong type.
- Pick the number of clusters from the elbow chart **and** the business test: can your team name each cluster and act on it differently?

## Read the post
[aimldl.io](https://aimldl.io/2026/11/09/dont-guess-let-customer-behaviour-find-your-segments/) · Kaggle notebook: [link](https://www.kaggle.com/code/krjynt/let-customer-behaviour-decide-your-segments)

Earlier in the series: Part 1, end customers: [code](../rfm-analysis) · [post](https://aimldl.io/2026/10/24/all-customers-are-equal-but-some-are-more-equal-than-others-rfm-step-by-step/) · Part 2, trade partners: [code](../rfm-b2b-trade-partners) · [post](https://aimldl.io/2026/11/01/rfm-b2-rfm-for-trade-partners/)
