# Arcane Référence - Implémentation GTM Web

L'objectif de ce projet est de donner un exemple d'implémentation "By the book" de GTM avec la méthodologie Arcane

##Contenu de ce projet

- Envoie d'un tag de pageView à chaque chargement d'une page HTML

- Tracking d'un funnel de conversion avec les étapes suivantes : 
    - Product Detail -> Page Produit
    - Add to Cart -> Evénement d'ajout au panier
    - Checkout step 1 -> Page Cart : confirmation du panier
    - Remove from Cart -> Evénement de retrait du panier
    - Checkout step 2 -> Page Checkout_1 -> Choix des options de livraison
    - Checkout step 3 -> Page Checkout_2 -> Choix des options de paiement
    - Purchase -> Confirmation de l'achat