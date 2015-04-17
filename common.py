#############################################################################
#############################################################################
import os,xbmc,xbmcgui,xbmcaddon,sys,logging,re,urllib,urllib2,htmllib,xbmcplugin,xbmcvfs,string,StringIO,random,array,time,datetime,mimetypes
try: 			from addon.common.addon 				import Addon
except:
	try: 		from t0mm0.common.addon 				import Addon
	except: 
		try: from z_t0mm0_common_addon 				import Addon
		except: pass
try: 			from addon.common.net 					import Net
except:
	try: 		from t0mm0.common.net 					import Net
	except: 
		try: from z_t0mm0_common_net 					import Net
		except: pass
net2=Net(); 
#############################################################################
#############################################################################
addon=xbmcaddon.Addon(); 
def aINFO(s,d=''):
	try: return addon.getAddonInfo(s)
	except: return d
addon_id   =addon.getAddonInfo('id'); 
addon_name =addon.getAddonInfo('name'); 
addon_path =addon.getAddonInfo('path'); addon_path8=addon.getAddonInfo('path').decode("utf-8"); 
#MediaPath  =xbmc.translatePath( os.path.join(addon_path8,'resources','skins','default','media').encode("utf-8") ).decode("utf-8"); 
MediaPath  =xbmc.translatePath( os.path.join(addon_path,'resources','skins','default','media') ); 
addonIcon  =addon.getAddonInfo('icon'); 
addonFanart=addon.getAddonInfo('fanart'); 
addon_profile=addon.getAddonInfo('profile'); 
def tP(p): return xbmc.translatePath(p)
addonPath=addon_path; addonId=addon_id; addonName=addon_name; addonUserDataPath=addon_profile; addonUserDataPathTP=tP(addon_profile); 
ADDON=Addon(addon_id,sys.argv); 
#############################################################################
#############################################################################
def MediaFile(n,e='',p=MediaPath): return os.path.join(p,n+e)
def MediaFileP(n,e='',p=MediaPath): return MediaFile(n,e='.png')
def MediaFileG(n,e='',p=MediaPath): return MediaFile(n,e='.gif')
def MediaFileJ(n,e='',p=MediaPath): return MediaFile(n,e='.jpg')
def getSet(id,d=''): 
    try: return addon.getSetting(id)
    except: return d
def setSet(id,v): 
    try: return addon.setSetting(id,v)
    except: pass
def tfalse(r,d=False): ## Get True / False
	if   (r.lower()=='true' ) or (r.lower()=='t') or (r.lower()=='y') or (r.lower()=='1') or (r.lower()=='yes'): return True
	elif (r.lower()=='false') or (r.lower()=='f') or (r.lower()=='n') or (r.lower()=='0') or (r.lower()=='no'): return False
	else: return d
def isPath(path): return os.path.exists(path)
def isFile(filename): return os.path.isfile(filename)
def deb(a,b):
	try: print "%s:  %s"%(str(a),str(b))
	except: pass
def debob(o):
	try: print o
	except: pass
def nolines(t):
	it=t.splitlines(); t=''
	for L in it: t=t+L
	t=((t.replace("\r","")).replace("\n",""))
	return t
def cFL( t,c='tan'): ### For Coloring Text ###
	try: return '[COLOR '+c+']'+t+'[/COLOR]'
	except: pass
def cFL_(t,c='tan'): ### For Coloring Text (First Letter-Only) ###
	try: return '[COLOR '+c+']'+t[0:1]+'[/COLOR]'+t[1:]
	except: pass
def DoE(e): xbmc.executebuiltin(e)
def DoAW(e): xbmc.executebuiltin("ActivateWindow(%s)"%str(e))
def DoRW(e): xbmc.executebuiltin("ReplaceWindow(%s)"%str(e))
def DoRA(e): xbmc.executebuiltin("RunAddon(%s)"%str(e))
def DoRA2(e,e2="1",e3=""): xbmc.executebuiltin('RunAddon(%s,"%s","%s")'%(str(e),str(e2),e3)); 
def DoRS(e): xbmc.executebuiltin("RunScript(%s)"%str(e))
def DoRP(e): xbmc.executebuiltin("RunPlugin(%s)"%str(e))
def DoA(a): xbmc.executebuiltin("Action(%s)"%str(a))
def DoCM(a): xbmc.executebuiltin("Control.Message(windowid=%s)"%(str(a)))
def DoSC(a): xbmc.executebuiltin("SendClick(%s)"%(str(a)))
def DoSC2(a,Id): xbmc.executebuiltin("SendClick(%s,%s)"%(str(a),str(Id)))
def DoStopScript(e): xbmc.executebuiltin("StopScript(%s)"%str(e))
def showAddonSettings(): addon.openSettings()
def note(title='',msg='',delay=5000,image='http://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/US_99_%281961%29.svg/40px-US_99_%281961%29.svg.png'): xbmc.executebuiltin('XBMC.Notification("%s","%s",%d,"%s")'%(title,msg,delay,image))
def popYN(title='',line1='',line2='',line3='',n='',y=''):
	diag=xbmcgui.Dialog()
	r=diag.yesno(title,line1,line2,line3,n,y)
	if r: return r
	else: return False
	#del diag
