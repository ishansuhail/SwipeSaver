
class SwipeSaverRouter:
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Make sure the app's models get migrated to the specific database."""
        if app_label == 'populate_db':
            return db == 'PostgresDB'  # Migrations for the 'populate_db' app will go to 'PostgresDB'
        return db == 'default'  # Other apps will migrate to the 'default' database