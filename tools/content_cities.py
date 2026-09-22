# -*- coding: utf-8 -*-
"""
Phase 2 — city pages, plus the projects gallery.

ACCURACY RULES:
  * Local facts used here are verifiable: Rockwall and Heath sit in Rockwall
    County on the east side of Lake Ray Hubbard; Rowlett is on the west side;
    the region sits on Blackland Prairie clay with high shrink-swell; the city
    of Rockwall takes its name from a naturally occurring rock wall formation
    found by early settlers.
  * DO NOT claim job counts, years-in-a-specific-city, neighborhood names we
    have worked in, review counts, or awards.
  * DO NOT publish warranty terms. "Fully insured" is fine.
  * Permitting differs by municipality — always phrase as "we'll confirm",
    never state a specific code requirement as fact.
"""

CLAY = """
      <h2>Building on Rockwall County clay</h2>
      <p>This side of the Metroplex sits on Blackland Prairie soil — dense, dark clay with a high shrink-swell capacity. It absorbs water and expands, then dries out in August and contracts. Over a year that is a lot of movement underneath anything you build, and it is the single biggest reason hardscape around here fails early.</p>
      <p>You cannot engineer the clay away. What you can do is build so the movement is anticipated: excavate to proper depth, remove unsuitable material, install and mechanically compact an aggregate base, reinforce properly, and put joints where the stress is going to want to go. That is ordinary, unglamorous work, and it is most of the difference between concrete that looks good for fifteen years and concrete that looks rough in three.</p>
"""

INSURED = """
      <h2>Working with us</h2>
      <p>A&amp;A Exteriors is family-owned, seven years in business, and fully insured. We are based in Rowlett, so this is local work for us, not a market we drive into. Estimates are free and done in person — we look at the actual site, because that is the only way to give you a number that means anything.</p>
      <p>You will get a written scope that spells out what is included before anything starts. Call <a href="tel:+14694967500">469-496-7500</a> or <a href="/estimate">request an estimate online</a>.</p>
"""


