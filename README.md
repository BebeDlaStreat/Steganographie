# Steganographie
Faire passer un message dans une image

La stéganographie est un domaine où l'on cherche à dissimuler discrètement de l'information dans un media de couverture. Elle se distingue de la cryptographie qui cherche à rendre un contenu inintelligible à autre que qui-de-droit.

Ce programme vient modifier les 3 bits faibles du rgb des premiers pixels de l'image
Ce n'est pas compatible avec des formats comme le jpeg car celui-ci compresse l'image
Ce programme dépend de la librairie pillow, pour l'installer: `pip install pillow`
