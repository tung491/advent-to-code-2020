import re



def main():
    with open('input/d16') as f:
        secs = f.read().split('\n\n')
    validator_groups = {}
    validators = []
    for rule_line in secs[0].splitlines():
        name, range_str = rule_line.split(':')
        ranges = [range(int(lo), int(hi) + 1)
                  for lo, hi in re.findall(r'(\d+)-(\d+)', range_str)]
        validators.extend(ranges)
        validator_groups[name] = ranges

    rs1 = 0
    valid_tickets = []
    for ticket in secs[2].splitlines()[1:]:
        vals = map(int, ticket.split(','))
        is_valid = True
        for val in vals:
            if all(val not in valid_range for valid_range in validators):
                rs1 += val
                is_valid = False
        if is_valid:
            valid_tickets.append(ticket)

    print(f'Part 1: {rs1}')
    valid_combs = set()
    remain_rows = list(range(validator_groups))
    while remain_rows:



if __name__ == '__main__':
    main()
