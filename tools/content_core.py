# -*- coding: utf-8 -*-
"""
Phase 1 — core service pages.

ACCURACY RULES (do not break when editing):
  * Concrete specs below (3500 PSI, 4" slab, 6" compacted base, steel
    reinforcement, control + expansion joints, broom finish, demo & haul-off,
    final walkthrough) come from A&A's own Concrete Driveway Proposal.
  * "Fully insured" is stated in that same proposal.
  * DO NOT publish warranty terms — they are set per proposal.
  * DO NOT publish prices, crew counts, review counts, or awards.
  * Pool deck page is RESURFACING / OVERLAYS ONLY — never promise new pours
    or tear-out-and-replace on that page.
"""

SPECS = """
      <div class="spec-grid reveal">
        <div class="spec"><b>3500 PSI</b><span>Ready-mix concrete</span></div>
        <div class="spec"><b>4"</b><span>Standard slab thickness</span></div>
        <div class="spec"><b>6"</b><span>Compacted aggregate base</span></div>
        <div class="spec"><b>Steel</b><span>Reinforcement throughout</span></div>
      </div>
"""

PROCESS_CONCRETE = """
      <h2>How we pour concrete that stays flat</h2>
      <p>Most of the concrete failures we get called out to look at are not concrete problems. They are base problems. North Texas sits on expansive clay that swells when it rains and shrinks when it bakes, and a slab is only ever as stable as what is underneath it. That is why the least visible part of our process is the part we are most particular about.</p>

      <h3>1. Site preparation</h3>
      <p>We verify measurements and layout, contact the utility locating service before anything goes in the ground, and protect the landscaping, sidewalks, and structures we are working around. Where we are tying into existing concrete, we saw-cut a clean transition joint rather than butting new against old and hoping for the best.</p>

      <h3>2. Excavation and base</h3>
      <p>Existing concrete is demolished and hauled off. We excavate to proper depth, remove unsuitable soil and organic material, then install roughly six inches of crushed aggregate base and compact it with mechanical equipment. Fine grading sets the drainage — always away from the house and the garage, never toward it.</p>

      <h3>3. Forms and reinforcement</h3>
      <p>Heavy-duty forming lumber goes in, and we verify elevation, pitch, and finished dimensions before bracing the forms so nothing moves during the pour. Steel reinforcement is installed throughout and properly supported so it sits centered in the slab, where it can actually do its job of adding structural strength and limiting cracking.</p>

      <h3>4. Placement and joints</h3>
      <p>We pour 3500 PSI ready-mix continuously to minimize cold joints, then screed, level, and consolidate to eliminate air pockets. Control joints go in at engineered spacing and expansion joints wherever the new concrete meets an existing structure. Concrete is going to move. Joints decide whether it moves where we planned or where it wants to.</p>

      <h3>5. Finish and cure</h3>
      <p>Edges are tooled for durability and appearance, and the surface gets a professional broom finish for traction. Then it cures using standard industry practice — which mostly means leaving it alone for the right amount of time, something that matters more in a Texas August than people expect. Forms come off after the appropriate cure, the work area is cleaned completely, and we walk the finished job with you.</p>
"""

WHY_LOCAL = """
      <h2>Why local matters</h2>
      <p>Soil behavior is regional. The clay under Rowlett, Rockwall, and Heath moves differently than soil two hours in any direction, and the crews who work here every week build for that by habit. We are based in Rowlett, our founders live here, and we drive past our own work on the way to yours — which is a decent accountability system on its own.</p>
      <p>A&amp;A Exteriors is family-owned, seven years in business, and fully insured. Estimates are free, in person, and come with a written scope so you know exactly what is included before anything starts.</p>
"""


