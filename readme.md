# Countdown for Olympic Wintergames 2026

Im Rahmen der Lehrveranstaltung Infrastructure Engineering /MCCE 2024, Hochschule Burgenland.

Lektoren: Hahn/Pailer

## Erzeugung einer HTML-Seite
Die Seite soll die verbleibende Zeit bis zum Beginn der Olympischen Winterspiele darstellen.

# Webserver
Zur Bereitstellung wird ein Webserver benötigt. Ind diesem Fall wurde unter Phyton Flask eingesetzt.
Ein Dockerfile auf Basis python:3.11-slim wird diesen Job erledigen. Der Webserver wird auf Port 5000 des Dockers laufen.

# IBM Cloud
erst einmal die Cloud CLI (hier WSL) installieren:
```curl -fsSL https://clis.cloud.ibm.com/install/linux | sh```

Nach der Anmeldung auf der Webseite wird ein API-Key erstellt: https://cloud.ibm.com/iam/apikeys

nun kann man sich bei der CLI anmelden
```ibmcloud login --apikey <<api-key>>```

jetzt noch ein Secret:
ibmcloud iam api-key-create github-deploy-key --file ibm_api_key.json
dieses wird auf in den GitHubSecrets gespeichert:
- im Repository auf github.com
- auf "Settings" (⚙️) klicken
- Scrolle links runter zu "Secrets and variables"
- Wähle "Actions"
- Klicke auf "New repository secret"
- Inhalt von ibm_api_key.json kopieren und in GitHub Secret IBM_CLOUD_API_KEY einfügen.

Außerdem brauchen wir noch ein paar andere Secrets:
- IBM_CLOUD_REGION	eu-de
- IBM_CLOUD_RESOURCE_GROUP  wjg
- IBM_CLOUD_PROJECT os-cd

Dann das Container Registry-Plugin istallieren:
```ibmcloud plugin install container-registry```

und die richtige Region auswählen:
```ibmcloud cr region-set eu-central```

weil wir gerade dabei sind. Etwas später brauchen wir auch noch dieses Plugin:
```ibmcloud plugin install code-engine```

an dieser Stelle wurde es kompliziert. Um ein Cloud-Projekt anzulegen, muss man eine Kreditkarte hinterlegen. Leider hat IBM meine verweigert - die Daten ließen sich nicht speichern. Möglicher Weise liegt das an den anstehenden Kündigungen nachdem Raiffeisen und CardComplete die Zusammenarbeit beendet haben. Also musste ich mir eine Alternative suchen und bei bei render.com gelandet.