PAGES = [
    # ------------------------------------------------- pool deck resurf: Heath
    {
        "url": "/pool-deck-resurfacing-heath-tx",
        "nav_active": "/services",
        "breadcrumbs": [("/services", "Services"), ("/pool-deck-resurfacing", "Pool Deck Resurfacing"),
                        ("/pool-deck-resurfacing-heath-tx", "Heath, TX")],
        "service_type": "Pool Deck Resurfacing",
        "area_served": "Heath, TX",
        "title": "Pool Deck Resurfacing in Heath, TX | A&A Exteriors",
        "description": "Pool deck resurfacing and concrete overlays in Heath, Texas. Cooler, better-gripping decking without tearing out sound concrete. Local Rowlett-based crew. Free estimates.",
        "eyebrow": "Heath, Texas",
        "h1": "Pool deck resurfacing in Heath, TX",
        "intro": "Heath is pool country — large lots, custom homes, and a lot of decking baking in full sun from May to September. If yours is sound underneath but hot, slick, or simply tired, resurfacing renews it without tearing out good concrete.",
        "hero_image": "/images/work-stamped.jpg",
        "cta_h": "Resurfacing your Heath pool deck?",
        "cta_p": "We'll assess the existing concrete on site and tell you honestly whether an overlay will hold.",
        "body": """
  <section class="section">
    <div class="container prose">
      <h2>Why Heath decks end up on our list</h2>
      <p>Heath sits southeast of Rockwall on the lake side of Rockwall County, and the housing stock reflects it: larger lots, plenty of acreage, custom builds, and a high proportion of homes with pools. That combination produces a lot of pool decking — and a lot of it is now old enough to show it.</p>
      <p>The three complaints we hear most from Heath homeowners are always the same. The deck is too hot to cross barefoot in midsummer. It has gone slick where traffic has polished it. Or it simply looks dated and stained next to a house that has been kept up. All three are surface problems, which is exactly what resurfacing addresses.</p>

      <h2>Resurfacing, specifically</h2>
      <p>To be clear about what this service is: we bond a new cementitious layer over your existing concrete. The slab you have stays and becomes the base; the overlay becomes the surface. <strong>This is resurfacing, not replacement</strong> — we do not tear out and repour pool decks. If the assessment shows the concrete underneath is failing, we will say so, because an overlay bonded onto a failing slab inherits every problem the slab has.</p>
      <p>Full detail on the system, the preparation, and the finishes is on our <a href="/pool-deck-resurfacing">pool deck resurfacing page</a>.</p>

      <h2>What we check on a Heath property</h2>
      <ul>
        <li><strong>Movement in the slab.</strong> Hairline and dormant cracks can be treated and bridged. Active, displaced, or widening cracks mean the concrete is still moving and an overlay will crack along the same line.</li>
        <li><strong>Settlement.</strong> An overlay follows whatever contour it is laid on. It cannot raise a sunken section back into plane.</li>
        <li><strong>Bond surface.</strong> Existing sealers, coatings, or flaking surface all have to be dealt with before anything new goes down. Overlays fail at the bond line far more often than in the material.</li>
        <li><strong>Drainage.</strong> Water pooling on the deck now will still pool after resurfacing unless the pitch is addressed.</li>
        <li><strong>Irrigation and sprinkler overspray.</strong> On bigger Heath lots this comes up more than you would think — constant overspray onto decking accelerates staining and mineral deposits.</li>
      </ul>
""" + CLAY + """
      <h2>Heat is the one worth planning around</h2>
      <p>If there is a single decision that determines whether you are happy with a resurfaced deck in Heath, it is color. Lighter finishes reflect materially more heat than dark ones, and on an exposed lot with little mature shade that difference is the difference between a deck you use in July and one you look at.</p>
      <p>Look at samples outdoors, in daylight, not under shop lighting. And go a shade lighter than instinct says — a color reads much brighter across 900 square feet than it does on a sample chip.</p>

      <h2>Permits and HOA</h2>
      <p>Resurfacing an existing deck is a surface finish rather than new structure, but requirements vary by municipality and plenty of Heath neighborhoods have architectural review. We will tell you during the estimate if anything on your project looks like it needs confirmation with the city or your HOA, rather than finding out partway through.</p>
""" + INSURED + """
    </div>
  </section>
""",
        "faqs": [
            ("Do you serve all of Heath?",
             "Yes. We're based in Rowlett, which is a straightforward drive around the lake, and we work throughout Heath and the rest of Rockwall County."),
            ("Do I need to drain the pool?",
             "No. The work happens on the deck. We mask and protect coping, tile, and the waterline, and the pool stays full — you'll just need to stay out of the area during the work and cure."),
            ("My Heath deck has a few cracks. Is it still a candidate?",
             "Often, yes. Hairline and dormant cracking is normal for concrete in Rockwall County clay and can generally be treated and bridged. What rules out an overlay is active movement — cracks that are widening or where the two sides sit at different heights."),
            ("Can you make it cooler underfoot?",
             "Color does most of the work, and lighter finishes reflect more heat. Tell us barefoot comfort is a priority during the estimate and we'll steer the selection that direction."),
        ],
        "related": [
            ("/pool-deck-resurfacing", "Pool Deck Resurfacing", "Full detail on overlay systems, prep, and finishes."),
            ("/concrete-driveway-replacement-heath-tx", "Driveway Replacement in Heath", "Tear-out and replacement for failing Heath driveways."),
            ("/concrete-patios-stamped-concrete", "Stamped Concrete Patios", "Stamped and broom-finish patios across the Metroplex."),
        ],
        "related_heading": "More for Heath homeowners",
    },

    # ------------------------------------------------- driveway replace: Heath
    {
        "url": "/concrete-driveway-replacement-heath-tx",
        "nav_active": "/services",
        "breadcrumbs": [("/services", "Services"), ("/concrete-driveways", "Concrete Driveways"),
                        ("/concrete-driveway-replacement-heath-tx", "Heath, TX")],
        "service_type": "Concrete Driveway Replacement",
        "area_served": "Heath, TX",
        "title": "Concrete Driveway Replacement in Heath, TX | A&A Exteriors",
        "description": "Concrete driveway replacement in Heath, Texas. 3500 PSI concrete, 6\" compacted base, steel reinforcement, full demolition and haul-off. Free written estimates.",
        "eyebrow": "Heath, Texas",
        "h1": "Concrete driveway replacement in Heath, TX",
        "intro": "Heath driveways tend to be long, and long driveways fail in more places. We tear out cracked, settled, and spalling concrete and replace it with a properly based, steel-reinforced 3500 PSI slab.",
        "hero_image": "/images/work-walkway.jpg",
        "cta_h": "Get a written estimate for your Heath driveway.",
        "cta_p": "Free, in-person, and itemized — so you know exactly what's included.",
        "body": """
  <section class="section">
    <div class="container prose">
      <h2>Long driveways, bigger consequences</h2>
      <p>Heath lots run larger than the Metroplex average, and that shows up in the driveways — longer runs, wider approaches, turnarounds, and often a separate path to a shop or secondary garage. More square footage means more base to get right, more joints to place correctly, and more opportunity for a slab to go wrong if the work underneath it was rushed.</p>
      <p>It also means replacement is a real investment, which is exactly why we would rather tell you on the estimate visit that yours is repairable than sell you a pour you do not need.</p>

      <h2>When replacement is the right call</h2>
      <ul>
        <li><strong>Slabs at different heights.</strong> A lip you can catch a toe on means the base beneath has failed. Nothing applied to the surface fixes that.</li>
        <li><strong>Wide or wandering cracks.</strong> Cracks you can get a finger into, particularly ones crossing the slab rather than following a joint, mean it has lost structural integrity.</li>
        <li><strong>Spalling.</strong> Surface flaking off in sheets and exposing aggregate underneath tends to keep progressing once it starts.</li>
        <li><strong>Standing water.</strong> Puddles after rain mean the drainage pitch is gone. Water collecting near the foundation is a far more expensive problem than the driveway itself.</li>
        <li><strong>Pumping at joints.</strong> Mud or fine material appearing at joints after rain means water is moving underneath the slab and taking the base with it.</li>
      </ul>
""" + CLAY + """
      <h2>What's included</h2>
      <p>Our driveway scope is written out so there is nothing ambiguous: complete demolition and disposal of the existing driveway, excavation and removal of unsuitable material, six inches of compacted aggregate base, form materials, steel reinforcement throughout, 3500 PSI ready-mix concrete, control joints at engineered spacing, expansion joint material where new concrete meets existing structures, a professional broom finish, and final site cleanup.</p>
      <p>The full step-by-step process — site prep through cure — is laid out on our <a href="/concrete-driveways">concrete driveways page</a>.</p>

      <h2>Sizing it for what actually drives on it</h2>
      <p>Four inches over a well-compacted six-inch base handles normal residential traffic. On Heath properties that assumption gets tested more often than it does in a subdivision — trailers, RVs, duallies, tractors, boats coming back from the lake. If any of that lives at your house, tell us, and we will size the slab and reinforcement for the real load rather than the average one.</p>

      <h2>Drainage on acreage</h2>
      <p>A driveway is a large impervious surface, and on a bigger lot with more grade change there is more water to manage and further for it to travel. Getting the pitch right means it leaves toward the street or a planned drainage path instead of collecting against the garage or the foundation. On flatter sections this takes genuine grading work during base prep — and it is the step most often skipped by whoever poured the driveway you are now replacing.</p>

      <h2>Access, timeline, and parking</h2>
      <p>Most residential driveways run several days: demolition and haul-off, base work and compaction, forms and steel, the pour, then cure. The cure is the part people underestimate, because the driveway looks finished well before it is ready for a vehicle — and driving on it early is one of the few things that genuinely damages a good pour.</p>
      <p>On a long Heath driveway, parking during the project takes a little planning. We work that out with you before we start, and where it is practical we can stage the work so you keep access longer.</p>

      <h2>Permits</h2>
      <p>Requirements for driveways, culverts, and street approaches vary by municipality, and work in the public right-of-way can carry its own rules. We will flag anything on your project that needs confirming with the City of Heath during the estimate rather than mid-project.</p>
""" + INSURED + """
    </div>
  </section>
""",
        "faqs": [
            ("How long until I can drive on it?",
             "Concrete gains strength progressively and driving on it too early is one of the few ways to damage a good pour. We give you a specific date at the final walkthrough, based on your pour and the weather it cured in."),
            ("Do you haul the old driveway away?",
             "Yes. Complete demolition and disposal is part of the standard scope, along with final site cleanup."),
            ("Can I get a stamped or colored driveway in Heath?",
             "Yes. The same stamping and coloring we use on patios and pool decks works on a driveway — or on just a border or apron, which lifts curb appeal without the cost of stamping the full run."),
            ("My driveway is long. Can you do it in sections?",
             "Sometimes, depending on layout and how the joints fall. It can help preserve access on a long drive. We'll talk through whether it makes sense for your property during the estimate."),
        ],
        "related": [
            ("/concrete-driveways", "Concrete Driveways", "Full process, specs, and what drives cost."),
            ("/pool-deck-resurfacing-heath-tx", "Pool Deck Resurfacing in Heath", "Renew hot or slick decking without tear-out."),
            ("/retaining-walls", "Retaining Walls", "Slope, drainage, and erosion control."),
        ],
        "related_heading": "More for Heath homeowners",
    },

    # ------------------------------------------------ retaining walls: Rockwall
    {
        "url": "/retaining-walls-rockwall-tx",
        "nav_active": "/services",
        "breadcrumbs": [("/services", "Services"), ("/retaining-walls", "Retaining Walls"),
                        ("/retaining-walls-rockwall-tx", "Rockwall, TX")],
        "service_type": "Retaining Wall Construction",
        "area_served": "Rockwall, TX",
        "title": "Retaining Walls in Rockwall, TX | A&A Exteriors",
        "description": "Residential retaining walls in Rockwall, Texas. Proper base, drainage, and soil reinforcement to control slope and erosion on Blackland clay. Free on-site assessment.",
        "eyebrow": "Rockwall, Texas",
        "h1": "Retaining walls in Rockwall, TX",
        "intro": "Rockwall took its name from a rock wall early settlers found running under the ground here. We build the modern kind — engineered walls that hold back slope, stop erosion, and turn an unusable grade into level yard.",
        "hero_image": "/images/work-fireplace.jpg",
        "cta_h": "Let's look at your Rockwall slope.",
        "cta_p": "Free on-site assessment. We'll tell you what the wall actually needs to do.",
        "body": """
  <section class="section">
    <div class="container prose">
      <h2>Slope, lake, and clay</h2>
      <p>Rockwall sits on the east shore of Lake Ray Hubbard, and that geography produces exactly the conditions that call for retaining walls. Lots that fall away toward the water. Newer subdivisions cut into grade. Established neighborhoods where thirty years of runoff has slowly moved the soil downhill. Add Blackland Prairie clay underneath all of it and you have a region where slopes need help staying put.</p>
      <p>The clay is the part that matters most structurally. It swells when it takes on water and shrinks when it dries, which means a wall in Rockwall is not resisting a constant load — it is resisting one that changes every season. Walls built without that in mind are the ones we get called out to look at when they start to lean.</p>

      <h2>What we build walls to do here</h2>
      <ul>
        <li><strong>Reclaim usable yard.</strong> A slope you cannot put a table, a playset, or a garden on is wasted space. A wall converts it into a level terrace you can actually use.</li>
        <li><strong>Stop erosion.</strong> If you lose soil and mulch downhill every heavy rain, a wall plus corrected grading ends the cycle instead of replacing the mulch annually.</li>
        <li><strong>Protect the foundation.</strong> On a sloped Rockwall lot, controlling where water goes keeps it moving away from the house rather than collecting against it.</li>
        <li><strong>Terrace a steep grade.</strong> Two shorter walls are frequently better engineering and better looking than one tall wall doing all the work.</li>
        <li><strong>Add built-in seating.</strong> Seat-height walls around a patio or fire feature give you permanent seating and give a flat yard some structure.</li>
      </ul>

      <h2>Drainage is the whole job</h2>
      <p>Retaining walls almost never fail because the block or stone was inadequate. They fail because water got trapped behind them with nowhere to go, or the base was not built properly, or nobody accounted for the load sitting above the slope.</p>
      <p>So our walls get clean aggregate backfill to give water a path that is not through the soil, drain pipe at the base carrying it out to daylight, and separation fabric so fine clay does not migrate into the aggregate and clog it over the years. None of that is visible when the job is done. All of it determines whether the wall is still straight a decade from now.</p>
""" + CLAY + """
      <h2>How we build</h2>
      <p>We excavate below grade and install a compacted aggregate leveling pad, then set and obsessively check the first course — every error in the bottom course multiplies as the wall rises. Burying that base course below finished grade is what stops the toe of the wall from kicking out. Block is laid with proper setback so the wall leans slightly into the slope it is holding. Taller walls, and walls with a load above them, get geogrid soil reinforcement extending back into the retained soil, which turns the soil mass itself into part of the structure. Caps are set and secured, and the area is backfilled and graded to drain.</p>
      <p>The full build sequence and material options — segmental block, natural stone, and poured concrete — are on our <a href="/retaining-walls">retaining walls page</a>.</p>

      <h2>Height, permits, and engineering in Rockwall</h2>
      <p>Wall height determines what the structure has to do. Past certain heights, or where there is a surcharge load above the wall such as a driveway, pool, or structure, a retaining wall may require engineering and permitting — and requirements differ between municipalities. We will tell you during the estimate if your wall falls into that category rather than discovering it halfway through, and we will confirm specifics with the City of Rockwall as needed.</p>

      <h2>Is your existing wall moving?</h2>
      <p>Look for leaning or bulging, a top course that no longer runs straight, blocks separating out of alignment, soil or water escaping through the face, water pooling behind the wall with no visible outlet, or settlement in the surface above it. A wall that has started moving rarely stops on its own, because whatever started it is still acting on it. Caught early, it is often a repair. Left alone, it becomes a rebuild.</p>
""" + INSURED + """
    </div>
  </section>
""",
        "faqs": [
            ("How tall can a retaining wall be in Rockwall?",
             "It depends on the wall system, the soil, and what's loading it from above. Past certain heights — or where a driveway, pool, or structure sits above — engineering and permitting may be required. Requirements vary by municipality, so we confirm with the city rather than guess."),
            ("Why do so many retaining walls around here lean?",
             "Almost always water, made worse by Blackland clay. Saturated soil behind a wall gets heavier and pushes harder, so with no drainage path the wall is fighting a load it was never built for. Inadequate base prep and skipped soil reinforcement are the other two usual causes."),
            ("Can a wall double as seating around a patio?",
             "Yes, and it's one of the better uses of a low wall — permanent seating without furniture. We detail the cap so it's actually comfortable to sit on."),
            ("Do you repair existing walls or only build new?",
             "Both, depending on why it's moving. If the base and drainage were done right and the problem is localized, repair can make sense. If drainage was never installed, rebuilding is usually the honest answer — we'll tell you which one you have."),
        ],
        "related": [
            ("/retaining-walls", "Retaining Walls", "Materials, full build process, and failure warning signs."),
            ("/stamped-concrete-patio-rockwall-tx", "Stamped Patios in Rockwall", "Level the grade, then build the patio."),
            ("/projects", "Our Projects", "Finished hardscape work around the Metroplex."),
        ],
        "related_heading": "More for Rockwall homeowners",
    },

    # ----------------------------------------------- stamped patio: Rockwall
    {
        "url": "/stamped-concrete-patio-rockwall-tx",
        "nav_active": "/services",
        "breadcrumbs": [("/services", "Services"), ("/concrete-patios-stamped-concrete", "Concrete & Stamped Patios"),
                        ("/stamped-concrete-patio-rockwall-tx", "Rockwall, TX")],
        "service_type": "Stamped Concrete Patio Construction",
        "area_served": "Rockwall, TX",
        "title": "Stamped Concrete Patios in Rockwall, TX | A&A Exteriors",
        "description": "Stamped concrete patios in Rockwall, Texas. The look of stone or flagstone in one monolithic slab — 3500 PSI concrete, compacted base, steel reinforcement. Free estimates.",
        "eyebrow": "Rockwall, Texas",
        "h1": "Stamped concrete patios in Rockwall, TX",
        "intro": "Stamped concrete gives you flagstone, slate, or brick without the individual units that settle, shift, and grow weeds. For Rockwall backyards it is usually the best-looking square footage per dollar you can add.",
        "hero_image": "/images/work-stamped.jpg",
        "cta_h": "Planning a patio in Rockwall?",
        "cta_p": "Free on-site estimate — we'll walk the yard and talk through patterns, colors, and layout.",
        "body": """
  <section class="section">
    <div class="container prose">
      <h2>Why stamped works well here</h2>
      <p>Rockwall backyards have a particular problem: a lot of them came with a builder-grade slab sized for a small table and nothing else. Making that space genuinely usable means more square footage, and once you are adding square footage the finish question comes up immediately.</p>
      <p>Stamped concrete is poured exactly like any other slab, then imprinted with a pattern and colored while it is still workable — ashlar slate, seamless stone, wood plank, running bond brick. The result reads like natural stone or pavers, but it is one monolithic slab. There are no individual units to settle out of plane, shift underfoot, or open up joints for weeds and ants, which on Blackland clay is a meaningful practical advantage over a paver field.</p>

      <h2>Stamped versus broom finish</h2>
      <p>We will lay out both honestly on the estimate. A well-poured broom-finish slab with clean tooled edges and properly placed joints looks intentional, costs less, and stays cooler underfoot than darker finishes. If the patio is going to live mostly under furniture, a grill, and a shade structure, plain concrete is often the smart money.</p>
      <p>Stamped earns its premium when the patio is a focal point — wrapping a pool, fronting an outdoor kitchen, or visible from every window across the back of the house. A common middle path is broom finish in the field with a stamped border, which gives definition at a fraction of the cost of stamping everything.</p>
""" + CLAY + """
      <h2>Patterns, color, and a bit of advice</h2>
      <p>Two things worth knowing before you choose. First, look at samples outdoors in daylight — color reads very differently in Texas sun than under shop lighting, and much brighter across 600 square feet than on a sample board. Second, if the patio gets full afternoon sun and you expect bare feet on it, lean lighter. Dark stamped concrete looks superb in photographs and gets genuinely hot in July.</p>
      <p>On pattern: larger-scale patterns tend to suit larger patios, and tighter patterns like running bond brick can make a small patio feel busy. Matching the stone or brick already on your house is usually a safer bet than introducing a third material.</p>

      <h2>Patio additions and extensions</h2>
      <p>A good share of our Rockwall patio work is extending what is already there rather than replacing it. Where we join new concrete to existing, we saw-cut a clean edge and install an expansion joint at the seam — new and old slabs always move somewhat independently, and the joint is what keeps that movement from cracking either one.</p>

      <h2>Build it for what comes next</h2>
      <p>The cheapest time to plan for a pergola, an outdoor kitchen, or landscape lighting is during the pour. Footings, sleeves, and conduit set now cost very little; retrofitting them later means cutting into a finished patio. If there is any chance a cover or kitchen is coming in a year or two, tell us at the estimate and we will build the provisions in.</p>
      <p>We handle pergolas, outdoor kitchens, fire features, lighting, and retaining walls as well, so a full backyard project can run under one crew rather than four separate trades and four separate schedules. Full detail on patio construction is on our <a href="/concrete-patios-stamped-concrete">concrete and stamped patio page</a>.</p>
""" + INSURED + """
    </div>
  </section>
""",
        "faqs": [
            ("Is stamped concrete cheaper than pavers?",
             "Generally yes, and the bigger difference is long-term. Pavers are individual units that can settle and shift on expansive clay and open joints for weeds. Stamped concrete is one slab, so there's nothing to come out of plane individually."),
            ("Will stamped concrete crack?",
             "Concrete moves — in Rockwall County clay that's unavoidable. The goal is controlled movement: control joints at engineered spacing give the slab planned places to relieve stress, and a compacted base plus steel reinforcement limit how much it moves. Joints are cut into the pattern so they read as part of the design."),
            ("Does stamped concrete get slippery?",
             "The pattern relief provides grip, and sealer choice matters. If the patio is a pool surround, tell us and we'll specify with slip resistance in mind."),
            ("How long does a stamped patio take?",
             "It varies with size, demolition, and access. The pour itself is a day; prep, forming, and cure are what set the schedule. We give you a timeline with the written estimate."),
            ("Can you match my existing patio?",
             "New concrete rarely matches aged concrete exactly — yours has years of weathering the new pour doesn't. Color can get close and stamped or stained finishes give more control. We'd rather set that expectation up front than at the walkthrough."),
        ],
        "related": [
            ("/concrete-patios-stamped-concrete", "Concrete & Stamped Patios", "Full detail on patterns, process, and cost drivers."),
            ("/retaining-walls-rockwall-tx", "Retaining Walls in Rockwall", "Level the slope before you build the patio."),
            ("/pool-deck-resurfacing", "Pool Deck Resurfacing", "Renew existing decking around the pool."),
        ],
        "related_heading": "More for Rockwall homeowners",
    },

    # ------------------------------------------------------------- projects
    {
        "url": "/projects",
        "nav_active": "/projects",
        "breadcrumbs": [("/projects", "Projects")],
        "title": "Our Projects | Concrete & Hardscape Work in Rowlett, Rockwall & Heath TX",
        "description": "Finished concrete, stamped concrete, pool deck, retaining wall and outdoor living projects by A&A Exteriors across Rowlett, Rockwall, Heath and the DFW Metroplex.",
        "eyebrow": "Our Work",
        "h1": "Projects we've finished",
        "intro": "Real work by our own crew — no stock photography. Filter by the kind of project you're considering.",
        "hero_image": "/images/work-fireplace.jpg",
        "cta_h": "Want something like this in your yard?",
        "cta_p": "Free on-site estimates across Rowlett, Rockwall, Heath and the DFW Metroplex.",
        "body": """
  <section class="section">
    <div class="container">
      <div class="filterbar reveal" id="projectFilter">
        <button class="chip is-on" data-filter="all">All projects</button>
        <button class="chip" data-filter="stamped">Stamped Concrete</button>
        <button class="chip" data-filter="concrete">Concrete Flatwork</button>
        <button class="chip" data-filter="outdoor-living">Outdoor Living</button>
        <button class="chip" data-filter="pavers">Pavers</button>
      </div>

      <div class="gallery" id="projectGrid">
        <figure class="gallery-item project" data-tags="outdoor-living" style="background-image:url('/images/work-fireplace.jpg')">
          <figcaption><b>Outdoor Fireplace &amp; Fire Pit</b><span>Covered pavilion, stone fireplace, and a stone fire pit off a finished concrete patio.</span></figcaption>
        </figure>
        <figure class="gallery-item project" data-tags="stamped concrete" style="background-image:url('/images/work-stamped.jpg')">
          <figcaption><b>Stamped Concrete Pool Deck</b><span>Multi-tone stamped stone pattern wrapping a pool and running back to the house.</span></figcaption>
        </figure>
        <figure class="gallery-item project" data-tags="outdoor-living stamped" style="background-image:url('/images/work-pavilion.jpg')">
          <figcaption><b>Covered Patio &amp; Pavilion</b><span>Timber-framed patio cover over a stamped concrete patio.</span></figcaption>
        </figure>
        <figure class="gallery-item project" data-tags="pavers" style="background-image:url('/images/work-pavers.jpg')">
          <figcaption><b>Paver Patio &amp; Walkway</b><span>Large-format pavers set in decorative gravel through a side yard.</span></figcaption>
        </figure>
        <figure class="gallery-item project" data-tags="concrete" style="background-image:url('/images/work-walkway.jpg')">
          <figcaption><b>Concrete Walkway</b><span>Broom-finish walkway with tooled edges and control joints at engineered spacing.</span></figcaption>
        </figure>
        <figure class="gallery-item project" data-tags="concrete" style="background-image:url('/images/work-patio.jpg')">
          <figcaption><b>Concrete Patio Addition</b><span>New patio slab extending usable space off the back of the house, with a drainage channel at the threshold.</span></figcaption>
        </figure>
      </div>

      <p class="center" style="margin-top:2.5rem;color:#6b7364;">More projects are added as we finish them. To see work similar to what you're planning, just ask &mdash; call <a href="tel:+14694967500">469-496-7500</a>.</p>
    </div>
  </section>
""",
        "related": [
            ("/concrete-patios-stamped-concrete", "Concrete & Stamped Patios", "Broom-finish and stamped patios, additions, and extensions."),
            ("/pool-deck-resurfacing", "Pool Deck Resurfacing", "Overlay systems that renew sound pool decking."),
            ("/retaining-walls", "Retaining Walls", "Engineered walls for slope, drainage, and erosion."),
        ],
        "related_heading": "Services shown here",
    },
]
