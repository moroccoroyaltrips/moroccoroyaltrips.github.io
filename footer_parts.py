import json, re
WA_NUM='+212 659 288 638'; WA_LINK='https://wa.me/212659288638'
MAIL='moroccoroyaltrips0@gmail.com'
TRIPADVISOR_URL='#'   # put the real Tripadvisor listing URL here
INSTAGRAM_URL='https://www.instagram.com/morocco_royal_trips/'
FACEBOOK_URL='https://www.facebook.com/share/1KHcsaf3p6/'      # put the real Instagram URL here (empty = hidden)
STAR='<path d="M12 2l2.9 5.1L20 4l-3.1 5.1L22 12l-5.1 2.9L20 20l-5.1-3.1L12 22l-2.9-5.1L4 20l3.1-5.1L2 12l5.1-2.9L4 4l5.1 3.1z" fill="currentColor"/>'
def ic(p): return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'
I_WA='<svg viewBox="0 0 24 24" aria-hidden="true"><use href="#i-wa"/></svg>'
I_MAIL=ic('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>')
I_PIN=ic('<circle cx="12" cy="10" r="3"/><path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/>')
I_CLK=ic('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>')
I_REV=ic('<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/><path d="M9 11l1.3 1.3L13.5 9"/>')
I_IG=ic('<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".6" fill="currentColor"/>')
I_FB='<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M13.5 21v-7.5h2.6l.4-3h-3V8.6c0-.9.3-1.5 1.6-1.5h1.6V4.4c-.3 0-1.2-.1-2.3-.1-2.3 0-3.9 1.4-3.9 4V10.5H7.9v3h2.6V21z"/></svg>'
I_OWL='<svg viewBox="0 0 32 20" aria-hidden="true"><path d="M9 3h14l-2 2.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><circle cx="8.5" cy="12" r="6" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="23.5" cy="12" r="6" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="8.5" cy="12" r="2.3" fill="currentColor"/><circle cx="23.5" cy="12" r="2.3" fill="currentColor"/><path d="M14.5 15l1.5 2.5 1.5-2.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>'
I_UP=ic('<path d="M12 19V5M5 12l7-7 7 7"/>')

CITIES=[('marrakech','c_mars'),('fes','c_fess'),('tangier','c_tans'),('casablanca','c_cass'),('errachidia','c_errs'),('ouarzazate','c_ouas'),('agadir','c_agas')]

