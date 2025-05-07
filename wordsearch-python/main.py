import random

SIZE = 10
WORDS = ["cat", "dog", "lion", "bat", "tiger"]
WORDS_TO_PLACE = 5
DIRS = [(0, 1), (1, 0), (1, 1), (-1, 1)]  # Right, Down, Diagonal, Up-Right

grid = [['.' for _ in range(SIZE)] for _ in range(SIZE)]
placed_words = []

def can_place(word, x, y, dx, dy):
    for i in range(len(word)):
        nx, ny = x + dx * i, y + dy * i
        if not (0 <= nx < SIZE and 0 <= ny < SIZE):
            return False
        if grid[nx][ny] != '.' and grid[nx][ny] != word[i]:
            return False
    return True

def place_word(word):
    for _ in range(100):
        x = random.randint(0, SIZE - 1)
        y = random.randint(0, SIZE - 1)
        dx, dy = random.choice(DIRS)
        if can_place(word, x, y, dx, dy):
            for i in range(len(word)):
                grid[x + dx * i][y + dy * i] = word[i]
            placed_words.append(word)
            return

def fill_random_letters():
    for i in range(SIZE):
        for j in range(SIZE):
            if grid[i][j] == '.':
                grid[i][j] = chr(random.randint(ord('a'), ord('z')))

def print_grid():
    for row in grid:
        print(' '.join(row))

def search_all_words():
    found_words = set()
    for word in WORDS:
        l = len(word)
        for x in range(SIZE):
            for y in range(SIZE):
                for dx, dy in DIRS:
                    found = True
                    for i in range(l):
                        nx, ny = x + dx * i, y + dy * i
                        if not (0 <= nx < SIZE and 0 <= ny < SIZE):
                            found = False
                            break
                        if grid[nx][ny] != word[i]:
                            found = False
                            break
                    if found:
                        found_words.add(word)
    return found_words

# ---- Main Execution ----
random.seed(42)  # Fixed seed for consistent output

for word in random.sample(WORDS, WORDS_TO_PLACE):
    place_word(word)

fill_random_letters()

print("Word Search Grid:")
print_grid()

print("\n AI Solver Found:")
found = search_all_words()
for word in sorted(found):
    print(f"- {word}")
