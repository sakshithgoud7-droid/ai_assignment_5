AI LAB ASSIGNMENT DOCUMENTATION

Table of Contents

1. Tic-Tac-Toe using AI Search Algorithms
2. Travel Planner System
3. Knowledge Graph using Python
4. Bayesian Network for Traffic Prediction
5. Software Requirements
6. Installation Steps
7. Program Execution
8. Expected Outputs
9. Conclusion

---

1. Tic-Tac-Toe using AI Search Algorithms

Objective

The aim of this project is to implement various Artificial Intelligence search techniques and compare their behavior in a Tic-Tac-Toe game environment.

The game allows the AI to select moves using different search strategies and evaluate possible future outcomes.

Algorithms Implemented

• Minimax Algorithm

Minimax is a game-search algorithm used in two-player games. It assumes that both players play optimally and selects the move that produces the best possible outcome for the AI player.

• Alpha-Beta Pruning

Alpha-Beta Pruning is an optimization of the Minimax algorithm. It reduces the number of nodes explored by eliminating branches that cannot influence the final decision.

• Heuristic Search

Instead of searching the complete game tree, a heuristic evaluation function is used to estimate the quality of a board position. This improves performance for deeper searches.

• Monte Carlo Tree Search (MCTS)

MCTS performs multiple random simulations from a given game state and chooses the move with the highest success rate based on those simulations.

Features

• Tic-Tac-Toe game board
• Move generation
• Winner detection
• Intelligent move selection
• Game state evaluation
• Simulation-based search

---

2. Travel Planner System

Objective

The purpose of this project is to develop a simple travel recommendation system that suggests destinations according to a user's budget and travel interests.

The system stores information about different tourist destinations and recommends suitable locations based on user requirements.

Destinations Included

• Goa
• Manali
• Jaipur

Features

• Budget-based recommendations
• Interest matching
• Tourist destination details
• Food recommendations
• Suggested travel duration

Information Stored

For every destination, the system maintains:

• Place type
• Estimated cost
• Popular foods
• Recommended number of travel days

Working

The user enters:

• Travel budget
• Interest category

The program compares user preferences with stored data and recommends matching destinations.

---

3. Knowledge Graph using Python

Objective

The objective of this project is to demonstrate knowledge representation using a graph structure.

Artificial Intelligence-related concepts are represented as nodes, while their relationships are represented as edges.

Libraries Used

• NetworkX
• Matplotlib

Concepts Represented

• Python
• Artificial Intelligence
• Machine Learning
• Deep Learning
• Data Science

Relationships

• Python → AI
• Python → Data Science
• AI → Machine Learning
• Machine Learning → Deep Learning

Features

• Node creation
• Relationship creation
• Graph visualization
• Concept representation

---

4. Bayesian Network for Traffic Prediction

Objective

The purpose of this project is to demonstrate probabilistic reasoning using Bayesian Networks.

The model predicts traffic conditions based on weather and accident information.

Variables Used

• Rain
• Accident
• Traffic

Model Structure

Rain ──► Traffic

Accident ──► Traffic

Features

• Bayesian Network construction
• Conditional Probability Distribution (CPD) definition
• Model validation
• Probabilistic inference
• Traffic prediction

Inference Performed

The system calculates the probability of traffic conditions when evidence about rainfall is provided.

Example

Evidence:
Rain = True

Query:
Probability distribution of Traffic

---

5. Software Requirements

Python Version

Python 3.10 or above

Required Libraries

pip install networkx

pip install matplotlib

pip install pgmpy

---

6. Installation Steps

7. Install Python.

8. Download the project files.

9. Install all required libraries.

10. Open a terminal or command prompt.

11. Navigate to the project folder.

12. Run the required Python file.

---

7. Program Execution

Run Tic-Tac-Toe AI

python tic_tac_toe.py

Run Travel Planner

python travel_planner.py

Run Knowledge Graph

python knowledge_graph.py

Run Bayesian Network

python bayesian_network.py

---

8. Expected Outputs

Tic-Tac-Toe Program

• Current board display
• Minimax evaluation score
• Alpha-Beta evaluation score
• Heuristic search evaluation
• Best move suggested by MCTS

Travel Planner Program

• Recommended destinations
• Travel cost information
• Food suggestions
• Recommended trip duration

Knowledge Graph Program

• Display of graph nodes
• Display of graph relationships
• Graph visualization window

Bayesian Network Program

• Model validation result
• Probability distribution for traffic prediction

---

9. Conclusion

This assignment demonstrates several fundamental Artificial Intelligence techniques through practical implementations.

The Tic-Tac-Toe project illustrates game-playing AI using Minimax, Alpha-Beta Pruning, Heuristic Search, and Monte Carlo Tree Search. The Travel Planner demonstrates simple recommendation-based decision making. The Knowledge Graph shows how concepts and relationships can be represented graphically, while the Bayesian Network demonstrates probabilistic reasoning under uncertainty.

Together, these programs provide hands-on experience with important AI concepts including search, optimization, recommendation systems, knowledge representation, and probabilistic inference.
