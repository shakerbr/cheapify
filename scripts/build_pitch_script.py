#!/usr/bin/env python3
"""Generate docs/pitch-script.md and docs/pitch-script.html from one data source.

Run from the project root:  python3 scripts/build_pitch_script.py
Edit the SLIDES data below, never the generated files.
"""
import html
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

TYPES = {
    "click": ("▶", "CLICK", "Press the clicker once. The next thing appears on the slide."),
    "pause": ("■", "PAUSE", "Stop talking. Breathe. Let the room react."),
    "action": ("◆", "ACTION", "What your body does: walk, point, gesture."),
    "tone": ("♪", "VOICE", "How it should sound: speed, volume, mood."),
    "look": ("◉", "BEHAVIOUR", "Eyes, face and reactions: look, smile, wait."),
}

S = lambda t: ("say", t)
C = lambda t="": ("click", t)
P = lambda t: ("pause", t)
A = lambda t: ("action", t)
V = lambda t: ("tone", t)
L = lambda t: ("look", t)

SLIDES = [
    ("Cover", [
        A("Walk to the centre of the stage and stop. Plant both feet."),
        L("Look across the whole crowd, left to right. Smile. Wait one second before speaking."),
        V("Warm, big and friendly, like greeting friends."),
        S("Hello everyone!"),
        A("Raise your own hand as you ask."),
        S("Raise your hand if you've ever bought something online here."),
        P("2 seconds. Let hands go up."),
        L("Scan the room. Nod at the people with raised hands."),
        V("Drop to a playful whisper for the little voice."),
        S("Keep it up if, right after paying, a tiny voice asked: \"Did I just overpay?\""),
        P("2 seconds. Let them laugh."),
        V("Light, a little self-teasing."),
        S("Me too."),
        A("Lower your hand with a small shrug."),
        V("Back to full voice."),
        S("I'm Shakir Bashar, and that voice is today's story."),
    ]),
    ("Problem", [
        V("Slow down. Serious and clear. This is the key sentence of the whole pitch."),
        S("Online in Iraq, you can't know the real price before you buy."),
        C("The Miswag screen appears."),
        V("Curious, like you are about to show a magic trick."),
        A("Gesture to the screen with an open hand."),
        S("Look: one power bank, the Anker 25,000, 165 watt, on Miswag's search screen. Same search, same model."),
        C("The 100,000 price appears."),
        V("Calm and matter of fact."),
        S("One seller says 100,000 dinars."),
        C("The 200,000 price appears."),
        V("Voice goes up. Pure disbelief on \"200,000\"."),
        A("Point at the second price."),
        S("Right beside it, another says 200,000."),
        C("The 2x bracket appears."),
        V("Flat and deadpan."),
        S("Twice the price. Same power bank."),
        P("2 seconds. Let the number sink in."),
        V("Dry humour. Small smile."),
        S("Somebody's having a very good day."),
        L("Wait for the laugh. Do not talk over it."),
    ]),
    ("Problem · evidence", [
        V("Energy up. You are widening the story."),
        S("And it's the whole market."),
        C("Apps with duplicate listings appear."),
        S("Apps list the same item twice, at two prices."),
        C("The Instagram no-price post appears."),
        V("Imitate a seller's tone, slightly bored."),
        S("Instagram says \"DM for price.\""),
        C("The vacuum comparison appears."),
        V("Incredulous. Slow down on both prices."),
        S("This vacuum: a marketplace calls 133,000 a big discount. Instagram sells it for 95,000."),
        C("The survey numbers appear."),
        V("Steady and factual. Let the numbers do the work."),
        S("Ninety-seven percent of the 179 shoppers we asked see this. And 55 percent of merchants say answering \"how much?\" is their top headache."),
        V("Softer, with a sigh."),
        S("Both sides are tired."),
    ]),
    ("Solution", [
        P("1 second before you start. This is the turning point."),
        V("Bright and confident. The mood lifts here."),
        L("Smile. Look at the far side of the room."),
        S("So I'm building Cheapify. The bright side of choosing."),
        C("The one-page idea appears."),
        S("Every seller's real price for the same product, on one page."),
        C("The scattered products appear."),
        S("Today, one product is scattered everywhere."),
        C("The side-by-side sellers appear."),
        V("Clear and simple, like explaining to a friend."),
        S("On Cheapify, every seller sits side by side with the doorstep total: item plus delivery."),
        C("The Best Value badge appears."),
        V("Proud and firm on \"no store can pay to win it\"."),
        S("Best Value goes to the lowest total, then fastest delivery, then best rating. And no store can pay to win it. You order in seconds, pay at your door, and the store is paid automatically 48 hours later."),
    ]),
    ("Value proposition", [
        V("Quick and upbeat."),
        S("What do you get? Shoppers:"),
        A("Hold out one hand for shoppers."),
        C("The shopper benefits appear."),
        S("every price side by side, an order in thirty seconds, and no \"price?\" messages. Stores:"),
        A("Hold out the other hand for stores."),
        C("The store benefits appear."),
        S("ready orders with address and variant, a free dashboard for stock and payouts, and a fair fee, about 3.8 percent on a typical 25,000-dinar order."),
    ]),
    ("Target market", [
        V("Steady and building, like zooming in on a map."),
        S("We start in Duhok city, Semel and Zakho. Iraq has 46.1 million people."),
        C("Duhok governorate appears."),
        S("Duhok governorate, 1.6 million."),
        C("The launch area appears."),
        S("Our launch area, 1.06 million, about 890,000 of them online, spending roughly 30 million dollars a year."),
        C("The break-even number appears."),
        V("Slow down. This is the small number that matters."),
        S("To break even, we need about 390 regular shoppers. That's 0.4 percent of that market."),
        P("1 second."),
        V("Almost a whisper, then smile."),
        S("Four-tenths of one percent."),
    ]),
    ("Target customers", [
        V("Conversational. You are introducing real people."),
        S("Who are those 390 people? Time-poor professionals buying chargers and gadgets. Household budget buyers shopping for the home. Students and deal hunters."),
        V("Confident. These are your proof numbers."),
        S("Ninety-seven percent notice the price gaps, and 88 percent would use a comparison app."),
        C("The merchant side appears."),
        V("Switch to the stores' point of view. Warm and respectful."),
        S("And the stores? Duhok's social sellers, who already sell through DMs. Eighty-five percent sell on Instagram or Facebook, and 75 percent want to try Cheapify. We start with 20 founding stores, signed in person."),
        L("If you are running long, cut the last two sentences here."),
    ]),
    ("Business model", [
        V("Clear and measured. Money slide: do not rush."),
        S("We earn only when an order is delivered. Fee: 5 percent on the first 10,000 dinars, 3 percent up to 100,000, 1.5 percent above. On a 25,000-dinar order, with delivery margin, we take 1,450 dinars."),
        C("The costs appear."),
        S("Minus 335 for messages, logins and returns,"),
        C("The 1,115 result appears."),
        V("Land the number with confidence."),
        S("and we keep 1,115 per delivered order."),
        P("1 second."),
        V("Short and punchy."),
        S("No delivery, no fee."),
    ]),
    ("Competitor analysis", [
        V("Fast and light. This is a quick slide."),
        S("Who else is out there?"),
        C("The competitor table appears."),
        S("Instagram hides prices. Miswag, iBazzar and Elryan show them, but the same product appears in several listings."),
        C("The Cheapify column appears."),
        V("Confident and proud."),
        S("Only Cheapify puts every seller on one page, and does the comparing for you."),
    ]),
    ("Growth strategy", [
        V("Energetic. This is the momentum slide."),
        S("We grow on two sides."),
        C("The stores plan appears."),
        S("Stores: I sign the first 20 in person, zero percent fee in month one, free ads."),
        C("The shoppers plan appears."),
        S("Shoppers: targeted ads, short videos, campus deals at three universities, and referrals, starting from 52 people already on our waitlist."),
        C("The flywheel appears."),
        A("Draw a small circle in the air with your hand."),
        S("Then the flywheel spins: more stores, lower prices, more shoppers."),
        C("The expansion roadmap appears."),
        V("Big and ambitious. Raise your voice on \"all of Iraq\"."),
        S("Duhok first, then Erbil, Mosul and Sulaymaniyah, then all of Iraq."),
    ]),
    ("Financial feasibility", [
        V("Calm and honest. You are earning trust with numbers."),
        S("Does the math work? Our costs are 435 dollars a month, so we break even at 585 orders, about 390 shoppers."),
        C("The planned curve appears."),
        V("Slow and clear. Three milestones."),
        S("Planned pace: lowest point minus 2,180 dollars in month three, monthly break-even in month four, every loss recovered by month eight."),
        C("The fast curve appears."),
        S("Fast case: month three and month six."),
        C("The slow curve appears."),
        V("Reassuring."),
        S("Even at half speed, profitable from month seven."),
    ]),
    ("Funding", [
        V("Direct and sincere. No fluff. You are asking for support."),
        L("Look at the judges, not the screen."),
        S("My ask: 5,480 dollars. Every dollar has a job."),
        C("The pilot block appears."),
        S("100 to run our pilot by hand."),
        C("The registration block appears."),
        S("1,000 for official registration."),
        C("The launch block appears."),
        S("840 to launch 20 founding stores."),
        C("The runway block appears."),
        S("1,340 to cover losses, even at half speed."),
        C("The growth block appears."),
        S("2,200 for a four-month growth push."),
        C("The smaller-award line appears."),
        V("Humble and positive."),
        S("Even a smaller award still launches Cheapify."),
        C("The zero-salary line appears."),
        V("Proud, with a small smile."),
        S("And the platform? I build it myself, for zero salary."),
    ]),
    ("Thank you", [
        P("1 second before you start. Slow everything down."),
        V("Warm, quiet and sure. This is the last memory they keep."),
        L("Look at the crowd, not the screen."),
        S("Next time you see a price online, you'll ask: is this the real one?"),
        P("2 seconds."),
        V("Bigger, brighter, a smile in the voice."),
        S("Soon, you won't have to."),
        V("Slow and proud."),
        S("Cheapify. The bright side of choosing."),
        V("Warm and loud."),
        S("Thank you!"),
        L("Stay silent for two seconds. Smile. Wait for the applause."),
    ]),
]

