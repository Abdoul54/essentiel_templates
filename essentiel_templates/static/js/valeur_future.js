var $ = function (id) {
  return document.getElementById(id);
};
var calculerVF = function (investissement, taux, duree) {
  var valeurFuture = investissement;
  for (var i = 1; i <= duree; i++) {
    valeurFuture += valeurFuture * taux / 100;
  }
  valeurFuture = valeurFuture.toFixed(2);
  return valeurFuture;
};
var traiterEntrees = function () {
  var investissement = parseFloat($("investissement").value);
  var taux = parseFloat($("taux_annuel").value);
  var duree = parseInt($("duree").value);
  var toutesValides = true;
  if (isNaN(investissement) || investissement <= 0 || investissement > 100000) {
    //$("investissement_erreur").firstChild.nodeValue = "doit être > 0 et <= 100000";
    $("investissement_erreur").innerHTML = "doit être > 0 et <= 100000";
    toutesValides = false;
  } else {
    //$("investissement_erreur").firstChild.nodeValue = "";
    $("investissement_erreur").innerHTML = "";
  }
  if (isNaN(taux) || taux <= 0 || taux > 15) {
    //$("taux_erreur").firstChild.nodeValue = "doit être > 0 et <= 15";
    $("taux_erreur").innerHTML = "doit être > 0 et <= 15";
    toutesValides = false;
  } else {
    //$("taux_erreur").firstChild.nodeValue = "";
    $("taux_erreur").innerHTML = "";
  }
  if (isNaN(duree) || duree <= 0 || duree > 50) {
    //$("duree_erreur").firstChild.nodeValue = "Doit être > 0 et <= 50";
    $("duree_erreur").innerHTML = "Doit être > 0 et <= 50";
    toutesValides = false;
  } else {
    //$("duree_erreur").firstChild.nodeValue = "";
    $("duree_erreur").innerHTML = "";
  }
  if (toutesValides) {
    $("valeur_future").value = calculerVF(investissement, taux, duree);
    //document.write(tableauInvestissement(investissement,taux,duree));
    $("tableau").innerHTML = tableauInvestissement(investissement, taux, duree);
  }
};
function tableauInvestissement(investissement, taux, duree) {
  var tab = "<caption>Tableau d'investissement</caption>" +
    "<tr><th>Année</th><th>Intérêts</th><th>ValeurFuture</th></tr>";
  var valeurFuture = investissement;
  for (var annee = 1; annee <= duree; annee++) {
    interet = valeurFuture * taux / 100;
    valeurFuture += interet;
    tab += "<tr><td>" + annee + "</td><td>" + interet.toFixed(2) +
      "</td><td>" + valeurFuture.toFixed(2) + "</td></tr>";
  }
  return tab;
}
window.onload = function () {
  $("calculer").onclick = traiterEntrees;
  $("investissement").focus();
};
