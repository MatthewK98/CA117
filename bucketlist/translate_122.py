from queue import Queue

num_trsl, num_pairs = (int(v) for v in input().split())
# build the graph
graph = dict()
for t in range(num_trsl):
    frm, to = input().split()
    graph[frm] = graph.get(frm, str()) + to

def has_path(graph, frm, to):
    """
    Return True if there is a path from 'frm' to 'to' in 'graph'.

    Uses a BFS (Breadth-First-Search)
    """

    q = Queue()
    q.put(frm)
    visited = set()
    while not q.empty():
        parent = q.get()
        if parent in visited:
            continue

        visited.add(parent)
        childs = graph.get(parent, [])
        for c in childs:
            if c == to:
                return True
            else:
                q.put(c)
    return False

for p in range(num_pairs):
    answer = True
    word_a, word_b = input().split()
    if len(word_a) != len(word_b):
        answer = False

    for char1, char2 in zip(word_a, word_b):
        if not answer:
            break
        if char1 == char2:
            continue
        if not has_path(graph, char1, char2):
            answer = False

    print('yes' if answer else 'no')
