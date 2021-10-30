import lxml.etree as ET
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
repo_ver = {}
def getVersion(xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    for item in root.iter('project'):
        name = item.attrib['name']
        revision = item.attrib['revision']
        repo_ver[name] = revision
        print(name)
        print(revision)
    pass
def parseXML(xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    print(root.tag)
    container = root.find('.//manifest')

    for item in root.iter('project'):
        name = item.attrib['name']
        if name in repo_ver.keys():
            item.attrib['revision'] = repo_ver[name]
            print(name)

    tree.write('out.xml', encoding="utf-8")


def main():
    getVersion('./snapshot/snapshot_wk2141.xml')
    parseXML('./aosp.xml')


if __name__ == "__main__":
    main()
