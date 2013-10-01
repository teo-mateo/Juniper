import json
import csv



__author__ = 'Teo hrc! Ptiu!'

jsonfile = "F:/_work/gits/juniper/static/contraptions/loto649ro.json"
csvfile = "F:/_work/gits/juniper/static/contraptions/loto649ro.csv"

input = '2 17 22 36 39 42'

def load_json():
    obj = json.loads(open(jsonfile).read())
    print obj
    print 'done loading json'
    return obj

def parse_obj(obj, input):
    res = [(1,0), (2,0), (3,0), (4,0), (5,0),(6,0)]
    in_arr = str(input).split(' ')
    for c in obj['alldraws']:
        r = 0
        for i in in_arr:
            if int(i) in c['n']:
                r += 1
        if r > 0:
            print str(c['n']) + str(r) + ' matches.'
            res[r-1] = (r, res[r][1] + 1)

    return res

def load_csv():
    with open(csvfile) as f:
        reader = csv.reader(f, delimiter=',')
        draws = list()

        for row in reader:
            draw = dict()
            draw[u'd'] = row[0]
            draw[u'n'] = [int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6])]
            draws.append(draw)

        d = dict()
        d[u'alldraws'] = draws
        return d

if __name__ == '__main__':
    obj = load_csv()
    #obj = load_json()
    print type(obj[u"alldraws"][0])
    res = parse_obj(obj, input)
    print res