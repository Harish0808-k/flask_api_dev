### Using ORM (SQLALCHEMY) and Migrations to Flask APP

### Why Migrations are important?

### Schema Evolution:
As your application evolves, its database schema will need to change. You may need to:

1. Add new tables (e.g., to support new features).
2. Modify existing tables (e.g., adding new columns, renaming fields).
3. Remove obsolete tables or fields.

Migrations automate this process, helping to ensure that changes are applied smoothly without manually altering the database, which is error-prone.

### Version-Control:
Just like version control for code, migrations track changes to your database schema over time. Each migration is a record of a specific change, meaning you can:

1. Roll back changes if something goes wrong.
2. Recreate the database at any point by applying all migrations in sequence.
3. Maintain a history of all changes, making it easy to collaborate in teams where different developers work on different parts of the schema.

### Consistency Between Environments
When working in multiple environments (local, staging, production), migrations ensure that:

1. Your database schema is consistent across all environments.
2. You avoid issues where one environment has changes that are missing in another environment, which could lead to errors or broken functionality.
3. Migrations help synchronize database schemas when you deploy new features or move between environments.

### Ease of Collaboration
In a team of developers, different team members might work on different parts of the application, leading to multiple, simultaneous changes to the database schema. 

With migrations:

1. Each developer can make and commit their own schema changes (as migrations).
2. These migrations can be safely applied by other team members to ensure that everyone is using the same version of the schema.
3. Migrations help avoid conflicts when different developers make changes to the same part of the database.


### Migration Conflicts:
In Flask, database migrations are typically handled by `Flask-Migrate`, which is built on top of `Alembic` and `SQLAlchemy`. Migration conflicts in Flask can happen in a similar way as they do in Django, usually when multiple developers or branches make conflicting changes to the database schema.

### Migration Conflict in Flask
A migration conflict in Flask occurs when two or more migrations attempt to alter the same part of the database schema (e.g., adding or modifying the same column or table) but are generated separately. 

For example:

1. Developer A creates a migration to add a new column email to the User table and generates migration file `migration_002_add_email.py`.
2. Developer B creates a migration to rename the username column to user_name in the User table and generates migration file `migration_002_rename_username.py`.

When these two migrations are applied together, a conflict arises because both migrations have the same identifier (002) and modify the same table but in different ways.

### How to Resolve a Migration Conflict in Flask
Here's how you can identify and resolve migration conflicts in Flask using `Flask-Migrate`:

### 1. Identify the Conflict
When trying to apply migrations (flask db upgrade), Flask will throw an error if a conflict exists. The error message will show conflicting versions or operations in the migration files.

```yaml
sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) duplicate column name: email
```
### 2. Merge the Conflicting Migrations
Flask doesn't have a built-in `--merge` option like Django, so you need to handle the migration conflict manually. Follow these steps:

### 1. Inspect the Migrations: 
Look at the conflicting migration files in the migrations/versions/ folder. Identify which changes each migration is trying to apply.

### 2. Create a New Migration: 
Write a new migration script that combines the changes from both conflicting migrations. You might need to use Alembic commands to generate the appropriate schema alterations.

### 3. Update the Migration Script: 
If both migrations change the same part of the schema, you may need to manually modify the migration script. Below is an example of what a combined migration might look like:

```python
# migration_003_merge.py
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '003'
down_revision = ('002_add_email', '002_rename_username')  # Specify the conflicting migrations
branch_labels = None
depends_on = None

def upgrade():
    # Add the new email field
    op.add_column('user', sa.Column('email', sa.String(length=255), nullable=True))
    
    # Rename the username column to user_name
    op.alter_column('user', 'username', new_column_name='user_name')


def downgrade():
    # Reverse the changes in case of rollback
    op.alter_column('user', 'user_name', new_column_name='username')
    op.drop_column('user', 'email')
```

This script merges the changes from the conflicting migrations and ensures both changes are applied in a single migration.

### 4. Commit the New Migration
Once you've resolved the conflict and applied the new migration, commit the new migration file to your version control system (e.g., Git). Make sure other team members are aware of the conflict resolution so they can apply the new migration as well.


### Flask Migration commands

#### 1. Initialize or create the migration folder
```bash
flask --app filename db init
or 
flask db init
```
if your db is present in a file called main.py then use
```bash
flask --app main db init
```

#### 2. After making changes to models, generate a migrations file
```bash
flask --app main db migrate -m "description of migration file"
```

#### 3. Apply migrations to database
```bash
flask --app main db upgrade
```

#### 4. Rollback the migrations
```bash
flask --app main db downgrade
```
for specific revision
```bash
flask --app main db downgrade <revision>
```
#### 5. Display migrations history
```bash
flask --app main db history
```

#### 6. Show the current migration version applied to the database
```bash
flask --app main db current
```