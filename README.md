# Search Engine Ranking Simulation Using PageRank Algorithm

## Project Overview

This project demonstrates how search engines rank webpages using the PageRank algorithm. We use concepts from Linear Algebra to represent web pages as matrices and compute their importance based on how they are connected to each other.

The goal of this project is to understand how mathematical concepts like matrices and eigenvectors can be applied to real-world problems such as search engine ranking.

This project was developed as part of the course:
UE24MA241B – Linear Algebra and Its Applications (Mini Project)

---

## Objectives

- Understand how PageRank works
- Apply Linear Algebra concepts to a real-world problem
- Represent data in matrix form
- Compute PageRank using iterative matrix multiplication
- Visualize the ranking results
- Analyze how PageRank converges over iterations

---

## Linear Algebra Concepts Used

- Matrix Representation
- Stochastic Matrix
- Eigenvectors
- Matrix Multiplication
- Convergence
- Graph Representation

---

## Project Workflow

Real-world Data  
↓  
Graph Representation  
↓  
Adjacency Matrix  
↓  
Stochastic Matrix  
↓  
Google Matrix (with Damping Factor)  
↓  
Iterative PageRank Computation  
↓  
Final Page Rankings  
↓  
Visualization and Convergence Plot  

---

## Dataset

The dataset represents a simplified real-world website link structure. Each line shows how one website links to other websites.

Example:

Google -> YouTube Gmail Maps Drive  
YouTube -> Google  
Gmail -> Google Drive  
Maps -> Google  
Drive -> Google Gmail  
Wikipedia -> Google YouTube  
Amazon -> Google YouTube  
Reddit -> Wikipedia YouTube  

---

## Installation

Install the required libraries before running the project:

pip install numpy networkx matplotlib

---

## How to Run

Run the following command from the project folder:

python src/main.py

---

## Output

The program generates:

- PageRank scores (sorted from highest to lowest)
- Graph visualization of the webpages
- Convergence plot showing how ranks stabilize

---

## Example Output

PageRank Results (Highest to Lowest):

1. Google → 0.31  
2. YouTube → 0.21  
3. Wikipedia → 0.14  

---

## Visualizations

The project generates two images:

- pagerank_graph.png — Visual representation of PageRank
- convergence_plot.png — Shows convergence of PageRank over iterations

---

## Team Members

- Vrinda Venugopal M
- Vyshali Aytha
- Vismaya Harish
- Yashita Anand

---

## Features

- Real-world inspired dataset
- Linear algebra based implementation
- PageRank simulation
- Graph visualization
- Convergence analysis
- Clean and readable output

---

## Conclusion

This project shows how Linear Algebra can be applied to real-world problems like search engine ranking. By representing webpages as matrices and using iterative computation, we are able to simulate how search engines determine the importance of webpages.