WPM = 140


def words(text):
    return len(text.split())


def stats():
    out, cum = [], 0
    for name, items in SLIDES:
        w = sum(words(t) for k, t in items if k == "say")
        c = sum(1 for k, _ in items if k == "click")
        cum += w
        out.append((name, w, c, w / WPM * 60, cum / WPM * 60))
    return out


def mmss(sec):
    sec = round(sec)
    return f"{sec // 60}:{sec % 60:02d}"


def build_md():
    st = stats()
    total_w = sum(s[1] for s in st)
    total_c = sum(s[2] for s in st)
    lines = [
        "# Cheapify — Live Pitch Script (5 November 2026)",
        "",
        "Normal text is what you say, word for word. Everything else is a marked block that you never say aloud.",
        "",
        "| Symbol | Block | Meaning |",
        "| :-- | :-- | :-- |",
        "| (plain text) | **SAY** | Say these words out loud. |",
    ]
    for k, (sym, label, desc) in TYPES.items():
        lines.append(f"| {sym} | **{label}** | {desc} |")
    lines += [
        "",
        f"Total: {total_w} spoken words, about {mmss(total_w / WPM * 60)} at {WPM} words per minute, {total_c} clicks. Hard cap: 6:00.",
        "",
        "Same script as a colour-coded page: [pitch-script.html](pitch-script.html).",
        "",
        "---",
        "",
    ]
    for i, (name, items) in enumerate(SLIDES, 1):
        n, w, c, sec, cum = st[i - 1]
        lines += [f"## Slide {i} — {name}", "", f"*About {mmss(sec)} spoken, {c} clicks, running total {mmss(cum)}*", ""]
        cn = 0
        for kind, text in items:
            if kind == "say":
                lines += [text, ""]
            elif kind == "click":
                cn += 1
                lines += [f"> ▶ **CLICK {cn}** · {text}", ""]
            else:
                sym, label, _ = TYPES[kind]
                lines += [f"> {sym} **{label}** · {text}", ""]
        lines += ["---", ""]
    return "\n".join(lines)