def popOK(msg="",title="",line2="",line3=""):
	dialog=xbmcgui.Dialog()
	#ok=dialog.ok(title,msg,line2,line3)
	dialog.ok(title,msg,line2,line3)
def FileSAVE(path,data): file=open(path,'w'); file.write(data); file.close()
def FileOPEN(path,d=''):
	try:
		#deb('File',path)
		if os.path.isfile(path): ## File found.
			#deb('Found',path)
			file = open(path, 'r')
			contents=file.read()
			file.close()
			return contents
		else: return d ## File not found.
	except: return d
def FolderNEW(dir_path):
	dir_path=dir_path.strip()
	if not os.path.exists(dir_path): os.makedirs(dir_path)
def FolderLIST(mypath,dirname): #...creates sub-directories if they are not found.
	subpath=os.path.join(mypath,dirname)
	if not os.path.exists(subpath): os.makedirs(subpath)
	return subpath
def dOmd5(s,d='TempFile'):
	import md5; 
	try: return md5.new(s).hexdigest()
	except: return d
def getURL(url,d=''):
	try:
		req=urllib2.Request(url)
		req.add_header('User-Agent',ps('User-Agent')) 
		response=urllib2.urlopen(req)
		link=response.read()
		response.close()
		return(link)
	except: deb('Failed to fetch url',''); return d
def getURL_WithCaching(url,d=''):
	try:
		tempFileName=addonPath2('zzz_'+dOmd5(url),'.txt')
		req=urllib2.Request(url)
		req.add_header('User-Agent',ps('User-Agent')) 
		response=urllib2.urlopen(req)
		link=response.read()
		response.close()
		if (len(link) > 0) and ('<?xml version="1.0" encoding="UTF-8"?>' in link):
			FileSAVE(tempFileName,link)
			return(link)
		elif (len(link) > 0):
			debob("The url has returned without the propper xml coding.")
		else:
			debob("The url has returned with a blank string.")
	except: deb('Failed to fetch url',''); link=d
	try:
		if isFile(tempFileName)==True:
			debob("Attempting to retreive the url from previous cached file.")
			link=FileOPEN(tempFileName)
			note("Getting url.","Using cached file.",2000,addonIcon)
		else:
			debob("No previous cached file exists.")
		return link
	except: 
		deb('Failed to fetch url**',''); 
		try: return link
		except: return d
def postURL(url,form_data={},headers={},compression=True):
	try:
		req=urllib2.Request(url)
		if form_data: form_data=urllib.urlencode(form_data); req=urllib2.Request(url,form_data)
		req.add_header('User-Agent',ps('User-Agent'))
		for k, v in headers.items(): req.add_header(k, v)
		if compression: req.add_header('Accept-Encoding', 'gzip')
		response=urllib2.urlopen(req)
		link=response.read()
		response.close()
		return link
	except: deb('Failed to fetch url',''); return ''
def postURL2(url,form_data={}):
	try:
		postData=urllib.urlencode(form_data)
		req=urllib2.Request(url,postData)
		req.add_header('User-Agent', ps('User-Agent')) 
		response=urllib2.urlopen(req)
		link=response.read()
		response.close()
		return(link)
	except: deb('Failed to fetch url',''); return ''
def showkeyboard(txtMessage="",txtHeader="",passwordField=False):
	try:
		if txtMessage=='None': txtMessage=''
		keyboard = xbmc.Keyboard(txtMessage, txtHeader, passwordField)#("text to show","header text", True="password field"/False="show text")
		keyboard.doModal()
		if keyboard.isConfirmed(): return keyboard.getText()
		else: return '' #return False
	except: return ''
def art(f,fe=''): 
	fe1='.png'; fe2='.jpg'; fe3='.gif'; 
	if   fe1 in f: f=f.replace(fe1,''); fe=fe1; 
	elif fe2 in f: f=f.replace(fe2,''); fe=fe2; 
	elif fe3 in f: f=f.replace(fe3,''); fe=fe3; 
	return xbmc.translatePath(os.path.join(addonPath,'art',f+fe))
