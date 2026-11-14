import random, json
from act_data import ACTS, G, L
from act_extra import EXTRA, LBL

STAR='<path d="M12 2l2.9 5.1L20 4l-3.1 5.1L22 12l-5.1 2.9L20 20l-5.1-3.1L12 22l-2.9-5.1L4 20l3.1-5.1L2 12l5.1-2.9L4 4l5.1 3.1z" fill="currentColor"/>'

# ---------- silhouettes (local coordinates) ----------
QUAD='''<g fill="{c}"><circle cx="22" cy="50" r="12"/><circle cx="92" cy="50" r="12"/><path d="M8 44L28 30h52l24 9 6 7H4z"/><circle cx="56" cy="5" r="6"/><path d="M50 12h11l4 19H47z"/><path d="M62 16l22 10-2 4-22-8z"/></g>'''
BUGGY='''<g fill="{c}"><circle cx="20" cy="52" r="13"/><circle cx="102" cy="52" r="13"/><path d="M4 46L30 34h66l24 10-6 6H8z"/></g><path d="M32 35L46 8h40l10 27M46 8l20 27M66 8v27" fill="none" stroke="{c}" stroke-width="4" stroke-linejoin="round"/>'''
CAMEL='''<g fill="{c}"><path d="M20 60C22 40 35 30 50 32 58 18 72 18 78 32 85 30 92 34 95 30l5-12c2-4 8-4 10 0l2 6-6 2-2 10c-2 8-8 12-12 12v32h-4l-1-28-27 2-2 26h-4l-1-26c-13 0-19 4-21 26h-4z"/><circle cx="64" cy="9" r="5"/><path d="M59 14h10l3 18H57z"/></g>'''
BOARDER='''<g fill="{c}"><circle cx="20" cy="6" r="6"/><path d="M15 13h10l3 18-4 16h-5l3-15-6 4-6 11-4-2 6-14z"/><path d="M14 16L2 22l2 3 12-5zM26 16l12 3-1 4-12-2z"/></g><path d="M0 52l40-8" stroke="{c}" stroke-width="5" stroke-linecap="round"/>'''

def stars(rng,n,w,h,col='#fff6e0'):
    return ''.join(f'<circle cx="{rng.uniform(0,w):.0f}" cy="{rng.uniform(0,h):.0f}" r="{rng.choice([.8,1,1.2,1.6,2.2]):.1f}" fill="{col}" opacity="{rng.uniform(.35,.95):.2f}"/>' for _ in range(n))

