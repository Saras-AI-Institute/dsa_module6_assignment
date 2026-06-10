# Module 6 Lab: LogiMax E-Commerce Optimization Engine

## 🎯 Objective & Overview
Welcome to the final lab! In this assignment, you will build **LogiMax**, an optimization engine designed to streamline e-commerce fulfillment operations. This lab tests your practical understanding of **Section 1 (Brute-Force)**, **Section 2 (Divide and Conquer)**, and **Section 4 (Dynamic Programming)**.

Instead of writing algorithms in isolation, you will observe how matching the right paradigm to the right problem scale prevents system crashes and optimizes corporate revenue.

---

## 📁 Repository Map

* **`paradigms/brute_force.py`**: Implementation file for exhausting small combinatoric solution spaces.
* **`paradigms/divide_conquer.py`**: Implementation file for log-linear data division and combination.
* **`paradigms/dynamic_programming.py`**: Implementation file for solving overlapping subproblems using memoization/tabulation.
* **`test_paradigms.py`**: The `pytest` script containing automated verification metrics.

---

## 🚀 System Components to Complete

### Task 1: High-Security Vault Pairing (`paradigms/brute_force.py`)
* **The Scenario:** A delivery van must carry exactly two high-value target items whose combined valuation equals a specific target threshold.
* **The Task:** Implement a Brute-Force algorithm that checks every single unique pair combination in the inventory list ($O(n^2)$) to find the correct indices. 

### Task 2: Mass Manifest Splitting (`paradigms/divide_conquer.py`)
* **The Scenario:** Before cargo can be loaded, tens of thousands of shipping manifest IDs must be sorted. Standard loops take too long.
* **The Task:** Implement an optimized Divide and Conquer sorting strategy (like Merge Sort). You must recursively divide the unsorted array into halves, solve the subproblems, and merge the sorted pieces back together in $O(n \log n)$ time.

### Task 3: The Cargo Truck Max-Value Loader (`paradigms/dynamic_programming.py`)
* **The Scenario:** You have a delivery truck with a strict weight capacity limitation. You are handed a list of packages, each with a specific weight and financial value. You want to load the truck to get the absolute maximum profit without exceeding the weight cap.
* **The Problem:** A brute-force approach ($O(2^n)$) will lock up the server if you have more than 30 packages.
* **The Task:** Implement a Dynamic Programming solution (0/1 Knapsack) using a 2D table or a memoization array to solve the problem in efficient $O(n \times \text{capacity})$ time.
