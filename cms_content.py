# Content added from the dashboard (Pages CMS): content/tours/*.json and content/blog/*.json
# are turned into the same data structures as the hand-written tours and articles, so they
# get the same page design, home cards, search, sitemap and Chinese translation.
import json, glob, os, re, html, hashlib, datetime

LANGS = ['en', 'es', 'fr', 'it']
ALL = LANGS + ['zh']
CITIES = ['marrakech', 'fes', 'tangier', 'casablanca', 'errachidia', 'ouarzazate', 'agadir', 'daytrip', 'special']
PLACE_ZH = {'Agadir': '阿加迪尔', 'Agafay': '阿加菲', 'Agdz': '阿格兹', 'Ait Ben Haddou': '阿伊特本哈杜', 'Alnif': '阿尔尼夫', 'Asilah': '艾西拉', 'Azrou': '阿兹鲁', 'Beni Mellal': '贝尼迈拉勒', 'Cape Spartel': '斯帕特尔角', 'Casablanca': '卡萨布兰卡', 'Chefchaouen': '舍夫沙万', 'Dades Valley': '达德斯河谷', 'Erfoud': '埃尔富德', 'Erg Chigaga': '契加加沙丘', 'Errachidia': '埃尔拉希迪亚', 'Essaouira': '索维拉', 'Fes': '非斯', 'Foum Zguid': '福姆兹吉德', 'Ifrane': '伊夫兰', 'Jorf': '焦尔夫', "Kelaat M'Gouna": '凯拉特姆古纳', "M'hamid": '姆哈米德', 'Marrakech': '马拉喀什', 'Meknes': '梅克内斯', 'Merzouga': '梅尔祖卡', 'Midelt': '米德尔特', 'Moulay Yacoub': '穆莱雅各布', "N'Kob": '恩科布', 'Ouarzazate': '瓦尔扎扎特', 'Ouzoud': '乌祖德', 'Rabat': '拉巴特', 'Rissani': '里萨尼', 'Rose Valley': '玫瑰谷', 'Setti Fatma': '塞蒂法特玛', 'Skoura': '斯库拉', 'Tafraoute Sidi Ali': '塔夫拉乌特西迪阿里', 'Taghazout': '塔哈佐特', 'Tagounite': '塔古尼特', 'Taliouine': '塔利温', 'Tamegroute': '塔姆格鲁特', 'Tangier': '丹吉尔', 'Taroudant': '塔鲁丹特', 'Taznakht': '塔兹纳赫特', 'Tetouan': '得土安', 'Tinghir': '廷吉尔', "Tizi n'Tichka": '提济恩提什卡山口', 'Tnine Ourika': '特宁乌里卡', 'Todra Gorge': '托德拉峡谷', 'Volubilis': '沃吕比利斯', 'Zagora': '扎戈拉'}
TAGS = ['planning', 'desert', 'cities', 'culture', 'coast', 'family', 'tips']

# ---- known places on the hand-drawn map (x, y in map units) ----
def places(TR):
    P = {}
    for e in TR.EXTRA_T.values():
        for s in e.get('stops2', []):
            n = s[0].replace('’', "'")
            if n == 'Nkob': n = "N'Kob"
            P.setdefault(n, (s[1], s[2]))
    P.pop('Argan coop', None)
    return dict(sorted(P.items()))

def _l(d, l):
    """value for language l, falling back to English"""
    if isinstance(d, str): return d
    d = d or {}
    v = (d.get(l) or '').strip()
    return v if v else (d.get('en') or '').strip()

def _slug(s):
    s = re.sub(r'[^a-z0-9]+', '-', (s or '').lower()).strip('-')
    return s[:70] or 'item'

def _inline(s):
    """light markdown: **bold**, *italic*, [text](url)"""
    s = html.escape(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'(?<!\*)\*(?!\s)(.+?)(?<!\s)\*(?!\*)', r'<i>\1</i>', s)
    s = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', lambda m: f'<a href="{m.group(2)}"' + ('' if m.group(2).endswith('.html') or m.group(2).startswith('#') else ' target="_blank" rel="noopener"') + f'>{m.group(1)}</a>', s)
    return s

def _paras(text):
    return [_inline(' '.join(p.split())) for p in re.split(r'\n\s*\n', text or '') if p.strip()]

def _lines(text):
    return [_inline(x.strip().lstrip('-•* ').strip()) for x in (text or '').splitlines() if x.strip()]

