import base64, json, os, sys, importlib
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,'.')
import contact_parts as C, act_data, act_pages as A, tours as TR, about_parts as AB, blog_data, blog_parts as BL
for m in (C, act_data, A, TR, AB, blog_data, BL): importlib.reload(m)
import cms_content as CMS; importlib.reload(CMS)
CMS.load_tours(TR,A); CMS.load_blog(blog_data,A)

def uri(p,t): return p  # images served as separate files (was inline base64)
EMB=uri('images/emblem.webp','webp'); FAV=uri('images/fav.png','png'); HERO=uri('images/hero-riad.webp','webp'); CHERO=uri('images/contact-hero.webp','webp')
src=open('src.html').read().replace('<link rel="icon" href="{{EMBLEM}}">','<link rel="icon" href="{{FAV}}">')
import re as _re
def dedup(s):
    s=s.replace('{{FAV}}',FAV)
    uris=_re.findall(r'src="(data:image/[a-z]+;base64,[A-Za-z0-9+/=]+)"',s)
    seen={};n=0
    for u in uris:
        if uris.count(u)<2 or u in seen: continue
        n+=1; seen[u]=f'd{n}'
        first=s.index(f'src="{u}"')
        rest=s[first+5+len(u)+1:].replace(f'src="{u}"',f'src="data:image/gif;base64,R0lGODlhAQABAAAAACw=" data-dup="d{n}"')
        s=s[:first]+f'src="{u}" data-dupsrc="d{n}"'+rest
    if seen:
        js='<script>document.querySelectorAll("[data-dup]").forEach(function(i){var o=document.querySelector(\'[data-dupsrc="\'+i.dataset.dup+\'"]\');if(o)i.src=o.src})</script>'
        i=s.rindex('</body>') if '</body>' in s else len(s)
        s=s[:i]+js+s[i:]
    return s
KEYS={'en':' en:{lph:"Language",','es':' es:{lph:"Idioma",','fr':' fr:{lph:"Langue",','it':' it:{lph:"Lingua",'}
HEAD='''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}</style>
<script>try{history.scrollRestoration='manual'}catch(e){}if(!location.hash){var _t=function(){window.scrollTo(0,0)};_t();addEventListener('DOMContentLoaded',_t);addEventListener('load',function(){_t();setTimeout(_t,60)});addEventListener('pageshow',_t)}</script>
'''

# ---------- index.html (home) ----------
import home_parts as HP; importlib.reload(HP)
_hh,_ht=HP.build(TR.TOURS,TR.EXTRA_T,act_data.ACTS)
_ix=src.replace('<!--HOME_SECTIONS-->',_hh).replace('</style>',HP.CSS+'</style>',1).rstrip()+'\n'+HP.JS+'\n'
for _c,_k in KEYS.items():
    _ix=_ix.replace(_k,_k+','.join(f'{x}:{json.dumps(y,ensure_ascii=False)}' for x,y in _ht[_c].items())+',',1)
_ix=_ix.replace('{{EMBLEM}}',EMB).replace('{{HERO}}',HERO).replace('{{CHERO}}',CHERO)
for _pid in A.PHOTOS:
    _t='{{IMG_'+_pid+'}}'
    if _t in _ix: _ix=_ix.replace(_t,uri(f'images/{_pid}.webp','webp'))
open('index.html','w').write(dedup(_ix))

def make_page(fname,title,main,css,tfn,js):
    s=src.replace('<title>MoroccoRoyalTrips</title>',f'<title>{title}</title>',1)
    a=s.index('<main id="top">'); b=s.index('</main>')+len('</main>')
    s=s[:a]+main+s[b:]
    s=s.replace('</style>',css+'</style>',1)
    acts=set(_re.findall(r'data-act="([^"]+)"',s))
    def _used(x):
        return (f'data-i="{x}"' in s) or (f'.{x}' in js) or (f"'{x}'" in js) or (f'"{x}"' in js) or (x[:-2] in acts and x.endswith('_t'))
    for c,k in KEYS.items():
        assert s.count(k)==1,k
        s=s.replace(k,k+','.join(f'{x}:{json.dumps(y,ensure_ascii=False)}' for x,y in tfn(c).items() if _used(x))+',')
    i=s.index('let saved="en"; try{'); s=s[:i]+js+s[i:]
    s=s.replace('href="#tours-','href="index.html#tours-')
    for h in ['#top','#tours','#day-trips','#about','#blog']:
        s=s.replace(f'href="{h}"',f'href="{"index.html" if h=="#top" else "index.html"+h}"')
    s=s.replace('{{EMBLEM}}',EMB).replace('{{CHERO}}',CHERO).replace('{{HERO}}',HERO)
    for pid in A.PHOTOS:
        tok='{{IMG_'+pid+'}}'
        if tok in s: s=s.replace(tok,uri(f'images/{pid}.webp','webp'))
    cut=s.index('</style>')+len('</style>')
    open(fname,'w').write(dedup(HEAD+s[:cut]+'\n</head>\n<body>\n'+s[cut:]+'\n</body>\n</html>\n'))

make_page('blog.html','Blog · MoroccoRoyalTrips',BL.list_main(),C.CSS+BL.CSS,BL.tdict,BL.JS)
for _a in blog_data.ARTICLES:
    make_page(_a['id']+'.html',_a['t']['en']+' · MoroccoRoyalTrips',BL.article_main(_a),C.CSS+BL.CSS,BL.tdict,BL.JS)