PAGES = [
    # ---------------------------------------------------------------- patios
    {
        "url": "/concrete-patios-stamped-concrete",
        "nav_active": "/services",
        "breadcrumbs": [("/services", "Services"), ("/concrete-patios-stamped-concrete", "Concrete & Stamped Patios")],
        "service_type": "Stamped Concrete Patio Construction",
        "title": "Stamped Concrete Patios in Rowlett, Rockwall & Heath TX | A&A Exteriors",
        "description": "Custom concrete and stamped concrete patios in Rowlett, Rockwall, Heath and the DFW area. 3500 PSI concrete, compacted base, steel reinforcement. Free estimates.",
        "eyebrow": "Concrete & Stamped Patios",
        "h1": "Concrete and stamped concrete patios",
        "intro": "A patio is the piece of the backyard you actually live on. We build them to hold up to North Texas heat, clay movement, and a decade of cookouts — in broom-finish concrete or stamped patterns that read like stone at a fraction of the cost.",
        "hero_image": "/images/work-stamped.jpg",
        "cta_h": "Let's design your patio.",
        "cta_p": "Free on-site estimates in Rowlett, Rockwall, Heath and across the DFW Metroplex.",
        "body": """
  <section class="section">
    <div class="container prose">
      <h2>Two ways to build a patio</h2>
      <p>Nearly every patio conversation we have starts in the same place: should it be plain concrete or stamped? The honest answer depends on the house, the budget, and how much of the yard the patio is going to dominate.</p>

      <h3>Broom-finish concrete</h3>
      <p>Straightforward, durable, and the most cost-effective square footage you can add to a backyard. A well-poured broom-finish slab with clean tooled edges and properly spaced joints looks intentional rather than cheap, and it stays cooler underfoot than most darker finished surfaces. If the patio is largely going to live under furniture, a grill, and a shade structure, plain concrete is often the smart money.</p>

      <h3>Stamped concrete</h3>
      <p>Stamped concrete is poured the same way, then imprinted with a pattern and color while it is still workable — ashlar slate, seamless stone, wood plank, running bond brick. You get the look of flagstone or pavers as a single monolithic slab, which means no individual units to settle, shift, or grow weeds between. It is the finish in most of the pool deck and patio photos on this site.</p>
      <p>Stamped costs more than broom finish and is worth it when the patio is a focal point — wrapping a pool, fronting an outdoor kitchen, or visible from every window on the back of the house.</p>
""" + SPECS + """
    </div>
  </section>

  <section class="section" style="background:var(--cream-2);">
    <div class="container prose">
""" + PROCESS_CONCRETE + """
    </div>
  </section>

  <section class="section">
    <div class="container prose">
      <h2>What drives the cost of a patio</h2>
      <p>We give written estimates rather than square-foot rules of thumb, because the variables genuinely move the number:</p>
      <ul>
        <li><strong>Size and shape.</strong> Square and rectangular pours are the most efficient. Curves, radiuses, and multi-level designs add forming labor.</li>
        <li><strong>Finish.</strong> Broom finish is the baseline. Stamping adds pattern work, color, and release agents. Multiple colors or borders add more.</li>
        <li><strong>Demolition.</strong> Replacing an existing slab means tear-out and haul-off before anything new gets poured.</li>
        <li><strong>Access.</strong> If a truck can reach the pour, the job is simpler. Tight side yards and locked-in backyards mean wheelbarrowing or pumping.</li>
        <li><strong>Grade and drainage.</strong> A flat, well-draining site is straightforward. Slopes, low spots, and water running toward the foundation require work before the pour.</li>
        <li><strong>Add-ons.</strong> Steps, seat walls, footings for a pergola, or sleeves for future lighting are easier and cheaper to build in now than to retrofit.</li>
      </ul>

      <h2>Patio additions and extensions</h2>
      <p>A lot of our patio work is not a new patio at all — it is making an existing one big enough to be useful. Builder-grade patios are frequently sized for a small table and nothing else. Extending out to fit a seating area, a grill run, or a dining table often transforms how much the backyard gets used, for meaningfully less than a full tear-out.</p>
      <p>Where we join new concrete to old, we saw-cut a clean edge and install an expansion joint at the seam. New and existing slabs will always move somewhat independently; the joint is what keeps that movement from cracking either one.</p>
""" + WHY_LOCAL + """
    </div>
  </section>
""",
        "faqs": [
            ("How long before I can use a new concrete patio?",
             "You can typically walk on it within a day or so, but concrete gains strength over time and we ask that you keep furniture and heavier loads off it during the initial cure. We'll give you the specific timeline for your pour at the final walkthrough, since weather affects it."),
            ("Will my concrete patio crack?",
             "Concrete moves — that is normal, and in North Texas clay it is unavoidable. The goal is not zero movement, it is controlled movement. Control joints at engineered spacing give the slab planned places to relieve stress, and steel reinforcement plus a properly compacted base limit how much it moves in the first place."),
            ("Is stamped concrete slippery around a pool?",
             "Texture and sealer choice matter here. Stamped patterns have surface relief that provides grip, and finishes can be specified with slip resistance in mind. Tell us the patio is a pool surround and we'll account for it."),
            ("Can you match a patio to my existing concrete?",
             "New concrete rarely matches aged concrete exactly — the existing slab has years of weathering and the new pour does not. Color can get close, and stamped or stained finishes give more control. We'd rather set expectations honestly up front than surprise you at the walkthrough."),
            ("Do you build patio covers and pergolas too?",
             "Yes. We build pergolas, patio covers, outdoor kitchens, fire features, and lighting, so a patio project can be coordinated under one crew rather than juggling trades. If you know a cover is coming later, we can set footings during the pour."),
        ],
        "related": [
            ("/concrete-driveways", "Concrete Driveways", "Replacement and new driveways built on a properly compacted base."),
            ("/pool-deck-resurfacing", "Pool Deck Resurfacing", "Resurface tired pool decking without tearing out sound concrete."),
            ("/retaining-walls", "Retaining Walls", "Engineered walls that control slope, drainage, and erosion."),
        ],
        "related_heading": "Related services",
    },

    # ------------------------------------------------------------- driveways
    {
        "url": "/concrete-driveways",
        "nav_active": "/services",
        "breadcrumbs": [("/services", "Services"), ("/concrete-driveways", "Concrete Driveways")],
        "service_type": "Concrete Driveway Construction and Replacement",
        "title": "Concrete Driveway Replacement in Rowlett, Rockwall & Heath TX | A&A Exteriors",
        "description": "Concrete driveway replacement and new driveways in Rowlett, Rockwall, Heath and DFW. 3500 PSI concrete, 6\" compacted base, steel reinforcement. Free written estimates.",
        "eyebrow": "Concrete Driveways",
        "h1": "Concrete driveway replacement",
        "intro": "A failing driveway is the first thing anyone sees of your house. We tear out cracked, settled, and spalling concrete and replace it with a properly based, steel-reinforced 3500 PSI slab built to carry vehicle loads for the long haul.",
        "hero_image": "/images/work-walkway.jpg",
        "cta_h": "Get a written driveway estimate.",
        "cta_p": "Free on-site estimates with a full written scope — no obligation, no pressure.",
        "body": """
  <section class="section">
    <div class="container prose">
      <h2>When a driveway needs replacing rather than patching</h2>
      <p>Not every crack means tear-out. Hairline cracking at control joints is concrete doing what concrete does. What tells us a driveway is past repair is usually one of these:</p>
      <ul>
        <li><strong>Sections at different heights.</strong> When slabs have settled against each other and you can catch a toe on the lip, the base beneath has failed. Resurfacing over that just hides it temporarily.</li>
        <li><strong>Wide or branching cracks.</strong> Cracks you can fit a finger into, especially ones that wander across the slab rather than following a joint, mean the slab has lost structural integrity.</li>
        <li><strong>Spalling and flaking.</strong> Surface popping off in sheets or chips, exposing aggregate underneath, usually points to a finish or freeze-cycle problem that will keep progressing.</li>
        <li><strong>Standing water.</strong> Puddles that sit after rain mean the drainage pitch is gone — and water pooling against your foundation is a much more expensive problem than a driveway.</li>
        <li><strong>Pumping at joints.</strong> Mud or fines appearing at joints after rain mean water is moving under the slab and carrying the base away with it.</li>
      </ul>
      <p>If what you have is genuinely repairable, we would rather tell you that on the estimate visit than sell you a pour you do not need.</p>
""" + SPECS + """
    </div>
  </section>

  <section class="section" style="background:var(--cream-2);">
    <div class="container prose">
""" + PROCESS_CONCRETE + """
      <h3>What's included in the scope</h3>
      <p>Our driveway proposals spell out the materials so nothing is ambiguous: 3500 PSI ready-mix concrete, steel reinforcement, six inches of compacted aggregate base, form materials, expansion joint material, control joints, professional broom finish, complete demolition and disposal of the old driveway, and final site cleanup.</p>
    </div>
  </section>

  <section class="section">
    <div class="container prose">
      <h2>Thickness, reinforcement, and why they matter</h2>
      <p>Four inches over a well-compacted six-inch base handles residential vehicle traffic. What changes that math is load. If you park an RV, a dually, a loaded trailer, or run heavy equipment across an apron, the slab should be thicker and the reinforcement heavier in those areas. Tell us what actually drives on it, including the truck that delivers to your house, and we will size it accordingly.</p>
      <p>Steel reinforcement does not prevent cracks. It holds the slab together across cracks that do form, keeping the two sides in plane so you never get the vertical displacement that ruins a driveway. That is why we support it properly rather than laying it on grade and pouring over it — steel sitting on the bottom of the slab does very little.</p>

      <h2>Drainage is the other half of the job</h2>
      <p>A driveway is a large impervious surface pointed at your house. Getting the pitch right means water leaves toward the street or a planned drainage path instead of collecting against the garage slab or the foundation. On flatter lots this takes real grading work during base prep, and it is the part of the job most likely to be skipped by whoever poured the driveway you are replacing.</p>

      <h2>What to expect on timeline</h2>
      <p>Most residential driveways are a multi-day job: demolition and haul-off, base work and compaction, forming and steel, the pour, then curing. The part people underestimate is the cure — the driveway looks finished long before it is ready for a vehicle. Driving on it too early is one of the few ways to damage a good pour, so we give you a specific date at the walkthrough and we would rather you wait an extra day than an hour too few.</p>
      <p>We'll also talk through parking during the project. For most homes it means a few days on the street, and knowing that in advance is easier than discovering it the morning the saw starts.</p>
""" + WHY_LOCAL + """
    </div>
  </section>
""",
        "faqs": [
            ("How long until I can drive on a new concrete driveway?",
             "Concrete gains strength progressively, and driving on it too early is one of the few things that can genuinely damage a good pour. We give you a specific date at the final walkthrough based on your pour and the weather it cured in."),
            ("Do you haul away the old driveway?",
             "Yes. Complete demolition and disposal of the existing concrete is part of our standard driveway scope, along with final site cleanup."),
            ("Can you pour a stamped or colored driveway?",
             "Yes. The same stamping and coloring we use on patios and pool decks can be applied to a driveway, or used just on a border or apron for a more restrained look that still lifts the curb appeal."),
            ("Will you need to call utility locates?",
             "We contact the utility locating service before we excavate on every job. It's a standard part of our site preparation, not an extra."),
            ("What about the sidewalk and approach?",
             "Public sidewalk and street approach work can fall under city requirements depending on your municipality. We'll flag anything in that category during the estimate so there are no surprises mid-project."),
        ],
        "related": [
            ("/concrete-patios-stamped-concrete", "Concrete & Stamped Patios", "Broom-finish and stamped patios, additions, and extensions."),
            ("/pool-deck-resurfacing", "Pool Deck Resurfacing", "Overlay systems that renew sound pool decking."),
            ("/retaining-walls", "Retaining Walls", "Slope control, drainage, and usable level ground."),
        ],
        "related_heading": "Related services",
    },

    # ------------------------------------------------------- pool deck resurf
    {
        "url": "/pool-deck-resurfacing",
        "nav_active": "/services",
        "breadcrumbs": [("/services", "Services"), ("/pool-deck-resurfacing", "Pool Deck Resurfacing")],
        "service_type": "Pool Deck Resurfacing",
        "title": "Pool Deck Resurfacing in Rowlett, Rockwall & Heath TX | A&A Exteriors",
        "description": "Pool deck resurfacing and concrete overlays in Rowlett, Rockwall, Heath and the DFW area. Renew worn, hot, or slick pool decking without tearing out sound concrete.",
        "eyebrow": "Pool Deck Resurfacing",
        "h1": "Pool deck resurfacing",
        "intro": "If your pool deck is structurally sound but looks tired, stains easily, or gets punishingly hot underfoot, you may not need to tear it out. A bonded overlay resurfaces what you already have — new texture, new color, a fraction of the disruption.",
        "hero_image": "/images/work-stamped.jpg",
        "cta_h": "Find out if your deck is a resurfacing candidate.",
        "cta_p": "We'll assess the existing concrete on site and tell you honestly whether an overlay will hold.",
        "body": """
  <section class="section">
    <div class="container prose">
      <h2>What resurfacing actually is</h2>
      <p>Resurfacing means bonding a new cementitious layer over your existing concrete rather than removing it. The old slab stays where it is and becomes the structural base; the overlay becomes the surface you see, walk on, and clean. Done properly, it changes the texture, color, and pattern of the deck completely.</p>
      <p>It is a genuinely different service from pouring a new deck, and it is the one we specialize in. <strong>We resurface existing decking — we do not tear out and repour pool decks.</strong> If your assessment shows the slab underneath is failing, we will tell you that plainly, because an overlay bonded to bad concrete inherits every one of its problems.</p>

      <h2>Is your deck a candidate?</h2>
      <p>Resurfacing works when the concrete underneath is sound. During the estimate we look at:</p>
      <ul>
        <li><strong>Structural cracking.</strong> Hairline and surface cracks can usually be addressed and bridged. Wide, actively moving, or displaced cracks mean the slab is still shifting, and anything bonded on top will crack again along the same line.</li>
        <li><strong>Settlement.</strong> Sections sitting at noticeably different heights indicate base failure below. An overlay follows the contour it is applied to; it cannot lift a sunken slab back into plane.</li>
        <li><strong>Delamination and spalling.</strong> If the existing surface is already flaking or popping loose, the overlay has nothing solid to bond to. Sometimes this is localized and repairable, sometimes it is widespread.</li>
        <li><strong>Prior coatings.</strong> Old sealers, paint, or previous coating systems affect bond and may need mechanical removal before anything new goes down.</li>
        <li><strong>Drainage.</strong> Water that currently pools on the deck will still pool on a resurfaced deck unless the pitch is corrected. Overlays can help modestly with minor low spots, but they are not a regrading tool.</li>
      </ul>

      <h2>Why people resurface</h2>
      <h3>Heat</h3>
      <p>A dark or dense pool deck in a Texas July is genuinely unusable barefoot. Lighter colors and textured overlay finishes reflect more and hold less heat, which for a lot of families is the entire reason the deck gets used again.</p>

      <h3>Slip resistance</h3>
      <p>Worn, polished, or slick decking around water is a real hazard. Textured overlay finishes restore grip, and texture can be specified to taste — enough to be safe without being abrasive to bare feet and swimsuits.</p>

      <h3>Appearance</h3>
      <p>Staining, discoloration, patchwork repairs, and dated finishes all disappear under an overlay. Stamped and textured overlay systems can read as stone, tile, or flagstone, which is often a dramatic change for a deck that was plain gray broom finish.</p>

      <h3>Cost and disruption</h3>
      <p>Because there is no demolition, no haul-off, and no new structural pour, resurfacing is typically a shorter and less invasive project than replacement — which matters when the work is happening in a fenced backyard around a full pool.</p>
    </div>
  </section>

  <section class="section" style="background:var(--cream-2);">
    <div class="container prose">
      <h2>How the work goes</h2>

      <h3>1. Assessment</h3>
      <p>We walk the deck with you, look for movement and delamination, check drainage, and identify any prior coatings. This is where we confirm the deck is a resurfacing candidate — and say so if it is not.</p>

      <h3>2. Surface preparation</h3>
      <p>Preparation is the whole job. The existing surface is cleaned and mechanically profiled so the overlay has something to key into, contaminants and failed coatings are removed, and cracks and defects are addressed before anything is applied. Overlays fail at the bond line far more often than they fail in the material itself.</p>

      <h3>3. Protection</h3>
      <p>Coping, tile, waterline, and the pool itself get masked and protected. So does surrounding landscape and any adjacent hardscape we are not resurfacing.</p>

      <h3>4. Application and finish</h3>
      <p>The overlay is applied and worked to the texture and pattern you chose, then colored to the selection you approved. Edges and transitions are detailed where the deck meets coping, structures, and existing hardscape.</p>

      <h3>5. Cure and sealing</h3>
      <p>The system cures, gets sealed as specified, and we walk the finished deck with you. You will need to keep the deck clear and stay out of the pool area for a period during cure — we give you specific timing before we start, so you can plan around it.</p>

      <h2>Choosing color and texture</h2>
      <p>Two practical pieces of advice. First, look at samples outdoors in daylight rather than under shop lighting, because color reads very differently in full Texas sun. Second, go lighter than instinct tells you if heat is a concern — the deck will look brighter than the sample once it is 800 square feet instead of a six-inch chip, and the temperature difference underfoot is real.</p>
""" + WHY_LOCAL + """
    </div>
  </section>
""",
        "faqs": [
            ("Do I have to drain my pool?",
             "No. Resurfacing happens on the deck, not in the pool. We mask and protect the coping, tile, and water, and the pool stays full — though you'll need to stay out of the area during the work and cure."),
            ("How long does the pool deck take?",
             "It depends on square footage, how much preparation and crack repair the existing surface needs, and the finish system. We give you a schedule before we start, including exactly how long you need to stay off the deck."),
            ("Will the old cracks come back through?",
             "Hairline and dormant cracks can generally be treated and bridged. Cracks that are still actively moving will eventually telegraph through any bonded overlay — that's physics, not workmanship. If we see active movement during the assessment, we'll tell you an overlay isn't the right answer."),
            ("Is a resurfaced deck cooler than plain concrete?",
             "Color is the biggest factor: lighter finishes reflect more heat than dark ones. Texture helps too. If barefoot comfort is your main goal, say so during the estimate and we'll steer the color selection accordingly."),
            ("Can you resurface just part of the deck?",
             "We can, but be aware that a partial overlay will read as a different surface from the untreated concrete next to it — different texture, different color, different weathering over time. Usually it looks intentional only if there's a natural break line to stop at."),
            ("Do you pour new pool decks?",
             "Pool deck resurfacing is what we do here — bonded overlays over existing sound concrete. If your deck needs full replacement, our concrete crew handles patios and flatwork, and we can talk through what that would involve on the estimate visit."),
        ],
        "related": [
            ("/concrete-patios-stamped-concrete", "Concrete & Stamped Patios", "Stamped and broom-finish patios, additions, and extensions."),
            ("/concrete-driveways", "Concrete Driveways", "Full replacement when concrete is past resurfacing."),
            ("/projects", "Our Projects", "Real finished work from around the DFW Metroplex."),
        ],
        "related_heading": "Related services",
    },

    # -------------------------------------------------------- retaining walls
    {
        "url": "/retaining-walls",
        "nav_active": "/services",
        "breadcrumbs": [("/services", "Services"), ("/retaining-walls", "Retaining Walls")],
        "service_type": "Retaining Wall Construction",
        "title": "Retaining Walls in Rowlett, Rockwall & Heath TX | A&A Exteriors",
        "description": "Engineered residential retaining walls in Rowlett, Rockwall, Heath and the DFW area. Proper drainage, base, and backfill to control slope and erosion. Free estimates.",
        "eyebrow": "Retaining Walls",
        "h1": "Retaining walls built to hold",
        "intro": "A retaining wall is a structure doing a structural job: holding back soil that wants to move. Built right, it turns an unusable slope into level, planted, living space. Built wrong, it leans, bulges, and eventually comes apart.",
        "hero_image": "/images/work-fireplace.jpg",
        "cta_h": "Let's look at your slope.",
        "cta_p": "Free on-site assessment across Rowlett, Rockwall, Heath and the DFW Metroplex.",
        "body": """
  <section class="section">
    <div class="container prose">
      <h2>What a retaining wall is actually fighting</h2>
      <p>Soil behind a wall is not static weight sitting still. It pushes laterally, and that push increases dramatically when the soil gets wet. North Texas clay makes this worse than most: it swells as it absorbs water and shrinks as it dries, so a wall here is resisting a load that changes with the season.</p>
      <p>This is why the walls that fail almost never fail because the blocks or stones were bad. They fail because water got trapped behind them and had nowhere to go, or because the base was not adequate, or because nobody accounted for what was sitting on top of the slope. Drainage is not a detail on a retaining wall. It is the job.</p>

      <h2>Reasons to build one</h2>
      <ul>
        <li><strong>Reclaiming usable yard.</strong> A slope you cannot put a table, a playset, or a garden bed on is wasted square footage. A wall converts it into a level terrace.</li>
        <li><strong>Stopping erosion.</strong> If you are losing soil, mulch, or topsoil downhill every time it rains hard, a wall plus proper grading ends the cycle.</li>
        <li><strong>Protecting the foundation.</strong> Controlling where water goes on a sloped lot keeps it moving away from the house rather than collecting against it.</li>
        <li><strong>Defining outdoor rooms.</strong> Seat-height walls create built-in seating around a fire feature or patio and give a flat yard structure and edge.</li>
        <li><strong>Tiering a steep grade.</strong> Two shorter terraced walls are often better engineering — and better looking — than one tall wall trying to do everything.</li>
      </ul>

      <h2>Materials</h2>
      <h3>Segmental block</h3>
      <p>Manufactured modular block is the workhorse of residential retaining walls. It is engineered for the purpose, installs with consistent alignment and setback, and comes in a wide range of colors and face textures. For most residential heights it is the best balance of performance, appearance, and cost.</p>

      <h3>Natural stone</h3>
      <p>Quarried stone gives a wall character that manufactured units cannot quite replicate, with variation in tone and texture that looks like it belongs to the landscape rather than sitting on it. It is more labor-intensive to build and generally the premium option.</p>

      <h3>Poured concrete</h3>
      <p>For certain conditions a poured, reinforced concrete wall is the right structural answer, and it can be faced or finished to suit the property. This is the same crew and the same standards as our flatwork.</p>
    </div>
  </section>

  <section class="section" style="background:var(--cream-2);">
    <div class="container prose">
      <h2>How we build a wall that stays put</h2>

      <h3>1. Assessment and layout</h3>
      <p>We look at the height you need, what is above and below the wall, how water currently moves across the site, and what is going to sit behind it. A wall holding back a flat lawn is a very different structure from one holding back a driveway or a slope that drains half the yard.</p>

      <h3>2. Excavation and base</h3>
      <p>We excavate below grade and install a compacted aggregate base — the leveling pad the entire wall depends on. The first course is set and checked obsessively, because every error in the bottom course multiplies as the wall goes up. Burying the base course below finished grade is what keeps the toe of the wall from kicking out.</p>

      <h3>3. Drainage</h3>
      <p>Clean aggregate backfill goes in behind the wall to give water a path that is not through the soil, with drain pipe at the base to carry it out to daylight. Separation fabric keeps fine soil from migrating into the aggregate and clogging it over time. This is the part nobody sees and the part that determines whether the wall is still straight in ten years.</p>

      <h3>4. Courses and reinforcement</h3>
      <p>Block is laid with the proper setback so the wall leans slightly into the slope it is holding. Taller walls and walls with loads above them get geogrid soil reinforcement extending back into the retained soil, which effectively turns the soil mass itself into part of the structure.</p>

      <h3>5. Cap and finish</h3>
      <p>Caps are set and secured, backfill is brought to final grade, and the area around the wall is cleaned up and graded to drain. Where a wall doubles as seating, we detail the cap for comfortable sitting.</p>

      <h2>Height, permits, and engineering</h2>
      <p>Wall height is not just an aesthetic decision — it determines what the structure has to do. Beyond certain heights, or where there is a surcharge load above the wall such as a driveway, pool, or structure, a retaining wall may require engineering and permitting depending on your municipality. Rowlett, Rockwall, and Heath each have their own requirements.</p>
      <p>We will tell you during the estimate if your wall falls into that category rather than discovering it halfway through. Sometimes the better answer is two terraced walls instead of one tall one, which can improve both the engineering and the way the yard actually looks.</p>

      <h2>Signs an existing wall is in trouble</h2>
      <ul>
        <li>Leaning, bulging, or a top course that no longer runs straight</li>
        <li>Separating joints or blocks shifting out of alignment</li>
        <li>Soil, mulch, or water escaping through the face of the wall</li>
        <li>Water pooling behind the wall, or no visible drainage outlet at all</li>
        <li>Settlement or cracking in the surface above the wall</li>
      </ul>
      <p>A wall that has started to move rarely stops on its own, because the same forces that started it are still acting on it. Catching it early is usually the difference between a repair and a rebuild.</p>
""" + WHY_LOCAL + """
    </div>
  </section>
""",
        "faqs": [
            ("How tall can a retaining wall be?",
             "It depends on the wall system, the soil, and what's loading it from above. Past certain heights — or where a driveway, pool, or structure sits above the wall — engineering and permitting may be required, and requirements vary between Rowlett, Rockwall, and Heath. We'll flag it during the estimate."),
            ("Why do retaining walls fail?",
             "Overwhelmingly, water. Soil behind a wall gets heavier and pushes harder when saturated, so if there's no drainage path the wall is fighting a load it was never designed for. Inadequate base preparation and skipped soil reinforcement are the other two common causes."),
            ("Do I need drainage behind my wall?",
             "Yes. Clean aggregate backfill and drain pipe at the base are standard on our walls, not an upgrade. It's the single most important thing determining whether a wall is still straight years from now."),
            ("Can a retaining wall double as seating?",
             "Absolutely, and it's one of the better uses of a low wall. Seat-height walls around a patio or fire feature add permanent seating without furniture, and we detail the cap so it's comfortable to actually sit on."),
            ("Can you repair my existing retaining wall?",
             "Sometimes. It depends on why it's moving. If the base and drainage were done properly and the issue is localized, repair can make sense. If the wall is failing because drainage was never installed, rebuilding is usually the honest answer — we'll tell you which one you're looking at."),
        ],
        "related": [
            ("/concrete-patios-stamped-concrete", "Concrete & Stamped Patios", "Level the yard, then build the patio it deserves."),
            ("/concrete-driveways", "Concrete Driveways", "Driveway replacement built on a properly compacted base."),
            ("/projects", "Our Projects", "See finished hardscape work across the Metroplex."),
        ],
        "related_heading": "Related services",
    },
]
