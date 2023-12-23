from Integrations.mispIntegration import *
def runManually(mispapi,mispurl,mispeventid,ioclist):
    misp_connect(mispapi,mispurl,mispeventid)
    ioclist_=list(ioclist)
    iocs=ioclist_[0].split("\r")
    for i in iocs:
        upload_attr(i.strip())