def artp(f,fe='.png'): 
	return art(f,fe)
def artj(f,fe='.jpg'): 
	return art(f,fe)
def addonPath2(f,fe=''):
	return xbmc.translatePath(os.path.join(addonPath,f+fe))
def get_xbmc_os():
	try: xbmc_os=str(os.environ.get('OS'))
	except:
		try: xbmc_os=str(sys.platform)
		except: xbmc_os="unknown"
	return xbmc_os
def doCtoS(c,s="",d=""): ## Put's an array (Example: [68,68,68,68]) into a string, converting each number in the array into it's character form to make up a string.
	try:
		if len(c)==0: return d
		for k in range(0,len(c)):
			s+=str(chr(c[k]))
	except: return d
#############################################################################
#############################################################################
def SKgetStringValue(Tag,ErResult=''): 
    try: return xbmc.getInfoLabel('Skin.String('+Tag+')')
    except: return ErResult
def SKchange(Tag,NewValue=''):  xbmc.executebuiltin('Skin.SetString('+Tag+', %s)' % NewValue)
def SKnchange(Tag,NewValue=0):  xbmc.executebuiltin('Skin.SetNumeric('+Tag+', %s)' % NewValue)
def SKgchange(Tag,NewValue=''):  xbmc.executebuiltin('Skin.SetImage('+Tag+', %s)' % NewValue)
def SKgLchange(Tag,NewValue=''):  xbmc.executebuiltin('Skin.SetLargeImage('+Tag+', %s)' % NewValue)
def SKbchange(Tag,NewValue=False):  xbmc.executebuiltin('Skin.SetBool('+Tag+', %s)' % NewValue)
def SKtchange(Tag,NewValue=False):  xbmc.executebuiltin('Skin.ToggleSetting('+Tag+', %s)' % NewValue)
def SKsetStringValue(Tag,NewValue=''):  xbmc.executebuiltin('Skin.SetString('+Tag+', %s)' % NewValue)
#############################################################################
#############################################################################
from base64 import b64decode
from base64 import b64encode
def DecodeUrlB64(link):
	try: return link.decode('base-64')
	except: return link
def EncodeUrlB64(link):
	try: return link.encode('base-64')
	except: return link
#############################################################################
#############################################################################
def PlaySndWav(f,e='.wav'):
	try:
		if f.endswith(e)==False: f+=e
		xbmc.playSFX(tP(os.path.join(MediaPath,'snd',f)),useCached=True)
	except: pass















#############################################################################
#############################################################################
def XBMC_UpdateLocalAddons(): 	xbmc.executebuiltin("XBMC.UpdateLocalAddons()")
def XBMC_System_Exec(url): 			xbmc.executebuiltin("XBMC.System.Exec(%s)"%url)
def XBMC_System_ExecWait(url): 	xbmc.executebuiltin("XBMC.System.ExecWait(%s)"%url)
def XBMC_ToggleDebug(): 				xbmc.executebuiltin("XBMC.ToggleDebug()")
def XBMC_Minimize(): 						xbmc.executebuiltin("XBMC.Minimize()")
def XBMC_ActivateScreensaver(): xbmc.executebuiltin("XBMC.ActivateScreensaver()")
def XBMC_Mute(): 								xbmc.executebuiltin("XBMC.Mute()")
def RefreshList(): 							xbmc.executebuiltin("XBMC.Container.Refresh")

#############################################################################
#############################################################################
def nURL(url,method='get',form_data={},headers={},html='',proxy='',User_Agent='',cookie_file='',load_cookie=False,save_cookie=False):
	if url=='': return ''
	dhtml=''+html
	if len(User_Agent) > 0: net2.set_user_agent(User_Agent)
	else: net2.set_user_agent(ps('User-Agent'))
	if len(proxy) > 9: net2.set_proxy(proxy)
	if (len(cookie_file) > 0) and (load_cookie==True): net2.set_cookies(cookie_file)
	if   method.lower()=='get':
		try: html=net2.http_GET(url,headers=headers).content
		except: html=dhtml
	elif method.lower()=='post':
		try: html=net2.http_POST(url,form_data=form_data,headers=headers).content #,compression=False
		except: html=dhtml
	elif method.lower()=='head':
		try: html=net2.http_HEAD(url,headers=headers).content
		except: html=dhtml
	if (len(html) > 0) and (len(cookie_file) > 0) and (save_cookie==True): net2.save_cookies(cookie_file)
	return html
