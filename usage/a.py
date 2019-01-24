import funniest
print(funniest.joke())

import pkgutil
greeting = pkgutil.get_data("funniest", 'data/greeting.txt')
print(greeting)

