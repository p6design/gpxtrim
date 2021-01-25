import sys
import xml.etree.ElementTree as ET
import re
import datetime
import getopt

# https://www.programiz.com/python-programming/datetime/strftime

xmltree = None

def xml_parsefile():

    global xmltree

    xmlroot = xmltree.getroot()
    t1 = xmlroot.tag
    m = re.match("{(.*)}.*",t1)
    ns1 = m.group(1)
    ns = {'d': ns1}




    starttime = ""
    endtime = "2021-01-16 11:27:10-08:00"
    b = datetime.datetime.strptime(endtime,"%Y-%m-%d %H:%M:%S%z")
    durationtime = ""

    # outer loop - find all track segments (trkseg)
    trkseg = xmlroot.findall("d:trk/d:trkseg", ns)
    print("Found {} track seg".format(len(trkseg)))
    for i in trkseg:
        x = xmlroot.findall("d:trk/d:trkseg/d:trkpt/d:time", ns)
        print("  Start Time Stamp: {}".format(x[0].text))
        print("  End Time Stamp: {}".format(x[len(x) - 1].text))

        for trkpt in i.findall("d:trkpt",ns):
            # find start timestamp


            ts = trkpt.find("d:time",ns)
            #print("  trkpt = {}, ts = {}".format(trkpt.attrib,ts.text))
            a = datetime.datetime.strptime(ts.text, "%Y-%m-%dT%H:%M:%S%z")
            delta = b - a
            if b > a:
                #print(delta)
                i.remove(trkpt)

    xmltree.write("out.xml")
    return

def main():

    global xmltree

    print("start gpxtrim")
    sXmlFile = "current.gpx"
    xmltree = ET.parse(sXmlFile)

    xml_parsefile()


if __name__ == '__main__':


    main()
    exit()