def scene(key, uid):
    rng=random.Random(key)
    g=lambda i,stops: f'<linearGradient id="{uid}{i}" x1="0" y1="0" x2="0" y2="1">'+''.join(f'<stop offset="{o}" stop-color="{c}"/>' for o,c in stops)+'</linearGradient>'
    head=f'<svg class="art-svg" viewBox="0 0 1600 900" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><defs>'
    if key=='stars':
        body=g('s',[(0,'#05081a'),(.55,'#1b2147'),(1,'#4a2f4f')])+f'<radialGradient id="{uid}g"><stop offset="0" stop-color="#ffb35c" stop-opacity=".9"/><stop offset="1" stop-color="#ffb35c" stop-opacity="0"/></radialGradient></defs>'
        body+=f'<rect width="1600" height="900" fill="url(#{uid}s)"/>'
        body+='<ellipse cx="800" cy="300" rx="900" ry="90" fill="#cdd6ff" opacity=".10" transform="rotate(-18 800 300)"/><ellipse cx="800" cy="300" rx="700" ry="40" fill="#fff" opacity=".07" transform="rotate(-18 800 300)"/>'
        body+=stars(rng,260,1600,620)
        body+='<path d="M0 640C220 560 420 580 640 640S1060 720 1280 640 1520 580 1600 600V900H0Z" fill="#2a1a24"/><path d="M0 740C260 690 520 700 760 750S1240 800 1600 730V900H0Z" fill="#160d16"/>'
        body+=f'<circle cx="1180" cy="660" r="90" fill="url(#{uid}g)"/><path d="M1140 690l40-40 40 40z" fill="#120a10"/>'
        body+=f'<g transform="translate(560 700) scale(1.3)"><path d="M0 14C10 6 30 4 46 10" stroke="#0e080e" stroke-width="8" stroke-linecap="round"/><circle cx="54" cy="8" r="7" fill="#0e080e"/></g>'
    elif key=='mquad':
        body=g('s',[(0,'#f7d8a6'),(1,'#f0a965')])+'</defs>'+f'<rect width="1600" height="900" fill="url(#{uid}s)"/><circle cx="1240" cy="230" r="80" fill="#fff3d6" opacity=".9"/>'
        body+='<path d="M0 520C300 380 560 400 820 500S1300 620 1600 470V900H0Z" fill="#e39a55"/><path d="M0 660C320 560 640 580 900 650S1360 720 1600 640V900H0Z" fill="#c8733a"/><path d="M0 790C360 740 760 760 1100 800S1500 820 1600 800V900H0Z" fill="#a4552a"/>'
        body+='<g opacity=".35" fill="#fbe2bf"><ellipse cx="560" cy="500" rx="120" ry="34"/><ellipse cx="470" cy="480" rx="80" ry="26"/><ellipse cx="400" cy="470" rx="50" ry="18"/></g>'
        body+='<g transform="translate(600 430) scale(1.5)">'+QUAD.format(c='#3a1c0e')+'</g>'
    elif key=='mbuggy':
        body=g('s',[(0,'#3d2445'),(.5,'#c4553a'),(1,'#f2a25a')])+'</defs>'+f'<rect width="1600" height="900" fill="url(#{uid}s)"/><circle cx="800" cy="560" r="150" fill="#ffd28a" opacity=".95"/>'
        body+='<path d="M0 600C300 520 560 540 800 600S1300 660 1600 580V900H0Z" fill="#9a4426"/><path d="M0 720C360 660 700 680 1000 730S1460 760 1600 720V900H0Z" fill="#6e2c18"/>'
        body+='<g opacity=".4" fill="#f6b27a"><ellipse cx="560" cy="650" rx="140" ry="30"/><ellipse cx="470" cy="635" rx="90" ry="22"/></g>'
        body+='<g transform="translate(600 560) scale(1.6)">'+BUGGY.format(c='#2a1009')+'</g>'
    elif key=='sand':
        body=g('s',[(0,'#a9c9e2'),(1,'#f6dcae')])+'</defs>'+f'<rect width="1600" height="900" fill="url(#{uid}s)"/>'
        body+='<path d="M0 760L520 260C560 230 600 230 640 262L1600 760V900H0Z" fill="#e7a35c"/><path d="M580 245L1600 760V900H900Z" fill="#c4733a" opacity=".55"/><path d="M0 820C400 780 900 790 1600 820V900H0Z" fill="#b3612f"/>'
        body+='<path d="M600 300C560 380 520 460 470 560" stroke="#fbe0b8" stroke-width="6" fill="none" opacity=".7" stroke-linecap="round"/>'
        body+='<g transform="translate(420 520) scale(2) rotate(-25)">'+BOARDER.format(c='#3b1f10')+'</g>'
    elif key in ('abuggy','aquad'):
        body=g('s',[(0,'#f4cfa2'),(1,'#eaa879')])+'</defs>'+f'<rect width="1600" height="900" fill="url(#{uid}s)"/><circle cx="{1260 if key=="abuggy" else 360}" cy="200" r="70" fill="#fff4dc" opacity=".85"/>'
        body+='<path d="M0 470L180 380 320 430 520 330 700 420 880 340 1080 430 1260 350 1440 420 1600 380V900H0Z" fill="#9fa9bd" opacity=".7"/><path d="M500 345l20-14 18 12-12 2zM860 352l20-12 18 14-14-2zM1250 362l12-10 14 10z" fill="#fff"/>'
        body+='<path d="M0 560L140 500 300 540 460 480 640 550 820 490 1000 560 1200 500 1400 560 1600 520V900H0Z" fill="#b98157"/><path d="M0 680L200 620 380 660 560 610 760 670 960 630 1160 690 1380 640 1600 680V900H0Z" fill="#94603f"/><path d="M0 800C400 770 900 780 1600 800V900H0Z" fill="#6f4229"/>'
        body+='<g fill="#5e3a24" opacity=".6"><circle cx="300" cy="760" r="6"/><circle cx="900" cy="775" r="8"/><circle cx="1300" cy="770" r="5"/><circle cx="640" cy="790" r="4"/></g>'
        body+='<g opacity=".35" fill="#f7d9b3"><ellipse cx="650" cy="650" rx="130" ry="30"/><ellipse cx="560" cy="635" rx="80" ry="22"/></g>'
        sil=BUGGY if key=='abuggy' else QUAD
        body+=f'<g transform="translate(690 560) scale(1.6)">'+sil.format(c='#3a2114')+'</g>'
    elif key=='acamel':
        body=g('s',[(0,'#6e4466'),(.45,'#f2845f'),(1,'#f9c27a')])+'</defs>'+f'<rect width="1600" height="900" fill="url(#{uid}s)"/><circle cx="1000" cy="560" r="160" fill="#ffe0a3"/>'
        body+='<path d="M0 560L200 500 400 540 600 480 820 540 1040 500 1260 560 1460 520 1600 550V900H0Z" fill="#a85b48" opacity=".8"/><path d="M0 680C300 640 700 650 1000 690S1450 710 1600 680V900H0Z" fill="#5b2c2a"/>'
        body+='<g transform="translate(560 520) scale(2.1)">'+CAMEL.format(c='#2b1214')+'</g>'
    elif key=='dinner':
        body=g('s',[(0,'#070b24'),(.6,'#22193d'),(1,'#4b2a3b')])+f'<radialGradient id="{uid}l"><stop offset="0" stop-color="#ffc56a"/><stop offset=".3" stop-color="#ff9a3c" stop-opacity=".7"/><stop offset="1" stop-color="#ff9a3c" stop-opacity="0"/></radialGradient></defs>'
        body+=f'<rect width="1600" height="900" fill="url(#{uid}s)"/>'+stars(rng,180,1600,500)
        body+='<path d="M0 640L260 600 520 630 800 590 1100 630 1380 600 1600 620V900H0Z" fill="#1c1220"/>'
        body+='<g fill="#120b14"><path d="M240 650l120-110 120 110z"/><path d="M520 655l150-140 150 140z"/><path d="M1040 650l120-110 120 110z"/></g>'
        for x,y,r in [(320,640,60),(670,645,70),(1160,640,60),(860,700,120),(430,700,40),(1300,700,40)]:
            body+=f'<circle cx="{x}" cy="{y}" r="{r}" fill="url(#{uid}l)"/>'
        body+='<path d="M0 760C400 730 900 740 1600 760V900H0Z" fill="#0d0810"/><path d="M840 720c10-30 30-40 20-70 20 20 30 40 20 70z" fill="#ffb347"/><path d="M852 722c4-14 12-20 8-34 10 10 14 20 10 34z" fill="#fff0b0"/>'
    return head+body+'</svg>'


