# median-cost
**NOTE: This function is intended to work with odd values of $n$ only, and will likely display incorrect results in the case of an even $n$ value.**

This is a simple python function that computes the distance cost for a list of $n$ numbers with with respect to a given order statistic, $\mu$. The value of $\mu$ in this function is chosen as the datapoint that lies distance $d$ from the median.

The cost function that this model was based upon is depicted as follows:

$$C = \sum_{i=1}^n | x_i - \mu |$$

Explanation of the $d$ variable:

> To use the median as the value for $\mu$, set $d$ equal to zero
> 
> For values to the right of the median, set $d$ equal to a positive integer that is $|d|$ steps to the right of the median within the list.
>
> For values to the left of the median, set $d$ equal to a negative integer that is $|d|$ steps to the left of the median within the list.
