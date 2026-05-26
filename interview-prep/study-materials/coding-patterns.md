# Coding Patterns — Python Templates & Idioms

Every LC medium maps to 1-3 patterns below. Memorise the **template** (the 5-10 lines of code that don't change problem-to-problem) and you reduce 30 min of think-time to 5 min — leaving you 25 min for the problem-specific logic.

For each pattern: when-to-use signal, the canonical Python template, 1-2 worked examples from your week's problem list, and the bug you'll actually hit.

---

## 1. Hash Map / Counter — Group / Frequency / Anagram

**Signal:** "group by", "count of", "frequency", "anagram", "two values that sum to".

**Template:**

```python
from collections import defaultdict, Counter

def group_by_signature(items):
    groups = defaultdict(list)
    for item in items:
        sig = compute_signature(item)  # tuple, sorted string, etc.
        groups[sig].append(item)
    return list(groups.values())
```

**Canonical example — Group Anagrams (LC 49):**

```python
def groupAnagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))     # or: counts as tuple of 26 ints
        groups[key].append(s)
    return list(groups.values())
```

**Bug you'll hit:** Using `list` as a dict key (unhashable). Use `tuple(sorted(s))` or freeze with `frozenset` if order doesn't matter.

**Python idiom:** `Counter("aabbc")` → `{'a': 2, 'b': 2, 'c': 1}`. `Counter(a) == Counter(b)` is the cleanest anagram check.

---

## 2. Two Pointers

**Signal:** "sorted array", "palindrome", "pair / triple summing to X", "in-place merge", "remove duplicates".

**Template (opposite ends):**

```python
def two_pointer_pair(nums, target):
    nums.sort()
    l, r = 0, len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s == target:
            return (l, r)
        elif s < target:
            l += 1
        else:
            r -= 1
    return None
```

**Template (same direction — read/write):**

```python
def remove_duplicates(nums):
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1
    return write
```

**Canonical example — 3Sum (LC 15):**

```python
def threeSum(nums):
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # skip dup anchor
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
            elif s < 0:
                l += 1
            else:
                r -= 1
    return res
```

**Bug you'll hit:** Forgetting to skip duplicates at all three positions (anchor `i`, then `l` and `r` after a hit). Test with `[0,0,0,0]`.

---

## 3. Sliding Window

**Signal:** "longest / shortest substring with property", "max sum of K consecutive", "subarray with at most K distinct".

**Template (variable-size, expand/shrink):**

```python
def longest_with_property(s):
    state = {}            # counts / sums for the current window
    l = 0
    best = 0
    for r, ch in enumerate(s):
        state[ch] = state.get(ch, 0) + 1
        while not is_valid(state):
            state[s[l]] -= 1
            if state[s[l]] == 0:
                del state[s[l]]
            l += 1
        best = max(best, r - l + 1)
    return best
```

**Canonical example — Longest Substring No Repeat (LC 3):**

```python
def lengthOfLongestSubstring(s):
    last = {}
    l = 0
    best = 0
    for r, ch in enumerate(s):
        if ch in last and last[ch] >= l:
            l = last[ch] + 1
        last[ch] = r
        best = max(best, r - l + 1)
    return best
```

**Bug you'll hit:** Off-by-one on window length (`r - l + 1`, not `r - l`). The shrink-while needs to be a `while`, not an `if`, for problems like "max distinct = k".

---

## 4. Binary Search

**Signal:** "sorted", "find first / last X", "minimise the max", "rotated sorted array". Also: "find peak", "search in matrix".

**Template (find first true in a boolean-monotone array):**

```python
def first_true(lo, hi, predicate):
    """Smallest x in [lo, hi] where predicate(x) is True. Assumes monotone F...FT...T."""
    while lo < hi:
        mid = (lo + hi) // 2
        if predicate(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

**Use this single template for every binary-search problem.** Rewrite the problem as "find smallest x such that predicate(x) is True." If you ever write `if a[mid] == target: return mid` you're going to get an off-by-one.

**Canonical example — Search in Rotated Sorted Array (LC 33):**

```python
def search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        # which half is sorted?
        if nums[lo] <= nums[mid]:
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1
```

**Bug you'll hit:** `<=` vs `<` in the half-check when comparing to a pivot. Drill rotated-array problems on paper.

**Python idiom:** `bisect.bisect_left(arr, x)` and `bisect.insort(arr, x)` for sorted arrays. Often replaces a hand-written binary search.

---

## 5. Stack / Monotonic Stack

**Signal:** "next greater / smaller", "valid parentheses", "evaluate expression", "max rectangle / area in histogram".

**Template (monotonic decreasing — for "next greater"):**

```python
def next_greater(nums):
    res = [-1] * len(nums)
    stack = []  # holds indices; nums at indices is decreasing
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            res[stack.pop()] = x
        stack.append(i)
    return res
```

**Canonical example — Daily Temperatures (LC 739):**

```python
def dailyTemperatures(temps):
    res = [0] * len(temps)
    stack = []
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            j = stack.pop()
            res[j] = i - j
        stack.append(i)
    return res
```

**Bug you'll hit:** Pushing values instead of indices. You almost always want indices.

---

## 6. Linked List

**Signal:** Anything mentioning `head` and `next`.

**Template — reverse:**

```python
def reverse(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
```

**Template — fast/slow (find middle, detect cycle):**

```python
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            return True
    return False
```

**Template — dummy head (insertion / removal at front-or-middle):**

```python
def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n):
        fast = fast.next
    while fast.next:
        fast, slow = fast.next, slow.next
    slow.next = slow.next.next
    return dummy.next
```

**Bug you'll hit:** Forgetting `dummy` when the head might be removed. Almost always use one.

---

## 7. Tree DFS / BFS

**Signal:** Any binary tree, "level order", "depth", "path sum", "ancestor".

**Template — recursive DFS (returns useful state):**

```python
def dfs(node):
    if not node:
        return base_value
    left = dfs(node.left)
    right = dfs(node.right)
    # combine left, right, node.val into the answer
    return combine(left, right, node.val)
```

**Template — BFS by level:**

```python
from collections import deque

def level_order(root):
    if not root:
        return []
    q = deque([root])
    res = []
    while q:
        level = []
        for _ in range(len(q)):   # snapshot size = level size
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(level)
    return res
```

**Canonical example — Validate BST (LC 98), with bounds:**

```python
def isValidBST(root):
    def go(node, lo, hi):
        if not node:
            return True
        if not (lo < node.val < hi):
            return False
        return go(node.left, lo, node.val) and go(node.right, node.val, hi)
    return go(root, float('-inf'), float('inf'))
```

**Bug you'll hit:** Trying to validate BST by checking only `node.left.val < node.val < node.right.val`. That's wrong. You need running bounds.

---

## 8. Graph BFS / DFS

**Signal:** Grid problems ("islands", "rotting oranges"), explicit graph with adjacency, "shortest path in unweighted".

**Template — grid BFS / DFS:**

```python
def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c):
        if (r, c) in visited or not (0 <= r < rows and 0 <= c < cols) or grid[r][c] == '0':
            return
        visited.add((r, c))
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            dfs(r+dr, c+dc)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                dfs(r, c)
                count += 1
    return count
