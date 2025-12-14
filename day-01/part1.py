"""
https://adventofcode.com/2025/day/1
"""

def count_stops_at_zero(instructions):
	current_number = 50
	count = 0
	for coefficient, value in instructions:
		current_number += coefficient * value
		current_number %= 100
		if current_number == 0:
			count += 1
	print(f"Part 1: {count=}")
