---
title: Lecture 29 (April 06, 2022)
classes: wide
excerpt: "Introduction to Cointegration and Vector Error Correction Model"
date: 2022-04-06

---

### Cointegration

THe model VARMA(1,1), $k=2$.  

$$
\begin{pmatrix} x_{1t} \\ x_{2t} \end{pmatrix} - \begin{pmatrix} 0.5 & -1.0 \\ -0.25 & 0.5 \end{pmatrix}
\begin{pmatrix} x_{1,t-1} \\ x_{2,t-1} \end{pmatrix} = \begin{pmatrix} \epsilon_{1t} \\ \epsilon_{2t} \end{pmatrix} - \begin{pmatrix} 0.2 & -0.4 \\ -0.1 & 0.2 \end{pmatrix}
\begin{pmatrix} \epsilon_{1,t-1} \\ \epsilon_{2,t-1} \end{pmatrix}
$$

we solve for the characteristic polynomial of $\Phi$. we have 

$$
(\lambda-0.5)^2 - 0.25 =0
$$

this shows that $\lambda_1 = 1$ and $\lambda_2 = 0$. This shows that $x_t$ is not weakly stationary. 

$$
\begin{pmatrix}
1 - 0.5 B & B \\ 0.25 B & 1-0.5 B 
\end{pmatrix} \begin{pmatrix} x_{1t} \\ x_{2t} \end{pmatrix} = \begin{pmatrix} 1-0.2 B & 0.4B \\ 0.1B & 1-0.2B \end{pmatrix}\begin{pmatrix}\epsilon_{1t} \\ \epsilon_{2t} \end{pmatrix}
$$

Multiply the matrix 

$$
\begin{pmatrix}
1-0.5 B & -B \\ - 0.25 B & 1-0.5 B
\end{pmatrix}
$$

This gives that 

$$
\begin{pmatrix}
1-B & 0 \\ 0 & 1- B 
\end{pmatrix}\begin{pmatrix} x_{1t} \\ x_{2t}\end{pmatrix} = \Delta X_t = \begin{pmatrix}1-0.7B & -0.6B \\ -0.15B & 1-0.7 B \end{pmatrix} \begin{pmatrix} \epsilon_{1t} \\ \epsilon_{2t}\end{pmatrix}
$$

which gives a VARIMA(0,1,1) model. Marginally, $x_{1t}$ and $x_{2t}$ are unit root non-stationary.  This deals with $\lambda=1$ cases. What about the $\lambda=0$ component? 

Define 

$$
y_t = \begin{pmatrix}y_{1t} \\ y_{2t} \end{pmatrix} = \begin{pmatrix} 1 & -2 \\ 0.5 & 1 \end{pmatrix}\begin{pmatrix} x_{1t} \\ x_{2t}\end{pmatrix} = L x_{t}
$$

The $L$ matrix is invertible and 

$$
L^{-1} = \begin{pmatrix} 0.5 & 1 \\ -0.25 & 0.5 \end{pmatrix}
$$

we call that 

$$
r_t = \begin{pmatrix} r_{1t} \\ r_{2t}\end{pmatrix} = L\epsilon_t 
$$

Recall VARMA(1,1):

$$
x_t = \Phi x_{t-1} + \epsilon_t - \Theta \epsilon_{t-1}
$$

thus, we have 

$$
\begin{aligned}
y_t &= L x_t = L \Phi x_{t-1} + L\epsilon_t - L\Theta \epsilon_{t-1} \\
&= (L\Phi L^{-1}) y_{t-1} + r_t - (L\Theta L^{-1}) r_{t-1} 
\end{aligned}
$$

This gives that 

$$
\begin{pmatrix} y_{1t} \\ y_{2t} \end{pmatrix} = \begin{pmatrix} 1& 0 \\ 0 & 0 \end{pmatrix}\begin{pmatrix}y_{1,t-1}\\y_{2,t-1} \end{pmatrix} + \begin{pmatrix} r_{1,t} \\r_{2,t} \end{pmatrix} - \begin{pmatrix}0.4 & 0 \\ 0 & 0\end{pmatrix}\begin{pmatrix} r_{1,t-1} \\ r_{2,t-1}\end{pmatrix}
$$

this shows that 

$$
\begin{aligned}
&y_{1t} = y_{1,t-1} + r_{1t} - 0.4 r_{1,t-1} \\
&y_{2t} = r_{2t}
\end{aligned}
$$

this shows that $y_{1t}$ is a univariate ARIMA(0,1) i.e. $y_{1t}$ is unit root nonstationary. $y_{2t}$ is stationary white noise model and $y_{1t}$ and $y_{2t}$ are decoupled. The model only exhibits a single unit root in the system. This is the vector error correction model. 

### Vector Error correction model

$$
\Delta x_{t} = (\Phi - I) x_{t-1} + \epsilon_t - \Theta \epsilon_{t-1}
$$

because $\Phi$ has a unit root eigen value, the matrix $\Phi-I$ is a rank $1$ matrix. In the above example we have 

$$
\begin{pmatrix} 
\Delta x_{1t} \\ \Delta x_{2t} 
\end{pmatrix} = \begin{pmatrix}-1 \\ 0.5\end{pmatrix}\begin{pmatrix} 0.5 & 1 \end{pmatrix} \begin{pmatrix}
x_{1,t-1} \\ x_{2,t-1} 
\end{pmatrix}+ \begin{pmatrix}\epsilon_{1t}\\ \epsilon_{2t} \end{pmatrix} - \begin{pmatrix} 0.2 & - 0.4\\ -0.1 & 0.2 \end{pmatrix} \begin{pmatrix}\epsilon_{1,t-1} \\ \epsilon_{2,t-1} \end{pmatrix}
$$

General case: VARMA(p,q) model 

$$
x_t - \sum_{i=1}^p \Phi_i x_{t-i} = \epsilon_t - \sum_{j=1}^q \theta_j \epsilon_{t-j}
$$

want: VECM for VARMA(p,q) in the form 

$$
\Delta x_t = \alpha \beta^T x_{t-1} + \sum_{i=1}^ {p-1} \Phi_i^* \Delta x_{t-i} + \epsilon_t - \sum_{j=1}^q \theta_j \epsilon_{t-j}
$$


