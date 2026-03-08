# AI Algorithms Implementation (A*, A-Priori, Genetic Algorithm)

# 1. A* Search Algorithm

## Example: Mountain Hiking Route (Energy Optimization)

In this example, the algorithm simulates a **hiker finding the most energy-efficient path through a mountain terrain grid**.

Each cell in the grid represents terrain with a different energy cost. The algorithm searches for the path that minimizes total energy consumption from the starting point to the destination.

### Terain Legend
| Terrain     | Symbol | Energy Cost |
| ----------- | ------ | ----------- |
| Start       | S      | 1           |
| Goal        | G      | 1           |
| Flat ground | .      | 1           |
| Uphill      | ^      | 4           |
| Downhill    | v      | 2           |
| Rock        | #      | blocked     |

### Objective

Find the **best hiking route from the starting point to the summit** while minimizing energy usage.

### Screenshot of the output

![A\* Hiking Route Output](screenshots%20of%20outputs/aStar.png)

---

# 2. A-Priori Algorithm

## Example: Study Material Recommendation

In this example, the algorithm analyzes study materials used by students to determine **which subjects are commonly studied together**.

This can help build a **study recommendation system** that suggests learning resources based on patterns found in student study habits.

### Objective

Identify **frequent combinations of study materials** and recommend related topics.

### Example Dataset

Example student study sets: (example 1)

```
Student 1: Python, Data Structures, Algorithms
Student 2: Python, Machine Learning
Student 3: Python, Data Structures
Student 4: Data Structures, Algorithms
Student 5: Python, Algorithms
```

Example student study sets: (example 2)

```
Student 1: AI, Python, Machine Learning
Student 2: Python, Data Science
Student 3: AI, Machine Learning
Student 4: Python, Machine Learning
Student 5: AI, Python
```
### Screenshot of the output

![A-Priori Output](screenshots%20of%20outputs/aPriori.png)

---

# 3. Genetic Algorithm

## Example: Designing the Best Workout Plan

In this example, the algorithm searches for the **best workout plan by selecting the most effective combination of exercises**.

### Objective

Generate the **best 3-exercise workout routine** that maximizes fitness effectiveness based on a scoring system.

### Screenshot of the output

![Genetic Algorithm Output](screenshots%20of%20outputs/evolution.png)
