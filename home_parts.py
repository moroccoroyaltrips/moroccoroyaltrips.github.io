import json, html as _h
LANGS=['en','es','fr','it']
STAR='<path d="M12 2l2.9 5.1L20 4l-3.1 5.1L22 12l-5.1 2.9L20 20l-5.1-3.1L12 22l-2.9-5.1L4 20l3.1-5.1L2 12l5.1-2.9L4 4l5.1 3.1z" fill="currentColor"/>'
CITIES=[('marrakech','c_mar','mk-jemaa2'),('fes','c_fes','fes-tannery-hero'),('tangier','c_tan','tangier-bay'),('casablanca','c_cas','casa-mosque-hero'),
        ('errachidia','c_err','erg-palm'),('ouarzazate','c_oua','abh-reflect'),('agadir','c_aga','agadir-marina')]
CNAME={'marrakech':'Marrakech','fes':{'en':'Fes','es':'Fez','fr':'Fès','it':'Fes'},'tangier':{'en':'Tangier','es':'Tánger','fr':'Tanger','it':'Tangeri'},'casablanca':'Casablanca','errachidia':'Errachidia','ouarzazate':'Ouarzazate','agadir':'Agadir'}
FEATURED=['tour-3day-fes-marrakech-merzouga','tour-12day-grand-tour-marrakech','tour-5day-honeymoon-marrakech','tour-4day-casablanca-marrakech-sahara','tour-7day-tangier-imperial-sahara','tour-5day-luxury-camp-marrakech']

