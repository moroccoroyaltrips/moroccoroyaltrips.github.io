# SEO: meta description, canonical, Open Graph / Twitter tags, JSON-LD, sitemap.xml, robots.txt
import re, html, json, datetime
DOMAIN='https://www.moroccoroyaltrips.com'   # <-- change to the real domain when known
SITE='Morocco Royal Trips'
DEF="Private tours in Morocco with a local team: Sahara desert camps in Merzouga and Erg Chigaga, imperial cities, Atlas mountains and day trips from Marrakech and Fes."
FIX={'index.html':DEF,
 'about.html':"Meet MoroccoRoyalTrips, a local Moroccan tour operator with 8 years of experience creating private, tailor-made journeys across Morocco.",
 'contact.html':"Plan your private tour in Morocco. Send us your dates and wishes and we reply personally with a free, tailor-made itinerary and quote.",
 'blog.html':"Travel guides for Morocco written by our local team: the Sahara, Marrakech, Fes, Chefchaouen, food, customs, family travel and practical tips.",
 'faq.html':"Answers to the most common questions about booking a private tour in Morocco: deposit, payment, what is included, desert camps, visas and more.",
 'privacy.html':"How MoroccoRoyalTrips collects, uses and protects your personal information when you contact us or book a private tour in Morocco.",
 'terms.html':"Booking terms for MoroccoRoyalTrips private tours in Morocco: quotes, deposit, payment on arrival, what the price includes and changes.",
 'merzouga.html':"Desert activities in Merzouga: camel rides, quad and buggy tours, 4x4 excursions, sandboarding and stargazing in the dunes of Erg Chebbi.",
 'agafay.html':"Activities in the Agafay desert near Marrakech: camel rides, quad and buggy tours and sunset dinners in a desert camp."}
def _clean(t):
    t=re.sub(r'<[^>]+>','',t); t=html.unescape(t).strip(); t=re.sub(r'\s+',' ',t)
    return t if len(t)<=160 else t[:157].rsplit(' ',1)[0]+'…'
def run(files,tours,acts,arts):
    desc=dict(FIX)
    for t in tours: desc[t['id']+'.html']=t['s']['en'] if isinstance(t.get('s'),dict) else DEF
    for a in acts: desc[a['id']+'.html']=a['s']['en'] if isinstance(a.get('s'),dict) else DEF
    for a in arts: desc[a['id']+'.html']=a['x']['en']
    urls=[]
    for f in files:
        s=open(f).read()
        s=re.sub(r'\n?<!--seo-->.*?<!--/seo-->','',s,flags=re.S)
        s=s.replace(' · MoroccoRoyalTrips</title>',' · Morocco Royal Trips</title>')
        if f=='index.html': s=re.sub(r'<title>.*?</title>','<title>Morocco Royal Trips | Private Tours &amp; Sahara Desert Trips in Morocco</title>',s,count=1,flags=re.S)
        s=s.replace('<link rel="icon" href="images/fav.png">','<link rel="icon" href="/favicon.ico" sizes="48x48"><link rel="icon" type="image/png" sizes="192x192" href="/images/icon-192.png"><link rel="apple-touch-icon" href="/images/apple-touch-icon.png">')
        title=html.unescape(re.search(r'<title>(.*?)</title>',s,re.S).group(1))
        d=_clean(desc.get(f,DEF))
        m=re.search(r'class="hero-bg[^"]*"[^>]*>\s*<img src="(images/[^"]+)"',s) or re.search(r'<img class="hero-bg" src="(images/[^"]+)"',s) or re.search(r'src="(images/[^"]+\.webp)"',s)
        img=DOMAIN+'/'+(m.group(1) if m else 'images/hero-riad.webp')
        url=DOMAIN+'/'+('' if f=='index.html' else f)
        e=lambda x: html.escape(x,quote=True)
        tags=[f'<meta name="description" content="{e(d)}">',f'<link rel="canonical" href="{url}">',
              '<meta property="og:type" content="'+('article' if f.startswith('blog-') else 'website')+'">',f'<meta property="og:site_name" content="{SITE}">',
              f'<meta property="og:title" content="{e(title)}">',f'<meta property="og:description" content="{e(d)}">',f'<meta property="og:url" content="{url}">',
              f'<meta property="og:image" content="{img}">','<meta name="twitter:card" content="summary_large_image">','<meta name="theme-color" content="#16213d">']
        for l,c in (('en','en'),('es','es'),('fr','fr'),('it','it')): pass
        if f=='index.html':
            ld={"@context":"https://schema.org","@type":"TravelAgency","name":SITE,"url":DOMAIN+'/',"logo":DOMAIN+'/images/logo-full.webp',"image":img,
                "description":DEF,"telephone":"+212659288638","email":"moroccoroyaltrips0@gmail.com","address":{"@type":"PostalAddress","addressCountry":"MA"},
                "areaServed":"Morocco","sameAs":["https://www.instagram.com/morocco_royal_trips/","https://www.facebook.com/share/1KHcsaf3p6/"],"knowsLanguage":["en","es","fr"]}
            tags.append('<script type="application/ld+json">'+json.dumps(ld,ensure_ascii=False)+'</script>')
            tags.append('<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"WebSite","name":"Morocco Royal Trips","alternateName":["MoroccoRoyalTrips","Morocco Royal Trips - Private Tours"],"url":DOMAIN+'/'},ensure_ascii=False)+'</script>')
        if f.startswith('blog-'):
            a=next((x for x in arts if x['id']+'.html'==f),None)
            if a: tags.append('<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"Article","headline":a['t']['en'],"description":a['x']['en'],"image":img,"datePublished":a['date'],"author":{"@type":"Organization","name":SITE},"publisher":{"@type":"Organization","name":SITE}},ensure_ascii=False)+'</script>')
        if f=='faq.html':
            import legal_parts as LG
            tags.append('<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":_clean(a) if len(_clean(a))<160 else re.sub(r'<[^>]+>','',a)}} for q,a in LG.FQ['en']]},ensure_ascii=False)+'</script>')
        blk='\n<!--seo-->'+'\n'.join(tags)+'<!--/seo-->'
        i=s.index('</title>')+len('</title>'); s=s[:i]+blk+s[i:]
        open(f,'w').write(s)
        pr='1.0' if f=='index.html' else '0.8' if f.startswith(('tour-','daytrip-')) else '0.6'
        urls.append((url,pr))
    today=datetime.date.today().isoformat()
    sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>{u}</loc><lastmod>{today}</lastmod><priority>{p}</priority></url>\n' for u,p in sorted(urls,key=lambda x:(-float(x[1]),x[0])))+'</urlset>\n'
    open('sitemap.xml','w').write(sm)
    open('robots.txt','w').write(f'User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n')
    print('seo:',len(urls),'pages, sitemap written')
