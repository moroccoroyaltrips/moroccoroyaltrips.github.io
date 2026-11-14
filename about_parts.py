STAR='<path d="M12 2l2.9 5.1L20 4l-3.1 5.1L22 12l-5.1 2.9L20 20l-5.1-3.1L12 22l-2.9-5.1L4 20l3.1-5.1L2 12l5.1-2.9L4 4l5.1 3.1z" fill="currentColor"/>'

def ic(p): return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">{p}</svg>'
ICONS=[
 ic('<path d="M12 3l8 4v5c0 5-3.5 8-8 9-4.5-1-8-4-8-9V7z"/><path d="M9 12l2 2 4-4"/>'),
 ic('<circle cx="12" cy="10" r="3"/><path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/>'),
 ic('<path d="M4 20h16"/><path d="M6 16l3-9 3 5 3-3 3 7"/>'),
 ic('<path d="M12 3v18"/><path d="M17 7.5c0-1.9-2.2-3-5-3s-5 1.1-5 3 2.2 2.7 5 3.4 5 1.5 5 3.5-2.2 3.1-5 3.1-5-1.2-5-3.1"/>'),
 ic('<path d="M3 12h3l2-6 4 12 2-6h7"/>'),
 ic('<path d="M12 21c5-2 8-6 8-11-4 0-6 1-8 3-2-2-4-3-8-3 0 5 3 9 8 11z"/><path d="M12 13v8"/>'),
]

