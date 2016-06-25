def numLines(filename):
    return sum(1 for line in open(filename))

def loadData(filename, startLine, endLine, posneg=True):
    data, labels = [], []
    i = 0

    for line in open(filename, 'r'):
        if i > endLine:
            break
        elif i >= startLine:
        	obj = line.split("^")
        	if len(obj[0]) >0:
        		data.append(obj[0])

        	if posneg:
        		labels.append(obj[3])
        	else:
        		labels.append(obj[4])

        i += 1

    return data, labels
