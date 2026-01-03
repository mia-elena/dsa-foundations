# DSA Foundations in Python

> 8-Week DSA Mastery Plan using Goodrich, Tamassia & Goldwasser

## Overview

**Timeline**: 8 weeks (January 1, 2026 - February 26, 2026)
**Daily Budget**: 2.5 hours
**Goal**: Solve medium LeetCode problems confidently for software engineering interviews

### Resources
- **Textbook**: "Data Structures and Algorithms in Python" by Goodrich, Tamassia & Goldwasser
- **NeetCode 150**: neetcode.io/practice
- **CodePath TIP2025**: Units 1-12

### Daily Minimum (Non-Negotiable)
> 1-2 NeetCode problems + 30 minutes textbook reading each day

---

## Phase 1: The Building Blocks (Weeks 1-2)

*Focus: Understanding memory, complexity, and basic logic.*

### Week 1: Analysis & Python Mechanics

**Book:** Chapters 1 (Review) & 3 (Algorithm Analysis)

**Why:** You must understand **Big-O** to pass a technical interview. If you solve a problem but can't explain why it's O(n), it's often a "fail."

**Key Tasks:**
- Implement the Big-O examples in Ch 3
- Start NeetCode "Arrays & Hashing" (Easies)

**Repo Goal:** Create notes in `/01-complexity-analysis` on time/space tradeoffs.

---

### Week 2: Recursion & Dynamic Arrays

**Book:** Chapters 4 (Recursion) & 5 (Array-Based Sequences)

**Why:** Chapter 5 explains how Python lists grow. This is vital for "String" and "Array" problems.

**Key Tasks:**
- Implement **Binary Search** (Recursive vs Iterative)
- Solve NeetCode "Two Pointers" (Easies)

**Repo Goal:** `/02-recursion/binary_search.py` and `/03-arrays-strings/dynamic_array_impl.py`

---

## Phase 2: Linear Data Structures (Weeks 3-4)

*Focus: Mastering the flow of data.*

### Week 3: Linked Lists

**Book:** Chapter 7 (Linked Lists)

**Why:** This is the #1 topic where "Intermediate" learners struggle because of pointers.

**Key Tasks:**
- Implement a **Singly Linked List** from scratch
- Implement a **Doubly Linked List** from scratch
- Solve NeetCode "Linked List" (Easies/Mediums)

**Repo Goal:** `/04-linked-lists/singly_linked.py` and `/04-linked-lists/doubly_linked.py`

---

### Week 4: Stacks, Queues, and Deques

**Book:** Chapter 6

**Why:** Stacks are the secret to solving many "Medium" string and tree problems (like Valid Parentheses).

**Key Tasks:**
- Implement a Stack using a List
- Solve NeetCode "Stack" section

**Repo Goal:** `/05-stacks-queues/stack.py` and `/05-stacks-queues/eval_rpn.py` (Reverse Polish Notation)

---

## Phase 3: Nonlinear Data Structures (Weeks 5-6)

*Focus: This is where most "Medium" problems live.*

### Week 5: Binary Trees & BSTs

**Book:** Chapter 8 (Trees)

**Why:** Trees are the bread and butter of technical interviews.

**Key Tasks:**
- Implement **DFS** (Pre-order, In-order, Post-order)
- Implement **BFS** (Level-order)
- Solve NeetCode "Trees" (Start with Easies)

**Repo Goal:** `/06-trees-and-bst/traversals.py` and `/06-trees-and-bst/bst.py`

---

### Week 6: Heaps & Priority Queues

**Book:** Chapter 9

**Why:** Heaps solve "Top K" problems (e.g., "Find the top 5 most frequent elements").

**Key Tasks:**
- Understand the "Array representation of a Heap"
- Implement a Min Heap from scratch
- Solve NeetCode "Heap / Priority Queue"

**Repo Goal:** `/07-heaps-priority-queues/min_heap.py`

---

## Phase 4: Optimization & Graphs (Weeks 7-8)

*Focus: The "Final Boss" of most interviews.*

### Week 7: Hash Tables & Maps

**Book:** Chapter 10 (Maps, Hash Tables, and Skip Lists)

**Why:** This explains why `dict` is so fast in Python.

**Key Tasks:**
- Learn about **Collisions** and **Hashing functions**
- Implement a basic Hash Map
- Go back and crush the "Medium" problems in NeetCode "Arrays & Hashing"

**Repo Goal:** `/08-hashing-maps/hash_map.py`

---

### Week 8: Graph Algorithms (BFS/DFS)

**Book:** Chapter 14

**Why:** Modern interviews love Graphs (social networks, maps, etc.).

**Key Tasks:**
- Implement an **Adjacency List**
- Learn **BFS** (Queue-based) and **DFS** (Stack/Recursive)
- Solve NeetCode "Graphs"

**Repo Goal:** `/09-graphs/adjacency_list.py` and `/09-graphs/bfs_dfs.py`

---

## Repository Structure

```
/dsa-foundations
  /01-complexity-analysis    # Week 1: Big-O notes and examples
  /02-recursion              # Week 2: Binary search, recursion patterns
  /03-arrays-strings         # Week 2: Dynamic arrays, two pointers
  /04-linked-lists           # Week 3: Singly/Doubly linked lists
  /05-stacks-queues          # Week 4: Stack, Queue, Deque implementations
  /06-trees-and-bst          # Week 5: Tree traversals, BST operations
  /07-heaps-priority-queues  # Week 6: Heap implementation
  /08-hashing-maps           # Week 7: Hash map implementation
  /09-graphs                 # Week 8: Graph representations, BFS/DFS
  /solutions                 # LeetCode/NeetCode solutions
```

---

## Progress Tracking

| Week | Phase | Book Chapters | NeetCode Section | Status |
|------|-------|---------------|------------------|--------|
| 1 | Building Blocks | Ch 1, 3 | Arrays & Hashing (Easy) | |
| 2 | Building Blocks | Ch 4, 5 | Two Pointers (Easy) | |
| 3 | Linear DS | Ch 7 | Linked List | |
| 4 | Linear DS | Ch 6 | Stack | |
| 5 | Nonlinear DS | Ch 8 | Trees | |
| 6 | Nonlinear DS | Ch 9 | Heap / Priority Queue | |
| 7 | Optimization | Ch 10 | Arrays & Hashing (Medium) | |
| 8 | Graphs | Ch 14 | Graphs | |

---

## Getting Started

1. Read this plan
2. Start Week 1: Open Chapter 1 of Goodrich textbook
3. Solve first NeetCode problem: Contains Duplicate (LC 217)
4. Create your first file in `/01-complexity-analysis`

**Start January 1st. One chapter, one problem at a time.**
