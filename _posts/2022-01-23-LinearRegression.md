---
title: Some Properties of Linear Regression
category: tech
classes: wide
---

**If we regress $X$ on $Y$ and get $\beta$ as the slope and if we regress $Y$ on $X$ and get slope $\beta'$. What is the product of $\beta$ and $\beta'$**

In one dimensional problem we have $\beta = S_{xy}/S_{yy}$ where 

$$
S_{xy} = \sum_i (x_i- \bar{x})(y_i - \bar{y})
$$

and 

$$
S_{xx} = \sum_i (x_i - \bar{x})(x_i-\bar{x})
$$

and similarly for $S_{yy}$. Then we have 

$$
\beta \beta' = \frac{S_{xy}}{S_{yy}}\frac{S_{xy}}{S_{xx}} = \frac{\left(\sum_i (x_i-\bar{x})(y_i-\bar{y})\right)^2}{\sum_i(x_i-\bar{x})^2 \sum_j(y_j-\bar{y})^2} 
$$

which is the square of sample correlation of $x_i$ and $y_i$.This is positive obviously and is less or equal to $1$ by the Cauchy Schwartz inequality if we treat the numerator as the square of dot product of the vector $x_i-\bar{x}$ and $y_i-\bar{y}$.



### Multivariate linear regression

***The range of $R^2$ in multivariate linear regression?***  

We first give a claim that in general linear regression, the $R^2$ is the estimate of the square of correlation between $y$ and predicted value $\hat{y}$.

$$
\begin{aligned}
\text{Corr}(y, \hat{y})^2 &= \frac{\left(\sum_i (y_i-\bar{y})(\hat{y}_i - \bar{\hat{y}}) \right)^2}{\sum_i (y_i-\bar{y})^2\sum_j(\hat{y}_j -\hat{\bar{y}})^2} \\
&= \frac{\left(\sum_i y_i \hat{y}_i - y_i\bar{\hat{y}}- \bar{y}\hat{y}_i + \bar{y}\bar{\hat{y}} \right)^2}{\sum_i (y_i-\bar{y})^2\sum_j(\hat{y}_j -\hat{\bar{y}})^2} \\
&= \frac{\left(\sum_i y_i \hat{y}_i  - 2n \bar{y} \bar{\hat{y}} + n \bar{y}\bar{\hat{y}} \right)^2}{\sum_i (y_i-\bar{y})^2\sum_j(\hat{y}_j -\hat{\bar{y}})^2} \\
&= \frac{\left(\sum_i y_i \hat{y}_i  - n \bar{y} \bar{\hat{y}} \right)^2}{\sum_i (y_i-\bar{y})^2\sum_j(\hat{y}_j -\hat{\bar{y}})^2} 
\end{aligned}
$$

We first note that in the optimization problem, 

$$
X^T(X\hat{\beta} - Y) = 0
$$

and since the first column of $X$ is all ones, we have 

$$
1^t(X\hat{\beta} - Y) = 0\quad \Rightarrow 1^t X\hat{\beta} = 1^t Y \quad \Rightarrow \boxed{\bar{\hat{Y}} = \bar{Y}}
$$

And notice 

$$
\hat{y}^T \hat{y} = y^T (X (X^TX)^{-1} X^T ) X(X^TX)^{-1}X^T y = y^TX(X^TX)^{-1}X^Ty = y^T\hat{y}
$$

Thus, we find 

$$
\sum_j(\hat{y}_j - \bar{\hat{y}})^2 = \sum_j \hat{y}_j^2 - n \bar{\hat{y}}^2 = \sum_j \hat{y}_j y_j - n \bar{y}^2
$$

where we used the $\hat{y}^T\hat{y} = y^T\hat{y}$  which means $\sum \hat{y}_j^2 = \sum_j \hat{y}_jy_j $  

Thus 

$$
\begin{aligned}
\text{Corr}(y, \hat{y})^2 &= \frac{\left(\sum_i y_i \hat{y}_i  - n \bar{y} \bar{\hat{y}} \right)^2}{\sum_i (y_i-\bar{y})^2\sum_j(\hat{y}_j -\hat{\bar{y}})^2}  \\
&=\frac{\left(\sum_i y_i \hat{y}_i  - n \bar{y}^2 \right)^2}{\sum_i (y_i-\bar{y})^2(\sum_j \hat{y}_j y_j - n \bar{y}^2)} \\
&= \frac{\sum_i y_i \hat{y}_i  - n \bar{y}^2}{\sum_i (y_i-\bar{y})^2} 
\end{aligned}
$$

