import csv
import json
import xml.etree.ElementTree as ET


class MyDialect(csv.Dialect):
    quoting = csv.QUOTE_ALL
    quotechar = '^'
    delimiter = '*'
    lineterminator = '\n'


csv.register_dialect('mydialect', MyDialect)

fl = ['name', 'surname', 'date of birthday', 'place of living']


def write(name):
    x = '1'
    with open(name, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fl, dialect='mydialect')
        writer.writeheader()
        while x == '1':
            name = input('name: ')
            surname = input('surname: ')
            birthday = input('date of birthday: ')
            place = input('place of living: ')
            writer.writerow({
                'name': name,
                'surname': surname,
                'date of birthday': birthday,
                'place of living': place
            })
            x = input("To continue press '1', to exit press any key")


def add_str(name):
    x = '1'
    with open(name, 'a') as f:
        writer = csv.DictWriter(f, fieldnames=fl, dialect='mydialect')
        while x == '1':
            name = input('name: ')
            surname = input('surname: ')
            birthday = input('date of birthday: ')
            place = input('place of living: ')
            writer.writerow({
                'name': name,
                'surname': surname,
                'date of birthday': birthday,
                'place of living': place
            })
            x = input("To continue press '1', to exit press any key")


def read(name):
    with open(name, 'r') as f:
        for line in f:
            print(line)


def convert_json(name):
    sd = []
    s =[]
    with open(name, 'r') as f:
        l = f.readline()
        l = l.split('*')
        l[3] = l[3][:-1]
        for element in l:
            element = element[1:-1]
            sd.append(element)
        for line in f:
            d = dict()
            line = line.split(('*'))
            line[0] = line[0][1:-1]
            d[sd[0]] = line[0]
            line[1] = line[1][1:-1]
            d[sd[1]] = line[1]
            line[2] = line[2][1:-1]
            d[sd[2]] = line[2]
            line[3] = line[3][1:-2]
            d[sd[3]] = line[3]
            s.append(d)
    name = name[:-3] + 'json'
    with open(name, 'w') as f:
        json.dump(s, f, indent=4)


def convert_xml(name):
    s = []
    with open(name, 'r') as f:
        # l = f.readline()
        # l = l.split('*')
        # l[3] = l[3][:-1]
        # for element in l:
        #     element = element[1:-1]
        #     s.append(element)
        for line in f:
            x = []
            line = line.split(('*'))
            line[0] = line[0][1:-1]
            x.append(line[0])
            line[1] = line[1][1:-1]
            x.append(line[1])
            line[2] = line[2][1:-1]
            x.append(line[2])
            line[3] = line[3][1:-2]
            x.append(line[3])
            s.append(x)
        del s[0]
    name = name[:-3] + 'xml'
    dat = ET.Element('data')
    for person in s:
        p = ET.SubElement(dat, 'person')
        n = ET.SubElement(p, 'name ')
        nc = ET.Comment(person[0])
        n.append(nc)
        f = ET.SubElement(p, 'surname ')
        fc = ET.Comment(person[1])
        f.append(fc)
        d = ET.SubElement(p, 'date of birthday ')
        dc = ET.Comment(person[2])
        d.append(dc)
        v = ET.SubElement(p, 'place of living ')
        vc = ET.Comment(person[3])
        v.append(vc)
    tree = ET.ElementTree(dat)
    ET.indent(dat, space=' ', level=2)
    tree.write(name)

convert_xml('data.csv')
