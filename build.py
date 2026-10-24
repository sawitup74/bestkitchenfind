import json,html,re,glob,zlib
CDN="https://cdn.shopify.com/s/files/1/0721/8833/0172/files/"
IMG={k:CDN+v for k,v in dict(c07="compact-07.jpg?v=1792382833",c28="compact-28.jpg?v=1792382861",c08="compact-08.jpg?v=1792382834",c13="compact-13.jpg?v=1792382834",both16="both-16.jpg?v=1792382825",both02="both-02.jpg?v=1792382824",full01="full-size-01.jpg?v=1792382862",full08="full-size-08.jpg?v=1792382863",full10="full-size-10.jpg?v=1792382864",full13="full-size-13.jpg?v=1792382866",pl0="zz_slot-grill-griddle-add-on-white.jpg?v=1792382974",pl1="zz_Slot_Grill_Plancha_1.jpg?v=1792382973",pl2="zz_Slot_Grill_Plancha_2.jpg?v=1792382973",balm="seasoning-balm-main.jpg?v=1791978819",thermo="thermometer-red-clean.jpg?v=1791939312",thermo2="thermometer-rinse-water.jpg?v=1791939206").items()}
SG="https://slotgrill.com"
COMPACT=SG+"/products/slot-grill-compact-carbon-steel-free-shipping"
FULL=SG+"/products/slot-grill-carbon-steel-collapsible-bbq-grill"
GRID=SG+"/products/slot-grill-griddle-plancha"
BALM=SG+"/products/seasoning-balm-for-slot-grill"
THERMO=SG+"/products/slot-grill-instant-read-digital-meat-thermometer"
BUNDLE=SG+"/products/seasoning-balm-meat-thermometer-bundle"
DOMAIN="https://bestkitchenfind.com"
SITE="Best Kitchen Find"
CSS="""
:root{--coal:#16151a;--coal2:#24222a;--tom:#e63b2e;--mus:#f4b81c;--cream:#fff4e0;--paper:#fffaf1;--ink:#1b1a1f;--mute:#6a6470;--line:#e9dcc4}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}body{margin:0;font:18px/1.72 system-ui,-apple-system,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;color:var(--ink);background:var(--paper)}
h1,h2,h3,.brand,.kick,.btn,nav,.num{font-family:'Arial Black','Helvetica Neue',Impact,system-ui,sans-serif;letter-spacing:-.02em}
a{color:var(--tom)}img{max-width:100%;height:auto;display:block}
.bar{background:var(--mus);color:var(--coal);text-align:center;font:700 13px/1.4 system-ui,sans-serif;padding:.45rem 1rem;letter-spacing:.06em;text-transform:uppercase}.bar a{color:var(--coal)}
.top{background:var(--coal);position:sticky;top:0;z-index:5}
.top .in{max-width:1240px;margin:auto;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;padding:.7rem 1rem;gap:.5rem}
.brand{color:#fff;text-decoration:none;font-size:1.35rem;text-transform:uppercase;line-height:1}.brand i{font-style:normal;color:var(--tom)}.brand b{color:var(--mus)}
nav{display:flex;flex-wrap:wrap;gap:.2rem .9rem}nav a{color:#f3ead8;text-decoration:none;font-size:.8rem;text-transform:uppercase;letter-spacing:.04em}nav a:hover{color:var(--mus)}
.kick{display:inline-block;background:var(--tom);color:#fff;font-size:.72rem;text-transform:uppercase;letter-spacing:.14em;padding:.25rem .6rem}
.kick.m{background:var(--mus);color:var(--coal)}
.hero{background:var(--coal);color:#fff;overflow:hidden;position:relative}
.hero:before{content:"";position:absolute;right:-10%;top:-30%;width:60%;height:160%;background:var(--tom);transform:rotate(12deg)}
.hero .in{position:relative;max-width:1240px;margin:auto;padding:3.5rem 1rem 4rem;display:grid;grid-template-columns:1.25fr 1fr;gap:2rem;align-items:center}
.hero h1{font-size:clamp(2.6rem,7.4vw,5.6rem);line-height:.92;margin:.6rem 0 1.1rem;text-transform:uppercase}.hero h1 em{font-style:normal;color:var(--mus)}
.hero p{font-size:1.15rem;max-width:600px;color:#e9e1d3}
.hero figure{margin:0;background:var(--mus);padding:12px;transform:rotate(-2.5deg);box-shadow:16px 16px 0 var(--coal2)}.hero figure img{aspect-ratio:4/3;object-fit:cover}
.hero figcaption{font:800 .8rem/1.3 system-ui;color:var(--coal);padding-top:.5rem;text-transform:uppercase;letter-spacing:.08em}
.btn{display:inline-block;background:var(--tom);color:#fff!important;text-decoration:none;font-size:.95rem;text-transform:uppercase;padding:.8rem 1.15rem;margin:.35rem .45rem .35rem 0;border:3px solid var(--tom);transition:transform .15s}.btn:hover{transform:translate(-2px,-2px);box-shadow:4px 4px 0 var(--coal)}
.btn.y{background:var(--mus);border-color:var(--mus);color:var(--coal)!important}.btn.o{background:transparent;border-color:currentColor;color:inherit!important}
.sec{max-width:1240px;margin:auto;padding:2.5rem 1rem}
.sec h2.big{font-size:clamp(2rem,5vw,3.4rem);line-height:.95;text-transform:uppercase;margin:0 0 1.2rem}.sec h2.big span{color:var(--tom)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:1.3rem}
.card{background:#fff;border:3px solid var(--coal);text-decoration:none;color:var(--ink);display:flex;flex-direction:column;transition:transform .15s}.card:hover{transform:translate(-3px,-3px);box-shadow:7px 7px 0 var(--tom)}
.card img{aspect-ratio:16/10;object-fit:cover;border-bottom:3px solid var(--coal)}.card div{padding:.9rem 1rem 1.1rem}.card h3{margin:.45rem 0 .35rem;font-size:1.15rem;line-height:1.15}.card p{margin:0;font-size:.92rem;color:var(--mute);line-height:1.5}
.cats{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:0;border:3px solid var(--coal)}
.cats a{padding:1.2rem;text-decoration:none;color:var(--ink);border:1.5px solid var(--coal);background:var(--cream)}.cats a:nth-child(3n+1){background:var(--mus)}.cats a:nth-child(3n+2){background:#fff}
.cats .num{font-size:2.4rem;line-height:1;color:var(--tom)}.cats b{display:block;font-family:'Arial Black',system-ui;font-size:1.05rem;margin:.3rem 0}.cats span{font-size:.88rem;color:#3a3640}
.band{background:var(--tom);color:#fff}.band .sec{display:grid;grid-template-columns:1fr 1fr;gap:2rem;align-items:center}.band img{border:6px solid #fff;aspect-ratio:4/3;object-fit:cover}.band h2{font-size:clamp(2rem,4.6vw,3.2rem);line-height:.95;text-transform:uppercase;margin:.4rem 0 .8rem}
.wrap{max-width:1240px;margin:auto;padding:1.5rem 1rem;display:grid;grid-template-columns:minmax(0,1fr) 310px;gap:2.6rem}.wrap.full{grid-template-columns:minmax(0,860px);justify-content:center}
.ahead{background:var(--coal);color:#fff}.ahead .in{max-width:1240px;margin:auto;padding:2.2rem 1rem 2.4rem}
.ahead h1{font-size:clamp(2.1rem,5.6vw,4rem);line-height:.98;margin:.6rem 0 .8rem;max-width:980px;text-transform:uppercase}.ahead .lede{font-size:1.2rem;color:#eadfca;max-width:760px;margin:0}
.crumbs{font-size:.8rem;color:#bdb3a3;text-transform:uppercase;letter-spacing:.06em}.crumbs a{color:var(--mus);text-decoration:none}
.meta{font-size:.85rem;color:#bdb3a3;margin-top:.8rem}
.heroimg{border:3px solid var(--coal);box-shadow:10px 10px 0 var(--mus);margin:.4rem 0 1.6rem;aspect-ratio:16/9;object-fit:cover;width:100%}
article h2{font-size:clamp(1.5rem,3vw,2.05rem);line-height:1.1;margin:2.4rem 0 .7rem;padding-top:.8rem;border-top:5px solid var(--coal)}
article h3{font-size:1.2rem;margin:1.6rem 0 .3rem}
article li{margin:.3rem 0}
.tip{background:var(--cream);border-left:8px solid var(--mus);padding:.9rem 1.1rem;font-size:.97rem}
.callout{margin:2.2rem 0;background:var(--coal);color:#fff;display:grid;grid-template-columns:230px 1fr;border:4px solid var(--coal);box-shadow:9px 9px 0 var(--tom)}
.callout img{height:100%;object-fit:cover;background:#fff}.callout div{padding:1.1rem 1.3rem}.callout h3{margin:.5rem 0 .4rem;font-size:1.45rem;line-height:1.08;color:var(--mus);text-transform:uppercase}.callout p{color:#ece3d4;font-size:.98rem;margin:.2rem 0 .6rem}
.duo{margin:2.2rem 0;display:grid;grid-template-columns:1fr 1fr;gap:1.1rem}.duo a{background:var(--mus);color:var(--coal);text-decoration:none;border:3px solid var(--coal);padding:.9rem;display:block;font-size:.93rem;line-height:1.45}.duo a+a{background:var(--cream)}.duo img{aspect-ratio:4/3;object-fit:cover;margin-bottom:.6rem;border:3px solid var(--coal)}.duo b{font-family:'Arial Black',system-ui;font-size:1.05rem}
aside .box{background:var(--cream);border:3px solid var(--coal);padding:1.1rem;position:sticky;top:5rem}aside h3{margin:0 0 .5rem;text-transform:uppercase;font-size:1rem}aside ul{padding-left:1.1rem;margin:.3rem 0 1rem}aside li{font-size:.92rem;line-height:1.4;margin:.4rem 0}aside img{border:3px solid var(--coal);margin:.4rem 0 .6rem}
table{border-collapse:collapse;width:100%;font-size:.93rem;background:#fff;margin:1rem 0}td,th{border:2px solid var(--coal);padding:.5rem .65rem;text-align:left;vertical-align:top}th{background:var(--mus)}
.tw{overflow-x:auto}
.faq h3{background:var(--cream);padding:.6rem .8rem;border-left:8px solid var(--tom)}
footer{background:var(--coal);color:#cfc6b6;margin-top:3rem;font-size:.9rem;line-height:1.6;border-top:10px solid var(--mus)}footer .in{max-width:1240px;margin:auto;padding:2.2rem 1rem}footer a{color:var(--mus)}footer .brand{font-size:1.8rem}
@media(max-width:900px){.hero .in,.band .sec{grid-template-columns:1fr}.hero:before{width:120%;right:-60%}.wrap{grid-template-columns:1fr}.callout{grid-template-columns:1fr}.callout img{max-height:240px;width:100%}.duo{grid-template-columns:1fr}aside .box{position:static}.top{position:static}}
"""
CATS={"grill":("grill-recipes","Grill Recipes","Charcoal-kissed mains, sides and weeknight wins straight off the grate."),
"griddle":("griddle-and-skillet","Griddle &amp; Skillet","Flat-top breakfasts, smash burgers, fried rice and cast-iron cooking over coals."),
"tech":("technique","Technique School","Heat zones, charcoal, searing, temperatures and the why behind them."),
"care":("carbon-steel-care","Carbon Steel Care","Seasoning, cleaning, rust rescue and storage for raw steel."),
"party":("cookouts-and-entertaining","Cookouts &amp; Entertaining","Backyard parties, tailgates, crowd math and game plans."),
"gift":("gift-guides","Gift Guides","Presents for cooks, dads, grads and holiday lists that actually get used."),
"pantry":("pantry-rubs-marinades","Pantry, Rubs &amp; Marinades","Spice blends, brines, sauces and the shelf that makes cooking easy.")}
PAGES=[]
def md(t):
    out=[]
    for blk in re.split(r"\n\s*\n",t.strip()):
        b=blk.strip()
        if b.startswith("<"): out.append(b);continue
        if b.startswith("## "): out.append(f"<h2>{b[3:]}</h2>");continue
        if b.startswith("### "): out.append(f"<h3>{b[4:]}</h3>");continue
        if b.startswith("| "):
            rows=[[c.strip() for c in r.strip().strip("|").split("|")] for r in b.split("\n") if r.strip() and not set(r.strip())<=set("|- ")]
            out.append('<div class="tw"><table><tr>'+"".join(f"<th>{c}</th>" for c in rows[0])+"</tr>"+"".join("<tr>"+"".join(f"<td>{c}</td>" for c in r)+"</tr>" for r in rows[1:])+"</table></div>");continue
        if b.startswith("- ") or b.startswith("1. "):
            tag="ol" if b.startswith("1. ") else "ul"
            items=[re.sub(r"^(- |\d+\. )","",x) for x in b.split("\n") if x.strip()]
            out.append(f"<{tag}>"+"".join(f"<li>{x}</li>" for x in items)+f"</{tag}>");continue
        if b.startswith("! "): out.append(f'<p class="tip">{b[2:]}</p>');continue
        out.append(f"<p>{b}</p>")
    o=re.sub(r"\*\*(.+?)\*\*",r"<b>\1</b>","\n".join(out))
    return re.sub(r"\[([^\]]+)\]\(([a-z0-9-]+\.html)\)",r'<a href="/\2">\1</a>',o)