CSS = '''
/* ===== pillars v2: travel-journal style ===== */
.pillars.pj{background:#f5efe4;color:#16213d;padding-block:110px;position:relative;overflow:hidden}
.pillars.pj h2{color:#16213d}.pillars.pj h2 em{color:#b0843f}.pillars.pj .eyebrow{color:#9a7433;text-shadow:none}
.pj-wrap{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:clamp(40px,6vw,96px);align-items:start}
.pj-side{position:sticky;top:110px}
.pj-lead{margin:18px 0 0;max-width:44ch;font-size:16.5px;line-height:1.8;color:#4a536d}
.pj-photos{position:relative;height:360px;margin-top:44px}
.pj-ph{position:absolute;margin:0;background:#fff;padding:10px 10px 40px;box-shadow:0 22px 44px rgba(22,33,61,.16);transition:transform .6s cubic-bezier(.2,.8,.2,1)}
.pj-ph img{display:block;width:100%;height:100%;object-fit:cover}
.pj-ph.a{left:0;top:10px;width:62%;height:250px;transform:rotate(-4deg)}
.pj-ph.b{right:4%;top:90px;width:52%;height:240px;transform:rotate(5deg)}
.pj-ph figcaption{position:absolute;left:12px;right:12px;bottom:6px;font-family:"Great Vibes",cursive;font-size:20px;line-height:1.2;color:#6a5a3c;text-align:center;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.pj-photos:hover .pj-ph.a{transform:rotate(-6deg) translate(-6px,-6px)}.pj-photos:hover .pj-ph.b{transform:rotate(7deg) translate(6px,4px)}
.pj-stamp{position:absolute;left:44%;top:-6px;width:108px;height:108px;color:#b0843f;z-index:2;background:#f5efe4;border-radius:50%}
.pj-ring{transform-origin:60px 60px;animation:pjspin 26s linear infinite}@keyframes pjspin{to{transform:rotate(360deg)}}
.pj-stamp text{font:500 9px var(--body,Jost),sans-serif;letter-spacing:.16em;text-transform:uppercase;fill:#9a7433}
.pj-stamp .pj-st-n{font-family:var(--display);font-size:34px;letter-spacing:0;fill:#16213d}
.pj-list{list-style:none;margin:0;padding:0;border-top:1px solid rgba(22,33,61,.14)}
.pj-i{display:grid;grid-template-columns:96px 1fr;gap:22px;padding:30px 0 32px;border-bottom:1px solid rgba(22,33,61,.14);position:relative;transition:padding .5s cubic-bezier(.2,.8,.2,1)}
.pj-i::before{content:"";position:absolute;left:0;bottom:-1px;height:2px;width:0;background:#c9a05a;transition:width .7s cubic-bezier(.2,.8,.2,1)}
.pj-i:hover{padding-left:14px}.pj-i:hover::before{width:100%}
.pj-n{font-family:var(--display);font-size:62px;line-height:.9;color:transparent;-webkit-text-stroke:1.4px #b0843f;transition:color .5s}
.pj-i:hover .pj-n{color:#c9a05a}
.pj-i h3{margin:4px 0 10px;font-family:var(--display);font-weight:400;font-size:clamp(22px,2vw,28px);line-height:1.1;text-transform:uppercase;color:#16213d}
.pj-i p{margin:0;max-width:58ch;font-size:16px;line-height:1.8;color:#4a536d}
@media(max-width:1000px){.pj-wrap{grid-template-columns:1fr}.pj-side{position:static}.pj-photos{height:320px;max-width:520px}}
@media(max-width:640px){.pillars.pj{padding-block:76px}.pj-i{grid-template-columns:62px 1fr;gap:14px;padding:24px 0}.pj-n{font-size:44px}.pj-photos{height:280px}.pj-ph.a{height:200px}.pj-ph.b{height:190px;top:80px}.pj-stamp{width:86px;height:86px}}
@media(prefers-reduced-motion:reduce){.pj-ring{animation:none}}

/* ================= ABOUT PAGE ================= */
.hero.hero-sm{min-height:clamp(520px,74vh,800px)}
.hero-sm .hero-shade{background:linear-gradient(180deg,rgba(0,0,0,.5) 0%,rgba(0,0,0,0) 30%),linear-gradient(0deg,rgba(0,0,0,.75) 0%,rgba(0,0,0,0) 58%)}
.hero-sm .hero-in{justify-content:flex-end;padding-block:160px 76px}
.hero-sm .hero-bg{object-position:50% 60%}
.crumbs{display:flex;gap:10px;align-items:center;font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:rgba(255,255,255,.75);text-shadow:0 1px 8px rgba(0,0,0,.6)}
.crumbs a:hover{color:var(--gold-hi)}
.crumbs svg{width:10px;height:10px;transform:rotate(-90deg)}

.ab{background:#f5efe4;color:#16213d}
.ab .eyebrow{color:#9a7433}
.ab .eyebrow::before{animation:none}
.ab h2{font-size:clamp(36px,4.4vw,60px);line-height:1;margin:14px 0 0}
.ab h2 em{color:#b0843f}
.ab-p{font-size:17px;line-height:1.8;color:#4a536d;margin:0}

.story{display:grid;grid-template-columns:1.05fr .95fr;gap:72px;align-items:center;padding-block:120px 100px}
.story-txt{display:grid;gap:20px}
.story-txt .sig{font-family:var(--display);font-size:20px;color:#b0843f;margin-top:6px}
.story-img{position:relative;aspect-ratio:4/5}
.story-img img{position:absolute;object-fit:cover;border-radius:22px;box-shadow:0 30px 60px rgba(22,33,61,.18)}
.story-img .a{inset:0 18% 14% 0;width:82%;height:86%}
.story-img .b{right:0;bottom:0;width:48%;height:46%;border:8px solid #f5efe4}
.story-img .badge{position:absolute;left:-18px;bottom:8%;background:#16213d;color:#fff;border-radius:18px;padding:18px 22px;display:grid;gap:4px;max-width:230px;box-shadow:0 20px 40px rgba(22,33,61,.25)}
.story-img .badge b{font-family:var(--display);font-size:22px;color:var(--gold-hi)}
.story-img .badge span{font-size:13px;line-height:1.5;color:rgba(255,255,255,.8)}

.pillars{background:#16213d;color:#fff;padding-block:110px}
.pillars .eyebrow{color:var(--gold-hi)}
.pillars h2{color:#fff;font-size:clamp(36px,4.4vw,60px);line-height:1;margin:14px 0 0}
.promise h2 em{color:#b0843f}
.pillars h2 em{color:var(--gold-hi)}
.pl-head{display:flex;justify-content:space-between;align-items:flex-end;gap:30px;flex-wrap:wrap;margin-bottom:54px}
.pl-head p{max-width:46ch;color:rgba(255,255,255,.72);font-size:16px;line-height:1.75;margin:0}
.pl-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:rgba(233,205,142,.18);border:1px solid rgba(233,205,142,.18);border-radius:24px;overflow:hidden}
.pl-grid .pl{background:#16213d;padding:40px 34px;display:grid;gap:14px;align-content:start;transition:background .4s}
.pl-grid .pl:hover{background:#1b2a4d}
.pl-grid .pl svg{width:34px;height:34px;color:var(--gold-hi)}
.pl-grid .pl h3{font-family:var(--display);font-size:22px;letter-spacing:.02em;margin:6px 0 0;color:#fff}
.pl-grid .pl p{margin:0;font-size:15px;line-height:1.75;color:rgba(255,255,255,.7)}

.steps{padding-block:110px}
.st-head{max-width:720px;margin-bottom:56px;display:grid;gap:14px}
.st-list{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,1fr);gap:26px;counter-reset:s}
.st-list li{position:relative;padding:30px 26px 32px;background:#fffaf1;border:1px solid rgba(22,33,61,.08);border-radius:22px;display:grid;gap:12px;align-content:start}
.st-list li::before{counter-increment:s;content:"0" counter(s);font-family:var(--display);font-size:44px;line-height:1;color:#b0843f}
.st-list h3{font-family:var(--display);font-size:20px;margin:0;color:#16213d}
.st-list p{margin:0;font-size:15px;line-height:1.7;color:#4a536d}

.team{padding-block:0 110px}
.tm-box{display:grid;grid-template-columns:.9fr 1.1fr;gap:0;background:#fffaf1;border-radius:28px;overflow:hidden;border:1px solid rgba(22,33,61,.08)}
.tm-box img{width:100%;height:100%;object-fit:cover;min-height:420px}
.tm-txt{padding:60px 56px;display:grid;gap:18px;align-content:center}
.tm-list{list-style:none;margin:6px 0 0;padding:0;display:grid;gap:12px}
.tm-list li{display:flex;gap:12px;font-size:15.5px;line-height:1.6;color:#16213d}
.tm-list li::before{content:"";flex:none;width:8px;height:8px;margin-top:8px;border-radius:50%;background:#b0843f}

.regions{padding-block:0 110px}
.rg-head{display:grid;gap:14px;margin-bottom:40px;max-width:720px}
.rg-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}
.rg{border-top:2px solid #b0843f;padding-top:18px;display:grid;gap:8px}
.rg b{font-family:var(--display);font-size:20px;color:#16213d}
.rg span{font-size:14.5px;line-height:1.7;color:#4a536d}

.promise{background:#efe5d3;padding-block:100px}
.pr-grid{display:grid;grid-template-columns:.8fr 1.2fr;gap:64px;align-items:start}
.pr-list{list-style:none;margin:0;padding:0;border-top:1px solid rgba(22,33,61,.15)}
.pr-list li{display:grid;grid-template-columns:auto 1fr;gap:18px;padding:22px 0;border-bottom:1px solid rgba(22,33,61,.15)}
.pr-list i{font-style:normal;font-family:var(--display);color:#b0843f;font-size:15px;padding-top:3px}
.pr-list b{display:block;font-size:17px;color:#16213d;margin-bottom:4px}
.pr-list span{font-size:15px;line-height:1.7;color:#4a536d}

.ab-cta{position:relative;padding-block:110px;text-align:center;background:#0e0e0e;color:#fff;overflow:hidden}
.ab-cta img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.35}
.ab-cta .in{position:relative;display:grid;gap:20px;justify-items:center}
.ab-cta h2{color:#fff;font-size:clamp(36px,4.8vw,64px);line-height:1;margin:0}
.ab-cta h2 em{color:var(--gold-hi)}
.ab-cta p{max-width:52ch;margin:0;color:rgba(255,255,255,.82);font-size:17px;line-height:1.7}
.ab-cta .row{display:flex;gap:14px;flex-wrap:wrap;justify-content:center;margin-top:8px}

@media(max-width:1000px){
 .story,.pr-grid,.tm-box{grid-template-columns:1fr}
 .story{gap:48px;padding-block:90px 70px}
 .story-img{max-width:520px}
 .pl-grid{grid-template-columns:repeat(2,1fr)}
 .st-list,.rg-grid{grid-template-columns:repeat(2,1fr)}
 .tm-txt{padding:40px 30px}
 .tm-box img{min-height:300px;max-height:420px}
}
@media(max-width:620px){
 .pl-grid,.st-list,.rg-grid{grid-template-columns:1fr}
 .pl-grid .pl{padding:30px 24px}
 .story-img .badge{left:10px;max-width:200px;padding:14px 16px}
 .pillars,.steps,.promise,.ab-cta{padding-block:80px}
 .team,.regions{padding-block:0 80px}
}
'''

