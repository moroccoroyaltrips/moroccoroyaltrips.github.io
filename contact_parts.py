STAR='<path d="M12 2l2.9 5.1L20 4l-3.1 5.1L22 12l-5.1 2.9L20 20l-5.1-3.1L12 22l-2.9-5.1L4 20l3.1-5.1L2 12l5.1-2.9L4 4l5.1 3.1z" fill="currentColor"/>'

CSS = '''
/* ================= CONTACT PAGE ================= */
/* contact hero: desert guide and camel photo */
.hero.hero-sm{min-height:clamp(520px,72vh,780px)}
.hero.hero-sm .hero-bg{object-position:50% 30%}
.hero-sm .hero-shade{background:
  linear-gradient(180deg,rgba(0,0,0,.5) 0%,rgba(0,0,0,0) 28%),
  linear-gradient(0deg,rgba(0,0,0,.72) 0%,rgba(0,0,0,0) 55%),
  radial-gradient(ellipse 55% 65% at 18% 78%,rgba(0,0,0,.4) 0%,rgba(0,0,0,0) 70%)}
@media (max-width:760px){.hero.hero-sm .hero-bg{object-position:63% 50%}}

.hero-sm{min-height:clamp(460px,62vh,640px)}
.hero-sm .hero-bg{object-position:50% 78%}
.hero-sm .hero-in{justify-content:flex-end;padding-block:160px 70px}
.crumbs{display:flex;gap:10px;align-items:center;font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:rgba(255,255,255,.7);text-shadow:0 1px 8px rgba(0,0,0,.6)}
.crumbs a:hover{color:var(--gold-hi)}
.crumbs svg{width:10px;height:10px;transform:rotate(-90deg)}

.contact{background:#f5efe4;color:#16213d;position:relative}
.c-grid{display:grid;grid-template-columns:6fr 5fr;gap:64px;align-items:start;padding-block:110px}
.c-info{display:grid;gap:22px;position:sticky;top:110px}
.c-info .eyebrow{color:#9a7433}
.c-info .eyebrow::before{animation:none}
.c-info h2{font-size:clamp(38px,4.4vw,60px);line-height:.98}
.c-info h2 em{color:#b0843f}
.c-info > p{margin:0;font-size:17px;line-height:1.75;color:#4a536d;max-width:46ch}

.channels{list-style:none;margin:8px 0 0;padding:0;border-top:1px solid rgba(22,33,61,.16)}
.ch{position:relative;display:flex;align-items:center;gap:18px;padding:22px 0;border-bottom:1px solid rgba(22,33,61,.16)}
.ch::after{content:"";position:absolute;left:0;bottom:-1px;height:1px;width:100%;background:#b0843f;transform:scaleX(0);transform-origin:left;transition:transform .6s var(--ease)}
.ch:hover::after{transform:scaleX(1)}
.ch .lbl{width:96px;flex:none;font-size:11px;font-weight:600;letter-spacing:.24em;text-transform:uppercase;color:#9a7433}
.ch .val{flex:1;min-width:0;font-size:19px;font-weight:500;color:#16213d;overflow-wrap:anywhere;user-select:all;transition:transform .5s var(--ease)}
.ch:hover .val{transform:translateX(6px)}
.ch .acts{display:flex;gap:8px;flex:none}
.ibtn{position:relative;width:40px;height:40px;border-radius:50%;border:1px solid rgba(22,33,61,.2);background:transparent;color:#16213d;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:background .3s,border-color .3s,color .3s,transform .4s var(--ease)}
.ibtn svg{width:17px;height:17px}
.ibtn:hover{background:#16213d;border-color:#16213d;color:var(--gold-hi);transform:translateY(-2px)}
.ibtn .tip{position:absolute;bottom:calc(100% + 8px);left:50%;transform:translate(-50%,4px);white-space:nowrap;font-size:11px;font-weight:500;letter-spacing:.06em;background:#16213d;color:#fff;padding:5px 9px;border-radius:6px;opacity:0;pointer-events:none;transition:opacity .25s,transform .3s var(--ease)}
.ibtn.done .tip{opacity:1;transform:translate(-50%,0)}
.c-meta{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:6px}
.c-meta div{display:grid;gap:4px}
.c-meta span{font-size:11px;font-weight:600;letter-spacing:.24em;text-transform:uppercase;color:#9a7433}
.c-meta b{font-weight:500;font-size:15px;color:#16213d}
.c-meta a{border-bottom:1px solid rgba(22,33,61,.25);transition:border-color .3s,color .3s}
.c-meta a:hover{color:#b0843f;border-color:#b0843f}

/* form panel (light, compact) */
.c-form-wrap{justify-self:end;width:100%;max-width:500px}
.c-form{position:relative;background:#fffdf9;color:#16213d;border-radius:20px;padding:34px 32px 30px;display:grid;grid-template-columns:1fr 1fr;gap:22px 22px;border:1px solid rgba(176,132,63,.22);box-shadow:0 30px 60px rgba(22,33,61,.1)}
.c-form::before{content:"";position:absolute;left:32px;right:32px;top:0;height:2px;background:linear-gradient(90deg,transparent,#c9a05a,transparent)}
.c-form .full{grid-column:1/-1}
.f-head{display:grid;gap:6px}
.f-head h3{font-size:clamp(26px,2.4vw,32px);line-height:1;color:#16213d}
.f-head h3 em{color:#b0843f;font-style:normal}
.f-head p{margin:0;color:#6b7289;font-size:14px}
.fld{position:relative;display:grid;gap:6px;min-width:0}
.fld > label,.fld > .lab{font-size:10.5px;font-weight:600;letter-spacing:.22em;text-transform:uppercase;color:#9a7433}
.fld input,.fld textarea{width:100%;background:transparent;border:0;border-bottom:1px solid rgba(22,33,61,.2);color:#16213d;font:400 15.5px var(--body);padding:6px 0 9px;border-radius:0;transition:border-color .3s;color-scheme:light}
.fld textarea{min-height:70px;resize:vertical;line-height:1.55}
.fld input::placeholder,.fld textarea::placeholder{color:rgba(22,33,61,.35)}
.fld .bar{position:absolute;left:0;right:0;bottom:0;height:1.5px;background:#b0843f;transform:scaleX(0);transform-origin:left;transition:transform .5s var(--ease)}
.fld input:focus,.fld textarea:focus{outline:none;border-bottom-color:transparent}
.fld input:focus ~ .bar,.fld textarea:focus ~ .bar{transform:scaleX(1)}
.fld input:user-invalid{border-bottom-color:#d9604c}
.stepper{display:flex;align-items:center;gap:12px;padding:2px 0 5px;border-bottom:1px solid rgba(22,33,61,.2)}
.stepper button{width:28px;height:28px;border-radius:50%;border:1px solid rgba(22,33,61,.22);background:transparent;color:#16213d;font-size:16px;line-height:1;cursor:pointer;transition:background .25s,border-color .25s,color .25s,transform .3s var(--ease)}
.stepper button:hover{background:#16213d;border-color:#16213d;color:#e9cd8e;transform:scale(1.08)}
.stepper output{min-width:20px;text-align:center;font-size:16px;font-variant-numeric:tabular-nums}
.f-foot{display:grid;gap:10px;margin-top:2px}
.f-foot .btn{width:100%;padding:16px 24px}
.f-foot small{color:#8a90a3;font-size:12px;text-align:center}

.sent{grid-column:1/-1;display:grid;justify-items:center;text-align:center;gap:14px;padding:16px 0 6px}
.sent .ok{width:64px;height:64px;border-radius:50%;border:1.5px solid #b0843f;display:flex;align-items:center;justify-content:center;color:#b0843f}
.sent .ok svg{width:30px;height:30px;stroke-dasharray:30;stroke-dashoffset:30;animation:draw .8s var(--ease) .2s forwards}
@keyframes draw{to{stroke-dashoffset:0}}
.sent h3{font-size:28px;color:#16213d}
.sent p{margin:0;color:#6b7289;font-size:14.5px;max-width:38ch}
.sent .row{display:flex;gap:10px;flex-wrap:wrap;justify-content:center;margin-top:4px}
.sent .btn.ghost{border:1px solid rgba(22,33,61,.25);color:#16213d;background:transparent}
.sent .btn.ghost:hover{background:#16213d;color:#fff}
.sent .again{background:none;border:0;color:#6b7289;font:500 11.5px var(--body);letter-spacing:.18em;text-transform:uppercase;cursor:pointer;border-bottom:1px solid rgba(22,33,61,.25);padding-bottom:3px}
.sent .again:hover{color:#16213d}

/* how it works */
.hw{position:relative;background:#f5efe4;padding-block:96px 104px;overflow:hidden;border-top:1px solid rgba(22,33,61,.08)}
.hw::before{content:"";position:absolute;inset:0;background:radial-gradient(rgba(176,138,72,.16) 1px,transparent 1.2px) 0 0/22px 22px;-webkit-mask:linear-gradient(180deg,transparent,#000 30%,#000 70%,transparent);mask:linear-gradient(180deg,transparent,#000 30%,#000 70%,transparent);pointer-events:none}
.hw .in{position:relative}
.hw-hd{text-align:center;max-width:640px;margin:0 auto 64px}
.hw-hd .eyebrow{display:inline-flex;align-items:center;gap:12px;font:600 11.5px var(--body);letter-spacing:.32em;text-transform:uppercase;color:#a07a3c}
.hw-hd .eyebrow::before,.hw-hd .eyebrow::after{content:"";width:28px;height:1px;background:currentColor;opacity:.6}
.hw-hd h2{margin:14px 0 0;font-family:var(--display);font-size:clamp(30px,4.2vw,46px);line-height:1.12;color:#16213d;font-weight:500}
.hw-hd h2 em{font-style:italic;color:#b08a48}
.hw-list{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,1fr);gap:28px;position:relative}
.hw-route{position:absolute;left:16.6%;right:16.6%;top:43px;border-top:2px dotted #c9a465;pointer-events:none}
.hw-st{position:relative;text-align:center;padding:0 10px}
.hw-ic{position:relative;z-index:1;width:88px;height:88px;margin:0 auto 26px;border-radius:50%;background:#fffdf8;border:1px solid rgba(176,138,72,.35);display:grid;place-items:center;color:#16213d;box-shadow:0 14px 30px -18px rgba(22,33,61,.35);transition:transform .5s cubic-bezier(.2,.8,.2,1),background .4s,color .4s}
.hw-ic svg{width:32px;height:32px}
.hw-ic b{position:absolute;top:-6px;right:-6px;width:30px;height:30px;border-radius:50%;background:#16213d;color:#e9cd8e;font:600 12px var(--body);display:grid;place-items:center;letter-spacing:.04em}
.hw-st:hover .hw-ic{transform:translateY(-6px);background:#16213d;color:#e9cd8e}
.hw-st h3{margin:0 0 10px;font-family:var(--display);font-size:24px;font-weight:500;color:#16213d}
.hw-st p{margin:0 auto;max-width:30ch;color:#6b7289;font-size:15px;line-height:1.7}
.hw-st.pay p strong{color:#16213d;font-weight:600}
@media (max-width:820px){
  .hw{padding-block:72px 80px}
  .hw-hd{margin-bottom:44px}
  .hw-list{grid-template-columns:1fr;gap:0;max-width:440px;margin:0 auto}
  .hw-route{display:none}
  .hw-st{display:grid;grid-template-columns:72px 1fr;gap:18px;text-align:left;padding:0 0 34px;align-items:start}
  .hw-st::before{content:"";position:absolute;left:35px;top:72px;bottom:6px;border-left:2px dotted #c9a465}
  .hw-st:last-child{padding-bottom:0}.hw-st:last-child::before{display:none}
  .hw-ic{width:72px;height:72px;margin:0}
  .hw-ic svg{width:26px;height:26px}
  .hw-ic b{width:26px;height:26px;font-size:11px}
  .hw-st h3{font-size:21px;margin:8px 0 6px}
  .hw-st p{max-width:none;margin:0}
}

/* footer */
.foot{background:#0a1226;color:rgba(255,255,255,.6);font-size:14px}
.foot .in{display:flex;align-items:center;justify-content:space-between;gap:20px;flex-wrap:wrap;padding-block:34px}
.foot .fb{display:flex;align-items:center;gap:12px}
.foot img{width:44px;height:44px;border-radius:50%}
.foot nav{display:flex;gap:22px;flex-wrap:wrap;font-size:12px;letter-spacing:.18em;text-transform:uppercase}
.foot nav a:hover{color:var(--gold-hi)}

@media (max-width:900px){
  .c-grid{grid-template-columns:1fr;gap:48px;padding-block:72px}
  .c-info{position:static}
  .c-form-wrap{justify-self:stretch;max-width:none}
  .c-form{padding:28px 20px 24px}
  .ch .lbl{width:78px}
  .ch .val{font-size:17px}
  .hero-sm .hero-in{padding-block:120px 48px}
}
@media (prefers-reduced-motion:reduce){.hw-ic{transition:none}}
'''

