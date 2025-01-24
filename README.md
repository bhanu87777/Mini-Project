Social Network Analysis Based on GraphSAGE

Project Overview:
This project focuses on analyzing social networks using GraphSAGE, a graph neural network model. By leveraging GraphSAGE, the project aims to classify nodes (users) in a 
social network by utilizing both structural and attribute information of the network. The methodology compares GraphSAGE's performance with traditional techniques, 
introduces improvements in model sampling, and demonstrates its effectiveness through experiments.

Goals of the Project:
1. To predict and classify user nodes in a social network based on their relationships and attributes.
2. To explore and enhance the GraphSAGE model for improved social network analysis.
3. To compare the performance of GraphSAGE with traditional methods like Logistic Regression and DeepWalk.

Development Process:
1. Data Collection and Preprocessing:
a. Collected user information and interaction data (e.g., followers, followees, retweets, comments, likes) from Sina Weibo.
b. Processed raw data into adjacency tables and feature matrices for graph-based analysis.

2. Model Development:
a. Implemented the GraphSAGE model with improvements in the sampling process to handle varying node adjacency sizes.
b. Used three types of aggregation functions: Mean, Pool, and LSTM, to extract and combine node and neighbor features.

3. Evaluation:
a. Compared the performance of GraphSAGE against traditional methods on a social network dataset.
b. Assessed the impact of different parameters, such as sampling depth and quantity, on model performance.

Key Features:
1. GraphSAGE Model:
a. Utilizes message propagation and aggregation to extract high-level node features.
b. Effectively integrates node attribute and structural information.

2. Sampling Optimization:
Introduced a dynamic sampling strategy based on adjacency size for improved classification.

3. Performance Comparison:
a. Benchmarked GraphSAGE against Logistic Regression and DeepWalk models.
b. Achieved higher accuracy in node classification.

4. Parameter Tuning:
Experimented with different sampling depths and quantities to optimize performance.

Results:
GraphSAGE achieved an accuracy of 53.87%, outperforming Logistic Regression (42.5%) and DeepWalk (32.12%) on the dataset.
Dynamic sampling further improved accuracy to 54.13%.
Technologies and Skills Used
Graph Neural Networks (GNNs): Implemented GraphSAGE for inductive representation learning.
Python: For data preprocessing, model implementation, and evaluation.
PyTorch/TensorFlow: Used for building and training the neural network.
Social Network Data Analysis: Processed real-world social media data to create graph representations.
