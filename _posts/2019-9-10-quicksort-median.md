---
layout: post
title: "Quicksort : Median Selection Strategies"
---

[`quicksort`](https://wikipedia.com/quicksort) is one of the most popular sorting algorithms out there due to its practical speed (ordered accesses and inplace). Any seasoned software engineer or computer scientist will know its average runtime of $\Theta(n \log n)$, like any efficient sorting algorithm, and most will also remember its worst case of $\Theta(n^2)$. Depending on the choice of the median during the partitioning phase of the array, performance can be drastically impacted by common cases such as an already sorted input. Ex: Suppose we pick the first or last element of an array of distinct elements as our pivot. For a sorted (or even and _almost-sorted_) input, the partitioning will split elements in a rather uneven manner. Most elements will be either greater or lesser than the pivot which will result in an undesirable performance.

The time taken by quicksort can be modeled by the following recurrence:

$$T(n) = T(q) + T(n - q) + cn \ \ 1 \leq q \leq n - 1$$

Note that an ideal split would be when $1=\frac{n}{2}$ and the worst split is when $q = \{1, n - 1\}$. Using the Master Theorem, it can be shown that for any value of $1$ that is not a proportion of $n$, $T(n) \in \Theta(n^2)$. Sometimes, it is convenient to rewrite the recurrence with a proportion term, $\alpha$ and it is that form that we will use for the remainder of this post.

$$T(n) = T(\alpha n) + T((1-\alpha)n) + cn \ \ 0 < \alpha < 1 \tag{1}$$

`quicksort`'s performance relies mostly on the strategy that we use to select the median. But why would a sorting algorithm be so popular if its worst case runtime behaves similarily to ugly, subpar algorithms like `insertion-sort` or `bubble-sort` ? Is it simply because of its average performance being better than the alternatives ? Lack of guarantees for non-critical systems ? Even if we were to shuffle the input array, there is still a possibility that our median was a bad choice. But how likely is it ? How likely is it that we get a bad split ? Formally,

__Given an array of $n$ distinct elements and a desired split of $\alpha$-to-$(1-\alpha)$, how likely is it to get a worse split ?__

## Pick one
It is possible to define a worse split as a split of ratio $\beta$ such that
$$
\begin{cases}
    \beta < \alpha \ \ \text{if } \alpha \leq \frac{1}{2}\\
    \beta > \alpha \ \ \text{if } \alpha > \frac{1}{2}
\end{cases}
$$

A popular strategy to median selection is to randomly pick an element from the array, rather than shuffling it and picking an element at a specific index. The probability that we get a worse split is the probability that we randomly pick all the elements that would make a worse median. There are $2 \cdot n \cdot \alpha$ elements that fit this criteria. The probability to pick one of those elements is $\frac{1}{n}$. Multiplying, we obtain $2\alpha$.

## Third time's the charm
Another approach to median selection is to pick three elements at distinct indices and to select the median out of them. The rationale behind this method would be that the probability of getting a inadequate median is lowered. We will assume that it is possible to select one element more than once. The probability that we select a worse median than $\alpha$ is twice the probability that at least two elements are picked from the $\alpha n$ smaller elements (the problem is symetrical). This comes down to the sum of the probability that three elements are in that range and that exactly two are in that range. 

$$
P[\text{two elements in $\alpha n$}] = P[\text{three elements in $\alpha n$}] + P[\text{exactly two elements in $\alpha n$}] \\
= \alpha^3 + 3\alpha^2 (1 - \alpha)
= 3\alpha^2 - 2 \alpha^3
$$

And so the probability to get a worse split is $6\\alpha^2 - 4\alpha^3$. Because $\alpha < 1$, this probability can be described as $O(\alpha^2)$ which means that the probability of getting a split worse than what we want gets smaller at a quadratic pace. Not bad!

## $k$ time's the charm
Can we do even better ? How about picking $k$ elements at random and computing the median out of them ? We can generalize the two previous strategies to an arbitrary amount of elements. The probability of getting a split worse than $\alpha$ is the probability that at least $\left \lceil \frac{k}{2} \right \rceil$ are in the $\alpha n$ smallest elements:

$$
P\left [\text{at least $\frac{k}{2}$ elements in $\alpha n$ smallest elements} \right ] \ \ \ k \leq \alpha n
$$

$$
= \sum_{i=\left \lceil \frac{k}{2} \right \rceil}^{k} P[\text{exactly $i$ elements in $\alpha n$ smallest elements}]
$$

$$
= \sum_{i=\left \lceil \frac{k}{2} \right \rceil}^{k} \alpha^i (1 - \alpha)^{k-i} \frac{k!}{(k-i)!i!}
$$

This sum cannot be simplified. But simplification is not required if we want to get an idea of how likely it is to get a worse split. We can bound the probability by observing that the values summed become very small as $i$ increases. This probability is $\Omega \left ( \alpha^{\frac{k}{2}} \right )$ and all the terms that we omitted are orders of magnitude smaller which won't affect the probability significantly. (Note: This is dependant on $\alpha$. For instance, if $\alpha=\frac{1}{10}$, the next elements are about 10 times smaller.) I have written a script that computes this probability for several $\alpha$ and $k$. Here are the results:

![results](/images/quicksort-median.png)

As expected, it looks like picking more elements to get a better probability of a good median becomes less and less worth the increased runtime (notice how the curve along the $k$ axis, when $\alpha=0.1$, barely moves anymore when $k > 5$).

## I want guarantees
What if we wanted a guarantee on the behavior of `quicksort` ? What if we selected the true median with a common algorithm like `median-of-median` that runs in $O(n)$. That would not change the time complexity of the algorithm but it would heavily impact the runtime of the algorithm nonetheless, because of the hidden constants. Given the previous results, it is deemed better to fallback to a simple median strategy that yields good results most of the time and opt for other sorting algorithms like `mergesort` or `heapsort` for systems that require guarantees.

### References
    - Cormen, T. H., & Cormen, T. H. (2001). Introduction to algorithms. Cambridge, Mass: MIT Press.