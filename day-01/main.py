import part1
import part2

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

def read_instructions():
	with open(INPUT_PATH) as input_file:
		for line in input_file:
			yield parse_line(line)

if __name__ == "__main__":
	instructions = list(read_instructions())
	part1.count_stops_at_zero(instructions)
	part2.count_zero_crossings(instructions)