MAIL_JS='<script>(function(){\nvar M={en:\'Email copied\',es:\'Email copiado\',fr:\'E-mail copié\',it:\'Email copiata\',zh:\'邮箱已复制\'};\nfunction toast(t){var d=document.createElement(\'div\');d.textContent=t;d.style.cssText=\'position:fixed;left:50%;bottom:28px;transform:translateX(-50%);background:#16213d;color:#e9cd8e;font:600 13px/1 system-ui,sans-serif;letter-spacing:.06em;padding:14px 20px;border-radius:999px;z-index:99999;box-shadow:0 12px 30px rgba(0,0,0,.35)\';document.body.appendChild(d);setTimeout(function(){d.remove()},2200)}\ndocument.addEventListener(\'click\',function(e){var a=e.target.closest&&e.target.closest(\'a[href^="mailto:"]\');if(!a)return;\n var mail=a.getAttribute(\'href\').slice(7).split(\'?\')[0];\n try{navigator.clipboard&&navigator.clipboard.writeText(mail)}catch(x){}\n var l=(document.documentElement.lang||\'en\').slice(0,2);toast((M[l]||M.en)+\' · \'+mail);\n e.preventDefault();var w=null;try{w=window.open(a.href,\'_blank\')}catch(x){}\n if(!w){try{window.top.location.href=a.href}catch(x){location.href=a.href}}\n},true);})();</script>\n'
def html():
    ig=f'<a class="r-ig" href="{INSTAGRAM_URL}" target="_blank" rel="noopener" aria-label="Instagram">{I_IG}</a>' if INSTAGRAM_URL else ''
    fb=f'<a class="r-fb" href="{FACEBOOK_URL}" target="_blank" rel="noopener" aria-label="Facebook">{I_FB}</a>' if FACEBOOK_URL else ''
    tours=''.join(f'<li><a href="index.html#tours-{c}" data-i="{k}">x</a></li>' for c,k in CITIES)
    return f'''<footer class="ft">
  <div class="ft-band">
    <div class="in ft-band-in">
      <div class="ft-band-t"><span class="ft-kh" aria-hidden="true"><svg viewBox="0 0 24 24">{STAR}</svg></span><div><b data-i="ft_bh">Ready to plan your journey?</b><span data-i="ft_bp">Tell us your dates and we reply personally with a free itinerary.</span></div></div>
      <div class="ft-band-b"><a class="ft-btn gold" href="{WA_LINK}" target="_blank" rel="noopener">{I_WA}<span data-i="ft_wa">Chat on WhatsApp</span></a><a class="ft-btn line" href="contact.html"><span data-i="ft_q">Free quote</span><svg aria-hidden="true"><use href="#i-arrow"/></svg></a></div>
    </div>
  </div>
  <div class="in ft-grid">
    <div class="ft-brand">
      <a class="ft-logo" href="index.html"><img src="{{{{EMBLEM}}}}" alt="MoroccoRoyalTrips logo"><span><b>MOROCCO ROYAL</b><small>TRIPS</small></span></a>
      <p data-i="ft_about">Private tours, day trips and desert experiences across Morocco, designed by a local team.</p>
      <a class="ft-ta2" href="{TRIPADVISOR_URL}" target="_blank" rel="noopener" aria-label="Tripadvisor"><small data-i="ft_ta1">Read our reviews on</small><img src="images/ta-logo.png" alt="Tripadvisor" width="163" height="58" loading="lazy"></a>
      <div class="ft-rnd">
        <a class="r-wa" href="{WA_LINK}" target="_blank" rel="noopener" aria-label="WhatsApp">{I_WA}</a>
        {ig}
        {fb}
        <a class="r-ml" href="mailto:{MAIL}" aria-label="Email">{I_MAIL}</a>
        <a class="r-ta" href="{TRIPADVISOR_URL}" target="_blank" rel="noopener" aria-label="Tripadvisor">{I_OWL}</a>
      </div>
    </div>
    <nav class="ft-col" aria-label="Tours"><h4 data-i="ft_h1">Tours</h4><ul>{tours}</ul></nav>
    <nav class="ft-col" aria-label="Experiences"><h4 data-i="ft_h2">Experiences</h4><ul>
      <li><a href="index.html#day-trips" data-i="m2">x</a></li><li><a href="index.html#special" data-i="ft_spe">x</a></li><li><a href="merzouga.html" data-i="ft_mz">x</a></li><li><a href="agafay.html" data-i="ft_ag">x</a></li></ul>
      <h4 class="ft-h2b" data-i="ft_h3">Company</h4><ul><li><a href="about.html" data-i="m4">x</a></li><li><a href="blog.html" data-i="m5">x</a></li><li><a href="faq.html" data-i="ft_faq">FAQ</a></li><li><a href="contact.html" data-i="m6">x</a></li></ul></nav>
    <div class="ft-col ft-contact"><h4 data-i="ft_h4">Contact</h4><ul>
      <li><a href="{WA_LINK}" target="_blank" rel="noopener">{I_WA}<span><small>WhatsApp</small>{WA_NUM}</span></a></li>
      <li><a href="mailto:{MAIL}">{I_MAIL}<span><small>Email</small>{MAIL}</span></a></li>
      <li><span class="ft-ci">{I_PIN}<span><small data-i="ft_loc">Based in</small><span data-i="ft_loc2">Morocco · tours nationwide</span></span></span></li>
      <li><span class="ft-ci">{I_CLK}<span><small data-i="ft_hr">Replies</small><span data-i="ft_hr2">7 days a week</span></span></span></li>
    </ul></div>
  </div>
  <div class="in ft-bot">
    <span>© <span class="ft-yr">2026</span> MoroccoRoyalTrips. <span data-i="ft_cr">All rights reserved.</span></span>
    <span class="ft-legal"><a href="privacy.html" data-i="ft_pr">Privacy Policy</a><a href="terms.html" data-i="ft_tm">Terms &amp; Conditions</a></span>
    <a class="ft-top" href="#top" aria-label="Back to top">{I_UP}</a>
  </div>
</footer>
{MAIL_JS}'''