PILL=''.join(f'<li class="pj-i reveal"><span class="pj-n">0{i+1}</span><div><h3 data-i="ab_v{i+1}">x</h3><p data-i="ab_v{i+1}p">x</p></div></li>' for i in range(6))
STEPS=''.join(f'<li class="reveal"><h3 data-i="ab_s{i+1}">x</h3><p data-i="ab_s{i+1}p">x</p></li>' for i in range(4))
TEAM=''.join(f'<li data-i="ab_t{i+1}">x</li>' for i in range(5))
REG=''.join(f'<div class="rg reveal"><b data-i="ab_r{i+1}">x</b><span data-i="ab_r{i+1}p">x</span></div>' for i in range(8))
PROM=''.join(f'<li><i>0{i+1}</i><div><b data-i="ab_p{i+1}">x</b><span data-i="ab_p{i+1}p">x</span></div></li>' for i in range(6))

MAIN = f'''<main id="top">
<section class="hero hero-sm" id="hero">
  <div class="hero-media" id="heroMedia"><img class="hero-bg" src="{{{{IMG_caravan-dusk}}}}" alt="Camel caravan on the dunes at dusk"></div>
  <div class="hero-shade" aria-hidden="true"></div>
  <canvas id="dust" aria-hidden="true"></canvas>
  <div class="in hero-in">
    <div class="hero-copy">
      <nav class="crumbs rise" aria-label="Breadcrumb"><a href="index.html" data-i="m0">Home</a><svg><use href="#i-chev"/></svg><span data-i="m4">About Us</span></nav>
      <h1 id="heroTitle" data-i="ab_h">About <em>us</em></h1>
      <div class="khatam" aria-hidden="true"><span></span><svg viewBox="0 0 24 24">{STAR}</svg><span></span></div>
      <p class="lead rise d3" data-i="ab_l">x</p>
    </div>
  </div>
</section>

<section class="ab">
  <div class="in story">
    <div class="story-txt reveal">
      <span class="eyebrow" data-i="ab_se">Our story</span>
      <h2 data-i="ab_sh">x</h2>
      <p class="ab-p" data-i="ab_s_p1">x</p>
      <p class="ab-p" data-i="ab_s_p2">x</p>
      <p class="ab-p" data-i="ab_s_p3">x</p>
      <span class="sig" data-brand="full">MoroccoRoyalTrips</span>
    </div>
    <div class="story-img reveal">
      <img class="a" src="{{{{IMG_es-hero}}}}" alt="Blue fishing boats in the port of Essaouira" loading="lazy">
      <img class="b" src="{{{{IMG_erg-palm}}}}" alt="A palm tree among the dunes of Erg Chebbi" loading="lazy">
      <div class="badge"><b data-i="ab_bd">x</b><span data-i="ab_bdp">x</span></div>
    </div>
  </div>
</section>

<section class="pillars pj">
  <div class="in pj-wrap">
    <div class="pj-side">
      <div class="reveal"><span class="eyebrow" data-i="ab_ve">What makes us different</span><h2 data-i="ab_vh">x</h2><p class="pj-lead" data-i="ab_vp">x</p></div>
      <div class="pj-photos" aria-hidden="true">
        <figure class="pj-ph a"><img src="{{{{IMG_dune-friends}}}}" alt="" loading="lazy"></figure>
        <figure class="pj-ph b"><img src="{{{{IMG_chef-alley}}}}" alt="" loading="lazy"><figcaption data-i="ab_cap">x</figcaption></figure>
        <svg class="pj-stamp" viewBox="0 0 120 120"><defs><path id="pjc" d="M60 60m-44 0a44 44 0 1 1 88 0a44 44 0 1 1-88 0"/></defs><g class="pj-ring"><circle cx="60" cy="60" r="56" fill="none" stroke="currentColor" stroke-width="1.2" stroke-dasharray="3 4"/><text><textPath href="#pjc" data-i="ab_stamp">x</textPath></text></g><text class="pj-st-n" x="60" y="70" text-anchor="middle">8</text></svg>
      </div>
    </div>
    <ol class="pj-list">{PILL}</ol>
  </div>
</section>

<section class="ab steps">
  <div class="in">
    <div class="st-head reveal"><span class="eyebrow" data-i="ab_se2">How we work</span><h2 data-i="ab_sh2">x</h2><p class="ab-p" data-i="ab_sp2">x</p></div>
    <ol class="st-list">{STEPS}</ol>
  </div>
</section>

<section class="ab team">
  <div class="in">
    <div class="tm-box reveal">
      <img src="{{{{IMG_lx-camp}}}}" alt="Tents of a desert camp at sunset" loading="lazy">
      <div class="tm-txt"><span class="eyebrow" data-i="ab_te">Our team</span><h2 data-i="ab_th">x</h2><p class="ab-p" data-i="ab_tp">x</p><ul class="tm-list">{TEAM}</ul></div>
    </div>
  </div>
</section>

<section class="ab regions">
  <div class="in">
    <div class="rg-head reveal"><span class="eyebrow" data-i="ab_re">Where we travel</span><h2 data-i="ab_rh">x</h2><p class="ab-p" data-i="ab_rp">x</p></div>
    <div class="rg-grid">{REG}</div>
  </div>
</section>

<section class="promise">
  <div class="in pr-grid">
    <div class="reveal"><span class="eyebrow" style="color:#9a7433" data-i="ab_pe">Our promise</span><h2 style="font-size:clamp(36px,4.4vw,60px);line-height:1;margin:14px 0 18px;color:#16213d" data-i="ab_ph">x</h2><p class="ab-p" style="color:#4a536d;font-size:17px;line-height:1.8;margin:0" data-i="ab_pp">x</p></div>
    <ul class="pr-list reveal">{PROM}</ul>
  </div>
</section>

<section class="ab-cta">
  <img src="{{{{IMG_camel-sunset}}}}" alt="" loading="lazy">
  <div class="in">
    <span class="eyebrow" style="color:var(--gold-hi)" data-i="ab_ce">Ready when you are</span>
    <h2 data-i="ab_ch">x</h2>
    <p data-i="ab_cp">x</p>
    <div class="row"><a class="btn gold" href="contact.html"><span data-i="ab_cb1">Plan my trip</span><svg><use href="#i-arrow"/></svg></a><a class="btn ghost" href="index.html#tours"><span data-i="ab_cb2">See our tours</span></a></div>
  </div>
</section>

<footer class="foot">
  <div class="in">
    <div class="fb"><img src="{{{{EMBLEM}}}}" alt=""><span>© <span id="yr">2026</span> <span data-brand="full">MoroccoRoyalTrips</span></span></div>
    <nav><a href="index.html" data-i="m0">Home</a><a href="index.html#tours" data-i="m1">Tours</a><a href="about.html" data-i="m4">About Us</a><a href="contact.html" data-i="m6">Contact</a></nav>
  </div>
</footer>
</main>'''

