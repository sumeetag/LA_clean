d = {}

with open("./data/la_geo_non_duplicate.txt", 'r') as f:
    for line in f:

        data = line.strip().split(";")
        try:
            zip = int(float(str(data[27])))
            if zip in d:
                d[zip] += 1
            else:
                d[zip] = 1
        except:
            continue


        #break

print d

flag = 0
with open("./data/2010_Census_Populations_by_Zip_Code_unclean_data.csv", 'w') as f1:
    with open("./data/2010_Census_Populations_by_Zip_Code.csv", 'r') as f:
        for line in f:
            if flag == 0:
                flag = 1
                continue
            data = line.strip().split(",")
            if int(data[0]) in d:
                f1.write(",".join(data) + "," + str(d[int(data[0])]) + "\n")
            else:
                f1.write(",".join(data) + "," + "0" + "\n")