def A(slug,title,desc,cat,img,body,faq=None): PAGES.append((slug,title,desc,cat,IMG.get(img,img),body,faq or []))
# Call-outs. Product facts verified against slotgrill.com/products.json (Oct 2026). Copy is original.
CALLS=[
("Kitchen find of the year","The Slot Grill: our kitchen find of the year","Thick carbon steel plates that slide together by hand in under a minute, burn real charcoal, and pack flat enough to file next to your sheet pans. Made in Texas and sold only by the maker.",IMG["both02"],FULL,"Shop the Full Size · from $139.97"),
("Small kitchen, big fire","Apartment-sized cook, serious steel","The Compact gives you a 16.25\" × 9\" grate, weighs about 14 lb, and slides down to roughly an inch thick. It feeds one to three people and still holds a cast-iron pan without a wobble.",IMG["c07"],COMPACT,"See the Compact · from $79.97"),
("Feed the whole crew","Cooking for six? Go Full Size","10-gauge steel, 231 square inches of grate, and the coals ride 3⅝\" above whatever surface it stands on. Enough room for a two-zone fire, a skillet and a row of burgers at once.",IMG["full01"],FULL,"See the Full Size"),
("Flat-top upgrade","Turn half the grate into a griddle","The Slot Grill Griddle add-on is cut from the same heavy carbon steel and stacks flat with your grill. Run one plate beside the grate or two for a full flat-top. Fits Compact or Full Size; the grill itself is sold separately.",IMG["pl1"],GRID,"See griddle options"),
("Steel that lasts","Ten bucks of insurance for raw steel","Slot Grill Seasoning Balm blends avocado oil and beeswax. Wipe on a whisper-thin layer, give the steel an hour in a 400°F oven, then do it again; each pass leaves a darker, slicker shield on carbon steel or cast iron.",IMG["balm"],BALM,"Seasoning Balm · $8.97"),
("Stop guessing","A three-second answer to 'is it done?'","The Slot Grill Instant-Read Thermometer reads in about three seconds, is accurate to ±1.8°F, and has a backlit screen for after-dark cooks plus a magnetic back for the fridge door.",IMG["thermo"],THERMO,"Thermometer · $19.97"),
("Gift-ready pair","The stocking-stuffer two-pack","Seasoning Balm plus the instant-read thermometer in one bundle: one keeps the steel happy, the other keeps the chicken safe. An easy add-on for anyone who already owns a Slot Grill.",IMG["thermo2"],BUNDLE,"See the bundle · $28.94"),
]
def callout(i):
    t,h,p,img,url,cta=CALLS[i%len(CALLS)]
    return f'<div class="callout"><img src="{img}" alt="{html.escape(h)}" loading="lazy"><div><span class="kick m">{t}</span><h3>{h}</h3><p>{p}</p><a class="btn" href="{url}">{cta}</a></div></div>'