ICON_COPY='<svg viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"><rect x="8" y="8" width="12" height="12" rx="2"/><path d="M16 8V5a1 1 0 0 0-1-1H5a1 1 0 0 0-1 1v10a1 1 0 0 0 1 1h3"/></g></svg>'
ICON_OUT='<svg viewBox="0 0 24 24"><path d="M7 17L17 7M9 7h8v8" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>'

MAIN = f'''<main id="top">
<section class="hero hero-sm" id="hero">
  <div class="hero-media" id="heroMedia"><img class="hero-bg" src="{{{{CHERO}}}}" alt="Desert guide in a blue robe leading a camel across the Sahara dunes"></div>
  <div class="hero-shade" aria-hidden="true"></div>
  <canvas id="dust" aria-hidden="true"></canvas>
  <div class="in hero-in">
    <div class="hero-copy">
      <nav class="crumbs rise" aria-label="Breadcrumb"><a href="index.html" data-i="m0">Home</a><svg><use href="#i-chev"/></svg><span data-i="m6">Contact</span></nav>
      <h1 id="heroTitle" data-i="c_t">Let's plan your <em>journey</em></h1>
      <div class="khatam" aria-hidden="true"><span></span><svg viewBox="0 0 24 24">{STAR}</svg><span></span></div>
      <p class="lead rise d3" data-i="c_p">Tell us how you imagine your trip. We answer personally with ideas, a clear itinerary and a free quote.</p>
    </div>
  </div>
</section>

<section class="contact" id="contact">
  <div class="in c-grid">
    <aside class="c-info reveal">
      <span class="eyebrow" data-i="ci_e">Get in touch</span>
      <h2 data-i="ci_h">Talk to a <em>real person</em></h2>
      <p data-i="ci_p">No call centre and no robots. Write to us on WhatsApp or by email and our team answers you directly.</p>
      <ul class="channels">
        <li class="ch"><span class="lbl">WhatsApp</span><span class="val js-wa">+212 659 288 638</span>
          <span class="acts"><a class="ibtn" id="waOpen" href="#" target="_blank" rel="noopener" aria-label="Open WhatsApp">{ICON_OUT}</a><button class="ibtn" type="button" data-copy="wa" aria-label="Copy">{ICON_COPY}<span class="tip" data-i="copied">Copied</span></button></span></li>
        <li class="ch"><span class="lbl">Email</span><span class="val js-mail">moroccoroyaltrips0@gmail.com</span>
          <span class="acts"><button class="ibtn" type="button" data-copy="mail" aria-label="Copy">{ICON_COPY}<span class="tip" data-i="copied">Copied</span></button></span></li>
        <li class="ch"><span class="lbl" data-i="ph">Phone</span><span class="val js-phone">+212 659 288 638</span>
          <span class="acts"><button class="ibtn" type="button" data-copy="phone" aria-label="Copy">{ICON_COPY}<span class="tip" data-i="copied">Copied</span></button></span></li>
      </ul>
      <div class="c-meta">
        <div><span data-i="mt1">Languages</span><b>EN · ES · FR · IT</b></div>
        <div><span data-i="mt2">Follow us</span><b><a href="https://www.instagram.com/morocco_royal_trips/" target="_blank" rel="noopener">Instagram</a> · <a href="https://www.facebook.com/share/1KHcsaf3p6/" target="_blank" rel="noopener">Facebook</a></b></div>
      </div>
    </aside>

    <div class="c-form-wrap reveal">
      <form class="c-form" id="cform" novalidate>
        <div class="f-head full"><h3 data-i="cf_h">Design your <em>trip</em></h3><p data-i="cf_p">A few details and we reply with ideas and a free quote.</p></div>
        <div class="fld full"><label for="f-name" data-i="f1">Full name</label><input id="f-name" required autocomplete="name"><i class="bar"></i></div>
        <div class="fld"><label for="f-email" data-i="f2">Email</label><input id="f-email" type="email" required autocomplete="email"><i class="bar"></i></div>
        <div class="fld"><label for="f-wa" data-i="fwa">WhatsApp number</label><input id="f-wa" type="tel" inputmode="tel" autocomplete="tel" placeholder="+44 7700 900000"><i class="bar"></i></div>
        <div class="fld"><label for="f-date" data-i="f5">Arrival date</label><input id="f-date" type="date"><i class="bar"></i></div>
        <div class="fld"><span class="lab" data-i="tv">Travellers</span><div class="stepper" data-step="ad"><button type="button" data-d="-1" aria-label="Fewer travellers">−</button><output id="v-ad">2</output><button type="button" data-d="1" aria-label="More travellers">+</button></div></div>
        <div class="fld full"><label for="f-msg" data-i="f11">Your message</label><textarea id="f-msg" data-ph="f11p" placeholder="Where would you like to go?"></textarea><i class="bar"></i></div>
        <div class="f-foot full"><button class="btn gold" type="submit"><span data-i="f13">Send my request</span><svg><use href="#i-arrow"/></svg></button><small data-i="f12">Opens in WhatsApp, ready to send.</small></div>
        <div class="sent" id="sent" hidden>
          <div class="ok"><svg viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
          <h3 data-i="ok_h">Your request is ready</h3>
          <p data-i="ok_p">Send it to our team on WhatsApp, or copy it and send it by email.</p>
          <div class="row"><a class="btn gold" id="sendWa" href="#" target="_blank" rel="noopener"><svg><use href="#i-wa"/></svg><span data-i="ok_b1">Send on WhatsApp</span></a><button class="btn ghost" type="button" id="copyMsg"><span data-i="ok_b2">Copy message</span></button></div>
          <button class="again" type="button" id="again" data-i="ok_b3">Edit my request</button>
        </div>
      </form>
    </div>
  </div>
</section>

<section class="hw" aria-labelledby="hwT">
  <div class="in">
    <div class="hw-hd">
      <span class="eyebrow" data-i="hw_e">How it works</span>
      <h2 id="hwT" data-i="hw_h">Three simple steps to your <em>journey</em></h2>
    </div>
    <ol class="hw-list">
      <li class="hw-route" aria-hidden="true"></li>
      <li class="hw-st"><div class="hw-ic"><b>01</b><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 3 10.5 13.5"/><path d="M21 3l-6.5 18-4-7.5L3 9.5z"/></svg></div><div><h3 data-i="hw1t">Send your request</h3><p data-i="hw1p">Fill in the form or write to us on WhatsApp with your dates and ideas.</p></div></li>
      <li class="hw-st"><div class="hw-ic"><b>02</b><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M9 4 3 6v14l6-2 6 2 6-2V4l-6 2z"/><path d="M9 4v14M15 6v14"/></svg></div><div><h3 data-i="hw2t">Receive your itinerary</h3><p data-i="hw2p">We reply personally with a tailor-made itinerary and a free quote, and adjust it until it feels right.</p></div></li>
      <li class="hw-st pay"><div class="hw-ic"><b>03</b><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="m8 12.5 2.6 2.6L16.5 9"/></svg></div><div><h3 data-i="hw3t">Confirm and travel</h3><p data-i="hw3p">A deposit confirms your trip and the balance is paid on arrival in Morocco.</p></div></li>
    </ol>
  </div>
</section>

<footer class="foot">
  <div class="in">
    <div class="fb"><img src="{{{{EMBLEM}}}}" alt=""><span>© <span id="yr">2026</span> <span data-brand="full">MoroccoRoyalTrips</span></span></div>
    <nav><a href="index.html" data-i="m0">Home</a><a href="index.html#tours" data-i="m1">Tours</a><a href="about.html" data-i="m4">About Us</a><a href="contact.html" data-i="m6">Contact</a></nav>
  </div>
</footer>
</main>'''

