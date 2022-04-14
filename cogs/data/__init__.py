import os
import sqlite3
from typing import Union


class Data:
    data_dir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(data_dir, "db.sqlite3")
    conn = sqlite3.connect(filename)
    c = conn.cursor()
    datetime_format = "%Y-%m-%d %H:%M:%S"

@classmethod
def create_tables(cls):
      cls.c.execute(
            """
            CREATE TABLE IF NOT EXISTS "webhooks" (
                "channel_id"	INTEGER NOT NULL,
                "webhook_url"	TEXT
            )
            """
        )

    # Webhook Data
@classmethod
def create_new_webhook_data(cls, channel, webhook_url):
        cls.c.execute(
            "INSERT INTO webhooks VALUES (:channel_id, :webhook_url)",
            {"channel_id": channel.id, "webhook_url": webhook_url},
        )
        cls.conn.commit()
        print(f"Created webhook entry for channel with ID {channel.id}")

@classmethod
def webhook_entry_exists(cls, channel) -> Union[str, bool]:
        cls.c.execute(
            "SELECT webhook_url FROM webhooks WHERE channel_id = :channel_id",
            {"channel_id": channel.id},
        )
        webhook_data = cls.c.fetchone()

        if webhook_data:
            return webhook_data[0]

        return False

