from core.lcg_generator import LCG
from core.gamma_transform import gamma_from_uniforms

class GammaSimulation:

    def __init__(self, alpha, beta, seed, a, c, m):
        self.alpha = alpha
        self.beta = beta
        self.generator = LCG(seed, a, c, m)

    def generate_samples_with_trace(self, n):

        results = []

        for i in range(1, n + 1):

            uniforms = []
            seeds_used = []

            for _ in range(self.alpha):
                xi = self.generator.next_seed()
                seeds_used.append(xi)

                ri = xi / self.generator.m
                uniforms.append(ri)

            gamma_value = gamma_from_uniforms(uniforms, self.beta)

            results.append({
                "i": i,
                "Xi": seeds_used,
                "Ri": uniforms,
                "Ni": gamma_value
            })

        return results
    

def generate_samples(self, n):

    samples = []

    for _ in range(n):

        uniforms = []

        for _ in range(self.alpha):
            xi = self.generator.next_seed()
            ri = xi / self.generator.m
            uniforms.append(ri)

        gamma_value = gamma_from_uniforms(uniforms, self.beta)
        samples.append(gamma_value)

    return samples