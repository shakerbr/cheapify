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
    "auto": ("◌", "AUTO", "Appears by itself when the slide starts. No click needed."),
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
N = lambda t: ("auto", t)

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
        S("I'm Shakir Bashar, and that tiny voice is today's story."),
    ]),
    ("Problem", [
        V("Slow down. Serious and clear. This is the key sentence of the whole pitch."),
        S("Online in Iraq, you can't know the real price before you buy."),
        C("The Miswag screenshot appears."),
        V("Curious, like you are about to show a magic trick."),
        A("Gesture to the screen with an open hand."),
        S("Here's one power bank, on Miswag. Same search. Same screen. Same model."),
        C("The first price, 100,000, is circled."),
        V("Calm and matter of fact."),
        S("One seller: 100,000 dinars."),
        C("The second price, 200,000, is circled."),
        V("Voice goes up. Pure disbelief on \"200,000\"."),
        A("Point at the second price."),
        S("Right beside it: 200,000."),
        C("The 2x bracket and the \"2x the price\" box appear."),
        V("Flat and deadpan."),
        S("Twice the price. Same power bank."),
        P("2 seconds. Let it sink in."),
        V("Dry humour. Small smile."),
        S("Somebody's having a very good day."),
        L("Wait for the laugh. Do not talk over it."),
    ]),
    ("Problem · evidence", [
        V("Knowing and a little tired, like someone who has seen this too many times."),
        L("Let the headline sit on screen for a beat."),
        S("And it's not just one power bank. It's everywhere."),
        C("Card 1 appears: the same item listed twice inside one app, 60,000 and 70,000."),
        V("Matter of fact. Keep it flowing, like one sentence."),
        S("The same product, at different prices..."),
        C("Card 2 appears: an Instagram ad with no price, and one comment underneath: \"How much?\""),
        V("A little dry, a half smile."),
        S("...or no price at all..."),
        C("Card 3 appears: the vacuum with a red \"-35%\" sticker at 133,250, against 95,000 on Instagram."),
        V("Drop the voice on the last words, with a hint of sarcasm."),
        S("...or a discount that isn't one."),
        P("1 second."),
        C("The 97% bar appears."),
        V("Steady and factual. Let the number do the work."),
        L("Pause, nod slowly, and let some of them nod back."),
        S("And almost everyone we asked, 97 percent, has seen it."),
    ]),
    ("Solution", [
        P("1 second of silence after the last slide. Let the tension hang."),
        A("Take half a step forward."),
        L("Smile. Look at the far side of the room."),
        V("Start curious and quiet, then let it bloom into bright and proud."),
        N("The logo, the name Cheapify and the slogan appear by themselves."),
        S("So I asked myself: what if every price lived in one place? That's why I came up with Cheapify."),
        P("1 second. Let the logo sit."),
        C("The logo fades out and the headline appears: \"Cheapify puts every seller's real price for the same product on one page.\""),
        V("Clear and simple, like explaining it to a friend."),
        S("Cheapify puts every seller's real price..."),
        C("Scattered price cards appear: the same power bank, all over the place."),
        V("Playfully annoyed. Let the mess sit for a moment."),
        S("...for the same product..."),
        P("1 second. Let them see the mess."),
        C("The cards fade out and the one-page comparison table appears."),
        A("Open both hands together, as if closing a book."),
        V("Relief. Slower and satisfied."),
        S("...on one page."),
        P("1 second. Let them read the table."),
        C("The Best Value badge and the three ranking rules appear."),
        V("Excited. You are revealing the clever part."),
        S("And it doesn't stop there. It also chooses the Best Value for you."),
        A("Point at the green Best Value badge, then sweep your hand down the three rules on the right."),
        V("Count them off, one beat each."),
        S("Based on the lowest total price, the fastest delivery, and the best-rated store."),
        P("1 second."),
        V("Warm and a little cheeky. A smile in the voice."),
        S("No more ten tabs to buy one power bank."),
    ]),
    ("Value proposition", [
        V("Warm and direct. Talk to the crowd, not the screen."),
        N("The two column headings, \"For shoppers\" and \"For merchants\", appear by themselves."),
        A("Open one hand toward the audience as you ask."),
        S("So what's in it for you?"),
        P("1 second. Let them think about it."),
        A("Hold out one hand for shoppers."),
        C("The three shopper benefits appear."),
        S("If you shop: no more ten pages, no more \"price?\" and waiting, and the full price upfront."),
        A("Hold out the other hand for merchants."),
        C("The three merchant benefits appear."),
        V("Shift to a respectful, business-to-business tone."),
        S("If you sell: no more answering the same question all day, orders arrive ready, and a small fee only on delivered orders."),
    ]),
    ("Target market", [
        V("Steady and building, like zooming in on a map. Keep it one flowing sentence."),
        N("The Iraq circle appears by itself."),
        S("Iraq is big. We start small,"),
        C("The Duhok governorate circle appears."),
        S("inside one governorate,"),
        C("The launch-area circle appears."),
        S("in three cities, with over a million people and 30 million dollars of online shopping a year."),
        C("The break-even card appears."),
        V("Slow down. This is the small number that matters."),
        S("And we need just 390 regular shoppers to break even."),
        P("1 second."),
        V("Almost a whisper, then a smile."),
        S("Less than half a percent of that market."),
    ]),
    ("Target customers", [
        V("Clear and conversational. You are painting three quick portraits."),
        N("The shoppers card appears by itself, with its three groups and the 97% gauge."),
        S("So who are those 390? People who already compare prices:"),
        A("Point to the first row, then move your hand down one row per group."),
        S("busy professionals with no time to hunt, households stretching a budget, and students chasing a deal."),
        P("1 second."),
        C("The merchants card appears, with its three rows and the 85% and 75% gauges."),
        A("Turn your hand toward the merchants card."),
        V("Brighter. This is the good news."),
        S("And the stores? Social-media sellers who already sell through DMs. Three in four want to try Cheapify."),
    ]),
    ("Business model", [
        V("Clear and measured. Money slide: do not rush."),
        N("The fee panel appears by itself."),
        S("How does Cheapify make money? A small fee, lighter on bigger orders. On a typical order, that's about 1,450 dinars for us."),
        C("The costs appear."),
        S("Out of that, we pay for messages, logins, returns and re-deliveries."),
        C("The 1,115 result appears."),
        V("Land the number with confidence."),
        S("And we keep 1,115 dinars."),
        P("1 second."),
        V("Short and punchy."),
        S("No delivery, no fee."),
    ]),
    ("Competitor analysis", [
        V("Fast and light. This is a quick slide."),
        N("The comparison table frame appears by itself."),
        S("So what's already out there?"),
        C("The competitor columns appear: Instagram, Miswag, iBazzar, Elryan."),
        S("Instagram hides prices. Miswag, iBazzar and Elryan show them, but one product, many separate listings."),
        C("The Cheapify column appears."),
        V("Confident, a little cheeky."),
        S("Nobody else puts every seller on one page and compares them for you. Only Cheapify."),
    ]),
    ("Growth strategy", [
        V("Energetic. You are letting them in on the secret of how it starts."),
        N("The two-sides ring appears by itself."),
        S("How does a marketplace start from nothing?"),
        C("The stores plan appears."),
        A("Gesture to the left column."),
        S("With stores. Twenty, signed in person, no fees the first month, free ads, and each one brings its followers."),
        C("The shoppers plan appears."),
        A("Gesture to the right column."),
        S("And the shoppers: they need to know Cheapify exists, so ads, short videos, campus deals. And 52 people are already waiting for launch day."),
        C("The flywheel appears."),
        A("Draw a small circle in the air with your hand."),
        S("Now the wheel spins by itself. More stores, lower prices, more shoppers, more orders."),
        C("The expansion roadmap appears."),
        A("Move your hand left to right along the strip."),
        V("Big and ambitious. Raise your voice on \"all of Iraq\"."),
        S("Duhok first. Then Erbil, Mosul, Sulaymaniyah. Then all of Iraq."),
    ]),
    ("Financial feasibility", [
        V("Calm and honest. You are earning trust with numbers."),
        N("Three key tiles appear by themselves."),
        S("Does the math work? Let's follow the money."),
        C("The planned curve appears."),
        V("Slow and clear. A dip, a turn, a payback. Keep it one flowing sentence."),
        S("Planned: it dips, turns profitable in month four, and pays everything back by month eight,"),
        C("The fast curve appears."),
        S("with a growth push, it's even sooner: month three and month six,"),
        C("The slow curve appears."),
        V("Reassuring, with a smile."),
        S("and even at half speed, we're profitable from month seven."),
    ]),
    ("Funding", [
        V("Direct and sincere. No fluff. You are asking for support."),
        L("Look at the judges, not the screen."),
        N("The timeline frame appears by itself."),
        S("5,480 dollars takes Cheapify from an idea to a business."),
        V("From here, keep it one flowing sentence, with a small lift at each comma."),
        C("The pilot block appears."),
        S("A 100-dollar pilot to prove it,"),
        C("The registration block appears."),
        S("1,000 to make it official,"),
        C("The launch block appears."),
        S("840 to open with twenty stores,"),
        C("The runway block appears."),
        S("1,340 to keep us steady through slow months,"),
        C("The growth block appears."),
        S("and 2,200 for growth."),
        P("1 second."),
        C("The \"Less? Still a plan.\" card appears."),
        V("Humble and positive."),
        S("Even with less, there's still a plan."),
        C("The \"No salaries\" bar appears."),
        V("Proud, with a small smile. Slow down on \"computer engineer\"."),
        A("Place a hand on your chest on \"I\"."),
        S("And the platform? I'm a computer engineer and software developer, so I build it all myself."),
    ]),
    ("Thank you", [
        P("1 second before you start. Slow everything down."),
        N("The logo, \"Thank You\", the slogan, the website and the QR code appear together."),
        V("Warm, quiet and sure. This is the last memory they keep."),
        L("Look at the crowd, not the screen."),
        S("Remember that tiny voice, asking \"Did I just overpay?\""),
        P("1 second."),
        V("Bigger, brighter, a smile in the voice. This is your ask."),
        A("Open your hand toward the QR code on the right."),
        S("Help me give it a holiday: scan the code and join the waitlist."),
        V("Slow and proud."),
        S("Cheapify. The bright side of choosing."),
        V("Warm and loud."),
        S("Thank you!"),
        L("Stay silent, smile, and keep the slide up for at least five seconds so people can scan. Wait for the applause."),
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
.auto{background:#eceff2;border-color:#5A6672}.auto .badge{background:#5A6672;color:#fff}
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
