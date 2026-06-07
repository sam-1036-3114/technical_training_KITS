"""
Sample file to trigger Copilot inline suggestions.

Type inside the function bodies and wait ~1-2s for suggestions.
Accept suggestions with Tab or Right Arrow.

If Copilot still doesn't suggest, follow COPILOT-HELP.md in the workspace root.
"""

def add(a, b):
	"""Return the sum of two numbers."""
	return a + b

def factorial(n):
	"""Return factorial of n (n!)."""
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)

def fibonacci(n):
	"""Return first n Fibonacci numbers as a list."""
	fib_sequence = []
	a, b = 0, 1
	for _ in range(n):
		fib_sequence.append(a)
		a, b = b, a + b
	return fib_sequence

class MathUtils:
	def is_prime(self, x):
		"""Return True if x is prime."""
		if x <= 1:
			return False
		for i in range(2, int(x**0.5) + 1):
			if x % i == 0:
				return False
		return True
# enter the 2 lines of codep
