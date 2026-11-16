import json,html,os
L=[json.loads(l) for l in open('vids.jsonl')]
vids=[dict(id=d['id'],title=d['title'],dur=d.get('duration') or 0,views=d.get('view_count') or 0) for d in L]
json.dump(vids,open('public_videos.json','w'))
os.makedirs('public',exist_ok=True)
CH="https://www.youtube.com/@StackWhiz"
SUB="https://www.youtube.com/channel/UCm0-thT9F1NVYH23dn2YBzA?sub_confirmation=1"
e=html.escape
def page(name,title,desc,body):
    nav=''.join(f'<a href="{h}"{" class=on" if h==name else ""}>{t}</a>' for h,t in [('/','Home'),('/videos.html','Videos'),('/about.html','About'),('/contact.html','Contact')])
    open('public/'+('index.html' if name=='/' else name.lstrip('/')),'w').write(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(desc)}"><link rel="canonical" href="https://stackwhiz.mohith.dev{name if name!='/' else '/'}">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:type" content="website">
<link rel="icon" href="/favicon.svg"><link rel="stylesheet" href="/style.css"></head><body>
<header><div class="wrap bar"><a class="logo" href="/"><span>S</span>StackWhiz</a><nav>{nav}<a class="btn" href="{SUB}" target="_blank" rel="noopener">Subscribe</a></nav></div></header>
<main class="wrap">{body}</main>
<footer><div class="wrap foot"><div>© 2026 StackWhiz · Open source dev tools, AI coding agents &amp; self-hosted apps</div><div><a href="/about.html">About</a><a href="/contact.html">Contact</a><a href="/privacy.html">Privacy Policy</a><a href="/terms.html">Terms</a><a href="{CH}" target="_blank" rel="noopener">YouTube</a></div></div></footer></body></html>''')
def card(v):
    m=v['dur']//60;s=v['dur']%60
    t=f"{m}:{s:02d}"
    return f'<a class="card" href="https://www.youtube.com/watch?v={v["id"]}" target="_blank" rel="noopener"><div class="th"><img loading="lazy" src="https://i.ytimg.com/vi/{v["id"]}/hqdefault.jpg" alt="{e(v["title"])}"><i>{t}</i></div><h3>{e(v["title"])}</h3></a>'
longs=[v for v in vids if v['dur']>180]
shorts=[v for v in vids if v['dur']<=180]
topics=[("AI coding agents","Claude Code, Codex, Cursor and the open source tooling around them: routers, skills, sandboxes and memory."),
("Self-hosted apps","Run your own scheduler, VPN mesh, notes or dashboard on a cheap VPS instead of paying monthly SaaS fees."),
("Developer tools","CLIs, UI libraries, icon sets and utilities that save real time, explained in under a minute."),
("Paid tool replacements","For every popular paid product, we look for the open source alternative and tell you honestly where it falls short.")]
body=f'''<section class="hero"><p class="eyebrow">Open source · AI agents · Self-hosting</p><h1>Find the open source tool that replaces your paid one.</h1>
<p class="lead">StackWhiz is a YouTube channel that explains open source developer tools, AI coding agents and self-hosted apps: what each one does, how to install it, and which paid tool it can replace.</p>
<p><a class="btn big" href="{CH}" target="_blank" rel="noopener">Watch on YouTube</a> <a class="btn ghost big" href="/videos.html">Browse all {len(vids)} videos</a></p>
<div class="stats"><div><b>{len(vids)}</b><span>videos</span></div><div><b>{len(longs)}</b><span>deep dives</span></div><div><b>{len(shorts)}</b><span>quick shorts</span></div></div></section>
<h2>What we cover</h2><div class="topics">{''.join(f'<div class="topic"><h3>{a}</h3><p>{b}</p></div>' for a,b in topics)}</div>
<h2>Latest deep dives</h2><div class="grid">{''.join(card(v) for v in longs[:6])}</div>
<h2>Latest shorts</h2><div class="grid">{''.join(card(v) for v in shorts[:8])}</div>
<p class="more"><a href="/videos.html">See every video →</a></p>
<section class="how"><h2>How we pick tools</h2><ol><li><b>It must be open source.</b> Every project we feature has a public repository and a clear license (usually MIT or Apache-2.0).</li><li><b>It must actually run.</b> We install it and show what it does, rather than reading the README aloud.</li><li><b>We link the source.</b> Every video description links to the repository so you can verify claims and star the project.</li><li><b>We are honest about limits.</b> If a tool is early, unmaintained or missing features, we say so.</li></ol></section>'''
page('/','StackWhiz — Open source dev tools, AI coding agents & self-hosted apps','StackWhiz covers open source developer tools, AI coding agents and self-hosted apps: what each one does, how to install it, and which paid tool it can replace.',body)
page('/videos.html','All Videos — StackWhiz','Every StackWhiz video: deep dives and quick shorts on open source tools, AI coding agents and self-hosted apps.',
 f'<h1>All videos</h1><p class="lead">{len(vids)} videos on open source developer tools, AI coding agents and self-hosted apps. Click any video to watch on YouTube.</p><h2>Deep dives ({len(longs)})</h2><div class="grid">{"".join(card(v) for v in longs)}</div><h2>Shorts ({len(shorts)})</h2><div class="grid">{"".join(card(v) for v in shorts)}</div>')
page('/about.html','About StackWhiz','About StackWhiz, a YouTube channel about open source developer tools, AI coding agents and self-hosted apps.',f'''<h1>About StackWhiz</h1>
<p class="lead">StackWhiz is an independent YouTube channel for developers who like useful open source software.</p>
<p>We cover open source developer tools, AI coding agents and self-hosted apps. In every video we explain what the project does, how to install it, and which paid tool it can replace, so you can decide quickly whether it is worth your time.</p>
<h2>What you will find</h2><ul><li><b>Deep dives</b> (8–12 minutes): full walkthroughs of a single project, such as AI gateways, agent orchestration platforms, mesh VPNs and social schedulers.</li><li><b>Shorts</b> (under a minute): a fast look at one tool, one idea, one reason to try it.</li></ul>
<h2>Who it is for</h2><p>Software engineers, indie hackers, DevOps and SRE folks, and anyone building with AI coding agents like Claude Code, Codex and Cursor who wants to cut subscription costs and keep control of their data.</p>
<h2>Editorial policy</h2><p>We choose projects on merit. Every video links to the project's public repository in the description. If a video is ever sponsored, it will be clearly disclosed. Visuals that are illustrations rather than real screenshots are noted in the description.</p>
<p><a class="btn big" href="{SUB}" target="_blank" rel="noopener">Subscribe on YouTube</a></p>''')
page('/contact.html','Contact — StackWhiz','Contact StackWhiz to suggest an open source project or ask a question.',f'''<h1>Contact</h1><p class="lead">Know a great open source tool we should cover? Found a mistake? We would like to hear from you.</p>
<ul><li><b>YouTube:</b> leave a comment on any video or visit the <a href="{CH}/about" target="_blank" rel="noopener">channel's About tab</a> for business contact details.</li><li><b>GitHub:</b> <a href="https://github.com/mohith-code" target="_blank" rel="noopener">github.com/mohith-code</a></li></ul>
<h2>Suggest a project</h2><p>Send us the repository link and a sentence on why it matters. We prioritise projects that are open source, actively maintained and solve a real problem for developers.</p>''')
page('/privacy.html','Privacy Policy — StackWhiz','Privacy policy for stackwhiz.mohith.dev, including cookies and Google AdSense advertising.','''<h1>Privacy Policy</h1><p><i>Last updated: November 16, 2026</i></p>
<p>This policy explains how stackwhiz.mohith.dev (“the Site”) handles information. The Site is operated by StackWhiz.</p>
<h2>Information we collect</h2><p>We do not require accounts and do not collect personal information through forms. Like most websites, our server may log standard technical data such as IP address, browser type, pages visited and timestamps, used for security and basic traffic understanding.</p>
<h2>Cookies and advertising</h2><p>Third-party vendors, including Google, use cookies to serve ads based on your prior visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on your visit to the Site and/or other sites on the Internet. You may opt out of personalized advertising by visiting <a href="https://www.google.com/settings/ads" target="_blank" rel="noopener">Google Ads Settings</a>, or opt out of third-party vendors' use of cookies for personalized advertising at <a href="https://www.aboutads.info" target="_blank" rel="noopener">aboutads.info</a>.</p>
<h2>Third-party content</h2><p>The Site links to and shows thumbnails from YouTube and links to GitHub. Those services have their own privacy policies: <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">Google/YouTube Privacy Policy</a>.</p>
<h2>Analytics</h2><p>We may use privacy-respecting analytics to understand which pages are popular. No analytics data is sold.</p>
<h2>Children</h2><p>The Site is not directed to children under 13 and we do not knowingly collect their data.</p>
<h2>Your choices</h2><p>You can disable cookies in your browser settings. Depending on your location you may have rights to access or delete your data; contact us through the channel to make a request.</p>
<h2>Changes</h2><p>We may update this policy; the date above shows the latest revision.</p>''')
page('/terms.html','Terms of Use — StackWhiz','Terms of use for stackwhiz.mohith.dev.','''<h1>Terms of Use</h1><p><i>Last updated: November 16, 2026</i></p>
<p>By using stackwhiz.mohith.dev you agree to these terms.</p><h2>Content</h2><p>Content on the Site is provided for general information. Project names, logos and trademarks belong to their respective owners. Tools we feature are third-party software; check each project's license and security before using it.</p>
<h2>No warranty</h2><p>The Site is provided “as is” without warranties. We are not liable for any loss arising from using the information or the tools described.</p>
<h2>Links</h2><p>We link to external sites we do not control and are not responsible for their content.</p><h2>Contact</h2><p>See the <a href="/contact.html">Contact page</a>.</p>''')
open('public/favicon.svg','w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#6d5efc"/><text x="32" y="45" font-size="38" text-anchor="middle" font-family="Arial" font-weight="700" fill="#fff">S</text></svg>')
open('public/robots.txt','w').write('User-agent: *\nAllow: /\nSitemap: https://stackwhiz.mohith.dev/sitemap.xml\n')
open('public/sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>https://stackwhiz.mohith.dev{p}</loc></url>' for p in ['/','/videos.html','/about.html','/contact.html','/privacy.html','/terms.html'])+'</urlset>')
open('public/style.css','w').write(''':root{--bg:#0b0d14;--card:#141826;--line:#232a3d;--tx:#e8ebf5;--mu:#9aa3bd;--ac:#6d5efc}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--bg);color:var(--tx);font:16px/1.65 system-ui,-apple-system,Segoe UI,Roboto,sans-serif}
a{color:#9d93ff}.wrap{max-width:1100px;margin:auto;padding:0 20px}
header{border-bottom:1px solid var(--line);position:sticky;top:0;background:#0b0d14ee;backdrop-filter:blur(8px);z-index:5}
.bar{display:flex;align-items:center;justify-content:space-between;height:64px;gap:12px}
.logo{font-weight:800;font-size:20px;color:var(--tx);text-decoration:none;display:flex;gap:10px;align-items:center}.logo span{background:var(--ac);width:32px;height:32px;border-radius:9px;display:grid;place-items:center}
nav{display:flex;gap:16px;align-items:center}nav a{color:var(--mu);text-decoration:none;font-size:15px}nav a.on,nav a:hover{color:var(--tx)}
.btn{background:var(--ac);color:#fff!important;padding:8px 16px;border-radius:10px;text-decoration:none;font-weight:600;display:inline-block}.btn.big{padding:12px 22px}.btn.ghost{background:transparent;border:1px solid var(--line);color:var(--tx)!important}
.hero{padding:64px 0 24px}.eyebrow{color:#9d93ff;font-weight:600;letter-spacing:.08em;text-transform:uppercase;font-size:13px;margin:0}
h1{font-size:clamp(32px,5vw,52px);line-height:1.12;margin:.3em 0}h2{margin:2.2em 0 .7em;font-size:26px}h3{font-size:16px;margin:.5em 0}
.lead{color:var(--mu);font-size:19px;max-width:760px}.stats{display:flex;gap:32px;margin-top:32px}.stats b{font-size:32px;display:block}.stats span{color:var(--mu);font-size:14px}
.topics{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px}.topic{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px}.topic h3{margin-top:0}.topic p{color:var(--mu);margin:0;font-size:15px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:18px}.card{color:var(--tx);text-decoration:none;background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden;transition:.15s}.card:hover{transform:translateY(-3px);border-color:var(--ac)}
.th{position:relative;aspect-ratio:16/9;background:#000}.th img{width:100%;height:100%;object-fit:cover;display:block}.th i{position:absolute;right:8px;bottom:8px;background:#000c;font-style:normal;font-size:12px;padding:2px 6px;border-radius:5px}
.card h3{padding:0 14px 14px;margin:12px 0 0;line-height:1.4;font-weight:600}.more{text-align:center;margin:28px 0}
.how ol{padding-left:20px}.how li{margin:.6em 0;color:var(--mu)}.how b{color:var(--tx)}
main{min-height:70vh;padding-bottom:40px}main>h1{margin-top:48px}main ul{padding-left:20px}
footer{border-top:1px solid var(--line);color:var(--mu);font-size:14px;padding:28px 0;margin-top:40px}.foot{display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px}.foot a{margin-left:16px;color:var(--mu)}
@media(max-width:640px){nav a:not(.btn){display:none}.foot a{margin:0 14px 0 0}}''')