L=dict(
 en=dict(hx_from="Tours from",hx_spt="Special tours",hx_thm="Themed journeys",hx_va="View all tours",hx_vl="Show less",hx_ce="Explore by city",hx_ch="Where will your journey <em>begin</em>?",hx_cp="Choose your arrival city and discover the private tours that start from there.",hx_n="tours",
  hx_te="Our tours",hx_th="Private tours across <em>Morocco</em>",hx_tp="Every tour is private and can be adapted to your dates, your pace and your budget.",hx_feat="Featured",hx_spe="Special",hx_days="days",hx_day="day",hx_view="View tour",hx_all="Tailor-made tour",
  hx_de="Day trips",hx_dh="One day, <em>one discovery</em>",hx_dp="Short on time? Leave your riad in the morning and be back for dinner, with a private driver.",hx_dm="From Marrakech",hx_df="From Fes",
  hx_ae="Activities",hx_ah="Adventures in <em>the desert</em>",hx_ap="Quads, buggies, camels and nights under the stars, in Merzouga and in the Agafay desert.",hx_am="Merzouga",hx_aa="Agafay",hx_aall="All activities",
  hx_fe="Ready when you are",hx_fh="Let’s design your <em>Morocco</em>",hx_fp="Tell us your dates and your dream. We reply personally with a free itinerary and quote.",hx_fb1="Plan my trip",hx_fb2="Chat on WhatsApp",
  hx_f1="Tours",hx_f2="Experiences",hx_f3="Company",hx_f4="Contact",hx_ft="Private tours, day trips and desert experiences across Morocco, designed by a local team.",hx_cr="All rights reserved."),
 es=dict(hx_from="Circuitos desde",hx_spt="Circuitos especiales",hx_thm="Viajes temáticos",hx_va="Ver todos los circuitos",hx_vl="Ver menos",hx_ce="Explora por ciudad",hx_ch="¿Dónde empieza tu <em>viaje</em>?",hx_cp="Elige tu ciudad de llegada y descubre los circuitos privados que salen desde allí.",hx_n="circuitos",
  hx_te="Nuestros circuitos",hx_th="Circuitos privados por <em>Marruecos</em>",hx_tp="Todos los circuitos son privados y se adaptan a tus fechas, tu ritmo y tu presupuesto.",hx_feat="Destacados",hx_spe="Especiales",hx_days="días",hx_day="día",hx_view="Ver circuito",hx_all="Circuito a medida",
  hx_de="Excursiones",hx_dh="Un día, <em>un descubrimiento</em>",hx_dp="¿Poco tiempo? Sal de tu riad por la mañana y vuelve para la cena, con conductor privado.",hx_dm="Desde Marrakech",hx_df="Desde Fez",
  hx_ae="Actividades",hx_ah="Aventuras en <em>el desierto</em>",hx_ap="Quads, buggies, camellos y noches bajo las estrellas, en Merzouga y en el desierto de Agafay.",hx_am="Merzouga",hx_aa="Agafay",hx_aall="Todas las actividades",
  hx_fe="Cuando tú quieras",hx_fh="Diseñemos tu <em>Marruecos</em>",hx_fp="Cuéntanos tus fechas y tu sueño. Te respondemos personalmente con un itinerario y presupuesto gratis.",hx_fb1="Planificar mi viaje",hx_fb2="Escribir por WhatsApp",
  hx_f1="Circuitos",hx_f2="Experiencias",hx_f3="Empresa",hx_f4="Contacto",hx_ft="Circuitos privados, excursiones y experiencias en el desierto por todo Marruecos, diseñados por un equipo local.",hx_cr="Todos los derechos reservados."),
 fr=dict(hx_from="Circuits au départ de",hx_spt="Circuits thématiques",hx_thm="Voyages à thème",hx_va="Voir tous les circuits",hx_vl="Voir moins",hx_ce="Explorer par ville",hx_ch="Où commencera votre <em>voyage</em> ?",hx_cp="Choisissez votre ville d’arrivée et découvrez les circuits privés qui en partent.",hx_n="circuits",
  hx_te="Nos circuits",hx_th="Circuits privés à travers le <em>Maroc</em>",hx_tp="Tous nos circuits sont privés et s’adaptent à vos dates, votre rythme et votre budget.",hx_feat="Coups de cœur",hx_spe="Thématiques",hx_days="jours",hx_day="jour",hx_view="Voir le circuit",hx_all="Circuit sur mesure",
  hx_de="Excursions",hx_dh="Une journée, <em>une découverte</em>",hx_dp="Peu de temps ? Quittez votre riad le matin et rentrez pour le dîner, avec chauffeur privé.",hx_dm="Depuis Marrakech",hx_df="Depuis Fès",
  hx_ae="Activités",hx_ah="Aventures dans <em>le désert</em>",hx_ap="Quads, buggys, dromadaires et nuits sous les étoiles, à Merzouga et dans le désert d’Agafay.",hx_am="Merzouga",hx_aa="Agafay",hx_aall="Toutes les activités",
  hx_fe="Quand vous voulez",hx_fh="Créons votre <em>Maroc</em>",hx_fp="Donnez-nous vos dates et vos envies. Nous répondons personnellement avec un itinéraire et un devis gratuits.",hx_fb1="Organiser mon voyage",hx_fb2="Écrire sur WhatsApp",
  hx_f1="Circuits",hx_f2="Expériences",hx_f3="Agence",hx_f4="Contact",hx_ft="Circuits privés, excursions et expériences dans le désert à travers le Maroc, conçus par une équipe locale.",hx_cr="Tous droits réservés."),
 it=dict(hx_from="Tour da",hx_spt="Tour speciali",hx_thm="Viaggi a tema",hx_va="Vedi tutti i tour",hx_vl="Mostra meno",hx_ce="Esplora per città",hx_ch="Da dove inizierà il tuo <em>viaggio</em>?",hx_cp="Scegli la città di arrivo e scopri i tour privati che partono da lì.",hx_n="tour",
  hx_te="I nostri tour",hx_th="Tour privati in <em>Marocco</em>",hx_tp="Ogni tour è privato e si adatta alle tue date, al tuo ritmo e al tuo budget.",hx_feat="In evidenza",hx_spe="Speciali",hx_days="giorni",hx_day="giorno",hx_view="Vedi il tour",hx_all="Tour su misura",
  hx_de="Escursioni",hx_dh="Un giorno, <em>una scoperta</em>",hx_dp="Poco tempo? Lascia il riad al mattino e rientra per cena, con autista privato.",hx_dm="Da Marrakech",hx_df="Da Fes",
  hx_ae="Attività",hx_ah="Avventure nel <em>deserto</em>",hx_ap="Quad, buggy, cammelli e notti sotto le stelle, a Merzouga e nel deserto di Agafay.",hx_am="Merzouga",hx_aa="Agafay",hx_aall="Tutte le attività",
  hx_fe="Quando vuoi tu",hx_fh="Progettiamo il tuo <em>Marocco</em>",hx_fp="Raccontaci le tue date e il tuo sogno. Ti rispondiamo di persona con itinerario e preventivo gratuiti.",hx_fb1="Organizza il mio viaggio",hx_fb2="Scrivi su WhatsApp",
  hx_f1="Tour",hx_f2="Esperienze",hx_f3="Agenzia",hx_f4="Contatti",hx_ft="Tour privati, escursioni ed esperienze nel deserto in tutto il Marocco, progettati da un team locale.",hx_cr="Tutti i diritti riservati."))

def _img(ex):
    h=ex.get('hero_src',('{{HERO}}',))[0]
    return h

