---
layout: post
title: "Master Theorem: An Intuitive Approach"
---

In this post, I would like to go through an intuitive reasoning that will leading to the Master Theorem. It is a theorem used in computer science and mathematics to get the asymptotical runtime of a divide and conquer algorithm. More precisely, it is used to solve a reccurence.

## Divide And Conquer
Divide and conquer is a class of algorithms that aim to solve a problem by dividing it into smaller chunks and recursively solving them. Generally, once the recursion is over, there is a final step that aims to combine the result of the recursive calls into a valid output.

A common representative of this class of algorithms is `merge-sort`. The input list is split in half and sorted by a recursive call (until the lists have a size of 1). Once both sides are sorted, the algorithm will merge the lists into a larger sorted list. It is rather difficult not to be charmed by the elegance of these algorithms. Nowhere in the process of sorting a list with `merge-sort` do we explicitly sort the two halves of the list. Instead, we start from the trivial base case of the single item lists and work our way up by merging sorted lists.

## Master Theorem
Divide and conquer algorithms' performance is usually modeled by a recurrence of the following form:

$$T(n) = a T\left(\frac{n}{b}\right) + f(n) \tag{1}$$

where $$T(n)$$ represents the time consumption of the algorithm for an input of size (or magnitude) of $$n$$, $$f(n)$$ represents the work accomplished within the current call to the algorithm to either split or combine the problem. $$a$$ and $$b$$ are constants. If we were to model the time consumption of `merge-sort`, we would get the following recurrence:

$$T(n) = T\left(\left\lfloor\frac{n}{2}\right\rfloor\right) + T\left(\left\lceil\frac{n}{2}\right\rceil\right) + n$$

$$T(1) \in \Theta(1)$$

which can be approximated to 

$$T(n) = 2T\left(\frac{n}{2}\right) + n$$

The Master Theorem is an approach that aims to provide an asymptotic analysis to the runtime to reccurence relations like the ones previously described. It is defined as:

$$ T(n) \in
\begin{cases}
       f(n) \in O(n ^ { \log_b{a - \epsilon} }) \land \epsilon > 0, &\Theta( n ^ { \log_ba } )\\
       f(n) \in \Theta(n ^ { \log_ba }), &\Theta( n ^ { \log_ba } \log n )\\
       f(n) \in \Omega(n ^ { \log_ba + \epsilon }) \land \epsilon > 0 \land af\left(\frac{n}{b}\right) < cf(n) \land c > 1 \land n > n_0, &\Theta(f(n))\\

\end{cases} \tag{2}$$

Again, in the case of `merge-sort`, $$T(n) \in \Theta(n \log n)$$ because $$n \in \Theta(n ^ { \log_22 }) = \Theta(n)$$.

## A Recursive Expansion
Looking at the theorem, it is difficult to intuitively make sense of the reasons behind the conditions. Before being presented to the Master Theorem, I would solve recurrences manually by expanding the equation until I got a good intuition on the end result. 

$$T(n) = a T\left(\frac{n}{b}\right) + f(n) $$

$$= f(n) + a \left[ f\left(\frac{n}{b}\right) + a T \left ( \frac{n}{b^2} \right ) \right ]$$

$$= f(n) + a \left[ f\left(\frac{n}{b}\right) + a \left[ f\left(\frac{n}{b^2}\right) + a T \left ( \frac{n}{b^3} \right) \right] \right ]$$

$$= f(n) + af(n/b) + a^2f(n/b^2) + \ ... \ + a^{ \log_b n } f(1)$$

$$= \sum_{i=0}^{ \log_b n } a^i f(n/b^i) \tag{3}$$

The idea behind the expansion is to compare the work that is done by the current call compared to previous calls. If we take a look at each recursive call, we observe that $$a$$ and $$b$$ are directly affecting the asymptotic analysis of the algorithm. A larger $$a$$ and a asymptotically larger $$f$$ will make each recursive calls more costly whereas a larger $$b$$ will reduce the amount of recursive calls.

Most [proofs](https://www.cs.cornell.edu/courses/cs3110/2012sp/lectures/lec20-master/mm-proof.pdf) that I have come across tend to assume the Master Theorem is right and use a direct approach to show that it does not lead to any contradictions. I believe that this type of approach does not lead to too much insight on the underlying logic behind the three cases of the teorem. Furthermore, the Master Theorem described here defined $$f$$ as an arbitrary function. Most of the time, $$f$$ will be a polynomial function of the $$k^{\text{th}}$$ order, that is $$f(n) \in \Theta(n^k)$$, and this is how most of the intuition will come from.

We can rewrite equation 3 as such:

$$T(n) = \sum_{i=0}^{ \log_b n } a^i f(n/b^i)$$

$$= \sum_{i=0}^{\log_b n } n^k\frac{a^i}{b^{ik}}$$

$$= n^k \sum_{i=0}^{ \log_b n } \frac{a^i}{b^{ik}} \tag{4}$$

This sum is a geometric serie of the form $$\sum_{i=0}^k c^i = \frac{c^{k+1} - 1}{c - 1}, \ c \neq 1$$ ($n^k$ was left out) where $$c = \frac{a}{b^k}$$. There are three interesting cases.
1. $$c < 1 \implies a < b^k$$ :

    $$\sum_{i=0}^{ \log_b n } c^i = \frac{c \cdot n^{\log_bc} - 1}{c - 1}$$

    Because $$c < 1$$, $$\log_bc < 1$$. As $$n$$ gets larger, the sum will converge towards a constant because $$n^{\log_bc}$$ converges towards $$0$$. Therefore, $$T(n) \in \Theta(n^k)$$.

2. $$c = 1 \implies a = b^k$$. This is a trivial case. $T(n) \in \Theta(n \log n)$.
3. $$c > 1 \implies a > b^k$$ :

    $$\frac{c \cdot n^{\log_bc} - 1}{c - 1} = \frac{\frac{a}{b^k} \cdot n^{\log_b{\frac{a}{b^k}}} - 1}{\frac{a}{b^k} - 1} \in \Theta(n^{\log_ba - k})$$

And so $T(n) \in \Theta(n^{\log_ba})$. In order to prove that we have in hand the Master Theorem itself, it is required to describe the the relationship between $f(n) = n^k$ and constants $a$ and $b$. For the first case, we stated that

$$a < b^k$$

In order to make $f(n)$ appear, $k$ must be isolated:

$$a < b^k$$

$$\log a < k \log b$$

$$ \log_b a < k$$

$$ n^{\log_ba} < n^k \implies f(n) \in \Omega(n ^ { \log_ba + \epsilon }) \land \epsilon > 0$$

And there we have it, the third case of the theorem. The two others can be derived the same way. The Master Theorem is no longer the intimidating theorem that it used to be. It all came down to a geometric serie with three interesting edge cases. 

Note: This is by no means a proof to the theorem. The assumption on $f$ being a polynomial function does not cover all the cases.

### References
 - Cormen, T. H., & Cormen, T. H. (2001). Introduction to algorithms. Cambridge, Mass: MIT Press.