T = {
'en':dict(fwa="WhatsApp number",mtv='Travellers',tv='Travellers',c_t="Let's plan your <em>journey</em>",c_p="Tell us how you imagine your trip. We answer personally with ideas, a clear itinerary and a free quote.",
 ci_e="Get in touch",ci_h="Talk to a <em>real person</em>",ci_p="No call centre and no robots. Write to us on WhatsApp or by email and our team answers you directly.",
 ph="Phone",copied="Copied",mt1="Languages",mt2="Follow us",cf_e="Trip request",cf_h="Design your <em>trip</em>",cf_p="A few details and we reply with ideas and a free quote.",
 f1="Full name",f2="Email",f3="WhatsApp (optional)",f4="Country",f5="Arrival date",f6="Number of days",f7="Adults",f8="Children",f9="What interests you?",f10="Accommodation",f11="Your message",
 f11p="Where would you like to go?",f12="Opens in WhatsApp, ready to send.",f13="Send my request",
 i1="Sahara desert",i2="Imperial cities",i3="Day trips",i4="Merzouga activities",i5="Agafay activities",i6="Honeymoon",i7="Family trip",s1="Comfort",s2="Charming riads",s3="Luxury",
 ok_h="Your request is ready",ok_p="Send it to our team on WhatsApp, or copy it and send it by email.",ok_b1="Send on WhatsApp",ok_b2="Copy message",ok_b3="Edit my request",okc="Message copied",
 err="Please add your name and a valid email.",
 mh="Hello MoroccoRoyalTrips! I would like to plan a trip.",mn="Name",me="Email",mw="WhatsApp",mc="Country",mar="Arrival",mdy="Days",mad="Adults",mch="Children",mi="Interests",ms="Accommodation",mm="Message"),
'es':dict(fwa="Número de WhatsApp",mtv='Viajeros',tv='Viajeros',c_t="Planeemos tu <em>viaje</em>",c_p="Cuéntanos cómo imaginas tu viaje. Te respondemos personalmente con ideas, un itinerario claro y un presupuesto gratuito.",
 ci_e="Contacto",ci_h="Habla con una <em>persona real</em>",ci_p="Sin centralitas ni robots. Escríbenos por WhatsApp o por email y nuestro equipo te responde directamente.",
 ph="Teléfono",copied="Copiado",mt1="Idiomas",mt2="Síguenos",cf_e="Solicitud de viaje",cf_h="Diseña tu <em>viaje</em>",cf_p="Unos pocos datos y te respondemos con ideas y un presupuesto gratis.",
 f1="Nombre completo",f2="Email",f3="WhatsApp (opcional)",f4="País",f5="Fecha de llegada",f6="Número de días",f7="Adultos",f8="Niños",f9="¿Qué te interesa?",f10="Alojamiento",f11="Tu mensaje",
 f11p="¿Adónde te gustaría ir?",f12="Se abre en WhatsApp, listo para enviar.",f13="Enviar mi solicitud",
 i1="Desierto del Sáhara",i2="Ciudades imperiales",i3="Excursiones",i4="Actividades en Merzouga",i5="Actividades en Agafay",i6="Luna de miel",i7="Viaje en familia",s1="Confort",s2="Riads con encanto",s3="Lujo",
 ok_h="Tu solicitud está lista",ok_p="Envíala a nuestro equipo por WhatsApp, o cópiala y envíala por email.",ok_b1="Enviar por WhatsApp",ok_b2="Copiar mensaje",ok_b3="Editar mi solicitud",okc="Mensaje copiado",
 err="Añade tu nombre y un email válido.",
 mh="¡Hola MoroccoRoyalTrips! Me gustaría organizar un viaje.",mn="Nombre",me="Email",mw="WhatsApp",mc="País",mar="Llegada",mdy="Días",mad="Adultos",mch="Niños",mi="Intereses",ms="Alojamiento",mm="Mensaje"),
'fr':dict(fwa="Numéro WhatsApp",mtv='Voyageurs',tv='Voyageurs',c_t="Organisons votre <em>voyage</em>",c_p="Dites-nous comment vous imaginez votre voyage. Nous répondons personnellement avec des idées, un itinéraire clair et un devis gratuit.",
 ci_e="Contact",ci_h="Parlez à une <em>vraie personne</em>",ci_p="Pas de centre d’appels ni de robots. Écrivez-nous sur WhatsApp ou par email et notre équipe vous répond directement.",
 ph="Téléphone",copied="Copié",mt1="Langues",mt2="Suivez-nous",cf_e="Demande de voyage",cf_h="Créez votre <em>voyage</em>",cf_p="Quelques détails et nous vous répondons avec des idées et un devis gratuit.",
 f1="Nom complet",f2="Email",f3="WhatsApp (facultatif)",f4="Pays",f5="Date d’arrivée",f6="Nombre de jours",f7="Adultes",f8="Enfants",f9="Qu’est-ce qui vous intéresse ?",f10="Hébergement",f11="Votre message",
 f11p="Où aimeriez-vous aller ?",f12="S’ouvre dans WhatsApp, prêt à envoyer.",f13="Envoyer ma demande",
 i1="Désert du Sahara",i2="Villes impériales",i3="Excursions",i4="Activités à Merzouga",i5="Activités à Agafay",i6="Lune de miel",i7="Voyage en famille",s1="Confort",s2="Riads de charme",s3="Luxe",
 ok_h="Votre demande est prête",ok_p="Envoyez-la à notre équipe sur WhatsApp, ou copiez-la pour l’envoyer par email.",ok_b1="Envoyer sur WhatsApp",ok_b2="Copier le message",ok_b3="Modifier ma demande",okc="Message copié",
 err="Indiquez votre nom et un email valide.",
 mh="Bonjour MoroccoRoyalTrips ! Je souhaite organiser un voyage.",mn="Nom",me="Email",mw="WhatsApp",mc="Pays",mar="Arrivée",mdy="Jours",mad="Adultes",mch="Enfants",mi="Centres d’intérêt",ms="Hébergement",mm="Message"),
'it':dict(fwa="Numero WhatsApp",mtv='Viaggiatori',tv='Viaggiatori',c_t="Organizziamo il tuo <em>viaggio</em>",c_p="Raccontaci come immagini il tuo viaggio. Ti rispondiamo di persona con idee, un itinerario chiaro e un preventivo gratuito.",
 ci_e="Contatti",ci_h="Parla con una <em>persona vera</em>",ci_p="Niente call center e niente robot. Scrivici su WhatsApp o via email e il nostro team ti risponde direttamente.",
 ph="Telefono",copied="Copiato",mt1="Lingue",mt2="Seguici",cf_e="Richiesta di viaggio",cf_h="Crea il tuo <em>viaggio</em>",cf_p="Pochi dettagli e ti rispondiamo con idee e un preventivo gratuito.",
 f1="Nome e cognome",f2="Email",f3="WhatsApp (facoltativo)",f4="Paese",f5="Data di arrivo",f6="Numero di giorni",f7="Adulti",f8="Bambini",f9="Cosa ti interessa?",f10="Sistemazione",f11="Il tuo messaggio",
 f11p="Dove ti piacerebbe andare?",f12="Si apre su WhatsApp, pronto da inviare.",f13="Invia la richiesta",
 i1="Deserto del Sahara",i2="Città imperiali",i3="Escursioni",i4="Attività a Merzouga",i5="Attività ad Agafay",i6="Luna di miele",i7="Viaggio in famiglia",s1="Comfort",s2="Riad di charme",s3="Lusso",
 ok_h="La tua richiesta è pronta",ok_p="Inviala al nostro team su WhatsApp, oppure copiala e inviala via email.",ok_b1="Invia su WhatsApp",ok_b2="Copia il messaggio",ok_b3="Modifica la richiesta",okc="Messaggio copiato",
 err="Inserisci il tuo nome e un’email valida.",
 mh="Ciao MoroccoRoyalTrips! Vorrei organizzare un viaggio.",mn="Nome",me="Email",mw="WhatsApp",mc="Paese",mar="Arrivo",mdy="Giorni",mad="Adulti",mch="Bambini",mi="Interessi",ms="Sistemazione",mm="Messaggio"),
}

