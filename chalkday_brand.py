from helpers import L, LM, opt, env_names

Q = [
    {"id": "concept", "type": "choice", "prompt": "What kind of spot do you run?",
     "options": [opt("cafe", "Cafe / bakery"), opt("casual", "Casual restaurant"), opt("fine", "Full-service / chef-driven"), opt("bar", "Bar / brewery with food"), opt("truck", "Food truck / pop-up")]},
    {"id": "cuisine", "type": "text", "prompt": "Describe your cuisine in a few words.", "placeholder": "e.g. Oaxacan, Cal-Italian, Ethiopian"},
    {"id": "dayparts", "type": "choice", "multi": True, "prompt": "Which dayparts do you want to promote?", "help": "Select all that apply.",
     "options": [opt("breakfast", "Breakfast / brunch"), opt("lunch", "Lunch"), opt("happy", "Happy hour"), opt("dinner", "Dinner"), opt("late", "Late night")]},
    {"id": "goal", "type": "choice", "prompt": "What should specials help with most?",
     "options": [opt("slow", "Fill a slow day or daypart"), opt("waste", "Use up ingredients / reduce waste"), opt("margin", "Feature higher-margin items"), opt("buzz", "Give regulars something new")]},
    {"id": "slow_day", "type": "choice", "prompt": "Which day is usually your slowest?",
     "options": [opt("mon", "Monday"), opt("tue", "Tuesday"), opt("wed", "Wednesday"), opt("thu", "Thursday"), opt("sun", "Sunday")]},
    {"id": "prep", "type": "choice", "prompt": "How much extra prep can the kitchen handle for a special?",
     "options": [opt("low", "Very little — reuse existing mise"), opt("med", "One new component a week"), opt("high", "A full new dish weekly")]},
    {"id": "channels", "type": "choice", "multi": True, "prompt": "Where do you tell guests about specials?",
     "options": [opt("ig", "Instagram"), opt("gbp", "Google Business updates"), opt("board", "Chalkboard / in-store"), opt("email", "Email / SMS list"), opt("staff", "Staff tell guests")]},
    {"id": "photos", "type": "choice", "prompt": "Who takes food photos?",
     "options": [opt("phone", "Someone with a phone"), opt("pro", "A pro occasionally"), opt("none", "Nobody yet")]},
    {"id": "events", "type": "choice", "prompt": "Any local hook coming up?",
     "options": [opt("holiday", "A holiday"), opt("sports", "Big game / sports season"), opt("market", "Farmers market season"), opt("none", "Nothing specific")]},
]

DAY = {"mon": "Monday", "tue": "Tuesday", "wed": "Wednesday", "thu": "Thursday", "sun": "Sunday"}


def plan(a):
    cuisine = a.get("cuisine") or "your cuisine"
    slow = DAY.get(a.get("slow_day"), "Tuesday")
    goal = a.get("goal", "slow")
    prep = a.get("prep", "med")
    idea = {"low": "a remix of an existing dish (new sauce, new side, family-style portion)", "med": "one new component on a proven base", "high": "a full limited-time dish"}[prep]
    weeks = [
        f"Week 1: ‘{slow} table’ — {idea}, announced the day before.",
        "Week 2: ingredient spotlight using what’s peaking at your supplier.",
        "Week 3: staff-pick week — one cook or server chooses and tells the story.",
        "Week 4: regulars’ favorite returns, framed as a thank-you.",
    ]
    return {
        "title": f"Chalkday 4-week specials calendar — {cuisine}",
        "summary": f"Goal: {L(Q[3]['options'], goal).lower()}. Slowest day: {slow}. Kitchen capacity: {L(Q[5]['options'], prep).lower()}. Channels: {LM(Q[6]['options'], a.get('channels') or ['board'])}. This plan is idea and scheduling support — it doesn’t promise covers or sales.",
        "preview_sections": [
            {"title": "Your 4-week rhythm (unlocked)", "bullets": weeks},
            {"title": "Staff talk track", "body": "One sentence per special: what it is, why it’s special this week, and a pairing. Brief it at pre-shift."},
            {"title": "Costing check", "body": "Before you post, cost each special with your own recipe card and supplier prices. Chalkday gives general menu-planning ideas, not accounting advice."},
        ],
        "locked_sections": [
            {"title": "Daily post + board copy", "teaser": "Captions and chalkboard lines for each special."},
            {"title": "Photo prompts", "teaser": "Angles and lighting tips for phone food photos."},
            {"title": "Holiday & local-event packs", "teaser": "Ideas tied to your upcoming hooks."},
            {"title": "Weekly debrief sheet", "teaser": "What sold, what got wasted, what to repeat."},
        ],
    }


