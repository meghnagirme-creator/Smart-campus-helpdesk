from flask import Flask, render_template_string
app = Flask(__name__)

announcements = [
    ("Practical Submission", "28 October 2026", "Submit your completed practical journal to your subject teacher."),
    ("Library Reminder", "30 October 2026", "Return borrowed books before their due date."),
    ("Project Guidance", "2 November 2026", "Meet your project guide during department hours.")
]
services = [
    ("📚", "Library", "Library timings, book returns and study resources."),
    ("🧪", "Laboratories", "Practical schedules and lab information."),
    ("🧑‍🏫", "Department", "Faculty and academic guidance."),
    ("🗓️", "Academic Calendar", "Important dates, submissions and events.")
]
@app.route("/")
def home():
    return render_template_string("""
<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Smart Campus Helpdesk</title><style>
*{box-sizing:border-box}body{margin:0;font-family:Arial,sans-serif;background:#f4f7fc;color:#1b2940}
header{padding:28px 7% 38px;color:white;background:linear-gradient(120deg,#142847,#2864dc)}
.brand{font-weight:bold;font-size:20px}.tag{float:right;border:1px solid #ffffff80;border-radius:20px;padding:7px 12px;font-size:12px}
h1{font-size:clamp(30px,5vw,46px);margin:35px 0 10px}header p{max-width:620px;line-height:1.6;color:#e4edff}
main{max-width:1050px;margin:auto;padding:28px 6% 50px}.welcome{display:flex;justify-content:space-between;gap:12px;align-items:center;flex-wrap:wrap}
h2{font-size:22px}.muted,.card p,.notice p{color:#64748b;line-height:1.5}.pill{background:#e1edff;color:#245bc7;border-radius:12px;padding:10px 14px;font-weight:bold;font-size:13px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:15px}.card,.notice{background:white;border:1px solid #e2e9f3;border-radius:15px;padding:19px;box-shadow:0 5px 18px #1d35570a}
.emoji{font-size:28px}.card h3{margin:12px 0 7px}.card p{font-size:14px;margin-bottom:0}
.notice{display:flex;gap:14px;margin:12px 0}.date{min-width:100px;background:#edf4ff;color:#245bc7;padding:10px;border-radius:10px;text-align:center;font-size:12px;font-weight:bold}
.notice h3{margin:0 0 6px}.notice p{font-size:14px;margin:0}.help{margin-top:25px;padding:22px;background:#e7f0ff;border-radius:15px;line-height:1.6}
footer{text-align:center;color:#718096;padding:20px;font-size:12px}@media(max-width:500px){.notice{flex-direction:column}.date{width:max-content}}
</style></head><body><header><span class="brand">🎓 Smart Campus Helpdesk</span><span class="tag">STUDENT SUPPORT PORTAL</span>
<h1>Your campus information, all in one place.</h1><p>A simple student-friendly portal for academic announcements, campus services and helpful college information.</p></header>
<main><div class="welcome"><div><h2>Welcome, Student!</h2><p class="muted">Find useful campus information quickly and easily.</p></div><span class="pill">● Demo Portal</span></div>
<h2>Campus Services</h2><div class="grid">{% for icon,title,desc in services %}<article class="card"><div class="emoji">{{icon}}</div><h3>{{title}}</h3><p>{{desc}}</p></article>{% endfor %}</div>
<h2>Latest Announcements</h2>{% for title,date,desc in announcements %}<article class="notice"><div class="date">{{date}}</div><div><h3>{{title}}</h3><p>{{desc}}</p></div></article>{% endfor %}
<section class="help"><h2>Need help?</h2><p>For official information, contact your department office or subject teacher. This demo uses sample announcements; replace them with information approved by your college.</p></section></main>
<footer>Smart Campus Helpdesk · Python · Flask · Google App Engine</footer></body></html>
""", services=services, announcements=announcements)

if __name__ == "__main__":
    app.run(debug=True)
