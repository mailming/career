# Coding Practice Log

Target Month 1: **25 LC mediums in Python** (1/day, 5 per week, weeks 1-5).  
Target Month 2: +30 mediums + 5 hards (cumulative ~60).

## Rules

- **Time-box:** 30 min think + code, 10 min review optimal solution. Stop at 40 min total.
- **Re-do at -3 days** any problem you didn't solve cleanly in 30 min.
- **Tag** each problem (`array`, `hash`, `graph`, `dp`, `intervals`, `trie`, `heap`, `bs`, `2p`, `slidwin`, `bt`, `string`, `tree`).
- **Note** the trick / pattern in one line. That's what shows up at interview time.
- **Mock cadence:** every 5th problem, do it on paper / in a plain editor with no autocomplete.

## Picks for Month 1 (curated NeetCode-150 mediums)

Pick 25 from this list; cross off as you go. Don't reorder — the sequence is designed to spiral patterns.

### Week 1 — Arrays / Hash / Two-Pointer ramp

- [ ] **Group Anagrams** (LC 49) · hash · `O(n·k)`
- [ ] **Top K Frequent Elements** (LC 347) · heap / bucket sort
- [ ] **Product of Array Except Self** (LC 238) · prefix/suffix
- [ ] **Longest Consecutive Sequence** (LC 128) · hashset
- [ ] **3Sum** (LC 15) · sort + two-pointer

### Week 2 — Sliding Window / Stack / Binary Search

- [ ] **Longest Substring Without Repeating Characters** (LC 3) · sliding window
- [ ] **Longest Repeating Character Replacement** (LC 424) · sliding window + freq map
- [ ] **Min Stack** (LC 155) · stack + min-tracker
- [ ] **Daily Temperatures** (LC 739) · monotonic stack
- [ ] **Search in Rotated Sorted Array** (LC 33) · binary search invariants

### Week 3 — Linked List / Trees / BFS-DFS

- [ ] **Reorder List** (LC 143) · LL pointer manipulation
- [ ] **Remove Nth Node From End of List** (LC 19) · 2-pointer
- [ ] **Validate Binary Search Tree** (LC 98) · in-order or bounds
- [ ] **Binary Tree Level Order Traversal** (LC 102) · BFS
- [ ] **Construct Binary Tree from Preorder and Inorder** (LC 105) · recursion + indexing

### Week 4 — Graphs + Trie + Heap

- [ ] **Number of Islands** (LC 200) · DFS/BFS
- [ ] **Clone Graph** (LC 133) · DFS + memo
- [ ] **Pacific Atlantic Water Flow** (LC 417) · multi-source BFS
- [ ] **Implement Trie (Prefix Tree)** (LC 208) · trie basics
- [ ] **Kth Largest Element in an Array** (LC 215) · quickselect / heap

### Week 5 — DP + Intervals + Greedy

- [ ] **House Robber** (LC 198) · 1D DP
- [ ] **Coin Change** (LC 322) · unbounded knapsack
- [ ] **Longest Increasing Subsequence** (LC 300) · DP + patience sort
- [ ] **Merge Intervals** (LC 56) · sort + merge
- [ ] **Non-overlapping Intervals** (LC 435) · greedy by end-time

---

## Daily template

Copy this block at the top of every entry below.

```
### YYYY-MM-DD · LC <num> <title>
- Tag: <tag>
- Time taken: <min>m think + <min>m code (solved? Y/N)
- Pattern / trick: <one line>
- Mistakes: <one line>
- Re-do by: <date if not solved cleanly>
```

---

## Log

### 2026-MM-DD · LC ___ ____

- Tag:
- Time taken:
- Pattern / trick:
- Mistakes:
- Re-do by:

<!-- copy & paste the block above for each day's problem -->

---

## Month 2 picks (additional 30 mediums + 5 hards, cumulative ~60)

Same rules; spiral patterns; pick from these. Cross off as you go.

### Week 6 — Arrays / Hash / Heap revisit + advanced two-pointer