# ---------- real photos (replace the illustration when available) ----------
PHOTOS={
 'agafay-quad':dict(pos='60% 55%',alt='Quad bikes on desert tracks'),
 'agafay-buggy':dict(pos='50% 55%',alt='Dune buggies parked on a desert crest'),
 'agafay-camel':dict(pos='50% 52%',alt='Camel caravan crossing the Agafay desert at sunset'),
 'merzouga-stargazing':dict(pos='50% 62%',alt='Desert camp with lanterns under the moon and night sky in Merzouga'),
 'merzouga-quad':dict(pos='50% 40%',alt='Two travellers standing on quad bikes at sunset over the Erg Chebbi dunes'),
 'merzouga-buggy':dict(pos='55% 50%',alt='Two dune buggies kicking up sand in the Merzouga dunes'),
 'merzouga-sandboarding':dict(pos='60% 62%',alt='Group of travellers with sandboards on top of a high dune'),
 'merzouga-4x4':dict(pos='60% 50%',alt='4x4 vehicle and camel caravan on the Erg Chebbi dunes'),
 'merzouga-hero':dict(pos='62% 48%',alt='Camel caravan silhouetted on the Erg Chebbi dunes at sunset'),
 'agafay-dinner':dict(pos='50% 50%',alt='Musicians performing around a fire in a desert camp'),
 'ha-abh-hero':dict(pos='50% 50%',alt='Ait Ben Haddou'),
 'ha-abh':dict(pos='50% 50%',alt='Ait Ben Haddou'),
 'ha-atlas':dict(pos='50% 50%',alt='High Atlas'),
 'ha-village':dict(pos='50% 50%',alt='Berber village'),
 'dades-road':dict(pos='50% 50%',alt='Dades Gorges road'),
 'uz-hero':dict(pos='50% 50%',alt='Boat at the foot of the Ouzoud waterfalls'),
 'uz-boat':dict(pos='50% 50%',alt='Boat at the foot of the Ouzoud waterfalls'),
 'uz-aerial':dict(pos='50% 50%',alt='Ouzoud gorge, cafés and pools seen from above'),
 'uz-monkey':dict(pos='50% 50%',alt='Barbary macaque above the Ouzoud falls'),
 'uz-lunch':dict(pos='50% 50%',alt='Lunch on a terrace facing the Ouzoud falls'),
 'es-hero':dict(pos='50% 50%',alt='Blue fishing boats and the Skala of the port of Essaouira'),
 'es-skala':dict(pos='50% 50%',alt='Sea ramparts of Essaouira with bronze cannons'),
 'es-medina':dict(pos='50% 50%',alt='Lane in the medina of Essaouira'),
 'es-fish':dict(pos='50% 50%',alt='Grilled fish at the port of Essaouira'),
 'es-argan':dict(pos='50% 50%',alt='Women cracking argan nuts in a cooperative'),
 'uz-couple':dict(pos='50% 50%',alt='Couple by a waterfall in the green gorge'),
 'ou-hero':dict(pos='50% 50%',alt='River and terrace cafés in the Ourika Valley'),
 'ou-cafes':dict(pos='50% 50%',alt='Riverside terraces in Setti Fatma'),
 'ou-lunch':dict(pos='50% 50%',alt='Tagine lunch on a terrace above the river'),
 'ou-river':dict(pos='50% 50%',alt='Mountain river in the valley'),
 'ou-oranges':dict(pos='50% 50%',alt='Oranges and water bottles cooling in a blue fountain'),
 'my-hero':dict(pos='50% 50%',alt='Thermal pool under Moroccan arches in Moulay Yacoub'),
 'my-pool':dict(pos='50% 50%',alt='Indoor thermal pool of the modern spa in Moulay Yacoub'),
 'my-town':dict(pos='50% 50%',alt='The hill town of Moulay Yacoub and its modern thermal spa'),
 'my-outdoor':dict(pos='50% 50%',alt='Outdoor pool facing the hills of Moulay Yacoub'),
 'casa-mosque-hero':dict(pos='50% 50%',alt='Hassan II Mosque in Casablanca'),
 'casa-mosque':dict(pos='50% 50%',alt='Hassan II Mosque in Casablanca'),
 'hm-couple':dict(pos='50% 50%',alt='Couple walking hand in hand on the dunes'),
 'jh-box':dict(pos='50% 50%',alt='Brass tzedakah box with a Star of David on Moroccan zellige tiles'),
 'mk-badi':dict(pos='50% 50%',alt='El Badi Palace, Marrakech'),
 'mk-jemaa':dict(pos='50% 50%',alt='Jemaa el-Fna square at sunset, Marrakech'),
 'mk-jemaa2':dict(pos='50% 50%',alt='Jemaa el-Fna square, Marrakech'),
 'chef-stairs':dict(pos='50% 50%',alt='Blue stairway in Chefchaouen'),
 'chef-alley':dict(pos='50% 50%',alt='Painted lane in Chefchaouen'),
 'rabat-hassan':dict(pos='50% 50%',alt='Hassan Tower, Rabat'),
 'fes-alley':dict(pos='50% 50%',alt='Lane in the medina of Fes'),
 'fes-tannery':dict(pos='50% 50%',alt='Chouara tannery, Fes'),
 'fes-tannery-hero':dict(pos='50% 50%',alt='Chouara tannery, Fes'),
 'meknes-bab':dict(pos='50% 50%',alt='Bab Mansour gate, Meknes'),
 'lx-camp':dict(pos='50% 50%',alt='Desert camp tents at sunset'),
 'lx-dunes':dict(pos='50% 50%',alt='Desert camp among the dunes of Merzouga'),
 'sg-group':dict(pos='50% 50%',alt='A group of friends on top of a dune'),
 'ph-walk':dict(pos='50% 50%',alt='Photographer walking towards the dunes'),
 'ph-dunes':dict(pos='50% 50%',alt='Photographer shooting in the dunes'),
 'tg-surf':dict(pos='50% 50%',alt='Surfer on the rocks of Taghazout'),
 'tg-camel':dict(pos='50% 50%',alt='Camel on the beach of Taghazout'),
 'mk-koutoubia':dict(pos='50% 50%',alt='Rooftop view of the Koutoubia minaret at dusk, Marrakech'),
 'chg-caravan':dict(pos='50% 80%',alt='Camel caravan crossing the dunes'),
 'agadir-marina':dict(pos='50% 50%',alt='Agadir marina below the Kasbah hill'),
 'casa-sunset':dict(pos='50% 50%',alt='Hassan II Mosque on the Atlantic at sunset, Casablanca'),
 'camp-sunset':dict(pos='50% 50%',alt='Desert camp with red carpets at sunset in Erg Chebbi'),
 'mk-koutoubia-arch':dict(pos='50% 50%',alt='Koutoubia minaret framed by an arch, Marrakech'),
 'fes-qarawiyyin':dict(pos='50% 50%',alt='Courtyard of the Al Quaraouiyine mosque, Fes'),
 'erg-palm':dict(pos='50% 50%',alt='A lone palm tree among the dunes of Erg Chebbi'),
 'caravan-dusk':dict(pos='50% 50%',alt='Camel caravan on a dune ridge at dusk'),
 'abh-reflect':dict(pos='50% 50%',alt='Ait Ben Haddou near Ouarzazate'),
 'camel-sunset':dict(pos='50% 50%',alt='Camels silhouetted against the setting sun'),
 'ouz-studios':dict(pos='50% 50%',alt='Egyptian film set at the Atlas Studios, Ouarzazate'),
 'dune-lounge':dict(pos='50% 50%',alt='Carpets, cushions and a fire pit set on the dunes of Erg Chebbi'),
 'dune-friends':dict(pos='50% 50%',alt='Travellers watching the sunset from a high dune'),
 'camp-tents':dict(pos='50% 50%',alt='Tents of a desert camp facing the dunes'),
 'sth-monkeys':dict(pos='50% 50%',alt='Barbary macaques in the cedar forest near Azrou'),
 'sth-ksar':dict(pos='50% 50%',alt='Palm grove and old ksar below the cliffs of the south'),
 'erg-caravan':dict(pos='50% 50%',alt='Camel caravan crossing the dunes of Erg Chebbi'),
 'ouz-taourirt':dict(pos='50% 50%',alt='Taourirt Kasbah, Ouarzazate'),
 'ifr-cedar':dict(pos='50% 50%',alt='Road through the cedar forest of the Middle Atlas'),
 'dades-bends':dict(pos='50% 60%',alt='Hairpin bends of the Dades Gorges road'),
 'draa-oasis':dict(pos='50% 45%',alt='River and palm groves of the Draa Valley'),
 'chg-dunes':dict(pos='50% 50%',alt='Camels walking through the dunes of Erg Chigaga'),
 'tangier-bay':dict(pos='50% 55%',alt='The white medina of Tangier above the bay'),
 'cs4-camp':dict(pos='50% 60%',alt='Luxury desert camp with carpets and cushions in the dunes of Merzouga'),
 'tz12-sun':dict(pos='50% 58%',alt='Camel caravan silhouetted against the setting sun in the Sahara'),
 'tn4-koutoubia':dict(pos='50% 45%',alt='Sunset behind the Koutoubia minaret above Jemaa el-Fna square, Marrakech'),
 'ag3-pool':dict(pos='50% 55%',alt='Pool and Moroccan arch framing the dunes of Merzouga'),
 'agafay-pool':dict(pos='50% 62%',alt='Pool lined with palm trees facing the Agafay hills and the Atlas at sunset'),
}
def art_html(a, uid, hero=False):
    ph=PHOTOS.get(a['id'])
    if ph:
        return f'<img class="art-svg art-photo" src="{{{{IMG_{a["id"]}}}}}" alt="{ph["alt"]}" style="object-position:{ph["pos"]}" loading="{'eager' if hero else 'lazy'}">'
    return scene(a['art'], uid)