T={
'en':dict(ft_bh="Ready to plan your journey?",ft_bp="Tell us your dates and we reply personally with a free itinerary.",ft_wa="Chat on WhatsApp",ft_q="Free quote",
 ft_about="Private tours, day trips and desert experiences across Morocco, designed by a local team that knows every road.",ft_ta1="Read our reviews on",
 ft_h1="Tours",ft_h2="Experiences",ft_h3="Company",ft_h4="Contact",ft_spe="Special tours",ft_mz="Merzouga activities",ft_ag="Agafay activities",
 ft_loc="Based in",ft_loc2="Morocco · tours nationwide",ft_hr="Replies",ft_hr2="7 days a week",ft_cr="All rights reserved.",ft_faq="FAQ",ft_pr="Privacy Policy",ft_tm="Terms & Conditions"),
'es':dict(ft_bh="¿Listo para planificar tu viaje?",ft_bp="Cuéntanos tus fechas y te respondemos personalmente con un itinerario gratis.",ft_wa="Escribir por WhatsApp",ft_q="Presupuesto gratis",
 ft_about="Circuitos privados, excursiones y experiencias en el desierto por todo Marruecos, diseñados por un equipo local que conoce cada carretera.",ft_ta1="Lee nuestras opiniones en",
 ft_h1="Circuitos",ft_h2="Experiencias",ft_h3="Empresa",ft_h4="Contacto",ft_spe="Circuitos especiales",ft_mz="Actividades en Merzouga",ft_ag="Actividades en Agafay",
 ft_loc="Con base en",ft_loc2="Marruecos · circuitos en todo el país",ft_hr="Respondemos",ft_hr2="7 días a la semana",ft_cr="Todos los derechos reservados.",ft_faq="Preguntas frecuentes",ft_pr="Privacidad",ft_tm="Términos y condiciones"),
'fr':dict(ft_bh="Prêt à organiser votre voyage ?",ft_bp="Donnez-nous vos dates, nous vous répondons personnellement avec un itinéraire gratuit.",ft_wa="Écrire sur WhatsApp",ft_q="Devis gratuit",
 ft_about="Circuits privés, excursions et expériences dans le désert à travers le Maroc, conçus par une équipe locale qui connaît chaque route.",ft_ta1="Lisez nos avis sur",
 ft_h1="Circuits",ft_h2="Expériences",ft_h3="Agence",ft_h4="Contact",ft_spe="Circuits thématiques",ft_mz="Activités à Merzouga",ft_ag="Activités à Agafay",
 ft_loc="Basés au",ft_loc2="Maroc · circuits dans tout le pays",ft_hr="Réponses",ft_hr2="7 jours sur 7",ft_cr="Tous droits réservés.",ft_faq="FAQ",ft_pr="Confidentialité",ft_tm="Conditions générales"),
'it':dict(ft_bh="Pronto a organizzare il tuo viaggio?",ft_bp="Raccontaci le tue date e ti rispondiamo di persona con un itinerario gratuito.",ft_wa="Scrivi su WhatsApp",ft_q="Preventivo gratuito",
 ft_about="Tour privati, escursioni ed esperienze nel deserto in tutto il Marocco, progettati da un team locale che conosce ogni strada.",ft_ta1="Leggi le nostre recensioni su",
 ft_h1="Tour",ft_h2="Esperienze",ft_h3="Agenzia",ft_h4="Contatti",ft_spe="Tour speciali",ft_mz="Attività a Merzouga",ft_ag="Attività ad Agafay",
 ft_loc="Con sede in",ft_loc2="Marocco · tour in tutto il paese",ft_hr="Rispondiamo",ft_hr2="7 giorni su 7",ft_cr="Tutti i diritti riservati.",ft_faq="FAQ",ft_pr="Privacy",ft_tm="Termini e condizioni")}