def build(TOURS,EXTRA_T,ACTS):
    T={l:dict(L[l]) for l in LANGS}
    for c,k,_ in CITIES:
        for l in LANGS:
            n=CNAME[c]; T[l]['hxc_'+c]=n if isinstance(n,str) else n[l]
    byc={}
    for t in TOURS: byc.setdefault(t['city'],[]).append(t)
    # city cards
    cc=''
    for c,k,img in CITIES:
        cc+=f'<button class="hx-city reveal" type="button" data-city="{c}"><img src="{{{{IMG_{img}}}}}" alt="" loading="lazy"><span class="hx-cn"><b data-i="hxc_{c}">x</b><small>{len(byc.get(c,[]))} <span data-i="hx_n">tours</span></small></span><svg class="hx-go"><use href="#i-arrow"/></svg></button>'
    # tour cards
    def card(t,extra=''):
        ex=EXTRA_T.get(t['id'],{}); k=t['k']
        for l in LANGS: T[l]['hxt_'+k]=t['t'][l]; T[l]['hxr_'+k]=t['route'][l]
        cities=' '.join(['all',t['city']]+(['feat'] if t['id'] in FEATURED else []))
        return (f'<a class="hx-tc{extra}" href="{t["id"]}.html" data-c="{cities}"><span class="hx-ti"><img src="{_img(ex)}" alt="" loading="lazy">'
                f'<span class="hx-dd"><b>{t["days"]}</b> <span data-i="{"hx_day" if t["days"]==1 else "hx_days"}">days</span></span></span>'
                f'<span class="hx-tb"><b data-i="hxt_{k}">x</b><small data-i="hxr_{k}">x</small><span class="hx-tl"><span data-i="hx_view">View tour</span><svg><use href="#i-arrow"/></svg></span></span></a>')
    tours=[t for t in TOURS if t['city']!='daytrip']
    blocks=''
    for c in [x for x,_,_ in CITIES]+['special']:
        lst=[t for t in tours if t['city']==c]
        if not lst: continue
        n=len(lst)
        head=(f'<small data-i="hx_from">x</small><h3 data-i="hxc_{c}">x</h3>' if c!='special' else '<small data-i="hx_thm">x</small><h3 data-i="hx_spt">x</h3>')
        cards=''.join(card(t,' xtra' if i>=4 else '') for i,t in enumerate(lst))
        more=(f'<div class="hx-cbf"><button class="hx-cbm" type="button"><span data-i="hx_va">View all tours</span> <span class="hx-cnt">({n})</span><svg><use href="#i-arrow"/></svg></button></div>' if n>4 else '')
        blocks+=f'<div class="hx-cb reveal" id="{"special" if c=="special" else "tours-"+c}"><div class="hx-cbh"><div>{head}</div><span class="hx-cbn">{n} <span data-i="hx_n">tours</span></span></div><div class="hx-tgrid">{cards}</div>{more}</div>'
    anchors=''
    # day trips
    dts=[t for t in TOURS if t['city']=='daytrip']
    dc=''
    for t in dts:
        ex=EXTRA_T.get(t['id'],{}); k=t['k']
        for l in LANGS: T[l]['hxt_'+k]=t['t'][l]
        frm='hx_df' if 'moulay' in t['id'] else 'hx_dm'
        dc+=f'<a class="hx-dt reveal" href="{t["id"]}.html"><img src="{_img(ex)}" alt="" loading="lazy"><span class="hx-dtb"><small data-i="{frm}">x</small><b data-i="hxt_{k}">x</b></span><svg class="hx-go"><use href="#i-arrow"/></svg></a>'
    # activities
    ac=''
    for a in ACTS:
        for l in LANGS: T[l]['hxa_'+a['id'].replace('-','_')]=a['t'][l]
        ac+=f'<a class="hx-ac" href="{a["id"]}.html"><img src="{{{{IMG_{a["id"]}}}}}" alt="" loading="lazy"><span><small data-i="{"hx_am" if a["dest"]=="m" else "hx_aa"}">x</small><b data-i="hxa_{a["id"].replace("-","_")}">x</b></span></a>'
    HTML=f'''
<section class="hx-cities" id="tours">
  {anchors}
  <div class="in">
    <div class="hx-head reveal"><span class="eyebrow" data-i="hx_ce">x</span><h2 data-i="hx_ch">x</h2><p data-i="hx_cp">x</p></div>
    <div class="hx-cgrid">{cc}</div>
  </div>
</section>
<section class="hx-tours" id="hxTours">
  <div class="in">
    <div class="hx-head hx-left reveal"><div><span class="eyebrow" data-i="hx_te">x</span><h2 data-i="hx_th">x</h2></div><p data-i="hx_tp">x</p></div>
    <div class="hx-cbs" id="hxGrid">{blocks}</div>
    <div class="hx-more"><a class="btn gold" href="contact.html"><span data-i="hx_all">x</span><svg><use href="#i-arrow"/></svg></a></div>
  </div>
</section>
<section class="hx-days" id="day-trips">
  <div class="in">
    <div class="hx-head reveal"><span class="eyebrow" data-i="hx_de">x</span><h2 data-i="hx_dh">x</h2><p data-i="hx_dp">x</p></div>
    <div class="hx-dgrid">{dc}</div>
  </div>
</section>
<section class="hx-acts" id="activities">
  <div class="in">
    <div class="hx-head hx-left reveal"><div><span class="eyebrow" data-i="hx_ae">x</span><h2 data-i="hx_ah">x</h2></div><div class="hx-ar"><p data-i="hx_ap">x</p><span class="hx-arr"><button type="button" class="hx-ab prev" aria-label="Previous"><svg><use href="#i-arrow"/></svg></button><button type="button" class="hx-ab next" aria-label="Next"><svg><use href="#i-arrow"/></svg></button></span></div></div>
  </div>
  <div class="hx-atrack" id="hxAct">{ac}</div>
</section>
<section class="hx-final">
  <img src="{{{{IMG_lx-camp}}}}" alt="" loading="lazy">
  <div class="in"><span class="eyebrow" data-i="hx_fe">x</span><h2 data-i="hx_fh">x</h2><p data-i="hx_fp">x</p>
   <div class="row"><a class="btn gold" href="contact.html"><span data-i="hx_fb1">x</span><svg><use href="#i-arrow"/></svg></a><a class="btn hx-wa" id="hxWa" href="#" target="_blank" rel="noopener"><svg><use href="#i-wa"/></svg><span data-i="hx_fb2">x</span></a></div></div>
</section>
<footer class="hx-foot">
  <div class="in hx-fgrid">
    <div class="hx-fbrand"><img src="{{{{EMBLEM}}}}" alt=""><b data-brand="full">MoroccoRoyalTrips</b><p data-i="hx_ft">x</p></div>
    <div><h4 data-i="hx_f1">x</h4>{''.join(f'<a href="#tours-{c}" data-i="c_{c[:3]}s">x</a>' for c,_,_ in CITIES)}</div>
    <div><h4 data-i="hx_f2">x</h4><a href="#day-trips" data-i="m2">x</a><a href="merzouga.html" data-i="hx_am">x</a><a href="agafay.html" data-i="hx_aa">x</a><a href="#special" data-i="hx_spe">x</a></div>
    <div><h4 data-i="hx_f3">x</h4><a href="about.html" data-i="m4">x</a><a href="contact.html" data-i="m6">x</a></div>
    <div><h4 data-i="hx_f4">x</h4><a class="js-hwa" href="#" target="_blank" rel="noopener">WhatsApp</a><a href="mailto:moroccoroyaltrips0@gmail.com">moroccoroyaltrips0@gmail.com</a><span class="hx-soc"><a href="https://www.instagram.com/morocco_royal_trips/" target="_blank" rel="noopener">Instagram</a><a href="https://www.facebook.com/share/1KHcsaf3p6/" target="_blank" rel="noopener">Facebook</a></span></div>
  </div>
  <div class="in hx-fbot"><span>© <span class="hx-yr">2026</span> <span data-brand="full">MoroccoRoyalTrips</span>. <span data-i="hx_cr">x</span></span><span>EN · ES · FR · IT</span></div>
</footer>
'''
    return HTML,T

