# Python
# 🐍 Python Learning Journey — Srinivas Barkunta

> From zero Python to FAANG-ready DSA in 90 days.  
> This repo documents my full learning journey — fundamentals, patterns, and problem solving — as I transition from JS/TS to Python and prepare for SDE interviews at MNCs.

---

## 👤 About me

- **Name:** Srinivas Barkunta
- **Location:** Hyderabad, India
- **Background:** BTech IT | Android (Kotlin) | Apache Spark | JS/TS
- **Goal:** Land a paid SDE role at an MNC → transition to AI/ML Engineer
- **LinkedIn:** [linkedin.com/in/srinivasbarkunta-335b85255](https://www.linkedin.com/in/srinivasbarkunta-335b85255)
- **Portfolio:** [barkunta-srinivasprotfolio.netlify.app](https://barkunta-srinivasprotfolio.netlify.app)
- **LeetCode:** [leetcode.com/u/SrinivasBarkunta_2025](https://leetcode.com/u/SrinivasBarkunta_2025)

---

## 🗺️ The plan

This repo follows a 3-phase structure:

| Phase | Duration | Focus |
|-------|----------|-------|
| **Phase 0** | 2 weeks | Python fundamentals — syntax, OOP, data structures, file handling |
| **Phase 1** | 90 days | DSA in Python — 90 sessions, 360 problems, FAANG patterns |
| **Phase 2** | After Phase 1 | AI/ML foundations — applied ML, LLMs, Python for data |

---

## 📁 Repo structure

```
python-learning-journey/
│
├── phase-0-fundamentals/
│   ├── day-01-basics/          # Variables, types, input/output
│   ├── day-02-loops/           # for, while, break, continue
│   ├── day-03-functions/       # def, recursion, scope
│   ├── day-04-lists/           # Lists, tuples, comprehensions
│   ├── day-05-dicts-sets/      # Dicts, sets, nested structures
│   ├── day-06-strings/         # String methods, slicing
│   ├── day-07-mini-project/    # Contact Book CLI app
│   ├── day-08-oop/             # Classes, inheritance, dunder methods
│   ├── day-09-files/           # File I/O, JSON, error handling
│   ├── day-10-arrays-hashmaps/ # DSA pattern 1
│   ├── day-11-two-pointers/    # DSA pattern 2
│   ├── day-12-sliding-window/  # DSA pattern 3
│   ├── day-13-stack/           # DSA pattern 4
│   └── day-14-readiness/       # Final check + first 5 problems
│
├── phase-1-dsa/
│   ├── session-01/             # Arrays & Hashing, Two Pointers, Binary Search
│   ├── session-02/             # Sliding Window, Strings
│   ├── ...
│   └── session-90/             # Design problems
│
├── phase-2-aiml/               # Coming after Phase 1
│   └── README.md
│
└── README.md
```

---

## 🏊 Phase 0 — Python fundamentals (2 weeks)

Learning Python from scratch before the DSA sprint.  
Every day has a folder with practice scripts and notes.

### Week 1 — Language foundations

| Day | Topic | Status |
|-----|-------|--------|
| 1 | Setup, variables, data types, f-strings | ✅ |
| 2 | Conditionals, loops, break/continue | ✅ |
| 3 | Functions, recursion, scope | ⬜ |
| 4 | Lists, tuples, list comprehensions | ⬜ |
| 5 | Dictionaries, sets, nested structures | ⬜ |
| 6 | Strings deep dive, palindrome, anagram | ⬜ |
| 7 | Revision + Contact Book CLI mini project | ⬜ |

### Week 2 — OOP + DSA patterns

| Day | Topic | Status |
|-----|-------|--------|
| 8 | OOP — classes, inheritance, dunder methods | ⬜ |
| 9 | File handling, JSON, error handling | ⬜ |
| 10 | DSA Pattern 1 — arrays + hashmaps | ⬜ |
| 11 | DSA Pattern 2 — two pointers | ⬜ |
| 12 | DSA Pattern 3 — sliding window | ⬜ |
| 13 | DSA Pattern 4 — stack + recursion | ⬜ |
| 14 | Readiness check — first 5 problems from the 90-day list | ⬜ |

> Update ⬜ to ✅ as each day is completed.

---

## ⚔️ Phase 1 — DSA sprint (90 days)

90 sessions. 360 problems. All in Python.  
Every session has 1 Medium + 3 Hard problems covering one DSA topic cluster.

### Core patterns covered

| Pattern | Sessions |
|---------|----------|
| Arrays, Hashing, Sliding Window | 1–10 |
| Binary Search, Linked List, Heap, Design | 11–20 |
| Stack, BST, Tree operations | 21–30 |
| Graphs, BFS, UnionFind, Tree traversal | 31–40 |
| LCA, BST validation, Backtracking | 41–52 |
| Graph DFS, Topological sort, Dijkstra | 53–60 |
| DP foundations — Coin, LIS, LCS, Palindrome | 61–70 |
| Interval DP, Greedy, Heap | 71–80 |
| Segment Tree, Trie, System Design problems | 81–90 |

### Problem solving protocol

1. Read the problem — think for 10 minutes without writing code
2. Identify the pattern — which of the 10 core patterns applies?
3. Attempt the solution — max 45 minutes on a Hard problem
4. If stuck after 45 min — read the approach only, not the full solution
5. Re-attempt from scratch
6. After solving — read the top 2 discussion solutions
7. Add a 2-line comment in the code explaining the key insight

---

## 🧠 The 10 core FAANG patterns

| # | Pattern | When to use |
|---|---------|-------------|
| 1 | Two Pointers | Sorted arrays, pairs, palindromes |
| 2 | Sliding Window | Subarrays, substrings, contiguous sequences |
| 3 | Binary Search | Sorted arrays, search space problems |
| 4 | Stack / Monotonic Stack | Next greater element, histograms, calculators |
| 5 | BFS / DFS | Graphs, trees, shortest path, connected components |
| 6 | Dynamic Programming | Optimal substructure, overlapping subproblems |
| 7 | Backtracking | All combinations, permutations, constraint satisfaction |
| 8 | Graphs + Topological Sort | Dependencies, ordering, course schedules |
| 9 | Heap / Priority Queue | Top K elements, streaming data, merge problems |
| 10 | Tree traversals + LCA | Binary trees, BSTs, ancestor problems |

---

## 🛠️ Tools and setup

```bash
# Python version
python --version   # 3.11+

# Run any solution
python phase-1-dsa/session-01/three_sum.py

# Dependencies (none required for DSA)
# AI/ML phase will use: numpy, pandas, torch, fastapi
```

---

## 📊 Progress tracker

| Metric | Target | Current |
|--------|--------|---------|
| Phase 0 days completed | 14 | 0 |
| DSA sessions completed | 90 | 0 |
| Problems solved | 360 | 0 |
| LeetCode problems | 360 | 0 |
| Projects shipped | 4 | 0 |

---

## 🚀 Projects built alongside this journey

| # | Project | Tech | Status |
|---|---------|------|--------|
| 1 | Full-stack web app | React, Node.js, PostgreSQL | 🔜 |
| 2 | System design project | TypeScript, Redis, Docker | 🔜 |
| 3 | DSA visualizer / dev tool | TypeScript, React | 🔜 |
| 4 | AI/ML beginner project | Python, HuggingFace API | 🔜 |

---

## 📅 Daily schedule

| Time | Block |
|------|-------|
| 7:00 – 9:30 AM | DSA block 1 — Medium problem |
| 10:00 AM – 12:30 PM | DSA block 2 — Hard problems |
| 1:30 – 4:00 PM | Project build block |
| 4:30 – 7:00 PM | Startup internship |
| 8:00 – 9:30 PM | SE module study (DevOps, Data Eng, System Design) |
| Sunday evening | LinkedIn post — project completions only |

---

## 🔗 Connect

If you're on a similar journey, feel free to connect:

- **LinkedIn:** [Srinivas Barkunta](https://www.linkedin.com/in/srinivasbarkunta-335b85255)
- **GitHub:** [barkuntasrinivas2025-stack](https://github.com/barkuntasrinivas2025-stack)
- **LeetCode:** [SrinivasBarkunta_2025](https://leetcode.com/u/SrinivasBarkunta_2025)

---

> "The goal is not to finish the list. The goal is to become the person who can solve any problem on the list."
