"""All slide text, numbers and speaker notes (verbatim from the approved spec)."""

# (slide key) -> dict(label, headline, footnote, seconds, notes)
SLIDES = {
    "cover": dict(
        seconds=8,
        notes="Good morning. I'm Shakir Bashar, a computer engineer — and this is Cheapify: the bright side of choosing.",
    ),
    "problem": dict(
        label="Problem",
        headline="Same power bank. 100,000 or 200,000 IQD.",
        footnote="Live app listings captured Oct 20, 2026 (Miswag, iBazzar); Instagram offers from seller posts dated Apr–Oct 2026. Seller names blurred.",
        seconds=30,
        notes="This is one power bank — the Anker 25,000, 165 watt. Same model. On one app's search page, it's listed at 100,000 dinars… [click] and right beside it, at 200,000. [click] Across Instagram and shopping apps, we found it anywhere from 90,000 to 200,000 dinars. [click] That's 122 percent more — for the exact same product.",
    ),
    "evidence": dict(
        label="Problem · evidence",
        headline="It's not one product. It's the whole market.",
        footnote="Screenshots Sep–Oct 2026 (shop names and phone numbers blurred) · Cheapify market survey, n=199 (179 shoppers, 20 merchants), Sep–Oct 2026.",
        seconds=30,
        notes="And it's not one product — it's the whole market. [click] Apps list the same item twice, at two prices. [click] Many Instagram pages hide the price: \"call to order\" — and under the post, someone asks: \"How much is it?\" [click] One app even added a button: \"Found it cheaper? Tell us.\" [click] We surveyed 199 people: 97 percent of shoppers see these gaps — and for merchants, answering \"price?\" messages is the most common headache.",
    ),
    "solution": dict(
        label="Solution",
        headline="One product. One page. Every seller.",
        footnote="Illustration — store names and prices are examples.",
        seconds=30,
        notes="Today, one product is scattered across pages and apps. Cheapify's rule is simple: [click] one product, one page. [click] Every seller of that product sits on it, showing the doorstep total — item plus delivery. [click] Then our Best Value ranking picks the winner: lowest doorstep total, then fastest delivery, then seller rating. And the ranking can never be bought.",
    ),
    "value": dict(
        label="Value proposition",
        headline="Shoppers save. Merchants sell.",
        footnote=None,
        seconds=20,
        notes="For shoppers: [click] every price side by side, an order in thirty seconds, and cash at the door. For merchants: [click] real orders instead of \"price?\" messages, a free dashboard for stock and payouts, and a fair fee — about 3.8 percent on a typical order.",
    ),
    "market": dict(
        label="Target market & customers",
        headline="Duhok first. Then all of Iraq.",
        footnote="Cheapify market survey, n=199, Sep–Oct 2026 · Internet users: DataReportal, Digital 2026: Iraq (late 2025) · E-commerce revenue: ECDB, Iraq 2025 (US$1.32B).",
        seconds=25,
        notes="Our customers are shoppers who buy through Instagram and Facebook — 88 percent said they'd use an app like this — and the social sellers behind those pages: 85 percent sell there, and 75 percent want to try Cheapify. [click] We launch in Duhok, [click] grow to Erbil, Mosul and Sulaymaniyah, [click] then all of Iraq — 39.6 million internet users and a 1.3-billion-dollar e-commerce market.",
    ),
    "product": dict(
        label="Product",
        headline="Order in 30 seconds. Pay at the door.",
        footnote="Concept screens — app in development.",
        seconds=30,
        notes="Here's how it works. A shopper searches for a product. [click] He sees every seller on one page, with Best Value on top. [click] He orders in under thirty seconds and pays cash on delivery. [click] The merchant gets a ready order on the dashboard and WhatsApp, packs it, and the courier picks it up. [click] Every Sunday, the merchant gets paid — minus our small fee.",
    ),
    "model": dict(
        label="Business model",
        headline="We earn only when an order is delivered.",
        footnote="Example: 25,000 IQD item delivered in Duhok city; courier rate 2,500 IQD quoted by Fast Delivery (Duhok). The delivery margin applies once the courier contract is signed.",
        seconds=25,
        notes="We only earn when an order is delivered. Take a 25,000-dinar order: the shopper pays 28,000 at the door. [click] 24,050 goes to the merchant — [click] 2,500 to the courier — [click] and 1,450 to Cheapify: our fee plus a small delivery margin. [click] Our fee gets lighter as prices rise, and after costs we keep about 1,100 dinars per order.",
    ),
    "competitors": dict(
        label="Competitor analysis",
        headline="Nobody else puts every seller on one page.",
        footnote="Based on in-app screenshots (Sep–Oct 2026) and public platform information.",
        seconds=22,
        notes="Look at today's options. [click] On Instagram, prices are often hidden. Miswag and iBazzar show prices, but list the same product more than once. Elryan sells only its own stock. [click] Only Cheapify puts every seller of a product on one page — and compares them for you.",
    ),
    "growth": dict(
        label="Growth strategy",
        headline="Every merchant brings their followers.",
        footnote=None,
        seconds=25,
        notes="Growth starts with merchants. [click] A store joins, [click] adds its Cheapify link to its bio, [click] and its followers order through us — at almost no cost. [click] More orders bring more stores. [click] We start with 20 founding stores in Duhok — first month commission-free, plus free ads — then Erbil, Mosul and Sulaymaniyah, then all of Iraq.",
    ),
    "finance": dict(
        label="Financial feasibility",
        headline="Break-even at about 20 orders a day.",
        footnote="Planning case: orders grow 100 → 2,000 a month; costs 652,000 IQD/month after launch (790,000 from month 6); includes 1.7M IQD startup costs. Assumes 25,000 IQD average order and a signed courier contract. USD at 1,500 IQD.",
        seconds=30,
        notes="Our numbers are deliberately conservative. We break even at about 585 orders a month — around 20 a day, roughly one order per store. [click] On our planning curve, the lowest cash point is about 2,200 dollars, in month three. [click] We break even in month four, [click] and recover everything by month eight. [click] Even at half the growth speed, the worst case stays under 2,800 dollars.",
    ),
    "funding": dict(
        label="Funding",
        headline="$7,500 launches Duhok.",
        footnote=None,
        seconds=25,
        notes="We're asking for 7,500 dollars. [click] It covers the launch gap, growth marketing, registration, merchant kits and a reserve. [click] I build the platform myself, so not one dollar goes to developers or salaries. [click] And at second place, 4,500, or third, 2,500, each amount still funds a complete plan.",
    ),
    "next": dict(
        label="Funding is done — what now?",
        headline="Grant → pilot → launch → break-even.",
        footnote=None,
        seconds=20,
        notes="Once funded: [click] we register and sign the courier contract — the rates are already quoted. [click] We run 10 to 20 real orders by hand. [click] We launch with 20 founding stores. [click] We break even by month four, [click] and then we bring Cheapify to Erbil, Mosul and Sulaymaniyah.",
    ),
    "thanks": dict(
        seconds=6,
        notes="Cheapify — the bright side of choosing. Thank you.",
    ),
}

