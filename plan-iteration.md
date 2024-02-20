# [Plan d'itération](#commentPlanifier "Comment planifier?")

## Étapes jalons

| Étape jalon                   | Date           |
| ------------------------------| -------------: |
| Début de l'itération          | 23/01/2024     |
| Intégration de pipeline       | 10/02/2024     |
| Démonstration et livraison    | 19/02/2024     |
| Fin de l'itération            | 19/02/2024     |

## Objectifs clés

-   <a name="O1">O1:</a> Création d'une pipeline de fôrage de projet GitHub jusqu'à l'identification des fichiers bogués utilisant SZZ

-   <a name="O2">O2:</a> Création d'une pipeline d'analyse avec Pharo à partir des fichiers bogués

-   <a name="O3">O3:</a> Production des métriques (LOC, CC) des fichiers bogués et non-bogués

-   <a name="O4">O4:</a> Production de corrélation des métriques avec la présence de bogue

-   <a name="O5">O5:</a> Présenter une démonstration technique de la pipeline.

## Affectations d'éléments de travail

Les éléments de travail suivants seront abordés dans cette itération:

Le rang priorisation est de 3 moins élévé à 1 plus élévé.
La signification est comme suit:
-   1: Nécessaire pour combler les objectifs
-   2: Nécessaire pour améliorer la qualité des résultats
-   3: Nécessaire pour diminuer les risques mais ne bloque pas l'atteinte d'un objectif
 
