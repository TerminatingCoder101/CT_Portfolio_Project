import numpy as np

def run_monte_carlo(S0, mu, sigma, T, N, M, theta):
    dt = T/N
    X = np.zeros((M, N+1))
    X[:,0] = S0
    for n in range(N):
        dW = np.sqrt(dt)*np.random.randn(M)
        X[:,n+1] = X[:,n]*(1 + theta*mu*dt + theta*sigma*dW)
    return X


def run_heston_monte_carlo(S0, mu, kappa, theta_v, xi, rho, T, N, M, theta_alloc):
    dt = T/N
    X = np.zeros((M, N+1))
    v = np.full(M, theta_v)
    X[:,0] = S0
    for n in range(N):
        dW1 = np.sqrt(dt)*np.random.randn(M)
        dW2 = rho*dW1 + np.sqrt(1-rho**2)*np.sqrt(dt)*np.random.randn(M)
        v = np.abs(v + kappa*(theta_v - v)*dt + xi*np.sqrt(v*dt)*dW2)
        X[:,n+1] = X[:,n]*(1 + theta_alloc*mu*dt + theta_alloc*np.sqrt(v)*dW1)
    return X
