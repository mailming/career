# Math foundation — probability + linear algebra

Last updated: 2026-09-30 (stats prep ~50% done; finish remaining half by mid-October)

Companion to [CAREER-GOAL-5-YEARS.md](../CAREER-GOAL-5-YEARS.md). For CNIT 57500 (now) and MA 59800 (next term). **Not** MA 51100.

**Diagnosis (from ECE 59500 HW1/HW2):** Linear algebra proofs are followable. **Probability is the blocker** (tower rule, probability spaces, Markov, Hoeffding). Put all math minutes into probability until that is no longer true.

**Progress (2026-09-30):** ~**half** of the AP Stats / probability prep is done (probability, gathering data, sampling-distribution intro). **Finish the rest before mid-October** (CI + significance tests + pass test) — dated plan: [STUDY-SPRINT-2026-09.md](STUDY-SPRINT-2026-09.md). Then CNIT 57500 (Oct 21) owns practice time.

**Budget:** 20–30 min/day, 5 days/week. Never steal application or LC time. Screens replace this block.

---

## What you are missing vs what each course needs

| Gap | CNIT 57500 (Oct 21 – Dec 19) | MA 59800 (later) | STAT 59800 (later) |
|-----|------------------------------|------------------|--------------------|
| Probability & sampling | **Required now** (catalog: moderate) | Not required | Core of the course |
| Linear algebra | Not required | **This is the course** | Not required |
| Calc III | No | No | Official prereq |

**Order:** Probability first (CNIT 57500 now, then Stat 110 if you ever want RL theory) → MA 59800 when offered as a light on-ramp, **not** because LA is the crisis. Skip MA 51100 unless you later want the RL theory course.

### ECE 59500 homework — what hurt vs what didn’t

| Problem | Topic | Your signal |
|---------|--------|-------------|
| HW1 P1 | Norms, Hölder | LA / analysis proofs — **you can follow these** |
| HW1 P2 | Tower rule, PDFs, geometric RV | **Probability — struggle** |
| HW1 P3 | \((\Omega,\mathcal{F},P)\), Hoeffding | **Probability — struggle** |
| HW1 P4 | Markov property proofs | **Probability — struggle** |
| HW2 P1–3 | Markov chain, MDP | Mix; the *story* is probability, the matrix multiply is LA |
| HW2 P4–5 | Value fn, \(I-\gamma P\) invertible | Mostly LA / algebra — **closer to your strength** |

CNIT 57500 covers **sampling and averages**, not the tower rule. It still helps. It does not replace a real probability course.

---

## Phase A — now until mid-October (finish remaining half)

**Goal:** complete the second half of AP Stats prep (**confidence intervals + significance tests**) and pass the paper test by **2026-10-12** (hard stop **2026-10-15**), then walk into CNIT 57500 on Oct 21 ready for homework.

**Status:** First half done (probability, sampling methods, sampling distributions intro). Remaining checklist lives in [STUDY-SPRINT-2026-09.md](STUDY-SPRINT-2026-09.md).

### Where to study (use in this order)

1. **Khan Academy — AP Statistics** (primary, has practice problems)
   - Unit: Exploring data (mean, median, SD, histograms)
   - Unit: Probability (events, independence, addition/multiplication)
   - Unit: Random variables (expected value, binomial)
   - Unit: Sampling distributions (this is the CNIT 57500 core)
   - Unit: Inference — confidence intervals + significance tests (z/t)
   - Link: https://www.khanacademy.org/math/ap-statistics

2. **StatQuest (Josh Starmer)** — watch **after** Khan, 10 min each, for intuition
   - Statistics Fundamentals playlist
   - Especially: mean vs variance, sampling, p-values, hypothesis testing, t-tests
   - YouTube: search `StatQuest statistics fundamentals`

3. **Seeing Theory** (Brown) — visual only, optional 15 min
   - https://seeing-theory.brown.edu/
   - Probability, distributions, inference

**Skip for now:** Calc-based probability textbooks, MIT 18.05 full lectures, R-from-scratch (CNIT 57500 uses tools).

### Daily practice (20–25 min)

| Minutes | Do |
|---------|----|
| 12 | Khan **exercise set** (not video-only — the quiz/practice is the work) |
| 8 | One StatQuest if a Khan unit felt foggy |
| 5 | Write 3 sentences in your own words: *what is a sampling distribution?* |

