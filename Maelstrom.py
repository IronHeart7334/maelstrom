from maelstrom_classes import *
import random

do_MHC = True
debug = False

weathers = (
    Weather("Lightning", 40.0, "Flashes of light can be seen in the distance..."),
    Weather("Lightning", 50.0, "Thunder rings not far away..."),
    Weather("Lightning", 60.0, "The sky rains down its fire upon the field..."),
    
    Weather("Wind", 40.0, "A gentle breeze whips through..."),
    Weather("Wind", 50.0, "The strong winds blow mightily..."),
    Weather("Wind", 60.0, "A twister rips up the land..."),
    
    Weather("Hail", 2.5, "A light snow was falling..."),
    Weather("Hail", 5, "Hail clatters along the ground..."),
    Weather("Hail", 7.5, "The field is battered by hail..."),
    
    Weather("Rain", 2.5, "A light rain falls..."),
    Weather("Rain", 5, "A brisk shower is forecast..."),
    Weather("Rain", 7.5, "A deluge of water pours forth from the sky...")
    )


lightning = Element("Lightning", "Wind")
wind = Element("Wind", "Hail")
hail = Element("Hail", "Rain")
rain = Element("Rain", "Lightning")
stone = Element ("Stone", None)

# use these in specials
no_MHC = (0, -1)
no_MHC_mult = (1, 1)
no_eff = (0, 0, 0)
act_ene = ("enemy", "act")

boom = Attack("BOOM!", 9999, no_MHC, no_MHC_mult, ("enemy", "all"), no_eff, 7)

LAct = Attack("Shock Pulse", 1.75, no_MHC, no_MHC_mult, act_ene, no_eff, 5)
RAct = Attack("Water Pulse", 1.75, no_MHC, no_MHC_mult, act_ene, no_eff, 5)
HAct = Attack("Icicle Pulse", 1.75, no_MHC, no_MHC_mult, act_ene, no_eff, 5)
WAct = Attack("Vacuum Pulse", 1.75, no_MHC, no_MHC_mult, act_ene, no_eff, 5)
SAct = Attack("Rock Slide", 1.75, no_MHC, no_MHC_mult, act_ene, no_eff, 5)

LAll = Attack("Shock Wave", 0.67, no_MHC, no_MHC_mult, ("enemy", "all"), no_eff, 5)
RAll = Attack("Tidal Wave", 0.67, no_MHC, no_MHC_mult, ("enemy", "all"), no_eff, 5)
HAll = Attack("Avalanche", 0.67, no_MHC, no_MHC_mult, ("enemy", "all"), no_eff, 5)
WAll = Attack("Tempest", 0.67, no_MHC, no_MHC_mult, ("enemy", "all"), no_eff, 5)

LAny = Attack("Thunderbolt", 1.25, no_MHC, no_MHC_mult, ("enemy", "any"), no_eff, 5)
RAny = Attack("Water bolt", 1.25, no_MHC, no_MHC_mult, ("enemy", "any"), no_eff, 5)
HAny = Attack("Frost bolt", 1.25, no_MHC, no_MHC_mult, ("enemy", "any"), no_eff, 5)
WAny = Attack("Wind bolt", 1.25, no_MHC, no_MHC_mult, ("enemy", "any"), no_eff, 5)

characters["Alexandre"] = ((0, 1, 1), lightning, LAct)
characters["Rene"] = ((0, -1, 1), rain, RAct)
characters["Ian"] = ((0, -1, -1), hail, HAct)
characters["Viktor"] = ((0, 1, -1), wind, WAct)

characters["Isaac"] = ((-1, 0, -3), lightning, LAll)
characters["Barry"] = ((1, -1, 1), rain, RAll)
characters["Nicole"] = ((1, 2, 2), hail, HAll)
characters["Colin"] = ((0, -1, 0), wind, WAll)

characters["Adrian"] = ((1, -2, 1), lightning, LAny)
characters["Omar"] = ((-1, 0, -2), rain, RAny)
characters["Richard"] = ((-1, -3, -3), hail, HAny)
characters["Tobias"] = ((0, -2, -1), wind, WAny)

enemies["TEST"] = ((0, 0, 0), stone, SAct)
enemies["MAX"] = ((5, 0, 0), stone, SAct)
enemies["MIN"] = ((-5, 0, 0), stone, SAct)

enemies["Lightning Entity"] = ((-3, 3, 3), lightning, LAct)
enemies["Rain Entity"] = ((3, -3, 3), rain, RAct)
enemies["Hail Entity"] = ((3, -3, -3), hail, HAct)
enemies["Wind Entity"] = ((-3, 3, -3), wind, WAct)

if __name__ == "__main__":
    """
    should_load = choose("Do you want to load from a save file?", ("Yes", "No"))
    
    if should_load == "Yes":
        m = Savefile("player_data.txt")
        player = m.upload_team()
    else:
        player = Team("Test team", (("Alexandre", 1), ("Rene", 1), ("Ian", 1), ("Viktor", 1)), False, False)
    """
    player = Team("Test team", (("Alexandre", 1), ("Rene", 1), ("Ian", 1), ("Viktor", 1)), False, False)
    
    """    
    # temporary
    t = Tavern("The salty spitoon")
    c = Contract(None)
    cc = Contract("Alexandre")
    t.recruit(player, (c, cc))
    """
    #r1 = Battle("Origin Beaches", "Start here", ("Encounter! Rain Entity", "Quick! Knock its hit points down to zero and escape!"), ("Congradulations!", "Perhaps an ally will help you in your quest."), 1, weathers[9])
    #r1.load_team(Team(" ", (("Rain Entity", 1)), True, True))
    
    test_fight = Battle("Test", "A quick test fight, just to try things out", None, ("Well, glad that's over", "But wait! There's more!"), 1, [weathers[0], weathers[3], weathers[6], weathers[9]])
    test_fight.load_team(Team("Test", (("TEST", 1)), True, True))
    
    test2 = Battle("Test2", "What's this? Another test?", ("Hello?", "Is this thing on?"), None, 4, weathers[2])
    test2.load_team(Team("Test2", (("Lightning Entity", 1), ("Rain Entity", 1), ("Hail Entity", 1), ("Wind Entity", 1)), False, True))
    
    test3 = Battle("Test3", "Arrows fly by like streaks of lightning", None, None, 3, None)
    test3.load_team(Team("Test3", (("Adrian", 1), ("Omar", 1), ("Richard", 5)), False, True))

    test_area = Area("Test", "Testing, 1, 2, 3", (test_fight, test2, test3))
    test_area.display_data(player)
    
    
    h1 = Battle("Forest Clearing", "A fresh coating of snow covers all the trees", None, None, 1, weathers[6])
    h1.load_team(Team(" ", (("Hail Entity", 1)), True, True))

    hail_village = Area("The Hail Village", "?", (h1))
    #hail_village.display_data(player)
    
    #m.update(test_team)