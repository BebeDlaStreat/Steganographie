# Steganographie
Faire passer un message dans une image

La stéganographie est un domaine où l'on cherche à dissimuler discrètement de l'information dans un media de couverture. Elle se distingue de la cryptographie qui cherche à rendre un contenu inintelligible à autre que qui-de-droit.

Ce programme vient modifier les 3 bits faibles du rgb des premiers pixels de l'image
Ce programme dépend de la librairie pillow, pour l'installer: `pip install pillow`
Si vous souhaitez tester, vous pouvez le faire avec l'image exemple.png

### Disclaimer:
- Il est possible que votre os compresse l'image à la sortie pour je ne sais quelle raison
- Ce n'est pas compatible avec des formats comme le jpeg car celui-ci compresse l'image
- J'ai crée ce programme pour le fun et pour m'entraîner donc je ne vais pas aller maintenir son fonctionnement ni vous avez si vous n'arrivez pas à lancer un script python
