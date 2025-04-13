# sully_engine/codex.py
# 📚 Sully's Symbolic Codex (Knowledge Book)

from datetime import datetime

class SullyCodex:
    """
    Stores named symbolic knowledge entries and enables semantic lookup.
    """

    def __init__(self):
        self.entries = {}

    def record(self, topic, data):
        """
        Records new symbolic knowledge under a topic name.

        Args:
            topic (str): The symbolic topic or name.
            data (dict): Associated symbolic data or metadata.
        """
        self.entries[topic.lower()] = {
            **data,
            "timestamp": datetime.now().isoformat()
        }

    def search(self, phrase, case_sensitive=False):
        """
        Searches the codex for entries matching a phrase.

        Args:
            phrase (str): The search keyword.
            case_sensitive (bool): Match case when scanning.

        Returns:
            dict: Matching entries (topic -> data).
        """
        results = {}
        phrase_check = phrase if case_sensitive else phrase.lower()

        for topic, data in self.entries.items():
            topic_check = topic if case_sensitive else topic.lower()
            values = [str(v) for v in data.values()]

            if phrase_check in topic_check or any(phrase_check in v.lower() for v in values):
                results[topic] = data

        return results

    def get(self, topic):
        """
        Gets a codex entry by topic name.
        """
        return self.entries.get(topic.lower(), {"message": "🔍 No codex entry found."})

    def list_topics(self):
        """
        Returns a list of all topic names currently in the codex.
        """
        return list(self.entries.keys())

    def export(self):
        """
        Returns all codex entries (for backup, JSON export, or UI rendering).
        """
        return self.entries