APPENDIX_NOTE = "Backup for questions."

# -------- slide 4
CHAOS = [  # x, y, source, price text, is_dm
    (1.00, 2.95, "Instagram", "95,000 IQD", False),
    (4.10, 3.35, "Miswag", "200,000 IQD", False),
    (7.60, 2.85, "iBazzar", "134,000 IQD", False),
    (10.20, 3.60, "Instagram", "Price? DM us", True),
    (2.20, 5.30, "Miswag", "100,000 IQD", False),
    (6.00, 5.60, "Instagram", "99,000 IQD", False),
    (9.30, 5.20, "Miswag", "121,000 IQD", False),
]
SELLERS = [
    ("Store A · Duhok", "92,000", "+3,000", "95,000 IQD", "Today"),
    ("Store D · Erbil", "91,000", "+5,000", "96,000 IQD", "1–2 days"),
    ("Store B · Duhok", "99,000", "+3,000", "102,000 IQD", "Today"),
    ("Store C · Duhok", "121,000", "+3,000", "124,000 IQD", "Today"),
]
RANKING = ["Lowest doorstep total", "Fastest delivery", "Best seller rating"]

# -------- slide 2 dot chart (value, channel)
DOTS = [(90000, "IG"), (95000, "IG"), (99000, "IG"), (100000, "IG"), (100000, "MS"),
        (121000, "MS"), (134000, "IB"), (135000, "MS"), (137200, "MS"), (200000, "MS")]