```

**Template — topological sort (Kahn's, for "course schedule" / dep-order):**

```python
from collections import defaultdict, deque

def topo(num, edges):
    adj = defaultdict(list)
    indeg = [0] * num
    for a, b in edges:    # b is prerequisite for a
        adj[b].append(a)
        indeg[a] += 1
    q = deque(i for i in range(num) if indeg[i] == 0)
    order = []
    while q:
        node = q.popleft()
        order.append(node)
        for nxt in adj[node]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)
    return order if len(order) == num else []   # [] => cycle
```

**Bug you'll hit:** Recursion-depth overflow on a 1000×1000 grid DFS. Switch to BFS (iterative `deque`) if `n > ~500`.

---

## 9. Heap / Priority Queue

**Signal:** "Kth largest / smallest", "merge K sorted", "median of stream", "schedule with priority".

**Template — top K:**

```python
import heapq

def k_largest(nums, k):
    return heapq.nlargest(k, nums)  # often the right answer
    # or, for streaming:
    # heap = []
    # for x in nums:
    #     heapq.heappush(heap, x)
    #     if len(heap) > k:
    #         heapq.heappop(heap)
    # return heap[0]  # kth largest
```

**Template — two heaps (median of data stream, LC 295):**

```python
class MedianFinder:
    def __init__(self):
        self.lo = []   # max-heap (store -x)
        self.hi = []   # min-heap

    def addNum(self, x):
        heapq.heappush(self.lo, -x)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self):
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        return (-self.lo[0] + self.hi[0]) / 2
```

**Python idiom:** `heapq` is min-only. For max-heap, push negatives. For tie-breaking, push tuples: `(priority, tiebreak, item)`.

---

## 10. Backtracking

**Signal:** "all combinations", "all subsets", "all permutations", "N-Queens", "word search".

**Template:**

```python
def backtrack(state, choices, results):
    if is_goal(state):
        results.append(state.copy())   # COPY, not reference
        return
    for choice in valid_choices(state, choices):
        state.append(choice)
        backtrack(state, choices, results)
        state.pop()                    # undo
```

**Canonical example — Subsets (LC 78):**

```python
def subsets(nums):
    res = []
    def bt(start, path):
        res.append(path.copy())
        for i in range(start, len(nums)):
            path.append(nums[i])
            bt(i + 1, path)
            path.pop()
    bt(0, [])
    return res
