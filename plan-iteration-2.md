# [Plan d'itération](#commentPlanifier "Comment planifier?")

## Étapes jalons

| Étape jalon                   | Date           |
| ------------------------------| -------------: |
| Début de l'itération          | 20/02/2024     |
| Présentation rapport final    | 04/04/2024     |
| Remise code fonctionnel       | 08/04/2024     |

## Objectifs clés

-   <a name="O1">O1:</a> Productions des corrélations par métriques et création de tendances de type de projet

-   <a name="O2">O2:</a> Création d'une pipeline d'analyse de code incluant Pharo sur GitHub Actions

-   <a name="O3">O3:</a> Création d'une pipeline d'analyse complète sur GitHub Actions avec des projets fixes

-   <a name="O4">O4:</a> Présenter rapport final et soumission de code

## Affectations d'éléments de travail

Les éléments de travail suivants seront abordés dans cette itération:

Le rang priorisation est de 3 moins élévé à 1 plus élévé.
La signification est comme suit:
-   1: Nécessaire pour combler les objectifs
-   2: Nécessaire pour améliorer la qualité des résultats
-   3: Nécessaire pour diminuer les risques mais ne bloque pas l'atteinte d'un objectif
 
| Nom / Description                                                                     | Priorité | [Taille estimée (points)] | Assigné à (nom)    | Documents de référence                                                                       |
| ------------------------------------------------------------------------------------- | -------: | ------------------------: | ------------------ | -------------------------------------------------------------------------------------------- |
| <a name="T1">T1:</a> Création de pipeline sur GitHub Actions                          | 1        | 4                         | Carlos             | https://github.com/pharo-open-documentation/pharo-wiki/blob/master/General/GithubActions.md  |
| <a name="T1.1">T1.1:</a> Intégration de l'analyse Pharo sur GitHub Actions            | 1        | 8                         | Carlos             | https://github.com/pharo-open-documentation/pharo-wiki/blob/master/General/GithubActions.md  |
| <a name="T1.2">T1.2:</a> Intégration de l'analyse complète sur GitHub Actions         | 1        | 4                         | Carlos             | https://github.com/pharo-open-documentation/pharo-wiki/blob/master/General/GithubActions.md  |
| <a name="T2">T2:</a> Production de corrélation par métriques                          | 1        | 4                         | Jouhaina           | SZZ Unleashed: An Open Implementation of the SZZ Algorithm                                   |
| <a name="T3">T4:</a> Utilisation des lignes de code pour corrélation avec métriques   | 1        | 4                         | Jouhaina           | GitHub fuhrmanator/SZZUnleashed pipeline.py                                                  |
| <a name="T3.1">T3.1:</a> Extraction des lignes de code bogué à partir de SZZ          | 1        | 4                         | Mohammed           | https://fuhrmanator.github.io/tuto-famix-ts/                                                 |
| <a name="T3.1">T3.1:</a> Extraction des lignes de code bogué à partir du modèle FAMIX | 1        | 4                         | Mohammed           | https://fuhrmanator.github.io/tuto-famix-ts/                                                 |
| <a name="T4">T5:</a> Compléter soumission: Rapport et Codeion                         | 1        | 2                         | (tous)             |                                                                                              |

## Problèmes

| Problème                                             | Statut   | Notes                                                                                                       |
| ---------------------------------------------------- | -------- | ----------------------------------------------------------------------------------------------------------- |
| L'équipe obtient une faible valeur de corrélation.   | En cours | L'équipe examine les données pour identifier et corriger les valeurs aberrantes et les données manquantes.  |

## Critères d'évaluation

- Pipeline exécute avec succès sur GitHub Actions.

- Pipeline retourne les artifacts de corrélation.

- L'analyse produit une corrélation répétable. 

- Les caractéristiques des projets analysés permettent la production de tendances pour poursuivre l'exploration des métriques qui influencenet la présence d'un bogue.

- L'expérience est répétable.

- Soumission de rapport final et du code final. 

## Évaluation

| Cible d'évaluation | Itération 01                                                                                                               |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| Date d'évaluation  | 04 avril 2024                                                                                                              |
| Participants       | **Coéquipiers** : Pinto, Carlos; Nasri, Jouhaina; Boutahar, Mohammed<br>**Chargé de laboratoire** : Fuhrman, Christopher   |
| État du projet     | Rouge, Orange, Jaune, Vert                                                                                                 |

###  Évaluation par rapport aux objectifs

-   [Objectif 1](#O1)
    > État d'avancement: ...

    > Activités réalisées: ...

    > Résultats obtenus: ...
    
    > Commentaires: ...

-   [Objectif 2](#O3)
    > État d'avancement: ...

    > Activités réalisées: ...

    > Résultats obtenus: ...
    
    > Commentaires: ...

-   [Objectif 3](#O3)
    > État d'avancement: ...

    > Activités réalisées: ...

    > Résultats obtenus: ...
    
    > Commentaires: ...

-   [Objectif 4](#O4)
    > État d'avancement: ...

    > Activités réalisées: ...

    > Résultats obtenus: ...
    
    > Commentaires: ...

### Éléments de travail: prévus vs réalisés

- ...

### Évaluation par rapport aux résultats selon les critères d'évaluation 

- ...

## Autres préoccupations et écarts

*Aucune pour l'instant*

---

<a name="commentPlanifier">Comment planifier une itération selon le
    processus unifié :</a>
    <https://docs.google.com/a/etsmtl.net/document/d/1xeCCdR4-sTznTPaSKYIl4l_bQi-gE5stPWSA5VArRlY/edit?usp=sharing>

<a name="commentEstimer">Comment estimer la taille :</a>
    <https://docs.google.com/a/etsmtl.net/document/d/1bDy0chpWQbK9bZ82zdsBweuAgNYni3T2k79xihr6CuU/edit?usp=sharing>


#[Retour au Readme](../README.md)