-- 1. Les 10 joueurs ayant le plus d’or
SELECT username, montant_or
FROM Joueur
ORDER BY montant_or DESC
LIMIT 10;

-- 2. Le joueur ayant le plus de personnages de la même classe
SELECT j.username, p.classe, COUNT(*) AS total
FROM Joueur j
JOIN Personnage p ON j.id = p.joueur_id
GROUP BY j.username, p.classe
ORDER BY total DESC
LIMIT 1;

-- 3. La quête ayant la plus grosse récompense en or par niveau de difficulté
SELECT nom_quete, niveau_difficulte, or_recompense
FROM Quete
ORDER BY (or_recompense / niveau_difficulte) DESC
LIMIT 1;

-- 4. Le PNJ possédant l'inventaire avec la plus grande valeur en or cumulée
SELECT p.nom, SUM(o.valeur_or) AS valeur_totale
FROM PNJ p
JOIN Inventaire i ON p.id = i.pnj_id
JOIN Objet o ON i.objet_id = o.id
GROUP BY p.nom
ORDER BY valeur_totale DESC
LIMIT 1;

-- 5. Le type d'objet le plus souvent offert en récompense de quêtes de niveau 5
SELECT o.type_objet, COUNT(*) AS nombre
FROM Recompense r
JOIN Objet o ON r.objet_id = o.id
JOIN Quete q ON r.quete_id = q.id
WHERE q.niveau_difficulte = 5
GROUP BY o.type_objet
ORDER BY nombre DESC
LIMIT 1;

-- 6. Les monstres avec les meilleures récompenses en or cumulées selon leurs PV
SELECT m.nom, SUM(o.valeur_or) AS total_or, m.vie
FROM Monstre m
JOIN Butin b ON m.id = b.monstre_id
JOIN Objet o ON b.objet_id = o.id
GROUP BY m.nom, m.vie
ORDER BY total_or DESC;
