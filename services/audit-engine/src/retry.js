// src/retry.js
export class CircuitBreaker {
  constructor({ failureThreshold = 5, resetTimeout = 60000, timeout = 30000 } = {}) {
    this.failureThreshold = failureThreshold;
    this.resetTimeout = resetTimeout;
    this.timeout = timeout;
    this.failures = 0;
    this.lastFailureTime = null;
    this.state = "closed";
  }

  async execute(fn) {
    if (this.state === "open") {
      if (Date.now() - this.lastFailureTime > this.resetTimeout) {
        this.state = "half-open";
      } else {
        throw new Error("Circuit breaker open");
      }
    }
    try {
      const result = await Promise.race([
        fn(),
        new Promise((_, reject) => setTimeout(() => reject(new Error("Timeout")), this.timeout))
      ]);
      this.onSuccess();
      return result;
    } catch (err) {
      this.onFailure();
      throw err;
    }
  }

  onSuccess() { this.failures = 0; this.state = "closed"; }
  onFailure() {
    this.failures++;
    this.lastFailureTime = Date.now();
    if (this.failures >= this.failureThreshold) this.state = "open";
  }
}

export async function exponentialBackoff(fn, maxRetries = 3, baseDelay = 1000) {
  for (let i = 0; i <= maxRetries; i++) {
    try { return await fn(); } 
    catch (err) {
      if (i === maxRetries) throw err;
      await new Promise(r => setTimeout(r, baseDelay * Math.pow(2, i) + Math.random() * 1000));
    }
  }
}
