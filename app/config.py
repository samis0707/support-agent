import os
from dataclasses import dataclass, field


@dataclass
class Config:
    imap_host: str = os.environ.get("IMAP_HOST", "imaps.strato.de")
    imap_port: int = int(os.environ.get("IMAP_PORT", "993"))
    imap_user: str = os.environ.get("IMAP_USER", "")
    imap_pass: str = os.environ.get("IMAP_PASS", "")
    imap_mailbox: str = os.environ.get("IMAP_MAILBOX", "INBOX")

    smtp_host: str = os.environ.get("SMTP_HOST", "smtp.strato.de")
    smtp_port: int = int(os.environ.get("SMTP_PORT", "465"))
    smtp_user: str = os.environ.get("SMTP_USER", "")
    smtp_pass: str = os.environ.get("SMTP_PASS", "")
    from_name: str = os.environ.get("FROM_NAME", "Seeraeuber digital Support")
    from_address: str = os.environ.get("FROM_ADDRESS", "")

    escalation_email: str = os.environ.get("ESCALATION_EMAIL", "")
    escalation_subject_prefix: str = os.environ.get(
        "ESCALATION_SUBJECT_PREFIX", "[Eskalation Support]"
    )

    poll_interval_seconds: int = int(os.environ.get("POLL_INTERVAL_SECONDS", "300"))
    max_batch: int = int(os.environ.get("MAX_BATCH", "20"))
    state_db: str = os.environ.get("STATE_DB", "/data/support.db")
    knowledge_dir: str = os.environ.get(
        "KNOWLEDGE_DIR",
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "knowledge"),
    )

    mistral_api_key: str = os.environ.get("MISTRAL_API_KEY", "")
    mistral_model: str = os.environ.get("MISTRAL_MODEL", "mistral-small-latest")
    mistral_base_url: str = os.environ.get(
        "MISTRAL_BASE_URL", "https://api.mistral.ai/v1"
    )

    dry_run: bool = os.environ.get("DRY_RUN", "false").lower() in ("1", "true", "yes")
    max_body_chars: int = int(os.environ.get("MAX_BODY_CHARS", "8000"))

    escalation_keywords: tuple = (
        "abmahnung",
        "anwalt",
        "rechtsanwalt",
        "gericht",
        "beschwerde",
        "erstattung",
        "rueckbuchung",
        "rückbuchung",
        "mahnung",
        "rechnung",
        "invoice",
        "preis",
        "kosten",
        "mit mensch",
        "mit person",
        "mit jemandem sprechen",
        "durchstellen",
        "techniker",
        "vor ort",
        "datenschutz",
        "loeschen",
        "löschen",
        "dsgvo",
    )
    skip_senders: tuple = field(default=("mailer-daemon", "postmaster", "noreply", "no-reply", "donotreply"))

    @property
    def from_header(self) -> str:
        addr = self.from_address or self.imap_user
        return f"{self.from_name} <{addr}>"


def load_config() -> Config:
    return Config()
