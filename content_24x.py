R={
"storing-a-flat-pack-grill":("rust-rescue-carbon-steel","how-to-season-carbon-steel","Storage is half of grill care. The other half is what you do when spring comes around and the steel needs a little attention before its first fire of the year."),
"tailgate-grilling-playbook":("perfect-smash-burgers-griddle","griddle-cheesesteaks","Game-day food should be fast, hand-held and hard to mess up in a crowded lot. These two griddle favorites check every box and feed a hungry group quickly."),
"smoke-flavor-wood-chunks-charcoal":("two-zone-fire-explained","charcoal-101-lump-briquettes-chimney","Smoke works best on a well-built fire. Learn how to light charcoal cleanly and arrange it in two zones, and your wood chunks will do their job far better."),
"cast-iron-on-the-grill":("cast-iron-cornbread-and-chili-over-coals","carbon-steel-vs-cast-iron-vs-stainless","Ready to put that heavy pan to work? Start with a one-fire supper, then compare how cast iron stacks up against the other metals in your kitchen."),
"holiday-gift-guide-for-cooks":("gifts-under-30-for-grillers","housewarming-and-wedding-gifts-for-cooks","Still shopping? These guides cover small stocking stuffers and bigger milestone gifts, with ideas for every budget and every kind of cook on your list."),
"park-and-picnic-grilling":("make-ahead-cookout-sides","chicken-souvlaki-skewers","A park cook is mostly preparation. Make your sides at home and skewer your chicken the night before, and the afternoon becomes easy and relaxed."),
"griddle-cheesesteaks":("hibachi-fried-rice-griddle","griddle-diner-breakfast","Once your griddle plate is seasoned and hot, there is a whole menu waiting. These two cooks use the same flat steel for very different meals."),
"how-to-season-carbon-steel":("cleaning-carbon-steel-grill","rust-rescue-carbon-steel","Seasoning is the start of a lifelong routine. Learn the daily cleaning habits that protect your work, and the rescue plan for when things go wrong."),
"charcoal-101-lump-briquettes-chimney":("two-zone-fire-explained","smoke-flavor-wood-chunks-charcoal","With good coals lit, the next step is arranging them for control and adding a little wood for flavor. Both skills build directly on this one."),
"fathers-day-gift-guide":("reverse-sear-ribeye-charcoal","gifts-for-home-cooks","Pair the gift with a great first cook, or browse more ideas for the cooks in your life who are not dads but deserve something just as good."),
"griddle-quesadillas-and-breakfast-tacos":("griddle-diner-breakfast","grilled-shrimp-tacos","Love tortillas on the flat-top? Try a full diner-style breakfast on the griddle next, or move over to the grates for charred shrimp tacos."),
"marinades-that-work":("brining-wet-vs-dry","all-purpose-bbq-rubs","Marinades are only one way to season. Compare them with brines and rubs, then choose the method that suits each cut and your schedule."),
"science-of-searing":("reverse-sear-ribeye-charcoal","perfect-smash-burgers-griddle","Put the science to work: a thick reverse-seared ribeye over coals and a thin smash burger on a griddle show both ends of the searing spectrum."),
"make-ahead-cookout-sides":("backyard-cookout-game-plan","fourth-of-july-cookout-menu","Sides are the backbone of a cookout. Fit them into a full party plan, or build a holiday menu that keeps the cook relaxed."),
"housewarming-and-wedding-gifts-for-cooks":("holiday-gift-guide-for-cooks","gifts-for-home-cooks","More gift ideas for every occasion, with picks for every budget and cooking style."),
"brining-wet-vs-dry":("meat-temperature-guide","spatchcock-chicken-charcoal","Brined meat still needs careful cooking. Learn the target temperatures, then put a dry brine to work on a spatchcocked chicken."),
"fourth-of-july-cookout-menu":("cooking-for-a-crowd-one-grill","make-ahead-cookout-sides","Feeding a big holiday crowd on a single grill takes planning. These guides show you how."),
"carbon-steel-vs-cast-iron-vs-stainless":("how-to-season-carbon-steel","cast-iron-on-the-grill","Chose carbon steel? Learn to season it well. Love cast iron? Take it outside over the coals."),
"all-purpose-bbq-rubs":("pork-tenderloin-coffee-rub","homemade-bbq-sauces","Put a rub to work on pork tenderloin, then finish your barbecue with a homemade sauce."),
"compound-butters-and-chimichurri":("reverse-sear-ribeye-charcoal","grilled-salmon-skin-on","A finished sauce needs something great to land on. Try it on a seared steak or crisp-skinned salmon."),
}
for k,(a,b,t) in R.items():
    ta=[p[1] for p in PAGES if p[0]==a][0]; tb=[p[1] for p in PAGES if p[0]==b][0]
    X(k,f"## Where to go next\n\n{t}\n\n- [{ta}]({a}.html)\n- [{tb}]({b}.html)")
