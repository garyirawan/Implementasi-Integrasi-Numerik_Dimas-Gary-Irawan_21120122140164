import numpy as np
import time

def trapezoid_integration(f, a, b, N):
    h = (b - a) / N
    x = np.linspace(a, b, N+1)
    y = f(x)
    integral = (h / 2) * np.sum(y[0] + 2 * np.sum(y[1:-1]) + y[-1])
    return integral

def f(x):
    return 4 / (1 + x**2)

# Nilai referensi pi
pi_ref = 3.14159265358979323846

# Variasi nilai N
N_values = [10, 100, 1000, 10000]

# Hasil dan pengukuran waktu
results = []
times = []

for N in N_values:
    start_time = time.time()
    pi_approx = trapezoid_integration(f, 0, 1, N)
    end_time = time.time()
    
    rms_error = np.sqrt((pi_ref - pi_approx) ** 2)
    execution_time = end_time - start_time
    
    results.append((N, pi_approx, rms_error, execution_time))
    times.append(execution_time)

# Cetak hasil
for result in results:
    N, pi_approx, rms_error, execution_time = result
    print(f"N = {N:5d} | Pi Approximation = {pi_approx:.15f} | RMS Error = {rms_error:.15f} | Execution Time = {execution_time:.8f} seconds")
    