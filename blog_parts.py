import html as _h
from blog_data import ARTICLES
L=['en','es','fr','it']
STAR='<path d="M12 2l2.9 5.1L20 4l-3.1 5.1L22 12l-5.1 2.9L20 20l-5.1-3.1L12 22l-2.9-5.1L4 20l3.1-5.1L2 12l5.1-2.9L4 4l5.1 3.1z" fill="currentColor"/>'
MON={'en':['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],'es':['ene','feb','mar','abr','may','jun','jul','ago','sep','oct','nov','dic'],
     'fr':['janv.','févr.','mars','avr.','mai','juin','juil.','août','sept.','oct.','nov.','déc.'],'it':['gen','feb','mar','apr','mag','giu','lug','ago','set','ott','nov','dic']}
UI={'en':dict(bl_tip="Good to know",bl_all="All",tg_cities="Cities",tg_culture="Culture",tg_coast="Coast",tg_family="Family",bl_e="Travel journal",bl_h="Our <em>Blog</em>",bl_p="Practical advice and stories from the road, written by our local team to help you plan your journey in Morocco.",bl_rd="Read article",bl_min="min read",bl_back="All articles",bl_more="More from the blog",
  bl_ce="Plan with us",bl_ch="Ready to turn the idea into a <em>journey</em>?",bl_cp="Send us your dates and wishes. We reply personally with a free, tailor-made itinerary.",bl_cb="Plan my trip",bl_cw="WhatsApp",bl_by="By the MoroccoRoyalTrips team",
  tg_desert="Sahara",tg_tips="Travel tips",tg_planning="Planning"),
 'es':dict(bl_tip="Bueno saber",bl_all="Todos",tg_cities="Ciudades",tg_culture="Cultura",tg_coast="Costa",tg_family="Familia",bl_e="Diario de viaje",bl_h="Nuestro <em>Blog</em>",bl_p="Consejos prácticos e historias del camino, escritos por nuestro equipo local para ayudarte a preparar tu viaje a Marruecos.",bl_rd="Leer artículo",bl_min="min de lectura",bl_back="Todos los artículos",bl_more="Más del blog",
  bl_ce="Planifica con nosotros",bl_ch="¿Listo para convertir la idea en un <em>viaje</em>?",bl_cp="Envíanos tus fechas y deseos. Te respondemos personalmente con un itinerario a medida y gratis.",bl_cb="Planificar mi viaje",bl_cw="WhatsApp",bl_by="Por el equipo de MoroccoRoyalTrips",
  tg_desert="Sáhara",tg_tips="Consejos",tg_planning="Planificación"),
 'fr':dict(bl_tip="Bon à savoir",bl_all="Tous",tg_cities="Villes",tg_culture="Culture",tg_coast="Côte",tg_family="Famille",bl_e="Carnet de voyage",bl_h="Notre <em>Blog</em>",bl_p="Conseils pratiques et récits de route, écrits par notre équipe locale pour vous aider à préparer votre voyage au Maroc.",bl_rd="Lire l’article",bl_min="min de lecture",bl_back="Tous les articles",bl_more="À lire aussi",
  bl_ce="Préparez avec nous",bl_ch="Prêt à transformer l’idée en <em>voyage</em> ?",bl_cp="Envoyez-nous vos dates et vos envies. Nous répondons personnellement avec un itinéraire sur mesure gratuit.",bl_cb="Organiser mon voyage",bl_cw="WhatsApp",bl_by="Par l’équipe MoroccoRoyalTrips",
  tg_desert="Sahara",tg_tips="Conseils",tg_planning="Préparation"),
 'it':dict(bl_tip="Da sapere",bl_all="Tutti",tg_cities="Città",tg_culture="Cultura",tg_coast="Costa",tg_family="Famiglia",bl_e="Diario di viaggio",bl_h="Il nostro <em>Blog</em>",bl_p="Consigli pratici e storie dalla strada, scritti dal nostro team locale per aiutarti a organizzare il tuo viaggio in Marocco.",bl_rd="Leggi l’articolo",bl_min="min di lettura",bl_back="Tutti gli articoli",bl_more="Altro dal blog",
  bl_ce="Organizza con noi",bl_ch="Pronto a trasformare l’idea in un <em>viaggio</em>?",bl_cp="Inviaci date e desideri. Ti rispondiamo di persona con un itinerario su misura gratuito.",bl_cb="Organizza il mio viaggio",bl_cw="WhatsApp",bl_by="Dal team di MoroccoRoyalTrips",
  tg_desert="Sahara",tg_tips="Consigli",tg_planning="Organizzazione")}

def key(a): return a['id'].replace('blog-','').replace('-','_')
def date(a,l):
    y,m,d=a['date'].split('-'); m=int(m)
    return f"{int(d)} {MON[l][m-1]} {y}" if l!='en' else f"{MON[l][m-1]} {int(d)}, {y}"

def tdict(l):
    d=dict(UI[l])
    for a in ARTICLES:
        k=key(a); d['bt_'+k]=a['t'][l]; d['bx_'+k]=a['x'][l]; d['bd_'+k]=date(a,l)
        for si,(hd,ps) in enumerate(a['b'][l]):
            if hd: d[f'bh_{k}_{si}']=hd
            html=''; lst=[]
            for p in ps:
                if p.startswith('- '): lst.append(p[2:]); continue
                if lst: html+='<ul>'+''.join(f'<li>{x}</li>' for x in lst)+'</ul>'; lst=[]
                if p.startswith('> '): html+=f'<blockquote class="bl-tip"><b>{UI[l]["bl_tip"]}</b>{p[2:]}</blockquote>'; continue
                html+=f'<p>{p}</p>'
            if lst: html+='<ul>'+''.join(f'<li>{x}</li>' for x in lst)+'</ul>'
            d[f'bp_{k}_{si}']=html
    return d

def card(a,big=False):
    k=key(a)
    return (f'<a class="bl-c{" big" if big else ""} reveal" data-tag="{a["tag"]}" href="{a["id"]}.html"><span class="bl-i"><img src="{{{{IMG_{a["img"]}}}}}" alt="" loading="lazy"><span class="bl-tag" data-i="tg_{a["tag"]}">x</span></span>'
            f'<span class="bl-b"><small><span data-i="bd_{k}">x</span> · {a["mins"]} <span data-i="bl_min">min read</span></small><b data-i="bt_{k}">x</b><span class="bl-x" data-i="bx_{k}">x</span>'
            f'<span class="bl-l"><span data-i="bl_rd">Read article</span><svg><use href="#i-arrow"/></svg></span></span></a>')

def hero(img,title_key,crumb,sub=''):
    return f'''<section class="hero hero-sm" id="hero">
  <div class="hero-media" id="heroMedia"><img class="hero-bg" src="{{{{IMG_{img}}}}}" alt=""></div>
  <div class="hero-shade" aria-hidden="true"></div>
  <div class="in hero-in"><div class="hero-copy">
    <nav class="crumbs rise" aria-label="Breadcrumb"><a href="index.html" data-i="m0">Home</a><svg><use href="#i-chev"/></svg>{crumb}</nav>
    <h1 id="heroTitle" class="bl-h1" data-i="{title_key}">x</h1>
    <div class="khatam" aria-hidden="true"><span></span><svg viewBox="0 0 24 24">{STAR}</svg><span></span></div>
    {sub}
  </div></div>
</section>'''

CTA='''<section class="bl-cta"><div class="in"><div class="bl-cta-in reveal"><span class="eyebrow" data-i="bl_ce">x</span><h2 data-i="bl_ch">x</h2><p data-i="bl_cp">x</p>
 <div class="row"><a class="btn gold" href="contact.html"><span data-i="bl_cb">x</span><svg><use href="#i-arrow"/></svg></a><a class="btn bl-wa" href="https://wa.me/212659288638" target="_blank" rel="noopener"><svg><use href="#i-wa"/></svg><span data-i="bl_cw">WhatsApp</span></a></div></div></div></section>'''
FOOT='<footer class="foot"></footer>'

def FLT():
    tags=[]
    for a in ARTICLES:
        if a['tag'] not in tags: tags.append(a['tag'])
    return '<button class="on" data-f="*" data-i="bl_all">All</button>'+''.join(f'<button data-f="{t}" data-i="tg_{t}">x</button>' for t in tags)
def list_main():
    first,rest=ARTICLES[0],ARTICLES[1:]
    return f'''<main id="top">
{hero('caravan-dusk','bl_h','<span data-i="m5">Blog</span>','<p class="lead rise d3" data-i="bl_p">x</p>')}
<section class="bl-list"><div class="in">
  <div class="bl-flt" role="tablist">{FLT()}</div>
  <div class="bl-feat">{card(first,True)}</div>
  <div class="bl-grid">{''.join(card(a) for a in rest)}</div>
</div></section>
{CTA}
{FOOT}
</main>'''

def article_main(a):
    k=key(a)
    secs=''
    for si,(hd,ps) in enumerate(a['b']['en']):
        secs+=(f'<h2 data-i="bh_{k}_{si}">x</h2>' if hd else '')+f'<div class="{"bl-lead" if si==0 and not hd else "bl-sec"}" data-i="bp_{k}_{si}">x</div>'
    _o=[x for x in ARTICLES if x['id']!=a['id']]
    others=([x for x in _o if x['tag']==a['tag']]+[x for x in _o if x['tag']!=a['tag']])[:3]
    meta=f'<p class="bl-meta rise d3"><span data-i="tg_{a["tag"]}">x</span><i></i><span data-i="bd_{k}">x</span><i></i>{a["mins"]} <span data-i="bl_min">min read</span></p>'
    return f'''<main id="top">
{hero(a['img'],'bt_'+k,'<a href="blog.html" data-i="m5">Blog</a>',meta)}
<section class="bl-art"><div class="in bl-wrap">
  <article class="bl-body reveal">{secs}
    <p class="bl-by"><img src="{{{{EMBLEM}}}}" alt=""><span data-i="bl_by">x</span></p>
  </article>
  <aside class="bl-side"><div class="bl-box"><span class="eyebrow" data-i="bl_ce">x</span><b data-i="bl_ch">x</b><p data-i="bl_cp">x</p><a class="btn gold" href="contact.html"><span data-i="bl_cb">x</span><svg><use href="#i-arrow"/></svg></a><a class="bl-back" href="blog.html"><svg><use href="#i-arrow"/></svg><span data-i="bl_back">x</span></a></div></aside>
</div></section>
<section class="bl-list bl-rel"><div class="in"><h2 class="bl-relh" data-i="bl_more">x</h2><div class="bl-grid">{''.join(card(x) for x in others)}</div></div></section>
{FOOT}
</main>'''

CSS='''
/* ===== BLOG ===== */
.bl-h1{font-size:clamp(38px,5.2vw,76px)!important;max-width:20ch}
.bl-meta{display:flex;align-items:center;gap:12px;flex-wrap:wrap;font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:rgba(255,255,255,.85);margin:6px 0 0}
.bl-meta i{width:4px;height:4px;border-radius:50%;background:var(--gold-hi)}
.bl-list{background:#f5efe4;padding-block:90px 100px}
.bl-feat{margin-bottom:28px}
.bl-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.bl-c{display:flex;flex-direction:column;background:#fffaf1;border-radius:22px;overflow:hidden;color:#16213d;box-shadow:0 18px 40px rgba(22,33,61,.08);transition:transform .5s var(--ease),box-shadow .5s}
.bl-c:hover{transform:translateY(-5px);box-shadow:0 26px 54px rgba(22,33,61,.14)}
.bl-i{position:relative;aspect-ratio:16/10;overflow:hidden;background:#e8dcc5}
.bl-i img{width:100%;height:100%;object-fit:cover;max-width:none;transition:transform 1.2s var(--ease)}
.bl-c:hover .bl-i img{transform:scale(1.06)}
.bl-tag{position:absolute;left:16px;top:16px;background:rgba(14,14,14,.78);color:var(--gold-hi);border-radius:999px;padding:7px 14px;font-size:11px;letter-spacing:.2em;text-transform:uppercase}
.bl-b{display:grid;gap:10px;padding:24px 26px 26px;align-content:start;flex:1}
.bl-b small{font-size:11.5px;letter-spacing:.18em;text-transform:uppercase;color:#9a7433}
.bl-b b{font-family:var(--display);font-weight:400;font-size:22px;line-height:1.15;text-transform:uppercase}
.bl-x{font-size:15px;line-height:1.65;color:#4a536d}
.bl-l{display:inline-flex;align-items:center;gap:10px;margin-top:6px;font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:#9a7433}
.bl-l svg{width:15px;height:15px;transition:transform .4s}.bl-c:hover .bl-l svg{transform:translateX(5px)}
.bl-c.big{display:grid;grid-template-columns:1.25fr 1fr}
.bl-c.big .bl-i{aspect-ratio:auto;min-height:420px}
.bl-c.big .bl-b{padding:48px 46px;align-content:center;gap:16px}
.bl-c.big b{font-size:clamp(28px,3vw,42px)}
.bl-c.big .bl-x{font-size:16.5px}
.bl-art{background:#fffaf1;color:#16213d;padding-block:80px 90px}
.bl-wrap{display:grid;grid-template-columns:minmax(0,1fr) 320px;gap:64px;align-items:start}
.bl-body{max-width:720px}
.bl-body h2{font-size:clamp(26px,2.6vw,36px);line-height:1.1;margin:46px 0 16px;color:#16213d}
.bl-body p{font-size:17.5px;line-height:1.85;color:#3c4560;margin:0 0 18px}
.bl-lead p{font-size:20px;line-height:1.75;color:#16213d}
.bl-lead p::first-letter{float:left;font-family:var(--display);font-size:68px;line-height:.9;padding:6px 12px 0 0;color:#b0843f}
.bl-body ul{list-style:none;margin:6px 0 22px;padding:0;display:grid;gap:12px}
.bl-body li{position:relative;padding-left:28px;font-size:17px;line-height:1.7;color:#3c4560}
.bl-body li::before{content:"";position:absolute;left:4px;top:11px;width:9px;height:9px;border-radius:50%;background:#c9a05a;box-shadow:0 0 0 4px rgba(201,160,90,.18)}
.bl-by{display:flex;align-items:center;gap:12px;margin-top:40px!important;padding-top:24px;border-top:1px solid rgba(22,33,61,.12);font-size:14px!important;letter-spacing:.06em;color:#6a7187!important}
.bl-by img{width:46px;height:46px;object-fit:contain}
.bl-side{position:sticky;top:110px}
.bl-box{background:#16213d;color:#fff;border-radius:24px;padding:30px 28px;display:grid;gap:14px}
.bl-box .eyebrow{color:var(--gold-hi);text-shadow:none}.bl-box .eyebrow::before{animation:none}
.bl-box b{font-family:var(--display);font-weight:400;font-size:26px;line-height:1.1;text-transform:uppercase}.bl-box b em{color:var(--gold-hi);font-style:normal}
.bl-box p{margin:0;font-size:14.5px;line-height:1.7;color:rgba(255,255,255,.75)}
.bl-box .btn{justify-content:center;margin-top:6px}
.bl-back{display:inline-flex;align-items:center;justify-content:center;gap:10px;font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:rgba(255,255,255,.75)}
.bl-back svg{width:14px;height:14px;transform:rotate(180deg)}.bl-back:hover{color:var(--gold-hi)}
.bl-rel{padding-block:80px 90px}
.bl-relh{text-align:center;font-size:clamp(30px,3.6vw,48px);margin:0 0 40px;color:#16213d}
.bl-cta{background:#16213d;padding-block:90px}
.bl-cta-in{display:grid;justify-items:center;text-align:center;gap:16px;max-width:760px;margin:0 auto}
.bl-cta .eyebrow{color:var(--gold-hi)}
.bl-cta h2{font-size:clamp(32px,4.4vw,58px);line-height:1;margin:0;color:#fff}.bl-cta h2 em{color:var(--gold-hi)}
.bl-cta p{margin:0;color:rgba(255,255,255,.78);font-size:17px;line-height:1.7}
.bl-cta .row{display:flex;gap:14px;flex-wrap:wrap;justify-content:center;margin-top:8px}
.btn.bl-wa{background:#25d366;color:#fff}.btn.bl-wa svg{width:18px;height:18px}
@media(max-width:1000px){.bl-grid{grid-template-columns:repeat(2,1fr)}.bl-c.big{grid-template-columns:1fr}.bl-c.big .bl-i{min-height:0;aspect-ratio:16/10}.bl-c.big .bl-b{padding:30px 28px}
 .bl-wrap{grid-template-columns:1fr;gap:40px}.bl-side{position:static}}
@media(max-width:640px){.bl-grid{grid-template-columns:1fr}.bl-list{padding-block:64px 70px}.bl-art{padding-block:56px 60px}.bl-body p{font-size:16.5px}.bl-lead p{font-size:18px}.bl-lead p::first-letter{font-size:56px}}
'''
CSS+='''
.bl-tip{margin:8px 0 26px;padding:20px 24px 20px 26px;background:#f5efe4;border-left:3px solid #c9a05a;border-radius:0 16px 16px 0;font-size:16.5px;line-height:1.75;color:#3c4560}
.bl-tip b{display:block;font-family:var(--display);font-weight:400;font-size:13px;letter-spacing:.22em;text-transform:uppercase;color:#9a7433;margin-bottom:6px}
.bl-body a{color:#9a7433;text-decoration:underline;text-underline-offset:3px;text-decoration-color:rgba(154,116,51,.4)}.bl-body a:hover{color:#16213d}
.bl-flt{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin:0 0 38px}
.bl-flt button{font:inherit;cursor:pointer;border:1px solid rgba(22,33,61,.18);background:transparent;color:#16213d;border-radius:999px;padding:10px 20px;font-size:12px;letter-spacing:.2em;text-transform:uppercase;transition:background .3s,color .3s,border-color .3s}
.bl-flt button:hover{border-color:#c9a05a}.bl-flt button.on{background:#16213d;border-color:#16213d;color:var(--gold-hi)}
.bl-list .bl-c.hid{display:none}
@media(max-width:640px){.bl-flt{flex-wrap:nowrap;overflow-x:auto;justify-content:flex-start;margin-inline:-16px;padding:0 16px 6px;scrollbar-width:none}.bl-flt button{flex:none}.bl-tip{padding:16px 18px}}
'''
JS='''
(function(){var f=document.querySelector('.bl-flt');if(!f)return;var feat=document.querySelector('.bl-feat');
f.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;
f.querySelectorAll('button').forEach(function(x){x.classList.toggle('on',x===b)});var t=b.getAttribute('data-f');
document.querySelectorAll('.bl-list .bl-c').forEach(function(c){var ok=t==='*'||c.getAttribute('data-tag')===t;c.classList.toggle('hid',!ok);if(ok)c.classList.add('seen')});
if(feat)feat.style.display=(t==='*'||feat.querySelector('[data-tag="'+t+'"]'))?'':'none';});})();
'''
