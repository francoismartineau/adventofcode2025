"""
https://adventofcode.com/2025/day/1#part2
"""

def count_zero_crossings(instructions):
	current_number = 50
	count = 0
	for coefficient, value in instructions:
		for _ in range(value):
			current_number += coefficient
			current_number %= 100
			count += (current_number == 0)
	print(f"Part 2: {count=}")