make_page('about.html','About Us · MoroccoRoyalTrips',AB.MAIN,C.CSS+AB.CSS,lambda c:AB.T[c],AB.JS)
make_page('contact.html','Contact · MoroccoRoyalTrips',C.MAIN,C.CSS,lambda c:C.T[c],C.JS)
make_page('merzouga.html','Merzouga Activities · MoroccoRoyalTrips',A.list_main('m'),A.CSS,A.tdict,A.JS)
make_page('agafay.html','Agafay Activities · MoroccoRoyalTrips',A.list_main('a'),A.CSS,A.tdict,A.JS)
for act in act_data.ACTS:
    make_page(act['id']+'.html',act['t']['en']+' · MoroccoRoyalTrips',A.detail_main(act),A.CSS,A.tdict,A.JS)

import legal_parts as LG; importlib.reload(LG)
make_page('privacy.html','Privacy Policy · MoroccoRoyalTrips',LG.legal_main('pr','mk-koutoubia'),C.CSS+BL.CSS+LG.CSS,LG.tdict,'')
make_page('terms.html','Terms & Conditions · MoroccoRoyalTrips',LG.legal_main('tm','caravan-dusk'),C.CSS+BL.CSS+LG.CSS,LG.tdict,'')
make_page('faq.html','FAQ · Private Tours in Morocco · MoroccoRoyalTrips',LG.faq_main(),C.CSS+BL.CSS+LG.CSS,LG.tdict,'')
PAGES=['contact.html','merzouga.html','agafay.html']+[a['id']+'.html' for a in act_data.ACTS]
print('built index +',len(PAGES),'pages:',', '.join(f'{p} {os.path.getsize(p)//1024}KB' for p in PAGES))

for t in TR.TOURS:
    make_page(t['id']+'.html',t['t']['en']+' · MoroccoRoyalTrips',TR.main2(t) if t['id'] in TR.EXTRA_T else TR.main(t),A.CSS+TR.CSS+TR.CSS2,lambda c:{**A.tdict(c),**TR.tdict2(c)},A.JS+TR.JS2)
print('tours:',', '.join(t['id'] for t in TR.TOURS))

# ---- shared professional footer on every page ----
import footer_parts as FT; importlib.reload(FT)
for _f in [f for f in _g.glob('*.html') if not f.startswith('backup') and f not in('src.html','logo.html','404.html')] if False else []: pass
import glob as _g
for _f in [f for f in _g.glob('*.html') if not f.startswith('backup') and f not in('src.html','logo.html','404.html')]:
    _s=open(_f).read(); _n=FT.apply(_s,KEYS).replace('{{EMBLEM}}',EMB)
    if _n!=_s: open(_f,'w').write(_n)
# ---- pre-render English text so pages show content immediately ----
import glob as _g, subprocess as _sp
_files=[f for f in _g.glob('*.html') if not f.startswith('backup') and f not in('src.html','logo.html','404.html')]
print(_sp.run(['node','prefill.js']+_files,capture_output=True,text=True).stdout.strip())

# ---- SEO: meta description, Open Graph, JSON-LD, sitemap ----
import seo_parts as SEO; importlib.reload(SEO)
SEO.run(_files,TR.TOURS,act_data.ACTS,blog_data.ARTICLES)

# ---- search index ----
import json as _js
_feat=set(HP.FEATURED) if hasattr(HP,'FEATURED') else set()
_idx=[]
def _img(ex,dflt):
    h=ex.get('hero_src',(None,))[0] if ex else None
    if h and h.startswith('{{IMG_'): return 'images/'+h[6:-2]+'.webp'
    if ex and ex.get('hero'): return 'images/'+ex['hero'][0]+'.webp'
    return dflt
for _t in TR.TOURS:
    _ex=TR.EXTRA_T.get(_t['id'],{})
    _idx.append(dict(u=_t['id']+'.html',k='d' if _t['city']=='daytrip' else 't',t=_t['t'],r=_t['route'],n=_t['days'],i=_img(_ex,'images/hero-riad.webp'),w=_t['city'],f=1 if (_t['id'] in _feat or _t['city']=='daytrip') else 0))
for _a in act_data.ACTS:
    _idx.append(dict(u=_a['id']+'.html',k='a',t=_a['t'],r={'en':'Merzouga' if _a['dest']=='m' else 'Agafay'},i='images/'+_a['id']+'.webp',w='activity desert',f=0))
for _a in blog_data.ARTICLES:
    _idx.append(dict(u=_a['id']+'.html',k='g',t=_a['t'],r=_a['x'],i='images/'+_a['img']+'.webp',w=_a['tag'],f=0))
open('search-index.js','w').write('window.SRCH_IDX='+_js.dumps(_idx,ensure_ascii=False,separators=(',',':'))+';')
print('search index',len(_idx),os.path.getsize('search-index.js')//1024,'KB')

# ---- Chinese (zh): inject translations from zh_tm/ ----
print('cms zh strings:',CMS.zh_memory(TR,BL,blog_data))
_files=[f for f in _g.glob('*.html') if not f.startswith('backup') and f not in('src.html','logo.html','404.html')]
print(_sp.run(['node','zh_inject.js']+_files,capture_output=True,text=True).stdout.strip())