# ---- images uploaded from the dashboard: resized and converted to webp ----
def image(path, A, pos=None):
    """returns an {{IMG_id}} token for an uploaded image, registering it like the built-in photos"""
    if isinstance(path, list): path = path[0] if path else None
    if not path: return None
    p = path.lstrip('/')
    if not os.path.exists(p): print('cms: missing image', p); return None
    base = 'u-' + _slug(os.path.splitext(os.path.basename(p))[0]) + '-' + hashlib.md5(p.encode()).hexdigest()[:6]
    out = f'images/{base}.webp'
    if not os.path.exists(out) or os.path.getmtime(out) < os.path.getmtime(p):
        from PIL import Image, ImageOps
        im = ImageOps.exif_transpose(Image.open(p)).convert('RGB')
        if im.width > 2000: im = im.resize((2000, round(im.height * 2000 / im.width)), Image.LANCZOS)
        im.save(out, 'webp', quality=80, method=6)
    A.PHOTOS.setdefault(base, {'pos': pos or '50% 50%', 'alt': ''})
    return '{{IMG_' + base + '}}'

def _read(folder):
    out = []
    for f in sorted(glob.glob(f'content/{folder}/*.json')):
        try:
            d = json.load(open(f, encoding='utf8'))
        except Exception as e:
            print('cms: cannot read', f, e); continue
        if d.get('published') is False: continue
        d['_file'] = os.path.splitext(os.path.basename(f))[0]
        out.append(d)
    return out

REG = {l: {} for l in ALL}   # translation keys created for dashboard content

def _reg(key, val):
    for l in ALL: REG[l][key] = _l(val, l) if not isinstance(val, str) else val

STAT = {'cms_st_n': {'en': 'nights', 'es': 'noches', 'fr': 'nuits', 'it': 'notti', 'zh': '晚'},
        'cms_st_s': {'en': 'stops on the way', 'es': 'etapas en el camino', 'fr': 'étapes en chemin', 'it': 'tappe lungo il percorso', 'zh': '沿途站点'},
        'cms_st_p': {'en': 'private tour with your own driver', 'es': 'circuito privado con tu propio conductor', 'fr': 'circuit privé avec votre chauffeur', 'it': 'tour privato con il tuo autista', 'zh': '私人专车之旅'},
        'cms_start': {'en': 'Start', 'es': 'Salida', 'fr': 'Départ', 'it': 'Partenza', 'zh': '起点'},
        'cms_end': {'en': 'End', 'es': 'Llegada', 'fr': 'Arrivée', 'it': 'Arrivo', 'zh': '终点'},
        'cms_dash': '—'}
for _k, _v in STAT.items(): _reg(_k, _v)
DAYW = {'en': 'Day', 'es': 'Día', 'fr': 'Jour', 'it': 'Giorno', 'zh': '第{n}天'}

def _dayword(l, n): return DAYW[l].format(n=n) if '{n}' in DAYW[l] else f'{DAYW[l]} {n}'