# ---------- CSS ----------
CSS='''
/* ================= ACTIVITY PAGES ================= */
.art-svg{width:100%;height:100%;display:block}
img.art-photo{object-fit:cover;max-width:none}
.hero.hero-act{min-height:clamp(480px,68vh,760px)}
.hero-act .hero-bg{width:100%;height:100%}
.hero-act .hero-shade{background:linear-gradient(180deg,rgba(0,0,0,.45) 0%,rgba(0,0,0,0) 28%),linear-gradient(0deg,rgba(0,0,0,.7) 0%,rgba(0,0,0,0) 55%),radial-gradient(ellipse 55% 65% at 18% 78%,rgba(0,0,0,.35) 0%,rgba(0,0,0,0) 70%)}
.hero-act .hero-in{justify-content:flex-end;padding-block:150px 64px}
.hero-act h1{font-size:clamp(44px,6.4vw,92px);max-width:16ch}
.crumbs{display:flex;flex-wrap:wrap;gap:10px;align-items:center;font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:rgba(255,255,255,.75);text-shadow:0 1px 8px rgba(0,0,0,.6)}
.crumbs a:hover{color:var(--gold-hi)}
.crumbs svg{width:10px;height:10px;transform:rotate(-90deg)}
.chip-tag{display:inline-flex;align-items:center;gap:8px;font-size:11px;font-weight:600;letter-spacing:.24em;text-transform:uppercase;color:#fff;padding:6px 12px;border-radius:999px;background:rgba(0,0,0,.35);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);border:1px solid rgba(255,255,255,.25)}

.act-sec{background:#f5efe4;color:#16213d}
.act-intro{display:grid;grid-template-columns:5fr 6fr;gap:64px;align-items:end;padding-block:100px 56px}
.act-intro .eyebrow{color:#9a7433}.act-intro .eyebrow::before{animation:none}
.act-intro h2{font-size:clamp(36px,4.4vw,60px);line-height:.98;margin-top:14px}
.act-intro h2 em{color:#b0843f}
.act-intro p{margin:0;font-size:17px;line-height:1.75;color:#4a536d;max-width:56ch}
.act-grid{display:grid;grid-template-columns:1fr 1fr;gap:28px;padding-bottom:110px}
.act-grid.odd > .acard:first-child{grid-column:1/-1}
.act-grid.odd > .acard:first-child .art{aspect-ratio:21/9}
.acard{display:flex;flex-direction:column;gap:20px}
.acard .art{position:relative;aspect-ratio:16/10;max-width:100%;border-radius:18px;overflow:hidden;box-shadow:0 20px 50px rgba(22,33,61,.12)}
.acard .art .art-svg{transition:transform 1.2s var(--ease)}
.acard:hover .art .art-svg{transform:scale(1.07)}
.acard .art .chip-tag{position:absolute;left:16px;top:16px}
.acard .txt{display:grid;gap:10px}
.acard h3{font-size:clamp(24px,2.3vw,32px);line-height:1.02;color:#16213d;transition:color .3s}
.acard:hover h3{color:#b0843f}
.acard p{margin:0;color:#4a536d;font-size:15.5px;line-height:1.65;max-width:52ch}
.acard .meta{display:flex;gap:18px;flex-wrap:wrap;font-size:12.5px;color:#6b7289}
.acard .meta b{font-weight:600;color:#9a7433;letter-spacing:.14em;text-transform:uppercase;font-size:10.5px;margin-right:6px}
.acard .go{display:inline-flex;align-items:center;gap:10px;font-size:12px;font-weight:600;letter-spacing:.2em;text-transform:uppercase;color:#16213d;padding-bottom:5px;width:max-content;background:linear-gradient(#b0843f,#b0843f) left bottom/0% 1px no-repeat;transition:background-size .5s var(--ease)}
.acard:hover .go{background-size:100% 1px}
.acard .go svg{width:15px;height:15px;transition:transform .4s var(--ease)}
.acard:hover .go svg{transform:translateX(6px)}


/* detailed layout */
.ad-text{display:grid;gap:14px}
.ad-text p{margin:0;font-size:16.5px;line-height:1.8;color:#4a536d;max-width:64ch}
.ad-text p:first-child{font-size:clamp(18px,1.5vw,20px);color:#16213d;line-height:1.65}
.ad-photo{position:relative;margin:0;border-radius:20px;overflow:hidden;aspect-ratio:16/10;max-width:100%;box-shadow:0 24px 60px rgba(22,33,61,.16)}
.ad-photo .art-svg{transition:transform 1.4s var(--ease)}
.ad-photo:hover .art-svg{transform:scale(1.05)}
.ad-photo::after{content:"";position:absolute;inset:0;background:linear-gradient(0deg,rgba(10,12,20,.82) 0%,rgba(10,12,20,.15) 55%,rgba(10,12,20,0) 100%)}
.ad-photo figcaption{position:absolute;left:0;right:0;bottom:0;z-index:1;padding:28px 30px;display:grid;gap:12px;color:#fff}
.ad-photo h3{font-size:clamp(28px,3.2vw,44px);line-height:1;color:#fff}
.ad-meta{display:flex;flex-wrap:wrap;gap:10px 24px;font-size:14px;color:rgba(255,255,255,.88)}
.ad-meta > span{display:inline-flex;align-items:center;gap:8px}
.ad-meta svg{width:16px;height:16px;color:var(--gold-hi)}
.ad-list.yes li::before,.ad-list.no li::before{width:18px;height:18px;flex:none;transform:translateY(3px);background:none;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:11px;font-weight:700}
.ad-list.yes li::before{content:"✓";color:#fff;background:#b0843f}
.ad-list.no li::before{content:"✕";color:#b4544a;border:1px solid rgba(180,84,74,.4)}
.itin{border-top:1px solid rgba(22,33,61,.15);border-bottom:1px solid rgba(22,33,61,.15)}
.itin-btn{width:100%;display:grid;grid-template-columns:auto 1fr auto;align-items:center;gap:20px;padding:24px 0;border:0;background:none;cursor:pointer;text-align:left;color:#16213d}
.itin-btn .eyebrow{color:#9a7433}.itin-btn .eyebrow::before{animation:none}
.itin-route{font-family:var(--display);font-size:clamp(17px,1.6vw,22px);text-transform:uppercase;letter-spacing:.02em;line-height:1.2}
.itin .acc-plus{position:relative;width:22px;height:22px;transition:transform .5s var(--ease)}
.itin .acc-plus::before,.itin .acc-plus::after{content:"";position:absolute;left:0;right:0;top:50%;height:1.5px;background:#16213d;transform:translateY(-50%);transition:transform .5s var(--ease),background .35s}
.itin .acc-plus::after{transform:translateY(-50%) rotate(90deg)}
.itin.open .acc-plus{transform:rotate(180deg)}
.itin.open .acc-plus::before,.itin.open .acc-plus::after{background:#b0843f}
.itin.open .acc-plus::after{transform:translateY(-50%) rotate(0)}
.itin .acc-panel{display:grid;grid-template-rows:0fr;transition:grid-template-rows .55s var(--ease)}
.itin.open .acc-panel{grid-template-rows:1fr}
.itin .acc-inner{overflow:hidden}
.steps{list-style:none;margin:0;padding:4px 0 30px;counter-reset:st;display:grid;gap:0}
.steps li{position:relative;counter-increment:st;padding:0 0 26px 62px;display:grid;gap:6px}
.steps li::before{content:counter(st,decimal-leading-zero);position:absolute;left:0;top:-2px;width:40px;height:40px;border-radius:50%;border:1px solid #b0843f;color:#9a7433;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:600;letter-spacing:.06em;background:#f5efe4}
.steps li::after{content:"";position:absolute;left:20px;top:42px;bottom:4px;width:1px;background:rgba(176,132,63,.35)}
.steps li:last-child{padding-bottom:0}
.steps li:last-child::after{display:none}
.steps b{font-family:var(--display);font-weight:400;font-size:21px;text-transform:uppercase;letter-spacing:.02em;color:#16213d;padding-top:7px}
.steps p{margin:0;color:#4a536d;font-size:15.5px;line-height:1.7;max-width:60ch}
@media (max-width:900px){.ad-photo{aspect-ratio:4/5}.ad-photo figcaption{padding:22px}.itin-btn{grid-template-columns:1fr auto}.itin-btn .eyebrow{grid-column:1/-1}.itin-route{grid-column:1}}

/* detail */
.ad{display:grid;grid-template-columns:7fr 4fr;gap:64px;align-items:start;padding-block:100px}
.ad-main{display:grid;gap:44px}
.ad-block{display:grid;gap:16px;align-content:start}
.ad-block .eyebrow{color:#9a7433}.ad-block .eyebrow::before{animation:none}
.ad-lead{font-size:clamp(19px,1.6vw,22px);line-height:1.6;color:#16213d;margin:0;max-width:60ch}
.ad-block p{margin:0;font-size:16.5px;line-height:1.8;color:#4a536d;max-width:62ch}
.ad-list{list-style:none;margin:0;padding:0;border-top:1px solid rgba(22,33,61,.15)}
.ad-list li{display:flex;gap:16px;align-items:baseline;padding:16px 0;border-bottom:1px solid rgba(22,33,61,.15);font-size:16.5px;color:#16213d}
.ad-list li::before{content:"";flex:none;width:12px;height:1px;background:#b0843f;transform:translateY(-4px)}
.ad-two{display:grid;grid-template-columns:1fr 1fr;gap:40px}
.book{position:sticky;top:110px;background:#fffdf9;border:1px solid rgba(176,132,63,.22);border-radius:20px;padding:30px 28px;display:grid;gap:18px;box-shadow:0 30px 60px rgba(22,33,61,.1)}
.book::before{content:"";position:absolute;left:28px;right:28px;top:0;height:2px;background:linear-gradient(90deg,transparent,#c9a05a,transparent)}
.book h3{font-size:28px;line-height:1;color:#16213d}
.book p{margin:0;color:#6b7289;font-size:14.5px;line-height:1.6}
.book dl{margin:0;display:grid;border-top:1px solid rgba(22,33,61,.12)}
.book dl div{display:grid;grid-template-columns:110px 1fr;gap:12px;padding:12px 0;border-bottom:1px solid rgba(22,33,61,.12)}
.book dt{font-size:10.5px;font-weight:600;letter-spacing:.22em;text-transform:uppercase;color:#9a7433;padding-top:3px}
.book dd{margin:0;font-size:14.5px;color:#16213d}
.book .btn{width:100%}
.btn.dark{background:#16213d;color:#fff}
.btn.dark:hover{background:#22345f;transform:translateY(-2px)}
.btn.ghost-d{border:1px solid rgba(22,33,61,.25);color:#16213d;background:transparent}
.btn.ghost-d:hover{background:#16213d;color:#fff}

.more{position:relative;background:#ede3d1;color:#16213d;border-top:1px solid rgba(176,132,63,.25)}
.more::before{content:"";position:absolute;left:50%;top:-9px;width:18px;height:18px;transform:translateX(-50%) rotate(45deg);background:#ede3d1;border-left:1px solid rgba(176,132,63,.35);border-top:1px solid rgba(176,132,63,.35)}
.more .in{padding-block:90px}
.more-head{display:flex;justify-content:space-between;align-items:flex-end;gap:20px;flex-wrap:wrap;margin-bottom:34px}
.more-head h2{font-size:clamp(32px,3.6vw,48px);color:#16213d}
.more-head a{font-size:12px;font-weight:600;letter-spacing:.2em;text-transform:uppercase;color:#9a7433;display:inline-flex;gap:10px;align-items:center}
.more-head a svg{width:15px;height:15px;transition:transform .4s var(--ease)}
.more-head a:hover svg{transform:translateX(6px)}
.more-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.more .acard h3{color:#16213d}
.more .acard p{color:#4a536d}
.more .acard .go{color:#16213d}
.more .acard:hover h3{color:#b0843f}
.more .acard .art{box-shadow:0 18px 40px rgba(22,33,61,.12)}

.foot{background:#0a1226;color:rgba(255,255,255,.6);font-size:14px}
.foot .in{display:flex;align-items:center;justify-content:space-between;gap:20px;flex-wrap:wrap;padding-block:34px}
.foot .fb{display:flex;align-items:center;gap:12px}
.foot img{width:44px;height:44px;border-radius:50%}
.foot nav{display:flex;gap:22px;flex-wrap:wrap;font-size:12px;letter-spacing:.18em;text-transform:uppercase}
.foot nav a:hover{color:var(--gold-hi)}

@media (max-width:900px){
  .act-intro,.ad{grid-template-columns:1fr;gap:28px}
  .act-intro{padding-block:70px 40px}
  .act-grid{grid-template-columns:1fr;gap:44px;padding-bottom:80px}
  .ad{padding-block:64px;gap:44px}
  .book{position:static}
  .ad-two{grid-template-columns:1fr;gap:44px}
  .more-grid{grid-template-columns:1fr;gap:40px}
  .hero-act .hero-in{padding-block:120px 44px}
}
'''