CSS='''
/* ===== FOOTER (all pages) ===== */
.ft{position:relative;background:#0b0a08;color:rgba(243,236,224,.68);font-size:14.5px;overflow:hidden}
.ft::before{content:"";position:absolute;inset:0;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160' viewBox='0 0 24 24'%3E%3Cpath d='M12 2l2.9 5.1L20 4l-3.1 5.1L22 12l-5.1 2.9L20 20l-5.1-3.1L12 22l-2.9-5.1L4 20l3.1-5.1L2 12l5.1-2.9L4 4l5.1 3.1z' fill='none' stroke='%23c9a05a' stroke-opacity='.06' stroke-width='.3'/%3E%3C/svg%3E");pointer-events:none}
.ft>*{position:relative}
.ft a{color:inherit;text-decoration:none}
.ft-band{border-bottom:1px solid rgba(233,205,142,.14);background:linear-gradient(90deg,rgba(201,160,90,.10),rgba(201,160,90,0) 60%)}
.ft-band-in{display:flex;align-items:center;justify-content:space-between;gap:28px;flex-wrap:wrap;padding-block:40px}
.ft-band-t{display:flex;align-items:center;gap:20px}
.ft-kh{width:54px;height:54px;flex:none;border-radius:50%;border:1px solid rgba(233,205,142,.4);display:grid;place-items:center;color:var(--gold-hi)}
.ft-kh svg{width:24px;height:24px;animation:ftspin 14s linear infinite}
@keyframes ftspin{to{transform:rotate(360deg)}}
.ft-band-t b{display:block;font-family:var(--display);font-weight:400;font-size:clamp(24px,2.6vw,34px);line-height:1.1;color:#fff;text-transform:uppercase;letter-spacing:.01em}
.ft-band-t span{display:block;margin-top:6px;color:rgba(243,236,224,.65)}
.ft-band-b{display:flex;gap:12px;flex-wrap:wrap}
.ft-btn{display:inline-flex;align-items:center;gap:10px;padding:15px 26px;border-radius:999px;font:500 12.5px var(--body,Jost),sans-serif;letter-spacing:.18em;text-transform:uppercase;transition:transform .35s var(--ease),background .3s,color .3s}
.ft-btn svg{width:17px;height:17px}
.ft-btn.gold{background:linear-gradient(135deg,#e2c07c,#c9a05a 55%,#b0843f);color:#16213d}
.ft-btn.line{border:1px solid rgba(233,205,142,.45);color:var(--gold-hi)}
.ft-btn:hover{transform:translateY(-2px)}.ft-btn.line:hover{background:rgba(233,205,142,.1)}
.ft-grid{display:grid;grid-template-columns:1.45fr 1fr 1fr 1.35fr;gap:48px;padding-block:68px 56px}
.ft-logo{display:inline-flex;align-items:center;gap:14px}
.ft-logo img{width:84px;height:84px;object-fit:contain;filter:drop-shadow(0 6px 14px rgba(0,0,0,.4))}
.ft-logo b{display:block;font:600 17px/1.1 var(--body,Jost),sans-serif;letter-spacing:.16em;color:#fff}
.ft-logo small{display:block;margin-top:5px;font-size:11px;letter-spacing:.42em;color:var(--gold-hi)}
.ft-brand p{margin:20px 0 24px;line-height:1.75;max-width:36ch}
.ft-socs{display:flex;gap:10px;flex-wrap:wrap}
.ft-ta2{display:inline-grid;gap:6px;justify-items:start;margin-top:4px;padding:10px 14px 8px;border-radius:14px;background:#599442;box-shadow:0 10px 24px rgba(89,148,66,.25);transition:transform .35s var(--ease),box-shadow .35s}
.ft-ta2:hover{transform:translateY(-2px);box-shadow:0 14px 30px rgba(89,148,66,.35)}
.ft-ta2 small{font-size:10.5px;letter-spacing:.08em;color:#fff;opacity:.92}
.ft-ta2 img{display:block;width:150px;height:auto}
.ft-rnd{display:flex;gap:12px;flex-wrap:wrap;margin-top:18px}
.ft-rnd a{width:46px;height:46px;border-radius:50%;display:grid;place-items:center;color:#fff;transition:transform .35s var(--ease),box-shadow .35s,filter .3s}
.ft-rnd a:hover{transform:translateY(-3px) scale(1.06);box-shadow:0 12px 24px rgba(0,0,0,.35)}
.ft-rnd svg{width:22px;height:22px}
.r-wa{background:#25d366}.r-wa svg{fill:#fff}
.r-ig{background:radial-gradient(circle at 30% 107%,#fdf497 0,#fdf497 5%,#fd5949 45%,#d6249f 60%,#285aeb 90%)}
.r-fb{background:#1877f2}
.r-ml{background:#c9a05a;color:#1a1206!important}
.r-ta{background:#34e0a1;color:#0b0a08!important}.r-ta svg{width:28px;height:28px}

.ft-ta{display:inline-flex;align-items:center;gap:12px;padding:10px 18px 10px 12px;border-radius:14px;background:#00af87;color:#fff!important;box-shadow:0 10px 24px rgba(0,175,135,.22);transition:transform .35s var(--ease),box-shadow .35s}
.ft-ta:hover{transform:translateY(-2px);box-shadow:0 14px 30px rgba(0,175,135,.32)}
.ft-ta svg{width:26px;height:26px;flex:none}
.ft-ta small{display:block;font-size:10.5px;letter-spacing:.06em;opacity:.9}
.ft-ta b{display:block;font:700 16px/1.15 var(--body,Jost),sans-serif;letter-spacing:.01em}
.ft-soc{display:inline-flex;align-items:center;gap:10px;padding:10px 16px;border-radius:14px;border:1px solid rgba(233,205,142,.25);color:#f3ece0}
.ft-soc svg{width:20px;height:20px;color:var(--gold-hi)}
.ft-col h4{margin:0 0 18px;font:500 11.5px var(--body,Jost),sans-serif;letter-spacing:.28em;text-transform:uppercase;color:var(--gold-hi)}
.ft-col .ft-h2b{margin-top:30px}
.ft-col ul{list-style:none;margin:0;padding:0;display:grid;gap:11px}
.ft-col a{position:relative;transition:color .3s,padding .35s var(--ease)}
.ft-col a:hover{color:var(--gold-hi);padding-left:6px}
.ft-contact a,.ft-contact .ft-ci{display:flex;align-items:flex-start;gap:12px;overflow-wrap:anywhere}
.ft-contact a:hover{padding-left:0}
.ft-contact svg{width:20px;height:20px;flex:none;margin-top:2px;color:var(--gold-hi)}
.ft-contact small{display:block;font-size:10.5px;letter-spacing:.2em;text-transform:uppercase;color:rgba(243,236,224,.45);margin-bottom:2px}
.ft-contact a:hover>span{color:var(--gold-hi)}
.ft-bot{display:flex;align-items:center;justify-content:space-between;gap:18px;flex-wrap:wrap;padding-block:22px;border-top:1px solid rgba(255,255,255,.08);font-size:12.5px;letter-spacing:.05em}
.ft-legal{display:flex;gap:22px;flex-wrap:wrap}.ft-legal a{color:inherit;letter-spacing:.06em}.ft-legal a:hover{color:var(--gold-hi)}
.ft-top{width:42px;height:42px;border-radius:50%;border:1px solid rgba(233,205,142,.35);display:grid;place-items:center;color:var(--gold-hi);transition:background .3s,color .3s,transform .35s var(--ease)}
.ft-top svg{width:18px;height:18px}.ft-top:hover{background:var(--gold-hi);color:#16213d;transform:translateY(-3px)}
@media(max-width:1000px){.ft-grid{grid-template-columns:1fr 1fr;gap:40px}.ft-brand{grid-column:1/-1}}
@media(max-width:640px){
 .ft-band-in{padding-block:34px;flex-direction:column;align-items:flex-start}
 .ft-band-b{width:100%;flex-direction:column}.ft-btn{width:100%;justify-content:center;padding:15px 16px}
 .ft-grid{grid-template-columns:1fr 1fr;gap:34px 22px;padding-block:48px 40px}
 .ft-contact{grid-column:1/-1}
 .ft-bot{padding-bottom:calc(22px + 76px)}
}
@media(prefers-reduced-motion:reduce){.ft-kh svg{animation:none}}

'''

def apply(s, lang_keys):
    """Replace any existing footer with the new one, add CSS + texts."""
    new=html()
    s2=re.sub(r'<footer class="(?:foot|hx-foot)".*?</footer>',lambda m:new,s,count=1,flags=re.S)
    if s2==s: return s
    s=s2.replace('</style>',CSS+'</style>',1)
    for c,k in lang_keys.items():
        if k in s: s=s.replace(k,k+','.join(f'{x}:{json.dumps(y,ensure_ascii=False)}' for x,y in T[c].items())+',',1)
    s=s.replace('class="ft-yr">2026<','class="ft-yr">2026<')
    return s
