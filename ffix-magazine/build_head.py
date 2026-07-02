# -*- coding: utf-8 -*-
import os
base = r'C:\Users\Stella\Desktop\ffix-magazine'
os.makedirs(base, exist_ok=True)
f = open(os.path.join(base, 'index.html'), 'w', encoding='utf-8')

f.write('''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>水晶的回忆 —《最终幻想IX》数字专题杂志</title>
<meta name="description" content="一本关于《最终幻想IX》的中文数字专题杂志，深度解析开发幕后、世界观、角色与文化影响。">
<meta name="keywords" content="最终幻想9, Final Fantasy IX, FF9, FFIX, Square Enix, JRPG">
<meta property="og:title" content="水晶的回忆 —《最终幻想IX》数字专题杂志">
<meta property="og:description" content="一本关于《最终幻想IX》的中文数字专题杂志">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="">
<style>
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
:root{--bg-hero:#080c1f;--gold:#c9a55c;--gold-light:#e8d5a3;--gold-dim:#8a7035;--bg-overview:#0b0f18;--bg-dev:#f5f0e6;--text-dev:#1c1a16;--accent-dev:#8b6914;--bg-world:#0c1a14;--text-world:#c8d4c0;--accent-world:#4a7a4a;--bg-char:#18080a;--text-char:#d8ccc8;--accent-char:#b8860b;--bg-story:#1a0e0e;--text-story:#c8bfb8;--accent-story:#8b3a3a;--bg-system:#121c28;--text-system:#b8c4d0;--accent-system:#4a7a9a;--bg-review:#0a0a0a;--bg-gallery:#0e0e0e;--bg-footer:#060608;--font-serif:"Georgia","Noto Serif SC","SimSun",serif;--font-sans:"Helvetica Neue","Noto Sans SC","PingFang SC","Microsoft YaHei",sans-serif;--font-display:"Georgia","Noto Serif SC",serif}
html{scroll-behavior:smooth;font-size:16px;scroll-padding-top:70px}
body{font-family:var(--font-sans);line-height:1.8;color:#c8c4bc;background:#080c1f;overflow-x:hidden;-webkit-font-smoothing:antialiased}
::selection{background:var(--gold);color:#0a0a0a}
img{max-width:100%;height:auto;display:block}
a{color:var(--gold);text-decoration:none;transition:color .3s}
a:hover{color:var(--gold-light)}
#progress-bar{position:fixed;top:0;left:0;height:3px;background:linear-gradient(90deg,var(--gold),var(--gold-light));z-index:10000;width:0%}
nav{position:fixed;top:0;left:0;right:0;z-index:9999;padding:0 2rem;height:60px;display:flex;align-items:center;justify-content:space-between;backdrop-filter:blur(20px) saturate(180%);-webkit-backdrop-filter:blur(20px) saturate(180%);background:rgba(8,12,31,.75);border-bottom:1px solid rgba(201,165,92,.15);transition:all .4s}
nav.scrolled{background:rgba(8,12,31,.92);box-shadow:0 2px 30px rgba(0,0,0,.5)}
.nav-logo{font-family:var(--font-display);font-size:1.1rem;color:var(--gold);letter-spacing:.15em;font-weight:400;white-space:nowrap}
.nav-logo span{color:rgba(201,165,92,.5);font-size:.8em;margin-left:.3em}
.nav-links{display:flex;gap:0;list-style:none;align-items:center;overflow-x:auto;scrollbar-width:none}
.nav-links::-webkit-scrollbar{display:none}
.nav-links li a{display:block;padding:.6rem .8rem;font-size:.72rem;letter-spacing:.08em;color:rgba(200,196,188,.6);text-transform:uppercase;white-space:nowrap;transition:all .3s;border-bottom:2px solid transparent}
.nav-links li a.active,.nav-links li a:hover{color:var(--gold);border-bottom-color:var(--gold)}
.nav-toggle{display:none;flex-direction:column;gap:4px;cursor:pointer;padding:8px}
.nav-toggle span{width:20px;height:1.5px;background:var(--gold);transition:all .3s}
#toc-sidebar{position:fixed;right:1.5rem;top:50%;transform:translateY(-50%);z-index:9998;display:flex;flex-direction:column;gap:8px;opacity:0;transition:opacity .5s}
#toc-sidebar.visible{opacity:1}
#toc-sidebar a{width:8px;height:8px;border-radius:50%;background:rgba(201,165,92,.2);border:1px solid rgba(201,165,92,.3);transition:all .3s;display:block}
#toc-sidebar a.active{background:var(--gold);transform:scale(1.4);box-shadow:0 0 10px rgba(201,165,92,.5)}
#toc-sidebar a:hover{background:var(--gold-light);transform:scale(1.2)}
#back-top{position:fixed;bottom:2rem;right:2rem;z-index:9998;width:44px;height:44px;border-radius:50%;background:rgba(201,165,92,.15);border:1px solid rgba(201,165,92,.3);color:var(--gold);cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:1.2rem;opacity:0;pointer-events:none;transition:all .4s;backdrop-filter:blur(10px)}
#back-top.visible{opacity:1;pointer-events:auto}
#back-top:hover{background:rgba(201,165,92,.3);transform:translateY(-2px)}
#theme-toggle{position:fixed;bottom:2rem;left:2rem;z-index:9998;width:44px;height:44px;border-radius:50%;background:rgba(201,165,92,.15);border:1px solid rgba(201,165,92,.3);color:var(--gold);cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:1rem;transition:all .4s;backdrop-filter:blur(10px)}
#theme-toggle:hover{background:rgba(201,165,92,.3)}
#lightbox{position:fixed;inset:0;z-index:20000;background:rgba(0,0,0,.95);display:none;align-items:center;justify-content:center;cursor:zoom-out;padding:2rem}
#lightbox.active{display:flex}
#lightbox img{max-width:95vw;max-height:90vh;object-fit:contain;border-radius:4px}
#lightbox-close{position:absolute;top:1.5rem;right:1.5rem;color:white;font-size:2rem;cursor:pointer;background:none;border:none;z-index:20001}
.reveal{opacity:0;transform:translateY(40px);transition:opacity .8s ease,transform .8s ease}
.reveal.visible{opacity:1;transform:translateY(0)}
.reveal-left{opacity:0;transform:translateX(-60px);transition:opacity .8s ease,transform .8s ease}
.reveal-left.visible{opacity:1;transform:translateX(0)}
.reveal-right{opacity:0;transform:translateX(60px);transition:opacity .8s ease,transform .8s ease}
.reveal-right.visible{opacity:1;transform:translateX(0)}
.reveal-scale{opacity:0;transform:scale(.9);transition:opacity .8s ease,transform .8s ease}
.reveal-scale.visible{opacity:1;transform:scale(1)}
.hero{position:relative;min-height:100vh;display:flex;align-items:center;justify-content:center;background:var(--bg-hero);overflow:hidden}
.hero-bg{position:absolute;inset:0;background:url('https://cdn.akamai.steamstatic.com/steam/apps/377840/library_hero.jpg') center/cover no-repeat;opacity:.3;filter:brightness(.6) saturate(.8)}
.hero-overlay{position:absolute;inset:0;background:linear-gradient(180deg,rgba(8,12,31,.3),rgba(8,12,31,.6) 50%,rgba(8,12,31,1))}
.hero-content{position:relative;z-index:2;text-align:center;padding:2rem;max-width:900px}
.hero-issue{font-size:.7rem;letter-spacing:.3em;text-transform:uppercase;color:var(--gold-dim);margin-bottom:2rem}
.hero h1{font-family:var(--font-display);font-size:clamp(2.5rem,6vw,5rem);color:var(--gold);line-height:1.15;margin-bottom:.5rem;font-weight:400;text-shadow:0 0 60px rgba(201,165,92,.3)}
.hero h1 em{font-style:normal;color:var(--gold-light);font-size:.6em;display:block;margin-top:.3rem}
.hero-subtitle{font-size:clamp(1rem,2vw,1.3rem);color:rgba(200,196,188,.7);margin-top:1.5rem;line-height:1.9;max-width:650px;margin-left:auto;margin-right:auto}
.hero-meta{margin-top:3rem;display:flex;gap:3rem;justify-content:center;flex-wrap:wrap}
.hero-meta-item{text-align:center}
.hero-meta-item .num{font-family:var(--font-display);font-size:clamp(2rem,4vw,3.5rem);color:var(--gold);display:block;line-height:1}
.hero-meta-item .label{font-size:.7rem;letter-spacing:.15em;text-transform:uppercase;color:rgba(200,196,188,.5);margin-top:.3rem}
.hero-scroll{position:absolute;bottom:2rem;left:50%;transform:translateX(-50%);display:flex;flex-direction:column;align-items:center;gap:.5rem;color:var(--gold-dim);font-size:.65rem;letter-spacing:.2em;animation:scrollPulse 2s infinite}
@keyframes scrollPulse{0%,100%{opacity:.4;transform:translateX(-50%) translateY(0)}50%{opacity:1;transform:translateX(-50%) translateY(5px)}}
.hero-scroll .line{width:1px;height:30px;background:linear-gradient(180deg,var(--gold-dim),transparent)}
.section{padding:clamp(4rem,8vw,8rem) clamp(1.5rem,5vw,4rem)}
.section-label{font-size:.65rem;letter-spacing:.35em;text-transform:uppercase;color:var(--gold-dim);margin-bottom:1rem}
.section-title{font-family:var(--font-display);font-size:clamp(2rem,4vw,3.2rem);color:var(--gold);line-height:1.3;margin-bottom:2rem;font-weight:400}
.section-intro{font-size:1.05rem;line-height:2;color:rgba(200,196,188,.8);max-width:700px;margin-bottom:3rem}
.container{max-width:1200px;margin:0 auto}
.container-wide{max-width:1400px;margin:0 auto}
.container-narrow{max-width:800px;margin:0 auto}
.prose{font-family:var(--font-serif);font-size:clamp(.95rem,1.5vw,1.08rem);line-height:2;color:rgba(200,196,188,.85);margin-bottom:2rem;text-align:justify}
.prose p{margin-bottom:1.5rem;text-indent:2em}
.prose p:first-child,.prose p.no-indent{text-indent:0}
.prose .drop-cap::first-letter{float:left;font-size:3.5em;line-height:.8;margin-right:.1em;margin-top:.05em;color:var(--gold);font-family:var(--font-display)}
.pullquote{position:relative;padding:2.5rem 0;margin:3rem 0;text-align:center}
.pullquote::before,.pullquote::after{content:'';position:absolute;left:50%;width:60px;height:1px;background:var(--gold);transform:translateX(-50%)}
.pullquote::before{top:0}.pullquote::after{bottom:0}
.pullquote blockquote{font-family:var(--font-display);font-size:clamp(1.2rem,2.5vw,1.8rem);color:var(--gold);line-height:1.7;font-style:italic;max-width:600px;margin:0 auto}
.pullquote cite{display:block;font-size:.75rem;letter-spacing:.15em;color:var(--gold-dim);margin-top:1rem;font-style:normal}
.img-feature{margin:3rem 0;border-radius:4px;overflow:hidden;position:relative}
.img-feature img{width:100%;height:auto;cursor:zoom-in;transition:transform .5s}
.img-feature:hover img{transform:scale(1.02)}
.img-feature figcaption{padding:1rem 1.5rem;font-size:.75rem;color:rgba(200,196,188,.5);border-top:1px solid rgba(201,165,92,.1)}
.img-feature figcaption .source{color:var(--gold-dim);font-style:italic}
.editorial-2col{display:grid;grid-template-columns:1fr 1fr;gap:clamp(2rem,4vw,4rem);align-items:start;margin:3rem 0}
.editorial-2col.reverse{direction:rtl}.editorial-2col.reverse>*{direction:ltr}
.img-text-row{display:grid;grid-template-columns:1fr 1fr;gap:3rem;align-items:center;margin:4rem 0}
.img-text-row.reverse{direction:rtl}.img-text-row.reverse>*{direction:ltr}
.img-banner{margin:4rem -4rem;position:relative;height:clamp(250px,40vw,500px);overflow:hidden}
.img-banner img{width:100%;height:100%;object-fit:cover;filter:brightness(.7)}
.img-banner .overlay-text{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;flex-direction:column;padding:2rem;text-align:center}
.img-banner .overlay-text h3{font-family:var(--font-display);font-size:clamp(1.5rem,3vw,2.5rem);color:white;text-shadow:0 2px 20px rgba(0,0,0,.8)}
.timeline{position:relative;padding:2rem 0;margin:3rem 0}
.timeline::before{content:'';position:absolute;left:50%;top:0;bottom:0;width:1px;background:linear-gradient(180deg,transparent,var(--gold-dim),transparent);transform:translateX(-50%)}
.timeline-item{position:relative;width:45%;padding:1.5rem;margin-bottom:2rem}
.timeline-item:nth-child(odd){margin-left:5%;text-align:right}
.timeline-item:nth-child(even){margin-left:55%}
.timeline-item::after{content:'';position:absolute;top:1.5rem;width:10px;height:10px;border-radius:50%;background:var(--gold);border:2px solid rgba(201,165,92,.3)}
.timeline-item:nth-child(odd)::after{right:-28px}
.timeline-item:nth-child(even)::after{left:-28px}
.timeline-item .year{font-family:var(--font-display);font-size:1.5rem;color:var(--gold);margin-bottom:.5rem}
.timeline-item .desc{font-size:.9rem;color:rgba(200,196,188,.7);line-height:1.7}
.stat-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:2rem;margin:3rem 0}
.stat-item{text-align:center;padding:2rem 1rem;border:1px solid rgba(201,165,92,.1);border-radius:4px;background:rgba(201,165,92,.03)}
.stat-item .value{font-family:var(--font-display);font-size:clamp(2rem,4vw,3rem);color:var(--gold);display:block}
.stat-item .desc{font-size:.75rem;letter-spacing:.1em;color:rgba(200,196,188,.5);margin-top:.5rem;text-transform:uppercase}
.char-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:2.5rem;margin:3rem 0}
.char-card{background:rgba(201,165,92,.04);border:1px solid rgba(201,165,92,.1);border-radius:6px;overflow:hidden;transition:transform .4s,border-color .4s}
.char-card:hover{transform:translateY(-4px);border-color:rgba(201,165,92,.3)}
.char-card-img{height:200px;overflow:hidden;position:relative}
.char-card-img img{width:100%;height:100%;object-fit:cover;object-position:center top;filter:saturate(.8)}
.char-card-img .char-name-overlay{position:absolute;bottom:0;left:0;right:0;padding:1.5rem;background:linear-gradient(transparent,rgba(0,0,0,.8))}
.char-card-img .char-name-overlay h4{font-family:var(--font-display);font-size:1.3rem;color:var(--gold);margin:0}
.char-card-img .char-name-overlay .en-name{font-size:.65rem;letter-spacing:.15em;color:rgba(200,196,188,.5);text-transform:uppercase}
.char-card-body{padding:1.5rem}
.char-card-body .role{font-size:.7rem;letter-spacing:.2em;text-transform:uppercase;color:var(--gold-dim);margin-bottom:.8rem}
.char-card-body p{font-size:.9rem;line-height:1.8;color:rgba(200,196,188,.7)}
.section-cover{position:relative;min-height:60vh;display:flex;align-items:center;justify-content:center;overflow:hidden}
.section-cover-bg{position:absolute;inset:0;background-size:cover;background-position:center;filter:brightness(.35) saturate(.7)}
.section-cover-overlay{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.2),rgba(0,0,0,.6))}
.section-cover-content{position:relative;z-index:2;text-align:center;padding:4rem 2rem;max-width:700px}
.section-cover-content h2{font-family:var(--font-display);font-size:clamp(2rem,5vw,3.5rem);color:white;line-height:1.3;text-shadow:0 2px 30px rgba(0,0,0,.5)}
.section-cover-content .sub{font-size:.85rem;color:rgba(255,255,255,.6);margin-top:1rem;letter-spacing:.1em}
.divider{width:60px;height:1px;background:var(--gold);margin:3rem auto;opacity:.3}
.gallery-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:1rem;margin:3rem 0}
.gallery-item{border-radius:4px;overflow:hidden;position:relative;cursor:zoom-in;aspect-ratio:16/10}
.gallery-item img{width:100%;height:100%;object-fit:cover;transition:transform .5s,filter .5s}
.gallery-item:hover img{transform:scale(1.05);filter:brightness(1.1)}
.gallery-item .caption{position:absolute;bottom:0;left:0;right:0;padding:1rem;background:linear-gradient(transparent,rgba(0,0,0,.8));color:white;font-size:.75rem;opacity:0;transition:opacity .4s}
.gallery-item:hover .caption{opacity:1}
.sec-overview{background:var(--bg-overview)}
.sec-dev{background:var(--bg-dev);color:var(--text-dev)}.sec-dev .section-label,.sec-dev .section-title{color:var(--accent-dev)}.sec-dev .prose p{color:rgba(28,26,22,.85)}.sec-dev .pullquote blockquote{color:var(--accent-dev)}.sec-dev .timeline-item .year{color:var(--accent-dev)}.sec-dev .timeline::before{background:linear-gradient(180deg,transparent,rgba(139,105,20,.3),transparent)}.sec-dev .timeline-item::after{background:var(--accent-dev)}
.sec-world{background:var(--bg-world);color:var(--text-world)}.sec-world .section-label,.sec-world .section-title{color:var(--accent-world)}.sec-world .pullquote blockquote{color:var(--accent-world)}
.sec-char{background:var(--bg-char);color:var(--text-char)}.sec-char .section-label,.sec-char .section-title{color:var(--accent-char)}.sec-char .pullquote blockquote{color:var(--accent-char)}
.sec-story{background:var(--bg-story);color:var(--text-story)}.sec-story .section-label,.sec-story .section-title{color:var(--accent-story)}.sec-story .pullquote blockquote{color:var(--accent-story)}
.sec-system{background:var(--bg-system);color:var(--text-system)}.sec-system .section-label,.sec-system .section-title{color:var(--accent-system)}.sec-system .pullquote blockquote{color:var(--accent-system)}
.sec-review{background:var(--bg-review)}.sec-review .section-label,.sec-review .section-title{color:var(--accent-review)}.sec-review .pullquote blockquote{color:var(--accent-review)}
.sec-gallery{background:var(--bg-gallery);color:var(--text-gallery)}
footer{background:var(--bg-footer);padding:4rem 2rem;text-align:center;border-top:1px solid rgba(201,165,92,.1)}
footer .footer-logo{font-family:var(--font-display);font-size:1.2rem;color:var(--gold);margin-bottom:1rem}
footer .footer-note{font-size:.75rem;color:rgba(200,196,188,.3);line-height:1.8;max-width:600px;margin:0 auto}
body.light-mode{--bg-hero:#f8f4ec;--bg-overview:#ffffff;--bg-dev:#f5f0e6;--text-dev:#1c1a16;--bg-world:#f0f4f0;--text-world:#1a2a1a;--bg-char:#faf5f0;--text-char:#2a1a1a;--bg-story:#f5f0ec;--text-story:#2a1a1a;--bg-system:#f0f4f8;--text-system:#1a2030;--bg-review:#f8f8f8;--bg-gallery:#f0f0f0;--bg-footer:#1a1a1a;background:#f8f4ec;color:#2a2520}
body.light-mode nav{background:rgba(248,244,236,.9)}
body.light-mode .hero-bg{opacity:.15;filter:brightness(1.2) saturate(.6)}
body.light-mode .hero h1{color:#5a4020;text-shadow:none}
body.light-mode .hero-subtitle{color:rgba(42,37,32,.7)}
body.light-mode .prose p{color:rgba(42,37,32,.85)}
body.light-mode .section-title{color:#5a4020}.body.light-mode .section-label{color:#8a7035}
body.light-mode .pullquote blockquote{color:#5a4020}
body.light-mode .char-card{background:rgba(90,64,32,.04);border-color:rgba(90,64,32,.1)}
body.light-mode .img-feature figcaption{color:rgba(42,37,32,.5)}
body.light-mode .char-card-body p,.body.light-mode .hero-meta-item .label{color:rgba(42,37,32,.5)}
body.light-mode #toc-sidebar a{background:rgba(90,64,32,.2);border-color:rgba(90,64,32,.3)}
body.light-mode #toc-sidebar a.active{background:#5a4020}
body.light-mode #back-top,body.light-mode #theme-toggle{background:rgba(90,64,32,.1);border-color:rgba(90,64,32,.2);color:#5a4020}
body.light-mode .sec-dev .section-title,body.light-mode .sec-dev .section-label{color:#8b6914}
body.light-mode .sec-dev .pullquote blockquote{color:#8b6914}
body.light-mode .sec-dev .timeline-item .year{color:#8b6914}
body.light-mode .sec-world .section-title{color:#2a5a2a}
@media(max-width:1024px){.nav-links li a{padding:.5rem .5rem;font-size:.65rem}.timeline::before{left:20px}.timeline-item{width:calc(100% - 50px);margin-left:50px!important;text-align:left!important}.timeline-item::after{left:-35px!important;right:auto!important}}
@media(max-width:768px){nav{padding:0 1rem;height:52px}.nav-links{display:none;position:absolute;top:52px;left:0;right:0;flex-direction:column;background:rgba(8,12,31,.95);padding:1rem}.nav-links.open{display:flex}.nav-toggle{display:flex}.editorial-2col,.img-text-row{grid-template-columns:1fr;gap:2rem}.img-text-row.reverse,.editorial-2col.reverse{direction:ltr}.img-banner{margin:3rem -1rem}.char-grid{grid-template-columns:1fr}.stat-grid{grid-template-columns:repeat(2,1fr)}.gallery-grid{grid-template-columns:repeat(auto-fill,minmax(200px,1fr))}#toc-sidebar{display:none}.hero-meta{gap:2rem}.section{padding:3rem 1.2rem}}
@media(max-width:480px){.stat-grid,.gallery-grid{grid-template-columns:1fr}}
@media print{nav,#progress-bar,#toc-sidebar,#back-top,#theme-toggle,.hero-scroll{display:none!important}body{background:white;color:#1a1a1a}.hero{min-height:auto;padding:2rem;background:white}.hero-bg,.hero-overlay{display:none}.section{padding:1rem 0;page-break-inside:avoid}}
</style>
</head>
<body>
<div id="progress-bar"></div>
<nav id="main-nav"><div class="nav-logo">水晶的回忆<span>FFIX MAGAZINE</span></div><div class="nav-toggle" id="nav-toggle"><span></span><span></span><span></span></div><ul class="nav-links" id="nav-links"><li><a href="#overview">概览</a></li><li><a href="#development">开发</a></li><li><a href="#world">世界</a></li><li><a href="#characters">人物</a></li><li><a href="#story">剧情</a></li><li><a href="#systems">系统</a></li><li><a href="#reviews">影响</a></li><li><a href="#gallery">图库</a></li></ul></nav>
<div id="toc-sidebar"><a href="#overview"></a><a href="#development"></a><a href="#world"></a><a href="#characters"></a><a href="#story"></a><a href="#systems"></a><a href="#reviews"></a><a href="#gallery"></a></div>
<button id="back-top" aria-label="返回顶部">&#8593;</button>
<button id="theme-toggle" aria-label="切换主题">&#9681;</button>
<div id="lightbox"><button id="lightbox-close">&times;</button><img src="" alt=""></div>
''')

f.close()
print("Head + CSS + nav written")