#############################################################################
#############################################################################
def eod(succeeded=True,updateListing=False,cacheToDisc=True,h=int(sys.argv[1])): 
	#ADDON.end_of_directory()
	xbmcplugin.endOfDirectory(h,succeeded=succeeded,updateListing=updateListing,cacheToDisc=cacheToDisc)
def messupText(t,_html=False,_ende=False,_a=False,Slashes=False,_UTF8=False):
	if (_html==True): 
		#try: 
		t=ParseDescription(HTMLParser.HTMLParser().unescape(t))
		#except: pass
	if (_ende==True): 
		try: t=t.encode('ascii', 'ignore'); t=t.decode('iso-8859-1')
		except: pass
	if (_a==True): 
		try: t=ADDON.decode(t); t=ADDON.unescape(t)
		except: pass
	if (Slashes==True): 
		try: t=t.replace( '_',' ')
		except: pass
	if (_UTF8==True): 
		try: t=t.encode('utf8', 'ignore'); t=t.decode('utf8')
		except: pass
	return t
def ParseDescription(plot): ## Cleans up the dumb number stuff thats ugly.
	#if chr(194) in plot: plot=plot.replace(chr(194),'%C2%BD')
	if ('&#' in plot) and (';' in plot):
		if ("&amp;"  in plot):  plot=plot.replace('&amp;'  ,'&')#&amp;#x27;
		if ("&ndash;" in plot): plot=plot.replace('&ndash;','-')
		if ("&#C2BD;" in plot): plot=plot.replace('&#00BD;',"%C2%BD")
		if ("&#00C2;" in plot): plot=plot.replace('&#00BD;',"")
		if ("&#00BD;" in plot): plot=plot.replace('&#00BD;',"%C2%BD")
		if ("&#8211;" in plot): plot=plot.replace("&#8211;",";") #unknown
		if ("&#8216;" in plot): plot=plot.replace("&#8216;","'")
		if ("&#8217;" in plot): plot=plot.replace("&#8217;","'")
		if ("&#8220;" in plot): plot=plot.replace('&#8220;','"')
		if ("&#8221;" in plot): plot=plot.replace('&#8221;','"')
		if ("&#215;"  in plot): plot=plot.replace('&#215;' ,'x')
		if ("&#x27;"  in plot): plot=plot.replace('&#x27;' ,"'")
		if ("&#xF4;"  in plot): plot=plot.replace('&#xF4;' ,"o")
		if ("&#xb7;"  in plot): plot=plot.replace('&#xb7;' ,"-")
		if ("&#xFB;"  in plot): plot=plot.replace('&#xFB;' ,"u")
		if ("&#xE0;"  in plot): plot=plot.replace('&#xE0;' ,"a")
		if ("&#0421;" in plot): plot=plot.replace('&#0421;',"")
		if ("&#xE9;" in plot):  plot=plot.replace('&#xE9;' ,"e")
		if ("&#xE2;" in plot):  plot=plot.replace('&#xE2;' ,"a")
		if ("&#038;" in plot):  plot=plot.replace('&#038;' ,"&")
		if ("&nbsp;" in plot):  plot=plot.replace('&nbsp;' ," ")
		if ('&#' in plot) and (';' in plot):
			try:		matches=re.compile('&#(.+?);').findall(plot)
			except:	matches=''
			if (matches is not ''):
				for match in matches:
					if (match is not '') and (match is not ' ') and ("&#"+match+";" in plot):  
						debob(['unhandled character',match]); 
						plot=plot.replace("&#"+match+";" ,""); 
		#if ("\xb7"  in plot):  plot=plot.replace('\xb7'   ,"-")
		#if ('&#' in plot) and (';' in plot): plot=unescape_(plot)
		if ("\u2019"  in plot):  plot=plot.replace('\u2019'   ,"'")
		for i in xrange(127,256):
			try: plot=plot.replace(chr(i),"")
			except: pass
		
	return plot
def unescape_(s):
	p = htmllib.HTMLParser(None)
	p.save_bgn()
	p.feed(s)
	return p.save_end()
#############################################################################
#############################################################################
def addstv(id,value=''): 
	try: ADDON.addon.setSetting(id=id,value=value) ## Save Settings
	except: pass
def addst(r,s=''): 
	try: return ADDON.get_setting(r)   ## Get Settings
	except: return s
def addpr(r,s=''): 
	try: return ADDON.queries.get(r,s) ## Get Params
	except: return s
def setView(content='none',view_mode=0,view2=0,do_sort=False,h=int(sys.argv[1])):
	try:
		if (content is not 'none') and (len(content) > 0): xbmcplugin.setContent(h,content)
		if (tfalse(getSet("auto-view"))==True):
			xbmc.executebuiltin("Container.SetViewMode(%s)"%view_mode)
		elif int(view2) > 0:
			xbmc.executebuiltin("Container.SetViewMode(%s)"%view2)
	except: pass
