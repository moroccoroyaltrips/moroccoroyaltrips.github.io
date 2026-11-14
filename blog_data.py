# Blog articles aggregated from blog_a1..a8 (4 languages each).
import importlib, datetime
import blog_a1,blog_a2,blog_a3,blog_a4,blog_a5,blog_a6,blog_a7,blog_a8
_M=[blog_a1,blog_a2,blog_a3,blog_a4,blog_a5,blog_a6,blog_a7,blog_a8]
for _m in _M: importlib.reload(_m)
_ALL={a['id']:a for m in _M for a in m.ARTS}
ORDER=['blog-first-trip-morocco','blog-best-time-sahara','blog-marrakech-two-days','blog-night-desert-camp','blog-fes-medina-guide',
 'blog-moroccan-food-guide','blog-merzouga-vs-chigaga','blog-chefchaouen-guide','blog-day-trips-marrakech','blog-morocco-etiquette',
 'blog-road-of-kasbahs','blog-what-to-pack-desert','blog-essaouira-guide','blog-morocco-with-kids','blog-morocco-practical-tips']
ARTICLES=[_ALL[i] for i in ORDER]+[a for i,a in _ALL.items() if i not in ORDER]
_d=datetime.date(2026,11,3)
for n,a in enumerate(ARTICLES):
    a.setdefault('date',(_d-datetime.timedelta(days=3*n)).isoformat())
    w=len(' '.join(p for _,ps in a['b']['en'] for p in ps).split())
    a['mins']=max(3,round(w/200))
