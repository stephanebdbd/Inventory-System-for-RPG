--TOPGOLD
SELECT username, montant_or
FROM Joueur
ORDER BY montant_or DESC
LIMIT 10;

--RANK1
SELECT j.username, p.classe, COUNT(*) AS total
FROM Joueur j
JOIN Personnage p ON j.id = p.joueur_id
GROUP BY j.username, p.classe
ORDER BY total DESC
LIMIT 1;

--TOPQUEST
SELECT nom_quete, niveau_difficulte, or_recompense
FROM Quete
ORDER BY (or_recompense / niveau_difficulte) DESC
LIMIT 1;

--TOPPNJ
SELECT p.nom, SUM(o.valeur_or) AS valeur_totale
FROM PNJ p
JOIN Inventaire i ON p.id = i.pnj_id
JOIN Objet o ON i.objet_id = o.id
GROUP BY p.nom
ORDER BY valeur_totale DESC
LIMIT 1;

--TOPITEM
SELECT o.type_objet, COUNT(*) AS nombre
FROM Recompense r
JOIN Objet o ON r.objet_id = o.id
JOIN Quete q ON r.quete_id = q.id
WHERE q.niveau_difficulte = 5
GROUP BY o.type_objet
ORDER BY nombre DESC
LIMIT 1;

--TOPMONSTER
SELECT m.nom, SUM(o.valeur_or) AS total_or, m.vie
FROM Monstre m
JOIN Butin b ON m.id = b.monstre_id
JOIN Objet o ON b.objet_id = o.id
GROUP BY m.nom, m.vie
ORDER BY total_or DESC;