# ---------------- tours ----------------
def load_tours(TR, A):
    P = places(TR)
    added = []
    for d in _read('tours'):
        days = d.get('itinerary') or []
        if not d.get('title') or not _l(d.get('title'), 'en') or not days:
            print('cms: tour skipped (needs a title and at least one day):', d['_file']); continue
        tid = 'tour-' + _slug(d.get('slug') or d['_file']).replace('tour-', '', 1)
        if any(t['id'] == tid for t in TR.TOURS):
            print('cms: tour id already used:', tid); continue
        k = 'cm' + hashlib.md5(tid.encode()).hexdigest()[:6]
        city = d.get('city') if d.get('city') in CITIES else 'special'
        n = len(days)
        # stops: the places of every day, in order, joined day to day
        seq, didx = [], []
        for dd in days:
            pl = dd.get('places') or []
            if isinstance(pl, str): pl = [x.strip() for x in pl.split(',')]
            names = [x for x in pl if x in P]
            if seq and (not names or names[0] != seq[-1]): names = [seq[-1]] + names
            idx = []
            for j, nm in enumerate(names):
                if j == 0 and seq and nm == seq[-1]: idx.append(len(seq) - 1); continue
                seq.append(nm); idx.append(len(seq) - 1)
            didx.append(idx if len(idx) > 1 else [])
        if len(seq) < 2:
            seq = [x for x in [d.get('start'), d.get('end')] if x in P] or ['Marrakech']
            if len(seq) == 1: seq = seq * 2
            didx = [[0, len(seq) - 1]]
        didx = [x for x in didx if x]
        stops2 = []
        for i, nm in enumerate(seq):
            x, y = P[nm]
            if i == 0: key, big = 'cms_start', 1
            elif i == len(seq) - 1: key, big = 'cms_end', 1
            else:
                dayn = next((j + 1 for j, ix in enumerate(didx) if ix and ix[-1] == i), None)
                key = f'{k}_s{i}'; big = 1 if dayn else 0
                _reg(key, {l: (_dayword(l, dayn) if dayn else '') for l in ALL})
            nx = P[seq[i + 1]][0] if i + 1 < len(seq) else P[seq[i - 1]][0]
            stops2.append([nm, x, y, key, big, 'l' if nx > x else 'r'])
        title = d['title']
        route = d.get('route') if _l(d.get('route'), 'en') else {l: ' · '.join(PLACE_ZH.get(x, x) if l == 'zh' else x for x in seq) for l in ALL}
        start = d.get('start') or seq[0]; end = d.get('end') or seq[-1]
        t = {'id': tid, 'k': k, 'city': city, 'days': n, 'art': 'mquad', '_cms': True,
             't': {}, 's': {}, 'start': {}, 'end': {}, 'o': {}, 'inc': {}, 'exc': {}, 'route': {}, 'steps': {}}
        if city == 'daytrip': t['dtrip'] = True
        meta = []
        for i, dd in enumerate(days):
            a, b = f'{k}_m{i}a', f'{k}_m{i}b'
            _reg(a, dd.get('sleep') if _l(dd.get('sleep'), 'en') else '—')
            _reg(b, dd.get('meals') if _l(dd.get('meals'), 'en') else '—')
            meta.append((a, b))
        _TX[tid] = {'d': d, 'route': route, 'start': start, 'end': end}
        hl = {l: ''.join(f'<li>{x}</li>' for x in (_lines(_l(d.get('highlights'), l)) or [PLACE_ZH.get(x, x) if l == 'zh' else x for x in dict.fromkeys(seq)])) for l in ALL}
        _reg(k + '_hl', hl)
        _fill_tour(t, 'en_as', None)
        hero = image(d.get('hero'), A, d.get('hero_position')) or '{{IMG_hero-riad}}'
        gal = []
        for gi, g in enumerate(d.get('gallery') or []):
            src = image(g.get('image') if isinstance(g, dict) else g, A)
            if not src: continue
            ck = f'{k}_g{gi}'; _reg(ck, (g.get('caption') if isinstance(g, dict) else None) or '')
            gal.append([src, ck, '50% 50%'])
        if not gal: gal = [[hero, f'{k}_g0', '50% 50%']]; _reg(f'{k}_g0', title)
        q = lambda s: s.replace(' ', '+').replace("'", '')
        gm = 'https://www.google.com/maps/dir/' + '/'.join(q(s) for s in seq)
        ge = ('https://maps.google.com/maps?saddr=' + q(seq[0]) + ',+Morocco&daddr=' +
              '+to:'.join(q(s) + ',+Morocco' for s in seq[1:]) + '&output=embed')
        north = city in ('tangier', 'fes', 'casablanca')
        TR.EXTRA_T[tid] = {'hero_src': (hero, d.get('hero_position') or '50% 50%'),
                           'stats2': [(str(n), 'st_days'), (str(max(n - 1, 0)), 'cms_st_n'), (str(len(seq)), 'cms_st_s'), ('100%', 'cms_st_p')],
                           'gallery': gal, 'stops2': stops2, 'days_idx': didx,
                           'bends': [(.12 if i % 2 == 0 else -.12) for i in range(len(didx))],
                           'meta': meta, 'deco': 'north' if north else 'chigaga', 'gmaps': gm, 'gembed': ge}
        TR.TOURS.append(t); added.append(tid)
    if added:
        _wrap(TR)
    print('cms tours:', ', '.join(added) or 'none')
    return added

_TX = {}

def _fill_tour(t, mode, _):
    """fill the tour's language fields; mode 'zh' puts the Chinese text in the 'en' slot (to build the translation memory)"""
    x = _TX[t['id']]; d = x['d']
    for l in LANGS:
        s = 'zh' if (mode == 'zh' and l == 'en') else l
        t['t'][l] = _l(d.get('title'), s)
        t['s'][l] = _l(d.get('summary'), s)
        t['start'][l] = _l(x['start'], s) if isinstance(x['start'], dict) else x['start']
        t['end'][l] = _l(x['end'], s) if isinstance(x['end'], dict) else x['end']
        t['route'][l] = _l(x['route'], s)
        t['o'][l] = _paras(_l(d.get('overview'), s)) or [t['s'][l]]
        t['inc'][l] = _lines(_l(d.get('included'), s))
        t['exc'][l] = _lines(_l(d.get('not_included'), s))
        t['steps'][l] = [(_inline(_l(dd.get('title'), s)) or f'{_dayword(s, i + 1)}', '</p><p>'.join(_paras(_l(dd.get('text'), s))))
                         for i, dd in enumerate(d.get('itinerary') or [])]

