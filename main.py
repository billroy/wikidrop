# [c] 2019 Bill Roy - all rights reserved
#

print("Startup...")
print("Fetching credentials...")
try:
    import secrets
except:
    print("Please set up secrets.py")

print("Connecting to WLAN...")
import network, os, time
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('CheshireCat', 'candlebar-monkey')
while not wlan.isconnected():
    print(".")
    time.sleep_ms(500)
print("Connected:", wlan.ifconfig())

print("Configuring webserver...")
from microWebSrv import MicroWebSrv

def filenameFromPageID(pageid):
    filename = "/pages/" + str(pageid) + ".txt"
    return filename

def serveFile(httpResponse, filename):
    print("serveFile:", filename)
    try:
        os.stat(filename)
        httpResponse.WriteResponseFile(filename)
    except:
        httpResponse.WriteResponseNotFound()

@MicroWebSrv.route("/page/<pageid>", "GET")
def handleView(httpClient, httpResponse, routeArgs):
    print("GET page/%s" % routeArgs['pageid'])
    serveFile(httpResponse, filenameFromPageID(routeArgs['pageid']))

@MicroWebSrv.route("/page/<pageid>", "POST")
def handleUpdate(httpClient, httpResponse, routeArgs):
    print("POST page/%s" % routeArgs['pageid'])
    print("request length:", httpClient.GetRequestContentLength())
    content = httpClient.ReadRequestContent()
    print("request content:", content, type(content))
    filename = filenameFromPageID(routeArgs['pageid'])
    f = open(filename, 'w')
    try:
        numbytes = f.write(content)
        httpResponse.WriteResponseOk()
    except:
        httpResponse.WriteResponseInternalServerError()
        #httpResponse.WriteResponseBadReqest()
    f.close()

@MicroWebSrv.route("/list", "GET")
def handleList(httpClient, httpResponse, routeArgs=None):
    print("GET /list")
    pages = str(os.listdir("/pages"))
    httpResponse.WriteResponseOk(content=pages)

@MicroWebSrv.route("/", "GET")
def handleIndex(httpClient, httpResponse, routeArgs=None):
    print("GET /")
    serveFile(httpResponse, 'www/index.html')

mws = MicroWebSrv(webPath="/www")  
#mws.SetNotFoundPageUrl("http://" + wlan.ifconfig()[0] + "/index.html")
mws.Start(threaded=True)                               # Starts server in a new thread
print("Web server started...")
