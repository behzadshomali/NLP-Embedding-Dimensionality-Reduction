# NLP - Embedding Dimensionality Reduction Approaches
Project repository of group 14, nlp course @ university of bonn

## Members
- Arwah Jawwad
- Behnam Fanitabasi
- Behzad Shomali
- Mahnaz Mirhaj
- Sven Knauer

## Project Outline
- [project_outline](https://github.com/s-knauer/nlp-edra/tree/main/project_outline)

## Dataset
- We use three different [datasets](https://github.com/s-knauer/nlp-edra/tree/main/datasets): [Aspect Sentiment Classification Dataset](https://github.com/akkarimi/BERT-For-ABSA/tree/master/asc) - [CheckThat Lab 2023 - Subjectivity Detection](https://gitlab.com/checkthat_lab) - [FEVER](https://fever.ai/dataset/fever.html)
- The [embeddings](https://github.com/s-knauer/nlp-edra/tree/main/SBERT) are calculated using [SBERT](https://www.sbert.net/). 

## Approach [1](https://github.com/s-knauer/nlp-edra/tree/main/Approach%201)
- Variational Autoencoder

<p align="center" width="100%">
    <img width="40%" src="/Approach%201/vae.jpg"> 
    <figcaption>Architecture of Variational Autoencoder (<a href="https://learnopencv.com/variational-autoencoder-in-tensorflow/">source</a>)</figcaption>
</p>


## Approach [2](https://github.com/s-knauer/nlp-edra/tree/main/Approach%202)
- Traditional Dimensionality Reduction techniques such as PCA, LDA, and t-SNE.

## Approach [3](https://github.com/s-knauer/nlp-edra/tree/main/Approach%203)
- Inspired by: A novel approach for dimension reduction using word embedding: An enhanced text classification approach [Link](https://www.sciencedirect.com/science/article/pii/S2667096822000052) Singh et al., International Journal of Information Management Data Insights
Volume 2, Issue 1, April 2022


## Results and Report
- Experiments are done with ML classifiers such as SVM, MLP, and Random Forest on the three datasets, Naive Bayes, and KNN. F1-Scores, Time Inference, and Memory Consumption Plots: [Result](https://github.com/s-knauer/nlp-edra/tree/main/plots)
- Report: ...
