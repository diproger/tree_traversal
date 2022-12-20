def construct_tree(nodes: dict, levels: set, tree: dict):
    for level in levels:
        tree[level] = construct_tree(nodes, nodes[level], {})
    return tree


def to_tree(source: list) -> dict:
    tree_nodes = {root: set() for row in source for root in row if root}
    tree_roots = set()
    for parent, child in source:
        if not parent:
            tree_roots.add(child)
            continue
        tree_nodes[parent].add(child)
    return construct_tree(nodes=tree_nodes, levels=tree_roots, tree={})


if __name__ == '__main__':
    source = [
        (None, 'a'),
        (None, 'b'),
        (None, 'c'),
        ('a', 'a1'),
        ('a', 'a2'),
        ('a2', 'a21'),
        ('a2', 'a22'),
        ('b', 'b1'),
        ('b1', 'b11'),
        ('b11', 'b111'),
        ('b', 'b2'),
        ('c', 'c1'),
    ]
    expected = {
        'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
        'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
        'c': {'c1': {}},
    }
    result = to_tree(source)
    assert result == expected