ARROW='<svg><use href="#i-arrow"/></svg>'
CHEV='<svg><use href="#i-chev"/></svg>'

def aid(a): return a['id'].replace('-','_')

def card(a, small=False):
    k=aid(a)
    meta='' if small else f'<span class="meta"><span><b data-i="lbl_best">Best time</b><span data-i="{k}_bt"></span></span></span>'
    return f'''<a class="acard reveal" href="{a['id']}.html">
  <span class="art">{art_html(a, 'c'+k+('s' if small else ''))}<span class="chip-tag" data-i="{k}_tag"></span></span>
  <span class="txt"><h3 data-i="{k}_t"></h3><p data-i="{k}_s"></p>{meta}<span class="go"><span data-i="view">View activity</span>{ARROW}</span></span>
</a>'''

FOOT='''<footer class="foot"><div class="in">
  <div class="fb"><img src="{{EMBLEM}}" alt=""><span>© <span class="yr">2026</span> <span data-brand="full">MoroccoRoyalTrips</span></span></div>
  <nav><a href="index.html" data-i="m0">Home</a><a href="merzouga.html" data-i="crumb_m">Merzouga activities</a><a href="agafay.html" data-i="crumb_a">Agafay activities</a><a href="contact.html" data-i="m6">Contact</a></nav>
</div></footer>'''