#############################################################################
#############################################################################
def GetPlayerCore():
	try:
		PlayerMethod=getSet("core-player")
		if   (PlayerMethod=='DVDPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_DVDPLAYER
		elif (PlayerMethod=='MPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_MPLAYER
		elif (PlayerMethod=='PAPLAYER'): PlayerMeth=xbmc.PLAYER_CORE_PAPLAYER
		else: PlayerMeth=xbmc.PLAYER_CORE_AUTO
	except: PlayerMeth=xbmc.PLAYER_CORE_AUTO
	return PlayerMeth
def PlayStreamWithResolver(url):
		play=xbmc.Player(GetPlayerCore()) ### xbmc.PLAYER_CORE_AUTO | xbmc.PLAYER_CORE_DVDPLAYER | xbmc.PLAYER_CORE_MPLAYER | xbmc.PLAYER_CORE_PAPLAYER
		import urlresolver
		url=urlresolver.HostedMediaFile(url).resolve()
		try: ADDON.resolve_url(url)
		except: pass
		try: play.play(url)
		except: pass
def PlayStream(url):
		play=xbmc.Player(GetPlayerCore()) ### xbmc.PLAYER_CORE_AUTO | xbmc.PLAYER_CORE_DVDPLAYER | xbmc.PLAYER_CORE_MPLAYER | xbmc.PLAYER_CORE_PAPLAYER
		try: ADDON.resolve_url(url)
		except: pass
		try: play.play(url)
		except: pass
def PlayURL(url):
		play=xbmc.Player(GetPlayerCore()) ### xbmc.PLAYER_CORE_AUTO | xbmc.PLAYER_CORE_DVDPLAYER | xbmc.PLAYER_CORE_MPLAYER | xbmc.PLAYER_CORE_PAPLAYER
		try: play.play(url)
		except: pass
def PlayStop():
		play=xbmc.Player(GetPlayerCore())
		try: play.stop()
		except: pass
def PlayPause():
		play=xbmc.Player(GetPlayerCore())
		try: play.pause()
		except: pass




#############################################################################
#############################################################################
def qP(u):
    try: return urllib.quote_plus(u)
    except: return u
def uqP(u):
    try: return urllib.unquote_plus(u)
    except: return u
def FixServerFile(i):
    try:
        if len(i)==0: return i
        ii=i.lower()
        for a in ['http://','https://','ftp://','rtmp://','rtmpe://','rtsp://','mms://']:
            if ii.startswith(a):
                return i
        return '/page?body=0&path='+i
    except: return i
def FixServerArt(i):
    try:
        if len(i)==0: return i
        ii=i.lower()
        for a in ['http://','https://','ftp://','rtmp://','rtmpe://','rtsp://','mms://']:
            if ii.startswith(a):
                return i
        return '/img?path='+i
    except: return i
def FixTextCodes(i):
    try:
        for a in ['[B]','[/B]','[I]','[/I]','[/COLOR]']:
            i=i.replace(a,'')
        i=i.replace('[CR]',' ')
        if '[COLOR ' in i:
            try: irR=re.compile('(\[COLOR [A-Za-z0-9]+\])').findall(i)
            except: irR=[]
            if len(irR) > 0:
              for a in irR:
                i=i.replace(a,'')
        return i
    except: return i


#############################################################################
#############################################################################




#############################################################################
#############################################################################




#############################################################################
#############################################################################




#############################################################################
#############################################################################




#############################################################################
#############################################################################
#############################################################################
#############################################################################
def zCoDeSz(x,d='',z=True):
	try:
		y= {
			'aaa':			''
			,'zzz':			''
		}[x]
		#if (len(y) > 0) and (z==True): return DecodeUrlB64(y)
		if (len(y) > 0) and (y.endswith("\n")) and (z==True): return DecodeUrlB64(y)
		return y
	except: return d


#############################################################################
#############################################################################
### Plugin Settings ###
def ps(x):
	try:
		return {
			'__authors__': '[COLOR white]The[COLOR tan]Highway[/COLOR][/COLOR]'
			,'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'
			#,'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; en-US; rv:24.0) Gecko/20100101 Firefox/24.0'
			,'User-Agent1': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
			,'User-Agent2': 'Mozilla/5.0 (Windows NT 6.2; rv:22.0) Gecko/20130405 Firefox/23.0'
			,'User-Agent2': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0'
		}[x]
	except: return ''


#############################################################################
#############################################################################