The $R^2$ can be calculated as 

$$
\begin{aligned}
R^2 &= 1-\frac{\sum_{i}(y_i-\hat{y}_i)^2}{\sum_i(y_i-\bar{y})^2} \\
&= \frac{\sum_i \left( 2 y_i\hat{y}_i - \hat{y}_i^2 - 2y_i\bar{y} + \bar{y}^2 \right)  }{\sum_i(y_i-\bar{y})^2} \\
&= \frac{\sum_i \left( 2 y_i\hat{y}_i - \hat{y}_iy_i \right) - 2 n \bar{y}\bar{y} + n\bar{y}^2   }{\sum_i(y_i-\bar{y})^2} \\
&= \frac{\sum_i y_i\hat{y}_i - n\bar{y}^2}{\sum_i(y_i-\bar{y})^2} = \text{Corr}(y,\hat{y})^2
\end{aligned}
$$


Since the correlation estimation is in $[0,1]$ by Cauchy-Schwartz inequality. We showed that for linear regression $R^2$ is also in that range. 

### R^2 is the correlation squared between $y$ and $x$ in $1D$ OLS

In 1d problem, $y\sim \beta x + \beta_0$. We know from above 

$$
\begin{aligned}
R^2 &= \text{Corr}^2(y,\hat{y}) \\
&=\frac{\left(\sum_{i}(y_i-\bar{y})(\hat{y}_i-\bar{\hat{y}})\right)^2}{\sum_i (y_i-\bar{y})^2\sum_i (\hat{y}_i-\bar{\hat{y}})^2} \\
&=\frac{\left(\sum_i(\hat{\beta}x-\hat{\beta}\bar{x})\cdot ( y_i-\bar{y})\right)^2}{\sum_i(\hat{\beta}x - \hat{\beta}\bar{x})^2\sum_i(y-y_i)^2}\\
&=\frac{\left(\sum_i(x-\bar{x})\cdot ( y_i-\bar{y})\right)^2}{\sum_i(x - \bar{x})^2\sum_i(y-y_i)^2}
\end{aligned}
$$

which means $R^2$ is the correlation squared between $y$ and $x$. 




### Some Notes on Projection

Consider the matrix $X^TX$ with $X$ as a matrix of column stacking $p$ Vectors. Each vector is denoted as $x_i$ and the vector has components $n$ and the component of $x_i$ is denoted as $x_{i}^\alpha$.  Let $G = X^TX$. It has components as $G_{ij}$. We denote the components of its inverse as $G^{ij}$. it is natrual to ask what the vector $\omega^{i\alpha} = G^{ij}x_j^\alpha$ is . Note that 

$$
\omega^{i\alpha} x^\alpha_k = G^{ij}x_j^\alpha x_k^\alpha = G^{ij}G_{jk} = \delta_{k}^i
$$

We can treat the $\omega^i$ as the dual basis of $x_i$. Let $P_i$ denote the projection on subspace spanned by $x_j$ for $j\neq i$ , we propose that 

$$
\tilde{\omega}^i = (1 - P_i) x_i
$$

and 

$$
\omega^i = \frac{\tilde{\omega}^i}{\tilde{\omega}^i\cdot x_i} = \frac{\tilde{\omega}^i}{\| \tilde{\omega}^i\|^2}
$$

This constructed $\omega^i$ satisfies the above property. 

Now come back to linear regression. The variance for the $\hat{\beta}_i$ will be the matrix $(X^TX)^{-1}_{ii}$  which is $G^{ii}$ which is 

$$
G^{ii} = G^{ij} \delta_{j}^i = G^{ij}G_{jk}G^{ki} = G^{ij} x_j x_k G^{ki} = \omega^i \omega^i = \frac{1}{\|\tilde{\omega}^i\|^2}
$$

The projected $\tilde{\omega}^i$ can then be constructed by regress $x_i$ on $x_{/i}$ where $x_{/i}$ is the space formed by $x_j$ for all $j\neq i$.  
