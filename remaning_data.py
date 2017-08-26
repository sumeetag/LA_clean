

d = set()


with open("./data/la_geo_output.txt", 'r') as f:
    for line in f:
        d.add(line)

print len(d)

with open("./data/la_geo_output_non_duplicate.txt", "w") as f2:
    for i in d:
        f2.write(i)



#
# d = set()
#
# with open("./data/la_geo_output_non_duplicate.txt", 'r') as f1:
#      for line in f1:
#          data = line.strip().split(";")
#          l = ";".join(data[:-2])
#          d.add(l.strip())
#
#
# print len(d)
#
# with open("./data/la_geo_remaining.txt", "w") as f2:
#     with open("./data/la_geo_non_duplicate.txt", 'r') as f:
#          for line in f:
#              if line.strip() not in d:
#                  #print line
#                  f2.write(line)