**Pass test before Oct 21** (do these by hand, no looking up):

- [ ] Mean, median, variance, SD of a 6-number list
- [ ] P(A and B) vs P(A or B); independence
- [ ] What a p-value is **and** what it is not
- [ ] Null vs alternative; Type I vs Type II
- [ ] Why n=30 sample mean is more stable than n=5 (sampling variability)
- [ ] Confidence interval in one sentence: “range of plausible values for μ given this sample”

If you fail two of those, stay on Khan another week before adding linear algebra.

---

## Phase B — Oct 21 to Dec 19 (CNIT 57500 is the probability class)

**CNIT 57500 homework is your probability course.** Do not run a second stats curriculum in parallel. **Do not add linear algebra this term** unless 57500 feels easy by week 3 — LA is not your bottleneck.

| Block | Time | What |
|-------|------|------|
| Tue / Thu | CNIT 57500 (6–8 hrs/week total) | Lectures + assignments = probability practice |
| 20 min, 4 mornings | Linear algebra | Phase B list below |
| Screens booked | Cut LA first, then LC below 3/week | Never cut applications |

### Linear algebra — where to study

1. **3Blue1Brown — Essence of Linear Algebra** (intuition; watch once, rewatch chapter when stuck)
   - https://www.3blue1brown.com/topics/linear-algebra
   - Must-watch chapters: vectors, linear combinations, matrices as transformations, determinants, inverse, eigenvalues/eigenvectors, change of basis

2. **Khan Academy — Linear Algebra** (practice problems)
   - https://www.khanacademy.org/math/linear-algebra
   - Vectors and spaces → Matrix transformations → Alternate coordinate systems (eigen stuff last)

3. **Optional code lab (15 min, Python you already know)**
   - `numpy`: `A @ B`, `np.linalg.inv`, `np.linalg.eig`, `np.linalg.lstsq`
   - Goal: *see* eigenvalues, not prove theorems

**Do not use yet:** Strang 18.06 full homework, MA 51100 notes, Jordan form, Schur form.

### Weekly LA practice (by hand, 2×2 matrices)

Week-by-week (repeat a week if you miss):

| Week | Skill | Practice |
|------|-------|----------|
| 1 | Vectors, dot product, length | 8 Khan problems |
| 2 | Matrix × vector, matrix × matrix | 8 problems; write one 2×2 × 2×1 by hand |
| 3 | Identity, inverse of 2×2 | Invert `[[2,1],[1,2]]` by hand |
| 4 | Linear systems / Gaussian elimination | Solve a 2×2 system two ways |
| 5 | Determinant (2×2, 3×3 optional) | 6 problems |
| 6 | Eigenvalues of 2×2 | Characteristic equation; check Av = λv |
| 7 | Eigenvectors | Find v for each λ; sketch the two directions |
| 8 | Least squares intuition | Overdetermined 2-eq / 1-unknown; “best fit” in words |
| 9+ | QR / projections (preview) | 3Blue1Brown “dot products and duality” + Khan projections |

**Pass test before MA 59800:**

- [ ] Multiply two 2×2 matrices by hand
- [ ] Invert a 2×2 (or know when you cannot)
- [ ] Eigenvalues of `[[4,2],[1,3]]` and check Av = λv
- [ ] Explain in one sentence: eigenvalue = stretch factor along an invariant direction
- [ ] Explain least squares: “find x that makes Ax as close as possible to b”

MA 59800 then teaches QR, larger matrices, MATLAB, spectral theorem — you will not be starting from zero.

---

## Phase C — after CNIT 57500, before / during MA 59800

If Spring has **STAT 59800**, add only if MA 59800 is light:

- Khan: random variables + CLT (refresh, not new)
- StatQuest: logistic regression, maximum likelihood (watch, don't derive)

If Spring is **MA 59800 only**: keep 2×2 eigen practice + numpy `eig` / `lstsq` 15 min, 3×/week.

Physics / mechanics stays **after** MA 59800 (Khan Physics 1 or MIT 8.01 kinematics). Not this fall.

---

## One-page weekly template

```
Week of YYYY-MM-DD
CNIT 57500 hours:
Khan stats units finished:
Khan LA problems (count):
3Blue1Brown chapter:
Pass-test items still red:
```

Log it Sunday with the weekly OS review.
