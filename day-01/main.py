INPUT_PATH = "input.txt"
COEFFICIENT_MAP = {
	"R": 1,
	"L": -1
}

def parse_line(line):
	direction = line[0]
	coefficient = COEFFICIENT_MAP.get(direction)
	value = int(line[1:])
	return coefficient, value

def get_instructions():
	with open(INPUT_PATH) as input_file:
		for line in input_file:
			yield parse_line(line)

if __name__ == "__main__":
	current_number = 50
	count = 0
	for coefficient, value in get_instructions():
		current_number += coefficient * value
		current_number %= 100
		if current_number == 0:
			count += 1
	print(f"{count=}")