CSS='''
/* ===== HOME: cities, tours, day trips, activities, footer ===== */
.hx-head{display:grid;justify-items:center;text-align:center;gap:12px;max-width:760px;margin:0 auto 54px}
.hx-head .eyebrow{color:#9a7433;text-shadow:none}.hx-head .eyebrow::before{animation:none}
.hx-head h2{font-size:clamp(34px,4.6vw,62px);line-height:1;margin:4px 0 0;color:#16213d}
.hx-head h2 em{color:#b0843f}
.hx-head p{margin:4px 0 0;font-size:17px;line-height:1.75;color:#4a536d}
.hx-left{max-width:none;display:flex;justify-content:space-between;align-items:flex-end;gap:30px;flex-wrap:wrap;text-align:left;justify-items:start}
.hx-left>div:first-child{display:grid;gap:12px}
.hx-left p{max-width:46ch}
.hx-anc{position:absolute;top:-90px}
.hx-cities{position:relative;background:#fffaf1;padding-block:110px}

.hx-cgrid{display:grid;grid-template-columns:repeat(4,1fr);grid-auto-rows:240px;gap:18px}
.hx-city{position:relative;border:0;padding:0;border-radius:22px;overflow:hidden;cursor:pointer;background:#e8dcc5;box-shadow:0 18px 40px rgba(22,33,61,.12);isolation:isolate;text-align:left;color:#fff;font:inherit}
.hx-city:first-child{grid-row:span 2;grid-column:span 2}
.hx-city:nth-child(6),.hx-city:nth-child(7){grid-column:span 2}
.hx-city img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;max-width:none;transition:transform 1.2s var(--ease);z-index:-2}
.hx-city::after{content:"";position:absolute;inset:0;background:linear-gradient(0deg,rgba(8,10,18,.82),rgba(8,10,18,.05) 60%);z-index:-1;transition:background .5s}
.hx-city:hover img{transform:scale(1.07)}
.hx-cn{position:absolute;left:24px;bottom:22px;display:grid;gap:4px}
.hx-cn b{font-family:var(--display);font-weight:400;font-size:clamp(24px,2.4vw,34px);text-transform:uppercase;letter-spacing:.02em}
.hx-city:first-child .hx-cn b{font-size:clamp(34px,4vw,54px)}
.hx-cn small{font-size:12px;letter-spacing:.22em;text-transform:uppercase;color:var(--gold-hi)}
.hx-go{position:absolute;right:22px;bottom:24px;width:40px;height:40px;padding:12px;border-radius:50%;border:1px solid rgba(255,255,255,.4);color:#fff;transition:background .4s,color .4s,transform .4s}
.hx-city:hover .hx-go,.hx-dt:hover .hx-go{background:var(--gold-hi);color:#16213d;border-color:var(--gold-hi);transform:translateX(3px)}
.hx-tours{background:#f5efe4;padding-block:110px}
.hx-cities,.hx-tours{position:relative;isolation:isolate;overflow:hidden}
.hx-cities{background:radial-gradient(1100px 520px at 50% 0,#fbf0da 0,rgba(251,240,218,0) 70%),#fffaf1}
.hx-cities::before{content:"";position:absolute;inset:0;z-index:-1;pointer-events:none;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='96' height='96' viewBox='0 0 96 96'%3E%3Cg fill='none' stroke='%23a87a35' stroke-width='1.1'%3E%3Crect x='31' y='31' width='34' height='34'/%3E%3Crect x='31' y='31' width='34' height='34' transform='rotate%2845 48 48%29'/%3E%3Ccircle cx='48' cy='48' r='5.5'/%3E%3Cpath d='M0 0l13 13M96 0L83 13M0 96l13-13M96 96l-13-13M48 0v7M48 96v-7M0 48h7M96 48h-7'/%3E%3C/g%3E%3C/svg%3E");background-size:96px 96px;opacity:.16;-webkit-mask-image:radial-gradient(ellipse 70% 60% at 50% 40%,transparent 25%,#000 90%);mask-image:radial-gradient(ellipse 70% 60% at 50% 40%,transparent 25%,#000 90%)}
.hx-tours{background:linear-gradient(180deg,#f3ead9 0,#f6f0e5 40%,#f3ead9 100%)}
.hx-tours::before{content:"";position:absolute;inset:0;z-index:-1;pointer-events:none;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='64' height='96' viewBox='0 0 64 96'%3E%3Cg fill='none' stroke='%23a87a35' stroke-width='1.1'%3E%3Cpath d='M32 0C32 24 0 24 0 48S32 72 32 96M32 0C32 24 64 24 64 48S32 72 32 96'/%3E%3Ccircle cx='32' cy='48' r='3'/%3E%3Ccircle cx='0' cy='0' r='3'/%3E%3Ccircle cx='64' cy='0' r='3'/%3E%3Ccircle cx='0' cy='96' r='3'/%3E%3Ccircle cx='64' cy='96' r='3'/%3E%3C/g%3E%3C/svg%3E");background-size:64px 96px;opacity:.13;-webkit-mask-image:linear-gradient(180deg,#000 0,rgba(0,0,0,.35) 30%,rgba(0,0,0,.35) 70%,#000 100%);mask-image:linear-gradient(180deg,#000 0,rgba(0,0,0,.35) 30%,rgba(0,0,0,.35) 70%,#000 100%)}
.hx-tours::after{content:"";position:absolute;left:50%;top:0;width:min(760px,80%);height:1px;transform:translateX(-50%);background:linear-gradient(90deg,transparent,#c9a05a,transparent);opacity:.7}

.hx-tabs{display:flex;gap:8px;overflow-x:auto;scrollbar-width:none;padding-bottom:6px;margin-bottom:34px}
.hx-tabs::-webkit-scrollbar{display:none}
.hx-tabs button{flex:none;border:1px solid rgba(22,33,61,.18);background:transparent;color:#16213d;border-radius:999px;padding:11px 20px;font:500 12px var(--body);letter-spacing:.16em;text-transform:uppercase;cursor:pointer;transition:background .3s,color .3s,border-color .3s}
.hx-tabs button:hover{border-color:#b0843f}
.hx-tabs button.on{background:#16213d;color:var(--gold-hi);border-color:#16213d}
.hx-tgrid{display:grid;grid-template-columns:repeat(4,1fr);gap:22px}
.hx-tb b{font-size:19px}
.hx-tb{padding:20px 20px 22px}
.hx-cnt{opacity:.7}
.hx-more{gap:14px;flex-wrap:wrap}
.hx-more .btn.ghost{border:1px solid rgba(22,33,61,.25);color:#16213d;background:transparent}.hx-more .btn.ghost:hover{background:#16213d;color:#fff}.hx-more .btn svg{width:16px;height:16px}
.hx-tc.xtra{display:none}.hx-cb.open .hx-tc.xtra{display:flex}
.hx-cbs{display:grid;gap:70px}
.hx-cb{scroll-margin-top:96px;min-width:0}.hx-cbs{grid-template-columns:minmax(0,1fr)}
.hx-cbh{display:flex;align-items:flex-end;justify-content:space-between;gap:16px;padding-bottom:16px;margin-bottom:26px;border-bottom:1px solid rgba(22,33,61,.14);position:relative}
.hx-cbh::after{content:"";position:absolute;left:0;bottom:-1px;width:90px;height:2px;background:linear-gradient(90deg,#c9a05a,#e9cd8e)}
.hx-cbh small{display:block;font-size:11.5px;letter-spacing:.26em;text-transform:uppercase;color:#9a7433;margin-bottom:6px}
.hx-cbh h3{margin:0;font-family:var(--display);font-weight:400;font-size:clamp(28px,3vw,42px);line-height:1;text-transform:uppercase;color:#16213d}
.hx-cbn{flex:none;font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:#6a7187}
.hx-cbf{display:flex;justify-content:center;margin-top:28px}
.hx-cbm{display:inline-flex;align-items:center;gap:10px;cursor:pointer;border:1px solid rgba(22,33,61,.25);background:transparent;color:#16213d;border-radius:999px;padding:13px 26px;font:500 12px var(--body);letter-spacing:.18em;text-transform:uppercase;transition:background .3s,color .3s,border-color .3s}
.hx-cbm:hover{background:#16213d;color:var(--gold-hi);border-color:#16213d}
.hx-cbm svg{width:15px;height:15px;transform:rotate(90deg);transition:transform .35s}.hx-cb.open .hx-cbm svg{transform:rotate(-90deg)}
@media(max-width:640px){.hx-cbs{gap:52px}.hx-cbh{align-items:flex-start;flex-direction:column;gap:6px}
 .hx-cb .hx-tgrid{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding-inline:16px;gap:14px;margin-inline:-16px;padding:4px 16px 14px;scrollbar-width:none}.hx-cb .hx-tgrid::-webkit-scrollbar{display:none}
 .hx-cb .hx-tc{flex:0 0 80%;scroll-snap-align:start}.hx-cbf{margin-top:14px}}
.hx-tc{display:flex;flex-direction:column;background:#fffaf1;border-radius:22px;overflow:hidden;box-shadow:0 18px 40px rgba(22,33,61,.08);transition:transform .5s var(--ease),box-shadow .5s;animation:hxin .6s var(--ease) both}
.hx-tc[hidden]{display:none}
@keyframes hxin{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}
.hx-tc:hover{transform:translateY(-5px);box-shadow:0 26px 54px rgba(22,33,61,.14)}
.hx-ti{position:relative;aspect-ratio:4/3;overflow:hidden;background:#e8dcc5}
.hx-ti img{width:100%;height:100%;object-fit:cover;max-width:none;transition:transform 1.2s var(--ease)}
.hx-tc:hover .hx-ti img{transform:scale(1.06)}
.hx-dd{position:absolute;left:16px;top:16px;background:rgba(14,14,14,.78);backdrop-filter:blur(6px);color:#fff;border-radius:999px;padding:7px 14px;font-size:11px;letter-spacing:.18em;text-transform:uppercase}
.hx-dd b{font-family:var(--display);font-weight:400;font-size:16px;letter-spacing:0;color:var(--gold-hi)}
.hx-tb{display:grid;gap:8px;padding:22px 24px 24px;flex:1;align-content:start}
.hx-tb b{font-family:var(--display);font-weight:400;font-size:21px;line-height:1.15;color:#16213d;text-transform:uppercase}
.hx-tb small{font-size:13.5px;line-height:1.6;color:#6a7187}
.hx-tl{display:inline-flex;align-items:center;gap:10px;margin-top:8px;font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:#9a7433}
.hx-tl svg{width:15px;height:15px;transition:transform .4s}.hx-tc:hover .hx-tl svg{transform:translateX(5px)}
.hx-more{display:flex;justify-content:center;margin-top:44px}
.hx-days{background:#efe5d3;padding-block:110px}
.hx-dgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.hx-dt{position:relative;border-radius:22px;overflow:hidden;aspect-ratio:4/5;color:#fff;isolation:isolate;display:block}
.hx-dt img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;max-width:none;z-index:-2;transition:transform 1.2s var(--ease)}
.hx-dt::after{content:"";position:absolute;inset:0;background:linear-gradient(0deg,rgba(8,10,18,.85),rgba(8,10,18,0) 55%);z-index:-1}
.hx-dt:hover img{transform:scale(1.06)}
.hx-dtb{position:absolute;left:24px;right:80px;bottom:24px;display:grid;gap:6px}
.hx-dtb small{font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--gold-hi)}
.hx-dtb b{font-family:var(--display);font-weight:400;font-size:clamp(22px,2.1vw,28px);line-height:1.1;text-transform:uppercase}
.hx-acts{background:#fffaf1;padding-block:110px;overflow:hidden}

.hx-ar{display:flex;align-items:flex-end;gap:26px}.hx-ar p{color:#4a536d;margin:0}
.hx-arr{display:flex;gap:10px;flex:none}
.hx-ab{width:48px;height:48px;border-radius:50%;border:1px solid rgba(22,33,61,.25);background:transparent;color:#16213d;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:background .3s,color .3s}
.hx-ab:hover{background:#16213d;color:var(--gold-hi);border-color:#16213d}
.hx-ab svg{width:16px;height:16px}.hx-ab.prev svg{transform:rotate(180deg)}
.hx-atrack{display:flex;gap:20px;padding-bottom:30px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-behavior:smooth;padding-inline:max(16px,calc((100vw - var(--max))/2 + 16px));scrollbar-width:none}
.hx-atrack::-webkit-scrollbar{display:none}
.hx-ac{position:relative;flex:0 0 clamp(240px,26vw,320px);box-shadow:0 18px 40px rgba(22,33,61,.12);background:#e8dcc5;aspect-ratio:3/4;border-radius:22px;overflow:hidden;scroll-snap-align:start;color:#fff;isolation:isolate}
.hx-ac img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;max-width:none;z-index:-2;transition:transform 1.2s var(--ease)}
.hx-ac::after{content:"";position:absolute;inset:0;background:linear-gradient(0deg,rgba(8,10,18,.85),rgba(8,10,18,0) 55%);z-index:-1}
.hx-ac:hover img{transform:scale(1.07)}
.hx-ac span{position:absolute;left:22px;right:22px;bottom:22px;display:grid;gap:6px}
.hx-ac small{font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--gold-hi)}
.hx-ac b{font-family:var(--display);font-weight:400;font-size:22px;line-height:1.12;text-transform:uppercase}
.hx-final{position:relative;padding-block:130px;text-align:center;color:#fff;background:#0e0e0e;overflow:hidden;isolation:isolate}
.hx-final>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;max-width:none;opacity:.42;z-index:-1}
.hx-final .in{display:grid;justify-items:center;gap:18px}
.hx-final .eyebrow{color:var(--gold-hi)}
.hx-final h2{font-size:clamp(38px,5.4vw,74px);line-height:1;margin:0;color:#fff}.hx-final h2 em{color:var(--gold-hi)}
.hx-final p{max-width:52ch;margin:0;font-size:17px;line-height:1.7;color:rgba(255,255,255,.85)}
.hx-final .row{display:flex;gap:14px;flex-wrap:wrap;justify-content:center;margin-top:10px}
.btn.hx-wa{background:#25d366;color:#fff}.btn.hx-wa svg{width:18px;height:18px}
.hx-foot{background:#0a0f1d;color:rgba(255,255,255,.72);padding-top:80px;font-size:14.5px}
.hx-fgrid{display:grid;grid-template-columns:1.5fr 1fr 1fr 1fr 1.3fr;gap:40px;padding-bottom:56px}
.hx-fbrand{display:grid;gap:14px;align-content:start}
.hx-fbrand img{width:110px;height:110px;object-fit:contain}
.hx-fbrand b{font-family:var(--display);font-weight:400;font-size:24px;color:#fff;letter-spacing:.04em}
.hx-fbrand p{margin:0;line-height:1.7;max-width:34ch}
.hx-fgrid h4{margin:0 0 16px;font-size:12px;letter-spacing:.24em;text-transform:uppercase;color:var(--gold-hi);font-weight:500}
.hx-fgrid>div:not(.hx-fbrand){display:grid;gap:10px;align-content:start}
.hx-fgrid a{color:rgba(255,255,255,.72);transition:color .3s;overflow-wrap:anywhere}.hx-fgrid a:hover{color:var(--gold-hi)}
.hx-fbot{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap;padding-block:24px;border-top:1px solid rgba(255,255,255,.1);font-size:12.5px;letter-spacing:.06em}
@media(max-width:1000px){
 .hx-cgrid{grid-template-columns:repeat(2,1fr);grid-auto-rows:200px}
 .hx-city:nth-child(6),.hx-city:nth-child(7){grid-column:span 1}
 .hx-tgrid,.hx-dgrid{grid-template-columns:repeat(2,1fr)}
 .hx-fgrid{grid-template-columns:1fr 1fr}.hx-fbrand{grid-column:1/-1}
}
@media(max-width:640px){
 .hx-cities,.hx-tours,.hx-days,.hx-acts{padding-block:80px}
 .hx-head{margin-bottom:38px}.hx-head h2{font-size:clamp(28px,8vw,40px)}
 .hx-cgrid{grid-auto-rows:170px;gap:12px}
 .hx-city:first-child{grid-row:span 1;grid-column:span 2}
 .hx-cn{left:16px;bottom:14px}.hx-cn b{font-size:22px}.hx-city:first-child .hx-cn b{font-size:30px}
 .hx-go{width:34px;height:34px;padding:10px;right:14px;bottom:16px}
 .hx-tgrid,.hx-dgrid{grid-template-columns:1fr}
 .hx-dt{aspect-ratio:16/11}
 .hx-ar{flex-direction:column;align-items:flex-start;gap:18px}
 .hx-final{padding-block:90px}
 .hx-fgrid>div:last-child{grid-column:1/-1}
}
'''