# -------- slide 7 stepper
STEPS = [
    ("Search", "Find any product in one place"),
    ("Compare", "Every seller on one page — Best Value on top"),
    ("Order", "Doorstep total upfront · cash on delivery"),
    ("Merchant packs, courier picks up", "The order lands on the dashboard and WhatsApp"),
    ("Weekly payout", "Paid every Sunday, minus our small fee"),
]

# -------- slide 9 grid: yes / partly / no
COMP_COLS = ["Instagram / Facebook", "Miswag", "iBazzar", "Elryan", "Cheapify"]
COMP_ROWS = [
    ("Prices shown upfront", ["partly", "yes", "yes", "yes", "yes"]),
    ("One page per product", ["no", "no", "no", "yes", "yes"]),
    ("Every seller compared on that page", ["no", "no", "no", "no", "yes"]),
    ("Third-party sellers can join", ["yes", "yes", "yes", "no", "yes"]),
]

# -------- slide 11 chart
CHART_PLANNING = [-1133, -1273, -1413, -1774, -2041, -2178, -2167, -1858, -1382, -719, 130, 1090, 2124]
CHART_SLOW = [-1133, -1273, -1413, -1811, -2160, -2446, -2658, -2721, -2746, -2678, -2517, -2300, -2083]

# -------- slide 12 donut
DONUT = [  # label, usd, degrees, color key
    ("Launch gap (until break-even)", 2200, 105.6, "INK"),
    ("Growth marketing", 2500, 120.0, "BLUE"),
    ("Registration & legal", 1000, 48.0, "INK60"),
    ("Merchant kits & packaging", 900, 43.2, "BLUE50"),
    ("Reserve", 800, 38.4, "NEUTRAL"),
    ("Pilot test (10–20 orders)", 100, 4.8, "ORANGE"),
]

# -------- slide 13
TIMELINE = [
    ("First", "Register & sign the courier contract", "Rates already quoted"),
    ("Next", "Hand-run pilot: 10–20 real orders", "Measure real order size and costs"),
    ("Launch", "20 founding stores go live in Duhok", "0% commission in month 1 + free ads"),
    ("Month 4", "Monthly break-even", "About 600 orders a month"),
    ("Month 7+", "Erbil · Mosul · Sulaymaniyah", "Then all of Iraq"),
]

