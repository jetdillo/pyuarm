import re
__version__ = '2.3.0.11'
support_versions = ['2.2','2.3','3.2']
""" @5 V1                                                                                      
@6 N0 V1                                                                                   
@1 """

def is_a_version(version):
    print "version=%s" % version
    version_pattern = re.compile(r'\d+\.\d+\.\d+\w*')
    if version_pattern.match(version):
        return True
    else:
        return False


def is_supported_version(version):
    pattern = re.compile(r'\d+\.\d+')
    major_version = pattern.match(version).group()
    for v in support_versions:
        print "major_version=%s read version=%s" % (major_version,v)
        if major_version == v:
            return True
    return False
