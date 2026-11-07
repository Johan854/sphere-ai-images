# Sphère AI – personnages

Images de personnages pour les sphères vocales ESPHome (Spotpear / Xiaozhi Ball v2, config RealDeco).

## Personnages

| Personnage | Aperçu |
|---|---|
| **MaxDresseur** : Max, soigneur au Parc des Géants, et Pico, son bébé tricératops (personnages originaux) | ![Max](images/MaxDresseur/apercu.png) |

## Structure

```
images/<Personnage>/240x240/
  idle.png  listening.png  thinking.png  replying.png
  error.png  timer_finished.png  mute.png  loading.png
```

Chaque image fait 240×240 px, fond transparent. L'écran est rond : garder l'essentiel dans le cercle central.

## Utilisation dans la config ESPHome

```yaml
substitutions:
  image_repo: "Johan854/sphere-ai-images"   # ou "RealDeco/xiaozhi-esphome" pour les personnages d'origine
  imagemodel: "MaxDresseur"
```

Les URL des images utilisent `https://github.com/${image_repo}/raw/main/images/${imagemodel}/240x240/<état>.png`.

## Ajouter un personnage

Créer `images/<NomDuPersonnage>/240x240/` avec les 8 PNG ci-dessus, puis changer `imagemodel`. Les sources vectorielles de Max sont dans `sources/MaxDresseur/` (`generer.py` régénère les SVG).
