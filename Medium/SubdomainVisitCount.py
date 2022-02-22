class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        def find_dot_positions(string):
            positions = []
            for i, ch in enumerate(string):
                if ch == '.':
                    positions.append(i)

            return positions

        results = []
        counter = {}

        for cp in cpdomains:
            count = cp.split()[0]
            domain = cp.split()[1]

            counter[domain] = counter.get(domain, 0) + int(count)

            dot_positions = find_dot_positions(domain)
            for dot_position in dot_positions:
                sub_domain = domain[dot_position + 1:]
                counter[sub_domain] = counter.get(sub_domain, 0) + int(count)

        for key, value in counter.items():
            results.append(str(value) + " " + key)

        return results