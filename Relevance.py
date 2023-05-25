class Relevance:
    def __init__(self):
        self.unemployment = None
        self.ethic = None
        self.security = None
        self.regulation = None
        self.potential = None

    def __str__(self):
        return "Desemprego: {} - Ética: {} - Segurança: {} - Regulação: {} - Potencial: {}".format(
            self.unemployment, self.ethic, self.security, self.regulation, self.potential
        )
