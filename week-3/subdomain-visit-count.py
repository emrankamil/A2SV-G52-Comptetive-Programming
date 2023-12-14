class Solution:
    def subdomainVisits(self, cpdomains) :
        domain_counter = {}

        for i in cpdomains:
            lst = i.split()
            visitors = int(lst[0])
            domain = lst[1]

            # Split the domain into subdomains and count the visits directly
            subdomains = domain.split('.')
            for j in range(len(subdomains)):
                subdomain = '.'.join(subdomains[j:])
                if subdomain not in domain_counter:
                    domain_counter[subdomain] = visitors
                else:
                    domain_counter[subdomain] += visitors

        output = []
        for i in domain_counter:
            domain_count = str(domain_counter[i]) + " " + i
            output.append(domain_count)

        return output