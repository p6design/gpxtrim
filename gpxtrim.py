import sys
import xml.etree.ElementTree as ET
import re
import datetime
import getopt

xmltree = None

def xml_parsefile():

    global xmltree

    xmlroot = xmltree.getroot()
    t1 = xmlroot.tag
    m = re.match("{(.*)}.*",t1)
    ns1 = m.group(1)
    ns = {'d': ns1}
    x = xmlroot.findall("d:trk/d:trkseg/d:trkpt/d:time",ns)

    starttime = ""
    endtime = ""
    durationtime = ""

    # outer loop - find all track segments (trkseg)
    trkseg = xmlroot.findall("d:trk/d:trkseg", ns)
    print("Found {} track seg".format(len(trkseg)))
    for i in trkseg:
        for trkpt in i.findall("d:trkpt",ns):
            ts = trkpt.find("d:time",ns)
            print("  trkpt = {}, ts = {}".format(trkpt.attrib,ts.text))
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
