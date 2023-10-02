# NLP - Embedding Dimensionality Reduction Approaches
Project repository of our group, NLP course @ University of Bonn

## Members
- Arwah Jawwad
- Behnam Fanitabasi
- Behzad Shomali
- Mahnaz Mirhaj
- Sven Knauer

## Project Outline
- [project_outline](https://github.com/s-knauer/nlp-edra/tree/main/project_outline)

## Dataset
In order to compare the results of the language models with compressed embeddings we train them to perform a downstream task such as classification on different datasets. For this, we will be using the following three classification datasets to compare the results ([datasets](https://github.com/s-knauer/nlp-edra/tree/main/datasets)):
- **Dataset: CheckThat Lab - Subjectivity Detection:**
    - The task is to predict whether a given sentence from a news article is subjective or objective.
    - The train/dev/test set contains 830/219/244 sentences
    - The data contains binary labels `SUBJ` or `OBJ`

- **Dataset: Aspect Sentiment Classification Dataset:**
    - The aim is to classify the sentiment toward each sentence as positive, negative, or neutral given the aspect and the review sentence.
    - The dataset is divided into train test and dev sets. Each entity has a classification label, `polarity` having the values positive, negative, or neutral.

- **Dataset: FEVER (Fact Extraction and VERification):**
    - The task is to predict whether a given claim is supported or refuted by verifying the facts or whether `notEnoughInfo` is present to make a decision.
    - The dataset consists of 185,445 sentences.
    - The claims are classified as `Supported`, `Refuted`, or `NotEnoughInfo`. 

- _The [embeddings](https://github.com/s-knauer/nlp-edra/tree/main/SBERT) are calculated using [SBERT](https://www.sbert.net/)._ 

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
- [Final Report](https://github.com/s-knauer/nlp-edra/tree/main/Problem_Solving)