def list_main(dest):
    p=dest  # 'm' or 'a'
    hero_art={'m':'stars','a':'acamel'}[dest]
    hero_html=art_html(dict(id='agafay-pool',art='acamel'),'h'+dest,True) if dest=='a' else art_html(dict(id='merzouga-hero',art='stars'),'h'+dest,True)
    acts=[a for a in ACTS if a['dest']==dest]
    acts.sort(key=lambda a:0 if a['id']=='merzouga-4x4' else 1)
    return f'''<main id="top">
<section class="hero hero-act" id="hero">
  <div class="hero-media" id="heroMedia"><span class="hero-bg" style="display:block">{hero_html}</span></div>
  <div class="hero-shade" aria-hidden="true"></div>
  <canvas id="dust" aria-hidden="true"></canvas>
  <div class="in hero-in"><div class="hero-copy">
    <nav class="crumbs rise" aria-label="Breadcrumb"><a href="index.html" data-i="m0">Home</a>{CHEV}<span data-i="crumb_{p}"></span></nav>
    <span class="eyebrow rise" data-i="{p}_eye"></span>
    <h1 id="heroTitle" data-i="{p}_t"></h1>
    <p class="lead rise d3" data-i="{p}_p"></p>
  </div></div>
</section>
<section class="act-sec">
  <div class="in">
    <div class="act-intro reveal"><div><span class="eyebrow" data-i="{p}_eye"></span><h2 data-i="{p}_ih"></h2></div><p data-i="{p}_ip"></p></div>
    <div class="act-grid{' odd' if len(acts)%2 else ''}">{''.join(card(a) for a in acts)}</div>
  </div>
</section>
{FOOT}
</main>'''

