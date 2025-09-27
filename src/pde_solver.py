import numpy as np

def solve_hjb_explicit(T, Xmax, NX, NT, r, mu, sigma, gamma):
    dX = Xmax/NX
    dt = T/NT
    X = np.linspace(0, Xmax, NX+1)
    V = np.zeros((NT+1, NX+1))
    V[-1,:] = np.log(X+1e-8)

    for n in reversed(range(NT)):
        for i in range(1, NX):
            dVdx = (V[n+1,i+1]-V[n+1,i-1])/(2*dX)
            d2Vdx2 = (V[n+1,i+1]-2*V[n+1,i]+V[n+1,i-1])/(dX**2)
            theta_star = mu/(gamma*sigma**2)
            drift = r*X[i] + theta_star*mu*X[i]
            diffusion = 0.5*(theta_star**2)*(sigma**2)*(X[i]**2)
            V[n,i] = V[n+1,i] + dt*(drift*dVdx + diffusion*d2Vdx2)
    return X, V


def solve_hjb_implicit(T, Xmax, NX, NT, r, mu, sigma, gamma, max_iter=500):
    dX = Xmax/NX
    dt = T/NT
    X = np.linspace(0, Xmax, NX+1)
    V = np.zeros((NT+1, NX+1))
    V[-1,:] = np.log(X+1e-8)

    A = np.zeros((NX-1, NX-1))
    for n in reversed(range(NT)):
        for i in range(1, NX):
            dVdx = (V[n+1,i+1]-V[n+1,i-1])/(2*dX)
            theta_star = mu/(gamma*sigma**2)
            drift = r*X[i] + theta_star*mu*X[i]
            diffusion = 0.5*(theta_star**2)*(sigma**2)*(X[i]**2)

            A[i-1,i-1] = 1 + dt*(2*diffusion/dX**2)
            if i > 1:
                A[i-1,i-2] = -dt*(diffusion/dX**2 - drift/(2*dX))
            if i < NX-1:
                A[i-1,i] = -dt*(diffusion/dX**2 + drift/(2*dX))

        b = V[n+1,1:NX]
        V[n,1:NX] = np.linalg.solve(A, b)

    return X, V