CSS = """
:root{--blue:#298FC2;--ink:#1c2630;--mute:#5a6672;--bg:#f4f7fa;--card:#fff}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:Inter,system-ui,-apple-system,Segoe UI,Roboto,sans-serif;line-height:1.5}
header{position:sticky;top:0;z-index:5;background:var(--card);border-bottom:1px solid #dbe3ea;padding:10px 20px;display:flex;flex-wrap:wrap;gap:14px;align-items:center}
header h1{font-family:Comfortaa,Inter,sans-serif;font-size:18px;margin:0;color:var(--blue)}
header nav{display:flex;flex-wrap:wrap;gap:4px}
header nav a{font-size:13px;text-decoration:none;color:var(--ink);background:var(--bg);border:1px solid #dbe3ea;border-radius:8px;padding:3px 9px}
header nav a:hover{background:var(--blue);color:#fff}
header label{font-size:13px;color:var(--mute);margin-left:auto;cursor:pointer;user-select:none}
main{max-width:860px;margin:0 auto;padding:20px}
.legend{background:var(--card);border:1px solid #dbe3ea;border-radius:14px;padding:16px 20px;margin-bottom:24px}
.legend h2{margin:0 0 10px;font-size:16px}
.legend .row{display:flex;gap:10px;align-items:baseline;margin:6px 0;font-size:14px}
.badge{display:inline-flex;gap:6px;align-items:center;font-size:12px;font-weight:700;letter-spacing:.06em;border-radius:6px;padding:2px 8px;white-space:nowrap}
.slide{background:var(--card);border:1px solid #dbe3ea;border-radius:16px;padding:20px 24px;margin:0 0 26px;box-shadow:0 1px 3px rgba(20,40,60,.06)}
.slide h2{font-family:Comfortaa,Inter,sans-serif;margin:0;font-size:22px}
.slide h2 span{color:var(--blue)}
.meta{color:var(--mute);font-size:13px;margin:2px 0 14px}
.say{font-size:22px;line-height:1.6;margin:12px 0;padding-left:16px;border-left:5px solid var(--ink)}
.cue{display:flex;gap:10px;align-items:flex-start;border-radius:10px;padding:8px 12px;margin:10px 0;font-size:15px;border-left:5px solid}
.cue .badge{margin-top:1px}
.click{background:#e3f2fb;border-color:#298FC2}.click .badge{background:#298FC2;color:#fff}
.pause{background:#fdeeee;border-color:#D22730}.pause .badge{background:#D22730;color:#fff}
.action{background:#fff4e0;border-color:#E08A00}.action .badge{background:#E08A00;color:#fff}
.tone{background:#f0e9fb;border-color:#7A4CC2}.tone .badge{background:#7A4CC2;color:#fff}
.look{background:#e5f6ec;border-color:#228848}.look .badge{background:#228848;color:#fff}
.say-badge{background:var(--ink);color:#fff}
body.spoken .cue{display:none}
body.spoken .click{display:flex;background:none;border:none;padding:0;margin:2px 0}
body.spoken .click .badge{font-size:11px}
body.spoken .click span:last-child{display:none}
@media print{header{display:none}.slide{break-inside:avoid;box-shadow:none}}
"""

