import sys
import urllib
import urllib2
import requests
import zlib
import json

url = 'https://prd-wlssb.temple.edu/prod8/bwckschd.p_get_crse_unsec'

class ClassForm:

  def __init__(self, term_in, subject):
    self.params = {
      'term_in' : '',
      'sel_subj' : ['dummy'],
      'sel_day' : 'dummy',
      'sel_schd' : 'dummy',
      'sel_insm' : 'dummy',
      'sel_camp' : ['dummy','%'],
      'sel_levl' : 'dummy',
      'sel_sess' : ['dummy', '%'],
      'sel_instr' : ['dummy','%'],
      'sel_ptrm' : ['dummy','%'],
      'sel_attr' : ['dummy','%'],
      'sel_divs' : ['dummy','%'],
      'sel_crse' : '',
      'sel_title' : '',
      'sel_from_cred' : '',
      'sel_to_cred' : '',
      'begin_hh' : '0',
      'begin_mi' : '0',
      'begin_ap' : 'a',
      'end_hh' : '0',
      'end_mi' : '0',
      'end_ap' : 'a'
    }

    self.params['term_in'] = term_in
    self.params['sel_subj'].append(subject)

  def submit(self):
    data = urllib.urlencode(self.params, True)
    req = urllib2.Request(url, data)
    req.add_header('Referer', 'https://prd-wlssb.temple.edu/prod8/bwckgens.p_proc_term_date')
    req.add_header('Connection', 'keep-alive')
    req.add_header('Host', "prd-wlssb.temple.edu")
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0')
    req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
    req.add_header('Accept-Language', 'en-US,en;q=0.5'),
    req.add_header('Accept-Encoding', 'gzip, deflate'),
    req.add_header('Cookie', '__utma=168561188.1286512682.1441240750.1442888175.1442890162.15; __utmz=168561188.1441240750.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=5159026.1758930790.1441240783.1442888056.1442889627.12; __utmz=5159026.1442889627.12.9.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmb=5159026.8.10.1442889627; __utmt=1; _ga=GA1.2.1286512682.1441240750; _gat=1; __utmb=168561188.3.9.1442890192564; __utmc=168561188; __utmt=1; Big_IP_prdwlssb=765786011.13091.0000; __utmc=5159026')
    response = urllib2.urlopen(req)
    html = zlib.decompress(response.read(), 16+zlib.MAX_WBITS)
    return html

test = ClassForm('201403', 'CIS')
html = test.submit()
html_file = open("Output.html", "w")
html_file.write(html)
html_file.close()

