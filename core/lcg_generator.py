# core/lcg_generator.py

class LinearCongruentialGenerator:
    """
    Mathematical PRNG using:
    X_{n+1} = (aX_n + c) mod m
    R_n = X_n / m
    """

    def __init__(self, seed: int, a: int, c: int, m: int):
        if m <= 0:
            raise ValueError("Modulus must be positive.")

        self.current = seed
        self.a = a
        self.c = c
        self.m = m

    def next_int(self) -> int:
        self.current = (self.a * self.current + self.c) % self.m
        return self.current

    def next_uniform(self) -> float:
        return self.next_int() / self.m

    def generate(self, n: int):
        return [self.next_uniform() for _ in range(n)]
    

class LCG:

    def __init__(self, seed, a, c, m):
        self.current = seed
        self.a = a
        self.c = c
        self.m = m

    def next_seed(self):
        self.current = (self.a * self.current + self.c) % self.m
        return self.current

    def random(self):
        return self.next_seed() / self.m