JS = """
const cb=document.getElementById('sp');
cb.addEventListener('change',()=>document.body.classList.toggle('spoken',cb.checked));
"""


def build_html():
    st = stats()
    total_w = sum(s[1] for s in st)
    total_c = sum(s[2] for s in st)
    e = html.escape
    nav = "".join(f'<a href="#s{i}">{i}</a>' for i in range(1, len(SLIDES) + 1))
    legend = ['<div class="row"><span class="badge say-badge">SAY</span><span>Plain large text with a dark bar: say these words, word for word.</span></div>']
    for k, (sym, label, desc) in TYPES.items():
        legend.append(f'<div class="row"><span class="badge cue {k}" style="padding:2px 8px;margin:0;border:none">{sym} {label}</span><span>{e(desc)}</span></div>')
    out = [
        "<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>",
        "<title>Cheapify — Live Pitch Script</title>",
        f"<style>{CSS}</style></head><body>",
        f"<header><h1>Cheapify pitch script</h1><nav>{nav}</nav><label><input type='checkbox' id='sp'> Spoken words only</label></header>",
        "<main>",
        f"<div class='legend'><h2>How to read this</h2>{''.join(legend)}",
        f"<p style='font-size:14px;color:var(--mute);margin:10px 0 0'>{total_w} spoken words, about {mmss(total_w / WPM * 60)} at {WPM} words per minute, {total_c} clicks. Hard cap: 6:00.</p></div>",
    ]
    for i, (name, items) in enumerate(SLIDES, 1):
        n, w, c, sec, cum = st[i - 1]
        out.append(f"<section class='slide' id='s{i}'><h2><span>Slide {i}</span> · {e(name)}</h2>")
        out.append(f"<div class='meta'>About {mmss(sec)} spoken · {c} clicks · running total {mmss(cum)}</div>")
        cn = 0
        for kind, text in items:
            if kind == "say":
                out.append(f"<p class='say'>{e(text)}</p>")
            elif kind == "click":
                cn += 1
                out.append(f"<div class='cue click'><span class='badge'>▶ CLICK {cn}</span><span>{e(text)}</span></div>")
            else:
                sym, label, _ = TYPES[kind]
                out.append(f"<div class='cue {kind}'><span class='badge'>{sym} {label}</span><span>{e(text)}</span></div>")
        out.append("</section>")
    out.append(f"</main><script>{JS}</script></body></html>")
    return "".join(out)


if __name__ == "__main__":
    (DOCS / "pitch-script.md").write_text(build_md(), encoding="utf-8")
    (DOCS / "pitch-script.html").write_text(build_html(), encoding="utf-8")
    st = stats()
    print("words", sum(s[1] for s in st), "time", mmss(sum(s[1] for s in st) / WPM * 60), "clicks", [s[2] for s in st])
