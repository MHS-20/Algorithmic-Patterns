def can_complete_circuit(A, B):
    total_gas = sum(A)
    total_cost = sum(B)

    if total_gas < total_cost:
        return -1

    start = 0
    tank = 0

    for i in range(len(A)):
        tank += A[i] - B[i]
        if tank < 0:
            start = i + 1
            tank = 0

    return start