# -------- appendix
APPENDIX = {
    "A1": dict(
        headline="Fee schedule: lighter as prices rise",
        line="5% on the first 10,000 IQD · 3% on 10,001–100,000 · 1.5% above 100,000 — marginal, like tax brackets: a higher price never pays a lower fee.",
        header=["Item price (IQD)", "Cheapify fee (IQD)", "Effective rate"],
        rows=[["5,000", "250", "5.0%"], ["10,000", "500", "5.0%"], ["25,000", "950", "3.8%"],
              ["45,000", "1,550", "3.4%"], ["100,000", "3,200", "3.2%"],
              ["150,000", "3,950", "2.6%"], ["350,000", "6,950", "2.0%"],
              ["1,200,000", "19,700", "1.6%"]],
    ),
    "A2": dict(
        headline="Unit economics per order",
        header=["Per 25,000 IQD order (Duhok city)", "IQD"],
        rows=[["Platform fee", "+950"],
              ["Delivery margin (3,000 charged − 2,500 courier)", "+500"],
              ["WhatsApp notifications", "−90"], ["Login codes (OTP)", "−25"],
              ["Returns", "−20"], ["Failed-delivery re-attempts", "−200"],
              ["Kept per delivered order", "+1,115"]],
        caption="Break-even (monthly costs 652,000 IQD after launch, incl. a capped 225,000 incentive pool)",
        header2=["Case", "Kept per order", "Break-even orders / month"],
        rows2=[["Base case", "1,115", "~585"], ["Courier contract not signed", "615", "~1,060"],
               ["Average order 20,000 IQD", "965", "~676"],
               ["Incentive pool doubled", "1,115", "~787"]],
    ),
    "A3": dict(
        headline="Three growth scenarios",
        header=["Scenario", "Orders by month 6", "Lowest cash point", "Monthly break-even",
                "All losses recovered"],
        rows=[["Fast (2× plan)", "2,700 / month", "−$1,800 (month 2)", "Month 3", "Month 6"],
              ["Planning", "1,350 / month", "−$2,180 (month 3)", "Month 4", "Month 8"],
              ["Slow (half of plan)", "675 / month", "−$2,750 (month 6)", "Month 7", "~Month 20"]],
        note="Includes 1.7M IQD startup costs and two build months before launch. USD at 1,500 IQD.",
    ),
    "A4": dict(
        headline="Survey: what 199 people told us",
        shoppers_title="Shoppers (179)",
        shoppers=["97% notice price gaps on the same item (39% often see large gaps)",
                  "88% would use a side-by-side app · 10% maybe · 2% prefer DMs",
                  "Top annoyances: untrusted / duplicate pages ~52% · found it cheaper after buying ~47% · DM just to ask the price ~46% · delivery delays ~27%",
                  "~52 usable beta-waitlist contacts"],
        merchants_title="Merchants (20)",
        merchants=["85% sell on Instagram / Facebook",
                   "75% would try Cheapify · 15% maybe (depends on commission) · 10% no",
                   "Top headaches: “price?” DMs 55% · price conflicts 45% · cost of own app/site 35% · manual delivery coordination 35%",
                   "~8 valid pilot-store leads"],
        bottom="Limits: self-selected sample; only 10 Kurdish-language responses; stated intent is not purchases — the hand-run pilot measures real behavior.",
    ),
    "A5": dict(
        headline="Six documented price cases",
        header=["Product", "Lowest", "Highest", "Gap", "Where"],
        rows=[["Anker power bank 25K 165W", "90,000 (Instagram)", "200,000 (Miswag)", "+122%", "Instagram, iBazzar, Miswag"],
              ["ASUS VA24EHF monitor", "135,000 (Elryan)", "163,350 (Miswag)", "+21%", "Elryan, Miswag"],
              ["Hoco HX80 coffee maker", "25,000 (Instagram)", "35,280 (Miswag)", "+41%", "Instagram, Miswag"],
              ["Newal 2000W vacuum", "95,000 (Instagram)", "133,250 (Miswag)", "+40%", "Instagram, Miswag"],
              ["Xiaomi 165W power bank", "60,000", "70,000", "+17%", "Same app (iBazzar)"],
              ["Coffee machines (two posts)", "—", "—", "No price shown", "Instagram: “call / DM to order”"]],
        note="Screenshots Sep–Oct 2026; Instagram posts dated Apr–Oct 2026.",
    ),
    "A6": dict(
        headline="Top risks and how we handle them",
        header=["Risk", "How we handle it"],
        rows=[["Buyers and sellers bypass the app", "Low fee (~3.8%), no contact details on parcels, credits and ratings count only on-platform"],
              ["Slower growth than planned", "Plan is already conservative; half-speed case capped at ~$2,750; hand-run pilot tests demand before spending"],
              ["Courier contract delayed", "Registration first (budgeted); second courier quote as fallback; without the margin, break-even ≈ 1,060 orders/month"],
              ["Failed deliveries (\"not at home\")", "One free re-attempt; 3 failures remove cash-on-delivery; WhatsApp reminder before delivery"],
              ["Courier holds the cash", "Contract fixes custody and timing; weekly settlement"]],
    ),
    "A7": dict(
        headline="How an order flows",
        steps=["Checkout (cash on delivery)", "Merchant accepts", "Sealed package + waybill",
               "Courier pickup", "Delivery + cash collected", "Sunday settlement"],
        lines=["Returns: 48 hours — faulty item: merchant pays the return; change of mind: customer pays 3,000 IQD.",
               "Failed delivery: one free re-attempt, then back to the merchant.",
               "Packaging: opaque and sealed; tamper tape on orders ≥ 50,000 IQD."],
    ),
}