| Nom / Description                                                         | Priorité | [Taille estimée (points)](#commentEstimer "Comment estimer?") | Assigné à (nom)    | Documents de référence                                      |
| ------------------------------------------------------------------------- | -------: | ------------------------------------------------------------: | ------------------ | ----------------------------------------------------------- |
| <a name="T1">T1:</a> Fôrage automatique de projets GitHub                 | 1        | 4                                                             | Carlos             | GitHub fuhrmanator/SZZUnleashed                             |
| <a name="T2">T2:</a> Détection de fichier bogué avec SZZ                  | 1        | 4                                                             | Carlos             | SZZ Unleashed: An Open Implementation of the SZZ Algorithm  |
| <a name="T3">T3:</a> Génération de modèle ts2famix sur projets            | 1        | 1                                                             | Carlos             | https://fuhrmanator.github.io/tuto-famix-ts/                |
| <a name="T4.1">T4.1:</a> Génération de LOC de classes                     | 1        | 4                                                             | Mohammed           | https://mooc.pharo.org/                                     |
| <a name="T4.2">T4.2:</a> Génération de CC de classes                      | 1        | 8                                                             | Mohammed           | https://mooc.pharo.org/                                     |
| <a name="T5.1">T5.1:</a> Calcul de corrélation de fichier bogué avec LOC  | 2        | 4                                                             | Jouhaina           | Aucun, connaissances en python                                   |
| <a name="T5.2">T5.2:</a> Calcul de corrélation de fichier bogué avec CC   | 2        | 4                                                             | Jouhaina           | Aucun, connaissances en python                                   |
| <a name="T6">T6:</a> Création de pipeline de analyse X projets            | 3        | 8                                                             | Carlos             | GitHub fuhrmanator/SZZUnleashed pipeline.py                 |
| <a name="T7">T7:</a> Préparation de démonstration                         | 3        | 1                                                             | (tous)             | GitHub fuhrmanator/SZZUnleashed README.md                   |

## Problèmes

| Problème                                                                                                  | Statut   | Notes                                                                         |
| --------------------------------------------------------------------------------------------------------- | -------- | ----------------------------------------------------------------------------- |
| <del>L'équipe rencontrait de robustess avec la pipeline.py fournit par fuhrmanator/SZZUnleashed</del>     | Réglé    | L'équipe a réécrit certains scripts et a modularisé avec une meta-pipeline.py |
| <del>Le fôrage des projets GitHub prends beaucoup de temps</del>                                          | Réglé    | L'équipe a modularisé le fôrage ainsi améliorant la robustesse                |
| <del> L'équipe ne comprends pas la source d'analyse faite par SZZ pour déterminer la source d'un fichier bogué  | Réglé <del>| L'équipe lit les références du projet GitHub                                  |
| L'équipe obtient une faible valeur de corrélation.  | En cours | L'équipe examine les données pour identifier et corriger les valeurs aberrantes et les données manquantes.                                  |
|   
                                                                                     

## Critères d'évaluation

- Extraction de LOC réussite pour les classes et les méthodes des projet GitHub identifiés.

- Extraction de CC réussite pour les méthodes des projet GitHub identifiés.

- L'analyse statistique produit une probabilité de présence de bogue en relation avec les métriques extraites. 

- Démonstration de la pipeline, par phase, et reception favorable de la présentation. 

## Évaluation

| Cible d'évaluation | Itération 01                                                                                                               |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| Date d'évaluation  | 19 février 2024                                                                                                            |
| Participants       | **Coéquipiers** : Pinto, Carlos; Nasri, Jouhaina; Boutahar, Mohammed<br>**Chargé de laboratoire** : Fuhrman, Christopher   |
| État du projet     | Vert                                                                                                  |

###  Évaluation par rapport aux objectifs

-   [Objectif 1](#O1)
    > État d'avancement: Complet 

    > Activités réalisées: La configuration de l'environnement, le forâge des projets GitHub, et l'implémentation de l'algorithme SZZ pour identifier les fichiers bogués.

    > Résultats obtenus: Nous avons réussi à identifier plusieurs fichiers potentiellement bogués à travers les différents projets GitHub analysés.
    
    > Commentaires: Déterminer les classes et méthodes à l'aide de l'analyse des lignes de code, fournits par SZZ, qui ont introduit les bogues pour une meilleure corrélation.


-   [Objectif 2](#O3)
    > État d'avancement: Complet 

    > Activités réalisées: L'intégration de Pharo au cœur de notre pipeline d'analyse, l'automatisation de l'utilisation des modèles et de l'exécution du code Pharo directement dans la pipeline.

    > Résultats obtenus: L'utilisation de Pharo dans notre pipeline a amélioré notre capacité à analyser.

-   [Objectif 3](#O3)
    > État d'avancement: Complet

    > Activités réalisées: L'utilisation de Pharo a permis d'automatiser l'extraction des métriques : le nombre de Lignes de Code (LOC) pour les classes et les méthodes, et la Complexité Cyclomatique (CC) pour les méthodes sous forme de fichiers csv.

    > Résultats obtenus : Grâce à cette méthodologie, nous avons réussi à identifier et à extraire efficacement les métriques associées tant aux fichiers bogués qu'aux fichiers non-bogués des divers projets GitHub analysés. 
    
    > Commentaires: Extraire d'autres caractéristiques du projet pour les étudier contre la corrélation des métriques et déterminer si elles ont un impact sur la corrélation.

-   [Objectif 4](#O4)
    > État d'avancement: En cours

    > Activités réalisées: nous avons employé un code Python conçu pour relier les fichiers de métriques générés par Pharo et calculer la corrélation entre ces métriques et la présence de bogues dans les fichiers.

    > Résultats obtenus: Les résultats de l'analyse de corrélation ont révélé une faible valeur de corrélation entre les métriques de LOC et de CC et la présence de bogues dans les fichiers.
    
    > Commentaires: Séparer la corrélation par LOC et par CC. De plus, avec les caractéristiques de l'objectif 3, il

-   [Objectif 5](#O4)
    > État d'avancement: Complet

    > Activités réalisées: nous avons présenté le projet et fait une démontration de la pipeline.

    > Résultats obtenus: LA démonstration a été appréciée et les explications ont été comprises par l'audience.

### Éléments de travail: prévus vs réalisés

- Durant cette itération, notre équipe a réalisé avec succès toutes les tâches prévues, conformément à nos objectifs stratégiques et livrables attendus.

### Évaluation par rapport aux résultats selon les critères d'évaluation 

- Nous avons identifié un taux d'AUC inférieur aux attentes pour nos analyses de corrélation, ce qui était en deçà de notre objectif de performance prédéterminé. Cette situation nous demande une réévaluation approfondie de nos méthodes d'analyse et de nos jeux de données.

## Autres préoccupations et écarts

*Aucune pour l'instant*

---

<a name="commentPlanifier">Comment planifier une itération selon le
    processus unifié :</a>
    <https://docs.google.com/a/etsmtl.net/document/d/1xeCCdR4-sTznTPaSKYIl4l_bQi-gE5stPWSA5VArRlY/edit?usp=sharing>

<a name="commentEstimer">Comment estimer la taille :</a>
    <https://docs.google.com/a/etsmtl.net/document/d/1bDy0chpWQbK9bZ82zdsBweuAgNYni3T2k79xihr6CuU/edit?usp=sharing>


#[Retour au Readme](../README.md)