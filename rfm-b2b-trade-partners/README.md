# RFM-B²: RFM for Trade Partners (B2B), Step by Step (Part 2)

Code for the aimldl.io post "RFM-B²: RFM for Trade Partners, and Why Your Biggest Partner Might not be The "Best One"".

Part 1 scored end customers. Part 2 scores dealers, distributors and trade partners: six measures read through three lenses, 27 cells and nine personas, each with an action on promotion spend, visits and PJP, and incentives.

## What's inside
- `RFM_Analysis_Trade_Partners.ipynb`: data prep, the six measures (Recency, Frequency, Monetary, Wallet share, absolute and % gross margin), 1–5 scoring, the three lenses (Activity, Scale & potential, Profitability), the 27-cell grid, persona mapping, charts and a partner-level table.
- `charts/`: the 27-cell grid by persona, business contribution by persona, the Pareto view, and revenue vs gross margin.

## Data
Microsoft AdventureWorks reseller sales (fictional bike manufacturer, 701 resellers), three tables merged and cleaned: https://www.kaggle.com/datasets/krjynt/rfm-for-b2b-reseller-sales-with-schemes
Licence MIT, Copyright (c) Microsoft Corporation. Used as an illustration of the framework, not as evidence.
The notebook pulls the data with kagglehub. To use your own copy, change the path in the data cell.

## Run it
- Kaggle: https://www.kaggle.com/code/krjynt/rfm-b-rfm-for-trade-partners-b2b-step-by-step
- Locally or in Colab: `pip install pandas numpy matplotlib scikit-learn kagglehub`, then run all cells.
- Settings (snapshot date, window, scoring bands, lens cut-offs) are in section 1. They are a starting point: tune them to your ordering cycle, margins and objectives.

## Read the post
[aimldl.io](BLOG_LINK_AFTER_PUBLISHING)

Part 1 (end customers): [code](../rfm-analysis) · [post](https://aimldl.io/2026/10/24/all-customers-are-equal-but-some-are-more-equal-than-others-rfm-step-by-step/)

Next in the series: unsupervised clustering.