JS = '''/* ===== CONTACT PAGE ===== */
const CONTACT_PAGE={email:"moroccoroyaltrips0@gmail.com",phone:CONTACT.whatsapp};
document.querySelectorAll('.js-wa').forEach(e=>e.textContent=CONTACT.whatsapp);
document.querySelectorAll('.js-phone').forEach(e=>e.textContent=CONTACT_PAGE.phone);
document.querySelectorAll('.js-mail').forEach(e=>e.textContent=CONTACT_PAGE.email);
document.getElementById('waOpen').href='https://wa.me/'+WA;
document.querySelectorAll('#yr,.ft-yr').forEach(function(e){e.textContent=new Date().getFullYear()});

function copyText(text,el){
  const ok=()=>{if(!el)return;el.classList.add('done');setTimeout(()=>el.classList.remove('done'),1600)};
  const fallback=()=>{const t=document.createElement('textarea');t.value=text;document.body.appendChild(t);t.select();try{document.execCommand('copy')}catch(e){}t.remove();ok()};
  try{navigator.clipboard.writeText(text).then(ok,fallback)}catch(e){fallback()}
}
document.querySelectorAll('[data-copy]').forEach(b=>b.addEventListener('click',()=>{
  const v={wa:CONTACT.whatsapp,mail:CONTACT_PAGE.email,phone:CONTACT_PAGE.phone}[b.dataset.copy];copyText(v,b);
}));

const cnt={ad:2};
document.querySelectorAll('.stepper').forEach(st=>st.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>{
  const k=st.dataset.step;cnt[k]=Math.min(40,Math.max(1,cnt[k]+ +b.dataset.d));document.getElementById('v-'+k).textContent=cnt[k];
})));

const form=document.getElementById('cform'),sent=document.getElementById('sent');
let lastMsg="";
function buildMsg(){
  const t=T[LANG],v=id=>document.getElementById(id).value.trim();
  return [t.mh," ",t.mn+": "+v('f-name'),t.me+": "+v('f-email'),v('f-wa')?t.mw+": "+v('f-wa'):null,t.mar+": "+(v('f-date')||"-"),t.mtv+": "+cnt.ad,
    v('f-msg')?"\\n"+t.mm+": "+v('f-msg'):null].filter(Boolean).join("\\n");
}
form.addEventListener('submit',e=>{
  e.preventDefault();
  const n=document.getElementById('f-name'),m=document.getElementById('f-email');
  if(!n.value.trim()||!m.checkValidity()||!m.value.trim()){(n.value.trim()?m:n).focus();n.reportValidity&&(!n.value.trim()?n.reportValidity():m.reportValidity());return}
  lastMsg=buildMsg();
  document.getElementById('sendWa').href='https://wa.me/'+WA+'?text='+encodeURIComponent(lastMsg);
  [...form.children].forEach(c=>{if(c!==sent)c.hidden=true});
  sent.hidden=false;form.scrollIntoView({behavior:reduce?'auto':'smooth',block:'center'});
});
document.getElementById('copyMsg').addEventListener('click',e=>{copyText(lastMsg);e.currentTarget.querySelector('span').textContent=T[LANG].okc});
document.getElementById('again').addEventListener('click',()=>{[...form.children].forEach(c=>c.hidden=false);sent.hidden=true;document.getElementById('copyMsg').querySelector('span').textContent=T[LANG].ok_b2});

'''

