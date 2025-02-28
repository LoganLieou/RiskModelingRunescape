import numpy as np
import matplotlib.pyplot as plt

def jump_diffusion(S0, mu, sigma, lambda_, jump_mean, jump_std, T, N):
    dt = T / N
    t = np.linspace(0, T, N)
    # Standard Brownian motion component
    W = np.random.randn(N) * np.sqrt(dt)
    # Poisson jump component
    N_t = np.random.poisson(lambda_ * dt, N)  # Number of jumps
    J = np.random.normal(jump_mean, jump_std, N) * N_t  # Jump magnitudes
    # Logarithmic return process with jumps
    S = np.zeros(N)
    S[0] = S0
    for i in range(1, N):
        dS = mu * S[i-1] * dt + sigma * S[i-1] * W[i] + S[i-1] * J[i]
        S[i] = S[i-1] + dS
    return t, S

# can probably use either MLE or ML to
# estimate some of these parameters
S0 = 34
mu = 0.32 # drift rate
sigma = 0.2 # volitility
lambda_ = 10 # jump freq
jump_mean = 0.1
jump_std = 0.05
T = 1 # time in years
N = 252 # steps

# Simulate and plot
t, S = jump_diffusion(S0, mu, sigma, lambda_, jump_mean, jump_std, T, N)
plt.plot(t, S)
plt.xlabel("Time")
plt.ylabel("Stock Price $")
plt.title("Normal (Merton) Jump Diffusion Process")
plt.show()

