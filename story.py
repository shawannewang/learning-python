bunnies = 50
deer = 50
hunters = 10
guns = 20
bullets_per_hunter = 100
licences = 5
average_bunnies_hunted = bunnies / hunters
total_bullets = hunters * bullets_per_hunter
total_prey = bunnies + deer
poachers = hunters - licences

print "There are", total_prey, "animals in the woods."
print "There are", hunters, "humans with guns."
print "Each person hunts", average_bunnies_hunted, "bunnies."
print "There are %d rounds in total" % total_bullets
print "%d come to hunting season illegally." % poachers