def duo():
    return f'<div class="duo"><a href="{COMPACT}"><img src="{IMG["c08"]}" alt="Slot Grill Compact" loading="lazy"><b>Slot Grill Compact · $79.97</b><br>12-gauge steel, about 14 lb, 146 sq in of grate, 1 to 3 eaters, packs about 1" thin.</a><a href="{FULL}"><img src="{IMG["full13"]}" alt="Slot Grill Full Size" loading="lazy"><b>Slot Grill Full Size · $139.97</b><br>10-gauge steel, about 27.6 lb, 231 sq in of grate, family cooks, packs about 1.25" thin.</a></div>'
def faqld(faq):
    if not faq: return ""
    return '<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]})+'</script>'
def crumbld(items):
    return '<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":html.unescape(n),"item":DOMAIN+u} for i,(n,u) in enumerate(items)]})+'</script>'
SHORT={"grill":"Recipes","griddle":"Griddle","tech":"Technique","care":"Steel Care","party":"Cookouts","gift":"Gifts","pantry":"Pantry"}
NAV="".join(f'<a href="/{CATS[k][0]}.html">{v}</a>' for k,v in SHORT.items())+'<a href="/faq.html">FAQ</a><a href="/about.html">About</a>'
def shell(title,desc,slug,inner,img=None,extra=""):
    canon=DOMAIN+("/" if slug=="index" else f"/{slug}.html")
    ld={"@context":"https://schema.org","@type":"WebSite" if slug=="index" else "Article","name":title,"headline":title,"url":canon,"image":img or IMG["both02"],"publisher":{"@type":"Organization","name":SITE}}
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}"><link rel="canonical" href="{canon}"><meta name="theme-color" content="#16151a">
<meta property="og:type" content="website"><meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:image" content="{img or IMG['both02']}"><meta property="og:url" content="{canon}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="preconnect" href="https://cdn.shopify.com"><link rel="stylesheet" href="/style.css"><script type="application/ld+json">{json.dumps(ld)}</script>{extra}</head><body>
<div class="bar">Kitchen find of the year: <a href="{FULL}">the Slot Grill</a> · collapsible carbon steel, made in Texas</div>
<header class="top"><div class="in"><a class="brand" href="/">Best<i>Kitchen</i><b>Find</b></a><nav>{NAV}</nav></div></header>
<main>{inner}</main>
<footer><div class="in"><p class="brand">Best<i>Kitchen</i><b>Find</b></p><p>Recipes, technique and gift ideas for home cooks, with one tool we keep coming back to: the Slot Grill. No ads, no tracking pixels, no sponsored lists. Every product link here points to <a href="{FULL}">SlotGrill.com</a>, which sells direct from the shop in Texas. Slot Grill® is a registered trademark.</p><p>{" · ".join(f'<a href="/{c[0]}.html">{c[1]}</a>' for c in CATS.values())} · <a href="/faq.html">FAQ</a> · <a href="/about.html">About</a></p><p style="font-size:.8rem">Food safety temperatures follow USDA guidance. Always grill outdoors with good ventilation and follow local burn rules.</p></div></footer></body></html>'''
def sidebar(slug,cat):
    rel=[p for p in DONE if p[3]==cat and p[0]!=slug][:7]
    c=CATS[cat]
    return f'<aside><div class="box"><h3>More {c[1]}</h3><ul>'+"".join(f'<li><a href="/{p[0]}.html">{html.escape(p[1])}</a></li>' for p in rel)+f'</ul><h3>The find</h3><img src="{IMG["c28"]}" alt="Slot Grill Compact burning charcoal" loading="lazy"><p style="font-size:.9rem;line-height:1.45">Flat-pack carbon steel that assembles by hand. Two sizes, one idea: real charcoal flavor without a bulky kettle.</p><a class="btn" href="{COMPACT}">Compact</a><a class="btn y" href="{FULL}">Full Size</a></div></aside>'
def wc(h): return len(re.sub("<[^>]+>"," ",h).split())
def card(p):
    return f'<a class="card" href="/{p[0]}.html"><img src="{p[4]}" alt="" loading="lazy"><div><span class="kick">{CATS[p[3]][1]}</span><h3>{html.escape(p[1])}</h3><p>{html.escape(p[2])}</p></div></a>'
def article(slug,title,desc,cat,img,body,faq):
    c=CATS[cat]; h=md(body); n=zlib.crc32(slug.encode())
    parts=h.split("<h2>")
    if len(parts)>4: h="<h2>".join(parts[:3])+callout(n)+"<h2>"+"<h2>".join(parts[3:])
    else: h+=callout(n)
    if len(parts)>8: h=h.replace("<h2>"+parts[7],callout(n+2)+"<h2>"+parts[7],1)
    fq=('<div class="faq"><h2>Quick questions</h2>'+"".join(f'<h3>{html.escape(q)}</h3><p>{html.escape(a)}</p>' for q,a in faq)+'</div>') if faq else ""
    w=wc(h+fq); mins=max(5,round(w/230))
    head=f'<section class="ahead"><div class="in"><p class="crumbs"><a href="/">Home</a> / <a href="/{c[0]}.html">{c[1]}</a></p><span class="kick">{c[1]}</span><h1>{html.escape(title)}</h1><p class="lede">{html.escape(desc)}</p><p class="meta">{mins} min read · Best Kitchen Find test kitchen</p></div></section>'
    inner=head+f'<div class="wrap"><article><img class="heroimg" src="{img}" alt="{html.escape(title)}">{h}{fq}{callout(n+4)}{duo()}</article>{sidebar(slug,cat)}</div>'
    return shell(title+" | "+SITE,desc,slug,inner,img,faqld(faq)+crumbld([("Home","/"),(c[1],f"/{c[0]}.html"),(title,f"/{slug}.html")])),w
EXTRA={}; XFAQ={}; FAQ=[]; ABOUT=""
for f in sorted(glob.glob("content_*.py")): exec(open(f).read())
PAGES=[(a,b,c,d,e,f+"\n\n"+EXTRA.get(a,""),g+XFAQ.get(a,[])) for a,b,c,d,e,f,g in PAGES]
open("style.css","w").write(CSS)
open("favicon.svg","w").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" fill="#16151a"/><rect x="10" y="28" width="44" height="8" fill="#e63b2e"/><rect x="10" y="42" width="44" height="8" fill="#f4b81c"/><rect x="10" y="14" width="44" height="8" fill="#fff4e0"/></svg>')
DONE=list(PAGES); WC={}
for p in PAGES:
    s,w=article(*p); open(p[0]+".html","w").write(s); WC[p[0]]=w
for i,(k,c) in enumerate(CATS.items()):
    ps=[p for p in DONE if p[3]==k]
    head=f'<section class="ahead"><div class="in"><p class="crumbs"><a href="/">Home</a> / {c[1]}</p><span class="kick">{len(ps)} stories</span><h1>{c[1]}</h1><p class="lede">{c[2]}</p></div></section>'
    inner=head+f'<div class="sec"><div class="grid">'+"".join(card(p) for p in ps)+'</div>'+callout(i)+duo()+'</div>'
    open(c[0]+".html","w").write(shell(html.unescape(c[1])+" | "+SITE,html.unescape(c[2]),c[0],inner,extra=crumbld([("Home","/"),(c[1],f"/{c[0]}.html")])))
head='<section class="ahead"><div class="in"><p class="crumbs"><a href="/">Home</a> / FAQ</p><span class="kick">Straight answers</span><h1>The Kitchen &amp; Cookout FAQ</h1><p class="lede">Charcoal, carbon steel, temperatures, gifting, and how the Slot Grill fits into a real home kitchen.</p></div></section>'
open("faq.html","w").write(shell("FAQ | "+SITE,"Answers about charcoal grilling, carbon steel care, food safety temperatures, and the Slot Grill Compact and Full Size.","faq",head+'<div class="wrap full"><article class="faq">'+"".join(f'<h3>{html.escape(q)}</h3><p>{html.escape(a)}</p>' for q,a in FAQ)+callout(0)+duo()+'</article></div>',extra=faqld(FAQ)+crumbld([("Home","/"),("FAQ","/faq.html")])))
head='<section class="ahead"><div class="in"><p class="crumbs"><a href="/">Home</a> / About</p><span class="kick">Who we are</span><h1>About Best Kitchen Find</h1><p class="lede">A small, ad-free food site built around cooking that gets people to the table.</p></div></section>'
open("about.html","w").write(shell("About | "+SITE,"Why Best Kitchen Find exists, how we test, and why the Slot Grill is the one product we point to.","about",head+'<div class="wrap full"><article><img class="heroimg" src="'+IMG["both16"]+'" alt="Slot Grill Compact and Full Size">'+md(ABOUT)+callout(0)+duo()+'</article></div>',extra=crumbld([("Home","/"),("About","/about.html")])))
cats="".join(f'<a href="/{c[0]}.html"><span class="num">{i+1:02d}</span><b>{c[1]}</b><span>{c[2]}</span></a>' for i,(k,c) in enumerate(CATS.items()))
feat=[p for p in DONE if p[3]=="grill"][:3]+[p for p in DONE if p[3]=="gift"][:1]+[p for p in DONE if p[3]=="griddle"][:2]
tech=[p for p in DONE if p[3] in("tech","care")][:6]
party=[p for p in DONE if p[3] in("party","pantry")][:6]
idx=f'''<section class="hero"><div class="in"><div><span class="kick m">Recipes · Technique · Gifts</span><h1>Cook loud. <em>Eat outside.</em> Feed everybody.</h1><p>A home-cook magazine for people who want dinner to taste like a cookout: charcoal recipes, griddle mornings, steel care, party game plans and gift guides. Starring the one find that earned a permanent spot in our kitchen.</p><a class="btn y" href="{FULL}">Meet the Slot Grill</a><a class="btn o" href="/grill-recipes.html">Get cooking</a></div><figure><img src="{IMG['both02']}" alt="Slot Grill Full Size and Compact carbon steel grills" fetchpriority="high"><figcaption>Kitchen find of the year · Slot Grill Full Size &amp; Compact</figcaption></figure></div></section>
<div class="sec"><h2 class="big">This week's <span>hot list</span></h2><div class="grid">{"".join(card(p) for p in feat)}</div></div>
<section class="band"><div class="sec"><img src="{IMG['c28']}" alt="Slot Grill Compact with glowing charcoal" loading="lazy"><div><span class="kick m">Kitchen find of the year</span><h2>One steel box. A thousand cookouts.</h2><p>The Slot Grill is a charcoal grill made of thick carbon steel plates that lock together with tabs and slots. No tools, no hinges, no bolts to lose. Build it in under a minute, cook, let it cool, and slide it flat into a closet. Full Size for family nights, Compact for small patios and road trips.</p><a class="btn y" href="{FULL}">Full Size · $139.97</a><a class="btn o" href="{COMPACT}">Compact · $79.97</a></div></div></section>
<div class="sec"><h2 class="big">Pick a <span>section</span></h2><div class="cats">{cats}</div></div>
<div class="sec"><h2 class="big">Technique &amp; <span>steel school</span></h2><div class="grid">{"".join(card(p) for p in tech)}</div>{callout(3)}</div>
<div class="sec"><h2 class="big">Party plans &amp; <span>pantry</span></h2><div class="grid">{"".join(card(p) for p in party)}</div>{duo()}</div>'''
open("index.html","w").write(shell("Best Kitchen Find: Grill Recipes, Cookout Plans & Gifts for Cooks","Bold recipes, grilling technique, carbon steel care, cookout planning and gift guides for home cooks, featuring the Slot Grill.","index",idx))
open("404.html","w").write(shell("Page not found | "+SITE,"That page is not on the menu.","404",'<section class="ahead"><div class="in"><h1>86’d: page not found</h1><p class="lede">That one is off the menu. Head back to the <a style="color:#f4b81c" href="/">front page</a>.</p></div></section>'))
urls=["/","/about.html","/faq.html"]+[f"/{c[0]}.html" for c in CATS.values()]+[f"/{p[0]}.html" for p in DONE]
open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"  <url><loc>{DOMAIN}{u}</loc><lastmod>2026-10-24</lastmod></url>\n" for u in urls)+"</urlset>\n")
open("robots.txt","w").write(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
json.dump(WC,open("wordcounts.json","w"),indent=0)
print(len(DONE),"articles",sum(WC.values()),"words; min",min(WC.values()) if WC else 0)
for k,v in WC.items():
    if v<1500: print("SHORT",k,v)