def _wrap(TR):
    if getattr(TR, '_cms_wrapped', False): return
    TR._cms_wrapped = True
    _orig = TR.tdict2
    def tdict2(lang):
        reg = REG['zh' if _SWAP[0] and lang == 'en' else lang]
        TR.G2[lang].update(reg)          # day labels (sleep / meals) are read from G2
        dd = _orig(lang); dd.update(reg); return dd
    TR.tdict2 = tdict2

_SWAP = [False]

# ---------------- blog ----------------
def _body(text):
    secs, cur = [], [None, []]
    para = []
    def flush():
        if para: cur[1].append(' '.join(para)); para.clear()
    for raw in (text or '').splitlines():
        ln = raw.strip()
        if ln.startswith('#'):
            flush()
            if cur[0] or cur[1]: secs.append(cur)
            cur = [_inline(ln.lstrip('#').strip()), []]
        elif not ln: flush()
        elif ln.startswith(('- ', '* ', '• ')): flush(); cur[1].append('- ' + _inline(ln[2:].strip()))
        elif ln.startswith('>'): flush(); cur[1].append('> ' + _inline(ln.lstrip('> ').strip()))
        else: para.append(_inline(ln))
    flush()
    if cur[0] or cur[1]: secs.append(cur)
    return secs

_BX = {}

def load_blog(BD, A):
    added = []
    new = []
    for d in _read('blog'):
        if not _l(d.get('title'), 'en') or not _l(d.get('body'), 'en'):
            print('cms: article skipped (needs a title and a text):', d['_file']); continue
        aid = 'blog-' + _slug(d.get('slug') or d['_file']).replace('blog-', '', 1)
        if any(a['id'] == aid for a in BD.ARTICLES):
            print('cms: article id already used:', aid); continue
        img = image(d.get('image'), A)
        a = {'id': aid, 'img': img[6:-2] if img else 'caravan-dusk', 'tag': d.get('tag') if d.get('tag') in TAGS else 'tips',
             't': {}, 'x': {}, 'b': {}, 'date': str(d.get('date') or datetime.date.today().isoformat())[:10], '_cms': True}
        _BX[aid] = d
        _fill_art(a, 'en_as')
        w = len(' '.join(p for _, ps in a['b']['en'] for p in ps).split()); a['mins'] = max(2, round(w / 200))
        new.append(a); added.append(aid)
    # newest first, before the older articles
    allarts = sorted(new + BD.ARTICLES, key=lambda a: a['date'], reverse=True) if new else BD.ARTICLES
    BD.ARTICLES[:] = allarts
    print('cms articles:', ', '.join(added) or 'none')
    return added

def _fill_art(a, mode):
    d = _BX[a['id']]
    en = _body(_l(d.get('body'), 'en'))
    for l in LANGS:
        src = 'zh' if (mode == 'zh' and l == 'en') else l
        a['t'][l] = _l(d.get('title'), src)
        a['x'][l] = _l(d.get('excerpt'), src) or _l(d.get('title'), src)
        b = _body(_l(d.get('body'), src))
        a['b'][l] = b if len(b) == len(en) else en   # a translation with a different layout falls back to English

# ---------------- Chinese translation memory for dashboard content ----------------
def zh_memory(TR, BL, BD):
    tm = {}
    def diff(fn, swap):
        base = fn('en'); swap(True); z = fn('en'); swap(False)
        for kk, v in base.items():
            zv = z.get(kk)
            if isinstance(v, str) and isinstance(zv, str) and zv != v and v.strip(): tm[v] = zv
    def sw_t(on):
        _SWAP[0] = on
        for t in TR.TOURS:
            if t.get('_cms'): _fill_tour(t, 'zh' if on else 'en_as', None)
    def sw_b(on):
        for a in BD.ARTICLES:
            if a.get('_cms'): _fill_art(a, 'zh' if on else 'en_as')
    if any(t.get('_cms') for t in TR.TOURS): diff(TR.tdict2, sw_t)
    if any(a.get('_cms') for a in BD.ARTICLES): diff(BL.tdict, sw_b)
    os.makedirs('zh_tm', exist_ok=True)
    json.dump(tm, open('zh_tm/zz_cms.json', 'w', encoding='utf8'), ensure_ascii=False)
    return len(tm)
