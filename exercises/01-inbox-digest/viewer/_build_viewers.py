"""
Build self-contained local viewers for the Exercise 1 simulated data.

Reads ../simulated-inbox/inbox.json and ../simulated-crm/crm.json and writes
inbox.html and crm.html in this folder, with the data inlined so they open with a
double-click (no server, no internet). Re-run this after editing the data.

    python _build_viewers.py
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
EX = os.path.dirname(HERE)
inbox = json.load(open(os.path.join(EX, "simulated-inbox", "inbox.json"), encoding="utf-8"))
crm = json.load(open(os.path.join(EX, "simulated-crm", "crm.json"), encoding="utf-8"))

CSS = """
:root{--ink:#1F2041;--coral:#F35B67;--teal:#72D9D3;--gold:#E8AD5A;--line:#E3E5EE;--muted:#6E7191}
*{box-sizing:border-box}
body{margin:0;font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;color:var(--ink);background:#F7F8FB}
header{background:var(--ink);color:#fff;padding:18px 28px;display:flex;align-items:center;gap:14px}
header .dot{width:18px;height:18px;border-radius:5px;background:linear-gradient(135deg,var(--teal),var(--coral))}
header h1{font-size:18px;margin:0;font-weight:700}
header .sub{color:#A0A3BD;font-size:13px;margin-left:6px}
nav{padding:10px 28px;background:#fff;border-bottom:1px solid var(--line);font-size:14px}
nav a{color:var(--ink);text-decoration:none;margin-right:18px;font-weight:600}
nav a.active{color:var(--coral)}
.wrap{max-width:1000px;margin:0 auto;padding:24px 28px}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin-bottom:12px}
.row{display:flex;justify-content:space-between;gap:12px;align-items:baseline}
.from{font-weight:700}
.subject{margin:4px 0 2px}
.snippet{color:var(--muted);font-size:14px}
.date{color:var(--muted);font-size:12px;white-space:nowrap}
.pill{display:inline-block;font-size:11px;font-weight:700;padding:2px 8px;border-radius:999px;vertical-align:middle}
.unread{background:#FDE7E9;color:var(--coral)}
.tag{background:#E9F8F6;color:#1f8e85}
.body{margin-top:8px;font-size:14px;color:#3a3d57;display:none;border-top:1px dashed var(--line);padding-top:8px}
.card.open .body{display:block}
.card.is-unread{border-left:4px solid var(--coral)}
.meta{color:var(--muted);font-size:13px;margin:2px 0}
.note{background:#FAFAFE;border:1px solid var(--line);border-radius:8px;padding:10px 12px;font-size:14px;margin-top:8px;color:#3a3d57}
.open-item{color:var(--coral);font-weight:600;font-size:14px}
h2.section{font-size:14px;color:var(--muted);text-transform:uppercase;letter-spacing:.05em;margin:18px 0 8px}
.count{font-size:13px;color:var(--muted);margin-bottom:6px}
"""

INBOX_JS = """
const inbox = DATA;
const ul = document.getElementById('list');
const unread = inbox.emails.filter(e=>e.unread).length;
document.getElementById('count').textContent =
  inbox.emails.length + ' messages · ' + unread + ' unread';
inbox.emails.forEach(e=>{
  const c = document.createElement('div');
  c.className = 'card' + (e.unread ? ' is-unread' : '');
  c.innerHTML =
    '<div class="row"><div class="from">'+e.from_name+
      (e.unread?' <span class="pill unread">unread</span>':'')+
      (e.contact_id?'':' <span class="pill tag">no contact</span>')+
    '</div><div class="date">'+e.date.replace('T',' ')+'</div></div>'+
    '<div class="meta">'+e.from_email+'</div>'+
    '<div class="subject"><b>'+e.subject+'</b></div>'+
    '<div class="snippet">'+e.snippet+'</div>'+
    '<div class="body">'+e.body+'</div>';
  c.addEventListener('click',()=>c.classList.toggle('open'));
  ul.appendChild(c);
});
"""

CRM_JS = """
const crm = DATA;
const ul = document.getElementById('list');
document.getElementById('count').textContent = crm.contacts.length + ' contacts';
crm.contacts.forEach(p=>{
  const c = document.createElement('div');
  c.className='card';
  c.innerHTML =
    '<div class="row"><div class="from">'+p.name+' <span class="pill tag">'+p.relationship+'</span></div>'+
      '<div class="date">last contact '+p.last_contact+'</div></div>'+
    '<div class="meta">'+p.role+' · '+p.company+' · '+p.email+'</div>'+
    '<div class="meta">Status: <b>'+p.status+'</b></div>'+
    '<div class="open-item">Open item: '+p.open_item+'</div>'+
    '<div class="note">'+p.notes+'</div>';
  ul.appendChild(c);
});
"""


def page(title, sub, active, data, js):
    return f"""<!doctype html><html><head><meta charset="utf-8">
<title>{title}</title><style>{CSS}</style></head><body>
<header><div class="dot"></div><h1>{title}</h1><span class="sub">{sub}</span></header>
<nav><a href="inbox.html" class="{'active' if active=='inbox' else ''}">Inbox</a>
<a href="crm.html" class="{'active' if active=='crm' else ''}">CRM</a></nav>
<div class="wrap"><div class="count" id="count"></div><div id="list"></div></div>
<script>const DATA = {json.dumps(data)};</script>
<script>{js}</script>
</body></html>"""


open(os.path.join(HERE, "inbox.html"), "w", encoding="utf-8").write(
    page("Simulated Inbox", "Exercise 1 · click a message to expand · simulated data",
         "inbox", inbox, INBOX_JS))
open(os.path.join(HERE, "crm.html"), "w", encoding="utf-8").write(
    page("Simulated CRM", "Exercise 1 · your notes on each contact · simulated data",
         "crm", crm, CRM_JS))
print("wrote inbox.html and crm.html")
