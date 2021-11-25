def C(m: float) -> float:
    return (
        m if m in [0, 1]
        else C(m / 2) if m % 2 == 0
        else C((m + 1) / 2)
    )
