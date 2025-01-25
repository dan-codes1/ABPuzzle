import sys
import heapq
import random

class ABPuzzle:
    def __init__(self, n: int, large_disks: [int], small_disks: [int]):
        self.n = n
        self.large_disks = large_disks
        self.small_disks = small_disks
        self.goal_state = self.compute_goal_state()

    def compute_goal_state(self) -> [int]:
        goal = []
        for i in range(1, self.n + 1):
            goal.extend([i] * self.n)
        goal.append(0)
        return goal

    def heuristic(self, state: [int]) -> int:
        sum = 0
        for i in range(0, n - 1):
            if state[i] != self.goal_state[i]:
                sum += 1
        return sum

    def get_neighbors(self, state: [int]) -> [[int]]:
        zero_index = state.index(0)
        k = self.large_disks[zero_index]
        neighbors = []

        def swap_and_create(new_index: int):
            new_state = state[:]
            # swap the disks
            new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
            neighbors.append(new_state)

        swap_and_create((zero_index - k) % len(state))
        swap_and_create((zero_index + k) % len(state))
        swap_and_create((zero_index - 1) % len(state))
        swap_and_create((zero_index + 1) % len(state))
        return neighbors

    def solve(self) -> [[int]]:
        initial_state = self.small_disks
        if initial_state == self.goal_state:
            return [initial_state]

        priority_queue: [(int, [int])] = []  # min-heap for best first search
        heapq.heappush(priority_queue, (self.heuristic(initial_state), initial_state))

        visited: set[tuple[int]] = set() # using tuples instead of arrays because they are hashable for sets
        visited.add(tuple(initial_state))

        # to help reconstruct the solution path. Key is the state, value is the parent of the state.
        parent_map: dict[(int), [int]] = {tuple(initial_state): None}

        while priority_queue:
            _, current_state = heapq.heappop(priority_queue)

            for neighbor in self.get_neighbors(current_state):
                neighbor_tuple = tuple(neighbor)
                if neighbor_tuple not in visited:
                    visited.add(neighbor_tuple)
                    parent_map[neighbor_tuple] = current_state

                    if neighbor == self.goal_state: # solved!
                        return self.reconstruct_path(parent_map, neighbor)

                    heapq.heappush(priority_queue, (self.heuristic(neighbor), neighbor))
        return None  # no solution

    def reconstruct_path(self, parent_map: dict[(int), [int]], end_state: [int]) -> [[int]]:
        path = []
        current = end_state
        while current is not None:
            path.append(current)
            current = parent_map[tuple(current)]
        path.reverse()
        return path


def generate_disks(n: int) -> ([int], [int]):
    large_disks = [random.randint(1, 4) for _ in range(n ** 2)]
    large_disks.append(random.randint(1, 4))  # n^2 + 1

    small_disks = []
    for i in range(1, n + 1):
        small_disks.extend([i] * n)
    small_disks.append(0)  # The uncovered small disk
    random.shuffle(small_disks)
    random.shuffle(large_disks)
    return large_disks, small_disks

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python index.py <number_of_disks>")
        sys.exit(1)

    n = int(sys.argv[1])
    large_disks, small_disks = generate_disks(n)

    print("Large disks:", large_disks)
    print("Small disks:", small_disks)

    # solver = ABPuzzle(3, [1, 2, 3, 4, 1, 2, 3, 1, 2, 3], [1, 1, 1, 3, 2, 2, 3, 3, 0, 2])
    solver = ABPuzzle(n, large_disks, small_disks)
    solution = solver.solve()
    print()
    if solution:
        print("Solution is")
        for state in solution:
            print(" ".join(map(str, state)))
    else:
        print("No solution")
