class TruckLoad:
    def __init__(self, rate_per_mile, miles):
        self._rate_per_mile = rate_per_mile
        self._miles = miles
        self._total_rate = self._rate_per_mile * self._miles

    # --- RATE PER MILE ---
    @property
    def rate_per_mile(self):
        return self._rate_per_mile

    @rate_per_mile.setter
    def rate_per_mile(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Rate per mile must be a number.")
        if value <= 0:
            raise ValueError("Rate per mile must be positive.")
        
        self._rate_per_mile = value
        self._update_total()

    # --- MILES ---
    @property
    def miles(self):
        return self._miles

    @miles.setter
    def miles(self, value):
        if not isinstance(value, int):
            raise TypeError("Miles must be an integer.")
        if value <= 0:
            raise ValueError("Miles must be positive.")
        
        self._miles = value
        self._update_total()

    # --- TOTAL RATE (READ ONLY) ---
    @property
    def total_rate(self):
        return self._total_rate

    # --- HELPER METHOD ---
    def _update_total(self):
        self._total_rate = self._rate_per_mile * self._miles