```

**Bug you'll hit:** Forgetting to copy `state` when appending to `results`. You'll get N copies of the same final reference. Always `path.copy()` or `path[:]`.

---

## 11. Dynamic Programming

**Signal:** "min / max cost", "count number of ways", "can you reach / partition", "longest X subsequence".

**Template — 1D DP (House Robber, LC 198):**

```python
def rob(nums):
    prev2, prev1 = 0, 0
    for x in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + x)
    return prev1
```

**Template — 2D DP (Unique Paths, LC 62):**

```python
def uniquePaths(m, n):
    dp = [[1] * n for _ in range(m)]
    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r-1][c] + dp[r][c-1]
    return dp[m-1][n-1]
```

**Template — knapsack (Coin Change, LC 322):**

```python
def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1
```

**Approach (do this on every DP problem):**
1. State: "what is `dp[i]` / `dp[i][j]`?" Write it in English.
2. Recurrence: how does `dp[i]` depend on smaller states?
3. Base case.
4. Order: iterate so dependencies are filled.
5. Space-optimise to O(N) → O(1) only if interviewer asks.

**Bug you'll hit:** Confusing index meanings. Always write the state definition as a comment above the loop.

---

## 12. Intervals

**Signal:** "merge", "overlapping", "free time", "meeting rooms".

**Template:**

```python
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    out = [intervals[0]]
    for s, e in intervals[1:]:
        if s <= out[-1][1]:
            out[-1][1] = max(out[-1][1], e)
        else:
            out.append([s, e])
    return out
```

**Template — count rooms (sweep line):**

```python
def min_rooms(intervals):
    starts = sorted(i[0] for i in intervals)
    ends = sorted(i[1] for i in intervals)
    rooms = 0
    j = 0
    for s in starts:
        if s < ends[j]:
            rooms += 1
        else:
            j += 1
    return rooms
```

**Bug you'll hit:** Sorting only by start when you also need ties broken by end. Use `key=lambda x: (x[0], x[1])`.

---

## 13. Trie

**Signal:** "prefix", "autocomplete", "word search II", "longest common prefix among many".

**Template:**

```python
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node['$'] = True  # word-end sentinel

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return '$' in node

    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True
```

**Why dict-of-dicts over a TrieNode class:** less boilerplate at interview time; identical asymptotics.

---

## Python idioms cheat sheet

```python
# Counter
from collections import Counter
c = Counter("banana")          # {'a':3,'n':2,'b':1}
c.most_common(2)               # [('a',3),('n',2)]

# defaultdict
from collections import defaultdict
d = defaultdict(list)          # d[key].append(x) — no KeyError

# heapq
import heapq
heapq.heappush(h, (-priority, item))   # max-heap via negation
heapq.heappushpop(h, x)        # push then pop, faster than two ops
heapq.nlargest(k, iterable)    # top-K in O(n log k)

# bisect
import bisect
bisect.bisect_left(sorted_arr, x)
bisect.insort(sorted_arr, x)   # insertion-sort an item

# deque (double-ended, O(1) append/popleft)
from collections import deque
q = deque([1,2,3])
q.appendleft(0); q.pop(); q.popleft()

# sorting with custom key
arr.sort(key=lambda x: (x[1], -x[0]))   # 2nd asc, 1st desc

# enumerate with start
for i, x in enumerate(arr, start=1): ...

# zip + unpack
for a, b in zip(prev, curr): ...

# any/all with generator (short-circuit)
all(c.isalpha() for c in s)

# powerful comprehensions
{ch: i for i, ch in enumerate(s)}      # last index of each char
[[0]*n for _ in range(m)]              # 2D zeros (do NOT use [[0]*n]*m)

# infinity sentinels
INF = float('inf')

# tuple as dict key
visited.add((r, c))            # not [r, c]

# Counter math
Counter("aab") - Counter("ab") # Counter({'a':1})
```

---

## The 10-min "before-you-code" ritual

For every problem in your daily practice:

1. **Restate** the problem in your own words (30s).
2. **2 examples** — the obvious one + an edge case (empty, single, duplicates, negatives) (1 min).
3. **Brute force** — even if you'd never ship it, name it and give its complexity. Often the interviewer wants to hear it (1 min).
4. **Optimise** — name the pattern (sliding window? two pointers? DP?). Cite the state / invariant in one sentence (2 min).
5. **Code** (15-18 min). If you're past 25 min without a working solution, switch to discussing where you're stuck.
6. **Test** on the 2 examples; trace one of them line-by-line (3 min).
7. **Complexity** — time & space, justified (1 min).

**The fastest way to fail a coding interview is to start typing within 60 seconds.** Step 1-4 are non-optional even when you "see the answer immediately."

---

## What to do after each problem

Add one line to [../coding-log.md](../coding-log.md):

```
2026-05-26 · LC 49 Group Anagrams · hash · tuple(sorted(s)) as key; could also use 26-tuple of counts
```

The post-mortem line is the actual learning. Without it you're just typing.
