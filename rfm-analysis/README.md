# RFM Analysis, Step by Step: End Customers (Part 1)

Code for the aimldl.io post "All Customers Are Equal, But Some Are More Equal Than Others: RFM, Step by Step".

## What's inside
- `RFM_Analysis_End_Customers.ipynb`: data prep, R/F/M scoring, the 125-cell ranking and 11 named segments, three composite scores (simple sum, business-set weights, AHP), five tiers, validation, profiling and charts.
- `charts/`: RF heatmap, segment sizes, Pareto curve.

## Data
UCI Online Retail II (2009–2011), merged and cleaned: https://www.kaggle.com/datasets/krjynt/online-retail-ii-2009-2011-merged
Licence CC BY 4.0. Credit: Chen, D. (2012), UCI ML Repository, doi 10.24432/C5CG6D.
The notebook pulls the data with kagglehub. To use your own copy, change the path in the data cell.

## Read the post
[aimldl.io](https://aimldl.io/2026/10/24/all-customers-are-equal-but-some-are-more-equal-than-others-rfm-step-by-step/)

Part 2 (dealers) coming next.
