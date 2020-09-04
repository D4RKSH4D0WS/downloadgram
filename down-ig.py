#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# Author D4RK5H4D0W5
G0 = '\033[0;32m'
C0 = '\033[0;36m'
W0 = '\033[0;37m'
R0 = '\033[0;31m'
import subprocess as sp,requests,os,sys
from bs4 import BeautifulSoup as bs
try:
	os.system('clear')
	r=requests.Session()
	print '''%s
╔╦╗╔═╗╦ ╦╔╗╔╦  ╔═╗╔═╗╔╦╗╔═╗╦═╗╔═╗╔╦╗  %sCoded by D4RKSH4D0WS%s
 ║║║ ║║║║║║║║  ║ ║╠═╣ ║║║ ╦╠╦╝╠═╣║║║  %sFb mimam.syafii.90%s
═╩╝╚═╝╚╩╝╝╚╝╩═╝╚═╝╩ ╩═╩╝╚═╝╩╚═╩ ╩╩ ╩  %sWa.me/628996604524%s
	'''%(C0,W0,C0,W0,C0,W0,C0)
	print '%s[%s*%s] Waiting ...'%(W0,G0,W0)
	sys.argv[1]
	web=r.get('https://downloadgram.com/').text
	proces=r.post('https://downloadgram.com/process.php',data={'url':sys.argv[1],'build_id':bs(web,'html.parser').find('input',attrs={'name':'build_id'})['value'],'build_key':bs(web,'html.parser').find('input',attrs={'name':'build_key'})['value']}).text
	if 'success' in proces:print '%s[%s✓%s] Success ...'%(W0,G0,W0);sp.check_output(['am', 'start', bs(proces,'html.parser').find('a')['href']])
	else:exit('%s[%sx%s] Failed, Enter the url correctly'%(W0,R0,W0))
except requests.exceptions.ConnectionError:exit('%s[%s!%s] Check internet'%(W0,R0,W0))
except IndexError:exit('%s[%s!%s] Use : python2 %s url-ig'%(W0,R0,W0,sys.argv[0]))
except KeyboardInterrupt:exit('\n%s[%s!%s] Exit'%(W0,R0,W0))
