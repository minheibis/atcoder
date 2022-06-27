from collections import defaultdict

def constant_factory(value):
    return lambda: value

d = defaultdict(constant_factory('<missing>'))
print("d", d)
d.update(name="John", action="ran")
print("d", d)

print('%(name)s %(action)s to %(object)s' % d)