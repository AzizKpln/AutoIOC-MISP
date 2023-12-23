from flask import Flask, render_template, redirect, request
from Integrations.abuseipdb import runAbuseIP
from Integrations.cinsscore import runCinsScore
from Integrations.killnet import runKillnet
from Integrations.emergingthreats import runEmergingThreats
from Integrations.honeydb import runHoneyDB
from Integrations.maltiverse import runMaltiverse
from Integrations.malware_bazar import runMalwareBazaar
from Integrations.openphish import runOpenPhish
from Integrations.phishunt import runPhishHunt
from Integrations.rescureme import runRescureMe
from Integrations.sslbl import runSSLbl
from Integrations.threatfox import runThreatFox
from Integrations.urlhaus import runURLHaus
from Integrations.virusshare import runVirusShare
from Integrations.vxvault import runVXVault
from Integrations.manual import runManually
import threading
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        operation = request.form['operation']
        if operation=="add_manually":
            return redirect("/manually")
        else:
            return redirect('/automaticlly')
    return render_template('main.html')
@app.route("/manually",methods=["GET","POST"])
def manually():
    if request.method=="POST":
        ioclist=request.form.getlist("iocList")
        mispapi=request.form["mispapi"];mispurl=request.form["mispurl"];mispeventid=request.form["mispeventid"]
        threading.Thread(target=runManually,args=(mispapi,mispurl,mispeventid,ioclist,)).start()
    return render_template("manual.html")
@app.route("/automaticlly",methods=["GET","POST"])
def automaticlly():
    if request.method=="POST":
        selected_sources = request.form.getlist('sources')
        mispapi=request.form["mispapi"];mispurl=request.form["mispurl"];mispeventid=request.form["mispeventid"]
        with open("MISP/Info","w") as f:
            f.write("MISPAPI:"+mispapi+"\n"+"MISPURL:"+mispurl+"\n"+"MISPEVENTID:"+mispeventid)
        for i in selected_sources:
            if i=="AbuseIPDB":
                with open("Selected/sources","a+") as f:
                    f.write("AbuseIPDB\n")
                threading.Thread(target=runAbuseIP,args=(mispapi,mispurl,mispeventid,)).start()
            if i=="CinsScore":
                with open("Selected/sources","a+") as f:
                    f.write("CinsScore\n")
                threading.Thread(target=runCinsScore,args=(mispapi,mispurl,mispeventid,)).start()
            if i=="KillNet":
                with open("Selected/sources","a+") as f:
                    f.write("KillNet\n")
                threading.Thread(target=runKillnet,args=(mispapi,mispurl,mispeventid,)).start()
            if i=="Emerging Threats":
                with open("Selected/sources","a+") as f:
                    f.write("Emerging_Threats\n")
                threading.Thread(target=runEmergingThreats,args=(mispapi,mispurl,mispeventid,)).start()
            if i=="HoneyDB":
                with open("Selected/sources","a+") as f:
                    f.write("HoneyDB\n")
                threading.Thread(target=runHoneyDB,args=(mispapi,mispurl,mispeventid,)).start()
            if i=="Maltiverse":
                with open("Selected/sources","a+") as f:
                    f.write("Maltiverse\n")
                threading.Thread(target=runMaltiverse,args=(mispapi,mispurl,mispeventid,)).start()
            if i=="Malware Bazaar":
                with open("Selected/sources","a+") as f:
                    f.write("Malware_Bazaar\n")
                threading.Thread(target=runMalwareBazaar,args=(mispapi,mispurl,mispeventid,)).start()
            if i=="OpenPhish":
                with open("Selected/sources","a+") as f:
                    f.write("OpenPhish\n")
                threading.Thread(target=runOpenPhish,args=(mispapi,mispurl,mispeventid,)).start()
            if i=="PhishHunt":
                with open("Selected/sources","a+") as f:
                    f.write("PhishHunt\n")
                threading.Thread(target=runPhishHunt,args=(mispapi,mispurl,mispeventid,)).start()
            if i=="RescureMe":
                with open("Selected/sources","a+") as f:
                    f.write("RescureMe\n")
                threading.Thread(target=runRescureMe,args=(mispapi,mispurl,mispeventid,)).start()
            if i=="SSLbl":
                with open("Selected/sources","a+") as f:
                    f.write("SSLbl\n")
                threading.Thread(target=runSSLbl,args=(mispapi,mispurl,mispeventid,)).start()
            if i=="ThreatFox":
                with open("Selected/sources","a+") as f:
                    f.write("ThreatFox\n")
                threading.Thread(target=runThreatFox,args=(mispapi,mispurl,mispeventid,)).start()
            if i=="URLHaus":
                with open("Selected/sources","a+") as f:
                    f.write("URLHaus\n")
                threading.Thread(target=runURLHaus,args=(mispapi,mispurl,mispeventid,)).start()
            if i=="VirusShare":
                with open("Selected/sources","a+") as f:
                    f.write("VirusShare\n")
                threading.Thread(target=runVirusShare,args=(mispapi,mispurl,mispeventid,)).start()
            if i=="VXVault":
                with open("Selected/sources","a+") as f:
                    f.write("VXVault\n")
                threading.Thread(target=runVXVault,args=(mispapi,mispurl,mispeventid,)).start()
        return render_template("integrations.html",selected_sources=selected_sources)
    return render_template("index.html")
if __name__ == '__main__':
    app.run("0.0.0.0",debug=True)