def detail_main(a):
    k=aid(a); p=a['dest']
    others=[o for o in ACTS if o['dest']==p and o['id']!=a['id']]
    listpage='merzouga.html' if p=='m' else 'agafay.html'
    ex=EXTRA.get(a['id'],{})
    dur_meta=f'<span><svg><use href="#i-clock"/></svg><span data-i="{k}_du"></span></span>' if 'dur' in ex else ''
    dur_row=f'<div><dt data-i="lbl_dur">Duration</dt><dd data-i="{k}_du"></dd></div>' if 'dur' in ex else ''
    itin=''
    if 'steps' in ex:
        itin=f'''<div class="itin open">
        <button class="itin-btn" type="button" aria-expanded="true"><span class="eyebrow" data-i="lbl_itin">Itinerary</span><span class="itin-route" data-i="{k}_ro"></span><span class="acc-plus" aria-hidden="true"></span></button>
        <div class="acc-panel"><div class="acc-inner"><ol class="steps" data-i="{k}_st"></ol></div></div>
      </div>'''
    return f'''<main id="top">
<section class="hero hero-act" id="hero">
  <div class="hero-media" id="heroMedia"><span class="hero-bg" style="display:block">{art_html(a,'h'+k,True)}</span></div>
  <div class="hero-shade" aria-hidden="true"></div>
  <canvas id="dust" aria-hidden="true"></canvas>
  <div class="in hero-in"><div class="hero-copy">
    <nav class="crumbs rise" aria-label="Breadcrumb"><a href="index.html" data-i="m0">Home</a>{CHEV}<a href="{listpage}" data-i="crumb_{p}"></a>{CHEV}<span data-i="{k}_tag"></span></nav>
    <h1 id="heroTitle" data-i="{k}_t"></h1>
    <p class="lead rise d3" data-i="{k}_s"></p>
  </div></div>
</section>
<section class="act-sec">
  <div class="in ad">
    <div class="ad-main reveal">
      <div class="ad-block"><span class="eyebrow" data-i="lbl_over">Overview</span><div class="ad-text" data-i="{k}_o"></div></div>
      <figure class="ad-photo">
        {art_html(a,'f'+k)}
        <figcaption><h3 data-i="{k}_t"></h3>
          <span class="ad-meta"><span><svg><use href="#i-pin"/></svg><span data-i="{k}_pl"></span></span>{dur_meta}</span>
        </figcaption>
      </figure>
      <div class="ad-two">
        <div class="ad-block"><span class="eyebrow" data-i="lbl_inc">Included</span><ul class="ad-list yes" data-i="{k}_i"></ul></div>
        <div class="ad-block"><span class="eyebrow" data-i="lbl_exc">Not included</span><ul class="ad-list no" data-i="{k}_x"></ul></div>
      </div>
      {itin}
    </div>
    <aside class="book reveal">
      <h3 data-i="bk_h">Book this activity</h3>
      <p data-i="bk_p"></p>
      <dl>
        {dur_row}
        <div><dt data-i="lbl_best">Best time</dt><dd data-i="{k}_bt"></dd></div>
        <div><dt data-i="lbl_good">Good for</dt><dd data-i="{k}_gf"></dd></div>
        <div><dt data-i="lbl_price">Price</dt><dd data-i="price_req">On request</dd></div>
      </dl>
      <a class="btn gold js-book" href="#" target="_blank" rel="noopener" data-act="{k}"><svg><use href="#i-wa"/></svg><span data-i="book">Book on WhatsApp</span></a>
      <a class="btn ghost-d" href="contact.html"><span data-i="ask">Ask a question</span></a>
    </aside>
  </div>
</section>
<section class="more">
  <div class="in">
    <div class="more-head"><h2 data-i="more_{p}"></h2><a href="{listpage}"><span data-i="all_{p}"></span>{ARROW}</a></div>
    <div class="more-grid">{''.join(card(o,small=True) for o in others[:3])}</div>
  </div>
</section>
{FOOT}
</main>'''

