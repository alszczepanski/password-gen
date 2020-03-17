import generator as g


easy = g.generate_lists(200,12,0)
average = g.generate_lists(200,12,1)
hard = g.generate_lists(200,12,2)

g.export_to_file(easy,'easy-pass.txt')
g.export_to_file(average,'average-pass.txt')
g.export_to_file(hard,'hard-pass.txt')