T={
'en':dict(
 ab_h="About <em>us</em>",
 ab_l="A Moroccan travel company built on one simple idea: private journeys, designed with care by people who know the country from the inside.",
 ab_se="Our story",ab_sh="Morocco, the way we would show it to <em>a friend</em>",
 ab_s_p1="MoroccoRoyalTrips was born from 8 years on the roads of Morocco: early mornings in the medinas, long drives over the High Atlas, nights under the stars of the Sahara. Along the way we met travellers who wanted more than a fixed programme. They wanted time, comfort and someone they could trust.",
 ab_s_p2="So we built a company around private travel. No crowded buses and no rigid timetables: every trip is yours alone, with your own driver, your own pace and an itinerary shaped around what you love, whether that is food, history, photography, the desert or simply a quiet riad with a view.",
 ab_s_p3="We are a local team, and we work with local guides, family-run riads and desert camps we know personally. When you travel with us, you are not buying a product from a catalogue. You are being welcomed into our country.",
 ab_bd="8 years",ab_bdp="of experience on the roads of Morocco. Every tour is 100% private: only you, your companions and your driver-guide.",
 ab_cap="On the road with our travellers",ab_stamp="8 years · private tours · Morocco · ",ab_ve="What makes us different",ab_vh="Travel designed around <em>you</em>",
 ab_vp="Six principles guide every journey we plan, from a single day trip to a two-week grand tour of the kingdom.",
 ab_v1="Private by design",ab_v1p="Your own vehicle, your own driver-guide and your own schedule. You stop where you want, for as long as you want.",
 ab_v2="Local knowledge",ab_v2p="We live here. We know which road to take after the rain, which riad has the best terrace and when the light is perfect on the dunes.",
 ab_v3="Tailor-made itineraries",ab_v3p="Every programme on this site is a starting point. We adapt the route, the rhythm and the accommodation to your wishes.",
 ab_v4="Clear, honest pricing",ab_v4p="We tell you exactly what is included and what is not, before you book. No hidden costs and no surprises on the way.",
 ab_v5="Comfort and safety",ab_v5p="Modern air-conditioned vehicles, experienced drivers who know every bend of the mountain roads, and carefully chosen places to stay.",
 ab_v6="Respect for people and places",ab_v6p="We work with local families, cooperatives and guides, and we travel in a way that respects the communities and landscapes we visit.",
 ab_se2="How we work",ab_sh2="From first message to <em>last goodbye</em>",
 ab_sp2="Planning a trip to Morocco should be a pleasure, not a puzzle. Here is how we take care of it with you.",
 ab_s1="Tell us your idea",ab_s1p="Send us a message on WhatsApp or through our form: your dates, how many you are and what you dream of seeing.",
 ab_s2="Receive your proposal",ab_s2p="We reply personally with a clear day-by-day itinerary, the accommodation we recommend and a transparent quote.",
 ab_s3="Shape it together",ab_s3p="Change a night, add a city, slow down the pace. We adjust everything until the trip feels exactly right for you.",
 ab_s4="Travel with peace of mind",ab_s4p="Your driver meets you on arrival, and our team stays reachable on WhatsApp throughout your journey.",
 ab_te="Our team",ab_th="People who love <em>their country</em>",
 ab_tp="Behind every trip there is a small team of Moroccan travel professionals: planners who answer your messages, drivers who know every road, and local guides in the cities who bring history to life.",
 ab_t1="Driver-guides speaking English and Spanish, with French and Italian on request",
 ab_t2="Licensed local guides for the medinas of Fes, Marrakech and other cities",
 ab_t3="Trusted partners: family riads, kasbahs and desert camps we know personally",
 ab_t4="A planning team that answers you directly, before and during your trip",
 ab_t5="Experience with couples, families, friends, student groups and special interests",
 ab_re="Where we travel",ab_rh="The whole kingdom, <em>north to south</em>",
 ab_rp="Our tours start from the main gateways of Morocco and reach every region, from the Mediterranean to the edge of the Sahara.",
 ab_r1="Imperial cities",ab_r1p="Fes, Meknes, Rabat and Marrakech: medinas, palaces and centuries of history.",
 ab_r2="The north",ab_r2p="Tangier, the blue lanes of Chefchaouen and the Roman ruins of Volubilis.",
 ab_r3="The Sahara",ab_r3p="The dunes of Erg Chebbi in Merzouga and the wild sands of Erg Chigaga.",
 ab_r4="The Atlas Mountains",ab_r4p="The Tizi n’Tichka pass, Berber villages, the Ourika Valley and the Middle Atlas cedars.",
 ab_r5="Valleys and gorges",ab_r5p="The Dades and Todra gorges, the Rose Valley and the palm groves of the Draa.",
 ab_r6="Kasbahs of the south",ab_r6p="Ouarzazate, Ait Ben Haddou and the road of a thousand kasbahs.",
 ab_r7="The Atlantic coast",ab_r7p="Casablanca, Essaouira, Agadir and the surf village of Taghazout.",
 ab_r8="Day trips",ab_r8p="Agafay, Ouzoud, Essaouira, Ourika, the High Atlas and Moulay Yacoub.",
 ab_pe="Our promise",ab_ph="What you can <em>count on</em>",
 ab_pp="Whatever the length of your trip, these are the commitments we make to every traveller who chooses us.",
 ab_p1="A personal reply",ab_p1p="A real person reads your message and answers you, usually within the same day.",
 ab_p2="A free, no-obligation quote",ab_p2p="You receive a detailed proposal and price before deciding anything.",
 ab_p3="Transparency",ab_p3p="Inclusions, exclusions and optional extras are written clearly in every itinerary.",
 ab_p4="Flexibility",ab_p4p="Routes, timings and stops can be adapted, before and during the trip.",
 ab_p5="Carefully chosen stays",ab_p5p="Riads, hotels and camps selected for comfort, cleanliness and character.",
 ab_p6="Support on the road",ab_p6p="Our team stays reachable on WhatsApp from your arrival to your departure.",
 ab_ce="Ready when you are",ab_ch="Let’s design your <em>Morocco</em>",
 ab_cp="Tell us how you imagine your journey. We will reply with ideas, a clear itinerary and a free quote.",
 ab_cb1="Plan my trip",ab_cb2="See our tours"),
'es':dict(
 ab_h="Sobre <em>nosotros</em>",
 ab_l="Una agencia de viajes marroquí construida sobre una idea sencilla: viajes privados, diseñados con cuidado por personas que conocen el país desde dentro.",
 ab_se="Nuestra historia",ab_sh="Marruecos, como se lo enseñaríamos a <em>un amigo</em>",
 ab_s_p1="MoroccoRoyalTrips nació de 8 años en las carreteras de Marruecos: mañanas tempranas en las medinas, largos trayectos por el Alto Atlas, noches bajo las estrellas del Sáhara. Por el camino conocimos a viajeros que querían algo más que un programa cerrado. Querían tiempo, comodidad y alguien de confianza.",
 ab_s_p2="Así que creamos una agencia centrada en el viaje privado. Sin autobuses llenos ni horarios rígidos: cada viaje es solo tuyo, con tu propio conductor, tu propio ritmo y un itinerario pensado para lo que te gusta, ya sea la gastronomía, la historia, la fotografía, el desierto o simplemente un riad tranquilo con vistas.",
 ab_s_p3="Somos un equipo local y trabajamos con guías locales, riads familiares y campamentos que conocemos personalmente. Cuando viajas con nosotros no compras un producto de catálogo. Te recibimos en nuestro país.",
 ab_bd="8 años",ab_bdp="de experiencia en las carreteras de Marruecos. Todos los circuitos son 100% privados: solo tú, tus acompañantes y tu conductor-guía.",
 ab_cap="En ruta con nuestros viajeros",ab_stamp="8 años · viajes privados · Marruecos · ",ab_ve="Lo que nos hace diferentes",ab_vh="Viajes pensados para <em>ti</em>",
 ab_vp="Seis principios guían cada viaje que organizamos, desde una excursión de un día hasta un gran circuito de dos semanas por el reino.",
 ab_v1="Privado por definición",ab_v1p="Tu propio vehículo, tu propio conductor-guía y tu propio horario. Paras donde quieras y el tiempo que quieras.",
 ab_v2="Conocimiento local",ab_v2p="Vivimos aquí. Sabemos qué carretera tomar después de la lluvia, qué riad tiene la mejor terraza y cuándo la luz es perfecta en las dunas.",
 ab_v3="Itinerarios a medida",ab_v3p="Cada programa de esta web es un punto de partida. Adaptamos la ruta, el ritmo y el alojamiento a tus deseos.",
 ab_v4="Precios claros y honestos",ab_v4p="Te decimos exactamente qué está incluido y qué no antes de reservar. Sin costes ocultos ni sorpresas en el camino.",
 ab_v5="Comodidad y seguridad",ab_v5p="Vehículos modernos con aire acondicionado, conductores con experiencia que conocen cada curva de la montaña y alojamientos elegidos con cuidado.",
 ab_v6="Respeto por las personas y los lugares",ab_v6p="Trabajamos con familias, cooperativas y guías locales, y viajamos respetando las comunidades y los paisajes que visitamos.",
 ab_se2="Cómo trabajamos",ab_sh2="Del primer mensaje a la <em>última despedida</em>",
 ab_sp2="Organizar un viaje a Marruecos debe ser un placer, no un rompecabezas. Así lo hacemos contigo.",
 ab_s1="Cuéntanos tu idea",ab_s1p="Escríbenos por WhatsApp o por el formulario: tus fechas, cuántos sois y lo que sueñas ver.",
 ab_s2="Recibe tu propuesta",ab_s2p="Te respondemos personalmente con un itinerario claro día a día, los alojamientos que recomendamos y un presupuesto transparente.",
 ab_s3="Ajústalo con nosotros",ab_s3p="Cambia una noche, añade una ciudad, baja el ritmo. Lo ajustamos todo hasta que el viaje sea exactamente como quieres.",
 ab_s4="Viaja tranquilo",ab_s4p="Tu conductor te recibe a la llegada y nuestro equipo sigue disponible por WhatsApp durante todo el viaje.",
 ab_te="Nuestro equipo",ab_th="Personas que aman <em>su país</em>",
 ab_tp="Detrás de cada viaje hay un pequeño equipo de profesionales marroquíes: organizadores que responden a tus mensajes, conductores que conocen cada carretera y guías locales en las ciudades que dan vida a la historia.",
 ab_t1="Conductores-guía que hablan inglés y español, con francés e italiano bajo petición",
 ab_t2="Guías locales oficiales para las medinas de Fez, Marrakech y otras ciudades",
 ab_t3="Socios de confianza: riads familiares, kasbahs y campamentos que conocemos personalmente",
 ab_t4="Un equipo de organización que te responde directamente, antes y durante tu viaje",
 ab_t5="Experiencia con parejas, familias, amigos, grupos de estudiantes e intereses especiales",
 ab_re="Dónde viajamos",ab_rh="Todo el reino, <em>de norte a sur</em>",
 ab_rp="Nuestros circuitos salen de las principales puertas de entrada de Marruecos y llegan a todas las regiones, del Mediterráneo al borde del Sáhara.",
 ab_r1="Ciudades imperiales",ab_r1p="Fez, Mequinez, Rabat y Marrakech: medinas, palacios y siglos de historia.",
 ab_r2="El norte",ab_r2p="Tánger, las callejuelas azules de Chefchaouen y las ruinas romanas de Volubilis.",
 ab_r3="El Sáhara",ab_r3p="Las dunas del Erg Chebbi en Merzouga y las arenas salvajes del Erg Chigaga.",
 ab_r4="El Atlas",ab_r4p="El puerto del Tizi n’Tichka, los pueblos bereberes, el valle de Ourika y los cedros del Medio Atlas.",
 ab_r5="Valles y gargantas",ab_r5p="Las gargantas del Dades y del Todra, el valle de las Rosas y los palmerales del Draa.",
 ab_r6="Kasbahs del sur",ab_r6p="Ouarzazate, Ait Ben Haddou y la ruta de las mil kasbahs.",
 ab_r7="La costa atlántica",ab_r7p="Casablanca, Esauira, Agadir y el pueblo surfero de Taghazout.",
 ab_r8="Excursiones de un día",ab_r8p="Agafay, Ouzoud, Esauira, Ourika, el Alto Atlas y Moulay Yacoub.",
 ab_pe="Nuestro compromiso",ab_ph="Con lo que puedes <em>contar</em>",
 ab_pp="Sea cual sea la duración de tu viaje, estos son los compromisos que asumimos con cada viajero que nos elige.",
 ab_p1="Una respuesta personal",ab_p1p="Una persona real lee tu mensaje y te responde, normalmente el mismo día.",
 ab_p2="Presupuesto gratis y sin compromiso",ab_p2p="Recibes una propuesta detallada con precio antes de decidir nada.",
 ab_p3="Transparencia",ab_p3p="Lo incluido, lo no incluido y los extras opcionales están escritos con claridad en cada itinerario.",
 ab_p4="Flexibilidad",ab_p4p="Rutas, horarios y paradas pueden adaptarse antes y durante el viaje.",
 ab_p5="Alojamientos elegidos con cuidado",ab_p5p="Riads, hoteles y campamentos seleccionados por su comodidad, limpieza y carácter.",
 ab_p6="Apoyo durante el viaje",ab_p6p="Nuestro equipo está disponible por WhatsApp desde tu llegada hasta tu salida.",
 ab_ce="Cuando tú quieras",ab_ch="Diseñemos tu <em>Marruecos</em>",
 ab_cp="Cuéntanos cómo imaginas tu viaje. Te responderemos con ideas, un itinerario claro y un presupuesto gratuito.",
 ab_cb1="Planificar mi viaje",ab_cb2="Ver nuestros circuitos"),
'fr':dict(
 ab_h="À propos de <em>nous</em>",
 ab_l="Une agence de voyage marocaine fondée sur une idée simple : des voyages privés, conçus avec soin par des gens qui connaissent le pays de l’intérieur.",
 ab_se="Notre histoire",ab_sh="Le Maroc, comme nous le montrerions à <em>un ami</em>",
 ab_s_p1="MoroccoRoyalTrips est née de 8 années sur les routes du Maroc : petits matins dans les médinas, longues traversées du Haut Atlas, nuits sous les étoiles du Sahara. En chemin, nous avons rencontré des voyageurs qui voulaient plus qu’un programme figé. Ils voulaient du temps, du confort et quelqu’un de confiance.",
 ab_s_p2="Nous avons donc créé une agence entièrement tournée vers le voyage privé. Pas de bus bondés ni d’horaires rigides : chaque voyage est le vôtre, avec votre propre chauffeur, votre propre rythme et un itinéraire construit autour de ce que vous aimez, la gastronomie, l’histoire, la photographie, le désert ou simplement un riad paisible avec vue.",
 ab_s_p3="Nous sommes une équipe locale, et nous travaillons avec des guides locaux, des riads familiaux et des camps que nous connaissons personnellement. Voyager avec nous, ce n’est pas acheter un produit sur catalogue. C’est être accueilli dans notre pays.",
 ab_bd="8 ans",ab_bdp="d’expérience sur les routes du Maroc. Tous nos circuits sont 100 % privés : vous, vos compagnons de voyage et votre chauffeur-guide.",
 ab_cap="Sur la route avec nos voyageurs",ab_stamp="8 ans · voyages privés · Maroc · ",ab_ve="Ce qui nous distingue",ab_vh="Des voyages pensés pour <em>vous</em>",
 ab_vp="Six principes guident chaque voyage que nous organisons, d’une simple excursion d’une journée à un grand tour du royaume de deux semaines.",
 ab_v1="Privé par nature",ab_v1p="Votre véhicule, votre chauffeur-guide et votre propre emploi du temps. Vous vous arrêtez où vous voulez, aussi longtemps que vous voulez.",
 ab_v2="Connaissance du terrain",ab_v2p="Nous vivons ici. Nous savons quelle route prendre après la pluie, quel riad a la plus belle terrasse et quand la lumière est parfaite sur les dunes.",
 ab_v3="Itinéraires sur mesure",ab_v3p="Chaque programme de ce site est un point de départ. Nous adaptons la route, le rythme et l’hébergement à vos envies.",
 ab_v4="Des prix clairs et honnêtes",ab_v4p="Nous vous disons exactement ce qui est inclus et ce qui ne l’est pas, avant la réservation. Pas de frais cachés ni de surprises en route.",
 ab_v5="Confort et sécurité",ab_v5p="Véhicules modernes climatisés, chauffeurs expérimentés qui connaissent chaque virage des routes de montagne, et hébergements choisis avec soin.",
 ab_v6="Respect des gens et des lieux",ab_v6p="Nous travaillons avec des familles, des coopératives et des guides locaux, et nous voyageons dans le respect des communautés et des paysages.",
 ab_se2="Notre méthode",ab_sh2="Du premier message au <em>dernier au revoir</em>",
 ab_sp2="Préparer un voyage au Maroc doit être un plaisir, pas un casse-tête. Voici comment nous nous en occupons avec vous.",
 ab_s1="Partagez votre idée",ab_s1p="Écrivez-nous sur WhatsApp ou via le formulaire : vos dates, le nombre de voyageurs et ce que vous rêvez de voir.",
 ab_s2="Recevez votre proposition",ab_s2p="Nous répondons personnellement avec un itinéraire clair jour par jour, les hébergements recommandés et un devis transparent.",
 ab_s3="Ajustez-la avec nous",ab_s3p="Changez une nuit, ajoutez une ville, ralentissez le rythme. Nous ajustons tout jusqu’à ce que le voyage vous ressemble.",
 ab_s4="Voyagez l’esprit tranquille",ab_s4p="Votre chauffeur vous accueille à l’arrivée, et notre équipe reste joignable sur WhatsApp pendant tout le voyage.",
 ab_te="Notre équipe",ab_th="Des passionnés de <em>leur pays</em>",
 ab_tp="Derrière chaque voyage, il y a une petite équipe de professionnels marocains : des conseillers qui répondent à vos messages, des chauffeurs qui connaissent chaque route et des guides locaux qui font vivre l’histoire des villes.",
 ab_t1="Chauffeurs-guides parlant anglais et espagnol, français et italien sur demande",
 ab_t2="Guides locaux officiels pour les médinas de Fès, Marrakech et d’autres villes",
 ab_t3="Des partenaires de confiance : riads familiaux, kasbahs et camps que nous connaissons personnellement",
 ab_t4="Une équipe d’organisation qui vous répond directement, avant et pendant le voyage",
 ab_t5="L’expérience des couples, des familles, des amis, des groupes d’étudiants et des voyages thématiques",
 ab_re="Où nous voyageons",ab_rh="Tout le royaume, <em>du nord au sud</em>",
 ab_rp="Nos circuits partent des principales portes d’entrée du Maroc et rejoignent toutes les régions, de la Méditerranée aux portes du Sahara.",
 ab_r1="Villes impériales",ab_r1p="Fès, Meknès, Rabat et Marrakech : médinas, palais et des siècles d’histoire.",
 ab_r2="Le nord",ab_r2p="Tanger, les ruelles bleues de Chefchaouen et les ruines romaines de Volubilis.",
 ab_r3="Le Sahara",ab_r3p="Les dunes de l’Erg Chebbi à Merzouga et les sables sauvages de l’Erg Chigaga.",
 ab_r4="L’Atlas",ab_r4p="Le col du Tizi n’Tichka, les villages berbères, la vallée de l’Ourika et les cèdres du Moyen Atlas.",
 ab_r5="Vallées et gorges",ab_r5p="Les gorges du Dadès et du Todra, la vallée des Roses et les palmeraies du Drâa.",
 ab_r6="Kasbahs du Sud",ab_r6p="Ouarzazate, Aït Ben Haddou et la route des mille kasbahs.",
 ab_r7="La côte atlantique",ab_r7p="Casablanca, Essaouira, Agadir et le village de surf de Taghazout.",
 ab_r8="Excursions d’une journée",ab_r8p="Agafay, Ouzoud, Essaouira, l’Ourika, le Haut Atlas et Moulay Yacoub.",
 ab_pe="Notre engagement",ab_ph="Ce sur quoi vous pouvez <em>compter</em>",
 ab_pp="Quelle que soit la durée de votre voyage, voici les engagements que nous prenons envers chaque voyageur qui nous choisit.",
 ab_p1="Une réponse personnelle",ab_p1p="Une vraie personne lit votre message et vous répond, généralement le jour même.",
 ab_p2="Un devis gratuit et sans engagement",ab_p2p="Vous recevez une proposition détaillée avec le prix avant de décider quoi que ce soit.",
 ab_p3="Transparence",ab_p3p="Ce qui est inclus, non inclus et en option est écrit clairement dans chaque itinéraire.",
 ab_p4="Flexibilité",ab_p4p="Itinéraires, horaires et étapes peuvent être adaptés, avant et pendant le voyage.",
 ab_p5="Des hébergements choisis avec soin",ab_p5p="Riads, hôtels et camps sélectionnés pour leur confort, leur propreté et leur caractère.",
 ab_p6="Assistance sur la route",ab_p6p="Notre équipe reste joignable sur WhatsApp de votre arrivée à votre départ.",
 ab_ce="Quand vous voulez",ab_ch="Créons votre <em>Maroc</em>",
 ab_cp="Dites-nous comment vous imaginez votre voyage. Nous vous répondrons avec des idées, un itinéraire clair et un devis gratuit.",
 ab_cb1="Organiser mon voyage",ab_cb2="Voir nos circuits"),
'it':dict(
 ab_h="Chi <em>siamo</em>",
 ab_l="Un’agenzia di viaggi marocchina nata da un’idea semplice: viaggi privati, progettati con cura da persone che conoscono il paese dall’interno.",
 ab_se="La nostra storia",ab_sh="Il Marocco, come lo mostreremmo a <em>un amico</em>",
 ab_s_p1="MoroccoRoyalTrips è nata da 8 anni sulle strade del Marocco: albe nelle medine, lunghi viaggi sull’Alto Atlante, notti sotto le stelle del Sahara. Lungo il cammino abbiamo incontrato viaggiatori che volevano più di un programma rigido. Volevano tempo, comfort e qualcuno di cui fidarsi.",
 ab_s_p2="Così abbiamo creato un’agenzia dedicata al viaggio privato. Niente pullman affollati né orari rigidi: ogni viaggio è solo tuo, con il tuo autista, il tuo ritmo e un itinerario costruito su ciò che ami, che sia la cucina, la storia, la fotografia, il deserto o semplicemente un riad tranquillo con vista.",
 ab_s_p3="Siamo un team locale e lavoriamo con guide locali, riad a conduzione familiare e campi tendati che conosciamo di persona. Viaggiare con noi non significa comprare un prodotto da catalogo. Significa essere accolti nel nostro paese.",
 ab_bd="8 anni",ab_bdp="di esperienza sulle strade del Marocco. Tutti i tour sono 100% privati: solo tu, i tuoi compagni di viaggio e il tuo autista-guida.",
 ab_cap="In viaggio con i nostri ospiti",ab_stamp="8 anni · tour privati · Marocco · ",ab_ve="Cosa ci rende diversi",ab_vh="Viaggi pensati per <em>te</em>",
 ab_vp="Sei principi guidano ogni viaggio che organizziamo, da un’escursione di un giorno a un grande tour del regno di due settimane.",
 ab_v1="Privato per natura",ab_v1p="Il tuo veicolo, il tuo autista-guida e i tuoi orari. Ti fermi dove vuoi, per tutto il tempo che vuoi.",
 ab_v2="Conoscenza locale",ab_v2p="Viviamo qui. Sappiamo quale strada prendere dopo la pioggia, quale riad ha la terrazza più bella e quando la luce è perfetta sulle dune.",
 ab_v3="Itinerari su misura",ab_v3p="Ogni programma di questo sito è un punto di partenza. Adattiamo percorso, ritmo e sistemazioni ai tuoi desideri.",
 ab_v4="Prezzi chiari e onesti",ab_v4p="Ti diciamo esattamente cosa è incluso e cosa no, prima della prenotazione. Nessun costo nascosto e nessuna sorpresa.",
 ab_v5="Comfort e sicurezza",ab_v5p="Veicoli moderni con aria condizionata, autisti esperti che conoscono ogni curva delle strade di montagna e sistemazioni scelte con cura.",
 ab_v6="Rispetto per le persone e i luoghi",ab_v6p="Lavoriamo con famiglie, cooperative e guide locali, e viaggiamo nel rispetto delle comunità e dei paesaggi che visitiamo.",
 ab_se2="Come lavoriamo",ab_sh2="Dal primo messaggio all’<em>ultimo saluto</em>",
 ab_sp2="Organizzare un viaggio in Marocco dovrebbe essere un piacere, non un rompicapo. Ecco come ce ne occupiamo insieme a te.",
 ab_s1="Raccontaci la tua idea",ab_s1p="Scrivici su WhatsApp o tramite il modulo: le date, quanti siete e cosa sogni di vedere.",
 ab_s2="Ricevi la tua proposta",ab_s2p="Ti rispondiamo di persona con un itinerario chiaro giorno per giorno, le sistemazioni consigliate e un preventivo trasparente.",
 ab_s3="Definiscila con noi",ab_s3p="Cambia una notte, aggiungi una città, rallenta il ritmo. Adattiamo tutto finché il viaggio non è perfetto per te.",
 ab_s4="Viaggia sereno",ab_s4p="Il tuo autista ti accoglie all’arrivo e il nostro team resta raggiungibile su WhatsApp per tutto il viaggio.",
 ab_te="Il nostro team",ab_th="Persone che amano <em>il loro paese</em>",
 ab_tp="Dietro ogni viaggio c’è un piccolo team di professionisti marocchini: organizzatori che rispondono ai tuoi messaggi, autisti che conoscono ogni strada e guide locali che danno vita alla storia delle città.",
 ab_t1="Autisti-guida che parlano inglese e spagnolo, francese e italiano su richiesta",
 ab_t2="Guide locali ufficiali per le medine di Fes, Marrakech e altre città",
 ab_t3="Partner di fiducia: riad di famiglia, kasbah e campi nel deserto che conosciamo di persona",
 ab_t4="Un team di organizzazione che ti risponde direttamente, prima e durante il viaggio",
 ab_t5="Esperienza con coppie, famiglie, amici, gruppi di studenti e viaggi tematici",
 ab_re="Dove viaggiamo",ab_rh="Tutto il regno, <em>da nord a sud</em>",
 ab_rp="I nostri tour partono dalle principali porte d’ingresso del Marocco e raggiungono ogni regione, dal Mediterraneo ai margini del Sahara.",
 ab_r1="Città imperiali",ab_r1p="Fes, Meknes, Rabat e Marrakech: medine, palazzi e secoli di storia.",
 ab_r2="Il nord",ab_r2p="Tangeri, i vicoli blu di Chefchaouen e le rovine romane di Volubilis.",
 ab_r3="Il Sahara",ab_r3p="Le dune dell’Erg Chebbi a Merzouga e le sabbie selvagge dell’Erg Chigaga.",
 ab_r4="L’Atlante",ab_r4p="Il passo del Tizi n’Tichka, i villaggi berberi, la valle dell’Ourika e i cedri del Medio Atlante.",
 ab_r5="Valli e gole",ab_r5p="Le gole del Dades e del Todra, la valle delle Rose e i palmeti del Draa.",
 ab_r6="Kasbah del sud",ab_r6p="Ouarzazate, Ait Ben Haddou e la strada delle mille kasbah.",
 ab_r7="La costa atlantica",ab_r7p="Casablanca, Essaouira, Agadir e il villaggio del surf di Taghazout.",
 ab_r8="Escursioni di un giorno",ab_r8p="Agafay, Ouzoud, Essaouira, Ourika, l’Alto Atlante e Moulay Yacoub.",
 ab_pe="Il nostro impegno",ab_ph="Su cosa puoi <em>contare</em>",
 ab_pp="Qualunque sia la durata del tuo viaggio, questi sono gli impegni che prendiamo con ogni viaggiatore che ci sceglie.",
 ab_p1="Una risposta personale",ab_p1p="Una persona vera legge il tuo messaggio e ti risponde, di solito in giornata.",
 ab_p2="Preventivo gratuito e senza impegno",ab_p2p="Ricevi una proposta dettagliata con il prezzo prima di decidere qualsiasi cosa.",
 ab_p3="Trasparenza",ab_p3p="Incluso, non incluso ed extra facoltativi sono scritti chiaramente in ogni itinerario.",
 ab_p4="Flessibilità",ab_p4p="Percorsi, orari e soste possono essere adattati, prima e durante il viaggio.",
 ab_p5="Sistemazioni scelte con cura",ab_p5p="Riad, hotel e campi selezionati per comfort, pulizia e carattere.",
 ab_p6="Assistenza durante il viaggio",ab_p6p="Il nostro team resta raggiungibile su WhatsApp dal tuo arrivo alla tua partenza.",
 ab_ce="Quando vuoi tu",ab_ch="Progettiamo il tuo <em>Marocco</em>",
 ab_cp="Raccontaci come immagini il tuo viaggio. Ti risponderemo con idee, un itinerario chiaro e un preventivo gratuito.",
 ab_cb1="Organizza il mio viaggio",ab_cb2="Scopri i nostri tour"),
}

JS=''
