# -*- coding: utf-8 -*-
"""Build the Final Fantasy IX digital magazine HTML file."""
import os

output_dir = r"C:\Users\Stella\Desktop\ffix-magazine"
output_file = os.path.join(output_dir, "index.html")

# We'll write the file in parts
parts = []

def add(s):
    parts.append(s)

# ============================================================
# HTML HEAD + CSS
# ============================================================
add(r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>最终幻想IX · 归处 — 数字专题杂志</title>
<meta name="description" content="一本关于《最终幻想IX》的中文数字杂志，涵盖游戏概览、开发幕后、世界观设定、人物介绍、主线剧情、游戏系统、评价与影响、图库与资料。">
<meta name="keywords" content="最终幻想9, Final Fantasy IX, FF9, Square Enix, 植松伸夫, 坂口博信, 伊藤裕之, 游戏杂志, 数字博物馆">
<meta property="og:title" content="最终幻想IX · 归处 — 数字专题杂志">
<meta property="og:description" content="一本关于《最终幻想IX》的中文数字杂志，出版级品质呈现PlayStation时代经典RPG。">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="">
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
--midnight:#0a0e1a;--midnight-light:#121832;--gold:#c8a84e;--gold-light:#e2c97e;--gold-dark:#9a7b2e;
--parchment:#f4eed7;--parchment-dark:#d9d0b3;--deep-green:#1a2e1a;--deep-green-light:#2a4a2a;
--crimson:#6b1a2a;--crimson-dark:#3d0f18;--crimson-light:#8b2a3a;--charcoal:#1a1a1a;
--wine:#4a1a2a;--wine-light:#6a2a3a;--blue-gray:#2a3a4a;--blue-gray-light:#3a4a5a;
--black-gold:#0a0a0a;--bg-hero:#050810;
--text-primary:#f0ece0;--text-secondary:#b0a890;--text-muted:#706858;
--font-serif:Georgia,'Noto Serif SC','Source Han Serif SC',SimSun,serif;
--font-sans:'Helvetica Neue','PingFang SC','Microsoft YaHei','Noto Sans SC',sans-serif;
--font-display:Georgia,'Noto Serif SC',serif;
--section-pad:clamp(3rem,8vw,8rem);--content-max:1200px;--content-wide:1400px;
}
html{scroll-behavior:smooth;font-size:16px;overflow-x:hidden}
body{font-family:var(--font-serif);color:var(--text-primary);background:var(--midnight);line-height:1.9;overflow-x:hidden;-webkit-font-smoothing:antialiased}
img{max-width:100%;height:auto;display:block}
a{color:var(--gold);text-decoration:none;transition:color .3s}
a:hover{color:var(--gold-light)}
::selection{background:var(--gold);color:var(--midnight)}
#progress-bar{position:fixed;top:0;left:0;height:3px;background:linear-gradient(90deg,var(--gold-dark),var(--gold),var(--gold-light));z-index:10000;transition:width .1s;width:0}
.nav-main{position:fixed;top:0;left:0;right:0;z-index:9999;transition:all .4s;padding:0}
.nav-main.scrolled{background:rgba(10,14,26,.92);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border-bottom:1px solid rgba(200,168,78,.15)}
.nav-inner{max-width:var(--content-wide);margin:0 auto;display:flex;align-items:center;justify-content:space-between;padding:.8rem 2rem}
.nav-logo{font-family:var(--font-display);font-size:1.1rem;color:var(--gold);letter-spacing:.15em;text-transform:uppercase;font-weight:400}
.nav-logo span{color:var(--text-muted);font-size:.75rem;display:block;letter-spacing:.3em;margin-top:2px}
.nav-links{display:flex;gap:0;list-style:none;flex-wrap:wrap}
.nav-links a{display:block;padding:.6rem 1rem;font-size:.8rem;color:var(--text-secondary);letter-spacing:.08em;transition:all .3s;border-bottom:2px solid transparent;text-transform:uppercase;font-family:var(--font-sans)}
.nav-links a:hover,.nav-links a.active{color:var(--gold);border-bottom-color:var(--gold)}
.nav-toggle{display:none;background:none;border:none;color:var(--gold);font-size:1.5rem;cursor:pointer;padding:.5rem}
.theme-toggle{background:none;border:1px solid rgba(200,168,78,.3);color:var(--gold);padding:.4rem .8rem;border-radius:20px;cursor:pointer;font-size:.75rem;letter-spacing:.1em;transition:all .3s;font-family:var(--font-sans)}
.theme-toggle:hover{background:var(--gold);color:var(--midnight)}
.toc-sidebar{position:fixed;right:1.5rem;top:50%;transform:translateY(-50%);z-index:9998;display:flex;flex-direction:column;gap:8px;align-items:flex-end}
.toc-sidebar a{display:flex;align-items:center;gap:8px;text-decoration:none;transition:all .3s}
.toc-sidebar a .toc-dot{width:8px;height:8px;border-radius:50%;background:rgba(200,168,78,.3);transition:all .3s;flex-shrink:0}
.toc-sidebar a .toc-label{font-size:.65rem;color:var(--text-muted);opacity:0;transform:translateX(5px);transition:all .3s;white-space:nowrap;letter-spacing:.1em;text-transform:uppercase;font-family:var(--font-sans)}
.toc-sidebar a:hover .toc-label,.toc-sidebar a.active .toc-label{opacity:1;transform:translateX(0)}
.toc-sidebar a:hover .toc-dot,.toc-sidebar a.active .toc-dot{background:var(--gold);width:10px;height:10px;box-shadow:0 0 12px rgba(200,168,78,.5)}
#back-top{position:fixed;bottom:2rem;right:2rem;z-index:9998;width:44px;height:44px;border-radius:50%;background:rgba(200,168,78,.15);border:1px solid rgba(200,168,78,.3);color:var(--gold);cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:1.2rem;opacity:0;pointer-events:none;transition:all .4s;backdrop-filter:blur(10px)}
#back-top.visible{opacity:1;pointer-events:all}
#back-top:hover{background:var(--gold);color:var(--midnight)}
.lightbox-overlay{position:fixed;inset:0;background:rgba(0,0,0,.92);z-index:10001;display:none;align-items:center;justify-content:center;cursor:zoom-out;backdrop-filter:blur(8px)}
.lightbox-overlay.active{display:flex}
.lightbox-overlay img{max-width:90vw;max-height:90vh;object-fit:contain;border-radius:4px;box-shadow:0 20px 60px rgba(0,0,0,.6)}
.lightbox-caption{position:absolute;bottom:2rem;left:50%;transform:translateX(-50%);color:var(--text-secondary);font-size:.85rem;text-align:center;max-width:600px;font-family:var(--font-sans)}
.section-hero{position:relative;min-height:100vh;display:flex;align-items:center;justify-content:center;overflow:hidden;background:var(--bg-hero)}
.hero-bg{position:absolute;inset:0;background:url('https://imguscdn.gamespress.com/cdn/files/Square-Enix/2019/02/na-1-20190213200906/FFIX_keyart_1920x1080_v2.jpg?w=1920&mode=max&otf=y&quality=90&format=jpg') center/cover no-repeat;opacity:.35;filter:brightness(.6) saturate(.8)}
.hero-gradient{position:absolute;inset:0;background:linear-gradient(180deg,rgba(5,8,16,.3) 0%,rgba(5,8,16,.6) 40%,rgba(5,8,16,.95) 100%)}
.hero-content{position:relative;text-align:center;max-width:900px;padding:2rem;animation:heroFadeIn 2s ease-out}
.hero-subtitle{font-family:var(--font-sans);font-size:clamp(.7rem,1.5vw,.9rem);color:var(--gold);letter-spacing:.5em;text-transform:uppercase;margin-bottom:1.5rem;opacity:.8}
.hero-title{font-family:var(--font-display);font-size:clamp(3rem,8vw,7rem);color:var(--text-primary);line-height:1.1;font-weight:400;letter-spacing:.05em;margin-bottom:.5rem}
.hero-title em{font-style:italic;color:var(--gold);display:block;font-size:.55em;letter-spacing:.15em;margin-top:.3rem}
.hero-edition{font-family:var(--font-sans);font-size:.75rem;color:var(--text-muted);letter-spacing:.3em;text-transform:uppercase;margin-top:2rem}
.hero-scroll{position:absolute;bottom:3rem;left:50%;transform:translateX(-50%);display:flex;flex-direction:column;align-items:center;gap:.5rem;color:var(--text-muted);font-size:.65rem;letter-spacing:.2em;text-transform:uppercase;font-family:var(--font-sans);animation:scrollPulse 2s ease-in-out infinite}
.hero-scroll-line{width:1px;height:40px;background:linear-gradient(180deg,var(--gold),transparent)}
@keyframes heroFadeIn{from{opacity:0;transform:translateY(30px)}to{opacity:1;transform:translateY(0)}}
@keyframes scrollPulse{0%,100%{opacity:.4}50%{opacity:1}}
.magazine-section{position:relative;padding:var(--section-pad) 0;overflow:hidden}
.section-inner{max-width:var(--content-max);margin:0 auto;padding:0 2rem}
.section-wide{max-width:var(--content-wide);margin:0 auto;padding:0 2rem}
.section-chapter{font-family:var(--font-sans);font-size:.7rem;color:var(--gold);letter-spacing:.4em;text-transform:uppercase;margin-bottom:.5rem;opacity:.7}
.section-title{font-family:var(--font-display);font-size:clamp(2rem,5vw,3.5rem);color:var(--text-primary);line-height:1.2;margin-bottom:1rem;font-weight:400}
.section-lead{font-size:1.15rem;color:var(--text-secondary);line-height:2;max-width:700px;margin-bottom:3rem}
.body-text{font-size:1.05rem;line-height:2;color:var(--text-primary);margin-bottom:1.5rem;text-align:justify}
.body-text.lead-drop::first-letter{float:left;font-size:4.5em;line-height:.85;margin-right:.1em;color:var(--gold);font-family:var(--font-display);padding-top:.1em}
.divider{width:60px;height:1px;background:var(--gold);margin:3rem 0;opacity:.5}
.quote-block{border-left:3px solid var(--gold);padding:1.5rem 2rem;margin:2.5rem 0;background:rgba(200,168,78,.04)}
.quote-block p{font-size:1.15rem;font-style:italic;color:var(--gold-light);line-height:1.8}
.quote-block cite{display:block;margin-top:.8rem;font-size:.85rem;color:var(--text-muted);font-style:normal;letter-spacing:.1em}
.figure-magazine{margin:3rem 0;position:relative}
.figure-magazine img{width:100%;border-radius:2px;cursor:zoom-in;transition:transform .4s}
.figure-magazine img:hover{transform:scale(1.01)}
.figure-magazine figcaption{font-family:var(--font-sans);font-size:.8rem;color:var(--text-muted);margin-top:.8rem;line-height:1.6;text-align:center}
.theme-overview{background:linear-gradient(180deg,var(--midnight) 0%,var(--midnight-light) 50%,var(--midnight) 100%)}
.theme-overview .section-title{color:var(--gold-light)}
.theme-dev{background:var(--parchment);color:var(--charcoal)}
.theme-dev .section-title{color:var(--charcoal)}
.theme-dev .section-chapter{color:var(--crimson)}
.theme-dev .body-text{color:#2a2a2a}
.theme-dev .quote-block p{color:var(--crimson)}
.theme-dev .quote-block cite{color:#666}
.theme-dev .divider{background:var(--crimson)}
.theme-dev a{color:var(--crimson)}
.theme-world{background:linear-gradient(180deg,var(--deep-green) 0%,#0f1f0f 100%)}
.theme-world .section-title{color:var(--parchment)}
.theme-world .section-chapter{color:var(--gold)}
.theme-world .divider{background:var(--parchment-dark)}
.theme-chars{background:linear-gradient(180deg,var(--wine) 0%,var(--crimson-dark) 100%)}
.theme-chars .section-title{color:var(--gold)}
.theme-story{background:linear-gradient(180deg,var(--charcoal) 0%,#1a0a0a 50%,var(--charcoal) 100%)}
.theme-story .section-title{color:var(--crimson-light)}
.theme-story .section-chapter{color:var(--crimson)}
.theme-system{background:linear-gradient(180deg,var(--blue-gray) 0%,var(--charcoal) 100%)}
.theme-system .section-title{color:var(--blue-gray-light)}
.theme-review{background:linear-gradient(180deg,var(--black-gold) 0%,var(--midnight) 100%)}
.theme-review .section-title{color:var(--gold)}
.theme-gallery{background:var(--charcoal)}
.layout-fullbleed{position:relative;margin:4rem 0;height:60vh;min-height:400px;overflow:hidden}
.layout-fullbleed img{width:100%;height:100%;object-fit:cover}
.layout-fullbleed .overlay-text{position:absolute;bottom:0;left:0;right:0;padding:4rem 3rem 3rem;background:linear-gradient(transparent,rgba(0,0,0,.85))}
.layout-fullbleed .overlay-text h3{font-family:var(--font-display);font-size:clamp(1.5rem,4vw,2.5rem);color:var(--gold);font-weight:400;margin-bottom:.5rem}
.layout-fullbleed .overlay-text p{color:var(--text-secondary);max-width:600px;font-size:.95rem;line-height:1.8}
.layout-split{display:grid;grid-template-columns:1fr 1fr;gap:0;min-height:70vh;margin:4rem 0}
.layout-split .split-img{overflow:hidden}
.layout-split .split-img img{width:100%;height:100%;object-fit:cover}
.layout-split .split-text{display:flex;flex-direction:column;justify-content:center;padding:3rem 4rem}
.stat-number{font-family:var(--font-display);font-size:clamp(4rem,10vw,8rem);color:var(--gold);line-height:1;font-weight:400;opacity:.8}
.stat-label{font-family:var(--font-sans);font-size:.85rem;color:var(--text-muted);letter-spacing:.15em;text-transform:uppercase;margin-top:.5rem}
.stat-row{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:3rem;margin:3rem 0;text-align:center}
.timeline{position:relative;padding-left:3rem;margin:3rem 0}
.timeline::before{content:'';position:absolute;left:0;top:0;bottom:0;width:1px;background:linear-gradient(180deg,transparent,var(--gold),var(--gold),transparent)}
.timeline-item{position:relative;margin-bottom:3rem}
.timeline-item::before{content:'';position:absolute;left:-3rem;top:.5rem;width:10px;height:10px;border-radius:50%;background:var(--gold);transform:translateX(-4.5px);box-shadow:0 0 12px rgba(200,168,78,.4)}
.timeline-year{font-family:var(--font-sans);font-size:.75rem;color:var(--gold);letter-spacing:.2em;margin-bottom:.5rem}
.timeline-title{font-size:1.2rem;color:var(--text-primary);margin-bottom:.5rem}
.timeline-desc{font-size:.95rem;color:var(--text-secondary);line-height:1.8}
.char-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:2rem;margin:3rem 0}
.char-card{background:rgba(200,168,78,.05);border:1px solid rgba(200,168,78,.12);border-radius:4px;overflow:hidden;transition:all .4s}
.char-card:hover{border-color:rgba(200,168,78,.3);transform:translateY(-4px);box-shadow:0 15px 40px rgba(0,0,0,.3)}
.char-card-img{height:300px;overflow:hidden}
.char-card-img img{width:100%;height:100%;object-fit:cover;transition:transform .6s}
.char-card:hover .char-card-img img{transform:scale(1.05)}
.char-card-body{padding:1.5rem}
.char-card-name{font-family:var(--font-display);font-size:1.4rem;color:var(--gold);margin-bottom:.3rem}
.char-card-role{font-family:var(--font-sans);font-size:.75rem;color:var(--text-muted);letter-spacing:.15em;text-transform:uppercase;margin-bottom:1rem}
.char-card-desc{font-size:.9rem;color:var(--text-secondary);line-height:1.8}
.gallery-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:2rem 0}
.gallery-grid .gallery-item{overflow:hidden;border-radius:2px;cursor:pointer;position:relative}
.gallery-grid .gallery-item img{width:100%;height:100%;object-fit:cover;transition:transform .6s;aspect-ratio:16/9}
.gallery-grid .gallery-item:hover img{transform:scale(1.08)}
.gallery-grid .gallery-item::after{content:attr(data-caption);position:absolute;bottom:0;left:0;right:0;padding:1rem;background:linear-gradient(transparent,rgba(0,0,0,.8));color:var(--text-secondary);font-size:.75rem;font-family:var(--font-sans);transform:translateY(100%);transition:transform .4s}
.gallery-grid .gallery-item:hover::after{transform:translateY(0)}
.gallery-grid .gallery-tall{grid-row:span 2}
.gallery-grid .gallery-wide{grid-column:span 2}
.callout-box{background:rgba(200,168,78,.06);border:1px solid rgba(200,168,78,.15);padding:2rem 2.5rem;border-radius:4px;margin:2.5rem 0}
.callout-box h4{font-family:var(--font-display);font-size:1.2rem;color:var(--gold);margin-bottom:1rem}
.callout-box p{color:var(--text-secondary);line-height:1.8}
.ornament{display:flex;align-items:center;justify-content:center;gap:1rem;margin:4rem 0;color:var(--gold);opacity:.4}
.ornament::before,.ornament::after{content:'';width:60px;height:1px;background:currentColor}
.ornament span{font-size:.8rem}
.site-footer{background:#050810;border-top:1px solid rgba(200,168,78,.1);padding:4rem 2rem;text-align:center}
.footer-logo{font-family:var(--font-display);font-size:1.3rem;color:var(--gold);letter-spacing:.15em;margin-bottom:1rem}
.footer-text{font-size:.8rem;color:var(--text-muted);line-height:1.8;max-width:600px;margin:0 auto}
.footer-credits{margin-top:2rem;font-size:.7rem;color:var(--text-muted);opacity:.5}
.reveal{opacity:0;transform:translateY(40px);transition:opacity .8s ease,transform .8s ease}
.reveal.visible{opacity:1;transform:translateY(0)}
.reveal-left{opacity:0;transform:translateX(-40px);transition:opacity .8s ease,transform .8s ease}
.reveal-left.visible{opacity:1;transform:translateX(0)}
.reveal-right{opacity:0;transform:translateX(40px);transition:opacity .8s ease,transform .8s ease}
.reveal-right.visible{opacity:1;transform:translateX(0)}
body.light{--midnight:#f5f0e8;--midnight-light:#ebe5d8;--gold:#8b6914;--gold-light:#a07818;--gold-dark:#6b5010;--parchment:#2a2418;--parchment-dark:#3a3428;--text-primary:#1a1510;--text-secondary:#4a4030;--text-muted:#8a7a6a;--bg-hero:#e8e0d0;--charcoal:#f8f5ef;--crimson:#8b2a3a;--wine:#f5e8e8;--wine-light:#f0e8e0;--crimson-dark:#f8f0e8;--deep-green:#e8f0e8;--blue-gray:#e0e8f0}
body.light .hero-bg{opacity:.2;filter:brightness(1.2)}
body.light .hero-gradient{background:linear-gradient(180deg,rgba(245,240,232,.3),rgba(245,240,232,.7) 40%,rgba(245,240,232,.98))}
body.light .nav-main.scrolled{background:rgba(245,240,232,.92);border-bottom-color:rgba(139,105,20,.15)}
body.light .char-card{background:rgba(139,105,20,.05);border-color:rgba(139,105,20,.12)}
body.light .site-footer{background:#f0ece4;border-top-color:rgba(139,105,20,.15)}
@media(max-width:1024px){.layout-split{grid-template-columns:1fr;min-height:auto}.layout-split .split-text{padding:2rem}.toc-sidebar{display:none}}
@media(max-width:768px){.nav-links{display:none;position:fixed;top:60px;left:0;right:0;background:rgba(10,14,26,.96);flex-direction:column;padding:1rem;backdrop-filter:blur(20px)}.nav-links.open{display:flex}.nav-toggle{display:block}.char-grid{grid-template-columns:1fr}.gallery-grid{grid-template-columns:repeat(2,1fr)}.stat-row{grid-template-columns:repeat(2,1fr)}.hero-title{font-size:clamp(2.5rem,10vw,4rem)}}
@media print{.nav-main,.toc-sidebar,#back-top,#progress-bar,.theme-toggle,.hero-scroll{display:none!important}body{background:#fff;color:#000}.magazine-section{page-break-inside:avoid}}
.pullquote{font-family:var(--font-display);font-size:clamp(1.5rem,3vw,2.2rem);color:var(--gold);line-height:1.5;text-align:center;padding:3rem 2rem;margin:3rem 0;position:relative}
.pullquote::before{content:'\201C';font-size:5rem;color:var(--gold);opacity:.2;position:absolute;top:0;left:50%;transform:translateX(-50%)}
.pullquote cite{display:block;font-size:.8rem;color:var(--text-muted);margin-top:1rem;letter-spacing:.15em;font-style:normal}
</style>
</head>
<body>
<div id="progress-bar"></div>
<nav class="nav-main" id="nav"><div class="nav-inner"><div class="nav-logo">FINAL FANTASY IX<span>数字专题杂志</span></div><button class="nav-toggle" id="navToggle" aria-label="菜单">&#9776;</button><ul class="nav-links" id="navLinks"><li><a href="#hero">首页</a></li><li><a href="#overview">概览</a></li><li><a href="#development">幕后</a></li><li><a href="#world">世界</a></li><li><a href="#characters">人物</a></li><li><a href="#story">剧情</a></li><li><a href="#system">系统</a></li><li><a href="#review">评价</a></li><li><a href="#gallery">图库</a></li></ul><button class="theme-toggle" id="themeToggle">切换主题</button></div></nav>
<aside class="toc-sidebar" id="tocSidebar"><a href="#hero"><span class="toc-label">首页</span><span class="toc-dot"></span></a><a href="#overview"><span class="toc-label">概览</span><span class="toc-dot"></span></a><a href="#development"><span class="toc-label">幕后</span><span class="toc-dot"></span></a><a href="#world"><span class="toc-label">世界</span><span class="toc-dot"></span></a><a href="#characters"><span class="toc-label">人物</span><span class="toc-dot"></span></a><a href="#story"><span class="toc-label">剧情</span><span class="toc-dot"></span></a><a href="#system"><span class="toc-label">系统</span><span class="toc-dot"></span></a><a href="#review"><span class="toc-label">评价</span><span class="toc-dot"></span></a><a href="#gallery"><span class="toc-label">图库</span><span class="toc-dot"></span></a></aside>
<button id="back-top" aria-label="返回顶部">&#8593;</button>
<div class="lightbox-overlay" id="lightbox"><img src="" alt=""><div class="lightbox-caption" id="lightboxCaption"></div></div>
''')

# ============================================================
# We'll read content from separate files and join
# ============================================================
content_dir = os.path.join(output_dir, "parts")
os.makedirs(content_dir, exist_ok=True)

# Now write the complete file
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(''.join(parts))

print(f"Part 1 written: {len(''.join(parts))} chars")
print(f"Will append content parts next...")
