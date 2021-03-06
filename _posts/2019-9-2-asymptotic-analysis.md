---
layout: post
title: "Better Algorithm or Better Hardware?"
---

In algorithmics, asymptotic analysis is used to describe the growth of functions that represent ressource usage (time and space). We say that algorithm $A$'s time complexity, $$T: \ \mathbb{N} \to \mathbb{R}_+$$ with relation to a function $$f: \ \mathbb{N} \to \mathbb{R}_+$$ is either

1. $T(n) \in O(f(n)) \iff \exists c \in \mathbb{R}_+ \land \exists n_0 \in \mathbb{N} \mid 0 \leq T(n) \leq cf(n) \ \ \forall n \geq n_0$
2. $T(n) \in \Theta(f(n)) \iff \exists c_1, c_2 \in \mathbb{R}_+ \land \exists n_0 \in \mathbb{N} \mid 0 \leq c_1f(n) \leq T(n) \leq c_2f(n) \ \ \forall n \geq n_0$
3. $T(n) \in \Omega(f(n)) \iff \exists c \in \mathbb{R}_+ \land \exists n_0 \in \mathbb{N} \mid 0 \leq cf(n) \leq T(n) \ \ \forall n \geq n_0$

Notice how the $\in$ operator has been used because $O$, $\Theta$ and $\Omega$ are sets. The $=$ sign is notation abuse. This notation tells us how the algorithm will behave according to a function. In asymptotic analysis, constants are stripped from the function because we only care about the behavior of the function, its growth. Assuming that $n$ is very large, the constants will not matter when comparing two algorithms (you can think of it as a limit).This notation proved itself to be very useful for analyzing algorithms, in theory at the very least. When we are given the task of chosing an algorithm over the other, we pick the one who's tightest time or space complexity seems to be more favorable.

I was always wondering what does the notation tell us about the growth of the input size or magnitude $n$. In the real world, we usually have a finite set of ressources. We want our algorithms to run fast and not to exceed a certain time to terminate or to hog too much memory. To accomplish a task faster, we can pick a different algorithm with a better complexity (for the given circumstances) or upgrade the hardware on which it is running. Upgrading the hardware will usually have a straightforward effect on the algorithm. All things being equal, a processor twice the clock speed of another will perform about twice faster. But how does that affect the input size or the magnitude of the algorithm's input ? Is it ever worth upgrading hardware ? Formally,

__Given an algorithm $A$ with a ressource consumption given by $T(n)$, available ressource $R$ and a speedup of $k$, how much larger can $n$ be such that $T(n) \leq R$?__

In other words, if my current system runs algorithm $A$ in $R$, if I were to upgrade for a better system that would run $k$ faster, how much larger $n$ could be and still statisfy the ressource constraint. Here, $R$ is not an entirely accurate representation of the ressource consumption of an algorithm as it is difficult to map an algorithm to an exact value, with units. Rather, we are interest into the _behavior_ of the algorithm and the magnitude of its input when ressources are finite. A speedup of $k$ means that

$$\frac{T(n)}{T'(n)} = k \tag{1}$$

where $T'$ represents the ressource consumption of the new system. The objective is to determine the relationship between $n_1$ and $n_2$. We know that

$$T(n_1) \leq R \implies n_1 \leq T^{-1}(R)$$

With equation 1, we can deduce that

$$T(n_2) \leq kR \implies n_2 \leq T^{-1}(kR)$$

And so

$$\frac{n_2}{n_1} \leq \frac{T^{-1}(kR)}{T^{-1}(R)} \tag{2}$$

With this in hand, we can substitute $T$ for any function and get our result. Here is a table of common functions:

<center>
<table style="width:75%">
  <tr>
    <th>$T(n)$</th>
    <th>$\frac{n_2}{n_1}$</th> 
  </tr>
  <tr>
    <td>$n^p$</td>
    <td>$k^{\frac{1}{p}}$</td> 
  </tr>
  <tr>
    <td>$\log_bn$</td>
    <td>$b^{k(R-1)}$</td> 
  </tr>
  <tr>
    <td>$b^n$</td>
    <td>$1 + \log_Rk$</td>
  </tr>
</table>
</center>

Notice how the slowest growing functions provide the largest growing ratio of input. For exponential functions, notice how the input can barely be any larger because of the base of the logarithm (and the logarithm itself that has a slow growth, relatively speaking). Finally, it is interesting that both logarithmic and exponential functions depend on the the value of $R$. A larger $R$ makes logarithmic functions all the more worth the it whereas, as just stated, exponential functions will be severely hindered in their acceptable input size. To double the input size of an algorithm that follows an exponential growth, one would have to get a computer $R$ times faster (up to a constant of course).

In conclusion, it appears that a better algorithm will usually beat better hardware, especially when the time complexity is undesirable. But it is not always about chosing one over the other. It is evident that a better algorithm will let you do even more with better hardware. A logarithmic algorithm will perform exponentially better with better hardware. In other words, hardware upgrade is all the more justified when it runs a good algorithm.

### References
 - Cormen, T. H., & Cormen, T. H. (2001). Introduction to algorithms. Cambridge, Mass: MIT Press.