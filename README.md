🏛️ Introduction à la Clean Architecture
📜 Historique
La Clean Architecture a été formalisée par Robert C. Martin, aussi connu sous le nom Uncle Bob, dans les années 2010. Elle s’inscrit dans la continuité de plusieurs architectures logicielles comme :

Hexagonal Architecture (Ports & Adapters, d’Alistair Cockburn)
Onion Architecture (de Jeffrey Palermo)
Layered Architecture (traditionnelle à 3 ou 4 couches)
Toutes partagent une même vision : séparer les préoccupations métier des détails techniques.

🧰 But principal
L’objectif de la Clean Architecture est d’organiser son code de manière à ce qu’il soit :

Indépendant du framework (comme Django, FastAPI, Flask, etc.)
Indépendant de la base de données (PostgreSQL, MongoDB, etc.)
Indépendant de l’interface utilisateur (HTML, API, CLI…)
Autrement dit : l’architecture doit servir le métier, pas l’outil.

💡 Principe fondamental
Le cœur du système est le métier, et tout le reste (framework, UI, DB, etc.) gravite autour de ce cœur.

🔁 Règle de dépendance :
Le code des couches extérieures peut dépendre des couches intérieures, mais jamais l’inverse.

📐 Structure visuelle (vue en cercles)
+----------------------------+
|   Frameworks & Drivers    |  <- Django, ORM, etc.
+----------------------------+
|    Interface Adapters     |  <- Views, Serializers, Forms
+----------------------------+
|      Application/UseCases |  <- Logique métier, Orchestration
+----------------------------+
|         Domain Entities   |  <- Règles métiers, Objets purs
+----------------------------+
🧠 Pourquoi l'utiliser dans Django ?
Django est un excellent framework, mais il tend à tout concentrer dans l’app (models.py, views.py, etc.). Cela fonctionne pour de petits projets, mais :

La logique métier se mélange au code technique
Les tests deviennent plus complexes
Le code devient difficilement réutilisable
La Clean Architecture force à séparer clairement les rôles, ce qui améliore la lisibilité, l’évolutivité et la testabilité.


🏛️ Introduction à la Clean Architecture
📜 Historique
La Clean Architecture a été formalisée par Robert C. Martin (Uncle Bob) dans les années 2010. Elle s’inspire d’architectures antérieures comme :

Hexagonal Architecture (Ports & Adapters)
Onion Architecture
Layered Architecture
Toutes ces approches cherchent à séparer la logique métier du reste des préoccupations techniques (framework, base de données, interface…).

🧰 Objectif
L’objectif principal est de rendre le code :

Indépendant des frameworks (comme Django)
Indépendant des bases de données
Facilement testable
Durable et maintenable dans le temps
🔁 Règle de dépendance
Les dépendances doivent toujours pointer vers le centre du système, c’est-à-dire vers les règles métier.

Ainsi :

domain ne dépend de rien.
application dépend de domain.
interfaces et infrastructure dépendent de application ou domain.

Arborescence du projet

```plaintext
project/
├── domain/                # Contient les entités et règles métier
│   ├── __init__.py
│   ├── models.py          # Entités du domaine
│   └── services.py        # Logique métier pure
├── application/           # Contient les cas d'utilisation et la logique métier
│   ├── __init__.py
│   ├── use_cases.py       # Cas d'utilisation
│   └── services.py        # Services applicatifs
├── interfaces/            # Contient les adaptateurs et interfaces
│   ├── __init__.py
│   ├── views.py           # Vues Django
│   ├── serializers.py     # Sérializers pour la validation des données
│   └── urls.py            # Routes de l'application
├── infrastructure/        # Contient les implémentations techniques
│   ├── __init__.py
│   ├── repositories.py    # Accès aux données (ORM, etc.)
│   └── settings.py        # Configuration de l'application
└── manage.py              # Point d'entrée de l'application Django