BRAND = {
    "name": "Chalkday", "slug": "chalkday", "port": 5108,
    "tagline": "A weekly specials and promo calendar for independent restaurants and cafes.",
    "eyebrow": "For owner-chefs & GMs",
    "hero_title": "Know what’s on the board every week — before Monday.",
    "hero_lede": "Chalkday asks about your concept, slow days, and kitchen capacity, then builds a 4-week specials rhythm with staff talk tracks and post copy.",
    "cta_primary": "Plan my specials", "cta_short": "Start quiz",
    "cta_band_title": "Less ‘what should we run?’ More service.",
    "cta_band_text": "A month of specials your kitchen can actually execute.",
    "honesty_line": "Menu-planning ideas only. No cover-count or sales guarantees.",
    "audience_line": "Single-location restaurants, cafes, bars, and trucks that want a steady specials habit without a marketing agency.",
    "personas": [
        {"title": "Owner-chef", "text": "Great ideas, no time to plan them."},
        {"title": "GM / marketer", "text": "You need a calendar the kitchen agrees to."},
        {"title": "Cafe owner", "text": "Small menu, regulars who want something new."},
    ],
    "journey": [
        {"stage": "Plan", "pain": "Specials are decided at 4 pm.", "fix": "A 4-week rhythm decided in one sitting."},
        {"stage": "Prep", "pain": "Specials strain the line.", "fix": "Ideas sized to your prep capacity."},
        {"stage": "Promote", "pain": "Nobody knows the special exists.", "fix": "Board lines, posts, and a staff talk track."},
        {"stage": "Review", "pain": "No idea what worked.", "fix": "A 10-minute weekly debrief sheet."},
    ],
    "how_steps": [
        {"title": "Quiz your kitchen", "text": "Concept, slow day, goals, and prep capacity."},
        {"title": "Preview your calendar", "text": "Your 4-week rhythm and staff talk track."},
        {"title": "Start your plan", "text": "Enter your email, then complete checkout on Gumroad."},
    ],
    "features": [
        {"title": "4-week specials rhythm", "text": "Themes that fit your slowest days."},
        {"title": "Staff talk tracks", "text": "One line per special for pre-shift."},
        {"title": "Board + post copy", "text": "Chalkboard lines and captions."},
        {"title": "Seasonal packs", "text": "Subscription: holiday and local-event ideas."},
    ],
    "sample_peek": ["Slow-day table special", "Ingredient spotlight week", "Staff-pick week", "Friday debrief"],
    "trust_points": [
        {"title": "You cost it", "text": "We suggest; your recipe cards decide price."},
        {"title": "Food safety stays yours", "text": "Follow your local health code for every special."},
        {"title": "No health claims", "text": "We don’t write nutrition or medical claims."},
    ],
    "faq": [
        {"q": "Will this increase my sales?", "a": "We don’t promise covers or revenue. Chalkday makes planning and promoting specials consistent."},
        {"q": "Do you post to my Instagram?", "a": "No. You get copy to paste; nothing is posted for you."},
        {"q": "Is food costing included?", "a": "We include a costing checklist. Your actual numbers come from your recipes and suppliers."},
        {"q": "How does billing work?", "a": "Choose Monthly or Quarterly, save your email, then complete payment on Gumroad. Renews automatically. Cancel anytime from your Gumroad library."},
    ],
    "pricing": [
        {"id": "monthly", "name": "Monthly", "price": "$29", "period": "/ month",
             "intro": "$29", "renewal": "$29 / month", "renewal_note": "Renews automatically. Cancel anytime from your Gumroad library.",
             "includes": ['4-week specials calendar', 'Staff talk tracks', 'Board + post copy']},
        {"id": "quarterly", "name": "Quarterly", "price": "$79", "period": "every 3 months",
             "intro": "$79", "renewal": "$79 every 3 months", "renewal_note": "Renews automatically. Cancel anytime from your Gumroad library.", "featured": True,
             "includes": ['Everything in Monthly', 'Holiday & event packs', 'Weekly debrief sheets']},
    ],
    "checkout_url": "https://solvfix.gumroad.com/l/pvjow",
    "disclaimer_short": "Menu-planning ideas only. No sales guarantees. Follow your local food-safety code. No nutrition or health claims.",
    "disclaimer_long": "Chalkday provides general menu-planning and promotional ideas for food businesses. It does not guarantee covers, sales, or profit, is not accounting advice, and does not make nutrition or health claims. Follow your local health department’s food-safety rules for every dish. Payments are processed by Gumroad, not on this site.",
    "font_url": "https://fonts.googleapis.com/css2?family=Caveat+Brush&family=Work+Sans:wght@400;500;700&display=swap",
    "fonts": ("Caveat Brush", "Work Sans"),
    "questions": Q, "generate_plan": plan,
    "voice": "Warm, brisk, kitchen-smart. Short like a pre-shift brief; a little chalkboard charm.",
    "palette": {"Background (chalkboard)": "#1E2B26", "Alt": "#24332D", "Card": "#2A3A33", "Chalk text": "#F3F0E6", "Muted": "#B7BFB4", "Accent (tomato)": "#F2643A", "Accent hover": "#D94E26", "Highlight (butter)": "#F7D774"},
    "logo_svg": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none"><rect width="64" height="64" rx="12" fill="#F2643A"/><rect x="13" y="15" width="38" height="28" rx="3" fill="#1E2B26"/><path d="M20 24h16M20 30h22M20 36h12" stroke="#F3F0E6" stroke-width="3" stroke-linecap="round"/><path d="M22 43l-4 8M42 43l4 8" stroke="#1E2B26" stroke-width="3.5" stroke-linecap="round"/></svg>',
    "css_vars": """
  --bg:#1E2B26;--bg-alt:#24332D;--card:#2A3A33;--ink:#F3F0E6;--muted:#B7BFB4;--line:#3D5048;
  --accent:#F2643A;--accent-2:#D94E26;--on-accent:#1E1208;--hi:#F7D774;--radius:12px;
  --font-display:'Caveat Brush', 'Comic Sans MS', cursive;--font-body:'Work Sans', system-ui, sans-serif;
  --shadow-card:0 16px 36px rgba(0,0,0,.35);--shadow-btn:0 8px 20px rgba(242,100,58,.3);
  --cta-band-bg:#F7D774;--cta-band-ink:#1E2B26;--cta-band-btn:#1E2B26;--cta-band-btn-ink:#F7D774;--tracking:0;
""",
    "personality": "background:radial-gradient(700px 360px at 80% 10%, rgba(247,215,116,.12) 0%, transparent 60%), var(--bg);",
    "extra_css": "h1{font-size:clamp(2.6rem,6vw,4.4rem);line-height:1}h2{font-size:clamp(2rem,4vw,2.8rem)}h3{font-family:var(--font-body);font-weight:700}.eyebrow{font-family:var(--font-body)}.amount{font-family:var(--font-body)}.journey-card{border-top:3px dashed var(--hi)}",
    "dos": ["Talk like a kitchen: mise, pre-shift, 86’d.", "Remind owners to cost every special and follow health code."],
    "donts": ["Make nutrition, diet, or health claims.", "Promise more covers or sales."],
}
BRAND.update(env_names("chalkday"))
