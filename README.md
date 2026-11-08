# Seeräuber digital – Support-Agent (Mistral Agents SDK)

Support-Agent für das Seeräuber-Blättle (Böckingen/Klingenberg). Beantwortet Support-E-Mails automatisch über den **Gmail-Connector** und eskaliert **ausschließlich per E-Mail** an einen Menschen.

## Was der Agent tut
1. Sucht unbearbeitete Support-Mails im verbundenen Postfach (`gmail_search_threads`, Label `bearbeitet`/`eskaliert`).
2. Beantwortet klar beantwortbare Fragen auf Deutsch aus seinem Wissen (Termine, Kalender-Abo, Login, Terminpflege, Freigabe, PDF/CSV, app.linqr.de/hilfe).
3. Eskaliert per E-Mail an `ESCALATION_EMAIL`: Originalverlauf mit `[Eskalation]`-Betreff weiterleiten + Empfangsbestätigung an den Absender.

## Voraussetzungen
- Gmail-Connector in Mistral Studio verbunden (Connectors → gmail). Die Strato-Support-Adresse leitet per Auto-Weiterleitung an diese Gmail-Adresse weiter.
- Workspace-Secret `ESCALATION_EMAIL` (Zieladresse für Eskalationen an Menschen).

## Deployment (Mistral-managed)
1. Projekt pushen: `git push origin <branch>`.
2. Deployen: `uv run --env-file .env agents deploy` (baut das gepushte Commit aus diesem Repo, Agent-Name `seeraeuber-support`) — oder über MCP `deploy_workflow_deployment` mit `github_url`, `revision`, `deployment_name=seeraeuber-support`, `hardened=true` (der Gmail-Connector läuft on-behalf-of).
3. Secret binden: `ESCALATION_EMAIL` als Workspace-Secret an die Deployment binden.
4. Danach erscheint der Agent im Agenten-Verzeichnis (`agents list` bzw. Studio/Vibe) und ist per `agents chat seeraeuber-support` bzw. `Agent.load_from(agent_name="seeraeuber-support")` erreichbar.

## Lokal testen
```bash
uv add mistralai-agents
export MISTRAL_API_KEY=<key>
export ESCALATION_EMAIL=<menschliche support adresse>
uv run agents chat
```

## Hinweis
Antworten und Eskalationen gehen über die verbundene Gmail-Adresse. Sollen sie von der Strato-Adresse selbst ausgehen, braucht es statt des Gmail-Connectors einen IMAP/SMTP-Dienst (z. B. `imap_backfill_service`-Muster) als MCP-Server.
