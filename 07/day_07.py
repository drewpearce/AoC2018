import string


def parse_challenge_07_inputs(inputs):
    order_rules = []
    for rule in inputs:
        f = rule.split(' ')[1]
        l = rule.split('step ')[1][0]
        order_rules.append(
            {
                'f': f,
                'l': l
            }
        )

    return order_rules


def challenge_07_1(inputs):
    rules = parse_challenge_07_inputs(inputs)
    all_used_ltrs = set([r['f'] for r in rules] + [r['l'] for r in rules])
    afters = {l: sorted([x['f'] for x in rules if x['l'] == l])
              for l in all_used_ltrs}
    out = ''
    while len(out) < len(all_used_ltrs):
        possible = sorted(
            [k for k, v in afters.items() if v == [] and k not in out]
        )
        out += possible[0]
        for k, v in afters.items():
            if possible[0] in v:
                afters[k].remove(possible[0])
    return out


def challenge_07_2(inputs, workers, time_mod):
    times = {v: i + 1 + time_mod for i, v in enumerate(string.ascii_uppercase)}
    rules = parse_challenge_07_inputs(inputs)
    all_used_ltrs = set([r['f'] for r in rules] + [r['l'] for r in rules])
    afters = {l: sorted([x['f'] for x in rules if x['l'] == l])
              for l in all_used_ltrs}
    out = []
    workers = {
        x: {'start': None, 'end': None, 'working': False, 'ltr': 0}
        for x in range(0, workers)
    }
    time = 0
    while len(all_used_ltrs) > 0:
        for w in workers:
            if workers[w]['working'] is True:
                if workers[w]['end'] == time:
                    for k, v in afters.items():
                        if workers[w]['ltr'] in v:
                            afters[k].remove(workers[w]['ltr'])
                    workers[w]['working'] = False
                    all_used_ltrs.remove(workers[w]['ltr'])
        possible = sorted(
            [k for k, v in afters.items() if v == [] and k not in out]
        )
        for x in possible:
            avail = [k for k, v in workers.items() if v['working'] is False]
            if avail:
                wkr = avail[0]
                workers[wkr]['start'] = time
                workers[wkr]['end'] = time + times[x]
                workers[wkr]['working'] = True
                workers[wkr]['ltr'] = x
                out.append(x)
        time += 1
    return time - 1