def tdict(lang):
    d=dict(G[lang]); d.update(LBL[lang])
    place={'m':'Merzouga','a':'Agafay, Marrakech'}
    for a in ACTS:
        k=aid(a)
        d[k+'_t']=a['t'][lang]; d[k+'_tag']=a['tag'][lang]; d[k+'_s']=a['s'][lang]; d[k+'_o']=a['o'][lang]
        d[k+'_h']=''.join(f'<li>{x}</li>' for x in a['h'][lang]); d[k+'_i']=''.join(f'<li>{x}</li>' for x in a['i'][lang])
        d[k+'_bt']=a['bt'][lang]; d[k+'_gf']=a['gf'][lang]
        ex=EXTRA.get(a['id'],{})
        d[k+'_o']=''.join(f'<p>{x}</p>' for x in ex['o'][lang]) if 'o' in ex else f'<p>{a["o"][lang]}</p>'
        if 'inc' in ex: d[k+'_i']=''.join(f'<li>{x}</li>' for x in ex['inc'][lang])
        exc=ex['exc'][lang] if 'exc' in ex else [x for x in G[lang]['exc_def'] if not (a['id']=='agafay-dinner' and x==G[lang]['exc_def'][1])]
        d[k+'_x']=''.join(f'<li>{x}</li>' for x in exc)
        d[k+'_pl']=ex['place'][lang] if 'place' in ex else place[a['dest']]
        if 'dur' in ex: d[k+'_du']=ex['dur'][lang]
        if 'route' in ex: d[k+'_ro']=ex['route'][lang]
        if 'steps' in ex: d[k+'_st']=''.join(f'<li><b>{t}</b><p>{x}</p></li>' for t,x in ex['steps'][lang])
    for kk in list(d):
        if isinstance(d[kk],list): del d[kk]
    return d

JS='''/* ===== ACTIVITY PAGES ===== */
document.querySelectorAll('.yr').forEach(e=>e.textContent=new Date().getFullYear());
function updateBook(){
  document.querySelectorAll('.js-book').forEach(b=>{
    const t=T[LANG],name=t[b.dataset.act+'_t']||'';
    b.href='https://wa.me/'+WA+'?text='+encodeURIComponent(t.bk_msg+' '+name.replace(/<[^>]+>/g,''));
  });
}
document.querySelectorAll('.itin-btn').forEach(b=>b.addEventListener('click',()=>{const it=b.closest('.itin');const o=it.classList.toggle('open');b.setAttribute('aria-expanded',o)}));
const _applyLang=applyLang;
applyLang=function(l){_applyLang(l);updateBook()};

'''