- [ ] **Container With Most Water** (LC 11) · two-pointer
- [ ] **Subarray Sum Equals K** (LC 560) · prefix sum + hash
- [ ] **Find All Anagrams in a String** (LC 438) · sliding window
- [ ] **Trapping Rain Water** (LC 42) · two-pointer / stack — **medium-hard, often asked**
- [ ] **K Closest Points to Origin** (LC 973) · heap / quickselect
- [ ] **Task Scheduler** (LC 621) · greedy / heap

### Week 7 — Graphs + Trees + Trie deeper

- [ ] **Course Schedule** (LC 207) · topological sort (DFS or Kahn)
- [ ] **Course Schedule II** (LC 210) · topo with ordering
- [ ] **Word Search** (LC 79) · DFS + backtracking
- [ ] **Word Search II** (LC 212) · trie + DFS — **LC HARD**
- [ ] **Lowest Common Ancestor of a Binary Tree** (LC 236) · recursion
- [ ] **Binary Tree Maximum Path Sum** (LC 124) · recursion + global max — **LC HARD**
- [ ] **Serialize and Deserialize Binary Tree** (LC 297) · DFS w/ markers — **LC HARD**
- [ ] **Word Ladder** (LC 127) · BFS + word transformation
- [ ] **Number of Connected Components in an Undirected Graph** (LC 323) · Union-Find

### Week 8 — DP + Intervals + Greedy

- [ ] **Unique Paths** (LC 62) · 2D DP basics
- [ ] **Longest Common Subsequence** (LC 1143) · classic LCS
- [ ] **Edit Distance** (LC 72) · DP — **medium-hard**
- [ ] **Word Break** (LC 139) · DP + dict
- [ ] **Partition Equal Subset Sum** (LC 416) · subset-sum DP
- [ ] **Maximum Product Subarray** (LC 152) · DP track min+max
- [ ] **Best Time to Buy and Sell Stock II / III / IV** (LC 122 / 123 / 188) · DP family
- [ ] **Burst Balloons** (LC 312) · interval DP — **LC HARD**
- [ ] **Insert Interval** (LC 57) · sweep
- [ ] **Meeting Rooms II** (LC 253) · heap / sweep
- [ ] **Jump Game** (LC 55) · greedy
- [ ] **Jump Game II** (LC 45) · BFS-style greedy

### Wildcards — pick 5 from this set to round out

- [ ] **Reverse Nodes in k-Group** (LC 25) · LL — **LC HARD**
- [ ] **Median of Two Sorted Arrays** (LC 4) · binary search — **LC HARD**
- [ ] **Sliding Window Maximum** (LC 239) · monotonic deque — **LC HARD**
- [ ] **Word Pattern / Encode and Decode Strings** (LC 290 / 271) · hash
- [ ] **Design Twitter / LRU Cache / LFU Cache** (LC 355 / 146 / 460) · design problems — frequently asked at staff loops

Total of this list = 30 mediums + 5 hards. If you hit them all, you've earned a confident Tier-1 coding bar.

---

## Pattern tracker (fill as you go)

| Pattern | Problems solved | Notes |
|---------|------------------|-------|
| arrays / hash | 0 / 6 | |
| sliding window | 0 / 3 | |
| stack | 0 / 2 | |
| binary search | 0 / 2 | |
| linked list | 0 / 2 | |
| trees / BFS / DFS | 0 / 5 | |
| graphs | 0 / 4 | |
| trie | 0 / 1 | |
| heap / quickselect | 0 / 2 | |
| DP | 0 / 4 | |
| intervals / greedy | 0 / 3 | |

When any row hits its denominator twice, that pattern is at ready-state.

## Interview-time cheats (write these in your own words after the first 10 problems)

- Hash-set vs hash-map vs sorted-set
- BFS vs DFS — when level matters, BFS
- Monotonic stack template
- Sliding-window expansion/contraction template
- Quickselect template for "kth"
- DP order: top-down memo first, then bottom-up
- Topological sort: Kahn vs DFS-stack
- Union-Find template (path compression + rank)
