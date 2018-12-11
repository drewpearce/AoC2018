from common import get_inputs_single_str
from common import log_runtime
from common import now_ms
import string


def challenge_08_get_nodes(inputs):
    def concat_x(val, count):
        x = val
        for _ in range(count):
            x += val
        return x

    # parse the inputs.
    inputs = [int(x) for x in inputs.split(' ')]
    nodes = []
    names = [x for x in string.ascii_uppercase]
    get_child = (False, None)
    complete_parent = False

    # loop through inputs and build the nodes object
    while inputs:
        if not names:
            count = len([x['name'] for x in nodes][-1])
            names = [concat_x(x, count) for x in string.ascii_uppercase]

        parent = get_child[1]
        if not complete_parent:
            name = names.pop(0)
            child_count = inputs.pop(0)
            meta_count = inputs.pop(0)
            if child_count == 0:
                children = None
                meta = [x for x in inputs[0: meta_count]]
                for _ in range(meta_count):
                    inputs.pop(0)
            else:
                children = []
                meta = []
                get_child = (True, name)

            nodes.append(
                {
                    'name': name,
                    'child_count': child_count,
                    'meta_count': meta_count,
                    'children': children,
                    'meta': meta,
                    'parent': parent
                }
            )

        else:
            node_id = [i for i, x in enumerate(nodes)
                       if x['name'] == parent][0]
            meta_count = nodes[node_id]['meta_count']
            meta = [x for x in inputs[0: meta_count]]
            for _ in range(meta_count):
                inputs.pop(0)
            nodes[node_id]['meta'] = meta
            parent = nodes[node_id]['parent']
            child_count = 0

        if parent:
            parent_id = [i for i, x in enumerate(nodes)
                         if x['name'] == parent][0]
            if not complete_parent:
                nodes[parent_id]['children'].append(name)
            if nodes[parent_id]['child_count'] == len(
                    nodes[parent_id]['children']) and child_count == 0:
                get_child = (False, parent)
                complete_parent = True
            elif child_count == 0:
                get_child = (True, parent)
                complete_parent = False
        else:
            complete_parent = False

    return nodes


def challenge_08_1(inputs):
    nodes = challenge_08_get_nodes(inputs)
    meta_sum = sum([sum(x['meta']) for x in nodes])
    return meta_sum


def challenge_08_2(inputs):
    nodes = challenge_08_get_nodes(inputs)

    def calcultate_node_values(node):
        id = [i for i, x in enumerate(nodes) if x['name'] == node][0]
        if nodes[id]['child_count'] == 0:
            return sum(nodes[id]['meta'])
        else:
            children = [0]
            for i in nodes[id]['meta']:
                if i > 0 and i <= nodes[id]['child_count']:
                    children.append(
                        calcultate_node_values(nodes[id]['children'][i - 1])
                    )
            return sum(children)
    root_val = calcultate_node_values('A')
    return root_val

inputs = get_inputs_single_str('day_08.txt')

start_ms = now_ms()
print('Challenge 1 results: {}'.format(challenge_08_1(inputs)))
log_runtime(start_ms)

star_ms = now_ms()
print('Challenge 2 results: {}'.format(challenge_08_2(inputs)))
log_runtime(start_ms)