# how-it-works strings
_HW={"en": {"hw_e": "How it works", "hw_h": "Three simple steps to your <em>journey</em>", "hw1t": "Send your request", "hw1p": "Fill in the form or write to us on WhatsApp with your dates and ideas.", "hw2t": "Receive your itinerary", "hw2p": "We reply personally with a tailor-made itinerary and a free quote, and adjust it until it feels right.", "hw3t": "Confirm and travel", "hw3p": "A deposit confirms your trip and the balance is paid on arrival in Morocco."}, "es": {"hw_e": "Cómo funciona", "hw_h": "Tres pasos sencillos hacia tu <em>viaje</em>", "hw1t": "Envía tu solicitud", "hw1p": "Rellena el formulario o escríbenos por WhatsApp con tus fechas e ideas.", "hw2t": "Recibe tu itinerario", "hw2p": "Te respondemos personalmente con un itinerario a medida y un presupuesto gratuito, y lo ajustamos hasta que te encaje.", "hw3t": "Confirma y viaja", "hw3p": "Un depósito confirma tu viaje y el resto se paga a la llegada a Marruecos."}, "fr": {"hw_e": "Comment ça marche", "hw_h": "Trois étapes simples vers votre <em>voyage</em>", "hw1t": "Envoyez votre demande", "hw1p": "Remplissez le formulaire ou écrivez-nous sur WhatsApp avec vos dates et vos idées.", "hw2t": "Recevez votre itinéraire", "hw2p": "Nous vous répondons personnellement avec un itinéraire sur mesure et un devis gratuit, ajusté jusqu’à ce qu’il vous convienne.", "hw3t": "Confirmez et partez", "hw3p": "Un acompte confirme votre voyage et le solde se règle à votre arrivée au Maroc."}, "it": {"hw_e": "Come funziona", "hw_h": "Tre semplici passi verso il tuo <em>viaggio</em>", "hw1t": "Invia la tua richiesta", "hw1p": "Compila il modulo o scrivici su WhatsApp con le tue date e le tue idee.", "hw2t": "Ricevi il tuo itinerario", "hw2p": "Ti rispondiamo personalmente con un itinerario su misura e un preventivo gratuito, e lo adattiamo finché non ti convince.", "hw3t": "Conferma e parti", "hw3p": "Un acconto conferma il viaggio e il saldo si paga all’arrivo in Marocco."}}
for _l,_d in _HW.items():
    if _l in T: T[_l].update(_d)