JS='''<script>(function(){var g=document.getElementById('hxGrid');if(!g)return;
document.querySelectorAll('.hx-cb').forEach(function(cb){var bt=cb.querySelector('.hx-cbm');if(!bt)return;var sp=bt.querySelector('[data-i]');
 bt.onclick=function(){var o=cb.classList.toggle('open');var k=o?'hx_vl':'hx_va';sp.dataset.i=k;sp.innerHTML=(T[LANG]||T.en)[k];if(!o)cb.scrollIntoView({behavior:'smooth'})}});
function go(id,sm){var el=document.getElementById(id);if(el)el.scrollIntoView({behavior:sm?'smooth':'auto'})}
[].slice.call(document.querySelectorAll('.hx-city')).forEach(function(c){c.onclick=function(){go('tours-'+c.dataset.city,true)}});
function hash(){var h=location.hash.replace('#','');if(/^tours-\w+$/.test(h)||h==='special')setTimeout(function(){go(h)},60)}
addEventListener('hashchange',hash);hash();
document.querySelectorAll('a[href^="#tours-"],a[href="#special"]').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();var id=a.getAttribute('href').slice(1);go(id,true);history.replaceState(null,'','#'+id)})});
var t=document.getElementById('hxAct');document.querySelector('.hx-ab.prev').onclick=function(){t.scrollBy({left:-t.clientWidth*0.8})};document.querySelector('.hx-ab.next').onclick=function(){t.scrollBy({left:t.clientWidth*0.8})};
try{var wa='https://wa.me/'+(typeof WA!=='undefined'?WA:'');document.getElementById('hxWa').href=wa;document.querySelectorAll('.js-hwa').forEach(function(a){a.href=wa});}catch(e){}
document.querySelectorAll('.hx-yr').forEach(function(e){e.textContent=new Date().getFullYear()});
})();</script>'''
