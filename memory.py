# memory.py

# sully_engine/memory.py
# 🧠 Sully's Searchable Symbolic Memory System

from datetime import datetime

class SullySearchMemory:
    def __init__(self):
        self.storage = []

    def store_query(self, query, result):
        """
        Stores a symbolic query and its result in memory, with a timestamp.
        """
        self.storage.append({
            "query": query,
            "result": result,
            "timestamp": datetime.now().isoformat()
        })

    def search(self, keyword, case_sensitive=False, limit=None):
        """
        Searches memory for entries containing the given keyword.

        Args:
            keyword (str): Term to search within queries.
            case_sensitive (bool): Whether to respect case during match.
            limit (int or None): Max number of results to return.

        Returns:
            dict: Indexed matches from memory.
        """
        matches = {}
        for i, entry in enumerate(self.storage):
            haystack = entry["query"] if case_sensitive else entry["query"].lower()
            needle = keyword if case_sensitive else keyword.lower()

            if needle in haystack:
                matches[i] = entry
                if limit and len(matches) >= limit:
                    break

        return matches

    def export_memory(self):
        """
        Returns the entire memory as a list of entries (for JSON export).
        """
        return self.storage

    def clear_memory(self):
        """
        Clears all stored symbolic queries and results.
        """
        self.storage = []
        return "[Memory cleared]"
